from __future__ import annotations

from dataclasses import dataclass
from dataclasses import is_dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.features.accounting import BusinessRuleViolation
from mfm.application.features.accounting import CloseFiscalYearRequest
from mfm.application.features.accounting import CreateFiscalYearRequest
from mfm.application.features.accounting import CreateJournalRequest
from mfm.application.features.accounting import CreateLedgerAccountRequest
from mfm.application.features.accounting import FiscalPeriodInput
from mfm.application.features.accounting import GetJournalRequest
from mfm.application.features.accounting import JournalLineInput
from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import ListJournalsRequest
from mfm.application.features.accounting import ListLedgerAccountsRequest
from mfm.application.features.accounting import OpenFiscalYearRequest
from mfm.application.features.accounting import PostJournalRequest
from mfm.application.features.accounting import RepositoryException
from mfm.application.features.accounting import ReverseJournalRequest
from mfm.application.features.accounting import close_fiscal_year
from mfm.application.features.accounting import create_fiscal_year
from mfm.application.features.accounting import create_journal
from mfm.application.features.accounting import create_ledger_account
from mfm.application.features.accounting import get_journal
from mfm.application.features.accounting import list_fiscal_years
from mfm.application.features.accounting import list_journals
from mfm.application.features.accounting import list_ledger_accounts
from mfm.application.features.accounting import open_fiscal_year
from mfm.application.features.accounting import post_journal
from mfm.application.features.accounting import reverse_journal
from mfm.application.accounting.close_fiscal_year import CloseFiscalYearUseCase
from mfm.application.accounting.create_fiscal_year import CreateFiscalYearUseCase
from mfm.application.accounting.create_journal import CreateJournalUseCase
from mfm.application.accounting.create_ledger_account import CreateLedgerAccountUseCase
from mfm.application.accounting.get_journal import GetJournalUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.list_journals import ListJournalsUseCase
from mfm.application.accounting.list_ledger_accounts import ListLedgerAccountsUseCase
from mfm.application.accounting.open_fiscal_year import OpenFiscalYearUseCase
from mfm.application.accounting.post_journal import PostJournalUseCase
from mfm.application.accounting.reverse_journal import ReverseJournalUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteFiscalYearRepository,
)
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteJournalRepository,
)
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteLedgerAccountRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


@pytest.fixture(autouse=True)
def _reset_accounting_class_state() -> None:
    LedgerAccount._registered_numbers.clear()
    FiscalYear._open_year_id = None
    try:
        yield
    finally:
        LedgerAccount._registered_numbers.clear()
        FiscalYear._open_year_id = None


class SQLiteAccountingApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session, *, fail_commit: bool = False) -> None:
        super().__init__()
        self._session = session
        self._fail_commit = fail_commit
        self._persistence_uow: UnitOfWork | None = None
        self.commit_count = 0
        self.rollback_count = 0

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.journal_repository = SQLiteJournalRepository(self._persistence_uow)
        self.ledger_account_repository = SQLiteLedgerAccountRepository(self._persistence_uow)
        self.fiscal_year_repository = SQLiteFiscalYearRepository(self._persistence_uow)

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None

    def _commit_impl(self) -> None:
        self.commit_count += 1
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")
        assert self._persistence_uow is not None
        self._persistence_uow.commit()

    def _rollback_impl(self) -> None:
        self.rollback_count += 1
        assert self._persistence_uow is not None
        self._persistence_uow.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        return None


@dataclass(frozen=True, slots=True)
class AccountingFeatureServices:
    create_fiscal_year_service: CreateFiscalYearUseCase
    open_fiscal_year_service: OpenFiscalYearUseCase
    close_fiscal_year_service: CloseFiscalYearUseCase
    create_ledger_account_service: CreateLedgerAccountUseCase
    create_journal_service: CreateJournalUseCase
    post_journal_service: PostJournalUseCase
    get_journal_service: GetJournalUseCase
    reverse_journal_service: ReverseJournalUseCase
    list_journals_service: ListJournalsUseCase
    list_ledger_accounts_service: ListLedgerAccountsUseCase
    list_fiscal_years_service: ListFiscalYearsUseCase


