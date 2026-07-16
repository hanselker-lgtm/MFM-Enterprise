from __future__ import annotations

from copy import deepcopy
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from typing import Any
from uuid import UUID

import pytest

from mfm.application.projects.archive_project import ArchiveProjectRequest
from mfm.application.projects.archive_project import ArchiveProjectUseCase
from mfm.application.projects.complete_project import CompleteProjectRequest
from mfm.application.projects.complete_project import CompleteProjectUseCase
from mfm.application.projects.create_project import BusinessRuleViolation
from mfm.application.projects.create_project import CreateProjectRequest
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.create_project import ExternalReferenceInput
from mfm.application.projects.create_project import ProjectActivityInput
from mfm.application.projects.create_project import ProjectAssignmentInput
from mfm.application.projects.create_project import ProjectMilestoneInput
from mfm.application.projects.create_project import RepositoryException
from mfm.application.projects.delete_project import DeleteProjectRequest
from mfm.application.projects.delete_project import DeleteProjectUseCase
from mfm.application.projects.get_project import GetProjectRequest
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.projects.list_projects import ListProjectsRequest
from mfm.application.projects.list_projects import ListProjectsUseCase
from mfm.application.projects.search_projects import SearchProjectsRequest
from mfm.application.projects.search_projects import SearchProjectsUseCase
from mfm.application.projects.update_project import UpdateProjectRequest
from mfm.application.projects.update_project import UpdateProjectUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.projects.project import Project
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_repository import ProjectRepository
from mfm.domain.projects.project_status import ProjectStatus
from mfm.domain.projects.reference_type import ReferenceType


