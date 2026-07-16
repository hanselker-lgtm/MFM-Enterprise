from mfm.domain.accounting.repositories import FiscalYearRepository
from mfm.domain.accounting.repositories import JournalRepository
from mfm.domain.accounting.repositories import LedgerAccountRepository


def test_repository_contracts_expose_expected_methods():
    journal_methods = {
        "add",
        "get_by_id",
        "get_by_number",
        "update",
        "list",
        "list_by_reference",
        "list_by_posting_date_range",
    }
    ledger_methods = {
        "add",
        "get_by_id",
        "get_by_number",
        "update",
        "list",
        "list_active",
    }
    fiscal_methods = {
        "add",
        "get_by_id",
        "get_by_year",
        "get_open",
        "update",
        "list",
    }

    assert journal_methods.issubset(set(JournalRepository.__dict__))
    assert ledger_methods.issubset(set(LedgerAccountRepository.__dict__))
    assert fiscal_methods.issubset(set(FiscalYearRepository.__dict__))
