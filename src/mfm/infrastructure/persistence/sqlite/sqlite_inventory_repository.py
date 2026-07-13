"""SQLite repository for InventoryItem aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.database.mappers.inventory_mapper import InventoryMapper
from mfm.database.models.inventory_item_model import InventoryItemModel
from mfm.database.models.inventory_stock_movement_model import InventoryStockMovementModel
from mfm.database.models.inventory_stock_position_model import InventoryStockPositionModel
from mfm.domain.inventory.inventory_item import InventoryItem
from mfm.repositories.inventory_repository import InventoryRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteInventoryRepository(InventoryRepository):
    """SQLAlchemy-backed repository for InventoryItem aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, item: InventoryItem) -> None:
        if self._session.scalar(
            select(InventoryItemModel).where(
                InventoryItemModel.item_reference == item.item_reference
            )
        ) is not None:
            raise ValueError(f"Inventory reference {item.item_reference} already exists")

        self._session.add(InventoryMapper.to_orm_inventory_item(item))
        self._session.flush()

    def get_by_id(self, inventory_item_id: UUID) -> InventoryItem | None:
        orm = self._session.scalar(
            select(InventoryItemModel)
            .options(
                joinedload(InventoryItemModel.positions),
                joinedload(InventoryItemModel.movements),
            )
            .where(InventoryItemModel.id == inventory_item_id)
        )
        if orm is None:
            return None
        return InventoryMapper.to_domain_inventory_item(orm)

    def get_by_reference(self, item_reference: str) -> InventoryItem | None:
        orm = self._session.scalar(
            select(InventoryItemModel)
            .options(
                joinedload(InventoryItemModel.positions),
                joinedload(InventoryItemModel.movements),
            )
            .where(InventoryItemModel.item_reference == item_reference)
        )
        if orm is None:
            return None
        return InventoryMapper.to_domain_inventory_item(orm)

    def update(self, item: InventoryItem) -> None:
        existing = self._session.scalar(
            select(InventoryItemModel)
            .options(
                joinedload(InventoryItemModel.positions),
                joinedload(InventoryItemModel.movements),
            )
            .where(InventoryItemModel.id == item.id.value)
        )
        if existing is None:
            raise ValueError(f"Inventory item {item.id.value} does not exist")

        duplicate = self._session.scalar(
            select(InventoryItemModel).where(
                InventoryItemModel.item_reference == item.item_reference,
                InventoryItemModel.id != item.id.value,
            )
        )
        if duplicate is not None:
            raise ValueError(f"Inventory reference {item.item_reference} already exists")

        existing.item_reference = item.item_reference
        existing.name = item.name
        existing.description = item.description
        existing.unit_code = item.unit_of_measure.unit_code
        existing.unit_decimal_places = item.unit_of_measure.decimal_places
        existing.unit_display_name = item.unit_of_measure.display_name
        existing.minimum_stock_level = item.minimum_stock_level
        existing.status = item.status

        existing.movements.clear()
        existing.positions.clear()

        # Flush orphan removals first so unique constraints do not conflict
        # when replacement rows are inserted for the same location key.
        self._session.flush()

        for position in item.positions:
            existing.positions.append(
                InventoryStockPositionModel(
                    inventory_item_id=item.id.value,
                    location_key=position.location.location_key,
                    location_name=position.location.location_name,
                    vessel_id=position.location.vessel_id,
                    quantity=position.quantity,
                )
            )

        for movement_order, movement in enumerate(item.movements):
            existing.movements.append(
                InventoryStockMovementModel(
                    id=movement.id.value,
                    inventory_item_id=item.id.value,
                    movement_order=movement_order,
                    movement_type=movement.movement_type,
                    quantity=movement.quantity,
                    occurred_at=movement.occurred_at,
                    location_key=movement.location.location_key,
                    location_name=movement.location.location_name,
                    vessel_id=movement.location.vessel_id,
                    external_reference=movement.external_reference,
                    note=movement.note,
                    reason=movement.reason,
                )
            )

        self._session.flush()

    def exists_by_reference(self, item_reference: str) -> bool:
        return self._session.scalar(
            select(InventoryItemModel.id).where(
                InventoryItemModel.item_reference == item_reference
            )
        ) is not None

    def list(self) -> list[InventoryItem]:
        orm_entities = self._session.scalars(
            select(InventoryItemModel)
            .options(
                joinedload(InventoryItemModel.positions),
                joinedload(InventoryItemModel.movements),
            )
            .order_by(
                InventoryItemModel.item_reference,
                InventoryItemModel.created_at,
            )
        ).unique().all()
        return [InventoryMapper.to_domain_inventory_item(orm) for orm in orm_entities]

    def get_low_stock(self) -> list[InventoryItem]:
        return [item for item in self.list() if item.low_stock]
