from __future__ import annotations

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QWidget

from mfm.presentation.application_shell import build_application_shell

from tests.presentation._dashboard_fixtures import active_projects_dashboard_report
from tests.presentation._dashboard_fixtures import budget_vs_actual_report
from tests.presentation._dashboard_fixtures import organization_dashboard_report
from tests.presentation._dashboard_fixtures import project_status_report


def test_application_shell_navigates_report_and_widget_routes(qapp) -> None:
    shell = build_application_shell(
        report_loaders={
            "dashboard.organization": organization_dashboard_report,
            "dashboard.active-projects": active_projects_dashboard_report,
            "dashboard.project-status": project_status_report,
            "dashboard.budget-vs-actual": budget_vs_actual_report,
        },
        widget_loaders={
            "operations.organizations": lambda: QLabel("Organizations"),
            "operations.projects": lambda: QLabel("Projects"),
            "operations.documents": lambda: QLabel("Documents"),
            "operations.accounting": lambda: QLabel("Accounting"),
            "administration.settings": lambda: QLabel("Settings"),
            "administration.logs": lambda: QLabel("Logs"),
            "administration.about": lambda: QLabel("About"),
        },
    )

    window = shell.main_window
    window.navigate_to("dashboard.budget-vs-actual")
    assert window.statusBar().currentMessage() == "Loaded Budget vs. Faktisk"
    assert window.centralWidget().currentWidget().workspace.current_route_id == "dashboard.budget-vs-actual"

    window.navigate_to("operations.projects")
    assert isinstance(window.centralWidget().currentWidget(), QWidget)
    assert window.statusBar().currentMessage() == "Loaded Projekter"
