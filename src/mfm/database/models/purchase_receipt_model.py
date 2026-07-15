"""SQLAlchemy ORM model for purchase order receipts."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.purchase_order_model import PurchaseOrderModel
    from mfm.database.models.purchase_receipt_line_model import PurchaseReceiptLineModel


class PurchaseReceiptModel(BaseModel):
    """Persistence model for immutable receipt records."""

    __tablename__ = "purchase_receipt"
    __table_args__ = (
        UniqueConstraint(
            "purchase_order_id",
            "receipt_order",
            name="uq_purchase_receipt_order",
        ),
    )

    purchase_order_id: Mapped[UUID] = mapped_column(
        ForeignKey("purchase_order.id"),
        nullable=False,
        index=True,
    )

    receipt_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    receipt_reference: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    received_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    purchase_order: Mapped["PurchaseOrderModel"] = relationship(
        "PurchaseOrderModel",
        back_populates="receipts",
    )

    lines: Mapped[list["PurchaseReceiptLineModel"]] = relationship(
        "PurchaseReceiptLineModel",
        back_populates="purchase_receipt",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="PurchaseReceiptLineModel.receipt_line_order",
    )
