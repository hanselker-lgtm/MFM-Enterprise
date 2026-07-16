"""Accounting public feature API."""

from mfm.application.features.accounting.close_fiscal_year_feature import (
    CloseFiscalYearFeature,
)
from mfm.application.features.accounting.close_fiscal_year_feature import (
    CloseFiscalYearRequest,
)
from mfm.application.features.accounting.close_fiscal_year_feature import (
    CloseFiscalYearResponse,
)
from mfm.application.features.accounting.close_fiscal_year_feature import (
    CloseFiscalYearService,
)
from mfm.application.features.accounting.create_fiscal_year_feature import (
    CreateFiscalYearFeature,
)
from mfm.application.features.accounting.create_fiscal_year_feature import (
    CreateFiscalYearRequest,
)
from mfm.application.features.accounting.create_fiscal_year_feature import (
    CreateFiscalYearResponse,
)
from mfm.application.features.accounting.create_fiscal_year_feature import (
    CreateFiscalYearService,
)
from mfm.application.features.accounting.create_fiscal_year_feature import (
    FiscalPeriodInput,
)
from mfm.application.features.accounting.create_fiscal_year_feature import (
    FiscalPeriodResponse,
)
from mfm.application.features.accounting.create_fiscal_year_feature import (
    FiscalYearResponse,
)
from mfm.application.features.accounting.create_journal_feature import (
    ApplicationException,
)
from mfm.application.features.accounting.create_journal_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.accounting.create_journal_feature import (
    CreateJournalFeature,
)
from mfm.application.features.accounting.create_journal_feature import (
    CreateJournalRequest,
)
from mfm.application.features.accounting.create_journal_feature import (
    CreateJournalResponse,
)
from mfm.application.features.accounting.create_journal_feature import (
    CreateJournalService,
)
from mfm.application.features.accounting.create_journal_feature import (
    JournalLineInput,
)
from mfm.application.features.accounting.create_journal_feature import (
    JournalLineResponse,
)
from mfm.application.features.accounting.create_journal_feature import (
    JournalResponse,
)
from mfm.application.features.accounting.create_journal_feature import (
    JournalSearchResultResponse,
)
from mfm.application.features.accounting.create_journal_feature import (
    RepositoryException,
)
from mfm.application.features.accounting.create_journal_feature import (
    ValidationException,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    CreateLedgerAccountFeature,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    CreateLedgerAccountRequest,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    CreateLedgerAccountResponse,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    CreateLedgerAccountService,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    LedgerAccountResponse,
)
from mfm.application.features.accounting.get_fiscal_year_feature import (
    GetFiscalYearFeature,
)
from mfm.application.features.accounting.get_fiscal_year_feature import (
    GetFiscalYearRequest,
)
from mfm.application.features.accounting.get_fiscal_year_feature import (
    GetFiscalYearResponse,
)
from mfm.application.features.accounting.get_fiscal_year_feature import (
    GetFiscalYearService,
)
from mfm.application.features.accounting.get_journal_feature import GetJournalFeature
from mfm.application.features.accounting.get_journal_feature import GetJournalRequest
from mfm.application.features.accounting.get_journal_feature import GetJournalResponse
from mfm.application.features.accounting.get_journal_feature import GetJournalService
from mfm.application.features.accounting.get_ledger_account_feature import (
    GetLedgerAccountFeature,
)
from mfm.application.features.accounting.get_ledger_account_feature import (
    GetLedgerAccountRequest,
)
from mfm.application.features.accounting.get_ledger_account_feature import (
    GetLedgerAccountResponse,
)
from mfm.application.features.accounting.get_ledger_account_feature import (
    GetLedgerAccountService,
)
from mfm.application.features.accounting.list_fiscal_years_feature import (
    ListFiscalYearsFeature,
)
from mfm.application.features.accounting.list_fiscal_years_feature import (
    ListFiscalYearsRequest,
)
from mfm.application.features.accounting.list_fiscal_years_feature import (
    ListFiscalYearsResponse,
)
from mfm.application.features.accounting.list_fiscal_years_feature import (
    ListFiscalYearsService,
)
from mfm.application.features.accounting.list_journals_feature import (
    ListJournalsFeature,
)
from mfm.application.features.accounting.list_journals_feature import (
    ListJournalsRequest,
)
from mfm.application.features.accounting.list_journals_feature import (
    ListJournalsResponse,
)
from mfm.application.features.accounting.list_journals_feature import (
    ListJournalsService,
)
from mfm.application.features.accounting.list_ledger_accounts_feature import (
    ListLedgerAccountsFeature,
)
from mfm.application.features.accounting.list_ledger_accounts_feature import (
    ListLedgerAccountsRequest,
)
from mfm.application.features.accounting.list_ledger_accounts_feature import (
    ListLedgerAccountsResponse,
)
from mfm.application.features.accounting.list_ledger_accounts_feature import (
    ListLedgerAccountsService,
)
from mfm.application.features.accounting.open_fiscal_year_feature import (
    OpenFiscalYearFeature,
)
from mfm.application.features.accounting.open_fiscal_year_feature import (
    OpenFiscalYearRequest,
)
from mfm.application.features.accounting.open_fiscal_year_feature import (
    OpenFiscalYearResponse,
)
from mfm.application.features.accounting.open_fiscal_year_feature import (
    OpenFiscalYearService,
)
from mfm.application.features.accounting.post_journal_feature import PostJournalFeature
from mfm.application.features.accounting.post_journal_feature import PostJournalRequest
from mfm.application.features.accounting.post_journal_feature import PostJournalResponse
from mfm.application.features.accounting.post_journal_feature import PostJournalService
from mfm.application.features.accounting.reverse_journal_feature import (
    ReverseJournalFeature,
)
from mfm.application.features.accounting.reverse_journal_feature import (
    ReverseJournalRequest,
)
from mfm.application.features.accounting.reverse_journal_feature import (
    ReverseJournalResponse,
)
from mfm.application.features.accounting.reverse_journal_feature import (
    ReverseJournalService,
)
from mfm.application.features.accounting.search_journals_feature import (
    SearchJournalsFeature,
)
from mfm.application.features.accounting.search_journals_feature import (
    SearchJournalsRequest,
)
from mfm.application.features.accounting.search_journals_feature import (
    SearchJournalsResponse,
)
from mfm.application.features.accounting.search_journals_feature import (
    SearchJournalsService,
)
from mfm.application.features.accounting.update_ledger_account_feature import (
    UpdateLedgerAccountFeature,
)
from mfm.application.features.accounting.update_ledger_account_feature import (
    UpdateLedgerAccountRequest,
)
from mfm.application.features.accounting.update_ledger_account_feature import (
    UpdateLedgerAccountResponse,
)
from mfm.application.features.accounting.update_ledger_account_feature import (
    UpdateLedgerAccountService,
)


