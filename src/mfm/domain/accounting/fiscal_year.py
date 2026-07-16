"""Fiscal year aggregate for accounting domain."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from datetime import timedelta
from typing import ClassVar
from uuid import UUID
from uuid import uuid4

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.accounting.exceptions import ClosedFiscalPeriodError
from mfm.domain.accounting.exceptions import DuplicateJournalNumberError
from mfm.domain.accounting.exceptions import InvalidFiscalPeriodError
from mfm.domain.accounting.exceptions import InvalidFiscalYearError
from mfm.domain.accounting.exceptions import InvalidFiscalYearTransitionError
from mfm.domain.accounting.exceptions import MultipleOpenFiscalYearsError
from mfm.domain.accounting.fiscal_period import FiscalPeriod
from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus


@dataclass(slots=True)
class FiscalYear(AggregateRoot):
    """Aggregate root representing a fiscal year and its periods."""

    year: int
    start_date: date
    end_date: date
    periods: list[FiscalPeriod]
    status: FiscalYearStatus = FiscalYearStatus.OPEN
    id: UUID = field(default_factory=uuid4)
    _journal_numbers: set[str] = field(default_factory=set, repr=False)

    _open_year_id: ClassVar[UUID | None] = None

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, UUID):
            raise InvalidFiscalYearError("id must be a UUID")

        if not isinstance(self.year, int) or self.year <= 0:
            raise InvalidFiscalYearError("year must be a positive integer")

        if not isinstance(self.start_date, date) or not isinstance(self.end_date, date):
            raise InvalidFiscalYearError("start_date and end_date must be dates")

        if self.start_date >= self.end_date:
            raise InvalidFiscalYearError("start_date must be before end_date")

        if not isinstance(self.status, FiscalYearStatus):
            raise InvalidFiscalYearError("status must be FiscalYearStatus")

        if not isinstance(self.periods, list) or not self.periods:
            raise InvalidFiscalYearError("periods must be a non-empty list")

        for period in self.periods:
            if not isinstance(period, FiscalPeriod):
                raise InvalidFiscalPeriodError("periods must contain FiscalPeriod")

        self._validate_periods()

        if self.status == FiscalYearStatus.OPEN:
            self._register_open_year()

    def open(self) -> None:
        if self.status == FiscalYearStatus.OPEN:
            raise InvalidFiscalYearTransitionError("fiscal year is already open")
        if self.status == FiscalYearStatus.ARCHIVED:
            raise InvalidFiscalYearTransitionError("archived fiscal year cannot be reopened")

        self._register_open_year()
        self.status = FiscalYearStatus.OPEN

    def close_period(self, period_number: int) -> None:
        self._assert_year_open_for_mutation()
        period = self._find_period(period_number)
        period.closed = True

    def reopen_period(self, period_number: int) -> None:
        self._assert_year_open_for_mutation()
        period = self._find_period(period_number)
        period.closed = False

    def close_year(self) -> None:
        if self.status != FiscalYearStatus.OPEN:
            raise InvalidFiscalYearTransitionError("only open fiscal year can be closed")

        if any(not period.closed for period in self.periods):
            raise InvalidFiscalYearTransitionError(
                "fiscal year can only be closed when all periods are closed"
            )

        self.status = FiscalYearStatus.CLOSED
        if FiscalYear._open_year_id == self.id:
            FiscalYear._open_year_id = None

    def reopen_year(self) -> None:
        if self.status != FiscalYearStatus.CLOSED:
            raise InvalidFiscalYearTransitionError("only closed fiscal year can be reopened")

        self._register_open_year()
        self.status = FiscalYearStatus.OPEN

    def contains(self, target_date: date) -> bool:
        return self.start_date <= target_date <= self.end_date

    def current_period(self, target_date: date) -> FiscalPeriod:
        for period in self.periods:
            if period.contains(target_date):
                if period.closed:
                    raise ClosedFiscalPeriodError("cannot post to a closed fiscal period")
                return period

        raise InvalidFiscalPeriodError("date is not within any fiscal period")

    def ensure_posting_allowed(self, posting_date: date) -> None:
        """Validate that posting is allowed for the provided accounting date."""
        if self.status == FiscalYearStatus.CLOSED:
            raise InvalidFiscalYearTransitionError("closed fiscal year rejects new journals")
        if self.status == FiscalYearStatus.ARCHIVED:
            raise InvalidFiscalYearTransitionError("archived fiscal year rejects new journals")
        self.current_period(posting_date)

    def register_journal_number(self, journal_number: str) -> str:
        """Register a unique journal number within this fiscal year."""
        if not isinstance(journal_number, str) or not journal_number.strip():
            raise InvalidFiscalYearError("journal_number must be a non-empty string")

        normalized = journal_number.strip().upper()
        if normalized in self._journal_numbers:
            raise DuplicateJournalNumberError(
                "journal numbers must be unique within fiscal year"
            )
        self._journal_numbers.add(normalized)
        return normalized

    def _find_period(self, period_number: int) -> FiscalPeriod:
        for period in self.periods:
            if period.number == period_number:
                return period
        raise InvalidFiscalPeriodError("period not found")

    def _validate_periods(self) -> None:
        sorted_periods = sorted(self.periods, key=lambda p: p.start_date)

        seen_numbers: set[int] = set()
        for period in sorted_periods:
            if period.number in seen_numbers:
                raise InvalidFiscalPeriodError("period numbers must be unique")
            seen_numbers.add(period.number)

        for index, period in enumerate(sorted_periods):
            if period.start_date < self.start_date or period.end_date > self.end_date:
                raise InvalidFiscalPeriodError(
                    "periods must be within fiscal year boundaries"
                )

            if index > 0:
                previous = sorted_periods[index - 1]
                if period.start_date <= previous.end_date:
                    raise InvalidFiscalPeriodError("fiscal periods must not overlap")
                if period.start_date != previous.end_date + timedelta(days=1):
                    raise InvalidFiscalPeriodError(
                        "fiscal periods must cover full fiscal year without gaps"
                    )

        if sorted_periods[0].start_date != self.start_date:
            raise InvalidFiscalPeriodError("periods must start at fiscal year start_date")

        if sorted_periods[-1].end_date != self.end_date:
            raise InvalidFiscalPeriodError("periods must end at fiscal year end_date")

    def _register_open_year(self) -> None:
        if FiscalYear._open_year_id is not None and FiscalYear._open_year_id != self.id:
            raise MultipleOpenFiscalYearsError("only one fiscal year can be open")
        FiscalYear._open_year_id = self.id

    def _assert_year_open_for_mutation(self) -> None:
        if self.status == FiscalYearStatus.CLOSED:
            raise InvalidFiscalYearTransitionError("closed fiscal year cannot be changed")
        if self.status == FiscalYearStatus.ARCHIVED:
            raise InvalidFiscalYearTransitionError("archived fiscal year cannot be changed")
