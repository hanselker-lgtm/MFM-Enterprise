from __future__ import annotations

from copy import deepcopy
from dataclasses import is_dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Any
from uuid import UUID

import pytest

from mfm.application.accounting.close_fiscal_year import CloseFiscalYearRequest
from mfm.application.accounting.close_fiscal_year import CloseFiscalYearUseCase
from mfm.application.accounting.create_fiscal_year import CreateFiscalYearRequest
from mfm.application.accounting.create_fiscal_year import CreateFiscalYearUseCase
from mfm.application.accounting.create_fiscal_year import FiscalPeriodInput
from mfm.application.accounting.create_journal import BusinessRuleViolation
from mfm.application.accounting.create_journal import CreateJournalRequest
from mfm.application.accounting.create_journal import CreateJournalUseCase
from mfm.application.accounting.create_journal import JournalLineInput
from mfm.application.accounting.create_journal import RepositoryException
from mfm.application.accounting.create_journal import to_journal_search_result_response
from mfm.application.accounting.create_ledger_account import CreateLedgerAccountRequest
from mfm.application.accounting.create_ledger_account import CreateLedgerAccountUseCase
from mfm.application.accounting.get_fiscal_year import GetFiscalYearRequest
from mfm.application.accounting.get_fiscal_year import GetFiscalYearUseCase
from mfm.application.accounting.get_journal import GetJournalRequest
from mfm.application.accounting.get_journal import GetJournalUseCase
from mfm.application.accounting.get_ledger_account import GetLedgerAccountRequest
from mfm.application.accounting.get_ledger_account import GetLedgerAccountUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsRequest
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.list_journals import ListJournalsRequest
from mfm.application.accounting.list_journals import ListJournalsUseCase
from mfm.application.accounting.list_ledger_accounts import ListLedgerAccountsRequest
from mfm.application.accounting.list_ledger_accounts import ListLedgerAccountsUseCase
from mfm.application.accounting.open_fiscal_year import OpenFiscalYearRequest
from mfm.application.accounting.open_fiscal_year import OpenFiscalYearUseCase
from mfm.application.accounting.post_journal import PostJournalRequest
from mfm.application.accounting.post_journal import PostJournalUseCase
from mfm.application.accounting.reverse_journal import ReverseJournalRequest
from mfm.application.accounting.reverse_journal import ReverseJournalUseCase
from mfm.application.accounting.search_journals import SearchJournalsRequest
from mfm.application.accounting.search_journals import SearchJournalsUseCase
from mfm.application.accounting.update_ledger_account import UpdateLedgerAccountRequest
from mfm.application.accounting.update_ledger_account import UpdateLedgerAccountUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus
from mfm.domain.accounting.journal import Journal
from mfm.domain.accounting.journal_entry import JournalEntryStatus
from mfm.domain.accounting.ledger_account import LedgerAccount


@pytest.fixture(autouse=True)
def _reset_accounting_class_state() -> None:
    LedgerAccount._registered_numbers.clear()
    FiscalYear._open_year_id = None
    try:
        yield
    finally:
        LedgerAccount._registered_numbers.clear()
        FiscalYear._open_year_id = None


