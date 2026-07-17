"""Controller for the project workspace."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Callable
from typing import Protocol
from uuid import UUID

from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import ListProjectsRequest
from mfm.application.features.projects import SearchProjectsRequest
from mfm.application.features.reporting import BudgetVsActualRequest
from mfm.application.features.reporting import ProjectStatusRequest
from mfm.application.workflows.complete_project_creation_workflow import (
    CompleteProjectCreationWorkflowRequest,
)
from mfm.presentation.projects.project_viewmodels import CreateProjectCommandViewModel
from mfm.presentation.projects.project_viewmodels import PaginationViewModel
from mfm.presentation.projects.project_viewmodels import ProjectAccountingSummaryViewModel
from mfm.presentation.projects.project_viewmodels import ProjectArchiveStatusViewModel
from mfm.presentation.projects.project_viewmodels import ProjectBudgetSummaryViewModel
from mfm.presentation.projects.project_viewmodels import ProjectDetailViewModel
from mfm.presentation.projects.project_viewmodels import ProjectDocumentSummaryViewModel
from mfm.presentation.projects.project_viewmodels import ProjectListFilterViewModel
from mfm.presentation.projects.project_viewmodels import ProjectListItemViewModel
from mfm.presentation.projects.project_viewmodels import ProjectListViewModel
from mfm.presentation.projects.project_viewmodels import ProjectOverviewViewModel
from mfm.presentation.projects.project_viewmodels import ProjectSortField
from mfm.presentation.projects.project_viewmodels import ProjectStatusSummaryViewModel


class ListProjectsPort(Protocol):
    def execute(self, request: ListProjectsRequest): ...


class SearchProjectsPort(Protocol):
    def execute(self, request: SearchProjectsRequest): ...


class GetProjectPort(Protocol):
    def execute(self, request: GetProjectRequest): ...


class ProjectStatusReportPort(Protocol):
    def execute(self, request: ProjectStatusRequest): ...


class BudgetVsActualReportPort(Protocol):
    def execute(self, request: BudgetVsActualRequest): ...


class CompleteProjectCreationWorkflowPort(Protocol):
    def execute(self, request: CompleteProjectCreationWorkflowRequest): ...


@dataclass(frozen=True, slots=True)
class ProjectNavigationCallbacks:
    to_documents: Callable[[UUID], None] | None = None
    to_accounting: Callable[[UUID], None] | None = None


class ProjectController:
    """UI controller that orchestrates project features and reporting features."""

    def __init__(
        self,
        *,
        list_projects_feature: ListProjectsPort,
        search_projects_feature: SearchProjectsPort,
        get_project_feature: GetProjectPort,
        project_status_feature: ProjectStatusReportPort,
        budget_vs_actual_feature: BudgetVsActualReportPort,
        create_project_workflow_feature: CompleteProjectCreationWorkflowPort,
        navigation: ProjectNavigationCallbacks | None = None,
    ) -> None:
        self._list_projects = list_projects_feature
        self._search_projects = search_projects_feature
        self._get_project = get_project_feature
        self._project_status = project_status_feature
        self._budget_vs_actual = budget_vs_actual_feature
        self._create_project_workflow = create_project_workflow_feature
        self._navigation = navigation or ProjectNavigationCallbacks()
        self._last_filters = ProjectListFilterViewModel()
        self._last_selected_project_id: UUID | None = None

    @property
    def last_selected_project_id(self) -> UUID | None:
        return self._last_selected_project_id

    def load_project_list(
        self,
        *,
        filters: ProjectListFilterViewModel,
    ) -> ProjectListViewModel:
        self._last_filters = filters

        if filters.text.strip() or filters.status != "ALL":
            status = None if filters.status == "ALL" else filters.status
            search_response = self._search_projects.execute(
                SearchProjectsRequest(text=filters.text.strip() or None, status=status)
            )
            items = tuple(
                ProjectListItemViewModel(
                    project_id=item.project_id,
                    project_number=item.project_number,
                    name=item.project_name,
                    status=item.status,
                    priority=item.priority,
                    created_at=None,
                )
                for item in search_response.projects
            )
        else:
            list_response = self._list_projects.execute(ListProjectsRequest())
            items = tuple(
                ProjectListItemViewModel(
                    project_id=item.project_id,
                    project_number=item.project_number,
                    name=item.project_name,
                    status=item.status,
                    priority=item.priority,
                    created_at=item.created_at,
                )
                for item in list_response.projects
            )

        sorted_items = self._sort_items(items, filters)
        paged_items, pagination = self._paginate(sorted_items, filters)

        return ProjectListViewModel(filters=filters, items=paged_items, pagination=pagination)

    def open_project(self, project_id: UUID) -> ProjectDetailViewModel:
        self._last_selected_project_id = project_id
        project_response = self._get_project.execute(GetProjectRequest(project_id=project_id)).project
        status_response = self._project_status.execute(ProjectStatusRequest(project_id=project_id))
        budget_response = self._budget_vs_actual.execute(BudgetVsActualRequest(project_id=project_id))

        return ProjectDetailViewModel(
            overview=ProjectOverviewViewModel(
                project_id=project_response.project_id,
                project_number=project_response.project_number,
                name=project_response.project_name,
                description=project_response.description or "",
                start_date=project_response.start_date,
                end_date=project_response.end_date,
            ),
            status=ProjectStatusSummaryViewModel(
                status=status_response.project.status,
                health_indicator=status_response.health.overall_health_indicator,
                ready_for_closure=status_response.health.ready_for_closure,
            ),
            budget_summary=ProjectBudgetSummaryViewModel(
                budget_status=budget_response.budget.budget_status,
                categories=budget_response.budget.budget_categories,
                planned_budget_total=budget_response.budget.planned_budget_total,
                budget_variance=budget_response.variance.budget_variance,
            ),
            accounting_summary=ProjectAccountingSummaryViewModel(
                accounting_status=status_response.accounting.accounting_status,
                journal_count=budget_response.accounting.journal_count,
                actual_total=budget_response.accounting.actual_total,
                fiscal_year=budget_response.accounting.fiscal_year,
            ),
            document_summary=ProjectDocumentSummaryViewModel(
                total_documents=status_response.documents.total_documents,
                finalized_documents=status_response.documents.finalized_documents,
                outstanding_documents=status_response.documents.outstanding_documents,
            ),
            archive_status=ProjectArchiveStatusViewModel(
                archive_status=status_response.archive.archive_status,
                closure_status=status_response.archive.closure_status,
            ),
        )

    def create_project(self, command: CreateProjectCommandViewModel) -> UUID:
        response = self._create_project_workflow.execute(
            CompleteProjectCreationWorkflowRequest(
                organization_id=command.organization_id,
                organization_owner_contact_id=command.organization_owner_contact_id,
                project_number=command.project_number,
                project_name=command.project_name,
                project_priority=command.project_priority,
                project_description=command.project_description,
                project_start_date=command.project_start_date,
                project_end_date=command.project_end_date,
            )
        )
        self._last_selected_project_id = response.project_id
        return response.project_id

    def refresh(self) -> tuple[ProjectListViewModel, ProjectDetailViewModel | None]:
        list_vm = self.load_project_list(filters=self._last_filters)
        detail_vm = None
        if self._last_selected_project_id is not None:
            detail_vm = self.open_project(self._last_selected_project_id)
        return list_vm, detail_vm

    def navigate_to_documents(self, project_id: UUID) -> None:
        if self._navigation.to_documents is not None:
            self._navigation.to_documents(project_id)

    def navigate_to_accounting(self, project_id: UUID) -> None:
        if self._navigation.to_accounting is not None:
            self._navigation.to_accounting(project_id)

    @staticmethod
    def _sort_items(
        items: tuple[ProjectListItemViewModel, ...],
        filters: ProjectListFilterViewModel,
    ) -> tuple[ProjectListItemViewModel, ...]:
        key_map = {
            ProjectSortField.PROJECT_NUMBER: lambda value: value.project_number,
            ProjectSortField.NAME: lambda value: value.name,
            ProjectSortField.STATUS: lambda value: value.status,
            ProjectSortField.PRIORITY: lambda value: value.priority,
            ProjectSortField.CREATED_AT: lambda value: value.created_at
            or datetime.min,
        }
        key = key_map[filters.sort_by]
        return tuple(sorted(items, key=key, reverse=filters.descending))

    @staticmethod
    def _paginate(
        items: tuple[ProjectListItemViewModel, ...],
        filters: ProjectListFilterViewModel,
    ) -> tuple[tuple[ProjectListItemViewModel, ...], PaginationViewModel]:
        total_items = len(items)
        page_size = max(filters.page_size, 1)
        total_pages = max((total_items + page_size - 1) // page_size, 1)
        page = min(max(filters.page, 1), total_pages)
        start = (page - 1) * page_size
        end = start + page_size
        paged = items[start:end]

        pagination = PaginationViewModel(
            page=page,
            page_size=page_size,
            total_items=total_items,
            total_pages=total_pages,
            has_previous=page > 1,
            has_next=page < total_pages,
        )
        return tuple(paged), pagination

