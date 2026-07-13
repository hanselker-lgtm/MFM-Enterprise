from __future__ import annotations

from datetime import UTC
from datetime import datetime
from decimal import Decimal
from pathlib import Path
import weakref
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.base_model import BaseModel
from mfm.domain.inventory.inventory_item import InventoryItem
from mfm.domain.inventory.stock_location import StockLocation
from mfm.domain.inventory.stock_movement_type import StockMovementType
from mfm.domain.inventory.unit_of_measure import UnitOfMeasure
from mfm.infrastructure.persistence.sqlite.sqlite_inventory_repository import (
    SQLiteInventoryRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


@pytest.fixture()
def sqlite_session(tmp_path: Path) -> Session:
    db_path = tmp_path / "sqlite-inventory-repository.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


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
    item_reference: str = "INV-REPO-001",
    minimum_stock_level: Decimal | str | int | None = Decimal("2.500"),
) -> InventoryItem:
    return InventoryItem(
        id=item_id or uuid4(),
        item_reference=item_reference,
        name="Marine Paint",
        description="Repository integration item",
        unit_of_measure=UnitOfMeasure(
            unit_code="LITRE",
            decimal_places=3,
            display_name="litre",
        ),
        minimum_stock_level=minimum_stock_level,
    )


def _aware(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, 0, tzinfo=UTC)


def _new_session(db_path: Path) -> Session:
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return session


def test_inventory_repository_add_and_get_by_id_roundtrip(sqlite_session: Session) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))
    item = _item(item_reference="INV-REPO-ADD")
    location = _location("STORE-A", "Store A")
    vessel_id = UUID("00000000-0000-0000-0000-00000000D401")

    item.receive_stock(
        location=_location("STORE-A", "Store A", vessel_id=vessel_id),
        quantity=Decimal("1.250"),
        occurred_at=_aware(2028, 1, 1, 8),
        external_reference="PROC-401",
        note="Initial receipt",
    )

    repository.add(item)
    sqlite_session.commit()

    restored = repository.get_by_id(item.id.value)
    assert restored is not None
    assert restored.id == item.id
    assert restored.item_reference == "INV-REPO-ADD"
    assert restored.total_quantity == Decimal("1.250")
    assert restored.positions[0].location.vessel_id == vessel_id
    assert restored.movements[0].external_reference == "PROC-401"
    assert restored.quantity_at(location) == Decimal("1.250")


def test_inventory_repository_get_by_id_missing_returns_none(sqlite_session: Session) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))

    missing = repository.get_by_id(UUID("00000000-0000-0000-0000-00000000EEEE"))

    assert missing is None


def test_inventory_repository_get_by_reference_and_exists_by_reference(sqlite_session: Session) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))
    item = _item(item_reference="INV-REPO-REF")

    repository.add(item)
    sqlite_session.commit()

    restored = repository.get_by_reference("INV-REPO-REF")
    missing = repository.get_by_reference("INV-REPO-NOT-FOUND")

    assert restored is not None
    assert restored.id == item.id
    assert missing is None
    assert repository.exists_by_reference("INV-REPO-REF") is True
    assert repository.exists_by_reference("INV-REPO-NOT-FOUND") is False


def test_inventory_repository_update_persists_historical_stock_truth(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-inventory-repository-history.sqlite"
    first_session = _new_session(db_path)
    item = _item(item_reference="INV-REPO-HISTORY", minimum_stock_level=Decimal("0.0"))
    try:
        repository = SQLiteInventoryRepository(UnitOfWork(first_session))
        location = _location("PAINT-SHELF", "Paint Shelf")

        item.receive_stock(
            location=location,
            quantity=Decimal("10.0"),
            occurred_at=_aware(2028, 2, 1, 8),
            note="START",
        )
        repository.add(item)
        first_session.commit()

        reloaded = repository.get_by_id(item.id.value)
        assert reloaded is not None

        reloaded.receive_stock(
            location=location,
            quantity=Decimal("5.0"),
            occurred_at=_aware(2028, 2, 2, 8),
            external_reference="PROC-502",
            note="RECEIVE",
        )
        reloaded.issue_stock(
            location=location,
            quantity=Decimal("3.0"),
            occurred_at=_aware(2028, 2, 3, 8),
            external_reference="WO-503",
            note="ISSUE",
        )
        reloaded.adjust_stock_to_count(
            location=location,
            counted_quantity=Decimal("11.0"),
            reason="Count correction",
            occurred_at=_aware(2028, 2, 4, 8),
            note="ADJUST",
        )

        repository.update(reloaded)
        first_session.commit()
    finally:
        first_session.close()

    reload_session = _new_session(db_path)
    try:
        reload_repository = SQLiteInventoryRepository(UnitOfWork(reload_session))
        restored = reload_repository.get_by_id(item.id.value)
        assert restored is not None

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
        reload_session.close()


def test_inventory_repository_movement_update_preserves_history_without_duplicates(
    sqlite_session: Session,
) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))
    item = _item(item_reference="INV-REPO-MOVES", minimum_stock_level=Decimal("0.0"))
    location = _location("STORE-A", "Store A")

    item.receive_stock(
        location=location,
        quantity=Decimal("2.000"),
        occurred_at=_aware(2028, 3, 1, 8),
        note="FIRST",
    )
    item.issue_stock(
        location=location,
        quantity=Decimal("1.000"),
        occurred_at=_aware(2028, 3, 1, 9),
        note="SECOND",
    )

    repository.add(item)
    sqlite_session.commit()

    first_reload = repository.get_by_id(item.id.value)
    assert first_reload is not None

    original_ids = [movement.id for movement in first_reload.movements]
    first_reload.adjust_stock_to_count(
        location=location,
        counted_quantity=Decimal("0.500"),
        reason="Cycle count",
        occurred_at=_aware(2028, 3, 1, 10),
        note="THIRD",
    )

    repository.update(first_reload)
    sqlite_session.commit()

    second_reload = repository.get_by_id(item.id.value)
    assert second_reload is not None

    assert len(second_reload.movements) == 3
    second_ids = [movement.id for movement in second_reload.movements]
    assert second_ids[:2] == original_ids
    assert len(set(second_ids)) == 3
    assert [movement.note for movement in second_reload.movements] == [
        "FIRST",
        "SECOND",
        "THIRD",
    ]


