"""Dashboard host that embeds the operational dashboard workspace."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusResponse
from mfm.presentation.dashboard.dashboard_controller import DashboardController
from mfm.presentation.dashboard.dashboard_controller import DashboardSnapshot
from mfm.presentation.dashboard.dashboard_workspace import DashboardWorkspace


@dataclass(frozen=True, slots=True)
class DashboardHostSnapshotLoader:
    organization_dashboard: Callable[[], OrganizationDashboardResponse]
    active_projects_dashboard: Callable[[], ActiveProjectsDashboardResponse]
    project_status_dashboard: Callable[[], ProjectStatusResponse]
    budget_vs_actual_dashboard: Callable[[], BudgetVsActualResponse]

    def load(self) -> DashboardSnapshot:
        return DashboardSnapshot(
            organization_dashboard=self.organization_dashboard(),
            active_projects_dashboard=self.active_projects_dashboard(),
            project_status_dashboard=self.project_status_dashboard(),
            budget_vs_actual_dashboard=self.budget_vs_actual_dashboard(),
        )


class DashboardHost(QWidget):
    """Host widget that owns the reporting dashboard workspace."""

    def __init__(self, *, snapshot_loader: DashboardHostSnapshotLoader | None = None) -> None:
        super().__init__()
        self._snapshot_loader = snapshot_loader
        self._controller = DashboardController(refresh_callback=self.refresh)
        self._workspace = DashboardWorkspace(controller=self._controller)

        layout = QVBoxLayout(self)
        layout.addWidget(self._workspace)

    @property
    def workspace(self) -> DashboardWorkspace:
        return self._workspace

    def refresh(self) -> None:
        snapshot = self._load_snapshot()
        self._workspace.set_reports(
            organization_dashboard=snapshot.organization_dashboard,
            active_projects_dashboard=snapshot.active_projects_dashboard,
            project_status_dashboard=snapshot.project_status_dashboard,
            budget_vs_actual_dashboard=snapshot.budget_vs_actual_dashboard,
        )

    def show_dashboard(self, route_id: str) -> None:
        if self._workspace.current_route_id is None:
            self.refresh()
        self._workspace.show_dashboard(route_id)

    def _load_snapshot(self) -> DashboardSnapshot:
        if self._snapshot_loader is None:
            raise RuntimeError("Dashboard snapshot loader is not configured")
        return self._snapshot_loader.load()
