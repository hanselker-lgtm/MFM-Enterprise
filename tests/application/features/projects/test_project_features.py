from __future__ import annotations

from dataclasses import FrozenInstanceError
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from importlib import import_module
from uuid import UUID

import pytest

from mfm.application.features.projects.archive_project_feature import ArchiveProjectFeature
from mfm.application.features.projects.archive_project_feature import ArchiveProjectRequest
from mfm.application.features.projects.complete_project_feature import CompleteProjectFeature
from mfm.application.features.projects.complete_project_feature import CompleteProjectRequest
from mfm.application.features.projects.create_project_feature import (
    BusinessRuleViolation as FeatureBusinessRuleViolation,
)
from mfm.application.features.projects.create_project_feature import (
    CreateProjectFeature,
)
from mfm.application.features.projects.create_project_feature import (
    CreateProjectRequest,
)
from mfm.application.features.projects.create_project_feature import (
    ExternalReferenceInput,
)
from mfm.application.features.projects.create_project_feature import (
    ProjectActivityInput,
)
from mfm.application.features.projects.create_project_feature import (
    ProjectAssignmentInput,
)
from mfm.application.features.projects.create_project_feature import (
    ProjectMilestoneInput,
)
from mfm.application.features.projects.create_project_feature import (
    RepositoryException as FeatureRepositoryException,
)
from mfm.application.features.projects.create_project_feature import (
    ValidationException as FeatureValidationException,
)
from mfm.application.features.projects.delete_project_feature import DeleteProjectFeature
from mfm.application.features.projects.delete_project_feature import DeleteProjectRequest
from mfm.application.features.projects.get_project_feature import GetProjectFeature
from mfm.application.features.projects.get_project_feature import GetProjectRequest
from mfm.application.features.projects.list_projects_feature import ListProjectsFeature
from mfm.application.features.projects.list_projects_feature import ListProjectsRequest
from mfm.application.features.projects.search_projects_feature import SearchProjectsFeature
from mfm.application.features.projects.search_projects_feature import SearchProjectsRequest
from mfm.application.features.projects.update_project_feature import UpdateProjectFeature
from mfm.application.features.projects.update_project_feature import UpdateProjectRequest
from mfm.application.projects.archive_project import ArchiveProjectUseCase
from mfm.application.projects.complete_project import CompleteProjectUseCase
from mfm.application.projects.create_project import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.projects.create_project import (
    CreateProjectResponse as ServiceCreateProjectResponse,
)
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.create_project import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.projects.create_project import (
    ValidationException as ServiceValidationException,
)
from mfm.application.projects.delete_project import DeleteProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.projects.list_projects import ListProjectsUseCase
from mfm.application.projects.search_projects import SearchProjectsUseCase
from mfm.application.projects.update_project import UpdateProjectUseCase
from mfm.domain.projects.project_status import ProjectStatus
from tests.application.projects.test_project_use_cases import FakeProjectsUnitOfWork


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        if self._error is not None:
            raise self._error
        return self._response


def _aware(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, 0, tzinfo=UTC)


def _milestone(name: str, sequence: int) -> ProjectMilestoneInput:
    return ProjectMilestoneInput(name=name, sequence=sequence, status="PLANNED")


def _activity(title: str, *, priority: str = "NORMAL") -> ProjectActivityInput:
    return ProjectActivityInput(
        title=title,
        status="ACTIVE",
        priority=priority,
        estimated_hours=Decimal("8.50"),
    )


def _assignment(role: str) -> ProjectAssignmentInput:
    return ProjectAssignmentInput(
        organisation_id=UUID("00000000-0000-0000-0000-00000000CC01"),
        contact_id=UUID("00000000-0000-0000-0000-00000000CC02"),
        role=role,
    )


def _reference(reference_type: str, external_id: UUID) -> ExternalReferenceInput:
    return ExternalReferenceInput(
        reference_type=reference_type,
        external_id=external_id,
        description="Feature reference",
    )


