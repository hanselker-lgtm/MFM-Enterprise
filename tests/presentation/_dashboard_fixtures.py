from __future__ import annotations

from datetime import date
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardResponse
from mfm.application.reporting.models.active_projects_dto import ActiveProjectsDashboardTotalsDTO
from mfm.application.reporting.models.active_projects_dto import ActiveProjectDashboardProjectDTO
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualAccountingResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualBudgetResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualProjectResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualStatusResponse
from mfm.application.reporting.models.budget_vs_actual_dto import BudgetVsActualVarianceResponse
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardAccountingDTO
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardDocumentsDTO
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardHealthIndicatorsDTO
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardOperationsDTO
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardOrganizationDTO
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardProjectsDTO
from mfm.application.reporting.models.organization_dashboard_dto import OrganizationDashboardResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusAccountingResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusArchiveResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusBudgetResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusDocumentsResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusHealthResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusOrganizationResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusProjectResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusResponse
from mfm.presentation.dashboard.dashboard_controller import DashboardSnapshot


PROJECT_ID = UUID("11111111-1111-1111-1111-111111111111")
PROJECT_STATUS_ID = UUID("22222222-2222-2222-2222-222222222222")
BUDGET_PROJECT_ID = UUID("33333333-3333-3333-3333-333333333333")
ORGANIZATION_ID = UUID("44444444-4444-4444-4444-444444444444")


def organization_dashboard_report() -> OrganizationDashboardResponse:
    return OrganizationDashboardResponse(
        organization=OrganizationDashboardOrganizationDTO(
            organization_id=ORGANIZATION_ID,
            name="MFM Enterprise",
            status="ACTIVE",
        ),
        projects=OrganizationDashboardProjectsDTO(
            active_projects=3,
            closed_projects=1,
            archived_projects=0,
            total_projects=4,
        ),
        documents=OrganizationDashboardDocumentsDTO(
            total_documents=8,
            documents_added_last_30_days=2,
        ),
        accounting=OrganizationDashboardAccountingDTO(
            journal_count=5,
            last_posted_journal="J-2024-05",
            open_fiscal_years=1,
            closed_fiscal_years=3,
        ),
        operations=OrganizationDashboardOperationsDTO(
            last_accounting_activity=date(2024, 5, 2),
            last_document_activity=datetime(2024, 5, 2, 12, 0),
        ),
        health_indicators=OrganizationDashboardHealthIndicatorsDTO(
            budget_coverage=0.75,
            accounting_status="HEALTHY",
            documentation_status="HEALTHY",
            archive_status="READY",
        ),
    )


def active_projects_dashboard_report() -> ActiveProjectsDashboardResponse:
    return ActiveProjectsDashboardResponse(
        projects=(
            ActiveProjectDashboardProjectDTO(
                project_id=PROJECT_ID,
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


def project_status_report() -> ProjectStatusResponse:
    return ProjectStatusResponse(
        project=ProjectStatusProjectResponse(
            project_id=PROJECT_STATUS_ID,
            name="Project Bravo",
            status="ACTIVE",
            created_date=date(2024, 1, 1),
            last_updated=datetime(2024, 2, 2, 9, 0),
            organization=ProjectStatusOrganizationResponse(
                organization_id=ORGANIZATION_ID,
                name="MFM Enterprise",
                status="ACTIVE",
            ),
        ),
        documents=ProjectStatusDocumentsResponse(
            total_documents=2,
            finalized_documents=1,
            outstanding_documents=1,
        ),
        budget=ProjectStatusBudgetResponse(
            budget_status="READY",
            budget_categories=("CAPEX",),
            budget_ready=True,
        ),
        accounting=ProjectStatusAccountingResponse(
            journal_count=2,
            last_journal="J-2024-05",
            fiscal_year=2024,
            accounting_status="COMPLETE",
        ),
        archive=ProjectStatusArchiveResponse(
            archive_status="READY_FOR_ARCHIVE",
            closure_status="OPEN",
        ),
        health=ProjectStatusHealthResponse(
            overall_health_indicator="HEALTHY",
            missing_requirements=(),
            ready_for_closure=True,
        ),
    )


def budget_vs_actual_report() -> BudgetVsActualResponse:
    return BudgetVsActualResponse(
        project=BudgetVsActualProjectResponse(
            project_id=BUDGET_PROJECT_ID,
            project_name="Budget Gamma",
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


def dashboard_snapshot() -> DashboardSnapshot:
    return DashboardSnapshot(
        organization_dashboard=organization_dashboard_report(),
        active_projects_dashboard=active_projects_dashboard_report(),
        project_status_dashboard=project_status_report(),
        budget_vs_actual_dashboard=budget_vs_actual_report(),
    )
