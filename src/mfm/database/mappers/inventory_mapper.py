"""Mapper between inventory domain and persistence models."""

from __future__ import annotations

from datetime import UTC
from datetime import datetime

from mfm.database.models.inventory_item_model import InventoryItemModel
from mfm.database.models.inventory_stock_movement_model import InventoryStockMovementModel
from mfm.database.models.inventory_stock_position_model import InventoryStockPositionModel
from mfm.domain.inventory.identifiers import InventoryItemId
from mfm.domain.inventory.identifiers import StockMovementId
from mfm.domain.inventory.inventory_item import InventoryItem
from mfm.domain.inventory.stock_location import StockLocation
from mfm.domain.inventory.stock_movement import StockMovement
from mfm.domain.inventory.stock_position import StockPosition
from mfm.domain.inventory.unit_of_measure import UnitOfMeasure


class InventoryMapper:
    """Map InventoryItem aggregate to/from SQLAlchemy models."""

    @staticmethod
    def to_orm_inventory_item(item: InventoryItem) -> InventoryItemModel:
        orm = InventoryItemModel(
            id=item.id.value,
            item_reference=item.item_reference,
            name=item.name,
            description=item.description,
            unit_code=item.unit_of_measure.unit_code,
            unit_decimal_places=item.unit_of_measure.decimal_places,
            unit_display_name=item.unit_of_measure.display_name,
            minimum_stock_level=item.minimum_stock_level,
            status=item.status,
        )

        for position in item.positions:
            orm.positions.append(
                InventoryStockPositionModel(
                    inventory_item_id=item.id.value,
                    location_key=position.location.location_key,
                    location_name=position.location.location_name,
                    vessel_id=position.location.vessel_id,
                    quantity=position.quantity,
                )
            )

        for movement_order, movement in enumerate(item.movements):
            orm.movements.append(
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

        return orm

    @staticmethod
    def to_domain_inventory_item(orm: InventoryItemModel) -> InventoryItem:
        unit = UnitOfMeasure(
            unit_code=orm.unit_code,
            decimal_places=orm.unit_decimal_places,
            display_name=orm.unit_display_name,
        )

        item = InventoryItem(
            id=InventoryItemId(orm.id),
            item_reference=orm.item_reference,
            name=orm.name,
            unit_of_measure=unit,
            status=orm.status,
            description=orm.description,
            minimum_stock_level=orm.minimum_stock_level,
        )

        item._positions.clear()
        item._movements.clear()

        for position_orm in orm.positions:
            location = StockLocation(
                location_key=position_orm.location_key,
                location_name=position_orm.location_name,
                vessel_id=position_orm.vessel_id,
            )
            item._positions[location.location_key] = StockPosition(
                location=location,
                quantity=unit.normalize_quantity(position_orm.quantity),
            )

        ordered_movements = sorted(orm.movements, key=lambda movement: movement.movement_order)
        for movement_orm in ordered_movements:
            item._movements.append(
                StockMovement(
                    id=StockMovementId(movement_orm.id),
                    movement_type=movement_orm.movement_type,
                    quantity=unit.normalize_quantity(movement_orm.quantity),
                    location=StockLocation(
                        location_key=movement_orm.location_key,
                        location_name=movement_orm.location_name,
                        vessel_id=movement_orm.vessel_id,
                    ),
                    occurred_at=InventoryMapper._normalize_timestamp(movement_orm.occurred_at),
                    external_reference=movement_orm.external_reference,
                    note=movement_orm.note,
                    reason=movement_orm.reason,
                )
            )

        item.pull_events()
        return item

    @staticmethod
    def _normalize_timestamp(value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)
