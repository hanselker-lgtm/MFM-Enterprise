"""Journal line value object for accounting."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from mfm.common.value_object import ValueObject
from mfm.domain.accounting.exceptions import InvalidJournalLineError
from mfm.domain.accounting.posting import Posting
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.money import Money


@dataclass(frozen=True, slots=True)
class JournalLine(ValueObject):
    """A single journal line with account and posting details."""

    account_id: UUID
    side: PostingSide
    amount: Money
    description: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.account_id, UUID):
            raise InvalidJournalLineError("account_id must be a UUID")

        if self.description is not None:
            if not isinstance(self.description, str):
                raise InvalidJournalLineError("description must be a string")
            normalized = self.description.strip()
            object.__setattr__(self, "description", normalized or None)

        Posting(side=self.side, amount=self.amount)

        if self.amount.amount <= Decimal("0"):
            raise InvalidJournalLineError("amount must be greater than zero")
