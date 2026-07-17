from __future__ import annotations

from mfm.presentation.dashboard.dashboard_controller import DashboardController
from mfm.presentation.dashboard.dashboard_workspace import DashboardWorkspace

from tests.presentation._dashboard_fixtures import dashboard_snapshot


def test_dashboard_workspace_receives_reporting_dtos_and_navigates_details(qapp) -> None:
    controller = DashboardController()
    workspace = DashboardWorkspace(controller=controller)
    workspace.set_reports(
        organization_dashboard=dashboard_snapshot().organization_dashboard,
        active_projects_dashboard=dashboard_snapshot().active_projects_dashboard,
        project_status_dashboard=dashboard_snapshot().project_status_dashboard,
        budget_vs_actual_dashboard=dashboard_snapshot().budget_vs_actual_dashboard,
    )

    assert workspace.current_route_id == "dashboard.organization"

    workspace.show_dashboard("dashboard.budget-vs-actual")

    assert workspace.current_route_id == "dashboard.budget-vs-actual"
    assert "LIMITED_BUDGET_METADATA" in workspace.detail_widget("dashboard.budget-vs-actual").rendered_text
    assert "Budget Gamma" in workspace.detail_widget("dashboard.budget-vs-actual").rendered_text
