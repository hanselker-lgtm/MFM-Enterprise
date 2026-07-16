"""SQLAlchemy ORM model for accounting fiscal periods."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.infrastructure.persistence.accounting.fiscal_year_model import FiscalYearModel


class FiscalPeriodModel(BaseModel):
    """Persistence model for FiscalPeriod child entity."""

    __tablename__ = "fiscal_period"
    __table_args__ = (
        UniqueConstraint(
            "fiscal_year_id",
            "number",
            name="uq_fiscal_period_number_per_year",
        ),
    )

    fiscal_year_id: Mapped[UUID] = mapped_column(
        ForeignKey("fiscal_year.id"),
        nullable=False,
        index=True,
    )

    number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    closed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    fiscal_year: Mapped["FiscalYearModel"] = relationship(
        "FiscalYearModel",
        back_populates="periods",
    )
