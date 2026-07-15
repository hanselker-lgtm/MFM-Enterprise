from __future__ import annotations

from dataclasses import FrozenInstanceError
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from importlib import import_module
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.features.inventory.adjust_stock_feature import AdjustStockFeature
from mfm.application.features.inventory.adjust_stock_feature import AdjustStockRequest
from mfm.application.features.inventory.create_inventory_item_feature import (
    BusinessRuleViolation as FeatureBusinessRuleViolation,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    CreateInventoryItemFeature,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    CreateInventoryItemRequest,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    RepositoryException as FeatureRepositoryException,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    StockLocationInput,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    ValidationException as FeatureValidationException,
)
from mfm.application.features.inventory.deactivate_inventory_item_feature import (
    DeactivateInventoryItemFeature,
)
from mfm.application.features.inventory.deactivate_inventory_item_feature import (
    DeactivateInventoryItemRequest,
)
from mfm.application.features.inventory.get_inventory_item_feature import GetInventoryItemFeature
from mfm.application.features.inventory.get_inventory_item_feature import GetInventoryItemRequest
from mfm.application.features.inventory.issue_stock_feature import IssueStockFeature
from mfm.application.features.inventory.issue_stock_feature import IssueStockRequest
from mfm.application.features.inventory.list_inventory_items_feature import (
    ListInventoryItemsFeature,
)
from mfm.application.features.inventory.list_inventory_items_feature import (
    ListInventoryItemsRequest,
)
from mfm.application.features.inventory.list_low_stock_items_feature import (
    ListLowStockItemsFeature,
)
from mfm.application.features.inventory.list_low_stock_items_feature import (
    ListLowStockItemsRequest,
)
from mfm.application.features.inventory.reactivate_inventory_item_feature import (
    ReactivateInventoryItemFeature,
)
from mfm.application.features.inventory.reactivate_inventory_item_feature import (
    ReactivateInventoryItemRequest,
)
from mfm.application.features.inventory.receive_stock_feature import ReceiveStockFeature
from mfm.application.features.inventory.receive_stock_feature import ReceiveStockRequest
from mfm.application.inventory.adjust_stock import AdjustStockUseCase
from mfm.application.inventory.create_inventory_item import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.inventory.create_inventory_item import (
    CreateInventoryItemResponse as ServiceCreateInventoryItemResponse,
)
from mfm.application.inventory.create_inventory_item import CreateInventoryItemUseCase
from mfm.application.inventory.create_inventory_item import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.inventory.create_inventory_item import (
    ValidationException as ServiceValidationException,
)
from mfm.application.inventory.deactivate_inventory_item import DeactivateInventoryItemUseCase
from mfm.application.inventory.get_inventory_item import GetInventoryItemUseCase
from mfm.application.inventory.issue_stock import IssueStockUseCase
from mfm.application.inventory.list_inventory_items import ListInventoryItemsUseCase
from mfm.application.inventory.list_low_stock_items import ListLowStockItemsUseCase
from mfm.application.inventory.reactivate_inventory_item import ReactivateInventoryItemUseCase
from mfm.application.inventory.receive_stock import ReceiveStockUseCase
from tests.application.inventory.test_inventory_use_cases import FakeInventoryUnitOfWork


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


def _location(
    key: str = "STORE-A",
    name: str = "Store A",
    *,
    vessel_id: UUID | None = None,
) -> StockLocationInput:
    return StockLocationInput(location_key=key, location_name=name, vessel_id=vessel_id)


def _service_create_response() -> ServiceCreateInventoryItemResponse:
    from mfm.application.inventory.create_inventory_item import InventoryItemResponse

    return ServiceCreateInventoryItemResponse(
        inventory_item=InventoryItemResponse(
            inventory_item_id=UUID("00000000-0000-0000-0000-00000000F001"),
            item_reference="INV-FEAT-001",
            name="Feature Item",
            description="Feature response",
            unit_code="LITRE",
            unit_decimal_places=2,
            unit_display_name="litre",
            status="ACTIVE",
            total_quantity=Decimal("0.00"),
            minimum_stock_level=Decimal("1.00"),
            low_stock=True,
            positions=(),
            movements=(),
        )
    )


def test_create_feature_request_mapping_and_response_mapping_and_immutability() -> None:
    service = StubService(response=_service_create_response())
    feature = CreateInventoryItemFeature(service=service)

    request = CreateInventoryItemRequest(
        item_reference="INV-FEAT-001",
        name="Feature Item",
        unit_code="LITRE",
        unit_decimal_places=2,
        description="Feature request",
        unit_display_name="litre",
        minimum_stock_level=Decimal("1.00"),
    )

    response = feature.execute(request)

    assert response.inventory_item.item_reference == "INV-FEAT-001"
    assert response.inventory_item.low_stock is True
    assert service.last_request.item_reference == "INV-FEAT-001"
    assert is_dataclass(response.inventory_item)

    with pytest.raises(FrozenInstanceError):
        request.item_reference = "INV-CHANGED"  # type: ignore[misc]


def test_create_feature_error_mapping() -> None:
    invalid = CreateInventoryItemFeature(
        service=StubService(error=ServiceValidationException("invalid"))
    )
    with pytest.raises(FeatureValidationException):
        invalid.execute(
            CreateInventoryItemRequest(
                item_reference="INV-FEAT-ERR-1",
                name="Error",
                unit_code="LITRE",
                unit_decimal_places=2,
            )
        )

    duplicate = CreateInventoryItemFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate"))
    )
    with pytest.raises(FeatureBusinessRuleViolation):
        duplicate.execute(
            CreateInventoryItemRequest(
                item_reference="INV-FEAT-ERR-2",
                name="Error",
                unit_code="LITRE",
                unit_decimal_places=2,
            )
        )

    failing = CreateInventoryItemFeature(
        service=StubService(error=ServiceRepositoryException("failed"))
    )
    with pytest.raises(FeatureRepositoryException):
        failing.execute(
            CreateInventoryItemRequest(
                item_reference="INV-FEAT-ERR-3",
                name="Error",
                unit_code="LITRE",
                unit_decimal_places=2,
            )
        )


def test_get_feature_existing_and_missing_mapping() -> None:
    uow = FakeInventoryUnitOfWork()
    create = CreateInventoryItemFeature(service=CreateInventoryItemUseCase(unit_of_work=uow))
    get_feature = GetInventoryItemFeature(service=GetInventoryItemUseCase(unit_of_work=uow))

    created = create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-GET",
            name="Get Item",
            unit_code="LITRE",
            unit_decimal_places=1,
        )
    )

    existing = get_feature.execute(
        GetInventoryItemRequest(inventory_item_id=created.inventory_item.inventory_item_id)
    )
    assert existing.inventory_item.item_reference == "INV-FEAT-GET"

    with pytest.raises(FeatureBusinessRuleViolation):
        get_feature.execute(
            GetInventoryItemRequest(
                inventory_item_id=UUID("00000000-0000-0000-0000-00000000F404")
            )
        )


def test_list_feature_preserves_deterministic_order_mapping() -> None:
    uow = FakeInventoryUnitOfWork()
    create = CreateInventoryItemFeature(service=CreateInventoryItemUseCase(unit_of_work=uow))
    listing = ListInventoryItemsFeature(service=ListInventoryItemsUseCase(unit_of_work=uow))

    create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-B",
            name="B",
            unit_code="LITRE",
            unit_decimal_places=1,
        )
    )
    create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-C",
            name="C",
            unit_code="LITRE",
            unit_decimal_places=1,
        )
    )
    create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-A",
            name="A",
            unit_code="LITRE",
            unit_decimal_places=1,
        )
    )

    response = listing.execute(ListInventoryItemsRequest())
    assert [item.item_reference for item in response.items] == [
        "INV-FEAT-A",
        "INV-FEAT-B",
        "INV-FEAT-C",
    ]


def test_receive_issue_adjust_feature_delegation_and_state_mapping() -> None:
    uow = FakeInventoryUnitOfWork()
    create = CreateInventoryItemFeature(service=CreateInventoryItemUseCase(unit_of_work=uow))
    receive = ReceiveStockFeature(service=ReceiveStockUseCase(unit_of_work=uow))
    issue = IssueStockFeature(service=IssueStockUseCase(unit_of_work=uow))
    adjust = AdjustStockFeature(service=AdjustStockUseCase(unit_of_work=uow))

    created = create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-STOCK",
            name="Stock Item",
            unit_code="LITRE",
            unit_decimal_places=1,
            minimum_stock_level=Decimal("2.0"),
        )
    )
    item_id = created.inventory_item.inventory_item_id

    received = receive.execute(
        ReceiveStockRequest(
            inventory_item_id=item_id,
            location=_location("SHELF-A", "Shelf A"),
            quantity=Decimal("5.0"),
            occurred_at=_aware(2028, 2, 1, 8),
            external_reference="PROC-1001",
        )
    )
    assert received.inventory_item.total_quantity == Decimal("5.0")
    assert received.inventory_item.movements[-1].movement_type == "RECEIPT"

    issued = issue.execute(
        IssueStockRequest(
            inventory_item_id=item_id,
            location=_location("SHELF-A", "Shelf A"),
            quantity=Decimal("3.0"),
            occurred_at=_aware(2028, 2, 1, 9),
            external_reference="WO-1002",
        )
    )
    assert issued.inventory_item.total_quantity == Decimal("2.0")
    assert issued.inventory_item.movements[-1].movement_type == "ISSUE"

    adjusted = adjust.execute(
        AdjustStockRequest(
            inventory_item_id=item_id,
            location=_location("SHELF-A", "Shelf A"),
            counted_quantity=Decimal("1.5"),
            reason="count correction",
            occurred_at=_aware(2028, 2, 1, 10),
            note="adjust",
        )
    )
    assert adjusted.inventory_item.total_quantity == Decimal("1.5")
    assert adjusted.inventory_item.movements[-1].movement_type == "ADJUSTMENT_DECREASE"