def _services(uow: SQLiteAccountingApplicationUnitOfWork) -> AccountingFeatureServices:
    return AccountingFeatureServices(
        create_fiscal_year_service=CreateFiscalYearUseCase(unit_of_work=uow),
        open_fiscal_year_service=OpenFiscalYearUseCase(unit_of_work=uow),
        close_fiscal_year_service=CloseFiscalYearUseCase(unit_of_work=uow),
        create_ledger_account_service=CreateLedgerAccountUseCase(unit_of_work=uow),
        create_journal_service=CreateJournalUseCase(unit_of_work=uow),
        post_journal_service=PostJournalUseCase(unit_of_work=uow),
        get_journal_service=GetJournalUseCase(unit_of_work=uow),
        reverse_journal_service=ReverseJournalUseCase(unit_of_work=uow),
        list_journals_service=ListJournalsUseCase(unit_of_work=uow),
        list_ledger_accounts_service=ListLedgerAccountsUseCase(unit_of_work=uow),
        list_fiscal_years_service=ListFiscalYearsUseCase(unit_of_work=uow),
    )


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "accounting_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _closed_period(number: int, start_day: int, end_day: int, *, year: int) -> FiscalPeriodInput:
    return FiscalPeriodInput(
        number=number,
        start_date=date(year, 1, start_day),
        end_date=date(year, 1, end_day),
        closed=True,
    )


def _open_period(number: int, start_day: int, end_day: int, *, year: int) -> FiscalPeriodInput:
    return FiscalPeriodInput(
        number=number,
        start_date=date(year, 1, start_day),
        end_date=date(year, 1, end_day),
        closed=False,
    )


def _line(account_id: UUID, side: str, amount: str) -> JournalLineInput:
    return JournalLineInput(
        account_id=account_id,
        side=side,
        amount=Decimal(amount),
        currency="DKK",
    )


