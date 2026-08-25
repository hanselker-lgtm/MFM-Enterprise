"""Invoice rule value object for contingent plans."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.exceptions import InvalidContingentReferenceError


@dataclass(frozen=True, slots=True)
class InvoiceRule:
    """How contingent plans should be invoiced."""

    billing_period: BillingPeriod
    due_days: int = 0
    prorate_on_start: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.billing_period, BillingPeriod):
            raise InvalidContingentReferenceError(
                "billing_period must be a BillingPeriod"
            )

        if not isinstance(self.due_days, int):
            raise InvalidContingentReferenceError("due_days must be an int")

        if self.due_days < 0:
            raise InvalidContingentReferenceError("due_days cannot be negative")
