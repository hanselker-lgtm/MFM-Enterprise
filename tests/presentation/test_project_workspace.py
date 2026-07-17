from __future__ import annotations

from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.presentation.projects import PaginationViewModel
from mfm.presentation.projects import ProjectDetailViewModel
from mfm.presentation.projects import ProjectListFilterViewModel
from mfm.presentation.projects import ProjectListItemViewModel
from mfm.presentation.projects import ProjectListViewModel
from mfm.presentation.projects.project_viewmodels import ProjectAccountingSummaryViewModel
from mfm.presentation.projects.project_viewmodels import ProjectArchiveStatusViewModel
from mfm.presentation.projects.project_viewmodels import ProjectBudgetSummaryViewModel
from mfm.presentation.projects.project_viewmodels import ProjectDocumentSummaryViewModel
from mfm.presentation.projects.project_viewmodels import ProjectOverviewViewModel
from mfm.presentation.projects.project_viewmodels import ProjectStatusSummaryViewModel
from mfm.presentation.projects.project_workspace import ProjectWorkspace


class _WorkspaceControllerStub:
    def __init__(self) -> None:
        self.load_calls = 0
        self.last_filters: ProjectListFilterViewModel | None = None
        self.last_opened: UUID | None = None

    def load_project_list(self, *, filters: ProjectListFilterViewModel) -> ProjectListViewModel:
        self.load_calls += 1
        self.last_filters = filters
        return ProjectListViewModel(
            filters=filters,
            items=(
                ProjectListItemViewModel(
                    project_id=uuid4(),
                    project_number="PRJ-777",
                    name="Workspace Test Project",
                    status="ACTIVE",
                    priority="NORMAL",
                    created_at=datetime(2024, 1, 1, tzinfo=UTC),
                ),
            ),
            pagination=PaginationViewModel(
                page=filters.page,
                page_size=filters.page_size,
                total_items=1,
                total_pages=1,
                has_previous=False,
                has_next=False,
            ),
        )

    def refresh(self):
        return self.load_project_list(filters=self.last_filters or ProjectListFilterViewModel()), None

    def open_project(self, project_id: UUID) -> ProjectDetailViewModel:
        self.last_opened = project_id
        return ProjectDetailViewModel(
            overview=ProjectOverviewViewModel(
                project_id=project_id,
                project_number="PRJ-777",
                name="Workspace Test Project",
                description="",
                start_date=None,
                end_date=None,
            ),
            status=ProjectStatusSummaryViewModel(
                status="ACTIVE",
                health_indicator="GREEN",
                ready_for_closure=False,
            ),
            budget_summary=ProjectBudgetSummaryViewModel(
                budget_status="OK",
                categories=("OPEX",),
                planned_budget_total=Decimal("100"),
                budget_variance=Decimal("0"),
            ),
            accounting_summary=ProjectAccountingSummaryViewModel(
                accounting_status="SYNCED",
                journal_count=1,
                actual_total=Decimal("100"),
                fiscal_year=2024,
            ),
            document_summary=ProjectDocumentSummaryViewModel(
                total_documents=1,
                finalized_documents=1,
                outstanding_documents=0,
            ),
            archive_status=ProjectArchiveStatusViewModel(
                archive_status="NOT_ARCHIVED",
                closure_status="OPEN",
            ),
        )

    def create_project(self, command):
        _ = command
        return uuid4()

    def navigate_to_documents(self, project_id: UUID) -> None:
        _ = project_id

    def navigate_to_accounting(self, project_id: UUID) -> None:
        _ = project_id


def test_project_workspace_performs_initial_lazy_load(qapp) -> None:
    controller = _WorkspaceControllerStub()

    _ = ProjectWorkspace(controller=controller)

    assert controller.load_calls == 1
