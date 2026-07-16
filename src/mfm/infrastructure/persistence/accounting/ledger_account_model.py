"""SQLAlchemy ORM model for accounting ledger accounts."""

from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.account_type import AccountType
from mfm.domain.accounting.normal_balance import NormalBalance


class LedgerAccountModel(BaseModel):
    """Persistence model for LedgerAccount aggregate root."""

    __tablename__ = "ledger_account"

    account_number: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    account_type: Mapped[AccountType] = mapped_column(
        Enum(AccountType, native_enum=False, length=20),
        nullable=False,
    )

    normal_balance: Mapped[NormalBalance] = mapped_column(
        Enum(NormalBalance, native_enum=False, length=20),
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    locked: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    has_postings: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )
