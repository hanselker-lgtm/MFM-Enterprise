from __future__ import annotations

from datetime import date
from decimal import Decimal
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.engine import Connection
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.account_type import AccountType
from mfm.domain.accounting.fiscal_period import FiscalPeriod
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus
from mfm.domain.accounting.journal import Journal
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.accounting.normal_balance import NormalBalance
from mfm.domain.accounting.posting_side import PostingSide
from mfm.domain.finance.currency import Currency
from mfm.domain.finance.money import Money
from mfm.infrastructure.persistence.accounting.fiscal_year_model import FiscalYearModel
from mfm.infrastructure.persistence.accounting.journal_model import JournalModel
from mfm.infrastructure.persistence.accounting.ledger_account_model import LedgerAccountModel
from mfm.infrastructure.persistence.accounting_mapper import AccountingMapper


@pytest.fixture(autouse=True)
def _reset_accounting_class_state():
    LedgerAccount._registered_numbers.clear()
    FiscalYear._open_year_id = None
    yield
    LedgerAccount._registered_numbers.clear()
    FiscalYear._open_year_id = None


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    connection = engine.connect()
    BaseModel.metadata.create_all(connection)
    session = Session(bind=connection)
    session.info["test_connection"] = connection
    session.info["test_engine"] = engine
    return session


def _close_session(session: Session) -> None:
    connection = session.info.pop("test_connection", None)
    engine = session.info.pop("test_engine", None)
    session.close()
    if isinstance(connection, Connection):
        connection.close()
    if isinstance(engine, Engine):
        engine.dispose()


