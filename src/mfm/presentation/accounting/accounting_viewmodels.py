"""ViewModels for accounting workspace presentation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import StrEnum
from uuid import UUID


class JournalSortField(StrEnum):
    JOURNAL_NUMBER = "journal_number"
    POSTING_DATE = "posting_date"
    STATUS = "status"


@dataclass(frozen=True, slots=True)
class JournalListFilterViewModel:
    text: str = ""
    status: str = "ALL"
    fiscal_year: int | None = None
    sort_by: JournalSortField = JournalSortField.POSTING_DATE
    descending: bool = True
    page: int = 1
    page_size: int = 25


@dataclass(frozen=True, slots=True)
class PaginationViewModel:
    page: int
    page_size: int
    total_items: int
    total_pages: int
    has_previous: bool
    has_next: bool


@dataclass(frozen=True, slots=True)
class JournalListItemViewModel:
    journal_id: UUID
    fiscal_year_id: UUID | None
    journal_number: str
    posting_date: date
    status: str
    reference: str | None


@dataclass(frozen=True, slots=True)
class JournalListViewModel:
    filters: JournalListFilterViewModel
    items: tuple[JournalListItemViewModel, ...]
    pagination: PaginationViewModel


@dataclass(frozen=True, slots=True)
class JournalLineViewModel:
    account_id: UUID
    side: str
    amount: Decimal
    currency: str
    description: str | None


@dataclass(frozen=True, slots=True)
class JournalInfoViewModel:
    journal_id: UUID
    journal_number: str
    posting_date: date
    description: str
    reference: str | None
    posting_status: str


@dataclass(frozen=True, slots=True)
class JournalProjectLinkViewModel:
    project_id: UUID | None
    linked: bool


@dataclass(frozen=True, slots=True)
class JournalFiscalYearViewModel:
    fiscal_year_id: UUID | None
    fiscal_year_label: str


@dataclass(frozen=True, slots=True)
class JournalAuditViewModel:
    references: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class JournalProjectSummaryViewModel:
    health_indicator: str | None
    budget_status: str | None
    actual_total: Decimal | None
    budget_variance: Decimal | None


@dataclass(frozen=True, slots=True)
class JournalDetailViewModel:
    journal: JournalInfoViewModel
    project_link: JournalProjectLinkViewModel
    fiscal_year: JournalFiscalYearViewModel
    audit: JournalAuditViewModel
    lines: tuple[JournalLineViewModel, ...]
    project_summary: JournalProjectSummaryViewModel


@dataclass(frozen=True, slots=True)
class CreateJournalCommandViewModel:
    project_id: UUID
    journal_number: str
    posting_date: date
    description: str
    debit_account_id: UUID
    credit_account_id: UUID
    amount: Decimal | str | int
    currency: str = "DKK"
    transaction_reference: str | None = None
