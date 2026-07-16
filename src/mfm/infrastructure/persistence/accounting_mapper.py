"""Mapper between accounting domain and persistence models."""

from __future__ import annotations

from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.fiscal_period import FiscalPeriod
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.journal import Journal
from mfm.domain.accounting.journal_line import JournalLine
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.accounting.money import Money
from mfm.infrastructure.persistence.accounting.fiscal_period_model import FiscalPeriodModel
from mfm.infrastructure.persistence.accounting.fiscal_year_model import FiscalYearModel
from mfm.infrastructure.persistence.accounting.journal_entry_model import JournalEntryModel
from mfm.infrastructure.persistence.accounting.journal_line_model import JournalLineModel
from mfm.infrastructure.persistence.accounting.journal_model import JournalModel
from mfm.infrastructure.persistence.accounting.ledger_account_model import LedgerAccountModel


class AccountingMapper:
    """Map accounting aggregates to/from SQLAlchemy models."""

    @staticmethod
    def to_orm_journal(*, journal: Journal, fiscal_year_id) -> JournalModel:
        orm = JournalModel(
            id=journal.id,
            fiscal_year_id=fiscal_year_id,
            journal_number=journal.journal_number,
            posting_date=journal.posting_date,
            description=journal.description,
            reference=journal.reference,
            status=journal.status,
            version=journal.version,
        )

        entry = JournalEntryModel(
            id=journal.id,
            journal_id=journal.id,
            entry_order=0,
            posting_date=journal.posting_date,
            description=journal.description,
            reference=journal.reference,
            status=journal.status,
        )

        for line_order, line in enumerate(journal.lines):
            entry.lines.append(
                JournalLineModel(
                    journal_entry_id=journal.id,
                    line_order=line_order,
                    account_id=line.account_id,
                    side=line.side,
                    amount=line.amount.amount,
                    currency=line.amount.currency,
                    description=line.description,
                )
            )

        orm.entries.append(entry)
        return orm

    @staticmethod
    def to_domain_journal(orm: JournalModel) -> Journal:
        if not orm.entries:
            raise ValueError("journal persistence row must contain one entry")

        entry_orm = sorted(orm.entries, key=lambda item: item.entry_order)[0]
        lines = [
            JournalLine(
                account_id=line_orm.account_id,
                side=line_orm.side,
                amount=Money(amount=line_orm.amount, currency=line_orm.currency),
                description=line_orm.description,
            )
            for line_orm in sorted(entry_orm.lines, key=lambda item: item.line_order)
        ]

        journal = Journal(
            id=orm.id,
            journal_number=orm.journal_number,
            posting_date=entry_orm.posting_date,
            description=entry_orm.description,
            lines=lines,
            reference=entry_orm.reference,
            status=entry_orm.status,
        )
        journal.version = orm.version
        journal.pull_events()
        return journal

    @staticmethod
    def to_orm_ledger_account(account: LedgerAccount) -> LedgerAccountModel:
        return LedgerAccountModel(
            id=account.id,
            account_number=account.account_number.value,
            name=account.name,
            account_type=account.account_type,
            normal_balance=account.normal_balance,
            active=account.active,
            locked=account.locked,
            has_postings=account.has_postings,
        )

    @staticmethod
    def to_domain_ledger_account(orm: LedgerAccountModel) -> LedgerAccount:
        account = LedgerAccount(
            id=orm.id,
            account_number=AccountNumber(orm.account_number),
            name=orm.name,
            account_type=orm.account_type,
            normal_balance=orm.normal_balance,
            active=orm.active,
            locked=orm.locked,
            has_postings=orm.has_postings,
        )
        account.pull_events()
        return account

    @staticmethod
    def to_orm_fiscal_year(fiscal_year: FiscalYear) -> FiscalYearModel:
        orm = FiscalYearModel(
            id=fiscal_year.id,
            year=fiscal_year.year,
            start_date=fiscal_year.start_date,
            end_date=fiscal_year.end_date,
            status=fiscal_year.status,
        )

        for period in sorted(fiscal_year.periods, key=lambda item: item.number):
            orm.periods.append(
                FiscalPeriodModel(
                    fiscal_year_id=fiscal_year.id,
                    number=period.number,
                    start_date=period.start_date,
                    end_date=period.end_date,
                    closed=period.closed,
                )
            )

        return orm

    @staticmethod
    def to_domain_fiscal_year(orm: FiscalYearModel) -> FiscalYear:
        periods = [
            FiscalPeriod(
                number=period_orm.number,
                start_date=period_orm.start_date,
                end_date=period_orm.end_date,
                closed=period_orm.closed,
            )
            for period_orm in sorted(orm.periods, key=lambda item: item.number)
        ]

        fiscal_year = FiscalYear(
            id=orm.id,
            year=orm.year,
            start_date=orm.start_date,
            end_date=orm.end_date,
            periods=periods,
            status=orm.status,
        )

        for journal_orm in orm.journals:
            fiscal_year.register_journal_number(journal_orm.journal_number)

        fiscal_year.pull_events()
        return fiscal_year
