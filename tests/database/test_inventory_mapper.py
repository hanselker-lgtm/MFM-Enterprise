from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from decimal import Decimal
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.mappers.inventory_mapper import InventoryMapper
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.database.models.inventory_item_model import InventoryItemModel
from mfm.database.models.inventory_stock_movement_model import InventoryStockMovementModel
from mfm.domain.inventory.exceptions import InvalidInventoryLifecycleError
from mfm.domain.inventory.exceptions import InvalidStockMovementError
from mfm.domain.inventory.inventory_item import InventoryItem
from mfm.domain.inventory.inventory_item_status import InventoryItemStatus
from mfm.domain.inventory.stock_location import StockLocation
from mfm.domain.inventory.stock_movement_type import StockMovementType
from mfm.domain.inventory.unit_of_measure import UnitOfMeasure


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    return Session(engine)


def _close_session(session: Session) -> None:
    bind = session.get_bind()
    session.close()
    bind.dispose()


def _aware(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int = 0,
    *,
    offset_hours: int = 0,
) -> datetime:
    local_tz = timezone(timedelta(hours=offset_hours))
    return datetime(year, month, day, hour, minute, tzinfo=local_tz)


def _location(
    key: str,
    name: str,
    *,
    vessel_id: UUID | None = None,
) -> StockLocation:
    return StockLocation(location_key=key, location_name=name, vessel_id=vessel_id)


def _item(
    *,
    item_id: UUID | None = None,
    item_reference: str = "INV-PAINT-001",
    unit_code: str = "LITRE",
    decimal_places: int = 3,
    minimum_stock_level: Decimal | str | int | None = Decimal("2.500"),
) -> InventoryItem:
    unit = UnitOfMeasure(
        unit_code=unit_code,
        decimal_places=decimal_places,
        display_name=unit_code.lower(),
    )
    return InventoryItem(
        id=item_id or uuid4(),
        item_reference=item_reference,
        name="Generic inventory item",
        description="Inventory mapper roundtrip",
        unit_of_measure=unit,
        minimum_stock_level=minimum_stock_level,
    )


def _persist_and_reload(session: Session, item: InventoryItem) -> InventoryItem:
    orm = InventoryMapper.to_orm_inventory_item(item)
    session.add(orm)
    session.commit()
    session.expunge_all()

    loaded = session.get(InventoryItemModel, item.id.value)
    assert loaded is not None
    return InventoryMapper.to_domain_inventory_item(loaded)


