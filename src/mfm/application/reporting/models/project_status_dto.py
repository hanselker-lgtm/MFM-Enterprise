"""DTOs for REP-003 project status dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ProjectStatusOrganizationResponse:
    organization_id: UUID | None
    name: str | None
    status: str | None


@dataclass(frozen=True, slots=True)
class ProjectStatusProjectResponse:
    project_id: UUID
    name: str
    status: str
    created_date: date
    last_updated: datetime | None
    organization: ProjectStatusOrganizationResponse


@dataclass(frozen=True, slots=True)
class ProjectStatusDocumentsResponse:
    total_documents: int
    finalized_documents: int
    outstanding_documents: int


@dataclass(frozen=True, slots=True)
class ProjectStatusBudgetResponse:
    budget_status: str
    budget_categories: tuple[str, ...]
    budget_ready: bool


@dataclass(frozen=True, slots=True)
class ProjectStatusAccountingResponse:
    journal_count: int
    last_journal: str | None
    fiscal_year: int | None
    accounting_status: str


@dataclass(frozen=True, slots=True)
class ProjectStatusArchiveResponse:
    archive_status: str
    closure_status: str


@dataclass(frozen=True, slots=True)
class ProjectStatusHealthResponse:
    overall_health_indicator: str
    missing_requirements: tuple[str, ...]
    ready_for_closure: bool


@dataclass(frozen=True, slots=True)
class ProjectStatusResponse:
    project: ProjectStatusProjectResponse
    documents: ProjectStatusDocumentsResponse
    budget: ProjectStatusBudgetResponse
    accounting: ProjectStatusAccountingResponse
    archive: ProjectStatusArchiveResponse
    health: ProjectStatusHealthResponse


ProjectStatusDTO = ProjectStatusResponse