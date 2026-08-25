"""SQLAlchemy ORM model for contingent plans."""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from mfm.database.models.base_model import BaseModel
from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.currency import Currency


class ContingentPlanModel(BaseModel):
    """Persistence model for contingent plans."""

    __tablename__ = "contingent_plan"

    membership_type_id: Mapped[UUID] = mapped_column(
        ForeignKey("membership_type.id"),
        nullable=False,
        index=True,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    currency: Mapped[Currency] = mapped_column(
        Enum(Currency, native_enum=False, length=10),
        nullable=False,
    )

    billing_period: Mapped[BillingPeriod] = mapped_column(
        Enum(BillingPeriod, native_enum=False, length=20),
        nullable=False,
    )

    due_days: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    prorate_on_start: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
    )

    valid_from: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    valid_to: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )
