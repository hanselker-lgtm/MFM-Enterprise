"""SQLAlchemy ORM model for accounting journal entries."""

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
    from mfm.infrastructure.persistence.accounting.journal_line_model import JournalLineModel
    from mfm.infrastructure.persistence.accounting.journal_model import JournalModel


class JournalEntryModel(BaseModel):
    """Persistence model for JournalEntry child records."""

    __tablename__ = "journal_entry"
    __table_args__ = (
        UniqueConstraint(
            "journal_id",
            "entry_order",
            name="uq_journal_entry_order",
        ),
    )

    journal_id: Mapped[UUID] = mapped_column(
        ForeignKey("journal.id"),
        nullable=False,
        index=True,
    )

    entry_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    posting_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
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

    journal: Mapped["JournalModel"] = relationship(
        "JournalModel",
        back_populates="entries",
    )

    lines: Mapped[list["JournalLineModel"]] = relationship(
        "JournalLineModel",
        back_populates="journal_entry",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="JournalLineModel.line_order",
    )
