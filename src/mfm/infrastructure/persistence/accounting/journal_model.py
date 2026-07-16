"""SQLAlchemy ORM model for accounting journal aggregate root."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.journal_entry import JournalEntryStatus

if TYPE_CHECKING:
    from mfm.infrastructure.persistence.accounting.fiscal_year_model import FiscalYearModel
    from mfm.infrastructure.persistence.accounting.journal_entry_model import JournalEntryModel


class JournalModel(BaseModel):
    """Persistence model for Journal aggregate root."""

    __tablename__ = "journal"
    __table_args__ = (
        UniqueConstraint(
            "fiscal_year_id",
            "journal_number",
            name="uq_journal_number_within_fiscal_year",
        ),
    )

    fiscal_year_id: Mapped[UUID] = mapped_column(
        ForeignKey("fiscal_year.id"),
        nullable=False,
        index=True,
    )

    journal_number: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        index=True,
    )

    posting_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    description: Mapped[str] = mapped_column(
        String(2000),
        nullable=False,
    )

    reference: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    status: Mapped[JournalEntryStatus] = mapped_column(
        Enum(JournalEntryStatus, native_enum=False, length=20),
        nullable=False,
        default=JournalEntryStatus.DRAFT,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    fiscal_year: Mapped["FiscalYearModel"] = relationship(
        "FiscalYearModel",
        back_populates="journals",
    )

    entries: Mapped[list["JournalEntryModel"]] = relationship(
        "JournalEntryModel",
        back_populates="journal",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="JournalEntryModel.entry_order",
    )
