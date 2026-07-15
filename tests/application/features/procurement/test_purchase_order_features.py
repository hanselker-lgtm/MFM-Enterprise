from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from uuid import UUID

import pytest

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
    BusinessRuleViolation as FeatureBusinessRuleViolation,
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
from mfm.application.features.procurement.create_purchase_order_feature import (
    RepositoryException as FeatureRepositoryException,
)
from mfm.application.features.procurement.create_purchase_order_feature import (
    ValidationException as FeatureValidationException,
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
from mfm.application.procurement.create_purchase_order import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.procurement.create_purchase_order import (
    CreatePurchaseOrderResponse as ServiceCreatePurchaseOrderResponse,
)
from mfm.application.procurement.create_purchase_order import CreatePurchaseOrderUseCase
from mfm.application.procurement.create_purchase_order import (
    PurchaseOrderLineResponse,
)
from mfm.application.procurement.create_purchase_order import PurchaseOrderResponse
from mfm.application.procurement.create_purchase_order import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.procurement.create_purchase_order import (
    ValidationException as ServiceValidationException,
)
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
from tests.application.procurement.test_purchase_order_use_cases import (
    FakeProcurementUnitOfWork,
)


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        if self._error is not None:
            raise self._error
        return self._response


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


def _service_create_response() -> ServiceCreatePurchaseOrderResponse:
    return ServiceCreatePurchaseOrderResponse(
        purchase_order=PurchaseOrderResponse(
            purchase_order_id=UUID("00000000-0000-0000-0000-00000000F111"),
            purchase_order_number="PO-FEAT-001",
            supplier_reference="SUP-001",
            status="DRAFT",
            currency="DKK",
            created_at=_aware(2030, 1, 1, 8),
            supplier_name_snapshot="Supplier A",
            supplier_contact_snapshot="supplier@example.invalid",
            notes="feature",
            requested_by_reference="requester-1",
            approved_by_reference=None,
            approved_at=None,
            ordered_at=None,
            external_order_reference=None,
            cancelled_at=None,
            cancellation_reason=None,
            order_total_amount=Decimal("200.20"),
            received_total_amount=Decimal("0.00"),
            lines=(
                PurchaseOrderLineResponse(
                    purchase_order_line_id=UUID("00000000-0000-0000-0000-00000000F211"),
                    description_snapshot="Marine paint",
                    quantity=Decimal("2.000"),
                    unit_price_amount=Decimal("100.10"),
                    unit_price_currency="DKK",
                    line_total_amount=Decimal("200.20"),
                    received_quantity=Decimal("0.000"),
                    outstanding_quantity=Decimal("2.000"),
                    inventory_item_reference="INV-PAINT",
                    expected_delivery_at=None,
                    line_note="note",
                ),
            ),
            receipts=(),
        )
    )


def _create_order(uow: FakeProcurementUnitOfWork, *, number: str, supplier: str) -> UUID:
    response = CreatePurchaseOrderFeature(
        service=CreatePurchaseOrderUseCase(unit_of_work=uow)
    ).execute(
        CreatePurchaseOrderRequest(
            purchase_order_number=number,
            supplier_reference=supplier,
            currency="DKK",
            created_at=_aware(2030, 1, 1, 8),
            lines=(
                _line(
                    description="Marine paint",
                    quantity=Decimal("2.000"),
                    unit_price_amount=Decimal("100.10"),
                    inventory_item_reference="INV-PAINT",
                ),
            ),
        )
    )
    return response.purchase_order.purchase_order_id


def test_create_feature_request_adaptation_response_mapping_and_decimal_truth() -> None:
    service = StubService(response=_service_create_response())
    feature = CreatePurchaseOrderFeature(service=service)

    request = CreatePurchaseOrderRequest(
        purchase_order_number="PO-FEAT-001",
        supplier_reference="SUP-001",
        currency="DKK",
        created_at=_aware(2030, 1, 1, 8),
        lines=(
            _line(
                description="Marine paint",
                quantity=Decimal("2.000"),
                unit_price_amount=Decimal("100.10"),
                inventory_item_reference="INV-PAINT",
            ),
        ),
    )

    response = feature.execute(request)

    assert response.purchase_order.purchase_order_number == "PO-FEAT-001"
    assert response.purchase_order.supplier_reference == "SUP-001"
    assert response.purchase_order.order_total_amount == Decimal("200.20")
    assert response.purchase_order.lines[0].unit_price_amount == Decimal("100.10")
    assert response.purchase_order.lines[0].inventory_item_reference == "INV-PAINT"
    assert isinstance(response.purchase_order.order_total_amount, Decimal)
    assert isinstance(response.purchase_order.lines[0].unit_price_amount, Decimal)
    assert service.last_request.purchase_order_number == "PO-FEAT-001"
    assert service.last_request.supplier_reference == "SUP-001"
    assert service.last_request.lines[0].inventory_item_reference == "INV-PAINT"
    assert isinstance(service.last_request.lines[0].unit_price_amount, Decimal)
    assert is_dataclass(response.purchase_order)

    with pytest.raises(FrozenInstanceError):
        request.currency = "USD"  # type: ignore[misc]


def test_create_feature_error_mapping() -> None:
    invalid = CreatePurchaseOrderFeature(
        service=StubService(error=ServiceValidationException("invalid"))
    )
    with pytest.raises(FeatureValidationException):
        invalid.execute(
            CreatePurchaseOrderRequest(
                purchase_order_number="PO-ERR-1",
                supplier_reference="SUP-ERR",
                currency="DKK",
                created_at=_aware(2030, 1, 1, 8),
                lines=(_line(description="x", quantity=1, unit_price_amount=1),),
            )
        )

    duplicate = CreatePurchaseOrderFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate"))
    )
    with pytest.raises(FeatureBusinessRuleViolation):
        duplicate.execute(
            CreatePurchaseOrderRequest(
                purchase_order_number="PO-ERR-2",
                supplier_reference="SUP-ERR",
                currency="DKK",
                created_at=_aware(2030, 1, 1, 8),
                lines=(_line(description="x", quantity=1, unit_price_amount=1),),
            )
        )

    failing = CreatePurchaseOrderFeature(
        service=StubService(error=ServiceRepositoryException("failed"))
    )
    with pytest.raises(FeatureRepositoryException):
        failing.execute(
            CreatePurchaseOrderRequest(
                purchase_order_number="PO-ERR-3",
                supplier_reference="SUP-ERR",
                currency="DKK",
                created_at=_aware(2030, 1, 1, 8),
                lines=(_line(description="x", quantity=1, unit_price_amount=1),),
            )
        )


