"""ViewModels for the project workspace presentation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from uuid import UUID


class ProjectSortField(StrEnum):
    PROJECT_NUMBER = "project_number"
    NAME = "name"
    STATUS = "status"
    PRIORITY = "priority"
    CREATED_AT = "created_at"


@dataclass(frozen=True, slots=True)
class ProjectListFilterViewModel:
    text: str = ""
    status: str = "ALL"
    sort_by: ProjectSortField = ProjectSortField.CREATED_AT
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
class ProjectListItemViewModel:
    project_id: UUID
    project_number: str
    name: str
    status: str
    priority: str
    created_at: datetime | None


@dataclass(frozen=True, slots=True)
class ProjectListViewModel:
    filters: ProjectListFilterViewModel
    items: tuple[ProjectListItemViewModel, ...]
    pagination: PaginationViewModel


@dataclass(frozen=True, slots=True)
class ProjectOverviewViewModel:
    project_id: UUID
    project_number: str
    name: str
    description: str
    start_date: datetime | None
    end_date: datetime | None


@dataclass(frozen=True, slots=True)
class ProjectStatusSummaryViewModel:
    status: str
    health_indicator: str
    ready_for_closure: bool


@dataclass(frozen=True, slots=True)
class ProjectBudgetSummaryViewModel:
    budget_status: str
    categories: tuple[str, ...]
    planned_budget_total: Decimal | None
    budget_variance: Decimal | None


@dataclass(frozen=True, slots=True)
class ProjectAccountingSummaryViewModel:
    accounting_status: str
    journal_count: int
    actual_total: Decimal
    fiscal_year: int | None


@dataclass(frozen=True, slots=True)
class ProjectDocumentSummaryViewModel:
    total_documents: int
    finalized_documents: int
    outstanding_documents: int


@dataclass(frozen=True, slots=True)
class ProjectArchiveStatusViewModel:
    archive_status: str
    closure_status: str


@dataclass(frozen=True, slots=True)
class ProjectDetailViewModel:
    overview: ProjectOverviewViewModel
    status: ProjectStatusSummaryViewModel
    budget_summary: ProjectBudgetSummaryViewModel
    accounting_summary: ProjectAccountingSummaryViewModel
    document_summary: ProjectDocumentSummaryViewModel
    archive_status: ProjectArchiveStatusViewModel


@dataclass(frozen=True, slots=True)
class CreateProjectCommandViewModel:
    organization_id: UUID
    organization_owner_contact_id: UUID
    project_number: str
    project_name: str
    project_priority: str = "NORMAL"
    project_description: str | None = None
    project_start_date: datetime | None = None
    project_end_date: datetime | None = None
