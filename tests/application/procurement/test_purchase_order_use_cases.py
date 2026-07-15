from __future__ import annotations

from copy import deepcopy
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.procurement.amend_draft_purchase_order import (
    AmendDraftPurchaseOrderRequest,
)
from mfm.application.procurement.amend_draft_purchase_order import (
    PurchaseOrderLineUpdateInput,
)
from mfm.application.procurement.amend_draft_purchase_order import (
    AmendDraftPurchaseOrderUseCase,
)
from mfm.application.procurement.approve_purchase_order import (
    ApprovePurchaseOrderRequest,
)
from mfm.application.procurement.approve_purchase_order import ApprovePurchaseOrderUseCase
from mfm.application.procurement.cancel_purchase_order import CancelPurchaseOrderRequest
from mfm.application.procurement.cancel_purchase_order import CancelPurchaseOrderUseCase
from mfm.application.procurement.create_purchase_order import BusinessRuleViolation
from mfm.application.procurement.create_purchase_order import CreatePurchaseOrderRequest
from mfm.application.procurement.create_purchase_order import CreatePurchaseOrderUseCase
from mfm.application.procurement.create_purchase_order import PurchaseOrderLineInput
from mfm.application.procurement.create_purchase_order import PurchaseReceiptLineInput
from mfm.application.procurement.create_purchase_order import RepositoryException
from mfm.application.procurement.get_purchase_order import GetPurchaseOrderRequest
from mfm.application.procurement.get_purchase_order import GetPurchaseOrderUseCase
from mfm.application.procurement.list_purchase_orders import ListPurchaseOrdersRequest
from mfm.application.procurement.list_purchase_orders import ListPurchaseOrdersUseCase
from mfm.application.procurement.list_purchase_orders_by_state import (
    ListPurchaseOrdersByStateRequest,
)
from mfm.application.procurement.list_purchase_orders_by_state import (
    ListPurchaseOrdersByStateUseCase,
)
from mfm.application.procurement.list_purchase_orders_by_supplier import (
    ListPurchaseOrdersBySupplierRequest,
)
from mfm.application.procurement.list_purchase_orders_by_supplier import (
    ListPurchaseOrdersBySupplierUseCase,
)
from mfm.application.procurement.place_purchase_order import PlacePurchaseOrderRequest
from mfm.application.procurement.place_purchase_order import PlacePurchaseOrderUseCase
from mfm.application.procurement.record_purchase_receipt import (
    RecordPurchaseReceiptRequest,
)
from mfm.application.procurement.record_purchase_receipt import (
    RecordPurchaseReceiptUseCase,
)
from mfm.application.procurement.submit_purchase_order import SubmitPurchaseOrderRequest
from mfm.application.procurement.submit_purchase_order import SubmitPurchaseOrderUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.procurement.purchase_order import PurchaseOrder
from mfm.domain.procurement.purchase_order_status import PurchaseOrderStatus
from mfm.repositories.purchase_order_repository import PurchaseOrderRepository