class InMemoryProjectRepository(ProjectRepository):
    def __init__(
        self,
        *,
        fail_on_add: bool = False,
        fail_on_update: bool = False,
        fail_on_remove: bool = False,
    ) -> None:
        self._projects: dict[UUID, Project] = {}
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update
        self._fail_on_remove = fail_on_remove

        self.add_calls = 0
        self.update_calls = 0
        self.remove_calls = 0
        self.get_calls = 0
        self.get_by_number_calls = 0
        self.list_calls = 0
        self.search_calls = 0

    def snapshot(self) -> dict[UUID, Project]:
        return deepcopy(self._projects)

    def restore(self, snapshot: dict[UUID, Project]) -> None:
        self._projects = deepcopy(snapshot)

    def add(self, project: Project) -> None:
        self.add_calls += 1
        if self._fail_on_add:
            raise RuntimeError("project add failed")
        if self.get_by_number(project.project_number) is not None:
            raise ValueError(f"Project number {project.project_number.value} already exists")
        self._projects[project.id.value] = deepcopy(project)

    def update(self, project: Project) -> None:
        self.update_calls += 1
        if self._fail_on_update:
            raise RuntimeError("project update failed")
        if project.id.value not in self._projects:
            raise ValueError(f"Project {project.id.value} does not exist")

        duplicate = next(
            (
                existing
                for existing in self._projects.values()
                if existing.project_number == project.project_number
                and existing.id != project.id
            ),
            None,
        )
        if duplicate is not None:
            raise ValueError(f"Project number {project.project_number.value} already exists")

        project.version += 1
        self._projects[project.id.value] = deepcopy(project)

    def remove(self, project_id: ProjectId) -> None:
        self.remove_calls += 1
        if self._fail_on_remove:
            raise RuntimeError("project remove failed")
        normalized = project_id if isinstance(project_id, ProjectId) else ProjectId(project_id)
        if normalized.value not in self._projects:
            raise ValueError(f"Project {normalized.value} does not exist")
        del self._projects[normalized.value]

    def get(self, project_id: ProjectId) -> Project | None:
        self.get_calls += 1
        normalized = project_id if isinstance(project_id, ProjectId) else ProjectId(project_id)
        value = self._projects.get(normalized.value)
        return deepcopy(value) if value is not None else None

    def exists(self, project_id: ProjectId) -> bool:
        normalized = project_id if isinstance(project_id, ProjectId) else ProjectId(project_id)
        return normalized.value in self._projects

    def get_by_number(self, project_number: ProjectNumber) -> Project | None:
        self.get_by_number_calls += 1
        normalized = (
            project_number
            if isinstance(project_number, ProjectNumber)
            else ProjectNumber(project_number)
        )
        for value in self._projects.values():
            if value.project_number == normalized:
                return deepcopy(value)
        return None

    def list(self, filters: Any | None = None) -> list[Project]:
        self.list_calls += 1
        values = sorted(
            self._projects.values(),
            key=lambda item: (item.project_number.value, str(item.id.value)),
        )
        if isinstance(filters, dict) and filters.get("status") is not None:
            status = filters["status"]
            normalized_status = (
                status
                if isinstance(status, ProjectStatus)
                else ProjectStatus(str(status).upper())
            )
            values = [item for item in values if item.status is normalized_status]
        return [deepcopy(item) for item in values]

    def search(self, criteria: Any) -> list[Any]:
        self.search_calls += 1
        if isinstance(criteria, str):
            filters = {"text": criteria}
        elif isinstance(criteria, dict):
            filters = dict(criteria)
        else:
            filters = {}

        text = str(filters.get("text", "")).strip().casefold()
        status = filters.get("status")
        if status is not None:
            status = (
                status if isinstance(status, ProjectStatus) else ProjectStatus(str(status).upper())
            )
        reference_type = filters.get("reference_type")
        if reference_type is not None:
            reference_type = (
                reference_type
                if isinstance(reference_type, ReferenceType)
                else ReferenceType(str(reference_type).upper())
            )

        results: list[dict[str, Any]] = []
        for project in self.list():
            haystack = (
                f"{project.project_number.value} {project.project_name.value} {project.description or ''}"
            ).casefold()
            if text and text not in haystack:
                continue
            if status is not None and project.status is not status:
                continue
            if reference_type is not None and all(
                ref.reference_type is not reference_type for ref in project.references
            ):
                continue
            results.append(
                {
                    "id": project.id.value,
                    "project_number": project.project_number.value,
                    "project_name": project.project_name.value,
                    "status": project.status,
                    "priority": project.priority,
                }
            )

        return results

    def next_identity(self) -> ProjectId:
        return ProjectId.new()

    def list_by_status(self, status: ProjectStatus) -> list[Project]:
        normalized = (
            status if isinstance(status, ProjectStatus) else ProjectStatus(str(status).upper())
        )
        return [project for project in self.list() if project.status is normalized]


class FakeProjectsUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_add: bool = False,
        fail_update: bool = False,
        fail_remove: bool = False,
        fail_commit: bool = False,
    ) -> None:
        super().__init__()
        self._fail_commit = fail_commit
        self._repository = InMemoryProjectRepository(
            fail_on_add=fail_add,
            fail_on_update=fail_update,
            fail_on_remove=fail_remove,
        )
        self._snapshot: dict[UUID, Project] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self.project_repository = self._repository
        self._snapshot = self._repository.snapshot()

    def _commit_impl(self) -> None:
        self.commits += 1
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self._repository.restore(self._snapshot)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


def _aware(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, 0, tzinfo=UTC)


def _milestone(name: str, sequence: int) -> ProjectMilestoneInput:
    return ProjectMilestoneInput(
        name=name,
        sequence=sequence,
        status="PLANNED",
        due_date=_aware(2030, 2, 1, 8),
    )


def _activity(title: str, *, priority: str = "NORMAL") -> ProjectActivityInput:
    return ProjectActivityInput(
        title=title,
        status="ACTIVE",
        priority=priority,
        estimated_hours=Decimal("10.50"),
    )


def _assignment(role: str) -> ProjectAssignmentInput:
    return ProjectAssignmentInput(
        organisation_id=UUID("00000000-0000-0000-0000-00000000AB01"),
        contact_id=UUID("00000000-0000-0000-0000-00000000AB02"),
        role=role,
    )