class InMemoryJournalRepository:
    def __init__(self, *, fail_on_add: bool = False, fail_on_update: bool = False) -> None:
        self._journals: dict[UUID, Journal] = {}
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

    def snapshot(self) -> dict[UUID, Journal]:
        return deepcopy(self._journals)

    def restore(self, snapshot: dict[UUID, Journal]) -> None:
        self._journals = deepcopy(snapshot)

    def add(self, journal: Journal) -> None:
        if self._fail_on_add:
            raise RuntimeError("journal add failed")
        if self.get_by_number(
            fiscal_year=journal.posting_date.year,
            journal_number=journal.journal_number,
        ) is not None:
            raise ValueError(
                f"Journal number {journal.journal_number} already exists in fiscal year {journal.posting_date.year}"
            )
        self._journals[journal.id] = deepcopy(journal)

    def get_by_id(self, journal_id: UUID) -> Journal | None:
        value = self._journals.get(journal_id)
        return deepcopy(value) if value is not None else None

    def get_by_number(self, *, fiscal_year: int, journal_number: str) -> Journal | None:
        normalized = journal_number.strip().upper()
        for value in self._journals.values():
            if value.posting_date.year == fiscal_year and value.journal_number == normalized:
                return deepcopy(value)
        return None

    def update(self, journal: Journal) -> None:
        if self._fail_on_update:
            raise RuntimeError("journal update failed")
        if journal.id not in self._journals:
            raise ValueError(f"Journal {journal.id} does not exist")

        for existing in self._journals.values():
            if (
                existing.id != journal.id
                and existing.posting_date.year == journal.posting_date.year
                and existing.journal_number == journal.journal_number
            ):
                raise ValueError(
                    f"Journal number {journal.journal_number} already exists in fiscal year {journal.posting_date.year}"
                )

        journal.version += 1
        self._journals[journal.id] = deepcopy(journal)

    def list(self) -> list[Journal]:
        values = sorted(
            self._journals.values(),
            key=lambda item: (item.journal_number, item.posting_date, str(item.id)),
        )
        return [deepcopy(item) for item in values]

    def list_by_reference(self, reference: str) -> list[Journal]:
        normalized = reference.strip()
        return [item for item in self.list() if item.reference == normalized]

    def list_by_posting_date_range(self, *, start_date: date, end_date: date) -> list[Journal]:
        return [
            item
            for item in self.list()
            if start_date <= item.posting_date <= end_date
        ]

    def search(self, criteria: Any) -> list[Any]:
        if isinstance(criteria, str):
            filters = {"text": criteria}
        elif isinstance(criteria, dict):
            filters = dict(criteria)
        else:
            filters = {}

        text = str(filters.get("text", "")).strip().casefold()
        status = filters.get("status")
        if status is not None:
            status = (
                status
                if isinstance(status, JournalEntryStatus)
                else JournalEntryStatus(str(status).upper())
            )

        fiscal_year = filters.get("fiscal_year")
        if fiscal_year is not None:
            fiscal_year = int(fiscal_year)

        rows: list[dict[str, Any]] = []
        for journal in self.list():
            haystack = (
                f"{journal.journal_number} {journal.description} {journal.reference or ''}"
            ).casefold()
            if text and text not in haystack:
                continue
            if status is not None and journal.status is not status:
                continue
            if fiscal_year is not None and journal.posting_date.year != fiscal_year:
                continue

            rows.append(
                {
                    "id": journal.id,
                    "fiscal_year_id": UUID(int=journal.posting_date.year),
                    "journal_number": journal.journal_number,
                    "posting_date": journal.posting_date,
                    "status": journal.status,
                    "reference": journal.reference,
                }
            )

        return rows


class InMemoryLedgerAccountRepository:
    def __init__(self, *, fail_on_add: bool = False, fail_on_update: bool = False) -> None:
        self._accounts: dict[UUID, LedgerAccount] = {}
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

    def snapshot(self) -> dict[UUID, LedgerAccount]:
        return deepcopy(self._accounts)

    def restore(self, snapshot: dict[UUID, LedgerAccount]) -> None:
        self._accounts = deepcopy(snapshot)

    def add(self, account: LedgerAccount) -> None:
        if self._fail_on_add:
            raise RuntimeError("ledger account add failed")

        if self.get_by_number(account.account_number) is not None:
            raise ValueError(
                f"Ledger account number {account.account_number.value} already exists"
            )

        self._accounts[account.id] = deepcopy(account)

    def get_by_id(self, account_id: UUID) -> LedgerAccount | None:
        value = self._accounts.get(account_id)
        return deepcopy(value) if value is not None else None

    def get_by_number(self, account_number: AccountNumber) -> LedgerAccount | None:
        for account in self._accounts.values():
            if account.account_number == account_number:
                return deepcopy(account)
        return None

    def update(self, account: LedgerAccount) -> None:
        if self._fail_on_update:
            raise RuntimeError("ledger account update failed")
        if account.id not in self._accounts:
            raise ValueError(f"Ledger account {account.id} does not exist")

        for existing in self._accounts.values():
            if (
                existing.id != account.id
                and existing.account_number == account.account_number
            ):
                raise ValueError(
                    f"Ledger account number {account.account_number.value} already exists"
                )

        self._accounts[account.id] = deepcopy(account)

    def list(self) -> list[LedgerAccount]:
        values = sorted(
            self._accounts.values(),
            key=lambda item: (item.account_number.value, str(item.id)),
        )
        return [deepcopy(item) for item in values]

    def list_active(self) -> list[LedgerAccount]:
        return [item for item in self.list() if item.active]


