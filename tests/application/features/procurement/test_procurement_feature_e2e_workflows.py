from __future__ import annotations

import ast
from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import mfm.database.models.purchase_order_line_model  # noqa: F401
import mfm.database.models.purchase_order_model  # noqa: F401
import mfm.database.models.purchase_receipt_line_model  # noqa: F401
import mfm.database.models.purchase_receipt_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.features.procurement.amend_draft_purchase_order_feature import (
    AmendDraftPurchaseOrderFeature,
)
from mfm.application.features.procurement.amend_draft_purchase_order_feature import (
    AmendDraftPurchaseOrderRequest,
)
from mfm.application.features.procurement.amend_draft_purchase_order_feature import (
    PurchaseOrderLineUpdateInput,
)
from mfm.application.features.procurement.approve_purchase_order_feature import (
    ApprovePurchaseOrderFeature,
)
from mfm.application.features.procurement.approve_purchase_order_feature import (
    ApprovePurchaseOrderRequest,
)
from mfm.application.features.procurement.cancel_purchase_order_feature import (
    CancelPurchaseOrderFeature,
)
from mfm.application.features.procurement.cancel_purchase_order_feature import (
    CancelPurchaseOrderRequest,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    CreatePurchaseOrderFeature,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    CreatePurchaseOrderRequest,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    PurchaseOrderLineInput,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    PurchaseReceiptLineInput,
)
from mfm.application.features.procurement.get_purchase_order_feature import (
    GetPurchaseOrderFeature,
)
from mfm.application.features.procurement.get_purchase_order_feature import (
    GetPurchaseOrderRequest,
)
from mfm.application.features.procurement.list_purchase_orders_by_state_feature import (
    ListPurchaseOrdersByStateFeature,
)
from mfm.application.features.procurement.list_purchase_orders_by_state_feature import (
    ListPurchaseOrdersByStateRequest,
)
from mfm.application.features.procurement.list_purchase_orders_by_supplier_feature import (
    ListPurchaseOrdersBySupplierFeature,
)
from mfm.application.features.procurement.list_purchase_orders_by_supplier_feature import (
    ListPurchaseOrdersBySupplierRequest,
)
from mfm.application.features.procurement.list_purchase_orders_feature import (
    ListPurchaseOrdersFeature,
)
from mfm.application.features.procurement.list_purchase_orders_feature import (
    ListPurchaseOrdersRequest,
)
from mfm.application.features.procurement.place_purchase_order_feature import (
    PlacePurchaseOrderFeature,
)
from mfm.application.features.procurement.place_purchase_order_feature import (
    PlacePurchaseOrderRequest,
)
from mfm.application.features.procurement.record_purchase_receipt_feature import (
    RecordPurchaseReceiptFeature,
)
from mfm.application.features.procurement.record_purchase_receipt_feature import (
    RecordPurchaseReceiptRequest,
)
from mfm.application.features.procurement.submit_purchase_order_feature import (
    SubmitPurchaseOrderFeature,
)
from mfm.application.features.procurement.submit_purchase_order_feature import (
    SubmitPurchaseOrderRequest,
)
from mfm.application.procurement.amend_draft_purchase_order import (
    AmendDraftPurchaseOrderUseCase,
)
from mfm.application.procurement.approve_purchase_order import ApprovePurchaseOrderUseCase
from mfm.application.procurement.cancel_purchase_order import CancelPurchaseOrderUseCase
from mfm.application.procurement.create_purchase_order import CreatePurchaseOrderUseCase
from mfm.application.procurement.get_purchase_order import GetPurchaseOrderUseCase
from mfm.application.procurement.list_purchase_orders import ListPurchaseOrdersUseCase
from mfm.application.procurement.list_purchase_orders_by_state import (
    ListPurchaseOrdersByStateUseCase,
)
from mfm.application.procurement.list_purchase_orders_by_supplier import (
    ListPurchaseOrdersBySupplierUseCase,
)
from mfm.application.procurement.place_purchase_order import PlacePurchaseOrderUseCase
from mfm.application.procurement.record_purchase_receipt import (
    RecordPurchaseReceiptUseCase,
)
from mfm.application.procurement.submit_purchase_order import SubmitPurchaseOrderUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.base_model import BaseModel
from mfm.infrastructure.persistence.sqlite.sqlite_purchase_order_repository import (
    SQLitePurchaseOrderRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteProcurementApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.purchase_order_repository = SQLitePurchaseOrderRepository(
            self._persistence_uow
        )

        self.inventory_repository = None
        self.organization_repository = None
        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

    def _commit_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.commit()

    def _rollback_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        return None


@dataclass(frozen=True, slots=True)
class ProcurementFeatureStack:
    create: CreatePurchaseOrderFeature
    amend: AmendDraftPurchaseOrderFeature
    submit: SubmitPurchaseOrderFeature
    approve: ApprovePurchaseOrderFeature
    place: PlacePurchaseOrderFeature
    receive: RecordPurchaseReceiptFeature
    cancel: CancelPurchaseOrderFeature
    get: GetPurchaseOrderFeature
    list_all: ListPurchaseOrdersFeature
    list_by_state: ListPurchaseOrdersByStateFeature
    list_by_supplier: ListPurchaseOrdersBySupplierFeature


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "procurement_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_feature_stack(session: Session) -> ProcurementFeatureStack:
    uow = SQLiteProcurementApplicationUnitOfWork(session)

    return ProcurementFeatureStack(
        create=CreatePurchaseOrderFeature(service=CreatePurchaseOrderUseCase(unit_of_work=uow)),
        amend=AmendDraftPurchaseOrderFeature(
            service=AmendDraftPurchaseOrderUseCase(unit_of_work=uow)
        ),
        submit=SubmitPurchaseOrderFeature(service=SubmitPurchaseOrderUseCase(unit_of_work=uow)),
        approve=ApprovePurchaseOrderFeature(
            service=ApprovePurchaseOrderUseCase(unit_of_work=uow)
        ),
        place=PlacePurchaseOrderFeature(service=PlacePurchaseOrderUseCase(unit_of_work=uow)),
        receive=RecordPurchaseReceiptFeature(
            service=RecordPurchaseReceiptUseCase(unit_of_work=uow)
        ),
        cancel=CancelPurchaseOrderFeature(service=CancelPurchaseOrderUseCase(unit_of_work=uow)),
        get=GetPurchaseOrderFeature(service=GetPurchaseOrderUseCase(unit_of_work=uow)),
        list_all=ListPurchaseOrdersFeature(service=ListPurchaseOrdersUseCase(unit_of_work=uow)),
        list_by_state=ListPurchaseOrdersByStateFeature(
            service=ListPurchaseOrdersByStateUseCase(unit_of_work=uow)
        ),
        list_by_supplier=ListPurchaseOrdersBySupplierFeature(
            service=ListPurchaseOrdersBySupplierUseCase(unit_of_work=uow)
        ),
    )


def _aware_utc(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


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
    stack: ProcurementFeatureStack,
    *,
    order_number: str,
    supplier_reference: str,
    lines: tuple[PurchaseOrderLineInput, ...],
) -> UUID:
    created = stack.create.execute(
        CreatePurchaseOrderRequest(
            purchase_order_number=order_number,
            supplier_reference=supplier_reference,
            currency="DKK",
            created_at=_aware_utc(2030, 1, 1, 8),
            lines=lines,
        )
    )
    return created.purchase_order.purchase_order_id


def test_e2e_workflow_1_create_retrieve_and_list(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)

        order_id = _create_order(
            stack,
            order_number="PO-E2E-001",
            supplier_reference="SUP-OPAQUE-001",
            lines=(
                _line(
                    description="Marine paint",
                    quantity=Decimal("2.000"),
                    unit_price_amount=Decimal("100.10"),
                    inventory_item_reference="INV-OPAQUE-001",
                ),
            ),
        )

        loaded = stack.get.execute(GetPurchaseOrderRequest(purchase_order_id=order_id))
        listed = stack.list_all.execute(ListPurchaseOrdersRequest())

        assert loaded.purchase_order.status == "DRAFT"
        assert loaded.purchase_order.purchase_order_number == "PO-E2E-001"
        assert loaded.purchase_order.supplier_reference == "SUP-OPAQUE-001"
        assert loaded.purchase_order.lines[0].inventory_item_reference == "INV-OPAQUE-001"
        assert loaded.purchase_order.order_total_amount == Decimal("200.20")
        assert [item.purchase_order_number for item in listed.purchase_orders] == [
            "PO-E2E-001"
        ]
    finally:
        session.close()


def test_e2e_workflow_2_order_line_and_money_truth(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)

        order_id = _create_order(
            stack,
            order_number="PO-E2E-MONEY",
            supplier_reference="SUP-OPAQUE-MONEY",
            lines=(
                _line(
                    description="Primer",
                    quantity=Decimal("2.000"),
                    unit_price_amount=Decimal("100.10"),
                    inventory_item_reference="INV-OPAQUE-A",
                ),
            ),
        )

        created = stack.get.execute(GetPurchaseOrderRequest(purchase_order_id=order_id))
        line_id = created.purchase_order.lines[0].purchase_order_line_id

        amended = stack.amend.execute(
            AmendDraftPurchaseOrderRequest(
                purchase_order_id=order_id,
                add_lines=(
                    _line(
                        description="Filter",
                        quantity=Decimal("3.000"),
                        unit_price_amount=Decimal("40.05"),
                        inventory_item_reference="INV-OPAQUE-B",
                    ),
                ),
                update_lines=(
                    PurchaseOrderLineUpdateInput(
                        purchase_order_line_id=line_id,
                        quantity=Decimal("3.000"),
                    ),
                ),
            )
        )

        loaded = stack.get.execute(GetPurchaseOrderRequest(purchase_order_id=order_id))

        assert amended.purchase_order.order_total_amount == Decimal("420.45")
        assert loaded.purchase_order.order_total_amount == Decimal("420.45")
        assert [line.line_total_amount for line in loaded.purchase_order.lines] == [
            Decimal("300.30"),
            Decimal("120.15"),
        ]
        assert loaded.purchase_order.lines[0].inventory_item_reference == "INV-OPAQUE-A"
        assert loaded.purchase_order.lines[1].inventory_item_reference == "INV-OPAQUE-B"
    finally:
        session.close()


def test_e2e_workflow_3_approved_lifecycle_journey(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)

        order_id = _create_order(
            stack,
            order_number="PO-E2E-LIFE",
            supplier_reference="SUP-LIFE",
            lines=(
                _line(
                    description="Hydraulic oil",
                    quantity=Decimal("5.000"),
                    unit_price_amount=Decimal("10.00"),
                ),
            ),
        )

        draft = stack.get.execute(GetPurchaseOrderRequest(purchase_order_id=order_id))
        assert draft.purchase_order.status == "DRAFT"

        submitted = stack.submit.execute(
            SubmitPurchaseOrderRequest(
                purchase_order_id=order_id,
                submitted_at=_aware_utc(2030, 1, 2, 8),
            )
        )
        assert submitted.purchase_order.status == "SUBMITTED"

        approved = stack.approve.execute(
            ApprovePurchaseOrderRequest(
                purchase_order_id=order_id,
                approved_at=_aware_utc(2030, 1, 2, 9),
                approved_by_reference="approver-1",
            )
        )
        assert approved.purchase_order.status == "APPROVED"
        assert approved.purchase_order.approved_by_reference == "approver-1"

        placed = stack.place.execute(
            PlacePurchaseOrderRequest(
                purchase_order_id=order_id,
                ordered_at=_aware_utc(2030, 1, 2, 10),
                external_order_reference="SUP-ORDER-001",
            )
        )
        assert placed.purchase_order.status == "ORDERED"

        line_id = placed.purchase_order.lines[0].purchase_order_line_id
        partial = stack.receive.execute(
            RecordPurchaseReceiptRequest(
                purchase_order_id=order_id,
                receipt_reference="RCPT-001",
                received_at=_aware_utc(2030, 1, 3, 8),
                lines=(
                    PurchaseReceiptLineInput(
                        purchase_order_line_id=line_id,
                        quantity=Decimal("2.000"),
                    ),
                ),
            )
        )
        assert partial.purchase_order.status == "PARTIALLY_RECEIVED"

        complete = stack.receive.execute(
            RecordPurchaseReceiptRequest(
                purchase_order_id=order_id,
                receipt_reference="RCPT-002",
                received_at=_aware_utc(2030, 1, 4, 8),
                lines=(
                    PurchaseReceiptLineInput(
                        purchase_order_line_id=line_id,
                        quantity=Decimal("3.000"),
                    ),
                ),
            )
        )
        assert complete.purchase_order.status == "RECEIVED"

        loaded = stack.get.execute(GetPurchaseOrderRequest(purchase_order_id=order_id))
        assert loaded.purchase_order.status == "RECEIVED"
        assert [receipt.receipt_reference for receipt in loaded.purchase_order.receipts] == [
            "RCPT-001",
            "RCPT-002",
        ]
    finally:
        session.close()


def test_e2e_workflow_4_forbidden_transition_truth(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)

        order_id = _create_order(
            stack,
            order_number="PO-E2E-FORBIDDEN",
            supplier_reference="SUP-FORBIDDEN",
            lines=(
                _line(
                    description="Forbidden",
                    quantity=Decimal("1.000"),
                    unit_price_amount=Decimal("1.00"),
                ),
            ),
        )

        with pytest.raises(BusinessRuleViolation):
            stack.approve.execute(
                ApprovePurchaseOrderRequest(
                    purchase_order_id=order_id,
                    approved_at=_aware_utc(2030, 2, 1, 8),
                    approved_by_reference="approver-1",
                )
            )

        loaded = stack.get.execute(GetPurchaseOrderRequest(purchase_order_id=order_id))
        assert loaded.purchase_order.status == "DRAFT"
        assert loaded.purchase_order.approved_at is None
        assert loaded.purchase_order.receipts == ()
    finally:
        session.close()


def test_e2e_workflow_5_query_truth_supplier_boundary_and_ordering(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)

        id_a = _create_order(
            stack,
            order_number="PO-E2E-Q-A",
            supplier_reference="ORG:SUP-A",
            lines=(_line(description="A", quantity=1, unit_price_amount="1.00"),),
        )
        id_b = _create_order(
            stack,
            order_number="PO-E2E-Q-B",
            supplier_reference="ORG:SUP-A",
            lines=(_line(description="B", quantity=1, unit_price_amount="2.00"),),
        )
        id_c = _create_order(
            stack,
            order_number="PO-E2E-Q-C",
            supplier_reference="CONTACT:SUP-B",
            lines=(_line(description="C", quantity=1, unit_price_amount="3.00"),),
        )

        stack.submit.execute(
            SubmitPurchaseOrderRequest(
                purchase_order_id=id_b,
                submitted_at=_aware_utc(2030, 3, 1, 8),
            )
        )
        stack.submit.execute(
            SubmitPurchaseOrderRequest(
                purchase_order_id=id_c,
                submitted_at=_aware_utc(2030, 3, 1, 9),
            )
        )
        stack.approve.execute(
            ApprovePurchaseOrderRequest(
                purchase_order_id=id_c,
                approved_at=_aware_utc(2030, 3, 1, 10),
                approved_by_reference="approver-2",
            )
        )

        listed = stack.list_all.execute(ListPurchaseOrdersRequest())
        by_state = stack.list_by_state.execute(
            ListPurchaseOrdersByStateRequest(status="SUBMITTED")
        )
        by_supplier = stack.list_by_supplier.execute(
            ListPurchaseOrdersBySupplierRequest(supplier_reference="ORG:SUP-A")
        )

        assert [item.purchase_order_number for item in listed.purchase_orders] == [
            "PO-E2E-Q-A",
            "PO-E2E-Q-B",
            "PO-E2E-Q-C",
        ]
        assert [item.purchase_order_number for item in by_state.purchase_orders] == [
            "PO-E2E-Q-B"
        ]
        assert [item.purchase_order_number for item in by_supplier.purchase_orders] == [
            "PO-E2E-Q-A",
            "PO-E2E-Q-B",
        ]
        assert [item.supplier_reference for item in by_supplier.purchase_orders] == [
            "ORG:SUP-A",
            "ORG:SUP-A",
        ]
    finally:
        session.close()


def test_e2e_workflow_6_historical_procurement_truth(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)

        order_id = _create_order(
            stack,
            order_number="PO-E2E-HISTORY",
            supplier_reference="SUP-HISTORY",
            lines=(
                _line(
                    description="History",
                    quantity=Decimal("4.000"),
                    unit_price_amount=Decimal("12.50"),
                    inventory_item_reference="INV-HISTORY-1",
                ),
            ),
        )

        stack.submit.execute(
            SubmitPurchaseOrderRequest(
                purchase_order_id=order_id,
                submitted_at=_aware_utc(2030, 4, 1, 8),
            )
        )
        stack.approve.execute(
            ApprovePurchaseOrderRequest(
                purchase_order_id=order_id,
                approved_at=_aware_utc(2030, 4, 1, 9),
                approved_by_reference="approver-history",
            )
        )
        placed = stack.place.execute(
            PlacePurchaseOrderRequest(
                purchase_order_id=order_id,
                ordered_at=_aware_utc(2030, 4, 1, 10),
                external_order_reference="SUP-HISTORY-ORDER",
            )
        )

        line_id = placed.purchase_order.lines[0].purchase_order_line_id
        stack.receive.execute(
            RecordPurchaseReceiptRequest(
                purchase_order_id=order_id,
                receipt_reference="RCPT-H-1",
                received_at=_aware_utc(2030, 4, 2, 8),
                lines=(
                    PurchaseReceiptLineInput(
                        purchase_order_line_id=line_id,
                        quantity=Decimal("1.500"),
                    ),
                ),
            )
        )
        final = stack.receive.execute(
            RecordPurchaseReceiptRequest(
                purchase_order_id=order_id,
                receipt_reference="RCPT-H-2",
                received_at=_aware_utc(2030, 4, 3, 8),
                lines=(
                    PurchaseReceiptLineInput(
                        purchase_order_line_id=line_id,
                        quantity=Decimal("2.500"),
                    ),
                ),
            )
        )

        assert final.purchase_order.status == "RECEIVED"
        assert [item.receipt_reference for item in final.purchase_order.receipts] == [
            "RCPT-H-1",
            "RCPT-H-2",
        ]
        assert [item.lines[0].quantity for item in final.purchase_order.receipts] == [
            Decimal("1.500"),
            Decimal("2.500"),
        ]
    finally:
        session.close()


def test_e2e_workflow_7_persistence_reopen_and_transaction_truth(sqlite_session_factory) -> None:
    order_id: UUID | None = None

    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)

        order_id = _create_order(
            stack,
            order_number="PO-E2E-REOPEN",
            supplier_reference="SUP-REOPEN",
            lines=(
                _line(
                    description="Reopen",
                    quantity=Decimal("2.000"),
                    unit_price_amount=Decimal("50.25"),
                    inventory_item_reference="INV-REOPEN-001",
                ),
            ),
        )

        stack.submit.execute(
            SubmitPurchaseOrderRequest(
                purchase_order_id=order_id,
                submitted_at=_aware_utc(2030, 5, 1, 8),
            )
        )
        stack.approve.execute(
            ApprovePurchaseOrderRequest(
                purchase_order_id=order_id,
                approved_at=_aware_utc(2030, 5, 1, 9),
                approved_by_reference="approver-reopen",
            )
        )
        placed = stack.place.execute(
            PlacePurchaseOrderRequest(
                purchase_order_id=order_id,
                ordered_at=_aware_utc(2030, 5, 1, 10),
            )
        )

        line_id = placed.purchase_order.lines[0].purchase_order_line_id
        stack.receive.execute(
            RecordPurchaseReceiptRequest(
                purchase_order_id=order_id,
                receipt_reference="RCPT-R-1",
                received_at=_aware_utc(2030, 5, 2, 8),
                lines=(
                    PurchaseReceiptLineInput(
                        purchase_order_line_id=line_id,
                        quantity=Decimal("1.000"),
                    ),
                ),
            )
        )

        before_query = stack.get.execute(GetPurchaseOrderRequest(purchase_order_id=order_id))
        _ = stack.list_all.execute(ListPurchaseOrdersRequest())
        after_query = stack.get.execute(GetPurchaseOrderRequest(purchase_order_id=order_id))
        assert before_query.purchase_order.status == after_query.purchase_order.status
    finally:
        write_session.close()

    assert order_id is not None

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)
        loaded = stack.get.execute(
            GetPurchaseOrderRequest(purchase_order_id=order_id)
        )
        assert loaded.purchase_order.purchase_order_number == "PO-E2E-REOPEN"
        assert loaded.purchase_order.supplier_reference == "SUP-REOPEN"
        assert loaded.purchase_order.status == "PARTIALLY_RECEIVED"
        assert loaded.purchase_order.order_total_amount == Decimal("100.50")
        assert loaded.purchase_order.lines[0].inventory_item_reference == "INV-REOPEN-001"
        assert loaded.purchase_order.lines[0].line_total_amount == Decimal("100.50")
        assert loaded.purchase_order.receipts[0].receipt_reference == "RCPT-R-1"
        assert loaded.purchase_order.receipts[0].lines[0].quantity == Decimal("1.000")
    finally:
        read_session.close()


def test_e2e_procurement_stack_has_no_inventory_runtime_dependency() -> None:
    module_path = Path(__file__).resolve()
    tree = ast.parse(module_path.read_text(encoding="utf-8"), filename=str(module_path))

    forbidden_prefixes = (
        "mfm.application.features.inventory",
        "mfm.application.inventory",
        "mfm.infrastructure.persistence.sqlite.sqlite_inventory_repository",
        "mfm.repositories.inventory_repository",
    )

    violations: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            imports = [node.module or ""]
        else:
            continue

        for imported in imports:
            if any(
                imported == prefix or imported.startswith(f"{prefix}.")
                for prefix in forbidden_prefixes
            ):
                violations.append(imported)

    assert not violations, f"forbidden inventory runtime imports: {violations}"
