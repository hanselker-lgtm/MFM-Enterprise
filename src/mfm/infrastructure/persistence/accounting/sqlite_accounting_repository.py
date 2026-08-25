"""SQLite repositories for accounting aggregates."""

from __future__ import annotations

from collections.abc import Mapping
from datetime import date
from typing import Any
from typing import cast
from uuid import UUID

from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus
from mfm.domain.accounting.journal import Journal
from mfm.domain.accounting.journal_entry import JournalEntryStatus
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.accounting.repositories import FiscalYearRepository
from mfm.domain.accounting.repositories import JournalRepository
from mfm.domain.accounting.repositories import LedgerAccountRepository
from mfm.infrastructure.persistence.accounting.fiscal_year_model import FiscalYearModel
from mfm.infrastructure.persistence.accounting.journal_entry_model import JournalEntryModel
from mfm.infrastructure.persistence.accounting.journal_model import JournalModel
from mfm.infrastructure.persistence.accounting.ledger_account_model import LedgerAccountModel
from mfm.infrastructure.persistence.accounting_mapper import AccountingMapper
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteJournalRepository(JournalRepository):
    """SQLAlchemy-backed repository for Journal aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, journal: Journal) -> None:
        fiscal_year = self._session.scalar(
            select(FiscalYearModel).where(FiscalYearModel.year == journal.posting_date.year)
        )
        if fiscal_year is None:
            raise ValueError(f"Fiscal year {journal.posting_date.year} does not exist")

        if self._session.scalar(
            select(JournalModel.id).where(
                and_(
                    JournalModel.fiscal_year_id == fiscal_year.id,
                    JournalModel.journal_number == journal.journal_number,
                )
            )
        ) is not None:
            raise ValueError(
                f"Journal number {journal.journal_number} already exists in fiscal year {fiscal_year.year}"
            )

        self._session.add(
            AccountingMapper.to_orm_journal(journal=journal, fiscal_year_id=fiscal_year.id)
        )
        self._session.flush()

    def get(self, journal_id: UUID) -> Journal | None:
        orm = self._session.scalar(self._base_query().where(JournalModel.id == journal_id))
        if orm is None:
            return None
        return AccountingMapper.to_domain_journal(orm)

    def get_by_id(self, journal_id: UUID) -> Journal | None:
        return self.get(journal_id)

    def get_by_number(self, *, fiscal_year: int, journal_number: str) -> Journal | None:
        orm = self._session.scalar(
            self._base_query()
            .join(JournalModel.fiscal_year)
            .where(
                FiscalYearModel.year == fiscal_year,
                JournalModel.journal_number == journal_number.strip().upper(),
            )
        )
        if orm is None:
            return None
        return AccountingMapper.to_domain_journal(orm)

    def update(self, journal: Journal) -> None:
        existing = self._session.scalar(
            self._base_query().where(JournalModel.id == journal.id)
        )
        if existing is None:
            raise ValueError(f"Journal {journal.id} does not exist")

        fiscal_year = self._session.scalar(
            select(FiscalYearModel).where(FiscalYearModel.year == journal.posting_date.year)
        )
        if fiscal_year is None:
            raise ValueError(f"Fiscal year {journal.posting_date.year} does not exist")

        duplicate = self._session.scalar(
            select(JournalModel.id).where(
                and_(
                    JournalModel.fiscal_year_id == fiscal_year.id,
                    JournalModel.journal_number == journal.journal_number,
                    JournalModel.id != journal.id,
                )
            )
        )
        if duplicate is not None:
            raise ValueError(
                f"Journal number {journal.journal_number} already exists in fiscal year {fiscal_year.year}"
            )

        if existing.version != journal.version:
            raise ValueError(
                f"Journal {journal.id} version conflict: expected {existing.version}, got {journal.version}"
            )

        existing.entries.clear()
        self._session.flush()

        updated = AccountingMapper.to_orm_journal(journal=journal, fiscal_year_id=fiscal_year.id)
        updated.version = journal.version + 1
        self._session.merge(updated)
        self._session.flush()

    def remove(self, journal_id: UUID) -> None:
        orm = self._session.get(JournalModel, journal_id)
        if orm is None:
            raise ValueError(f"Journal {journal_id} does not exist")
        self._session.delete(orm)
        self._session.flush()

    def exists(self, journal_id: UUID) -> bool:
        return self._session.get(JournalModel, journal_id) is not None

    def list(self) -> list[Journal]:
        orm_entities = self._session.scalars(
            self._base_query().order_by(JournalModel.journal_number, JournalModel.posting_date)
        ).unique().all()
        return [AccountingMapper.to_domain_journal(orm) for orm in orm_entities]

    def list_by_reference(self, reference: str) -> list[Journal]:
        normalized = reference.strip()
        orm_entities = self._session.scalars(
            self._base_query()
            .where(JournalModel.reference == normalized)
            .order_by(JournalModel.journal_number, JournalModel.posting_date)
        ).unique().all()
        return [AccountingMapper.to_domain_journal(orm) for orm in orm_entities]

    def list_by_posting_date_range(self, *, start_date: date, end_date: date) -> list[Journal]:
        orm_entities = self._session.scalars(
            self._base_query()
            .where(JournalModel.posting_date >= start_date, JournalModel.posting_date <= end_date)
            .order_by(JournalModel.posting_date, JournalModel.journal_number)
        ).unique().all()
        return [AccountingMapper.to_domain_journal(orm) for orm in orm_entities]

    def search(self, criteria: Any) -> list[Any]:
        if isinstance(criteria, str):
            text = criteria.strip()
            filters: dict[str, Any] = {"text": text} if text else {}
        elif isinstance(criteria, Mapping):
            filters = dict(criteria)
        else:
            filters = {}

        query = select(JournalModel).join(JournalModel.fiscal_year)

        text = str(filters.get("text", "")).strip()
        if text:
            like_pattern = f"%{text}%"
            query = query.where(
                or_(
                    JournalModel.journal_number.ilike(like_pattern),
                    JournalModel.description.ilike(like_pattern),
                    JournalModel.reference.ilike(like_pattern),
                )
            )

        fiscal_year = filters.get("fiscal_year")
        if fiscal_year is not None:
            query = query.where(FiscalYearModel.year == int(fiscal_year))

        status = filters.get("status")
        if status is not None:
            normalized_status = (
                status
                if isinstance(status, JournalEntryStatus)
                else JournalEntryStatus(str(status).upper())
            )
            query = query.where(JournalModel.status == normalized_status)

        entities = self._session.scalars(
            query.order_by(JournalModel.journal_number, JournalModel.posting_date)
        ).unique().all()

        return [
            {
                "id": orm.id,
                "fiscal_year_id": orm.fiscal_year_id,
                "journal_number": orm.journal_number,
                "posting_date": orm.posting_date,
                "status": orm.status,
                "reference": orm.reference,
            }
            for orm in entities
        ]

    @staticmethod
    def _base_query():
        return select(JournalModel).options(
            joinedload(JournalModel.entries).joinedload(JournalEntryModel.lines),
            joinedload(JournalModel.fiscal_year),
        )


class SQLiteLedgerAccountRepository(LedgerAccountRepository):
    """SQLAlchemy-backed repository for LedgerAccount aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, account: LedgerAccount) -> None:
        number = account.account_number.value
        if self._session.scalar(
            select(LedgerAccountModel.id).where(LedgerAccountModel.account_number == number)
        ) is not None:
            raise ValueError(f"Ledger account number {number} already exists")

        self._session.add(AccountingMapper.to_orm_ledger_account(account))
        self._session.flush()

    def get(self, account_id: UUID) -> LedgerAccount | None:
        orm = self._session.get(LedgerAccountModel, account_id)
        if orm is None:
            return None
        return self._to_domain(orm)

    def get_by_id(self, account_id: UUID) -> LedgerAccount | None:
        return self.get(account_id)

    def get_by_number(self, account_number: AccountNumber) -> LedgerAccount | None:
        orm = self._session.scalar(
            select(LedgerAccountModel).where(
                LedgerAccountModel.account_number == account_number.value
            )
        )
        if orm is None:
            return None
        return self._to_domain(orm)

    def update(self, account: LedgerAccount) -> None:
        existing = self._session.get(LedgerAccountModel, account.id)
        if existing is None:
            raise ValueError(f"Ledger account {account.id} does not exist")

        duplicate = self._session.scalar(
            select(LedgerAccountModel.id).where(
                LedgerAccountModel.account_number == account.account_number.value,
                LedgerAccountModel.id != account.id,
            )
        )
        if duplicate is not None:
            raise ValueError(
                f"Ledger account number {account.account_number.value} already exists"
            )

        existing.account_number = account.account_number.value
        existing.name = account.name
        existing.account_type = account.account_type
        existing.normal_balance = account.normal_balance
        existing.active = account.active
        existing.locked = account.locked
        existing.has_postings = account.has_postings
        self._session.flush()

    def exists(self, account_id: UUID) -> bool:
        return self._session.get(LedgerAccountModel, account_id) is not None

    def list(self) -> list[LedgerAccount]:
        orm_entities = self._session.scalars(
            select(LedgerAccountModel).order_by(LedgerAccountModel.account_number)
        ).all()
        return [self._to_domain(orm) for orm in orm_entities]

    def list_active(self) -> list[LedgerAccount]:
        orm_entities = self._session.scalars(
            select(LedgerAccountModel)
            .where(LedgerAccountModel.active.is_(True))
            .order_by(LedgerAccountModel.account_number)
        ).all()
        return [self._to_domain(orm) for orm in orm_entities]

    @staticmethod
    def _to_domain(orm: LedgerAccountModel) -> LedgerAccount:
        LedgerAccount._registered_numbers.discard(orm.account_number)
        return AccountingMapper.to_domain_ledger_account(orm)


