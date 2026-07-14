from __future__ import annotations

from copy import deepcopy
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.inventory.adjust_stock import AdjustStockRequest
from mfm.application.inventory.adjust_stock import AdjustStockUseCase
from mfm.application.inventory.create_inventory_item import BusinessRuleViolation
from mfm.application.inventory.create_inventory_item import CreateInventoryItemRequest
from mfm.application.inventory.create_inventory_item import CreateInventoryItemUseCase
from mfm.application.inventory.create_inventory_item import RepositoryException
from mfm.application.inventory.create_inventory_item import StockLocationInput
from mfm.application.inventory.get_inventory_item import GetInventoryItemRequest
from mfm.application.inventory.get_inventory_item import GetInventoryItemUseCase
from mfm.application.inventory.issue_stock import IssueStockRequest
from mfm.application.inventory.issue_stock import IssueStockUseCase
from mfm.application.inventory.list_inventory_items import ListInventoryItemsRequest
from mfm.application.inventory.list_inventory_items import ListInventoryItemsUseCase
from mfm.application.inventory.list_low_stock_items import ListLowStockItemsRequest
from mfm.application.inventory.list_low_stock_items import ListLowStockItemsUseCase
from mfm.application.inventory.receive_stock import ReceiveStockRequest
from mfm.application.inventory.receive_stock import ReceiveStockUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.inventory.inventory_item import InventoryItem
from mfm.domain.inventory.stock_location import StockLocation
from mfm.domain.inventory.stock_movement_type import StockMovementType
from mfm.domain.inventory.unit_of_measure import UnitOfMeasure
from mfm.repositories.inventory_repository import InventoryRepository


class InMemoryInventoryRepository(InventoryRepository):
    def __init__(
        self,
        *,
        fail_on_add: bool = False,
        fail_on_update: bool = False,
    ) -> None:
        self._items: dict[UUID, InventoryItem] = {}
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

        self.add_calls = 0
        self.get_by_id_calls = 0
        self.update_calls = 0
        self.list_calls = 0
        self.low_stock_calls = 0

    def snapshot(self) -> dict[UUID, InventoryItem]:
        return deepcopy(self._items)

    def restore(self, snapshot: dict[UUID, InventoryItem]) -> None:
        self._items = deepcopy(snapshot)

    def add(self, item: InventoryItem) -> None:
        self.add_calls += 1
        if self._fail_on_add:
            raise RuntimeError("inventory add failed")
        if self.exists_by_reference(item.item_reference):
            raise ValueError(f"Inventory reference {item.item_reference} already exists")
        self._items[item.id.value] = deepcopy(item)

    def get_by_id(self, inventory_item_id: UUID) -> InventoryItem | None:
        self.get_by_id_calls += 1
        item = self._items.get(inventory_item_id)
        return deepcopy(item) if item is not None else None

    def get_by_reference(self, item_reference: str) -> InventoryItem | None:
        normalized = item_reference.strip()
        for item in self._items.values():
            if item.item_reference == normalized:
                return deepcopy(item)
        return None

    def update(self, item: InventoryItem) -> None:
        self.update_calls += 1
        if self._fail_on_update:
            raise RuntimeError("inventory update failed")
        if item.id.value not in self._items:
            raise ValueError(f"Inventory item {item.id.value} does not exist")

        duplicate = next(
            (
                existing
                for existing in self._items.values()
                if existing.item_reference == item.item_reference
                and existing.id.value != item.id.value
            ),
            None,
        )
        if duplicate is not None:
            raise ValueError(f"Inventory reference {item.item_reference} already exists")

        self._items[item.id.value] = deepcopy(item)

    def exists_by_reference(self, item_reference: str) -> bool:
        normalized = item_reference.strip()
        return any(item.item_reference == normalized for item in self._items.values())

    def list(self) -> list[InventoryItem]:
        self.list_calls += 1
        return [
            deepcopy(item)
            for _, item in sorted(
                self._items.items(),
                key=lambda pair: (pair[1].item_reference, str(pair[0])),
            )
        ]

    def get_low_stock(self) -> list[InventoryItem]:
        self.low_stock_calls += 1
        return [item for item in self.list() if item.low_stock]


class FakeInventoryUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_add: bool = False,
        fail_update: bool = False,
        fail_commit: bool = False,
    ) -> None:
        super().__init__()
        self._fail_commit = fail_commit
        self._repository = InMemoryInventoryRepository(
            fail_on_add=fail_add,
            fail_on_update=fail_update,
        )
        self._snapshot: dict[UUID, InventoryItem] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self.inventory_repository = self._repository
        self._snapshot = self._repository.snapshot()

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

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


def _location(
    key: str = "STORE-A",
    name: str = "Store A",
    *,
    vessel_id: UUID | None = None,
) -> StockLocationInput:
    return StockLocationInput(location_key=key, location_name=name, vessel_id=vessel_id)


def _create_inventory_item(
    uow: FakeInventoryUnitOfWork,
    *,
    item_reference: str = "INV-APP-001",
    minimum_stock_level: Decimal | str | int | None = Decimal("2.0"),
) -> UUID:
    response = CreateInventoryItemUseCase(unit_of_work=uow).execute(
        CreateInventoryItemRequest(
            item_reference=item_reference,
            name="Marine Paint",
            description="Application item",
            unit_code="LITRE",
            unit_decimal_places=1,
            unit_display_name="litre",
            minimum_stock_level=minimum_stock_level,
        )
    )
    return response.inventory_item.inventory_item_id


def test_create_inventory_item_success_and_duplicate_reference() -> None:
    uow = FakeInventoryUnitOfWork()
    use_case = CreateInventoryItemUseCase(unit_of_work=uow)

    created = use_case.execute(
        CreateInventoryItemRequest(
            item_reference="INV-APP-100",
            name="Hydraulic Oil",
            description="Main stock",
            unit_code="LITRE",
            unit_decimal_places=2,
            unit_display_name="litre",
            minimum_stock_level=Decimal("5.00"),
        )
    )

    assert uow.commits == 1
    assert created.inventory_item.item_reference == "INV-APP-100"
    assert created.inventory_item.total_quantity == Decimal("0.00")

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            CreateInventoryItemRequest(
                item_reference="INV-APP-100",
                name="Hydraulic Oil Duplicate",
                unit_code="LITRE",
                unit_decimal_places=2,
            )
        )

    assert uow.commits == 1


def test_get_inventory_item_existing_and_missing() -> None:
    uow = FakeInventoryUnitOfWork()
    item_id = _create_inventory_item(uow, item_reference="INV-APP-GET")
    get_use_case = GetInventoryItemUseCase(unit_of_work=uow)

    existing = get_use_case.execute(GetInventoryItemRequest(inventory_item_id=item_id))
    assert existing.inventory_item.inventory_item_id == item_id

    with pytest.raises(BusinessRuleViolation):
        get_use_case.execute(
            GetInventoryItemRequest(
                inventory_item_id=UUID("00000000-0000-0000-0000-00000000E404")
            )
        )


def test_receive_stock_updates_quantity_keeps_history_and_commits() -> None:
    uow = FakeInventoryUnitOfWork()
    item_id = _create_inventory_item(uow, item_reference="INV-APP-RECEIVE")

    response = ReceiveStockUseCase(unit_of_work=uow).execute(
        ReceiveStockRequest(
            inventory_item_id=item_id,
            location=_location("SHELF-A", "Shelf A"),
            quantity=Decimal("5.0"),
            occurred_at=_aware(2028, 1, 1, 8),
            external_reference="PROC-901",
            note="Initial receipt",
        )
    )

    assert uow.commits == 2
    assert response.inventory_item.total_quantity == Decimal("5.0")
    assert len(response.inventory_item.movements) == 1
    assert response.inventory_item.movements[0].movement_type == "RECEIPT"
    assert response.inventory_item.movements[0].external_reference == "PROC-901"