def create_journal(*, service: CreateJournalService, request: CreateJournalRequest) -> CreateJournalResponse:
    return CreateJournalFeature(service=service).execute(request)


def post_journal(*, service: PostJournalService, request: PostJournalRequest) -> PostJournalResponse:
    return PostJournalFeature(service=service).execute(request)


def reverse_journal(*, service: ReverseJournalService, request: ReverseJournalRequest) -> ReverseJournalResponse:
    return ReverseJournalFeature(service=service).execute(request)


def get_journal(*, service: GetJournalService, request: GetJournalRequest) -> GetJournalResponse:
    return GetJournalFeature(service=service).execute(request)


def list_journals(*, service: ListJournalsService, request: ListJournalsRequest) -> ListJournalsResponse:
    return ListJournalsFeature(service=service).execute(request)


def search_journals(*, service: SearchJournalsService, request: SearchJournalsRequest) -> SearchJournalsResponse:
    return SearchJournalsFeature(service=service).execute(request)


def create_ledger_account(
    *,
    service: CreateLedgerAccountService,
    request: CreateLedgerAccountRequest,
) -> CreateLedgerAccountResponse:
    return CreateLedgerAccountFeature(service=service).execute(request)


def update_ledger_account(
    *,
    service: UpdateLedgerAccountService,
    request: UpdateLedgerAccountRequest,
) -> UpdateLedgerAccountResponse:
    return UpdateLedgerAccountFeature(service=service).execute(request)


def get_ledger_account(
    *,
    service: GetLedgerAccountService,
    request: GetLedgerAccountRequest,
) -> GetLedgerAccountResponse:
    return GetLedgerAccountFeature(service=service).execute(request)


