"""SQLAlchemy ORM model for accounting fiscal years."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus

if TYPE_CHECKING:
    from mfm.infrastructure.persistence.accounting.fiscal_period_model import FiscalPeriodModel
    from mfm.infrastructure.persistence.accounting.journal_model import JournalModel


class FiscalYearModel(BaseModel):
    """Persistence model for FiscalYear aggregate root."""

    __tablename__ = "fiscal_year"

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        unique=True,
        index=True,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[FiscalYearStatus] = mapped_column(
        Enum(FiscalYearStatus, native_enum=False, length=20),
        nullable=False,
        default=FiscalYearStatus.OPEN,
    )

    periods: Mapped[list["FiscalPeriodModel"]] = relationship(
        "FiscalPeriodModel",
        back_populates="fiscal_year",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="FiscalPeriodModel.number",
    )

    journals: Mapped[list["JournalModel"]] = relationship(
        "JournalModel",
        back_populates="fiscal_year",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="JournalModel.journal_number",
    )