class InMemoryFiscalYearRepository:
    def __init__(self, *, fail_on_add: bool = False, fail_on_update: bool = False) -> None:
        self._years: dict[UUID, FiscalYear] = {}
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

    def snapshot(self) -> dict[UUID, FiscalYear]:
        return deepcopy(self._years)

    def restore(self, snapshot: dict[UUID, FiscalYear]) -> None:
        self._years = deepcopy(snapshot)

    def add(self, fiscal_year: FiscalYear) -> None:
        if self._fail_on_add:
            raise RuntimeError("fiscal year add failed")
        if self.get_by_year(fiscal_year.year) is not None:
            raise ValueError(f"Fiscal year {fiscal_year.year} already exists")
        self._years[fiscal_year.id] = deepcopy(fiscal_year)

    def get_by_id(self, fiscal_year_id: UUID) -> FiscalYear | None:
        value = self._years.get(fiscal_year_id)
        return deepcopy(value) if value is not None else None

    def get_by_year(self, year: int) -> FiscalYear | None:
        for value in self._years.values():
            if value.year == year:
                return deepcopy(value)
        return None

    def get_open(self) -> FiscalYear | None:
        for value in self.list():
            if value.status is FiscalYearStatus.OPEN:
                return value
        return None

    def update(self, fiscal_year: FiscalYear) -> None:
        if self._fail_on_update:
            raise RuntimeError("fiscal year update failed")
        if fiscal_year.id not in self._years:
            raise ValueError(f"Fiscal year {fiscal_year.id} does not exist")

        for value in self._years.values():
            if value.id != fiscal_year.id and value.year == fiscal_year.year:
                raise ValueError(f"Fiscal year {fiscal_year.year} already exists")

        self._years[fiscal_year.id] = deepcopy(fiscal_year)

    def list(self) -> list[FiscalYear]:
        values = sorted(self._years.values(), key=lambda item: (item.year, str(item.id)))
        return [deepcopy(item) for item in values]


class FakeAccountingUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_journal_add: bool = False,
        fail_journal_update: bool = False,
        fail_commit: bool = False,
    ) -> None:
        super().__init__()
        self._fail_commit = fail_commit

        self._journal_repository = InMemoryJournalRepository(
            fail_on_add=fail_journal_add,
            fail_on_update=fail_journal_update,
        )
        self._ledger_account_repository = InMemoryLedgerAccountRepository()
        self._fiscal_year_repository = InMemoryFiscalYearRepository()

        self._journal_snapshot: dict[UUID, Journal] = {}
        self._ledger_snapshot: dict[UUID, LedgerAccount] = {}
        self._fiscal_year_snapshot: dict[UUID, FiscalYear] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self.journal_repository = self._journal_repository
        self.ledger_account_repository = self._ledger_account_repository
        self.fiscal_year_repository = self._fiscal_year_repository

        self._journal_snapshot = self._journal_repository.snapshot()
        self._ledger_snapshot = self._ledger_account_repository.snapshot()
        self._fiscal_year_snapshot = self._fiscal_year_repository.snapshot()

    def _commit_impl(self) -> None:
        self.commits += 1
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self._journal_repository.restore(self._journal_snapshot)
        self._ledger_account_repository.restore(self._ledger_snapshot)
        self._fiscal_year_repository.restore(self._fiscal_year_snapshot)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


def _period(
    number: int,
    start_day: int,
    end_day: int,
    *,
    year: int,
    month: int = 1,
    closed: bool = False,
) -> FiscalPeriodInput:
    return FiscalPeriodInput(
        number=number,
        start_date=date(year, month, start_day),
        end_date=date(year, month, end_day),
        closed=closed,
    )