def test_issue_stock_valid_and_insufficient_stock_no_commit() -> None:
    uow = FakeInventoryUnitOfWork()
    item_id = _create_inventory_item(uow, item_reference="INV-APP-ISSUE")
    receiver = ReceiveStockUseCase(unit_of_work=uow)
    issuer = IssueStockUseCase(unit_of_work=uow)

    receiver.execute(
        ReceiveStockRequest(
            inventory_item_id=item_id,
            location=_location("SHELF-A", "Shelf A"),
            quantity=Decimal("4.0"),
            occurred_at=_aware(2028, 1, 2, 8),
        )
    )

    issued = issuer.execute(
        IssueStockRequest(
            inventory_item_id=item_id,
            location=_location("SHELF-A", "Shelf A"),
            quantity=Decimal("1.5"),
            occurred_at=_aware(2028, 1, 2, 9),
            external_reference="WO-902",
        )
    )
    assert issued.inventory_item.total_quantity == Decimal("2.5")
    assert uow.commits == 3

    before_commits = uow.commits
    with pytest.raises(BusinessRuleViolation):
        issuer.execute(
            IssueStockRequest(
                inventory_item_id=item_id,
                location=_location("SHELF-A", "Shelf A"),
                quantity=Decimal("9.9"),
                occurred_at=_aware(2028, 1, 2, 10),
            )
        )

    assert uow.commits == before_commits
    stored = uow.inventory_repository.get_by_id(item_id)
    assert stored is not None
    assert stored.total_quantity == Decimal("2.5")


def test_adjust_stock_persists_and_retains_history() -> None:
    uow = FakeInventoryUnitOfWork()
    item_id = _create_inventory_item(uow, item_reference="INV-APP-ADJUST")

    ReceiveStockUseCase(unit_of_work=uow).execute(
        ReceiveStockRequest(
            inventory_item_id=item_id,
            location=_location("SHELF-A", "Shelf A"),
            quantity=Decimal("7.0"),
            occurred_at=_aware(2028, 1, 3, 8),
        )
    )

    adjusted = AdjustStockUseCase(unit_of_work=uow).execute(
        AdjustStockRequest(
            inventory_item_id=item_id,
            location=_location("SHELF-A", "Shelf A"),
            counted_quantity=Decimal("6.0"),
            reason="Cycle count",
            occurred_at=_aware(2028, 1, 3, 9),
            note="Adjustment after count",
        )
    )

    assert adjusted.inventory_item.total_quantity == Decimal("6.0")
    assert len(adjusted.inventory_item.movements) == 2
    assert adjusted.inventory_item.movements[-1].movement_type == "ADJUSTMENT_DECREASE"
    assert adjusted.inventory_item.movements[-1].reason == "Cycle count"


def test_historical_stock_truth_sequence_results_in_expected_quantity() -> None:
    uow = FakeInventoryUnitOfWork()
    item_id = _create_inventory_item(
        uow,
        item_reference="INV-APP-HISTORY",
        minimum_stock_level=Decimal("0.0"),
    )
    location = _location("PAINT-SHELF", "Paint Shelf")

    ReceiveStockUseCase(unit_of_work=uow).execute(
        ReceiveStockRequest(
            inventory_item_id=item_id,
            location=location,
            quantity=Decimal("10.0"),
            occurred_at=_aware(2028, 1, 4, 8),
            note="opening",
        )
    )
    ReceiveStockUseCase(unit_of_work=uow).execute(
        ReceiveStockRequest(
            inventory_item_id=item_id,
            location=location,
            quantity=Decimal("5.0"),
            occurred_at=_aware(2028, 1, 5, 8),
            note="receive",
        )
    )
    IssueStockUseCase(unit_of_work=uow).execute(
        IssueStockRequest(
            inventory_item_id=item_id,
            location=location,
            quantity=Decimal("3.0"),
            occurred_at=_aware(2028, 1, 6, 8),
            note="issue",
        )
    )
    AdjustStockUseCase(unit_of_work=uow).execute(
        AdjustStockRequest(
            inventory_item_id=item_id,
            location=location,
            counted_quantity=Decimal("11.0"),
            reason="count correction",
            occurred_at=_aware(2028, 1, 7, 8),
            note="adjust",
        )
    )

    item = uow.inventory_repository.get_by_id(item_id)
    assert item is not None
    assert item.total_quantity == Decimal("11.0")
    assert item.explained_quantity_from_history() == Decimal("11.0")
    assert [movement.movement_type for movement in item.movements] == [
        StockMovementType.RECEIPT,
        StockMovementType.RECEIPT,
        StockMovementType.ISSUE,
        StockMovementType.ADJUSTMENT_DECREASE,
    ]