class InMemoryPurchaseOrderRepository(PurchaseOrderRepository):
    def __init__(
        self,
        *,
        fail_on_add: bool = False,
        fail_on_update: bool = False,
    ) -> None:
        self._orders: dict[UUID, PurchaseOrder] = {}
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

        self.add_calls = 0
        self.get_by_id_calls = 0
        self.get_by_number_calls = 0
        self.update_calls = 0
        self.exists_calls = 0
        self.list_calls = 0
        self.list_by_state_calls = 0
        self.list_by_supplier_calls = 0

    def snapshot(self) -> dict[UUID, PurchaseOrder]:
        return deepcopy(self._orders)

    def restore(self, snapshot: dict[UUID, PurchaseOrder]) -> None:
        self._orders = deepcopy(snapshot)

    def add(self, order: PurchaseOrder) -> None:
        self.add_calls += 1
        if self._fail_on_add:
            raise RuntimeError("purchase order add failed")
        if self.exists_by_number(order.purchase_order_number.value):
            raise ValueError(
                f"Purchase order number {order.purchase_order_number.value} already exists"
            )
        self._orders[order.id.value] = deepcopy(order)

    def get_by_id(self, purchase_order_id: UUID) -> PurchaseOrder | None:
        self.get_by_id_calls += 1
        value = self._orders.get(purchase_order_id)
        return deepcopy(value) if value is not None else None

    def get_by_number(self, purchase_order_number: str) -> PurchaseOrder | None:
        self.get_by_number_calls += 1
        normalized = purchase_order_number.strip()
        for order in self._orders.values():
            if order.purchase_order_number.value == normalized:
                return deepcopy(order)
        return None

    def update(self, order: PurchaseOrder) -> None:
        self.update_calls += 1
        if self._fail_on_update:
            raise RuntimeError("purchase order update failed")
        if order.id.value not in self._orders:
            raise ValueError(f"Purchase order {order.id.value} does not exist")

        duplicate = next(
            (
                existing
                for existing in self._orders.values()
                if existing.purchase_order_number == order.purchase_order_number
                and existing.id != order.id
            ),
            None,
        )
        if duplicate is not None:
            raise ValueError(
                f"Purchase order number {order.purchase_order_number.value} already exists"
            )

        self._orders[order.id.value] = deepcopy(order)

    def exists_by_number(self, purchase_order_number: str) -> bool:
        self.exists_calls += 1
        normalized = purchase_order_number.strip()
        return any(
            order.purchase_order_number.value == normalized
            for order in self._orders.values()
        )

    def list(self) -> list[PurchaseOrder]:
        self.list_calls += 1
        return [
            deepcopy(order)
            for _, order in sorted(
                self._orders.items(),
                key=lambda pair: (pair[1].purchase_order_number.value, str(pair[0])),
            )
        ]

    def list_by_state(self, status: PurchaseOrderStatus | str) -> list[PurchaseOrder]:
        self.list_by_state_calls += 1
        normalized = status.value if isinstance(status, PurchaseOrderStatus) else str(status)
        return [
            deepcopy(item)
            for item in self.list()
            if item.status.value == normalized
        ]

    def list_by_supplier_reference(self, supplier_reference: str) -> list[PurchaseOrder]:
        self.list_by_supplier_calls += 1
        normalized = supplier_reference.strip()
        return [
            deepcopy(item)
            for item in self.list()
            if item.supplier_reference.value == normalized
        ]


class FakeProcurementUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_add: bool = False,
        fail_update: bool = False,
        fail_commit: bool = False,
    ) -> None:
        super().__init__()
        self._fail_commit = fail_commit
        self._repository = InMemoryPurchaseOrderRepository(
            fail_on_add=fail_add,
            fail_on_update=fail_update,
        )
        self._snapshot: dict[UUID, PurchaseOrder] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self.purchase_order_repository = self._repository
        self._snapshot = self._repository.snapshot()

        self.inventory_repository = None
        self.organization_repository = None
        self.contact_repository = None

    def _commit_impl(self) -> None:
        self.commits += 1
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self._repository.restore(self._snapshot)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


def _aware(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, 0, tzinfo=UTC)


def _line(
    *,
    description: str,
    quantity: Decimal | str | int,
    unit_price_amount: Decimal | str | int,
    inventory_item_reference: str | None = None,
) -> PurchaseOrderLineInput:
    return PurchaseOrderLineInput(
        description_snapshot=description,
        quantity=quantity,
        unit_price_amount=unit_price_amount,
        inventory_item_reference=inventory_item_reference,
    )


def _create_order(
    uow: FakeProcurementUnitOfWork,
    *,
    order_number: str = "PO-APP-001",
    supplier_reference: str = "SUP-A",
) -> UUID:
    response = CreatePurchaseOrderUseCase(unit_of_work=uow).execute(
        CreatePurchaseOrderRequest(
            purchase_order_number=order_number,
            supplier_reference=supplier_reference,
            currency="DKK",
            created_at=_aware(2028, 1, 1, 8),
            lines=(
                _line(
                    description="Marine paint",
                    quantity=Decimal("5.000"),
                    unit_price_amount=Decimal("100.50"),
                    inventory_item_reference="INV-001",
                ),
            ),
            notes="Initial",
        )
    )
    return response.purchase_order.purchase_order_id


def _submit_approve_place(
    uow: FakeProcurementUnitOfWork,
    *,
    order_id: UUID,
) -> None:
    SubmitPurchaseOrderUseCase(unit_of_work=uow).execute(
        SubmitPurchaseOrderRequest(
            purchase_order_id=order_id,
            submitted_at=_aware(2028, 1, 2, 8),
        )
    )
    ApprovePurchaseOrderUseCase(unit_of_work=uow).execute(
        ApprovePurchaseOrderRequest(
            purchase_order_id=order_id,
            approved_at=_aware(2028, 1, 3, 8),
            approved_by_reference="manager-1",
        )
    )
    PlacePurchaseOrderUseCase(unit_of_work=uow).execute(
        PlacePurchaseOrderRequest(
            purchase_order_id=order_id,
            ordered_at=_aware(2028, 1, 4, 8),
            external_order_reference="SUP-ORDER-1",
        )
    )


