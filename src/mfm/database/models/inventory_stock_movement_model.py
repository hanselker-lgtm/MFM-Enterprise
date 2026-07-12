"""SQLAlchemy ORM model for immutable inventory stock movements."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.inventory.stock_movement_type import StockMovementType

if TYPE_CHECKING:
    from mfm.database.models.inventory_item_model import InventoryItemModel


class InventoryStockMovementModel(BaseModel):
    """Persistence model for historical InventoryItem stock movements."""

    __tablename__ = "inventory_stock_movement"
    __table_args__ = (
        UniqueConstraint(
            "inventory_item_id",
            "movement_order",
            name="uq_inventory_stock_movement_item_order",
        ),
    )

    inventory_item_id: Mapped[UUID] = mapped_column(
        ForeignKey("inventory_item.id"),
        nullable=False,
        index=True,
    )

    movement_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True,
    )

    movement_type: Mapped[StockMovementType] = mapped_column(
        Enum(StockMovementType, native_enum=False, length=30),
        nullable=False,
    )

    quantity: Mapped[Decimal] = mapped_column(
        Numeric(24, 12),
        nullable=False,
    )

    occurred_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    location_key: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    location_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    vessel_id: Mapped[UUID | None] = mapped_column(
        nullable=True,
    )

    external_reference: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    note: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    reason: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    inventory_item: Mapped["InventoryItemModel"] = relationship(
        "InventoryItemModel",
        back_populates="movements",
    )