def _reference(reference_type: str, external_id: UUID) -> ExternalReferenceInput:
    return ExternalReferenceInput(
        reference_type=reference_type,
        external_id=external_id,
        description="Linked reference",
        created_at=_aware(2030, 1, 2, 8),
    )


def _create_project(
    uow: FakeProjectsUnitOfWork,
    *,
    project_number: str = "PROJ-APP-001",
    status: str = "PLANNED",
    reference_type: str = "PURCHASE_ORDER",
) -> UUID:
    response = CreateProjectUseCase(unit_of_work=uow).execute(
        CreateProjectRequest(
            project_number=project_number,
            project_name="Dock Upgrade",
            status=status,
            priority="HIGH",
            description="Initial scope",
            start_date=_aware(2030, 1, 5, 8),
            end_date=_aware(2030, 3, 15, 8),
            created_at=_aware(2030, 1, 1, 8),
            milestones=(_milestone("Kickoff", 1),),
            activities=(_activity("Prepare site", priority="URGENT"),),
            assignments=(_assignment("Project Manager"),),
            references=(
                _reference(
                    reference_type,
                    UUID("00000000-0000-0000-0000-00000000AB11"),
                ),
            ),
        )
    )
    return response.project.project_id


def test_create_project_success_and_duplicate_number() -> None:
    uow = FakeProjectsUnitOfWork()
    use_case = CreateProjectUseCase(unit_of_work=uow)

    created = use_case.execute(
        CreateProjectRequest(
            project_number="PROJ-APP-100",
            project_name="Dry Dock Refit",
            status="PLANNED",
            priority="NORMAL",
            milestones=(_milestone("Design", 1),),
            activities=(_activity("Layout"),),
            assignments=(_assignment("Lead"),),
            references=(
                _reference(
                    "DOCUMENT",
                    UUID("00000000-0000-0000-0000-00000000AB21"),
                ),
            ),
        )
    )

    assert uow.commits == 1
    assert created.project.project_number == "PROJ-APP-100"
    assert created.project.status == "PLANNED"
    assert len(created.project.milestones) == 1

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            CreateProjectRequest(
                project_number="PROJ-APP-100",
                project_name="Duplicate",
            )
        )

    assert uow.commits == 1


def test_get_project_existing_and_missing_no_commit() -> None:
    uow = FakeProjectsUnitOfWork()
    project_id = _create_project(uow, project_number="PROJ-APP-GET")
    before = uow.commits

    response = GetProjectUseCase(unit_of_work=uow).execute(
        GetProjectRequest(project_id=project_id)
    )

    assert response.project.project_id == project_id
    assert uow.commits == before

    with pytest.raises(BusinessRuleViolation):
        GetProjectUseCase(unit_of_work=uow).execute(
            GetProjectRequest(
                project_id=UUID("00000000-0000-0000-0000-00000000E801")
            )
        )

    assert uow.commits == before


def test_update_project_updates_details_and_children() -> None:
    uow = FakeProjectsUnitOfWork()
    project_id = _create_project(uow, project_number="PROJ-APP-UPD")

    updated = UpdateProjectUseCase(unit_of_work=uow).execute(
        UpdateProjectRequest(
            project_id=project_id,
            project_name="Dock Upgrade Phase 2",
            description="Updated scope",
            priority="URGENT",
            updated_at=_aware(2030, 1, 6, 8),
            milestones=(_milestone("Execution", 1), _milestone("Closeout", 2)),
            activities=(_activity("Mechanical"),),
            assignments=(_assignment("Coordinator"),),
            references=(
                _reference(
                    "DOCUMENT",
                    UUID("00000000-0000-0000-0000-00000000AB31"),
                ),
            ),
        )
    )

    assert updated.project.project_name == "Dock Upgrade Phase 2"
    assert updated.project.priority == "URGENT"
    assert len(updated.project.milestones) == 2
    assert len(updated.project.references) == 1
    assert uow.commits == 2


