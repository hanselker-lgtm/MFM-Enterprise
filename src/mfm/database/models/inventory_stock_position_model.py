"""SQLAlchemy ORM model for current inventory stock positions."""

from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.inventory_item_model import InventoryItemModel


class InventoryStockPositionModel(BaseModel):
    """Persistence model for InventoryItem location-scoped current balance."""

    __tablename__ = "inventory_stock_position"
    __table_args__ = (
        UniqueConstraint(
            "inventory_item_id",
            "location_key",
            name="uq_inventory_stock_position_item_location",
        ),
    )

    inventory_item_id: Mapped[UUID] = mapped_column(
        ForeignKey("inventory_item.id"),
        nullable=False,
        index=True,
    )

    location_key: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    location_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    vessel_id: Mapped[UUID | None] = mapped_column(
        nullable=True,
        index=True,
    )

    quantity: Mapped[Decimal] = mapped_column(
        Numeric(24, 12),
        nullable=False,
    )

    inventory_item: Mapped["InventoryItemModel"] = relationship(
        "InventoryItemModel",
        back_populates="positions",
    )
