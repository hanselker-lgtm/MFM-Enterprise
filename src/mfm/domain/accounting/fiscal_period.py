"""Fiscal period model for accounting domain."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from mfm.domain.accounting.exceptions import InvalidFiscalPeriodError


@dataclass(slots=True)
class FiscalPeriod:
    """A period within a fiscal year."""

    number: int
    start_date: date
    end_date: date
    closed: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.number, int) or self.number <= 0:
            raise InvalidFiscalPeriodError("period number must be a positive integer")

        if not isinstance(self.start_date, date) or not isinstance(self.end_date, date):
            raise InvalidFiscalPeriodError("period start_date and end_date must be dates")

        if self.start_date >= self.end_date:
            raise InvalidFiscalPeriodError("period start_date must be before end_date")

    def contains(self, target_date: date) -> bool:
        return self.start_date <= target_date <= self.end_date
