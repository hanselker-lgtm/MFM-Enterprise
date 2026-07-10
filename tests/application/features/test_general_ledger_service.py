from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.application.features.general_ledger_service import ListGeneralLedgerFeature
from mfm.application.features.general_ledger_service import ListGeneralLedgerRequest
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.domain.accounting.journal_entry import JournalEntryStatus
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.normal_balance import NormalBalance
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money


@dataclass(slots=True)
class StubAccount:
    id: UUID
    account_number: AccountNumber
    name: str
    normal_balance: NormalBalance


class InMemoryAccountRepository:
    def __init__(self, accounts: list[StubAccount]) -> None:
        self._accounts = accounts

    def list(self) -> list[StubAccount]:
        return list(self._accounts)


class InMemoryJournalRepository:
    def __init__(self, journals: list[JournalEntry]) -> None:
        self._journals = journals

    def list(self) -> list[JournalEntry]:
        return list(self._journals)


def _money(value: str) -> Money:
    return Money(amount=Decimal(value), currency=Currency.DKK)


def _journal(
    *,
    posting_date: date,
    debit_account_id: UUID,
    credit_account_id: UUID,
    amount: str,
    status: JournalEntryStatus = JournalEntryStatus.POSTED,
) -> JournalEntry:
    value = _money(amount)
    return JournalEntry(
        journal_number=f"JRN-{posting_date:%Y%m%d}-{uuid4().hex[:4]}",
        posting_date=posting_date,
        description="Posting",
        status=status,
        lines=[
            JournalLine(
                account_id=debit_account_id,
                side=PostingSide.DEBIT,
                amount=value,
                description="Debit",
            ),
            JournalLine(
                account_id=credit_account_id,
                side=PostingSide.CREDIT,
                amount=value,
                description="Credit",
            ),
        ],
    )


def _service(accounts: list[StubAccount], journals: list[JournalEntry]) -> ListGeneralLedgerFeature:
    return ListGeneralLedgerFeature(
        account_repository=InMemoryAccountRepository(accounts),
        journal_repository=InMemoryJournalRepository(journals),
    )


def test_empty_ledger():
    service = _service([], [])

    result = service.execute(
        ListGeneralLedgerRequest(
            fiscal_year=2026,
            from_date=date(2026, 1, 1),
            to_date=date(2026, 1, 31),
        )
    )

    assert result == []


def test_one_posting():
    cash = StubAccount(uuid4(), AccountNumber("1000"), "Cash", NormalBalance.DEBIT)
    revenue = StubAccount(uuid4(), AccountNumber("3000"), "Revenue", NormalBalance.CREDIT)
    journals = [
        _journal(
            posting_date=date(2026, 1, 10),
            debit_account_id=cash.id,
            credit_account_id=revenue.id,
            amount="100.00",
        )
    ]

    result = _service([cash, revenue], journals).execute(
        ListGeneralLedgerRequest(
            fiscal_year=2026,
            from_date=date(2026, 1, 1),
            to_date=date(2026, 1, 31),
        )
    )

    cash_row = next(row for row in result if row.account_number == "1000")
    revenue_row = next(row for row in result if row.account_number == "3000")

    assert cash_row.debit_turnover_amount == Decimal("100.00")
    assert cash_row.debit_turnover_currency == "DKK"
    assert cash_row.credit_turnover_amount == Decimal("0.00")
    assert cash_row.credit_turnover_currency == "DKK"
    assert cash_row.closing_balance_amount == Decimal("100.00")
    assert cash_row.closing_balance_currency == "DKK"

    assert revenue_row.debit_turnover_amount == Decimal("0.00")
    assert revenue_row.debit_turnover_currency == "DKK"
    assert revenue_row.credit_turnover_amount == Decimal("100.00")
    assert revenue_row.credit_turnover_currency == "DKK"
    assert revenue_row.closing_balance_amount == Decimal("100.00")
    assert revenue_row.closing_balance_currency == "DKK"


def test_multiple_postings():
    cash = StubAccount(uuid4(), AccountNumber("1000"), "Cash", NormalBalance.DEBIT)
    revenue = StubAccount(uuid4(), AccountNumber("3000"), "Revenue", NormalBalance.CREDIT)
    journals = [
        _journal(posting_date=date(2026, 1, 5), debit_account_id=cash.id, credit_account_id=revenue.id, amount="50.00"),
        _journal(posting_date=date(2026, 1, 20), debit_account_id=cash.id, credit_account_id=revenue.id, amount="75.00"),
    ]

    result = _service([cash, revenue], journals).execute(
        ListGeneralLedgerRequest(
            fiscal_year=2026,
            from_date=date(2026, 1, 1),
            to_date=date(2026, 1, 31),
        )
    )

    cash_row = next(row for row in result if row.account_number == "1000")
    assert cash_row.debit_turnover_amount == Decimal("125.00")
    assert cash_row.closing_balance_amount == Decimal("125.00")


