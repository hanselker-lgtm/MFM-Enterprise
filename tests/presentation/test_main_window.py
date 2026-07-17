from __future__ import annotations

from datetime import date
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QWidget

from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardResponse
from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardTotalsDTO
from mfm.application.reporting.models.active_projects_dto import ActiveProjectDashboardProjectDTO
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualAccountingResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualBudgetResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualProjectResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualStatusResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualVarianceResponse
from mfm.presentation.application_shell import build_application_shell


def test_application_shell_navigates_report_and_widget_routes(qapp) -> None:
    report = ActiveProjectsDashboardResponse(
        projects=(
            ActiveProjectDashboardProjectDTO(
                project_id=UUID("11111111-1111-1111-1111-111111111111"),
                name="Project Alpha",
                status="ACTIVE",
                created_date=date(2024, 1, 1),
                budget_status="READY",
                accounting_status="COMPLETE",
                documentation_status="COMPLETE",
                archive_status="READY_FOR_CLOSURE",
                last_activity=datetime(2024, 2, 1, 8, 0),
                health_indicator="HEALTHY",
            ),
        ),
        totals=ActiveProjectsDashboardTotalsDTO(
            active_project_count=1,
            projects_missing_budget=0,
            projects_missing_documentation=0,
            projects_missing_accounting=0,
            projects_ready_for_closure=1,
        ),
    )

    shell = build_application_shell(
        report_loaders={
            "dashboard.organization": lambda: report,
            "dashboard.active-projects": lambda: report,
            "dashboard.project-status": lambda: report,
            "dashboard.budget-vs-actual": lambda: BudgetVsActualResponse(
                project=BudgetVsActualProjectResponse(
                    project_id=UUID("22222222-2222-2222-2222-222222222222"),
                    project_name="Budget Test",
                ),
                budget=BudgetVsActualBudgetResponse(
                    budget_status="READY",
                    budget_categories=("CAPEX",),
                    planned_budget_total=None,
                    budget_ready=True,
                ),
                accounting=BudgetVsActualAccountingResponse(
                    actual_total=Decimal("0"),
                    journal_count=0,
                    last_journal_date=None,
                    fiscal_year=None,
                ),
                variance=BudgetVsActualVarianceResponse(
                    budget_variance=None,
                    variance_percentage=None,
                ),
                status=BudgetVsActualStatusResponse(
                    within_budget=None,
                    reporting_confidence="LIMITED_BUDGET_METADATA",
                ),
            ),
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
    assert window.statusBar().currentMessage() == "Loaded Budget vs Actual"
    assert shell.main_window.centralWidget().currentWidget().objectName() == ""

    window.navigate_to("operations.projects")
    assert isinstance(window.centralWidget().currentWidget(), QWidget)
    assert window.statusBar().currentMessage() == "Loaded Projects"