def _create_fiscal_year(
    uow: FakeAccountingUnitOfWork,
    *,
    year: int = 2030,
    status: str = "OPEN",
    periods: tuple[FiscalPeriodInput, ...] | None = None,
) -> UUID:
    feb_end_day = 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
    used_periods = periods or (
        FiscalPeriodInput(number=1, start_date=date(year, 1, 1), end_date=date(year, 1, 31)),
        FiscalPeriodInput(
            number=2,
            start_date=date(year, 2, 1),
            end_date=date(year, 2, feb_end_day),
        ),
        FiscalPeriodInput(number=3, start_date=date(year, 3, 1), end_date=date(year, 3, 31)),
    )
    response = CreateFiscalYearUseCase(unit_of_work=uow).execute(
        CreateFiscalYearRequest(
            year=year,
            start_date=used_periods[0].start_date,
            end_date=used_periods[-1].end_date,
            status=status,
            periods=used_periods,
        )
    )

    fiscal_year_id = response.fiscal_year.fiscal_year_id
    if status == "CLOSED":
        FiscalYear._open_year_id = None
    return fiscal_year_id


def _create_ledger_account(
    uow: FakeAccountingUnitOfWork,
    *,
    account_number: str,
    name: str,
    account_type: str,
    normal_balance: str,
) -> UUID:
    response = CreateLedgerAccountUseCase(unit_of_work=uow).execute(
        CreateLedgerAccountRequest(
            account_number=account_number,
            name=name,
            account_type=account_type,
            normal_balance=normal_balance,
        )
    )
    return response.account.account_id


def _journal_line(account_id: UUID, side: str, amount: str) -> JournalLineInput:
    return JournalLineInput(
        account_id=account_id,
        side=side,
        amount=Decimal(amount),
        currency="DKK",
    )


def test_journal_lifecycle_posting_and_reversal_workflow() -> None:
    uow = FakeAccountingUnitOfWork()
    _create_fiscal_year(uow, year=2030)
    receivable_id = _create_ledger_account(
        uow,
        account_number="1100-AR",
        name="Accounts receivable",
        account_type="ASSET",
        normal_balance="DEBIT",
    )
    revenue_id = _create_ledger_account(
        uow,
        account_number="4100-SALES",
        name="Sales income",
        account_type="INCOME",
        normal_balance="CREDIT",
    )

    created = CreateJournalUseCase(unit_of_work=uow).execute(
        CreateJournalRequest(
            journal_number="JRN-2030-0001",
            posting_date=date(2030, 1, 15),
            description="Membership annual invoice",
            reference="INV-2030-0001",
            lines=(
                _journal_line(receivable_id, "DEBIT", "100.00"),
                _journal_line(revenue_id, "CREDIT", "100.00"),
            ),
        )
    )

    loaded = GetJournalUseCase(unit_of_work=uow).execute(
        GetJournalRequest(journal_id=created.journal.journal_id)
    )
    assert loaded.journal.status == "DRAFT"

    posted = PostJournalUseCase(unit_of_work=uow).execute(
        PostJournalRequest(journal_id=created.journal.journal_id)
    )
    assert posted.journal.status == "POSTED"

    reversed_journal = ReverseJournalUseCase(unit_of_work=uow).execute(
        ReverseJournalRequest(journal_id=created.journal.journal_id)
    )
    assert reversed_journal.journal.status == "REVERSED"


