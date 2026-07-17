"""Dashboard workspace controller driven only by reporting DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusResponse
from mfm.presentation.dashboard.dashboard_cards import DashboardCardView


from collections.abc import Callable

RefreshCallback = Callable[[], None]


@dataclass(frozen=True, slots=True)
class DashboardSnapshot:
    organization_dashboard: OrganizationDashboardResponse
    active_projects_dashboard: ActiveProjectsDashboardResponse
    project_status_dashboard: ProjectStatusResponse
    budget_vs_actual_dashboard: BudgetVsActualResponse


class DashboardController:
    """Translate reporting DTOs into workspace-ready card views."""

    def __init__(self, *, refresh_callback: RefreshCallback | None = None) -> None:
        self._refresh_callback = refresh_callback
        self._snapshot: DashboardSnapshot | None = None
        self._current_route_id: str | None = None

    def set_snapshot(self, snapshot: DashboardSnapshot) -> None:
        self._snapshot = snapshot

    def refresh(self) -> None:
        if self._refresh_callback is not None:
            self._refresh_callback()

    def select(self, route_id: str) -> None:
        self._current_route_id = route_id

    @property
    def current_route_id(self) -> str | None:
        return self._current_route_id

    def card_views(self) -> tuple[DashboardCardView, ...]:
        snapshot = self._require_snapshot()
        return (
            DashboardCardView(
                route_id="dashboard.organization",
                title="Organization Dashboard",
                summary=f"{snapshot.organization_dashboard.projects.total_projects} projects",
                detail="Organization-wide reporting overview.",
                tile_title="Projects",
                tile_value=str(snapshot.organization_dashboard.projects.total_projects),
                tile_subtitle="Total projects across the organization",
            ),
            DashboardCardView(
                route_id="dashboard.active-projects",
                title="Active Projects",
                summary=f"{snapshot.active_projects_dashboard.totals.active_project_count} active projects",
                detail="Active portfolio health and readiness.",
                tile_title="Active",
                tile_value=str(snapshot.active_projects_dashboard.totals.active_project_count),
                tile_subtitle="Projects currently active",
            ),
            DashboardCardView(
                route_id="dashboard.project-status",
                title="Project Status",
                summary=snapshot.project_status_dashboard.project.name,
                detail="Project-level archive and accounting status.",
                tile_title="Project",
                tile_value=snapshot.project_status_dashboard.health.overall_health_indicator,
                tile_subtitle=snapshot.project_status_dashboard.project.name,
            ),
            DashboardCardView(
                route_id="dashboard.budget-vs-actual",
                title="Budget vs Actual",
                summary=f"Actual {snapshot.budget_vs_actual_dashboard.accounting.actual_total}",
                detail="Budget metadata and actual accounting movement.",
                tile_title="Actual",
                tile_value=str(snapshot.budget_vs_actual_dashboard.accounting.actual_total),
                tile_subtitle=snapshot.budget_vs_actual_dashboard.status.reporting_confidence,
            ),
        )

    @property
    def snapshot(self) -> DashboardSnapshot:
        return self._require_snapshot()

    def _require_snapshot(self) -> DashboardSnapshot:
        if self._snapshot is None:
            raise RuntimeError("Dashboard snapshot has not been loaded")
        return self._snapshot
