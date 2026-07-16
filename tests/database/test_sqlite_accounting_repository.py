from __future__ import annotations

from datetime import date
from decimal import Decimal
from pathlib import Path
import weakref
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.account_type import AccountType
from mfm.domain.accounting.fiscal_period import FiscalPeriod
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus
from mfm.domain.accounting.journal import Journal
from mfm.domain.accounting.journal_entry import JournalEntryStatus
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.accounting.normal_balance import NormalBalance
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money
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


def _new_session(db_path: Path) -> Session:
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return session


def _fiscal_year(*, year: int, closed: bool = False) -> FiscalYear:
    feb_end_day = 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
    fiscal_year = FiscalYear(
        id=UUID(f"00000000-0000-0000-0000-00000000{year:04d}"),
        year=year,
        start_date=date(year, 1, 1),
        end_date=date(year, 3, 31),
        periods=[
            FiscalPeriod(number=1, start_date=date(year, 1, 1), end_date=date(year, 1, 31)),
            FiscalPeriod(number=2, start_date=date(year, 2, 1), end_date=date(year, 2, feb_end_day)),
            FiscalPeriod(number=3, start_date=date(year, 3, 1), end_date=date(year, 3, 31)),
        ],
        status=FiscalYearStatus.OPEN,
    )

    if closed:
        fiscal_year.close_period(1)
        fiscal_year.close_period(2)
        fiscal_year.close_period(3)
        fiscal_year.close_year()

    fiscal_year.pull_events()
    return fiscal_year


def _ledger_account(*, account_id: UUID, number: str, active: bool = True) -> LedgerAccount:
    account = LedgerAccount(
        id=account_id,
        account_number=AccountNumber(number),
        name=f"Account {number}",
        account_type=AccountType.ASSET,
        normal_balance=NormalBalance.DEBIT,
        active=active,
        locked=False,
        has_postings=False,
    )
    account.pull_events()
    return account


def _journal(
    *,
    journal_id: UUID,
    number: str,
    posting_date: date,
    reference: str,
    debit_account_id: UUID,
    credit_account_id: UUID,
    description: str = "Membership posting",
) -> Journal:
    journal = Journal(
        id=journal_id,
        journal_number=number,
        posting_date=posting_date,
        description=description,
        reference=reference,
        lines=[
            JournalLine(
                account_id=debit_account_id,
                side=PostingSide.DEBIT,
                amount=Money(amount=Decimal("150.00"), currency=Currency.DKK),
                description="Receivable",
            ),
            JournalLine(
                account_id=credit_account_id,
                side=PostingSide.CREDIT,
                amount=Money(amount=Decimal("150.00"), currency=Currency.DKK),
                description="Revenue",
            ),
        ],
        status=JournalEntryStatus.DRAFT,
    )
    journal.pull_events()
    return journal


