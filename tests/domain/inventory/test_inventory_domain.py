from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.inventory.events import InventoryItemCreated
from mfm.domain.inventory.events import InventoryItemDeactivated
from mfm.domain.inventory.events import InventoryItemReactivated
from mfm.domain.inventory.events import StockAdjusted
from mfm.domain.inventory.events import StockIssued
from mfm.domain.inventory.events import StockReceived
from mfm.domain.inventory.exceptions import InsufficientStockError
from mfm.domain.inventory.exceptions import InvalidInventoryAdjustmentError
from mfm.domain.inventory.exceptions import InvalidInventoryLifecycleError
from mfm.domain.inventory.exceptions import InvalidInventoryQuantityError
from mfm.domain.inventory.exceptions import InvalidInventoryReferenceError
from mfm.domain.inventory.exceptions import InvalidStockLocationError
from mfm.domain.inventory.exceptions import InvalidUnitOfMeasureError
from mfm.domain.inventory.inventory_item import InventoryItem
from mfm.domain.inventory.inventory_item_status import InventoryItemStatus
from mfm.domain.inventory.stock_location import StockLocation
from mfm.domain.inventory.stock_movement_type import StockMovementType
from mfm.domain.inventory.unit_of_measure import UnitOfMeasure


def _dt(year: int, month: int, day: int, hour: int = 8, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _unit_piece() -> UnitOfMeasure:
    return UnitOfMeasure(unit_code="PIECE", decimal_places=0, display_name="piece")


def _unit_litre() -> UnitOfMeasure:
    return UnitOfMeasure(unit_code="LITRE", decimal_places=1, display_name="litre")


def _location(
    key: str = "WORKSHOP-SHELF-A",
    name: str = "Workshop Shelf A",
    *,
    vessel_id: UUID | None = None,
) -> StockLocation:
    return StockLocation(location_key=key, location_name=name, vessel_id=vessel_id)


def _item(
    *,
    item_reference: str = "INV-PAINT-001",
    name: str = "Marine paint",
    unit_of_measure: UnitOfMeasure | None = None,
    minimum_stock_level: Decimal | str | int | None = Decimal("2.0"),
) -> InventoryItem:
    return InventoryItem(
        item_reference=item_reference,
        name=name,
        unit_of_measure=unit_of_measure or _unit_litre(),
        description="Generic inventory item",
        minimum_stock_level=minimum_stock_level,
    )


def test_unit_of_measure_is_immutable_and_normalizes_code() -> None:
    unit = UnitOfMeasure(unit_code=" litre ", decimal_places=1, display_name=" litre ")

    assert unit.unit_code == "LITRE"
    assert unit.display_name == "litre"

    with pytest.raises(FrozenInstanceError):
        unit.unit_code = "PIECE"  # type: ignore[misc]


def test_unit_of_measure_rejects_invalid_decimal_places() -> None:
    with pytest.raises(InvalidUnitOfMeasureError):
        UnitOfMeasure(unit_code="PIECE", decimal_places=-1)


def test_stock_location_allows_optional_vessel_reference_only() -> None:
    vessel_id = uuid4()
    location = _location(vessel_id=vessel_id)

    assert location.vessel_id == vessel_id
    assert isinstance(location.vessel_id, UUID)


def test_stock_location_invalid_vessel_id_rejected() -> None:
    with pytest.raises(InvalidStockLocationError):
        StockLocation(
            location_key="VESSEL-LOCKER-1",
            location_name="Vessel Locker 1",
            vessel_id="invalid-uuid",
        )


def test_inventory_item_creation_emits_created_event() -> None:
    item = _item()
    events = item.pull_events()

    assert item.status is InventoryItemStatus.ACTIVE
    assert item.item_reference == "INV-PAINT-001"
    assert item.total_quantity == Decimal("0.0")
    assert any(isinstance(event, InventoryItemCreated) for event in events)


def test_inventory_item_reference_must_be_non_empty() -> None:
    with pytest.raises(InvalidInventoryReferenceError):
        _item(item_reference=" ")


def test_inventory_rejects_float_quantity_authority() -> None:
    item = _item()

    with pytest.raises(InvalidInventoryQuantityError):
        item.receive_stock(
            location=_location(),
            quantity=1.5,  # type: ignore[arg-type]
            occurred_at=_dt(2027, 1, 1),
        )


def test_receive_stock_creates_position_normalizes_quantity_and_emits_event() -> None:
    item = _item()
    item.pull_events()
    location = _location()

    movement = item.receive_stock(
        location=location,
        quantity="10.00",
        occurred_at=_dt(2027, 1, 1, 9),
        external_reference="PROC-100",
        note="Opening stock",
    )
    events = item.pull_events()

    assert item.quantity_at(location) == Decimal("10.0")
    assert item.total_quantity == Decimal("10.0")
    assert movement.movement_type is StockMovementType.RECEIPT
    assert movement.external_reference == "PROC-100"
    assert movement.note == "Opening stock"
    assert any(isinstance(event, StockReceived) for event in events)


def test_issue_stock_requires_sufficient_stock_at_location_and_emits_event() -> None:
    item = _item(unit_of_measure=_unit_piece(), minimum_stock_level=2)
    location = _location()
    item.receive_stock(location=location, quantity=5, occurred_at=_dt(2027, 1, 1, 8))
    item.pull_events()

    movement = item.issue_stock(
        location=location,
        quantity=2,
        occurred_at=_dt(2027, 1, 2, 10),
        external_reference="WO-200",
        note="Maintenance use",
    )
    events = item.pull_events()

    assert item.quantity_at(location) == Decimal("3")
    assert item.total_quantity == Decimal("3")
    assert movement.movement_type is StockMovementType.ISSUE
    assert movement.external_reference == "WO-200"
    assert any(isinstance(event, StockIssued) for event in events)


def test_issue_stock_cannot_make_quantity_negative() -> None:
    item = _item()
    location = _location()
    item.receive_stock(location=location, quantity="1.0", occurred_at=_dt(2027, 1, 1, 8))

    with pytest.raises(InsufficientStockError):
        item.issue_stock(
            location=location,
            quantity="2.0",
            occurred_at=_dt(2027, 1, 2, 9),
        )


def test_adjust_stock_to_count_records_explicit_decrease_and_reason() -> None:
    item = _item()
    location = _location()
    item.receive_stock(location=location, quantity="5.0", occurred_at=_dt(2027, 1, 1, 8))
    item.pull_events()

    movement = item.adjust_stock_to_count(
        location=location,
        counted_quantity="4.0",
        reason="Physical count correction",
        occurred_at=_dt(2027, 1, 3, 14),
        note="One litre missing",
    )
    events = item.pull_events()

    assert item.quantity_at(location) == Decimal("4.0")
    assert movement.movement_type is StockMovementType.ADJUSTMENT_DECREASE
    assert movement.quantity == Decimal("1.0")
    assert movement.reason == "Physical count correction"
    assert any(isinstance(event, StockAdjusted) for event in events)


def test_adjust_stock_requires_actual_change() -> None:
    item = _item()
    location = _location()
    item.receive_stock(location=location, quantity="4.0", occurred_at=_dt(2027, 1, 1, 8))

    with pytest.raises(InvalidInventoryAdjustmentError):
        item.adjust_stock_to_count(
            location=location,
            counted_quantity="4.0",
            reason="Counted",
            occurred_at=_dt(2027, 1, 2, 8),
        )


def test_item_cannot_change_stock_while_inactive() -> None:
    item = _item(unit_of_measure=_unit_piece(), minimum_stock_level=1)
    location = _location()
    item.pull_events()
    item.deactivate()

    with pytest.raises(InvalidInventoryLifecycleError):
        item.receive_stock(location=location, quantity=1, occurred_at=_dt(2027, 1, 1, 9))


def test_item_can_deactivate_only_when_total_quantity_zero_and_reactivate() -> None:
    item = _item(unit_of_measure=_unit_piece(), minimum_stock_level=1)
    item.pull_events()

    item.deactivate()
    deactivate_events = item.pull_events()
    item.reactivate()
    reactivate_events = item.pull_events()

    assert item.status is InventoryItemStatus.ACTIVE
    assert any(isinstance(event, InventoryItemDeactivated) for event in deactivate_events)
    assert any(isinstance(event, InventoryItemReactivated) for event in reactivate_events)


def test_deactivation_with_stock_is_rejected() -> None:
    item = _item(unit_of_measure=_unit_piece(), minimum_stock_level=1)
    location = _location()
    item.receive_stock(location=location, quantity=1, occurred_at=_dt(2027, 1, 1, 8))

    with pytest.raises(InvalidInventoryLifecycleError):
        item.deactivate()


def test_low_stock_is_derived_from_total_quantity() -> None:
    item = _item(unit_of_measure=_unit_piece(), minimum_stock_level=5)
    location_a = _location("LOCKER-A", "Locker A")
    location_b = _location("LOCKER-B", "Locker B")

    item.receive_stock(location=location_a, quantity=3, occurred_at=_dt(2027, 1, 1, 8))
    item.receive_stock(location=location_b, quantity=1, occurred_at=_dt(2027, 1, 1, 9))

    assert item.total_quantity == Decimal("4")
    assert item.low_stock is True


def test_multiple_locations_hold_separate_balances() -> None:
    item = _item(unit_of_measure=_unit_piece(), minimum_stock_level=1)
    location_a = _location("WORKSHOP", "Workshop")
    location_b = _location("VESSEL-STORE", "Vessel Store", vessel_id=uuid4())

    item.receive_stock(location=location_a, quantity=2, occurred_at=_dt(2027, 2, 1, 8))
    item.receive_stock(location=location_b, quantity=3, occurred_at=_dt(2027, 2, 1, 9))

    assert item.quantity_at(location_a) == Decimal("2")
    assert item.quantity_at(location_b) == Decimal("3")
    assert item.total_quantity == Decimal("5")


def test_stock_movements_require_timezone_aware_datetime() -> None:
    item = _item()

    with pytest.raises(Exception):
        item.receive_stock(
            location=_location(),
            quantity="1.0",
            occurred_at=datetime(2027, 1, 1, 8, 0),
        )


def test_mandatory_history_proof_explains_current_quantity() -> None:
    item = _item()
    location = _location("PAINT-SHELF", "Paint Shelf")
    item.pull_events()

    item.receive_stock(location=location, quantity="10.0", occurred_at=_dt(2027, 3, 1, 8))
    item.receive_stock(location=location, quantity="5.0", occurred_at=_dt(2027, 3, 2, 8))
    item.issue_stock(
        location=location,
        quantity="3.0",
        occurred_at=_dt(2027, 3, 3, 8),
        external_reference="WO-300",
    )
    item.adjust_stock_to_count(
        location=location,
        counted_quantity="11.0",
        reason="Physical count correction",
        occurred_at=_dt(2027, 3, 4, 8),
    )

    movement_types = [movement.movement_type for movement in item.movements]
    movement_quantities = [movement.quantity for movement in item.movements]

    assert movement_types == [
        StockMovementType.RECEIPT,
        StockMovementType.RECEIPT,
        StockMovementType.ISSUE,
        StockMovementType.ADJUSTMENT_DECREASE,
    ]
    assert movement_quantities == [
        Decimal("10.0"),
        Decimal("5.0"),
        Decimal("3.0"),
        Decimal("1.0"),
    ]
    assert item.explained_quantity_from_history() == Decimal("11.0")
    assert item.total_quantity == Decimal("11.0")


def test_maintenance_and_procurement_references_are_metadata_only() -> None:
    item = _item(unit_of_measure=_unit_piece(), minimum_stock_level=1)
    location = _location()
    receipt = item.receive_stock(
        location=location,
        quantity=4,
        occurred_at=_dt(2027, 4, 1, 8),
        external_reference="PROC-401",
    )
    issue = item.issue_stock(
        location=location,
        quantity=1,
        occurred_at=_dt(2027, 4, 2, 8),
        external_reference="WO-401",
    )

    assert receipt.external_reference == "PROC-401"
    assert issue.external_reference == "WO-401"
    assert item.total_quantity == Decimal("3")