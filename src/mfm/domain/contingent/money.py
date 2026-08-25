"""Money value object for contingent pricing."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from mfm.domain.contingent.currency import Currency
from mfm.domain.contingent.exceptions import (
    InvalidContingentAmountError,
    InvalidContingentReferenceError,
)


@dataclass(frozen=True, slots=True)
class Money:
    """Monetary value with currency and non-negative amount."""

    amount: Decimal
    currency: Currency

    def __post_init__(self) -> None:
        if not isinstance(self.currency, Currency):
            raise InvalidContingentReferenceError("currency must be a Currency")

        normalized_amount = Decimal(self.amount)
        if normalized_amount < Decimal("0"):
            raise InvalidContingentAmountError("amount cannot be negative")

        object.__setattr__(self, "amount", normalized_amount)