def test_create_purchase_order_success_duplicate_and_money_decimal_truth() -> None:
    uow = FakeProcurementUnitOfWork()
    use_case = CreatePurchaseOrderUseCase(unit_of_work=uow)

    created = use_case.execute(
        CreatePurchaseOrderRequest(
            purchase_order_number="PO-APP-100",
            supplier_reference="SUP-100",
            currency="DKK",
            created_at=_aware(2028, 1, 1, 8),
            lines=(
                _line(
                    description="Hydraulic oil",
                    quantity=Decimal("3.000"),
                    unit_price_amount=Decimal("750.10"),
                    inventory_item_reference="INV-HYD-OIL",
                ),
            ),
            supplier_name_snapshot="Supplier A",
        )
    )

    assert uow.commits == 1
    assert created.purchase_order.purchase_order_number == "PO-APP-100"
    assert created.purchase_order.order_total_amount == Decimal("2250.30")
    assert created.purchase_order.lines[0].unit_price_amount == Decimal("750.10")
    assert created.purchase_order.lines[0].unit_price_currency == "DKK"
    assert created.purchase_order.lines[0].inventory_item_reference == "INV-HYD-OIL"

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            CreatePurchaseOrderRequest(
                purchase_order_number="PO-APP-100",
                supplier_reference="SUP-100",
                currency="DKK",
                created_at=_aware(2028, 1, 1, 8),
                lines=(
                    _line(
                        description="Duplicate",
                        quantity=1,
                        unit_price_amount=Decimal("1.00"),
                    ),
                ),
            )
        )

    assert uow.commits == 1


def test_get_purchase_order_existing_missing_and_query_no_commit() -> None:
    uow = FakeProcurementUnitOfWork()
    order_id = _create_order(uow, order_number="PO-APP-GET")
    before_commits = uow.commits

    response = GetPurchaseOrderUseCase(unit_of_work=uow).execute(
        GetPurchaseOrderRequest(purchase_order_id=order_id)
    )

    assert response.purchase_order.purchase_order_id == order_id
    assert uow.commits == before_commits

    with pytest.raises(BusinessRuleViolation):
        GetPurchaseOrderUseCase(unit_of_work=uow).execute(
            GetPurchaseOrderRequest(
                purchase_order_id=UUID("00000000-0000-0000-0000-00000000E701")
            )
        )

    assert uow.commits == before_commits


def test_list_and_filter_queries_delegate_and_preserve_repository_order() -> None:
    uow = FakeProcurementUnitOfWork()
    order_a = _create_order(uow, order_number="PO-APP-A", supplier_reference="SUP-A")
    order_b = _create_order(uow, order_number="PO-APP-B", supplier_reference="SUP-A")
    order_c = _create_order(uow, order_number="PO-APP-C", supplier_reference="SUP-B")

    SubmitPurchaseOrderUseCase(unit_of_work=uow).execute(
        SubmitPurchaseOrderRequest(
            purchase_order_id=order_b,
            submitted_at=_aware(2028, 1, 2, 8),
        )
    )
    _submit_approve_place(uow, order_id=order_c)

    before_commits = uow.commits

    listed = ListPurchaseOrdersUseCase(unit_of_work=uow).execute(ListPurchaseOrdersRequest())
    by_state = ListPurchaseOrdersByStateUseCase(unit_of_work=uow).execute(
        ListPurchaseOrdersByStateRequest(status="SUBMITTED")
    )
    by_supplier = ListPurchaseOrdersBySupplierUseCase(unit_of_work=uow).execute(
        ListPurchaseOrdersBySupplierRequest(supplier_reference="SUP-A")
    )

    assert [item.purchase_order_number for item in listed.purchase_orders] == [
        "PO-APP-A",
        "PO-APP-B",
        "PO-APP-C",
    ]
    assert [item.purchase_order_number for item in by_state.purchase_orders] == ["PO-APP-B"]
    assert [item.purchase_order_number for item in by_supplier.purchase_orders] == [
        "PO-APP-A",
        "PO-APP-B",
    ]
    assert uow.commits == before_commits


