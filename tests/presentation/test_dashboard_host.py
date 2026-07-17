from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import UUID

from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualAccountingResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualBudgetResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualProjectResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualStatusResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualVarianceResponse
from mfm.presentation.dashboard_host import DashboardHost


def test_dashboard_host_accepts_reporting_dto_only(qapp) -> None:
    host = DashboardHost()
    report = BudgetVsActualResponse(
        project=BudgetVsActualProjectResponse(
            project_id=UUID("11111111-1111-1111-1111-111111111111"),
            project_name="Harbor Project",
        ),
        budget=BudgetVsActualBudgetResponse(
            budget_status="READY",
            budget_categories=("CAPEX",),
            planned_budget_total=None,
            budget_ready=True,
        ),
        accounting=BudgetVsActualAccountingResponse(
            actual_total=Decimal("125.50"),
            journal_count=1,
            last_journal_date=date(2024, 2, 1),
            fiscal_year=2024,
        ),
        variance=BudgetVsActualVarianceResponse(
            budget_variance=None,
            variance_percentage=None,
        ),
        status=BudgetVsActualStatusResponse(
            within_budget=None,
            reporting_confidence="LIMITED_BUDGET_METADATA",
        ),
    )

    host.set_budget_vs_actual(report)

    assert host.current_payload == report
    assert "Harbor Project" in host.findChild(type(host._viewer)).toPlainText()
    assert "LIMITED_BUDGET_METADATA" in host.findChild(type(host._viewer)).toPlainText()