def test_inventory_repository_decimal_roundtrip_preserves_exact_decimal_type(
    sqlite_session: Session,
) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))
    item = _item(item_reference="INV-REPO-DECIMAL", minimum_stock_level=Decimal("0.375"))
    location = _location("STORE-A", "Store A")

    item.receive_stock(
        location=location,
        quantity=Decimal("10.125"),
        occurred_at=_aware(2028, 4, 1, 8),
    )
    item.issue_stock(
        location=location,
        quantity=Decimal("2.500"),
        occurred_at=_aware(2028, 4, 1, 9),
    )

    repository.add(item)
    sqlite_session.commit()

    restored = repository.get_by_id(item.id.value)
    assert restored is not None
    assert isinstance(restored.total_quantity, Decimal)
    assert restored.total_quantity == Decimal("7.625")
    assert restored.minimum_stock_level == Decimal("0.375")


def test_inventory_repository_get_low_stock_threshold_semantics(sqlite_session: Session) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))
    location = _location("STORE-A", "Store A")

    above = _item(item_reference="INV-REPO-ABOVE", minimum_stock_level=Decimal("2.500"))
    equal = _item(item_reference="INV-REPO-EQUAL", minimum_stock_level=Decimal("2.500"))
    below = _item(item_reference="INV-REPO-BELOW", minimum_stock_level=Decimal("2.500"))

    above.receive_stock(
        location=location,
        quantity=Decimal("3.000"),
        occurred_at=_aware(2028, 5, 1, 8),
    )
    equal.receive_stock(
        location=location,
        quantity=Decimal("2.500"),
        occurred_at=_aware(2028, 5, 1, 9),
    )
    below.receive_stock(
        location=location,
        quantity=Decimal("2.000"),
        occurred_at=_aware(2028, 5, 1, 10),
    )

    repository.add(above)
    repository.add(equal)
    repository.add(below)
    sqlite_session.commit()

    low_stock = repository.get_low_stock()
    low_stock_refs = {item.item_reference for item in low_stock}

    assert "INV-REPO-BELOW" in low_stock_refs
    assert "INV-REPO-EQUAL" not in low_stock_refs
    assert "INV-REPO-ABOVE" not in low_stock_refs


def test_inventory_repository_list_returns_domain_items_with_deterministic_order(
    sqlite_session: Session,
) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))

    first = _item(item_reference="INV-REPO-A")
    second = _item(item_reference="INV-REPO-B")
    third = _item(item_reference="INV-REPO-C")

    repository.add(second)
    repository.add(third)
    repository.add(first)
    sqlite_session.commit()

    listed = repository.list()
    assert [item.item_reference for item in listed] == [
        "INV-REPO-A",
        "INV-REPO-B",
        "INV-REPO-C",
    ]


def test_inventory_repository_duplicate_reference_raises_value_error(
    sqlite_session: Session,
) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))
    first = _item(item_reference="INV-REPO-DUP")
    duplicate = _item(item_reference="INV-REPO-DUP")

    repository.add(first)
    sqlite_session.commit()

    with pytest.raises(ValueError):
        repository.add(duplicate)


def test_inventory_repository_rollback_keeps_uncommitted_add_non_durable(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "sqlite-inventory-repository-rollback.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)

    first_session = Session(engine)
    try:
        repository = SQLiteInventoryRepository(UnitOfWork(first_session))
        item = _item(item_reference="INV-REPO-ROLLBACK")

        repository.add(item)
        first_session.rollback()
    finally:
        first_session.close()

    second_session = Session(engine)
    try:
        repository = SQLiteInventoryRepository(UnitOfWork(second_session))
        assert repository.get_by_reference("INV-REPO-ROLLBACK") is None
    finally:
        second_session.close()
        engine.dispose()


def test_inventory_repository_reload_does_not_emit_false_domain_events(
    sqlite_session: Session,
) -> None:
    repository = SQLiteInventoryRepository(UnitOfWork(sqlite_session))
    item = _item(item_reference="INV-REPO-EVENTS")

    item.receive_stock(
        location=_location("STORE-A", "Store A"),
        quantity=Decimal("1.000"),
        occurred_at=_aware(2028, 6, 1, 8),
    )
    item.pull_events()

    repository.add(item)
    sqlite_session.commit()

    restored = repository.get_by_id(item.id.value)
    assert restored is not None
    assert restored.pull_events() == []