def test_journal_repository_create_read_exists_list_and_search(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-accounting-journal-basic.sqlite"
    session = _new_session(db_path)
    try:
        uow = UnitOfWork(session)
        fiscal_year_repository = SQLiteFiscalYearRepository(uow)
        journal_repository = SQLiteJournalRepository(uow)

        fiscal_year_repository.add(_fiscal_year(year=2026))

        first = _journal(
            journal_id=UUID("00000000-0000-0000-0000-00000000A101"),
            number="JRN-2026-0001",
            posting_date=date(2026, 1, 10),
            reference="INV-2026-0001",
            debit_account_id=UUID("00000000-0000-0000-0000-00000000B101"),
            credit_account_id=UUID("00000000-0000-0000-0000-00000000B102"),
        )
        second = _journal(
            journal_id=UUID("00000000-0000-0000-0000-00000000A102"),
            number="JRN-2026-0002",
            posting_date=date(2026, 2, 12),
            reference="INV-2026-0002",
            debit_account_id=UUID("00000000-0000-0000-0000-00000000B103"),
            credit_account_id=UUID("00000000-0000-0000-0000-00000000B104"),
            description="Equipment procurement",
        )

        journal_repository.add(second)
        journal_repository.add(first)
        session.commit()

        loaded = journal_repository.get_by_id(first.id)
        assert loaded is not None
        assert loaded.id == first.id
        assert loaded.journal_number == "JRN-2026-0001"
        assert loaded.reference == "INV-2026-0001"

        assert journal_repository.exists(first.id) is True
        assert (
            journal_repository.exists(UUID("00000000-0000-0000-0000-00000000A1FF"))
            is False
        )

        listed = journal_repository.list()
        assert [item.journal_number for item in listed] == ["JRN-2026-0001", "JRN-2026-0002"]

        by_number = journal_repository.get_by_number(
            fiscal_year=2026,
            journal_number="jrn-2026-0002",
        )
        assert by_number is not None
        assert by_number.id == second.id

        by_reference = journal_repository.list_by_reference("INV-2026-0002")
        assert [item.journal_number for item in by_reference] == ["JRN-2026-0002"]

        by_period = journal_repository.list_by_posting_date_range(
            start_date=date(2026, 2, 1),
            end_date=date(2026, 2, 28),
        )
        assert [item.journal_number for item in by_period] == ["JRN-2026-0002"]

        text_hits = journal_repository.search("Equipment")
        assert [row["journal_number"] for row in text_hits] == ["JRN-2026-0002"]

        status_hits = journal_repository.search({"status": "DRAFT"})
        assert [row["journal_number"] for row in status_hits] == [
            "JRN-2026-0001",
            "JRN-2026-0002",
        ]
    finally:
        session.close()


def test_journal_repository_update_remove_and_version_roundtrip(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-accounting-journal-update.sqlite"
    first_session = _new_session(db_path)
    try:
        uow = UnitOfWork(first_session)
        fiscal_year_repository = SQLiteFiscalYearRepository(uow)
        journal_repository = SQLiteJournalRepository(uow)

        fiscal_year_repository.add(_fiscal_year(year=2027))
        journal = _journal(
            journal_id=UUID("00000000-0000-0000-0000-00000000A201"),
            number="JRN-2027-0001",
            posting_date=date(2027, 1, 15),
            reference="INV-2027-0001",
            debit_account_id=UUID("00000000-0000-0000-0000-00000000B201"),
            credit_account_id=UUID("00000000-0000-0000-0000-00000000B202"),
        )
        journal_repository.add(journal)
        first_session.commit()

        loaded = journal_repository.get_by_id(journal.id)
        assert loaded is not None
        loaded.description = "Membership posting updated"
        loaded.reference = "INV-2027-UPDATED"

        journal_repository.update(loaded)
        first_session.commit()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        journal_repository = SQLiteJournalRepository(UnitOfWork(second_session))
        restored = journal_repository.get_by_id(
            UUID("00000000-0000-0000-0000-00000000A201")
        )

        assert restored is not None
        assert restored.description == "Membership posting updated"
        assert restored.reference == "INV-2027-UPDATED"
        assert restored.version == 2

        journal_repository.remove(restored.id)
        second_session.commit()

        assert journal_repository.get_by_id(restored.id) is None

        with pytest.raises(ValueError):
            journal_repository.remove(restored.id)
    finally:
        second_session.close()


def test_journal_repository_duplicate_number_within_fiscal_year_rejected(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "sqlite-accounting-journal-duplicate.sqlite"
    session = _new_session(db_path)
    try:
        uow = UnitOfWork(session)
        fiscal_year_repository = SQLiteFiscalYearRepository(uow)
        journal_repository = SQLiteJournalRepository(uow)

        fiscal_year_repository.add(_fiscal_year(year=2028))

        first = _journal(
            journal_id=UUID("00000000-0000-0000-0000-00000000A301"),
            number="JRN-2028-0001",
            posting_date=date(2028, 1, 10),
            reference="INV-2028-0001",
            debit_account_id=UUID("00000000-0000-0000-0000-00000000B301"),
            credit_account_id=UUID("00000000-0000-0000-0000-00000000B302"),
        )
        duplicate = _journal(
            journal_id=UUID("00000000-0000-0000-0000-00000000A302"),
            number="JRN-2028-0001",
            posting_date=date(2028, 2, 10),
            reference="INV-2028-0002",
            debit_account_id=UUID("00000000-0000-0000-0000-00000000B303"),
            credit_account_id=UUID("00000000-0000-0000-0000-00000000B304"),
        )

        journal_repository.add(first)
        session.commit()

        with pytest.raises(ValueError):
            journal_repository.add(duplicate)
    finally:
        session.close()


def test_ledger_account_repository_roundtrip_duplicate_and_active_listing(tmp_path: Path) -> None:
    db_path = tmp_path / "sqlite-accounting-ledger.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteLedgerAccountRepository(UnitOfWork(session))

        active = _ledger_account(
            account_id=UUID("00000000-0000-0000-0000-00000000C101"),
            number="1100-AR",
            active=True,
        )
        inactive = _ledger_account(
            account_id=UUID("00000000-0000-0000-0000-00000000C102"),
            number="4100-SALES",
            active=False,
        )

        repository.add(active)
        repository.add(inactive)
        session.commit()

        loaded = repository.get_by_id(active.id)
        assert loaded is not None
        assert loaded.account_number.value == "1100-AR"

        by_number = repository.get_by_number(AccountNumber("4100-sales"))
        assert by_number is not None
        assert by_number.id == inactive.id

        all_accounts = repository.list()
        assert [account.account_number.value for account in all_accounts] == [
            "1100-AR",
            "4100-SALES",
        ]

        active_accounts = repository.list_active()
        assert [account.account_number.value for account in active_accounts] == ["1100-AR"]

        loaded.rename(name="Accounts Receivable Updated")
        repository.update(loaded)
        session.commit()

        updated = repository.get_by_id(active.id)
        assert updated is not None
        assert updated.name == "Accounts Receivable Updated"
        assert repository.exists(active.id) is True
        assert repository.exists(UUID("00000000-0000-0000-0000-00000000C1FF")) is False

        LedgerAccount._registered_numbers.clear()
        duplicate = _ledger_account(
            account_id=uuid4(),
            number="1100-AR",
            active=True,
        )
        with pytest.raises(ValueError):
            repository.add(duplicate)
    finally:
        session.close()


def test_fiscal_year_repository_roundtrip_getters_update_and_closed_reconstruction(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "sqlite-accounting-fiscal-year.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteFiscalYearRepository(UnitOfWork(session))

        closed_year = _fiscal_year(year=2030, closed=True)
        open_year = _fiscal_year(year=2029)

        repository.add(open_year)
        repository.add(closed_year)
        session.commit()

        fetched_open = repository.get_open()
        assert fetched_open is not None
        assert fetched_open.year == 2029

        fetched_by_id = repository.get_by_id(closed_year.id)
        assert fetched_by_id is not None
        assert fetched_by_id.status is FiscalYearStatus.CLOSED
        assert all(period.closed for period in fetched_by_id.periods)

        fetched_by_year = repository.get_by_year(2029)
        assert fetched_by_year is not None
        fetched_by_year.close_period(1)

        repository.update(fetched_by_year)
        session.commit()

        updated = repository.get_by_year(2029)
        assert updated is not None
        assert updated.periods[0].closed is True

        listed = repository.list()
        assert [year.year for year in listed] == [2029, 2030]

        with pytest.raises(ValueError):
            repository.add(_fiscal_year(year=2029))
    finally:
        session.close()
