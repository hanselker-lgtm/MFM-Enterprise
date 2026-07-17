from __future__ import annotations

from datetime import UTC
from datetime import datetime
from decimal import Decimal
from types import SimpleNamespace
from uuid import UUID
from uuid import uuid4

from mfm.presentation.projects import CreateProjectCommandViewModel
from mfm.presentation.projects import ProjectController
from mfm.presentation.projects import ProjectListFilterViewModel
from mfm.presentation.projects import ProjectNavigationCallbacks
from mfm.presentation.projects import ProjectSortField


class _StubPort:
    def __init__(self, response: object) -> None:
        self.response = response
        self.requests: list[object] = []

    def execute(self, request: object) -> object:
        self.requests.append(request)
        return self.response


def _list_item(project_number: str, created_at: datetime) -> SimpleNamespace:
    return SimpleNamespace(
        project_id=uuid4(),
        project_number=project_number,
        project_name=f"Project {project_number}",
        status="ACTIVE",
        priority="NORMAL",
        created_at=created_at,
    )


def test_project_controller_loads_list_and_paginates() -> None:
    list_port = _StubPort(
        SimpleNamespace(
            projects=(
                _list_item("PRJ-002", datetime(2024, 2, 1, tzinfo=UTC)),
                _list_item("PRJ-001", datetime(2024, 1, 1, tzinfo=UTC)),
            )
        )
    )
    search_port = _StubPort(SimpleNamespace(projects=()))

    controller = ProjectController(
        list_projects_feature=list_port,
        search_projects_feature=search_port,
        get_project_feature=_StubPort(None),
        project_status_feature=_StubPort(None),
        budget_vs_actual_feature=_StubPort(None),
        create_project_workflow_feature=_StubPort(None),
    )

    vm = controller.load_project_list(
        filters=ProjectListFilterViewModel(
            sort_by=ProjectSortField.PROJECT_NUMBER,
            descending=False,
            page=1,
            page_size=1,
        )
    )

    assert len(list_port.requests) == 1
    assert len(search_port.requests) == 0
    assert vm.items[0].project_number == "PRJ-001"
    assert vm.pagination.total_items == 2
    assert vm.pagination.total_pages == 2
    assert vm.pagination.has_next is True


def test_project_controller_uses_search_when_filtering() -> None:
    project_id = uuid4()
    search_port = _StubPort(
        SimpleNamespace(
            projects=(
                SimpleNamespace(
                    project_id=project_id,
                    project_number="PRJ-ABC",
                    project_name="Search Match",
                    status="DRAFT",
                    priority="HIGH",
                ),
            )
        )
    )

    controller = ProjectController(
        list_projects_feature=_StubPort(SimpleNamespace(projects=())),
        search_projects_feature=search_port,
        get_project_feature=_StubPort(None),
        project_status_feature=_StubPort(None),
        budget_vs_actual_feature=_StubPort(None),
        create_project_workflow_feature=_StubPort(None),
    )

    vm = controller.load_project_list(
        filters=ProjectListFilterViewModel(text="abc", status="ALL")
    )

    assert len(search_port.requests) == 1
    assert vm.items[0].project_id == project_id
    assert vm.items[0].created_at is None


def test_project_controller_maps_detail_and_navigation_callbacks() -> None:
    project_id = uuid4()
    documents_calls: list[UUID] = []
    accounting_calls: list[UUID] = []

    controller = ProjectController(
        list_projects_feature=_StubPort(SimpleNamespace(projects=())),
        search_projects_feature=_StubPort(SimpleNamespace(projects=())),
        get_project_feature=_StubPort(
            SimpleNamespace(
                project=SimpleNamespace(
                    project_id=project_id,
                    project_number="PRJ-100",
                    project_name="Dock Refit",
                    description="Scheduled refit",
                    start_date=None,
                    end_date=None,
                )
            )
        ),
        project_status_feature=_StubPort(
            SimpleNamespace(
                project=SimpleNamespace(status="ACTIVE"),
                health=SimpleNamespace(
                    overall_health_indicator="GREEN",
                    ready_for_closure=False,
                ),
                accounting=SimpleNamespace(accounting_status="SYNCED"),
                documents=SimpleNamespace(
                    total_documents=10,
                    finalized_documents=7,
                    outstanding_documents=3,
                ),
                archive=SimpleNamespace(
                    archive_status="NOT_ARCHIVED",
                    closure_status="OPEN",
                ),
            )
        ),
        budget_vs_actual_feature=_StubPort(
            SimpleNamespace(
                budget=SimpleNamespace(
                    budget_status="LIMITED_BUDGET_METADATA",
                    budget_categories=("OPEX",),
                    planned_budget_total=Decimal("100.00"),
                ),
                variance=SimpleNamespace(budget_variance=Decimal("-20.00")),
                accounting=SimpleNamespace(
                    journal_count=2,
                    actual_total=Decimal("120.00"),
                    fiscal_year=2024,
                ),
            )
        ),
        create_project_workflow_feature=_StubPort(None),
        navigation=ProjectNavigationCallbacks(
            to_documents=lambda value: documents_calls.append(value),
            to_accounting=lambda value: accounting_calls.append(value),
        ),
    )

    detail = controller.open_project(project_id)

    assert detail.overview.project_number == "PRJ-100"
    assert detail.status.health_indicator == "GREEN"
    assert detail.document_summary.outstanding_documents == 3

    controller.navigate_to_documents(project_id)
    controller.navigate_to_accounting(project_id)

    assert documents_calls == [project_id]
    assert accounting_calls == [project_id]


def test_project_controller_create_project_uses_workflow() -> None:
    project_id = uuid4()
    create_port = _StubPort(SimpleNamespace(project_id=project_id))

    controller = ProjectController(
        list_projects_feature=_StubPort(SimpleNamespace(projects=())),
        search_projects_feature=_StubPort(SimpleNamespace(projects=())),
        get_project_feature=_StubPort(None),
        project_status_feature=_StubPort(None),
        budget_vs_actual_feature=_StubPort(None),
        create_project_workflow_feature=create_port,
    )

    created = controller.create_project(
        CreateProjectCommandViewModel(
            organization_id=UUID("00000000-0000-0000-0000-000000000001"),
            organization_owner_contact_id=UUID("00000000-0000-0000-0000-000000000002"),
            project_number="PRJ-501",
            project_name="New Yard Project",
        )
    )

    assert created == project_id
    assert controller.last_selected_project_id == project_id
    assert len(create_port.requests) == 1