def _service_create_response() -> ServiceCreateProjectResponse:
    return CreateProjectUseCase(unit_of_work=FakeProjectsUnitOfWork()).execute(
        request=CreateProjectUseCase(unit_of_work=FakeProjectsUnitOfWork())
        .execute.__self__  # type: ignore[attr-defined]
    )


def _create_project(
    uow: FakeProjectsUnitOfWork,
    *,
    number: str,
    status: str = "PLANNED",
    reference_type: str = "PURCHASE_ORDER",
) -> UUID:
    response = CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow)).execute(
        CreateProjectRequest(
            project_number=number,
            project_name="Dock Program",
            status=status,
            priority="HIGH",
            description="Feature flow",
            milestones=(_milestone("Kickoff", 1),),
            activities=(_activity("Preparation", priority="URGENT"),),
            assignments=(_assignment("Project Manager"),),
            references=(
                _reference(
                    reference_type,
                    UUID("00000000-0000-0000-0000-00000000CC11"),
                ),
            ),
        )
    )
    return response.project.project_id


def test_create_feature_request_mapping_response_mapping_and_immutability() -> None:
    uow = FakeProjectsUnitOfWork()
    feature = CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow))

    request = CreateProjectRequest(
        project_number="PROJ-FEAT-001",
        project_name="Feature Project",
        status="PLANNED",
        priority="NORMAL",
        milestones=(_milestone("Design", 1),),
        activities=(_activity("Draft plan"),),
        assignments=(_assignment("Lead"),),
        references=(
            _reference("DOCUMENT", UUID("00000000-0000-0000-0000-00000000CC21")),
        ),
    )

    response = feature.execute(request)

    assert response.project.project_number == "PROJ-FEAT-001"
    assert response.project.status == "PLANNED"
    assert response.project.activities[0].priority == "NORMAL"
    assert response.project.references[0].reference_type == "DOCUMENT"
    assert is_dataclass(response.project)

    with pytest.raises(FrozenInstanceError):
        request.project_name = "Changed"  # type: ignore[misc]


def test_create_feature_error_mapping() -> None:
    invalid = CreateProjectFeature(
        service=StubService(error=ServiceValidationException("invalid"))
    )
    with pytest.raises(FeatureValidationException):
        invalid.execute(CreateProjectRequest(project_number="PROJ-ERR-1", project_name="x"))

    duplicate = CreateProjectFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate"))
    )
    with pytest.raises(FeatureBusinessRuleViolation):
        duplicate.execute(CreateProjectRequest(project_number="PROJ-ERR-2", project_name="x"))

    failing = CreateProjectFeature(
        service=StubService(error=ServiceRepositoryException("failed"))
    )
    with pytest.raises(FeatureRepositoryException):
        failing.execute(CreateProjectRequest(project_number="PROJ-ERR-3", project_name="x"))


def test_get_feature_existing_and_missing_mapping() -> None:
    uow = FakeProjectsUnitOfWork()
    project_id = _create_project(uow, number="PROJ-FEAT-GET")

    get_feature = GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow))
    existing = get_feature.execute(GetProjectRequest(project_id=project_id))
    assert existing.project.project_id == project_id

    with pytest.raises(FeatureBusinessRuleViolation):
        get_feature.execute(
            GetProjectRequest(project_id=UUID("00000000-0000-0000-0000-00000000F404"))
        )