class SQLiteFiscalYearRepository(FiscalYearRepository):
    """SQLAlchemy-backed repository for FiscalYear aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, fiscal_year: FiscalYear) -> None:
        if self._session.scalar(
            select(FiscalYearModel.id).where(FiscalYearModel.year == fiscal_year.year)
        ) is not None:
            raise ValueError(f"Fiscal year {fiscal_year.year} already exists")

        self._session.add(AccountingMapper.to_orm_fiscal_year(fiscal_year))
        self._session.flush()

    def get(self, fiscal_year_id: UUID) -> FiscalYear | None:
        orm = self._session.scalar(self._base_query().where(FiscalYearModel.id == fiscal_year_id))
        if orm is None:
            return None
        return AccountingMapper.to_domain_fiscal_year(orm)

    def get_by_id(self, fiscal_year_id: UUID) -> FiscalYear | None:
        return self.get(fiscal_year_id)

    def get_by_year(self, year: int) -> FiscalYear | None:
        orm = self._session.scalar(self._base_query().where(FiscalYearModel.year == year))
        if orm is None:
            return None
        return AccountingMapper.to_domain_fiscal_year(orm)

    def get_open(self) -> FiscalYear | None:
        orm = self._session.scalar(
            self._base_query().where(FiscalYearModel.status == FiscalYearStatus.OPEN)
        )
        if orm is None:
            return None
        return AccountingMapper.to_domain_fiscal_year(orm)

    def ensure_posting_allowed(self, posting_date: date) -> None:
        """Raise if no fiscal year covers ``posting_date`` for posting.

        Delegates to :meth:`FiscalYear.ensure_posting_allowed`, which
        already implements the open/closed/archived and period checks
        -- this just resolves the right fiscal year first. Not part
        of the original ``FiscalYearRepository`` ABC, but required by
        :class:`mfm.application.features.annual_contingent_generation.
        AnnualContingentGenerationFeature`'s narrower protocol of the
        same name; both are satisfied by this same object.
        """

        fiscal_year = self.get_by_year(posting_date.year)
        if fiscal_year is None:
            raise ValueError(f"Fiscal year {posting_date.year} does not exist")
        fiscal_year.ensure_posting_allowed(posting_date)

    def update(self, fiscal_year: FiscalYear) -> None:
        existing = self._session.scalar(
            self._base_query().where(FiscalYearModel.id == fiscal_year.id)
        )
        if existing is None:
            raise ValueError(f"Fiscal year {fiscal_year.id} does not exist")

        duplicate = self._session.scalar(
            select(FiscalYearModel.id).where(
                FiscalYearModel.year == fiscal_year.year,
                FiscalYearModel.id != fiscal_year.id,
            )
        )
        if duplicate is not None:
            raise ValueError(f"Fiscal year {fiscal_year.year} already exists")

        existing.periods.clear()
        self._session.flush()

        updated = AccountingMapper.to_orm_fiscal_year(fiscal_year)
        self._session.merge(updated)
        self._session.flush()

    def list(self) -> list[FiscalYear]:
        orm_entities = self._session.scalars(
            self._base_query().order_by(FiscalYearModel.year)
        ).unique().all()
        return [AccountingMapper.to_domain_fiscal_year(orm) for orm in orm_entities]

    @staticmethod
    def _base_query():
        return select(FiscalYearModel).options(
            joinedload(FiscalYearModel.periods),
            joinedload(FiscalYearModel.journals),
        )
