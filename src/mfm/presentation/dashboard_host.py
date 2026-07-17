"""Dashboard host that renders reporting DTOs only."""

from __future__ import annotations

from dataclasses import fields
from decimal import Decimal

from PySide6.QtWidgets import QScrollArea
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QTextBrowser

from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusResponse


class DashboardHost(QWidget):
    """Render the reporting dashboards inside the application shell."""

    def __init__(self) -> None:
        super().__init__()
        self._viewer = QTextBrowser()
        self._viewer.setOpenExternalLinks(False)
        self._viewer.setReadOnly(True)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        scroll_area.setWidget(self._viewer)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)
        self._current_title = "Dashboard"
        self._current_payload: object | None = None
        self._render_empty_state()

    @property
    def current_payload(self) -> object | None:
        return self._current_payload

    def set_organization_dashboard(self, report: OrganizationDashboardResponse) -> None:
        self._current_title = "Organization Dashboard"
        self._current_payload = report
        self._viewer.setPlainText(self._format_report(report))

    def set_active_projects_dashboard(self, report: ActiveProjectsDashboardResponse) -> None:
        self._current_title = "Active Projects"
        self._current_payload = report
        self._viewer.setPlainText(self._format_report(report))

    def set_project_status(self, report: ProjectStatusResponse) -> None:
        self._current_title = "Project Status"
        self._current_payload = report
        self._viewer.setPlainText(self._format_report(report))

    def set_budget_vs_actual(self, report: BudgetVsActualResponse) -> None:
        self._current_title = "Budget vs Actual"
        self._current_payload = report
        self._viewer.setPlainText(self._format_report(report))

    def _render_empty_state(self) -> None:
        self._viewer.setPlainText(
            "Select a dashboard on the left to view reporting output."
        )

    def _format_report(self, report: object) -> str:
        lines = [self._current_title, ""]
        for field in fields(report):
            value = getattr(report, field.name)
            lines.append(f"{field.name}: {self._format_value(value)}")
        return "\n".join(lines)

    def _format_value(self, value: object) -> str:
        if isinstance(value, tuple):
            return ", ".join(self._format_value(item) for item in value) if value else "(none)"
        if isinstance(value, Decimal):
            return format(value, "f")
        return str(value)