def test_e2e_workflow_accounting_feature_api_with_roundtrip_and_invariants(
    sqlite_session_factory,
) -> None:
    write_session = sqlite_session_factory()
    reversal_journal_id: UUID | None = None

    try:
        uow = SQLiteAccountingApplicationUnitOfWork(write_session)
        services = _services(uow)

        # 1) Create Fiscal Year
        fiscal_year = create_fiscal_year(
            service=services.create_fiscal_year_service,
            request=CreateFiscalYearRequest(
                year=2036,
                start_date=date(2036, 1, 1),
                end_date=date(2036, 1, 31),
                status="CLOSED",
                periods=(
                    _open_period(1, 1, 10, year=2036),
                    _open_period(2, 11, 20, year=2036),
                    _open_period(3, 21, 31, year=2036),
                ),
            ),
        )
        assert is_dataclass(fiscal_year.fiscal_year)
        assert fiscal_year.fiscal_year.status == "CLOSED"

        # 2) Open Fiscal Year
        opened_fiscal_year = open_fiscal_year(
            service=services.open_fiscal_year_service,
            request=OpenFiscalYearRequest(
                fiscal_year_id=fiscal_year.fiscal_year.fiscal_year_id
            ),
        )
        assert opened_fiscal_year.fiscal_year.status == "OPEN"

        # 3) Create Ledger Accounts
        debit_account = create_ledger_account(
            service=services.create_ledger_account_service,
            request=CreateLedgerAccountRequest(
                account_number="1100-AR",
                name="Accounts receivable",
                account_type="ASSET",
                normal_balance="DEBIT",
            ),
        )
        credit_account = create_ledger_account(
            service=services.create_ledger_account_service,
            request=CreateLedgerAccountRequest(
                account_number="4100-SALES",
                name="Sales income",
                account_type="INCOME",
                normal_balance="CREDIT",
            ),
        )

        # 4) Create Journal
        # 5) Add Journal Lines (provided during create request)
        created_journal = create_journal(
            service=services.create_journal_service,
            request=CreateJournalRequest(
                journal_number="JRN-2036-0001",
                posting_date=date(2036, 1, 15),
                description="Membership annual invoice",
                reference="INV-2036-0001",
                lines=(
                    _line(debit_account.account.account_id, "DEBIT", "150.00"),
                    _line(credit_account.account.account_id, "CREDIT", "150.00"),
                ),
            ),
        )

        # 6) Validate balanced Journal (double-entry invariant)
        debit_total = sum(
            line.amount
            for line in created_journal.journal.lines
            if line.side == "DEBIT"
        )
        credit_total = sum(
            line.amount
            for line in created_journal.journal.lines
            if line.side == "CREDIT"
        )
        assert debit_total == Decimal("150.00")
        assert credit_total == Decimal("150.00")
        assert debit_total == credit_total

        # Create a second draft journal for listing and round-trip checks.
        draft_journal = create_journal(
            service=services.create_journal_service,
            request=CreateJournalRequest(
                journal_number="JRN-2036-0002",
                posting_date=date(2036, 1, 16),
                description="Deferred posting",
                reference="INV-2036-0002",
                lines=(
                    _line(debit_account.account.account_id, "DEBIT", "75.00"),
                    _line(credit_account.account.account_id, "CREDIT", "75.00"),
                ),
            ),
        )
        assert draft_journal.journal.status == "DRAFT"

        # 7) Post Journal
        posted_journal = post_journal(
            service=services.post_journal_service,
            request=PostJournalRequest(journal_id=created_journal.journal.journal_id),
        )
        assert posted_journal.journal.status == "POSTED"

        # 8) Retrieve Posted Journal
        retrieved_posted_journal = get_journal(
            service=services.get_journal_service,
            request=GetJournalRequest(journal_id=created_journal.journal.journal_id),
        )
        assert retrieved_posted_journal.journal.status == "POSTED"

        # Additional invariant: posted journals are immutable for posting operation.
        with pytest.raises(BusinessRuleViolation):
            post_journal(
                service=services.post_journal_service,
                request=PostJournalRequest(journal_id=created_journal.journal.journal_id),
            )

        reloaded_after_failed_repost = get_journal(
            service=services.get_journal_service,
            request=GetJournalRequest(journal_id=created_journal.journal.journal_id),
        )
        assert tuple(reloaded_after_failed_repost.journal.lines) == tuple(
            retrieved_posted_journal.journal.lines
        )

        # 9) Reverse Journal
        reversed_journal = reverse_journal(
            service=services.reverse_journal_service,
            request=ReverseJournalRequest(journal_id=created_journal.journal.journal_id),
        )
        reversal_journal_id = reversed_journal.journal.journal_id
        assert reversed_journal.journal.status == "REVERSED"

        assert uow.commit_count >= 7
        assert uow.rollback_count >= 1

        listed_journals = list_journals(
            service=services.list_journals_service,
            request=ListJournalsRequest(),
        )
        assert [item.journal_number for item in listed_journals.journals] == [
            "JRN-2036-0001",
            "JRN-2036-0002",
        ]

        listed_ledger_accounts = list_ledger_accounts(
            service=services.list_ledger_accounts_service,
            request=ListLedgerAccountsRequest(),
        )
        assert [item.account_number for item in listed_ledger_accounts.accounts] == [
            "1100-AR",
            "4100-SALES",
        ]

        listed_fiscal_years = list_fiscal_years(
            service=services.list_fiscal_years_service,
            request=ListFiscalYearsRequest(),
        )
        assert [item.status for item in listed_fiscal_years.fiscal_years] == ["OPEN"]
    finally:
        write_session.close()

    assert reversal_journal_id is not None
    read_session = sqlite_session_factory()
    try:
        read_uow = SQLiteAccountingApplicationUnitOfWork(read_session)
        read_services = _services(read_uow)

        reloaded_reversed_journal = get_journal(
            service=read_services.get_journal_service,
            request=GetJournalRequest(journal_id=reversal_journal_id),
        )
        assert reloaded_reversed_journal.journal.status == "REVERSED"
        assert len(reloaded_reversed_journal.journal.lines) == 2
        assert reloaded_reversed_journal.journal.lines[0].amount == Decimal("150.00")

        readback_journals = list_journals(
            service=read_services.list_journals_service,
            request=ListJournalsRequest(),
        )
        assert [item.journal_number for item in readback_journals.journals] == [
            "JRN-2036-0001",
            "JRN-2036-0002",
        ]
    finally:
        read_session.close()