def test_get_list_and_filtered_list_features_delegate_and_preserve_order() -> None:
    uow = FakeProcurementUnitOfWork()
    id_a = _create_order(uow, number="PO-FEAT-A", supplier="SUP-A")
    id_b = _create_order(uow, number="PO-FEAT-B", supplier="SUP-A")
    id_c = _create_order(uow, number="PO-FEAT-C", supplier="SUP-B")

    SubmitPurchaseOrderFeature(service=SubmitPurchaseOrderUseCase(unit_of_work=uow)).execute(
        SubmitPurchaseOrderRequest(
            purchase_order_id=id_b,
            submitted_at=_aware(2030, 1, 2, 8),
        )
    )

    get_feature = GetPurchaseOrderFeature(service=GetPurchaseOrderUseCase(unit_of_work=uow))
    list_feature = ListPurchaseOrdersFeature(service=ListPurchaseOrdersUseCase(unit_of_work=uow))
    by_state_feature = ListPurchaseOrdersByStateFeature(
        service=ListPurchaseOrdersByStateUseCase(unit_of_work=uow)
    )
    by_supplier_feature = ListPurchaseOrdersBySupplierFeature(
        service=ListPurchaseOrdersBySupplierUseCase(unit_of_work=uow)
    )

    loaded = get_feature.execute(GetPurchaseOrderRequest(purchase_order_id=id_a))
    assert loaded.purchase_order.purchase_order_id == id_a

    with pytest.raises(FeatureBusinessRuleViolation):
        get_feature.execute(
            GetPurchaseOrderRequest(
                purchase_order_id=UUID("00000000-0000-0000-0000-00000000F404")
            )
        )

    listed = list_feature.execute(ListPurchaseOrdersRequest())
    listed_by_state = by_state_feature.execute(ListPurchaseOrdersByStateRequest(status="SUBMITTED"))
    listed_by_supplier = by_supplier_feature.execute(
        ListPurchaseOrdersBySupplierRequest(supplier_reference="SUP-A")
    )

    assert [item.purchase_order_number for item in listed.purchase_orders] == [
        "PO-FEAT-A",
        "PO-FEAT-B",
        "PO-FEAT-C",
    ]
    assert [item.purchase_order_number for item in listed_by_state.purchase_orders] == [
        "PO-FEAT-B"
    ]
    assert [item.purchase_order_number for item in listed_by_supplier.purchase_orders] == [
        "PO-FEAT-A",
        "PO-FEAT-B",
    ]

    _ = id_c


