"""SQLAlchemy ORM models for member invoices (finance domain).

Backs :class:`mfm.domain.finance.invoice.Invoice`. Previously had no
persistence at all -- the annual contingent billing feature
(:mod:`mfm.application.features.annual_contingent_generation`) could
not run because there was nowhere to store the invoices it creates.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel


class InvoiceModel(BaseModel):
    """Persistence model for the Invoice aggregate root."""

    __tablename__ = "invoice"

    invoice_number: Mapped[str] = mapped_column(String(60), unique=True, index=True, nullable=False)
    member_id: Mapped[UUID] = mapped_column(nullable=False, index=True)
    issue_date: Mapped[date] = mapped_column(Date, nullable=False)
    due_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="DRAFT")
    paid_amount: Mapped[Decimal | None] = mapped_column(Numeric(18, 2), nullable=True)
    paid_currency: Mapped[str | None] = mapped_column(String(3), nullable=True)

    lines: Mapped[list["InvoiceLineModel"]] = relationship(
        back_populates="invoice", cascade="all, delete-orphan", order_by="InvoiceLineModel.line_order"
    )


class InvoiceLineModel(BaseModel):
    """A single line on an invoice."""

    __tablename__ = "invoice_line"

    invoice_id: Mapped[UUID] = mapped_column(ForeignKey("invoice.id"), nullable=False, index=True)
    line_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    quantity: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    unit_price_amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    unit_price_currency: Mapped[str] = mapped_column(String(3), nullable=False)

    invoice: Mapped[InvoiceModel] = relationship(back_populates="lines")
