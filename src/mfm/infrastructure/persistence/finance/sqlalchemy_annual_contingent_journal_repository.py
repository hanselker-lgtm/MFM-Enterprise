"""Real, database-backed repository for standalone accounting journal entries.

Backs the narrow ``JournalRepository`` protocol expected by
:class:`mfm.application.features.annual_contingent_generation.
AnnualContingentGenerationFeature` (``add(journal: JournalEntry)``).

This is a different aggregate from :class:`mfm.domain.accounting.
journal.Journal` (the one used by the Accounting workspace), but they
share the same underlying table structure: a ``Journal`` header row
groups one or more ``JournalEntry`` rows, which each group one or more
``JournalLine`` rows. Since a bare draft entry has no natural parent
journal of its own, one is created transparently here, keyed by
fiscal year and the entry's own journal number.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.infrastructure.persistence.accounting.fiscal_year_model import FiscalYearModel
from mfm.domain.accounting.journal_entry import JournalEntry
from mfm.infrastructure.persistence.accounting.journal_entry_model import JournalEntryModel
from mfm.infrastructure.persistence.accounting.journal_line_model import JournalLineModel
from mfm.infrastructure.persistence.accounting.journal_model import JournalModel


class SqlAlchemyAnnualContingentJournalRepository:
    """Persists standalone :class:`JournalEntry` drafts via the Journal tables."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, journal: JournalEntry) -> None:
        fiscal_year = self._session.scalar(
            select(FiscalYearModel).where(FiscalYearModel.year == journal.posting_date.year)
        )
        if fiscal_year is None:
            raise ValueError(f"Fiscal year {journal.posting_date.year} does not exist")

        journal_header = JournalModel(
            fiscal_year_id=fiscal_year.id,
            journal_number=journal.journal_number,
            posting_date=journal.posting_date,
            description=journal.description,
            reference=journal.reference,
            status=journal.status,
        )
        journal_entry_row = JournalEntryModel(
            entry_order=0,
            posting_date=journal.posting_date,
            description=journal.description,
            reference=journal.reference,
            status=journal.status,
        )
        journal_entry_row.lines = [
            JournalLineModel(
                line_order=index,
                account_id=line.account_id,
                side=line.side,
                amount=line.amount.amount,
                currency=line.amount.currency,
                description=line.description,
            )
            for index, line in enumerate(journal.lines)
        ]
        journal_header.entries = [journal_entry_row]

        self._session.add(journal_header)
        self._session.flush()