def test_closed_fiscal_year_rejection() -> None:
    uow = FakeAccountingUnitOfWork()
    periods = (
        FiscalPeriodInput(
            number=1,
            start_date=date(2031, 1, 1),
            end_date=date(2031, 1, 31),
            closed=True,
        ),
        FiscalPeriodInput(
            number=2,
            start_date=date(2031, 2, 1),
            end_date=date(2031, 2, 28),
            closed=True,
        ),
        FiscalPeriodInput(
            number=3,
            start_date=date(2031, 3, 1),
            end_date=date(2031, 3, 31),
            closed=True,
        ),
    )
    fiscal_year_id = _create_fiscal_year(uow, year=2031, periods=periods)
    closed = CloseFiscalYearUseCase(unit_of_work=uow).execute(
        CloseFiscalYearRequest(fiscal_year_id=fiscal_year_id)
    )
    assert closed.fiscal_year.status == "CLOSED"

    receivable_id = _create_ledger_account(
        uow,
        account_number="1200-AR",
        name="Receivable",
        account_type="ASSET",
        normal_balance="DEBIT",
    )
    revenue_id = _create_ledger_account(
        uow,
        account_number="4200-SALES",
        name="Revenue",
        account_type="INCOME",
        normal_balance="CREDIT",
    )

    with pytest.raises(BusinessRuleViolation):
        CreateJournalUseCase(unit_of_work=uow).execute(
            CreateJournalRequest(
                journal_number="JRN-2031-0001",
                posting_date=date(2031, 1, 15),
                description="Should fail in closed year",
                lines=(
                    _journal_line(receivable_id, "DEBIT", "50.00"),
                    _journal_line(revenue_id, "CREDIT", "50.00"),
                ),
            )
        )


def test_search_and_list_journals() -> None:
    uow = FakeAccountingUnitOfWork()
    _create_fiscal_year(uow, year=2032)

    debit_a = _create_ledger_account(
        uow,
        account_number="1300-A",
        name="Debit A",
        account_type="ASSET",
        normal_balance="DEBIT",
    )
    credit_a = _create_ledger_account(
        uow,
        account_number="4300-A",
        name="Credit A",
        account_type="INCOME",
        normal_balance="CREDIT",
    )

    CreateJournalUseCase(unit_of_work=uow).execute(
        CreateJournalRequest(
            journal_number="JRN-2032-0001",
            posting_date=date(2032, 1, 5),
            description="Fuel order",
            lines=(
                _journal_line(debit_a, "DEBIT", "10.00"),
                _journal_line(credit_a, "CREDIT", "10.00"),
            ),
        )
    )
    second = CreateJournalUseCase(unit_of_work=uow).execute(
        CreateJournalRequest(
            journal_number="JRN-2032-0002",
            posting_date=date(2032, 1, 6),
            description="Harbor fee",
            lines=(
                _journal_line(debit_a, "DEBIT", "20.00"),
                _journal_line(credit_a, "CREDIT", "20.00"),
            ),
        )
    )

    PostJournalUseCase(unit_of_work=uow).execute(
        PostJournalRequest(journal_id=second.journal.journal_id)
    )

    listed = ListJournalsUseCase(unit_of_work=uow).execute(ListJournalsRequest())
    assert [journal.journal_number for journal in listed.journals] == [
        "JRN-2032-0001",
        "JRN-2032-0002",
    ]

    search_text = SearchJournalsUseCase(unit_of_work=uow).execute(
        SearchJournalsRequest(text="Harbor")
    )
    assert [journal.journal_number for journal in search_text.journals] == [
        "JRN-2032-0002"
    ]

    search_status = SearchJournalsUseCase(unit_of_work=uow).execute(
        SearchJournalsRequest(status="POSTED")
    )
    assert [journal.journal_number for journal in search_status.journals] == [
        "JRN-2032-0002"
    ]


def test_ledger_account_lifecycle() -> None:
    uow = FakeAccountingUnitOfWork()

    created = CreateLedgerAccountUseCase(unit_of_work=uow).execute(
        CreateLedgerAccountRequest(
            account_number="1400-BANK",
            name="Bank",
            account_type="ASSET",
            normal_balance="DEBIT",
        )
    )

    loaded = GetLedgerAccountUseCase(unit_of_work=uow).execute(
        GetLedgerAccountRequest(account_id=created.account.account_id)
    )
    assert loaded.account.name == "Bank"

    updated = UpdateLedgerAccountUseCase(unit_of_work=uow).execute(
        UpdateLedgerAccountRequest(
            account_id=created.account.account_id,
            name="Bank operating account",
            active=False,
            locked=True,
        )
    )
    assert updated.account.name == "Bank operating account"
    assert updated.account.active is False
    assert updated.account.locked is True

    listed_all = ListLedgerAccountsUseCase(unit_of_work=uow).execute(
        ListLedgerAccountsRequest()
    )
    listed_active = ListLedgerAccountsUseCase(unit_of_work=uow).execute(
        ListLedgerAccountsRequest(active_only=True)
    )

    assert len(listed_all.accounts) == 1
    assert len(listed_active.accounts) == 0


