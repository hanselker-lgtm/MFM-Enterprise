from __future__ import annotations

from PySide6.QtWidgets import QLabel

from mfm.presentation.application_shell import build_application_shell

from tests.presentation._dashboard_fixtures import active_projects_dashboard_report
from tests.presentation._dashboard_fixtures import budget_vs_actual_report
from tests.presentation._dashboard_fixtures import organization_dashboard_report
from tests.presentation._dashboard_fixtures import project_status_report


def test_application_shell_can_use_dedicated_documents_workspace_loader(qapp) -> None:
    shell = build_application_shell(
        report_loaders={
            "dashboard.organization": organization_dashboard_report,
            "dashboard.active-projects": active_projects_dashboard_report,
            "dashboard.project-status": project_status_report,
            "dashboard.budget-vs-actual": budget_vs_actual_report,
        },
        documents_workspace_loader=lambda: QLabel("Documents Workspace"),
    )

    window = shell.main_window
    window.navigate_to("operations.documents")

    assert window.centralWidget().currentWidget().text() == "Documents Workspace"
    assert window.statusBar().currentMessage() == "Loaded Dokumenter"