def test_e2e_close_fiscal_year_and_reject_journal_in_closed_year(
    sqlite_session_factory,
) -> None:
    session = sqlite_session_factory()
    try:
        uow = SQLiteAccountingApplicationUnitOfWork(session)
        services = _services(uow)

        # 10) Close Fiscal Year
        closable_fiscal_year = create_fiscal_year(
            service=services.create_fiscal_year_service,
            request=CreateFiscalYearRequest(
                year=2037,
                start_date=date(2037, 1, 1),
                end_date=date(2037, 1, 31),
                status="OPEN",
                periods=(
                    _closed_period(1, 1, 10, year=2037),
                    _closed_period(2, 11, 20, year=2037),
                    _closed_period(3, 21, 31, year=2037),
                ),
            ),
        )

        closed_fiscal_year = close_fiscal_year(
            service=services.close_fiscal_year_service,
            request=CloseFiscalYearRequest(
                fiscal_year_id=closable_fiscal_year.fiscal_year.fiscal_year_id
            ),
        )
        assert closed_fiscal_year.fiscal_year.status == "CLOSED"

        debit_account = create_ledger_account(
            service=services.create_ledger_account_service,
            request=CreateLedgerAccountRequest(
                account_number="1200-AR",
                name="Accounts receivable",
                account_type="ASSET",
                normal_balance="DEBIT",
            ),
        )
        credit_account = create_ledger_account(
            service=services.create_ledger_account_service,
            request=CreateLedgerAccountRequest(
                account_number="4200-SALES",
                name="Sales income",
                account_type="INCOME",
                normal_balance="CREDIT",
            ),
        )

        # 11) Verify posting rejection in closed Fiscal Year.
        # Accepted architectural constraint: with public Feature API only, journals
        # in a closed fiscal year are rejected at journal creation boundary.
        with pytest.raises(BusinessRuleViolation):
            create_journal(
                service=services.create_journal_service,
                request=CreateJournalRequest(
                    journal_number="JRN-2037-0001",
                    posting_date=date(2037, 1, 15),
                    description="Rejected in closed fiscal year",
                    reference="INV-2037-0001",
                    lines=(
                        _line(debit_account.account.account_id, "DEBIT", "25.00"),
                        _line(credit_account.account.account_id, "CREDIT", "25.00"),
                    ),
                ),
            )
    finally:
        session.close()


def test_uow_rollback_on_commit_failure_preserves_repository_state(
    sqlite_session_factory,
) -> None:
    session = sqlite_session_factory()
    try:
        failing_uow = SQLiteAccountingApplicationUnitOfWork(session, fail_commit=True)
        failing_services = _services(failing_uow)

        with pytest.raises(RepositoryException):
            create_fiscal_year(
                service=failing_services.create_fiscal_year_service,
                request=CreateFiscalYearRequest(
                    year=2037,
                    start_date=date(2037, 1, 1),
                    end_date=date(2037, 1, 31),
                    periods=(
                        _closed_period(1, 1, 10, year=2037),
                        _closed_period(2, 11, 20, year=2037),
                        _closed_period(3, 21, 31, year=2037),
                    ),
                ),
            )

        assert failing_uow.commit_count == 1
        assert failing_uow.rollback_count == 1

        probe_uow = SQLiteAccountingApplicationUnitOfWork(session)
        probe_services = _services(probe_uow)

        listed_fiscal_years = list_fiscal_years(
            service=probe_services.list_fiscal_years_service,
            request=ListFiscalYearsRequest(),
        )
        assert listed_fiscal_years.fiscal_years == ()
    finally:
        session.close()