def test_fiscal_year_lifecycle() -> None:
    uow = FakeAccountingUnitOfWork()
    periods = (
        _period(1, 1, 10, year=2033, closed=True),
        _period(2, 11, 20, year=2033, closed=True),
        _period(3, 21, 31, year=2033, closed=True),
    )

    created = CreateFiscalYearUseCase(unit_of_work=uow).execute(
        CreateFiscalYearRequest(
            year=2033,
            start_date=date(2033, 1, 1),
            end_date=date(2033, 1, 31),
            periods=periods,
        )
    )

    closed = CloseFiscalYearUseCase(unit_of_work=uow).execute(
        CloseFiscalYearRequest(fiscal_year_id=created.fiscal_year.fiscal_year_id)
    )
    assert closed.fiscal_year.status == "CLOSED"

    opened = OpenFiscalYearUseCase(unit_of_work=uow).execute(
        OpenFiscalYearRequest(fiscal_year_id=created.fiscal_year.fiscal_year_id)
    )
    assert opened.fiscal_year.status == "OPEN"

    loaded = GetFiscalYearUseCase(unit_of_work=uow).execute(
        GetFiscalYearRequest(fiscal_year_id=created.fiscal_year.fiscal_year_id)
    )
    listed = ListFiscalYearsUseCase(unit_of_work=uow).execute(ListFiscalYearsRequest())

    assert loaded.fiscal_year.year == 2033
    assert [item.year for item in listed.fiscal_years] == [2033]


def test_application_wraps_repository_failures_and_rolls_back() -> None:
    uow = FakeAccountingUnitOfWork(fail_journal_add=True)
    _create_fiscal_year(uow, year=2034)

    debit_id = _create_ledger_account(
        uow,
        account_number="1500-A",
        name="Debit",
        account_type="ASSET",
        normal_balance="DEBIT",
    )
    credit_id = _create_ledger_account(
        uow,
        account_number="4500-A",
        name="Credit",
        account_type="INCOME",
        normal_balance="CREDIT",
    )

    with pytest.raises(RepositoryException):
        CreateJournalUseCase(unit_of_work=uow).execute(
            CreateJournalRequest(
                journal_number="JRN-2034-0001",
                posting_date=date(2034, 1, 10),
                description="Failure case",
                lines=(
                    _journal_line(debit_id, "DEBIT", "25.00"),
                    _journal_line(credit_id, "CREDIT", "25.00"),
                ),
            )
        )

    assert uow.commits == 3
    assert uow.rollbacks == 1


def test_to_journal_search_result_response_maps_projection() -> None:
    row = {
        "id": UUID("00000000-0000-0000-0000-00000000A901"),
        "fiscal_year_id": UUID("00000000-0000-0000-0000-00000000B901"),
        "journal_number": "JRN-TEST-1",
        "posting_date": date(2035, 1, 1),
        "status": JournalEntryStatus.DRAFT,
        "reference": "REF-1",
    }

    mapped = to_journal_search_result_response(row)

    assert is_dataclass(mapped)
    assert mapped.status == "DRAFT"
    assert mapped.journal_number == "JRN-TEST-1"


def test_accounting_application_has_no_sqlalchemy_or_infrastructure_imports() -> None:
    accounting_dir = Path("src/mfm/application/accounting")
    forbidden_markers = (
        "sqlalchemy",
        "mfm.infrastructure.persistence",
        "mfm.database.models",
    )

    for path in accounting_dir.glob("*.py"):
        content = path.read_text(encoding="utf-8")
        lowered = content.casefold()
        for marker in forbidden_markers:
            assert marker not in lowered, f"{path} contains forbidden marker: {marker}"