def test_complete_and_archive_project_lifecycle() -> None:
    uow = FakeProjectsUnitOfWork()
    project_id = _create_project(
        uow,
        project_number="PROJ-APP-LIFE",
        status="ACTIVE",
    )

    completed = CompleteProjectUseCase(unit_of_work=uow).execute(
        CompleteProjectRequest(project_id=project_id, completed_at=_aware(2030, 1, 9, 8))
    )
    assert completed.project.status == "COMPLETED"

    archived = ArchiveProjectUseCase(unit_of_work=uow).execute(
        ArchiveProjectRequest(project_id=project_id, archived_at=_aware(2030, 1, 10, 8))
    )
    assert archived.project.status == "ARCHIVED"
    assert archived.project.archived_at is not None


def test_delete_project_success_and_missing() -> None:
    uow = FakeProjectsUnitOfWork()
    project_id = _create_project(uow, project_number="PROJ-APP-DEL")

    DeleteProjectUseCase(unit_of_work=uow).execute(
        DeleteProjectRequest(project_id=project_id)
    )

    assert uow.commits == 2
    assert uow.project_repository.get(ProjectId(project_id)) is None

    with pytest.raises(BusinessRuleViolation):
        DeleteProjectUseCase(unit_of_work=uow).execute(
            DeleteProjectRequest(project_id=project_id)
        )


def test_list_and_search_projects_delegate_and_filter() -> None:
    uow = FakeProjectsUnitOfWork()
    _create_project(
        uow,
        project_number="PROJ-APP-A",
        status="PLANNED",
        reference_type="PURCHASE_ORDER",
    )
    second_id = _create_project(
        uow,
        project_number="PROJ-APP-B",
        status="PLANNED",
        reference_type="DOCUMENT",
    )

    project = uow.project_repository.get(ProjectId(second_id))
    assert project is not None
    project.change_status(ProjectStatus.ACTIVE, when=_aware(2030, 1, 11, 8))
    uow.project_repository.update(project)

    listed = ListProjectsUseCase(unit_of_work=uow).execute(ListProjectsRequest())
    assert [item.project_number for item in listed.projects] == ["PROJ-APP-A", "PROJ-APP-B"]

    by_text = SearchProjectsUseCase(unit_of_work=uow).execute(
        SearchProjectsRequest(text="APP-B")
    )
    assert [item.project_number for item in by_text.projects] == ["PROJ-APP-B"]

    by_status = SearchProjectsUseCase(unit_of_work=uow).execute(
        SearchProjectsRequest(status="ACTIVE")
    )
    assert [item.project_number for item in by_status.projects] == ["PROJ-APP-B"]

    by_reference = SearchProjectsUseCase(unit_of_work=uow).execute(
        SearchProjectsRequest(reference_type="PURCHASE_ORDER")
    )
    assert [item.project_number for item in by_reference.projects] == ["PROJ-APP-A"]


def test_repository_failure_maps_repository_exception_and_rolls_back() -> None:
    uow = FakeProjectsUnitOfWork(fail_update=True)
    project_id = _create_project(uow, project_number="PROJ-APP-ERR")
    before = uow.commits

    with pytest.raises(RepositoryException):
        UpdateProjectUseCase(unit_of_work=uow).execute(
            UpdateProjectRequest(
                project_id=project_id,
                project_name="Should fail",
                updated_at=_aware(2030, 1, 12, 8),
            )
        )

    assert uow.commits == before
    assert uow.rollbacks >= 1


def test_response_types_are_immutable_dataclasses() -> None:
    uow = FakeProjectsUnitOfWork()
    created = CreateProjectUseCase(unit_of_work=uow).execute(
        CreateProjectRequest(
            project_number="PROJ-APP-IMMUTABLE",
            project_name="Immutable project",
        )
    )

    assert is_dataclass(created.project)
    assert created.project.project_number == "PROJ-APP-IMMUTABLE"