def test_lifecycle_features_map_requests_and_response_without_domain_logic_duplication() -> None:
    uow = FakeProcurementUnitOfWork()
    order_id = _create_order(uow, number="PO-FEAT-LIFE", supplier="SUP-LIFE")

    submit_feature = SubmitPurchaseOrderFeature(service=SubmitPurchaseOrderUseCase(unit_of_work=uow))
    approve_feature = ApprovePurchaseOrderFeature(
        service=ApprovePurchaseOrderUseCase(unit_of_work=uow)
    )
    place_feature = PlacePurchaseOrderFeature(service=PlacePurchaseOrderUseCase(unit_of_work=uow))
    cancel_feature = CancelPurchaseOrderFeature(
        service=CancelPurchaseOrderUseCase(unit_of_work=uow)
    )

    submitted = submit_feature.execute(
        SubmitPurchaseOrderRequest(
            purchase_order_id=order_id,
            submitted_at=_aware(2030, 1, 2, 8),
        )
    )
    assert submitted.purchase_order.status == "SUBMITTED"

    approved = approve_feature.execute(
        ApprovePurchaseOrderRequest(
            purchase_order_id=order_id,
            approved_at=_aware(2030, 1, 2, 9),
            approved_by_reference="approver-1",
        )
    )
    assert approved.purchase_order.status == "APPROVED"

    placed = place_feature.execute(
        PlacePurchaseOrderRequest(
            purchase_order_id=order_id,
            ordered_at=_aware(2030, 1, 2, 10),
            external_order_reference="SUP-ORD-1",
        )
    )
    assert placed.purchase_order.status == "ORDERED"

    cancelled = cancel_feature.execute(
        CancelPurchaseOrderRequest(
            purchase_order_id=order_id,
            cancelled_at=_aware(2030, 1, 2, 11),
            cancellation_reason="supplier closed",
        )
    )
    assert cancelled.purchase_order.status == "CANCELLED"