def test_issue_feature_insufficient_stock_error_mapping() -> None:
    uow = FakeInventoryUnitOfWork()
    create = CreateInventoryItemFeature(service=CreateInventoryItemUseCase(unit_of_work=uow))
    issue = IssueStockFeature(service=IssueStockUseCase(unit_of_work=uow))

    created = create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-INSUFF",
            name="Insuff",
            unit_code="LITRE",
            unit_decimal_places=1,
        )
    )

    with pytest.raises(FeatureBusinessRuleViolation):
        issue.execute(
            IssueStockRequest(
                inventory_item_id=created.inventory_item.inventory_item_id,
                location=_location("SHELF-A", "Shelf A"),
                quantity=Decimal("1.0"),
                occurred_at=_aware(2028, 2, 2, 8),
            )
        )


def test_deactivate_and_reactivate_feature_mapping() -> None:
    uow = FakeInventoryUnitOfWork()
    create = CreateInventoryItemFeature(service=CreateInventoryItemUseCase(unit_of_work=uow))
    deactivate = DeactivateInventoryItemFeature(
        service=DeactivateInventoryItemUseCase(unit_of_work=uow)
    )
    reactivate = ReactivateInventoryItemFeature(
        service=ReactivateInventoryItemUseCase(unit_of_work=uow)
    )

    created = create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-LC",
            name="Lifecycle",
            unit_code="LITRE",
            unit_decimal_places=1,
        )
    )
    item_id = created.inventory_item.inventory_item_id

    deactivated = deactivate.execute(DeactivateInventoryItemRequest(inventory_item_id=item_id))
    assert deactivated.inventory_item.status == "INACTIVE"

    reactivated = reactivate.execute(ReactivateInventoryItemRequest(inventory_item_id=item_id))
    assert reactivated.inventory_item.status == "ACTIVE"


def test_low_stock_feature_mapping_and_no_procurement_side_effect() -> None:
    uow = FakeInventoryUnitOfWork()
    create = CreateInventoryItemFeature(service=CreateInventoryItemUseCase(unit_of_work=uow))
    receive = ReceiveStockFeature(service=ReceiveStockUseCase(unit_of_work=uow))
    low_stock = ListLowStockItemsFeature(service=ListLowStockItemsUseCase(unit_of_work=uow))

    above = create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-ABOVE",
            name="Above",
            unit_code="LITRE",
            unit_decimal_places=1,
            minimum_stock_level=Decimal("2.0"),
        )
    )
    below = create.execute(
        CreateInventoryItemRequest(
            item_reference="INV-FEAT-BELOW",
            name="Below",
            unit_code="LITRE",
            unit_decimal_places=1,
            minimum_stock_level=Decimal("2.0"),
        )
    )

    receive.execute(
        ReceiveStockRequest(
            inventory_item_id=above.inventory_item.inventory_item_id,
            location=_location(),
            quantity=Decimal("3.0"),
            occurred_at=_aware(2028, 2, 3, 8),
        )
    )
    receive.execute(
        ReceiveStockRequest(
            inventory_item_id=below.inventory_item.inventory_item_id,
            location=_location(),
            quantity=Decimal("1.0"),
            occurred_at=_aware(2028, 2, 3, 9),
        )
    )

    listed = low_stock.execute(ListLowStockItemsRequest())
    refs = {item.item_reference for item in listed.items}

    assert refs == {"INV-FEAT-BELOW"}
    assert not hasattr(low_stock, "purchase_order_repository")


def test_feature_boundary_no_sqlalchemy_or_sqlite_repository_dependencies() -> None:
    modules = [
        import_module("mfm.application.features.inventory.create_inventory_item_feature"),
        import_module("mfm.application.features.inventory.get_inventory_item_feature"),
        import_module("mfm.application.features.inventory.list_inventory_items_feature"),
        import_module("mfm.application.features.inventory.list_low_stock_items_feature"),
        import_module("mfm.application.features.inventory.receive_stock_feature"),
        import_module("mfm.application.features.inventory.issue_stock_feature"),
        import_module("mfm.application.features.inventory.adjust_stock_feature"),
        import_module("mfm.application.features.inventory.deactivate_inventory_item_feature"),
        import_module("mfm.application.features.inventory.reactivate_inventory_item_feature"),
    ]

    for module in modules:
        text = (module.__doc__ or "") + "\n" + "\n".join(sorted(module.__dict__.keys()))
        lowered = text.lower()
        assert "sqlalchemy" not in lowered
        assert "sqliteinventoryrepository" not in lowered
        assert "session" not in lowered