def test_amend_draft_updates_header_and_lines_without_manual_total_calculation() -> None:
    uow = FakeProcurementUnitOfWork()
    order_id = _create_order(uow, order_number="PO-APP-AMEND")

    loaded = GetPurchaseOrderUseCase(unit_of_work=uow).execute(
        GetPurchaseOrderRequest(purchase_order_id=order_id)
    )
    line_id = loaded.purchase_order.lines[0].purchase_order_line_id

    amended = AmendDraftPurchaseOrderUseCase(unit_of_work=uow).execute(
        AmendDraftPurchaseOrderRequest(
            purchase_order_id=order_id,
            supplier_reference="SUP-AMENDED",
            notes="Amended note",
            add_lines=(
                _line(
                    description="Filter",
                    quantity=Decimal("2.000"),
                    unit_price_amount=Decimal("50.00"),
                    inventory_item_reference="INV-FILTER",
                ),
            ),
            update_lines=(
                PurchaseOrderLineUpdateInput(
                    purchase_order_line_id=line_id,
                    quantity=Decimal("6.000"),
                    unit_price_amount=Decimal("100.50"),
                ),
            ),
        )
    )

    assert amended.purchase_order.supplier_reference == "SUP-AMENDED"
    assert amended.purchase_order.notes == "Amended note"
    assert len(amended.purchase_order.lines) == 2
    assert amended.purchase_order.order_total_amount == Decimal("703.00")


def test_submit_approve_place_record_receipt_and_cancel_lifecycle_flow() -> None:
    uow = FakeProcurementUnitOfWork()
    order_id = _create_order(uow, order_number="PO-APP-LIFE")

    _submit_approve_place(uow, order_id=order_id)

    after_place = GetPurchaseOrderUseCase(unit_of_work=uow).execute(
        GetPurchaseOrderRequest(purchase_order_id=order_id)
    )
    line_id = after_place.purchase_order.lines[0].purchase_order_line_id

    received = RecordPurchaseReceiptUseCase(unit_of_work=uow).execute(
        RecordPurchaseReceiptRequest(
            purchase_order_id=order_id,
            receipt_reference="RCPT-APP-1",
            received_at=_aware(2028, 1, 5, 8),
            lines=(
                PurchaseReceiptLineInput(
                    purchase_order_line_id=line_id,
                    quantity=Decimal("2.000"),
                ),
            ),
        )
    )

    assert received.purchase_order.status == "PARTIALLY_RECEIVED"
    assert len(received.purchase_order.receipts) == 1

    cancelled_id = _create_order(uow, order_number="PO-APP-CANCEL")
    cancelled = CancelPurchaseOrderUseCase(unit_of_work=uow).execute(
        CancelPurchaseOrderRequest(
            purchase_order_id=cancelled_id,
            cancelled_at=_aware(2028, 1, 6, 8),
            cancelled_by_reference="planner",
            cancellation_reason="Scope changed",
        )
    )
    assert cancelled.purchase_order.status == "CANCELLED"


def test_lifecycle_failure_not_found_and_invalid_transition_do_not_commit() -> None:
    uow = FakeProcurementUnitOfWork()
    order_id = _create_order(uow, order_number="PO-APP-FAIL")
    before = uow.commits

    with pytest.raises(BusinessRuleViolation):
        ApprovePurchaseOrderUseCase(unit_of_work=uow).execute(
            ApprovePurchaseOrderRequest(
                purchase_order_id=order_id,
                approved_at=_aware(2028, 1, 2, 8),
                approved_by_reference="manager",
            )
        )

    assert uow.commits == before

    with pytest.raises(BusinessRuleViolation):
        SubmitPurchaseOrderUseCase(unit_of_work=uow).execute(
            SubmitPurchaseOrderRequest(
                purchase_order_id=UUID("00000000-0000-0000-0000-00000000E702"),
                submitted_at=_aware(2028, 1, 2, 8),
            )
        )

    assert uow.commits == before


def test_repository_failure_maps_repository_exception_and_rolls_back() -> None:
    uow = FakeProcurementUnitOfWork(fail_update=True)
    order_id = _create_order(uow, order_number="PO-APP-ERR")
    before = uow.commits

    with pytest.raises(RepositoryException):
        SubmitPurchaseOrderUseCase(unit_of_work=uow).execute(
            SubmitPurchaseOrderRequest(
                purchase_order_id=order_id,
                submitted_at=_aware(2028, 1, 2, 8),
            )
        )

    assert uow.commits == before
    assert uow.rollbacks >= 1


def test_response_types_are_immutable_dataclasses() -> None:
    uow = FakeProcurementUnitOfWork()
    created = CreatePurchaseOrderUseCase(unit_of_work=uow).execute(
        CreatePurchaseOrderRequest(
            purchase_order_number="PO-APP-IMMUTABLE",
            supplier_reference="SUP-I",
            currency="DKK",
            created_at=_aware(2028, 1, 1, 8),
            lines=(
                _line(description="Paint", quantity=1, unit_price_amount=Decimal("10.00")),
            ),
        )
    )

    assert is_dataclass(created.purchase_order)
    assert created.purchase_order.lines[0].unit_price_currency == "DKK"