def list_ledger_accounts(
    *,
    service: ListLedgerAccountsService,
    request: ListLedgerAccountsRequest,
) -> ListLedgerAccountsResponse:
    return ListLedgerAccountsFeature(service=service).execute(request)


def create_fiscal_year(
    *,
    service: CreateFiscalYearService,
    request: CreateFiscalYearRequest,
) -> CreateFiscalYearResponse:
    return CreateFiscalYearFeature(service=service).execute(request)


def open_fiscal_year(
    *,
    service: OpenFiscalYearService,
    request: OpenFiscalYearRequest,
) -> OpenFiscalYearResponse:
    return OpenFiscalYearFeature(service=service).execute(request)


def close_fiscal_year(
    *,
    service: CloseFiscalYearService,
    request: CloseFiscalYearRequest,
) -> CloseFiscalYearResponse:
    return CloseFiscalYearFeature(service=service).execute(request)


def get_fiscal_year(
    *,
    service: GetFiscalYearService,
    request: GetFiscalYearRequest,
) -> GetFiscalYearResponse:
    return GetFiscalYearFeature(service=service).execute(request)


def list_fiscal_years(
    *,
    service: ListFiscalYearsService,
    request: ListFiscalYearsRequest,
) -> ListFiscalYearsResponse:
    return ListFiscalYearsFeature(service=service).execute(request)


__all__ = [
    "ApplicationException",
    "BusinessRuleViolation",
    "CloseFiscalYearFeature",
    "CloseFiscalYearRequest",
    "CloseFiscalYearResponse",
    "CloseFiscalYearService",
    "CreateFiscalYearFeature",
    "CreateFiscalYearRequest",
    "CreateFiscalYearResponse",
    "CreateFiscalYearService",
    "CreateJournalFeature",
    "CreateJournalRequest",
    "CreateJournalResponse",
    "CreateJournalService",
    "CreateLedgerAccountFeature",
    "CreateLedgerAccountRequest",
    "CreateLedgerAccountResponse",
    "CreateLedgerAccountService",
    "FiscalPeriodInput",
    "FiscalPeriodResponse",
    "FiscalYearResponse",
    "GetFiscalYearFeature",
    "GetFiscalYearRequest",
    "GetFiscalYearResponse",
    "GetFiscalYearService",
    "GetJournalFeature",
    "GetJournalRequest",
    "GetJournalResponse",
    "GetJournalService",
    "GetLedgerAccountFeature",
    "GetLedgerAccountRequest",
    "GetLedgerAccountResponse",
    "GetLedgerAccountService",
    "JournalLineInput",
    "JournalLineResponse",
    "JournalResponse",
    "JournalSearchResultResponse",
    "LedgerAccountResponse",
    "ListFiscalYearsFeature",
    "ListFiscalYearsRequest",
    "ListFiscalYearsResponse",
    "ListFiscalYearsService",
    "ListJournalsFeature",
    "ListJournalsRequest",
    "ListJournalsResponse",
    "ListJournalsService",
    "ListLedgerAccountsFeature",
    "ListLedgerAccountsRequest",
    "ListLedgerAccountsResponse",
    "ListLedgerAccountsService",
    "OpenFiscalYearFeature",
    "OpenFiscalYearRequest",
    "OpenFiscalYearResponse",
    "OpenFiscalYearService",
    "PostJournalFeature",
    "PostJournalRequest",
    "PostJournalResponse",
    "PostJournalService",
    "RepositoryException",
    "ReverseJournalFeature",
    "ReverseJournalRequest",
    "ReverseJournalResponse",
    "ReverseJournalService",
    "SearchJournalsFeature",
    "SearchJournalsRequest",
    "SearchJournalsResponse",
    "SearchJournalsService",
    "UpdateLedgerAccountFeature",
    "UpdateLedgerAccountRequest",
    "UpdateLedgerAccountResponse",
    "UpdateLedgerAccountService",
    "ValidationException",
    "close_fiscal_year",
    "create_fiscal_year",
    "create_journal",
    "create_ledger_account",
    "get_fiscal_year",
    "get_journal",
    "get_ledger_account",
    "list_fiscal_years",
    "list_journals",
    "list_ledger_accounts",
    "open_fiscal_year",
    "post_journal",
    "reverse_journal",
    "search_journals",
    "update_ledger_account",
]