def test_amend_and_record_receipt_features_preserve_inventory_reference_and_decimal_quantity() -> None:
    uow = FakeProcurementUnitOfWork()
    order_id = _create_order(uow, number="PO-FEAT-AMEND", supplier="SUP-AMEND")

    loaded = GetPurchaseOrderFeature(service=GetPurchaseOrderUseCase(unit_of_work=uow)).execute(
        GetPurchaseOrderRequest(purchase_order_id=order_id)
    )
    line_id = loaded.purchase_order.lines[0].purchase_order_line_id

    amend_feature = AmendDraftPurchaseOrderFeature(
        service=AmendDraftPurchaseOrderUseCase(unit_of_work=uow)
    )
    amended = amend_feature.execute(
        AmendDraftPurchaseOrderRequest(
            purchase_order_id=order_id,
            supplier_reference="SUP-AMEND-2",
            add_lines=(
                _line(
                    description="Filter",
                    quantity=Decimal("1.000"),
                    unit_price_amount=Decimal("50.00"),
                    inventory_item_reference="INV-FILTER",
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

    assert amended.purchase_order.supplier_reference == "SUP-AMEND-2"
    assert any(
        line.inventory_item_reference == "INV-FILTER"
        for line in amended.purchase_order.lines
    )

    SubmitPurchaseOrderFeature(service=SubmitPurchaseOrderUseCase(unit_of_work=uow)).execute(
        SubmitPurchaseOrderRequest(
            purchase_order_id=order_id,
            submitted_at=_aware(2030, 1, 3, 8),
        )
    )
    ApprovePurchaseOrderFeature(service=ApprovePurchaseOrderUseCase(unit_of_work=uow)).execute(
        ApprovePurchaseOrderRequest(
            purchase_order_id=order_id,
            approved_at=_aware(2030, 1, 3, 9),
            approved_by_reference="approver-1",
        )
    )
    PlacePurchaseOrderFeature(service=PlacePurchaseOrderUseCase(unit_of_work=uow)).execute(
        PlacePurchaseOrderRequest(
            purchase_order_id=order_id,
            ordered_at=_aware(2030, 1, 3, 10),
        )
    )

    receipt_feature = RecordPurchaseReceiptFeature(
        service=RecordPurchaseReceiptUseCase(unit_of_work=uow)
    )
    receipt_response = receipt_feature.execute(
        RecordPurchaseReceiptRequest(
            purchase_order_id=order_id,
            receipt_reference="RCPT-1",
            received_at=_aware(2030, 1, 4, 8),
            lines=(
                PurchaseReceiptLineInput(
                    purchase_order_line_id=line_id,
                    quantity=Decimal("1.500"),
                ),
            ),
        )
    )

    assert receipt_response.purchase_order.receipts[-1].receipt_reference == "RCPT-1"
    assert receipt_response.purchase_order.receipts[-1].lines[0].quantity == Decimal("1.500")
    assert isinstance(receipt_response.purchase_order.receipts[-1].lines[0].quantity, Decimal)


def test_feature_validation_paths_for_explicit_request_types() -> None:
    with pytest.raises(FeatureValidationException):
        SubmitPurchaseOrderRequest(
            purchase_order_id=UUID("00000000-0000-0000-0000-00000000F501"),
            submitted_at="2030-01-02",  # type: ignore[arg-type]
        ).validate()

    with pytest.raises(FeatureValidationException):
        ListPurchaseOrdersByStateRequest(status="").validate()

    with pytest.raises(FeatureValidationException):
        ListPurchaseOrdersBySupplierRequest(supplier_reference="").validate()


def test_procurement_feature_layer_has_no_inventory_or_organization_dependencies() -> None:
    project_root = Path(__file__).resolve().parents[4]
    package_path = project_root / "src" / "mfm" / "application" / "features" / "procurement"

    forbidden_prefixes = (
        "mfm.application.features.inventory",
        "mfm.application.inventory",
        "mfm.repositories.inventory",
        "mfm.infrastructure.persistence.sqlite.sqlite_inventory",
        "mfm.application.features.organization",
        "mfm.application.organization",
        "mfm.repositories.organization",
    )

    violations: list[str] = []

    for file_path in sorted(package_path.rglob("*.py")):
        tree = ast.parse(file_path.read_text(encoding="utf-8"), filename=str(file_path))

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
                    violations.append(f"{file_path}: forbidden import {imported}")

    assert not violations, "\n".join(violations)
