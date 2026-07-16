"""SQLAlchemy ORM model for accounting journal lines."""

from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.currency import Currency

if TYPE_CHECKING:
    from mfm.infrastructure.persistence.accounting.journal_entry_model import JournalEntryModel


class JournalLineModel(BaseModel):
    """Persistence model for JournalLine child rows."""

    __tablename__ = "journal_line"
    __table_args__ = (
        UniqueConstraint(
            "journal_entry_id",
            "line_order",
            name="uq_journal_line_order",
        ),
    )

    journal_entry_id: Mapped[UUID] = mapped_column(
        ForeignKey("journal_entry.id"),
        nullable=False,
        index=True,
    )

    line_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    account_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    side: Mapped[PostingSide] = mapped_column(
        Enum(PostingSide, native_enum=False, length=20),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(24, 2),
        nullable=False,
    )

    currency: Mapped[Currency] = mapped_column(
        Enum(Currency, native_enum=False, length=3),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    journal_entry: Mapped["JournalEntryModel"] = relationship(
        "JournalEntryModel",
        back_populates="lines",
    )