def test_list_and_search_features_delegate_and_preserve_order() -> None:
    uow = FakeProjectsUnitOfWork()
    _create_project(uow, number="PROJ-FEAT-A", status="PLANNED", reference_type="PURCHASE_ORDER")
    second_id = _create_project(uow, number="PROJ-FEAT-B", status="PLANNED", reference_type="DOCUMENT")

    project = uow.project_repository.get(project_id=project_id_from_uuid(second_id))
    assert project is not None
    project.change_status(ProjectStatus.ACTIVE, when=_aware(2030, 1, 8, 8))
    uow.project_repository.update(project)

    listed = ListProjectsFeature(service=ListProjectsUseCase(unit_of_work=uow)).execute(
        ListProjectsRequest()
    )
    assert [item.project_number for item in listed.projects] == ["PROJ-FEAT-A", "PROJ-FEAT-B"]

    searched_text = SearchProjectsFeature(service=SearchProjectsUseCase(unit_of_work=uow)).execute(
        SearchProjectsRequest(text="FEAT-B")
    )
    assert [item.project_number for item in searched_text.projects] == ["PROJ-FEAT-B"]

    searched_status = SearchProjectsFeature(service=SearchProjectsUseCase(unit_of_work=uow)).execute(
        SearchProjectsRequest(status="ACTIVE")
    )
    assert [item.project_number for item in searched_status.projects] == ["PROJ-FEAT-B"]

    searched_ref = SearchProjectsFeature(service=SearchProjectsUseCase(unit_of_work=uow)).execute(
        SearchProjectsRequest(reference_type="PURCHASE_ORDER")
    )
    assert [item.project_number for item in searched_ref.projects] == ["PROJ-FEAT-A"]


def test_update_complete_archive_delete_features_end_to_end() -> None:
    uow = FakeProjectsUnitOfWork()
    project_id = _create_project(uow, number="PROJ-FEAT-LIFE", status="ACTIVE")

    updated = UpdateProjectFeature(service=UpdateProjectUseCase(unit_of_work=uow)).execute(
        UpdateProjectRequest(
            project_id=project_id,
            project_name="Lifecycle Project",
            priority="URGENT",
            updated_at=_aware(2030, 1, 9, 8),
            activities=(_activity("Execution", priority="HIGH"),),
        )
    )
    assert updated.project.project_name == "Lifecycle Project"

    completed = CompleteProjectFeature(service=CompleteProjectUseCase(unit_of_work=uow)).execute(
        CompleteProjectRequest(project_id=project_id, completed_at=_aware(2030, 1, 10, 8))
    )
    assert completed.project.status == "COMPLETED"

    archived = ArchiveProjectFeature(service=ArchiveProjectUseCase(unit_of_work=uow)).execute(
        ArchiveProjectRequest(project_id=project_id, archived_at=_aware(2030, 1, 11, 8))
    )
    assert archived.project.status == "ARCHIVED"

    deleted = DeleteProjectFeature(service=DeleteProjectUseCase(unit_of_work=uow)).execute(
        DeleteProjectRequest(project_id=project_id)
    )
    assert deleted.project_id == project_id


def test_delete_feature_missing_maps_business_rule() -> None:
    uow = FakeProjectsUnitOfWork()
    delete_feature = DeleteProjectFeature(service=DeleteProjectUseCase(unit_of_work=uow))

    with pytest.raises(FeatureBusinessRuleViolation):
        delete_feature.execute(
            DeleteProjectRequest(project_id=UUID("00000000-0000-0000-0000-00000000F405"))
        )


def test_feature_modules_do_not_reference_sqlalchemy_or_sqlite_repo() -> None:
    modules = [
        import_module("mfm.application.features.projects.create_project_feature"),
        import_module("mfm.application.features.projects.update_project_feature"),
        import_module("mfm.application.features.projects.complete_project_feature"),
        import_module("mfm.application.features.projects.archive_project_feature"),
        import_module("mfm.application.features.projects.delete_project_feature"),
        import_module("mfm.application.features.projects.get_project_feature"),
        import_module("mfm.application.features.projects.list_projects_feature"),
        import_module("mfm.application.features.projects.search_projects_feature"),
    ]

    for module in modules:
        text = (module.__doc__ or "") + "\n" + "\n".join(sorted(module.__dict__.keys()))
        lowered = text.lower()
        assert "sqlalchemy" not in lowered
        assert "sqliteprojectrepository" not in lowered
        assert "session" not in lowered


def project_id_from_uuid(value: UUID):
    from mfm.domain.projects.project_id import ProjectId

    return ProjectId(value)
