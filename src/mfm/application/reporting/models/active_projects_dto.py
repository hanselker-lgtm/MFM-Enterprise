"""DTOs for REP-002 active projects dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ActiveProjectDashboardProjectDTO:
    project_id: UUID
    name: str
    status: str
    created_date: date
    budget_status: str
    accounting_status: str
    documentation_status: str
    archive_status: str
    last_activity: datetime | None
    health_indicator: str


@dataclass(frozen=True, slots=True)
class ActiveProjectsDashboardTotalsDTO:
    active_project_count: int
    projects_missing_budget: int
    projects_missing_documentation: int
    projects_missing_accounting: int
    projects_ready_for_closure: int


@dataclass(frozen=True, slots=True)
class ActiveProjectsDashboardResponse:
    projects: tuple[ActiveProjectDashboardProjectDTO, ...]
    totals: ActiveProjectsDashboardTotalsDTO


ActiveProjectsDashboardDTO = ActiveProjectsDashboardResponse