def test_multiple_accounts():
    cash = StubAccount(uuid4(), AccountNumber("1000"), "Cash", NormalBalance.DEBIT)
    bank = StubAccount(uuid4(), AccountNumber("1010"), "Bank", NormalBalance.DEBIT)
    revenue = StubAccount(uuid4(), AccountNumber("3000"), "Revenue", NormalBalance.CREDIT)
    journals = [
        _journal(posting_date=date(2026, 1, 5), debit_account_id=cash.id, credit_account_id=revenue.id, amount="30.00"),
        _journal(posting_date=date(2026, 1, 6), debit_account_id=bank.id, credit_account_id=revenue.id, amount="70.00"),
    ]

    result = _service([cash, bank, revenue], journals).execute(
        ListGeneralLedgerRequest(
            fiscal_year=2026,
            from_date=date(2026, 1, 1),
            to_date=date(2026, 1, 31),
        )
    )

    assert [row.account_number for row in result] == ["1000", "1010", "3000"]


def test_date_filtering():
    cash = StubAccount(uuid4(), AccountNumber("1000"), "Cash", NormalBalance.DEBIT)
    revenue = StubAccount(uuid4(), AccountNumber("3000"), "Revenue", NormalBalance.CREDIT)
    journals = [
        _journal(posting_date=date(2026, 1, 2), debit_account_id=cash.id, credit_account_id=revenue.id, amount="40.00"),
        _journal(posting_date=date(2026, 1, 15), debit_account_id=cash.id, credit_account_id=revenue.id, amount="60.00"),
        _journal(posting_date=date(2026, 2, 1), debit_account_id=cash.id, credit_account_id=revenue.id, amount="20.00"),
        _journal(posting_date=date(2026, 1, 10), debit_account_id=cash.id, credit_account_id=revenue.id, amount="999.00", status=JournalEntryStatus.DRAFT),
    ]

    result = _service([cash, revenue], journals).execute(
        ListGeneralLedgerRequest(
            fiscal_year=2026,
            from_date=date(2026, 1, 10),
            to_date=date(2026, 1, 31),
        )
    )

    cash_row = next(row for row in result if row.account_number == "1000")

    assert cash_row.opening_balance_amount == Decimal("40.00")
    assert cash_row.debit_turnover_amount == Decimal("60.00")
    assert cash_row.credit_turnover_amount == Decimal("0.00")
    assert cash_row.closing_balance_amount == Decimal("100.00")


def test_account_filtering():
    cash = StubAccount(uuid4(), AccountNumber("1000"), "Cash", NormalBalance.DEBIT)
    bank = StubAccount(uuid4(), AccountNumber("1010"), "Bank", NormalBalance.DEBIT)
    revenue = StubAccount(uuid4(), AccountNumber("3000"), "Revenue", NormalBalance.CREDIT)

    result = _service([cash, bank, revenue], []).execute(
        ListGeneralLedgerRequest(
            fiscal_year=2026,
            from_date=date(2026, 1, 1),
            to_date=date(2026, 1, 31),
            account_range=("1000", "1999"),
        )
    )

    assert [row.account_number for row in result] == ["1000", "1010"]


def test_balance_calculation():
    receivable = StubAccount(uuid4(), AccountNumber("1100"), "Receivable", NormalBalance.DEBIT)
    payable = StubAccount(uuid4(), AccountNumber("2100"), "Payable", NormalBalance.CREDIT)
    cash = StubAccount(uuid4(), AccountNumber("1000"), "Cash", NormalBalance.DEBIT)

    journals = [
        _journal(posting_date=date(2026, 1, 3), debit_account_id=receivable.id, credit_account_id=payable.id, amount="120.00"),
        _journal(posting_date=date(2026, 1, 8), debit_account_id=cash.id, credit_account_id=receivable.id, amount="20.00"),
    ]

    result = _service([cash, receivable, payable], journals).execute(
        ListGeneralLedgerRequest(
            fiscal_year=2026,
            from_date=date(2026, 1, 1),
            to_date=date(2026, 1, 31),
        )
    )

    receivable_row = next(row for row in result if row.account_number == "1100")
    payable_row = next(row for row in result if row.account_number == "2100")

    assert receivable_row.debit_turnover_amount == Decimal("120.00")
    assert receivable_row.credit_turnover_amount == Decimal("20.00")
    assert receivable_row.closing_balance_amount == Decimal("100.00")

    assert payable_row.debit_turnover_amount == Decimal("0.00")
    assert payable_row.credit_turnover_amount == Decimal("120.00")
    assert payable_row.closing_balance_amount == Decimal("120.00")
