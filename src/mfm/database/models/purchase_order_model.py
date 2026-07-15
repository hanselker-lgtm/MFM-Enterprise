"""SQLAlchemy ORM model for procurement purchase orders."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.finance.currency import Currency
from mfm.domain.procurement.purchase_order_status import PurchaseOrderStatus

if TYPE_CHECKING:
    from mfm.database.models.purchase_order_line_model import PurchaseOrderLineModel
    from mfm.database.models.purchase_receipt_model import PurchaseReceiptModel


class PurchaseOrderModel(BaseModel):
    """Persistence model for PurchaseOrder aggregate root."""

    __tablename__ = "purchase_order"

    purchase_order_number: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True,
        index=True,
    )

    supplier_reference: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    status: Mapped[PurchaseOrderStatus] = mapped_column(
        Enum(PurchaseOrderStatus, native_enum=False, length=40),
        nullable=False,
        default=PurchaseOrderStatus.DRAFT,
    )

    currency: Mapped[Currency] = mapped_column(
        Enum(Currency, native_enum=False, length=10),
        nullable=False,
    )

    order_created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    supplier_name_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    supplier_contact_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        String(4000),
        nullable=True,
    )

    requested_by_reference: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    approved_by_reference: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    approved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    ordered_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    external_order_reference: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    cancelled_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    cancellation_reason: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    lines: Mapped[list["PurchaseOrderLineModel"]] = relationship(
        "PurchaseOrderLineModel",
        back_populates="purchase_order",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="PurchaseOrderLineModel.line_order",
    )

    receipts: Mapped[list["PurchaseReceiptModel"]] = relationship(
        "PurchaseReceiptModel",
        back_populates="purchase_order",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="PurchaseReceiptModel.receipt_order",
    )
