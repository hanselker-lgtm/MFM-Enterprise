"""SQLAlchemy ORM models for the membership billing capability.

Replaces the previous ``SQLiteMembershipBillingRepository``, which
despite its name was not backed by SQLite at all -- it stored
profiles in a plain process-lifetime Python dict, so all fee
schedules, reminders, and billing history silently vanished on every
application restart.
"""

from __future__ import annotations

from datetime import date
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel


class MembershipFeeScheduleModel(BaseModel):
    """One fee schedule per membership type (1:1 with MembershipBillingProfile)."""

    __tablename__ = "membership_fee_schedule"

    membership_type_id: Mapped[UUID] = mapped_column(unique=True, index=True, nullable=False)
    membership_type_code: Mapped[str] = mapped_column(String(50), nullable=False)
    membership_type_name: Mapped[str] = mapped_column(String(255), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False)
    due_days: Mapped[int] = mapped_column(Integer, nullable=False)
    billing_period: Mapped[str] = mapped_column(String(20), nullable=False, default="YEARLY")
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    reminders: Mapped[list["MembershipBillingReminderModel"]] = relationship(
        back_populates="fee_schedule", cascade="all, delete-orphan"
    )
    runs: Mapped[list["MembershipBillingRunModel"]] = relationship(
        back_populates="fee_schedule", cascade="all, delete-orphan"
    )


class MembershipBillingReminderModel(BaseModel):
    """A payment reminder tied to a member and, optionally, an invoice."""

    __tablename__ = "membership_billing_reminder"

    fee_schedule_id: Mapped[UUID] = mapped_column(
        ForeignKey("membership_fee_schedule.id"), nullable=False, index=True
    )
    member_id: Mapped[UUID] = mapped_column(nullable=False, index=True)
    invoice_id: Mapped[UUID | None] = mapped_column(nullable=True)
    message: Mapped[str] = mapped_column(String(1000), nullable=False)
    due_date: Mapped[date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="PENDING")
    sent_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    fee_schedule: Mapped[MembershipFeeScheduleModel] = relationship(back_populates="reminders")


class MembershipBillingRunModel(BaseModel):
    """Historical record of one billing execution for a membership type."""

    __tablename__ = "membership_billing_run"

    fee_schedule_id: Mapped[UUID] = mapped_column(
        ForeignKey("membership_fee_schedule.id"), nullable=False, index=True
    )
    fiscal_year: Mapped[int] = mapped_column(Integer, nullable=False)
    billing_date: Mapped[date] = mapped_column(Date, nullable=False)
    processed: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    invoices_created: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    journals_created: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    skipped: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    errors: Mapped[str | None] = mapped_column(String(4000), nullable=True)

    fee_schedule: Mapped[MembershipFeeScheduleModel] = relationship(back_populates="runs")
