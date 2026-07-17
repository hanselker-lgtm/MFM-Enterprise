"""DTOs for REP-001 organization dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class OrganizationDashboardOrganizationDTO:
    organization_id: UUID
    name: str | None
    status: str | None


@dataclass(frozen=True, slots=True)
class OrganizationDashboardProjectsDTO:
    active_projects: int
    closed_projects: int
    archived_projects: int
    total_projects: int


@dataclass(frozen=True, slots=True)
class OrganizationDashboardDocumentsDTO:
    total_documents: int
    documents_added_last_30_days: int


@dataclass(frozen=True, slots=True)
class OrganizationDashboardAccountingDTO:
    journal_count: int
    last_posted_journal: str | None
    open_fiscal_years: int
    closed_fiscal_years: int


@dataclass(frozen=True, slots=True)
class OrganizationDashboardOperationsDTO:
    last_accounting_activity: date | None
    last_document_activity: datetime | None


@dataclass(frozen=True, slots=True)
class OrganizationDashboardHealthIndicatorsDTO:
    budget_coverage: float
    accounting_status: str
    documentation_status: str
    archive_status: str


@dataclass(frozen=True, slots=True)
class OrganizationDashboardResponse:
    organization: OrganizationDashboardOrganizationDTO
    projects: OrganizationDashboardProjectsDTO
    documents: OrganizationDashboardDocumentsDTO
    accounting: OrganizationDashboardAccountingDTO
    operations: OrganizationDashboardOperationsDTO
    health_indicators: OrganizationDashboardHealthIndicatorsDTO


# Backward-compatible DTO alias for reporting callers.
OrganizationDashboardDTO = OrganizationDashboardResponse
