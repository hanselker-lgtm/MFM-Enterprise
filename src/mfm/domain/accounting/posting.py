"""Posting value object for accounting."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from mfm.common.value_object import ValueObject
from mfm.domain.accounting.exceptions import InvalidJournalLineError
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.money import Money


@dataclass(frozen=True, slots=True)
class Posting(ValueObject):
    """A posting amount on one side of a journal entry."""

    side: PostingSide
    amount: Money

    def __post_init__(self) -> None:
        if not isinstance(self.side, PostingSide):
            raise InvalidJournalLineError("side must be PostingSide")

        if not isinstance(self.amount, Money):
            raise InvalidJournalLineError("amount must be Money")

        if self.amount.amount <= Decimal("0"):
            raise InvalidJournalLineError("amount must be greater than zero")