def test_inventory_creation_roundtrip_persists_initial_state(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-create-roundtrip")
    try:
        item = _item()

        restored = _persist_and_reload(session, item)

        assert restored.id == item.id
        assert restored.item_reference == "INV-PAINT-001"
        assert restored.name == "Generic inventory item"
        assert restored.description == "Inventory mapper roundtrip"
        assert restored.status is InventoryItemStatus.ACTIVE
        assert restored.unit_of_measure.unit_code == "LITRE"
        assert restored.unit_of_measure.decimal_places == 3
        assert restored.minimum_stock_level == Decimal("2.500")
        assert restored.total_quantity == Decimal("0.000")
    finally:
        _close_session(session)


def test_quantity_decimal_roundtrip_preserves_domain_precision(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-quantity-roundtrip")
    try:
        item = _item(minimum_stock_level=Decimal("0.375"))
        location = _location("STORE-A", "Store A")

        item.receive_stock(
            location=location,
            quantity=Decimal("10.125"),
            occurred_at=_aware(2027, 1, 1, 8),
        )
        item.issue_stock(
            location=location,
            quantity=Decimal("2.500"),
            occurred_at=_aware(2027, 1, 2, 9),
        )

        restored = _persist_and_reload(session, item)

        assert isinstance(restored.total_quantity, Decimal)
        assert restored.total_quantity == Decimal("7.625")
        assert restored.minimum_stock_level == Decimal("0.375")
    finally:
        _close_session(session)


def test_unit_of_measure_roundtrip_preserves_exact_domain_representation(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-unit-roundtrip")
    try:
        item = _item(unit_code="METRE", decimal_places=2, minimum_stock_level=Decimal("1.00"))

        restored = _persist_and_reload(session, item)

        assert restored.unit_of_measure.unit_code == "METRE"
        assert restored.unit_of_measure.decimal_places == 2
        assert restored.unit_of_measure.display_name == "metre"
    finally:
        _close_session(session)


def test_stock_location_roundtrip_preserves_current_and_historical_context(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-location-roundtrip")
    try:
        vessel_id = UUID("00000000-0000-0000-0000-00000000D101")
        store_a = _location("STORE-A", "Store A", vessel_id=vessel_id)
        store_b = _location("STORE-B", "Store B", vessel_id=vessel_id)
        item = _item(minimum_stock_level=Decimal("0.000"))

        item.receive_stock(
            location=store_a,
            quantity=Decimal("5.000"),
            occurred_at=_aware(2027, 2, 1, 8),
        )
        item.issue_stock(
            location=store_a,
            quantity=Decimal("5.000"),
            occurred_at=_aware(2027, 2, 2, 8),
        )
        item.receive_stock(
            location=store_b,
            quantity=Decimal("5.000"),
            occurred_at=_aware(2027, 2, 3, 8),
        )

        restored = _persist_and_reload(session, item)

        assert restored.quantity_at(store_b) == Decimal("5.000")
        assert restored.quantity_at(store_a) == Decimal("0.000")
        assert restored.movements[0].location.location_key == "STORE-A"
        assert restored.movements[2].location.location_key == "STORE-B"
        assert restored.movements[0].location.vessel_id == vessel_id
    finally:
        _close_session(session)


def test_vessel_reference_roundtrip_keeps_opaque_identity_only(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-vessel-reference")
    try:
        vessel_id = UUID("00000000-0000-0000-0000-00000000D202")
        item = _item(minimum_stock_level=None)
        location = _location("VESSEL-LOCKER", "Vessel Locker", vessel_id=vessel_id)

        item.receive_stock(
            location=location,
            quantity=Decimal("1.000"),
            occurred_at=_aware(2027, 3, 1, 9),
        )

        restored = _persist_and_reload(session, item)

        assert restored.positions[0].location.vessel_id == vessel_id
        assert not hasattr(restored, "vessel")
    finally:
        _close_session(session)


def test_stock_movement_roundtrip_preserves_immutable_history_fields(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-movement-roundtrip")
    try:
        item = _item()
        location = _location("STORE-A", "Store A")

        item.receive_stock(
            location=location,
            quantity=Decimal("4.000"),
            occurred_at=_aware(2027, 4, 1, 8),
            external_reference="PROC-401",
            note="Receipt",
        )
        item.issue_stock(
            location=location,
            quantity=Decimal("1.000"),
            occurred_at=_aware(2027, 4, 2, 9),
            external_reference="WO-401",
            note="Issue",
        )
        item.adjust_stock_to_count(
            location=location,
            counted_quantity=Decimal("2.500"),
            reason="Physical count",
            occurred_at=_aware(2027, 4, 3, 10),
            note="Adjustment",
        )

        restored = _persist_and_reload(session, item)

        assert len(restored.movements) == 3
        assert restored.movements[0].movement_type is StockMovementType.RECEIPT
        assert restored.movements[0].external_reference == "PROC-401"
        assert restored.movements[1].movement_type is StockMovementType.ISSUE
        assert restored.movements[1].external_reference == "WO-401"
        assert restored.movements[2].movement_type is StockMovementType.ADJUSTMENT_DECREASE
        assert restored.movements[2].reason == "Physical count"
    finally:
        _close_session(session)


def test_movement_order_roundtrip_preserves_operation_order_not_timestamp_sort(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-movement-order")
    try:
        item = _item()
        location = _location("STORE-A", "Store A")

        item.receive_stock(
            location=location,
            quantity=Decimal("2.000"),
            occurred_at=_aware(2027, 5, 1, 12),
            note="First",
        )
        item.issue_stock(
            location=location,
            quantity=Decimal("1.000"),
            occurred_at=_aware(2027, 5, 1, 10),
            note="Second",
        )
        item.adjust_stock_to_count(
            location=location,
            counted_quantity=Decimal("0.500"),
            reason="Count",
            occurred_at=_aware(2027, 5, 1, 11),
            note="Third",
        )

        restored = _persist_and_reload(session, item)

        assert [movement.note for movement in restored.movements] == [
            "First",
            "Second",
            "Third",
        ]
        assert [movement.movement_type for movement in restored.movements] == [
            StockMovementType.RECEIPT,
            StockMovementType.ISSUE,
            StockMovementType.ADJUSTMENT_DECREASE,
        ]
    finally:
        _close_session(session)


def test_historical_stock_truth_roundtrip_mandatory_proof(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-historical-truth")
    try:
        item = _item(decimal_places=1, minimum_stock_level=Decimal("0.0"))
        location = _location("PAINT-SHELF", "Paint Shelf")

        item.receive_stock(
            location=location,
            quantity=Decimal("10.0"),
            occurred_at=_aware(2027, 6, 1, 8),
            note="START",
        )
        item.receive_stock(
            location=location,
            quantity=Decimal("5.0"),
            occurred_at=_aware(2027, 6, 2, 8),
            external_reference="PROC-502",
            note="RECEIVE",
        )
        item.issue_stock(
            location=location,
            quantity=Decimal("3.0"),
            occurred_at=_aware(2027, 6, 3, 8),
            external_reference="WO-503",
            note="ISSUE",
        )
        item.adjust_stock_to_count(
            location=location,
            counted_quantity=Decimal("11.0"),
            reason="Count correction",
            occurred_at=_aware(2027, 6, 4, 8),
            note="ADJUST",
        )

        restored = _persist_and_reload(session, item)

        assert restored.total_quantity == Decimal("11.0")
        assert [movement.movement_type for movement in restored.movements] == [
            StockMovementType.RECEIPT,
            StockMovementType.RECEIPT,
            StockMovementType.ISSUE,
            StockMovementType.ADJUSTMENT_DECREASE,
        ]
        assert [movement.quantity for movement in restored.movements] == [
            Decimal("10.0"),
            Decimal("5.0"),
            Decimal("3.0"),
            Decimal("1.0"),
        ]
        assert restored.movements[1].external_reference == "PROC-502"
        assert restored.movements[2].external_reference == "WO-503"
        assert restored.movements[3].reason == "Count correction"
        assert restored.explained_quantity_from_history() == Decimal("11.0")
    finally:
        _close_session(session)


def test_receipt_roundtrip_preserves_resulting_state_and_history(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-receipt-roundtrip")
    try:
        item = _item(decimal_places=3)
        location = _location("STORE-A", "Store A")
        item.receive_stock(
            location=location,
            quantity=Decimal("0.375"),
            occurred_at=_aware(2027, 7, 1, 8),
            external_reference="PROC-601",
            note="Receipt test",
        )

        restored = _persist_and_reload(session, item)

        assert restored.total_quantity == Decimal("0.375")
        assert restored.movements[0].movement_type is StockMovementType.RECEIPT
        assert restored.movements[0].quantity == Decimal("0.375")
        assert restored.movements[0].external_reference == "PROC-601"
        assert restored.movements[0].location.location_key == "STORE-A"
    finally:
        _close_session(session)


def test_issue_roundtrip_preserves_resulting_state_and_work_reference(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-issue-roundtrip")
    try:
        item = _item(decimal_places=3)
        location = _location("STORE-A", "Store A")
        item.receive_stock(
            location=location,
            quantity=Decimal("2.500"),
            occurred_at=_aware(2027, 8, 1, 8),
        )
        item.issue_stock(
            location=location,
            quantity=Decimal("0.375"),
            occurred_at=_aware(2027, 8, 2, 8),
            external_reference="WO-701",
            note="Issue test",
        )

        restored = _persist_and_reload(session, item)

        assert restored.total_quantity == Decimal("2.125")
        assert restored.movements[-1].movement_type is StockMovementType.ISSUE
        assert restored.movements[-1].quantity == Decimal("0.375")
        assert restored.movements[-1].external_reference == "WO-701"
    finally:
        _close_session(session)


def test_adjustment_roundtrip_preserves_delta_reason_and_result(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-adjust-roundtrip")
    try:
        item = _item(decimal_places=3)
        location = _location("STORE-A", "Store A")
        item.receive_stock(
            location=location,
            quantity=Decimal("2.500"),
            occurred_at=_aware(2027, 9, 1, 8),
        )
        item.adjust_stock_to_count(
            location=location,
            counted_quantity=Decimal("2.125"),
            reason="Cycle count",
            occurred_at=_aware(2027, 9, 2, 8),
            note="Adjustment test",
        )

        restored = _persist_and_reload(session, item)

        assert restored.total_quantity == Decimal("2.125")
        movement = restored.movements[-1]
        assert movement.movement_type is StockMovementType.ADJUSTMENT_DECREASE
        assert movement.quantity == Decimal("0.375")
        assert movement.reason == "Cycle count"
        assert movement.note == "Adjustment test"
    finally:
        _close_session(session)


def test_minimum_stock_roundtrip_absent_zero_positive_and_low_stock(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-minimum-stock")
    try:
        no_min = _item(item_id=UUID("00000000-0000-0000-0000-00000000E101"), minimum_stock_level=None)
        zero_min = _item(item_id=UUID("00000000-0000-0000-0000-00000000E102"), minimum_stock_level=Decimal("0.000"))
        positive_min = _item(item_id=UUID("00000000-0000-0000-0000-00000000E103"), minimum_stock_level=Decimal("2.500"))
        location = _location("STORE-A", "Store A")

        positive_min.receive_stock(
            location=location,
            quantity=Decimal("2.125"),
            occurred_at=_aware(2027, 10, 1, 8),
        )

        for candidate in (no_min, zero_min, positive_min):
            session.add(InventoryMapper.to_orm_inventory_item(candidate))
        session.commit()
        session.expunge_all()

        loaded_no_min = session.get(InventoryItemModel, no_min.id.value)
        loaded_zero_min = session.get(InventoryItemModel, zero_min.id.value)
        loaded_positive_min = session.get(InventoryItemModel, positive_min.id.value)
        assert loaded_no_min is not None
        assert loaded_zero_min is not None
        assert loaded_positive_min is not None

        restored_no_min = InventoryMapper.to_domain_inventory_item(loaded_no_min)
        restored_zero_min = InventoryMapper.to_domain_inventory_item(loaded_zero_min)
        restored_positive_min = InventoryMapper.to_domain_inventory_item(loaded_positive_min)

        assert restored_no_min.minimum_stock_level is None
        assert restored_no_min.low_stock is False
        assert restored_zero_min.minimum_stock_level == Decimal("0.000")
        assert restored_zero_min.low_stock is False
        assert restored_positive_min.minimum_stock_level == Decimal("2.500")
        assert restored_positive_min.total_quantity == Decimal("2.125")
        assert restored_positive_min.low_stock is True
    finally:
        _close_session(session)


def test_lifecycle_roundtrip_for_active_and_inactive_states(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-lifecycle-roundtrip")
    try:
        active = _item(item_id=UUID("00000000-0000-0000-0000-00000000F101"))
        inactive = _item(item_id=UUID("00000000-0000-0000-0000-00000000F102"))
        inactive.pull_events()
        inactive.deactivate()

        session.add(InventoryMapper.to_orm_inventory_item(active))
        session.add(InventoryMapper.to_orm_inventory_item(inactive))
        session.commit()
        session.expunge_all()

        loaded_active = session.get(InventoryItemModel, active.id.value)
        loaded_inactive = session.get(InventoryItemModel, inactive.id.value)
        assert loaded_active is not None
        assert loaded_inactive is not None

        restored_active = InventoryMapper.to_domain_inventory_item(loaded_active)
        restored_inactive = InventoryMapper.to_domain_inventory_item(loaded_inactive)

        assert restored_active.status is InventoryItemStatus.ACTIVE
        assert restored_inactive.status is InventoryItemStatus.INACTIVE
    finally:
        _close_session(session)


def test_external_reference_roundtrip_keeps_procurement_and_work_order_refs(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-external-reference")
    try:
        item = _item()
        location = _location("STORE-A", "Store A")
        item.receive_stock(
            location=location,
            quantity=Decimal("3.000"),
            occurred_at=_aware(2027, 11, 1, 8),
            external_reference="PROC-901",
        )
        item.issue_stock(
            location=location,
            quantity=Decimal("1.000"),
            occurred_at=_aware(2027, 11, 2, 8),
            external_reference="WO-901",
        )

        restored = _persist_and_reload(session, item)

        assert restored.movements[0].external_reference == "PROC-901"
        assert restored.movements[1].external_reference == "WO-901"
    finally:
        _close_session(session)


def test_timezone_roundtrip_preserves_utc_semantics(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-timezone-roundtrip")
    try:
        item = _item()
        location = _location("STORE-A", "Store A")

        item.receive_stock(
            location=location,
            quantity=Decimal("1.000"),
            occurred_at=_aware(2027, 12, 1, 10, offset_hours=2),
        )
        item.issue_stock(
            location=location,
            quantity=Decimal("0.500"),
            occurred_at=_aware(2027, 12, 1, 9, offset_hours=-3),
        )

        restored = _persist_and_reload(session, item)

        assert restored.movements[0].occurred_at.tzinfo is UTC
        assert restored.movements[1].occurred_at.tzinfo is UTC
        assert restored.movements[0].occurred_at == datetime(2027, 12, 1, 8, 0, tzinfo=UTC)
        assert restored.movements[1].occurred_at == datetime(2027, 12, 1, 12, 0, tzinfo=UTC)
    finally:
        _close_session(session)


def test_false_domain_event_restoration_no_new_history_events(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "inventory-false-events")
    try:
        item = _item()
        location = _location("STORE-A", "Store A")
        item.receive_stock(
            location=location,
            quantity=Decimal("2.000"),
            occurred_at=_aware(2028, 1, 1, 8),
        )
        item.issue_stock(
            location=location,
            quantity=Decimal("1.000"),
            occurred_at=_aware(2028, 1, 2, 8),
        )
        item.pull_events()

        restored = _persist_and_reload(session, item)

        assert restored.pull_events() == []
    finally:
        _close_session(session)


def test_invalid_persistence_state_unsupported_status_fails_domain_restore() -> None:
    orm = InventoryItemModel(
        id=UUID("00000000-0000-0000-0000-00000000AA01"),
        item_reference="INV-INVALID-1",
        name="Invalid status item",
        description=None,
        unit_code="PIECE",
        unit_decimal_places=0,
        unit_display_name="piece",
        minimum_stock_level=None,
        status="UNKNOWN",  # type: ignore[arg-type]
    )

    with pytest.raises(InvalidInventoryLifecycleError):
        InventoryMapper.to_domain_inventory_item(orm)


def test_invalid_persistence_state_unsupported_movement_type_fails_restore() -> None:
    orm = InventoryItemModel(
        id=UUID("00000000-0000-0000-0000-00000000AA02"),
        item_reference="INV-INVALID-2",
        name="Invalid movement type item",
        description=None,
        unit_code="PIECE",
        unit_decimal_places=0,
        unit_display_name="piece",
        minimum_stock_level=None,
        status=InventoryItemStatus.ACTIVE,
    )
    orm.movements.append(
        InventoryStockMovementModel(
            id=UUID("00000000-0000-0000-0000-00000000BB01"),
            inventory_item_id=orm.id,
            movement_order=0,
            movement_type="UNKNOWN",  # type: ignore[arg-type]
            quantity=Decimal("1"),
            occurred_at=datetime(2028, 2, 1, 8, tzinfo=UTC),
            location_key="STORE-A",
            location_name="Store A",
            vessel_id=None,
        )
    )

    with pytest.raises(InvalidStockMovementError):
        InventoryMapper.to_domain_inventory_item(orm)
