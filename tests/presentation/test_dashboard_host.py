from __future__ import annotations

from mfm.presentation.dashboard_host import DashboardHost
from mfm.presentation.dashboard_host import DashboardHostSnapshotLoader

from tests.presentation._dashboard_fixtures import active_projects_dashboard_report
from tests.presentation._dashboard_fixtures import budget_vs_actual_report
from tests.presentation._dashboard_fixtures import organization_dashboard_report
from tests.presentation._dashboard_fixtures import project_status_report


def test_dashboard_host_loads_snapshot_and_selects_route(qapp) -> None:
    host = DashboardHost(
        snapshot_loader=DashboardHostSnapshotLoader(
            organization_dashboard=organization_dashboard_report,
            active_projects_dashboard=active_projects_dashboard_report,
            project_status_dashboard=project_status_report,
            budget_vs_actual_dashboard=budget_vs_actual_report,
        )
    )

    host.show_dashboard("dashboard.budget-vs-actual")

    assert host.workspace.current_route_id == "dashboard.budget-vs-actual"
    assert "LIMITED_BUDGET_METADATA" in host.workspace.detail_widget("dashboard.budget-vs-actual").rendered_text
