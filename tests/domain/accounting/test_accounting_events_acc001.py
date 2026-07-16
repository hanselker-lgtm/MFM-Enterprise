from uuid import uuid4

from mfm.common.domain_event import DomainEvent
from mfm.domain.accounting.events import ChartOfAccountsLocked
from mfm.domain.accounting.events import ClosingBalanceFinalized
from mfm.domain.accounting.events import FiscalPeriodClosed
from mfm.domain.accounting.events import FiscalPeriodReopened
from mfm.domain.accounting.events import FiscalYearArchived
from mfm.domain.accounting.events import FiscalYearClosed
from mfm.domain.accounting.events import FiscalYearReopened
from mfm.domain.accounting.events import JournalEntryDrafted
from mfm.domain.accounting.events import JournalEntryPosted
from mfm.domain.accounting.events import JournalEntryReversed
from mfm.domain.accounting.events import LedgerAccountCreated
from mfm.domain.accounting.events import LedgerAccountLocked
from mfm.domain.accounting.events import LedgerAccountRenamed
from mfm.domain.accounting.events import OpeningBalanceRegistered


def test_all_accounting_events_are_domain_events():
    chart_id = uuid4()
    account_id = uuid4()
    journal_id = uuid4()
    fiscal_year_id = uuid4()

    events = [
        ChartOfAccountsLocked(chart_id=chart_id),
        LedgerAccountCreated(account_id=account_id, account_number="1000"),
        LedgerAccountRenamed(account_id=account_id, name="Receivable"),
        LedgerAccountLocked(account_id=account_id),
        JournalEntryDrafted(journal_id=journal_id, journal_number="JRN-1"),
        JournalEntryPosted(journal_id=journal_id, journal_number="JRN-1"),
        JournalEntryReversed(journal_id=journal_id, journal_number="JRN-1"),
        FiscalPeriodClosed(fiscal_year_id=fiscal_year_id, period_number=1),
        FiscalPeriodReopened(fiscal_year_id=fiscal_year_id, period_number=1),
        FiscalYearClosed(fiscal_year_id=fiscal_year_id, year=2026),
        FiscalYearReopened(fiscal_year_id=fiscal_year_id, year=2026),
        FiscalYearArchived(fiscal_year_id=fiscal_year_id, year=2026),
        OpeningBalanceRegistered(fiscal_year_id=fiscal_year_id),
        ClosingBalanceFinalized(fiscal_year_id=fiscal_year_id),
    ]

    for event in events:
        assert isinstance(event, DomainEvent)
        assert event.event_id is not None
