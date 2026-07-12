"""SQLAlchemy ORM model for inventory items."""

from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.inventory.inventory_item_status import InventoryItemStatus

if TYPE_CHECKING:
    from mfm.database.models.inventory_stock_movement_model import (
        InventoryStockMovementModel,
    )
    from mfm.database.models.inventory_stock_position_model import (
        InventoryStockPositionModel,
    )


class InventoryItemModel(BaseModel):
    """Persistence model for InventoryItem aggregate root."""

    __tablename__ = "inventory_item"

    item_reference: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    unit_code: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )

    unit_decimal_places: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    unit_display_name: Mapped[str | None] = mapped_column(
        String(120),
        nullable=True,
    )

    minimum_stock_level: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 12),
        nullable=True,
    )

    status: Mapped[InventoryItemStatus] = mapped_column(
        Enum(InventoryItemStatus, native_enum=False, length=20),
        nullable=False,
        default=InventoryItemStatus.ACTIVE,
    )

    positions: Mapped[list["InventoryStockPositionModel"]] = relationship(
        "InventoryStockPositionModel",
        back_populates="inventory_item",
        cascade="all, delete-orphan",
        single_parent=True,
    )

    movements: Mapped[list["InventoryStockMovementModel"]] = relationship(
        "InventoryStockMovementModel",
        back_populates="inventory_item",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="InventoryStockMovementModel.movement_order",
    )
