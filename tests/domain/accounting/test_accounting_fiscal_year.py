from datetime import date

import pytest

from mfm.domain.accounting.exceptions import ClosedFiscalPeriodError
from mfm.domain.accounting.exceptions import InvalidFiscalPeriodError
from mfm.domain.accounting.exceptions import InvalidFiscalYearError
from mfm.domain.accounting.exceptions import InvalidFiscalYearTransitionError
from mfm.domain.accounting.exceptions import MultipleOpenFiscalYearsError
from mfm.domain.accounting.fiscal_period import FiscalPeriod
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money


@pytest.fixture(autouse=True)
def _reset_open_fiscal_year_registry():
    FiscalYear._open_year_id = None
    yield
    FiscalYear._open_year_id = None


def _monthly_periods_2026() -> list[FiscalPeriod]:
    return [
        FiscalPeriod(number=1, start_date=date(2026, 1, 1), end_date=date(2026, 1, 31)),
        FiscalPeriod(number=2, start_date=date(2026, 2, 1), end_date=date(2026, 2, 28)),
        FiscalPeriod(number=3, start_date=date(2026, 3, 1), end_date=date(2026, 3, 31)),
    ]


def _fiscal_year() -> FiscalYear:
    return FiscalYear(
        year=2026,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
        status=FiscalYearStatus.OPEN,
        periods=_monthly_periods_2026(),
    )


def test_create_fiscal_year():
    year = _fiscal_year()

    assert year.year == 2026
    assert year.status == FiscalYearStatus.OPEN
    assert len(year.periods) == 3


def test_overlapping_periods_are_rejected():
    periods = [
        FiscalPeriod(number=1, start_date=date(2026, 1, 1), end_date=date(2026, 1, 31)),
        FiscalPeriod(number=2, start_date=date(2026, 1, 31), end_date=date(2026, 2, 28)),
    ]

    with pytest.raises(InvalidFiscalPeriodError):
        FiscalYear(
            year=2026,
            start_date=date(2026, 1, 1),
            end_date=date(2026, 2, 28),
            periods=periods,
        )


def test_invalid_dates_are_rejected():
    with pytest.raises(InvalidFiscalYearError):
        FiscalYear(
            year=2026,
            start_date=date(2026, 3, 31),
            end_date=date(2026, 1, 1),
            periods=_monthly_periods_2026(),
        )


def test_close_and_reopen_period():
    year = _fiscal_year()

    year.close_period(1)
    assert year.periods[0].closed is True

    year.reopen_period(1)
    assert year.periods[0].closed is False


def test_close_year_requires_all_periods_closed():
    year = _fiscal_year()

    with pytest.raises(InvalidFiscalYearTransitionError):
        year.close_year()

    year.close_period(1)
    year.close_period(2)
    year.close_period(3)
    year.close_year()

    assert year.status == FiscalYearStatus.CLOSED


def test_reopen_year():
    year = _fiscal_year()
    year.close_period(1)
    year.close_period(2)
    year.close_period(3)
    year.close_year()

    year.reopen_year()

    assert year.status == FiscalYearStatus.OPEN


def test_current_period_and_closed_period_posting_rule():
    year = _fiscal_year()

    period = year.current_period(date(2026, 2, 15))
    assert period.number == 2

    year.close_period(2)
    with pytest.raises(ClosedFiscalPeriodError):
        year.current_period(date(2026, 2, 15))


def test_contains_date():
    year = _fiscal_year()

    assert year.contains(date(2026, 1, 1)) is True
    assert year.contains(date(2026, 3, 31)) is True
    assert year.contains(date(2025, 12, 31)) is False
    assert year.contains(date(2026, 4, 1)) is False


def test_invalid_transitions():
    year = _fiscal_year()

    with pytest.raises(InvalidFiscalYearTransitionError):
        year.open()

    with pytest.raises(InvalidFiscalYearTransitionError):
        year.reopen_year()

    year.close_period(1)
    year.close_period(2)
    year.close_period(3)
    year.close_year()

    with pytest.raises(InvalidFiscalYearTransitionError):
        year.close_period(1)


def test_only_one_open_fiscal_year():
    first = _fiscal_year()

    with pytest.raises(MultipleOpenFiscalYearsError):
        FiscalYear(
            year=2027,
            start_date=date(2027, 1, 1),
            end_date=date(2027, 3, 31),
            periods=[
                FiscalPeriod(number=1, start_date=date(2027, 1, 1), end_date=date(2027, 1, 31)),
                FiscalPeriod(number=2, start_date=date(2027, 2, 1), end_date=date(2027, 2, 28)),
                FiscalPeriod(number=3, start_date=date(2027, 3, 1), end_date=date(2027, 3, 31)),
            ],
            status=FiscalYearStatus.OPEN,
        )

    first.close_period(1)
    first.close_period(2)
    first.close_period(3)
    first.close_year()

    second = FiscalYear(
        year=2027,
        start_date=date(2027, 1, 1),
        end_date=date(2027, 3, 31),
        periods=[
            FiscalPeriod(number=1, start_date=date(2027, 1, 1), end_date=date(2027, 1, 31)),
            FiscalPeriod(number=2, start_date=date(2027, 2, 1), end_date=date(2027, 2, 28)),
            FiscalPeriod(number=3, start_date=date(2027, 3, 1), end_date=date(2027, 3, 31)),
        ],
        status=FiscalYearStatus.OPEN,
    )
    assert second.status == FiscalYearStatus.OPEN


def test_fiscal_year_status_values():
    assert FiscalYearStatus.OPEN.value == "OPEN"
    assert FiscalYearStatus.CLOSED.value == "CLOSED"
    assert FiscalYearStatus.ARCHIVED.value == "ARCHIVED"


def test_closed_fiscal_year_rejects_new_journals():
    year = _fiscal_year()
    year.close_period(1)
    year.close_period(2)
    year.close_period(3)
    year.close_year()

    with pytest.raises(InvalidFiscalYearTransitionError):
        JournalEntry.create_for_fiscal_year(
            fiscal_year=year,
            journal_number="JRN-2026-0900",
            posting_date=date(2026, 1, 20),
            description="Closed year posting",
            lines=[
                JournalLine(
                    account_id=year.id,
                    side=PostingSide.DEBIT,
                    amount=Money(amount="10.00", currency=Currency.DKK),
                ),
                JournalLine(
                    account_id=year.id,
                    side=PostingSide.CREDIT,
                    amount=Money(amount="10.00", currency=Currency.DKK),
                ),
            ],
        )
