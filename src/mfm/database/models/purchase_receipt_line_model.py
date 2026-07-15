"""SQLAlchemy ORM model for receipt line quantities."""

from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.purchase_order_line_model import PurchaseOrderLineModel
    from mfm.database.models.purchase_receipt_model import PurchaseReceiptModel


class PurchaseReceiptLineModel(BaseModel):
    """Persistence model for quantities received per purchase order line."""

    __tablename__ = "purchase_receipt_line"
    __table_args__ = (
        UniqueConstraint(
            "purchase_receipt_id",
            "receipt_line_order",
            name="uq_purchase_receipt_line_order",
        ),
    )

    purchase_receipt_id: Mapped[UUID] = mapped_column(
        ForeignKey("purchase_receipt.id"),
        nullable=False,
        index=True,
    )

    purchase_order_line_id: Mapped[UUID] = mapped_column(
        ForeignKey("purchase_order_line.id"),
        nullable=False,
        index=True,
    )

    receipt_line_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    quantity: Mapped[Decimal] = mapped_column(
        Numeric(24, 12),
        nullable=False,
    )

    purchase_receipt: Mapped["PurchaseReceiptModel"] = relationship(
        "PurchaseReceiptModel",
        back_populates="lines",
    )

    purchase_order_line: Mapped["PurchaseOrderLineModel"] = relationship(
        "PurchaseOrderLineModel",
        back_populates="receipt_lines",
    )