def test_list_low_stock_items_uses_threshold_semantics_without_procurement_side_effects() -> None:
    uow = FakeInventoryUnitOfWork()

    above_id = _create_inventory_item(
        uow,
        item_reference="INV-APP-ABOVE",
        minimum_stock_level=Decimal("2.0"),
    )
    equal_id = _create_inventory_item(
        uow,
        item_reference="INV-APP-EQUAL",
        minimum_stock_level=Decimal("2.0"),
    )
    below_id = _create_inventory_item(
        uow,
        item_reference="INV-APP-BELOW",
        minimum_stock_level=Decimal("2.0"),
    )

    receiver = ReceiveStockUseCase(unit_of_work=uow)
    receiver.execute(
        ReceiveStockRequest(
            inventory_item_id=above_id,
            location=_location(),
            quantity=Decimal("3.0"),
            occurred_at=_aware(2028, 1, 8, 8),
        )
    )
    receiver.execute(
        ReceiveStockRequest(
            inventory_item_id=equal_id,
            location=_location(),
            quantity=Decimal("2.0"),
            occurred_at=_aware(2028, 1, 8, 9),
        )
    )
    receiver.execute(
        ReceiveStockRequest(
            inventory_item_id=below_id,
            location=_location(),
            quantity=Decimal("1.0"),
            occurred_at=_aware(2028, 1, 8, 10),
        )
    )

    listed = ListLowStockItemsUseCase(unit_of_work=uow).execute(ListLowStockItemsRequest())
    refs = {item.item_reference for item in listed.items}

    assert refs == {"INV-APP-BELOW"}
    assert uow.inventory_repository.low_stock_calls == 1


def test_list_inventory_items_returns_deterministic_reference_order() -> None:
    uow = FakeInventoryUnitOfWork()
    _create_inventory_item(uow, item_reference="INV-APP-B")
    _create_inventory_item(uow, item_reference="INV-APP-C")
    _create_inventory_item(uow, item_reference="INV-APP-A")

    listed = ListInventoryItemsUseCase(unit_of_work=uow).execute(ListInventoryItemsRequest())
    assert [item.item_reference for item in listed.items] == [
        "INV-APP-A",
        "INV-APP-B",
        "INV-APP-C",
    ]


def test_transaction_failure_path_rolls_back_and_does_not_commit_invalid_state() -> None:
    uow = FakeInventoryUnitOfWork(fail_update=True)
    item_id = _create_inventory_item(uow, item_reference="INV-APP-TX")

    with pytest.raises(RepositoryException):
        ReceiveStockUseCase(unit_of_work=uow).execute(
            ReceiveStockRequest(
                inventory_item_id=item_id,
                location=_location(),
                quantity=Decimal("1.0"),
                occurred_at=_aware(2028, 1, 9, 8),
            )
        )

    assert uow.rollbacks == 1
    assert uow.commits == 1

    stored = uow.inventory_repository.get_by_id(item_id)
    assert stored is not None
    assert stored.total_quantity == Decimal("0.0")
    assert len(stored.movements) == 0


def test_inventory_request_response_dtos_are_immutable_dataclasses() -> None:
    request = CreateInventoryItemRequest(
        item_reference="INV-APP-FROZEN",
        name="Frozen",
        unit_code="PIECE",
        unit_decimal_places=0,
    )

    response = CreateInventoryItemUseCase(unit_of_work=FakeInventoryUnitOfWork()).execute(
        request
    )

    assert is_dataclass(type(request))
    assert is_dataclass(type(response.inventory_item))

    with pytest.raises(AttributeError):
        request.item_reference = "INV-APP-CHANGED"  # type: ignore[misc]


def test_vessel_location_reference_is_preserved_as_metadata_only() -> None:
    uow = FakeInventoryUnitOfWork()
    item_id = _create_inventory_item(uow, item_reference="INV-APP-VESSEL-REF")
    vessel_id = UUID("00000000-0000-0000-0000-00000000D777")

    response = ReceiveStockUseCase(unit_of_work=uow).execute(
        ReceiveStockRequest(
            inventory_item_id=item_id,
            location=_location("VESSEL-STORE", "Vessel Store", vessel_id=vessel_id),
            quantity=Decimal("2.0"),
            occurred_at=_aware(2028, 1, 10, 8),
        )
    )

    assert response.inventory_item.positions[0].vessel_id == vessel_id

    location = StockLocation(
        location_key="VESSEL-STORE",
        location_name="Vessel Store",
        vessel_id=vessel_id,
    )
    domain_item = uow.inventory_repository.get_by_id(item_id)
    assert domain_item is not None
    assert domain_item.quantity_at(location) == Decimal("2.0")
