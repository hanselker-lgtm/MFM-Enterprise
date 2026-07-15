"""SQLAlchemy ORM model for purchase order lines."""

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
from mfm.domain.finance.currency import Currency

if TYPE_CHECKING:
    from mfm.database.models.purchase_order_model import PurchaseOrderModel
    from mfm.database.models.purchase_receipt_line_model import PurchaseReceiptLineModel


class PurchaseOrderLineModel(BaseModel):
    """Persistence model for line commitments on purchase orders."""

    __tablename__ = "purchase_order_line"
    __table_args__ = (
        UniqueConstraint(
            "purchase_order_id",
            "line_order",
            name="uq_purchase_order_line_order",
        ),
    )

    purchase_order_id: Mapped[UUID] = mapped_column(
        ForeignKey("purchase_order.id"),
        nullable=False,
        index=True,
    )

    line_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    description_snapshot: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    quantity: Mapped[Decimal] = mapped_column(
        Numeric(24, 12),
        nullable=False,
    )

    unit_price_amount: Mapped[Decimal] = mapped_column(
        Numeric(24, 2),
        nullable=False,
    )

    unit_price_currency: Mapped[Currency] = mapped_column(
        Enum(Currency, native_enum=False, length=10),
        nullable=False,
    )

    inventory_item_reference: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    expected_delivery_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    line_note: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    received_quantity: Mapped[Decimal] = mapped_column(
        Numeric(24, 12),
        nullable=False,
        default=Decimal("0"),
    )

    purchase_order: Mapped["PurchaseOrderModel"] = relationship(
        "PurchaseOrderModel",
        back_populates="lines",
    )

    receipt_lines: Mapped[list["PurchaseReceiptLineModel"]] = relationship(
        "PurchaseReceiptLineModel",
        back_populates="purchase_order_line",
    )
