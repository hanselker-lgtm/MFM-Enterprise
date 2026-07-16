from datetime import date
from decimal import Decimal
from uuid import uuid4

import pytest

from mfm.domain.accounting.exceptions import InvalidJournalBalanceError
from mfm.domain.accounting.exceptions import DuplicateJournalNumberError
from mfm.domain.accounting.exceptions import ClosedFiscalPeriodError
from mfm.domain.accounting.exceptions import InvalidJournalLineError
from mfm.domain.accounting.exceptions import InvalidJournalTransitionError
from mfm.domain.accounting.fiscal_period import FiscalPeriod
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.journal import Journal
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.accounting.journal_entry import JournalEntryStatus
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money


def _line(*, side: PostingSide, amount: str, description: str = "") -> JournalLine:
    return JournalLine(
        account_id=uuid4(),
        side=side,
        amount=Money(amount=Decimal(amount), currency=Currency.DKK),
        description=description,
    )


def _balanced_journal() -> JournalEntry:
    return JournalEntry(
        journal_number="jrn-2026-0001",
        posting_date=date(2026, 1, 15),
        description="Membership invoicing",
        reference="INV-2026-0001",
        lines=[
            _line(side=PostingSide.DEBIT, amount="100.00", description="Receivable"),
            _line(side=PostingSide.CREDIT, amount="100.00", description="Revenue"),
        ],
    )


@pytest.fixture(autouse=True)
def _reset_open_fiscal_year_registry():
    FiscalYear._open_year_id = None
    yield
    FiscalYear._open_year_id = None


def _fiscal_year() -> FiscalYear:
    return FiscalYear(
        year=2026,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
        periods=[
            FiscalPeriod(number=1, start_date=date(2026, 1, 1), end_date=date(2026, 1, 31)),
            FiscalPeriod(number=2, start_date=date(2026, 2, 1), end_date=date(2026, 2, 28)),
            FiscalPeriod(number=3, start_date=date(2026, 3, 1), end_date=date(2026, 3, 31)),
        ],
    )


def test_balanced_journal_is_valid_and_totals_match():
    journal = _balanced_journal()

    assert journal.journal_number == "JRN-2026-0001"
    assert journal.is_balanced() is True
    assert journal.total_debit() == Money(amount=Decimal("100.00"), currency=Currency.DKK)
    assert journal.total_credit() == Money(amount=Decimal("100.00"), currency=Currency.DKK)


def test_unbalanced_journal_is_rejected():
    with pytest.raises(InvalidJournalBalanceError):
        JournalEntry(
            journal_number="JRN-2026-0002",
            posting_date=date(2026, 1, 15),
            description="Unbalanced",
            lines=[
                _line(side=PostingSide.DEBIT, amount="100.00"),
                _line(side=PostingSide.CREDIT, amount="90.00"),
            ],
        )


def test_post_changes_status_to_posted():
    journal = _balanced_journal()

    journal.post()

    assert journal.status == JournalEntryStatus.POSTED


def test_reverse_changes_status_from_posted_to_reversed():
    journal = _balanced_journal()
    journal.post()

    journal.reverse()

    assert journal.status == JournalEntryStatus.REVERSED


def test_invalid_transitions():
    journal = _balanced_journal()

    with pytest.raises(InvalidJournalTransitionError):
        journal.reverse()

    journal.post()

    with pytest.raises(InvalidJournalTransitionError):
        journal.add_line(_line(side=PostingSide.DEBIT, amount="10.00"))

    with pytest.raises(InvalidJournalTransitionError):
        journal.remove_line(journal.lines[0])

    journal.reverse()

    with pytest.raises(InvalidJournalTransitionError):
        journal.post()


def test_remove_lines_but_not_below_two():
    first = _line(side=PostingSide.DEBIT, amount="50.00")
    second = _line(side=PostingSide.DEBIT, amount="50.00")
    third = _line(side=PostingSide.CREDIT, amount="100.00")
    journal = JournalEntry(
        journal_number="JRN-2026-0003",
        posting_date=date(2026, 1, 16),
        description="Three lines",
        lines=[first, second, third],
    )

    journal.remove_line(second)
    assert len(journal.lines) == 2

    with pytest.raises(InvalidJournalLineError):
        journal.remove_line(first)


def test_multiple_debit_credit_lines_balance_correctly():
    journal = JournalEntry(
        journal_number="JRN-2026-0004",
        posting_date=date(2026, 1, 17),
        description="Split posting",
        lines=[
            _line(side=PostingSide.DEBIT, amount="70.00"),
            _line(side=PostingSide.DEBIT, amount="30.00"),
            _line(side=PostingSide.CREDIT, amount="60.00"),
            _line(side=PostingSide.CREDIT, amount="40.00"),
        ],
    )

    assert journal.total_debit() == Money(amount=Decimal("100.00"), currency=Currency.DKK)
    assert journal.total_credit() == Money(amount=Decimal("100.00"), currency=Currency.DKK)
    assert journal.is_balanced() is True


def test_zero_amount_line_is_rejected():
    with pytest.raises(InvalidJournalLineError):
        _line(side=PostingSide.DEBIT, amount="0.00")


def test_negative_amount_line_is_rejected():
    with pytest.raises(InvalidJournalLineError):
        _line(side=PostingSide.CREDIT, amount="-1.00")


def test_posting_side_values():
    assert PostingSide.DEBIT.value == "DEBIT"
    assert PostingSide.CREDIT.value == "CREDIT"


def test_journal_alias_class_works():
    journal = Journal(
        journal_number="JRN-2026-0005",
        posting_date=date(2026, 1, 18),
        description="Alias class",
        lines=[
            _line(side=PostingSide.DEBIT, amount="10.00"),
            _line(side=PostingSide.CREDIT, amount="10.00"),
        ],
    )

    assert isinstance(journal, JournalEntry)


def test_create_for_fiscal_year_requires_unique_journal_number_within_year():
    fiscal_year = _fiscal_year()

    JournalEntry.create_for_fiscal_year(
        fiscal_year=fiscal_year,
        journal_number="JRN-2026-0100",
        posting_date=date(2026, 1, 10),
        description="First",
        lines=[
            _line(side=PostingSide.DEBIT, amount="10.00"),
            _line(side=PostingSide.CREDIT, amount="10.00"),
        ],
    )

    with pytest.raises(DuplicateJournalNumberError):
        JournalEntry.create_for_fiscal_year(
            fiscal_year=fiscal_year,
            journal_number="jrn-2026-0100",
            posting_date=date(2026, 1, 11),
            description="Duplicate",
            lines=[
                _line(side=PostingSide.DEBIT, amount="20.00"),
                _line(side=PostingSide.CREDIT, amount="20.00"),
            ],
        )


def test_create_for_fiscal_year_rejects_closed_period_postings():
    fiscal_year = _fiscal_year()
    fiscal_year.close_period(2)

    with pytest.raises(ClosedFiscalPeriodError):
        JournalEntry.create_for_fiscal_year(
            fiscal_year=fiscal_year,
            journal_number="JRN-2026-0200",
            posting_date=date(2026, 2, 10),
            description="Closed period posting",
            lines=[
                _line(side=PostingSide.DEBIT, amount="15.00"),
                _line(side=PostingSide.CREDIT, amount="15.00"),
            ],
        )