def _fiscal_year(*, year: int = 2026) -> FiscalYear:
    feb_end_day = 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28
    return FiscalYear(
        id=UUID(f"00000000-0000-0000-0000-00000000{year % 10000:04d}"),
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


def _ledger_account(*, number: str = "1100-AR") -> LedgerAccount:
    return LedgerAccount(
        id=uuid4(),
        account_number=AccountNumber(number),
        name="Accounts Receivable",
        account_type=AccountType.ASSET,
        normal_balance=NormalBalance.DEBIT,
        active=True,
        locked=False,
        has_postings=False,
    )


def _journal(*, number: str = "JRN-2026-0001") -> Journal:
    return Journal(
        id=UUID("00000000-0000-0000-0000-00000000A001"),
        journal_number=number,
        posting_date=date(2026, 1, 15),
        description="Membership contingent posting",
        reference="INV-2026-0001",
        lines=[
            JournalLine(
                account_id=UUID("00000000-0000-0000-0000-00000000B001"),
                side=PostingSide.DEBIT,
                amount=Money(amount=Decimal("100.00"), currency=Currency.DKK),
                description="Receivable",
            ),
            JournalLine(
                account_id=UUID("00000000-0000-0000-0000-00000000B002"),
                side=PostingSide.CREDIT,
                amount=Money(amount=Decimal("100.00"), currency=Currency.DKK),
                description="Revenue",
            ),
        ],
    )


def test_accounting_model_creation_registers_tables(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "accounting-models")
    try:
        inspector = inspect(session.info["test_connection"])
        tables = set(inspector.get_table_names())

        assert "ledger_account" in tables
        assert "fiscal_year" in tables
        assert "fiscal_period" in tables
        assert "journal" in tables
        assert "journal_entry" in tables
        assert "journal_line" in tables
    finally:
        _close_session(session)


def test_domain_to_orm_mapping_persists_journal_with_multiple_lines(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "journal-domain-to-orm")
    try:
        fiscal_year = _fiscal_year(year=2026)
        fy_orm = AccountingMapper.to_orm_fiscal_year(fiscal_year)
        session.add(fy_orm)
        session.flush()

        journal = _journal(number="JRN-2026-0100")
        journal_orm = AccountingMapper.to_orm_journal(journal=journal, fiscal_year_id=fiscal_year.id)
        session.add(journal_orm)
        session.commit()

        loaded = session.get(JournalModel, journal.id)
        assert loaded is not None
        assert loaded.journal_number == "JRN-2026-0100"
        assert len(loaded.entries) == 1
        assert len(loaded.entries[0].lines) == 2
        assert loaded.entries[0].lines[0].amount == Decimal("100.00")
        assert loaded.entries[0].lines[1].currency == Currency.DKK
    finally:
        _close_session(session)


def test_orm_to_domain_mapping_restores_journal_without_information_loss(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "journal-orm-to-domain")
    try:
        fiscal_year = _fiscal_year(year=2026)
        session.add(AccountingMapper.to_orm_fiscal_year(fiscal_year))
        journal = _journal(number="JRN-2026-0200")
        session.add(AccountingMapper.to_orm_journal(journal=journal, fiscal_year_id=fiscal_year.id))
        session.commit()
        session.expunge_all()

        loaded = session.get(JournalModel, journal.id)
        assert loaded is not None
        restored = AccountingMapper.to_domain_journal(loaded)

        assert restored.id == journal.id
        assert restored.journal_number == journal.journal_number
        assert restored.posting_date == journal.posting_date
        assert restored.description == journal.description
        assert restored.reference == journal.reference
        assert len(restored.lines) == 2
        assert restored.lines[0].description == "Receivable"
        assert restored.lines[1].amount == Money(amount=Decimal("100.00"), currency=Currency.DKK)
        assert restored.pull_events() == []
    finally:
        _close_session(session)


def test_roundtrip_preserves_fiscal_year_and_periods(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "fiscal-year-roundtrip")
    try:
        fiscal_year = _fiscal_year(year=2027)
        fiscal_year.close_period(2)

        fy_orm = AccountingMapper.to_orm_fiscal_year(fiscal_year)
        session.add(fy_orm)
        session.commit()
        session.expunge_all()

        loaded = session.get(FiscalYearModel, fiscal_year.id)
        assert loaded is not None
        restored = AccountingMapper.to_domain_fiscal_year(loaded)

        assert restored.id == fiscal_year.id
        assert restored.year == 2027
        assert restored.status == FiscalYearStatus.OPEN
        assert len(restored.periods) == 3
        assert restored.periods[1].closed is True
    finally:
        _close_session(session)


def test_ledger_account_uniqueness_enforced_by_database_constraint(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "ledger-account-unique")
    try:
        first = AccountingMapper.to_orm_ledger_account(_ledger_account(number="2000-AR"))
        second = AccountingMapper.to_orm_ledger_account(_ledger_account(number="2000-AR-2"))
        second.account_number = "2000-AR"
        session.add(first)
        session.add(second)

        with pytest.raises(Exception):
            session.commit()
    finally:
        _close_session(session)


def test_journal_number_unique_within_fiscal_year_constraint(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "journal-unique-per-fiscal-year")
    try:
        fiscal_year = _fiscal_year(year=2028)
        session.add(AccountingMapper.to_orm_fiscal_year(fiscal_year))
        session.flush()

        first = AccountingMapper.to_orm_journal(
            journal=_journal(number="JRN-2028-0001"),
            fiscal_year_id=fiscal_year.id,
        )
        second_journal = _journal(number="JRN-2028-0002")
        second = AccountingMapper.to_orm_journal(
            journal=second_journal,
            fiscal_year_id=fiscal_year.id,
        )
        second.journal_number = "JRN-2028-0001"

        session.add(first)
        session.add(second)
        with pytest.raises(Exception):
            session.commit()
    finally:
        _close_session(session)


def test_ledger_account_domain_orm_roundtrip(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "ledger-account-roundtrip")
    try:
        original = _ledger_account(number="3000-CASH")
        orm = AccountingMapper.to_orm_ledger_account(original)
        session.add(orm)
        session.commit()
        session.expunge_all()

        loaded = session.get(LedgerAccountModel, original.id)
        assert loaded is not None
        LedgerAccount._registered_numbers.clear()
        restored = AccountingMapper.to_domain_ledger_account(loaded)

        assert restored.id == original.id
        assert restored.account_number.value == "3000-CASH"
        assert restored.name == original.name
        assert restored.account_type == original.account_type
        assert restored.normal_balance == original.normal_balance
    finally:
        _close_session(session)


def test_fiscal_year_mapping_registers_persisted_journal_numbers(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "fiscal-year-journal-register")
    try:
        fiscal_year = _fiscal_year(year=2029)
        session.add(AccountingMapper.to_orm_fiscal_year(fiscal_year))
        session.flush()

        session.add(
            AccountingMapper.to_orm_journal(
                journal=_journal(number="JRN-2029-0001"),
                fiscal_year_id=fiscal_year.id,
            )
        )
        session.commit()
        session.expunge_all()

        loaded_year = session.get(FiscalYearModel, fiscal_year.id)
        assert loaded_year is not None
        restored_year = AccountingMapper.to_domain_fiscal_year(loaded_year)

        with pytest.raises(Exception):
            restored_year.register_journal_number("JRN-2029-0001")
    finally:
        _close_session(session)
