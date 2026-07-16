"""Create Project use case and shared projects application DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any
from typing import Mapping
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.projects.exceptions import ProjectError
from mfm.domain.projects.external_reference import ExternalReference
from mfm.domain.projects.project import Project
from mfm.domain.projects.project_activity import ProjectActivity
from mfm.domain.projects.project_assignment import ProjectAssignment
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_milestone import ProjectMilestone
from mfm.domain.projects.project_name import ProjectName
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_priority import ProjectPriority
from mfm.domain.projects.project_repository import ProjectRepository
from mfm.domain.projects.project_status import ProjectStatus
from mfm.domain.projects.reference_type import ReferenceType


class ApplicationException(Exception):
    """Base exception for projects application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository and persistence failures."""


@dataclass(frozen=True, slots=True)
class ProjectMilestoneInput:
    name: str
    sequence: int
    status: str = "PLANNED"
    description: str | None = None
    due_date: datetime | None = None
    completed_date: datetime | None = None
    milestone_id: UUID | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException(f"{field_name}.name must be a non-empty string")
        if not isinstance(self.sequence, int) or isinstance(self.sequence, bool):
            raise ValidationException(f"{field_name}.sequence must be integer")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException(f"{field_name}.status must be a non-empty string")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException(f"{field_name}.description must be string or None")
        if self.due_date is not None and not isinstance(self.due_date, datetime):
            raise ValidationException(f"{field_name}.due_date must be datetime or None")
        if self.completed_date is not None and not isinstance(self.completed_date, datetime):
            raise ValidationException(f"{field_name}.completed_date must be datetime or None")
        if self.milestone_id is not None and not isinstance(self.milestone_id, UUID):
            raise ValidationException(f"{field_name}.milestone_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class ProjectActivityInput:
    title: str
    status: str = "PLANNED"
    description: str | None = None
    planned_start: datetime | None = None
    planned_finish: datetime | None = None
    actual_start: datetime | None = None
    actual_finish: datetime | None = None
    priority: str = "NORMAL"
    estimated_hours: Decimal | str | int | None = None
    actual_hours: Decimal | str | int | None = None
    activity_id: UUID | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValidationException(f"{field_name}.title must be a non-empty string")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException(f"{field_name}.status must be a non-empty string")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException(f"{field_name}.description must be string or None")
        if self.planned_start is not None and not isinstance(self.planned_start, datetime):
            raise ValidationException(f"{field_name}.planned_start must be datetime or None")
        if self.planned_finish is not None and not isinstance(self.planned_finish, datetime):
            raise ValidationException(f"{field_name}.planned_finish must be datetime or None")
        if self.actual_start is not None and not isinstance(self.actual_start, datetime):
            raise ValidationException(f"{field_name}.actual_start must be datetime or None")
        if self.actual_finish is not None and not isinstance(self.actual_finish, datetime):
            raise ValidationException(f"{field_name}.actual_finish must be datetime or None")
        if not isinstance(self.priority, str) or not self.priority.strip():
            raise ValidationException(f"{field_name}.priority must be a non-empty string")
        if self.estimated_hours is not None and (
            isinstance(self.estimated_hours, bool) or isinstance(self.estimated_hours, float)
        ):
            raise ValidationException(
                f"{field_name}.estimated_hours must not be bool/float"
            )
        if self.actual_hours is not None and (
            isinstance(self.actual_hours, bool) or isinstance(self.actual_hours, float)
        ):
            raise ValidationException(
                f"{field_name}.actual_hours must not be bool/float"
            )
        if self.activity_id is not None and not isinstance(self.activity_id, UUID):
            raise ValidationException(f"{field_name}.activity_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class ProjectAssignmentInput:
    organisation_id: UUID
    contact_id: UUID
    role: str
    assigned_from: datetime | None = None
    assigned_until: datetime | None = None
    assignment_id: UUID | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.organisation_id, UUID):
            raise ValidationException(f"{field_name}.organisation_id must be UUID")
        if not isinstance(self.contact_id, UUID):
            raise ValidationException(f"{field_name}.contact_id must be UUID")
        if not isinstance(self.role, str) or not self.role.strip():
            raise ValidationException(f"{field_name}.role must be a non-empty string")
        if self.assigned_from is not None and not isinstance(self.assigned_from, datetime):
            raise ValidationException(f"{field_name}.assigned_from must be datetime or None")
        if self.assigned_until is not None and not isinstance(self.assigned_until, datetime):
            raise ValidationException(f"{field_name}.assigned_until must be datetime or None")
        if self.assignment_id is not None and not isinstance(self.assignment_id, UUID):
            raise ValidationException(f"{field_name}.assignment_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class ExternalReferenceInput:
    reference_type: str
    external_id: UUID
    description: str | None = None
    created_at: datetime | None = None
    reference_id: UUID | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.reference_type, str) or not self.reference_type.strip():
            raise ValidationException(
                f"{field_name}.reference_type must be a non-empty string"
            )
        if not isinstance(self.external_id, UUID):
            raise ValidationException(f"{field_name}.external_id must be UUID")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException(f"{field_name}.description must be string or None")
        if self.created_at is not None and not isinstance(self.created_at, datetime):
            raise ValidationException(f"{field_name}.created_at must be datetime or None")
        if self.reference_id is not None and not isinstance(self.reference_id, UUID):
            raise ValidationException(f"{field_name}.reference_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class ProjectMilestoneResponse:
    milestone_id: UUID
    name: str
    sequence: int
    status: str
    description: str | None
    due_date: datetime | None
    completed_date: datetime | None


@dataclass(frozen=True, slots=True)
class ProjectActivityResponse:
    activity_id: UUID
    title: str
    status: str
    description: str | None
    planned_start: datetime | None
    planned_finish: datetime | None
    actual_start: datetime | None
    actual_finish: datetime | None
    priority: str
    estimated_hours: Decimal | None
    actual_hours: Decimal | None


@dataclass(frozen=True, slots=True)
class ProjectAssignmentResponse:
    assignment_id: UUID
    organisation_id: UUID
    contact_id: UUID
    role: str
    assigned_from: datetime | None
    assigned_until: datetime | None


@dataclass(frozen=True, slots=True)
class ExternalReferenceResponse:
    reference_id: UUID
    reference_type: str
    external_id: UUID
    description: str | None
    created_at: datetime


@dataclass(frozen=True, slots=True)
class ProjectResponse:
    project_id: UUID
    project_number: str
    project_name: str
    status: str
    priority: str
    description: str | None
    start_date: datetime | None
    end_date: datetime | None
    created_at: datetime
    updated_at: datetime | None
    archived_at: datetime | None
    version: int
    milestones: tuple[ProjectMilestoneResponse, ...]
    activities: tuple[ProjectActivityResponse, ...]
    assignments: tuple[ProjectAssignmentResponse, ...]
    references: tuple[ExternalReferenceResponse, ...]


@dataclass(frozen=True, slots=True)
class ProjectSearchResultResponse:
    project_id: UUID
    project_number: str
    project_name: str
    status: str
    priority: str


@dataclass(frozen=True, slots=True)
class CreateProjectRequest:
    project_number: str
    project_name: str
    project_id: UUID | None = None
    status: str = "DRAFT"
    priority: str = "NORMAL"
    description: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    archived_at: datetime | None = None
    milestones: tuple[ProjectMilestoneInput, ...] = ()
    activities: tuple[ProjectActivityInput, ...] = ()
    assignments: tuple[ProjectAssignmentInput, ...] = ()
    references: tuple[ExternalReferenceInput, ...] = ()

    def validate(self) -> None:
        if not isinstance(self.project_number, str) or not self.project_number.strip():
            raise ValidationException("project_number must be a non-empty string")
        if not isinstance(self.project_name, str) or not self.project_name.strip():
            raise ValidationException("project_name must be a non-empty string")
        if self.project_id is not None and not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID or None")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be a non-empty string")
        if not isinstance(self.priority, str) or not self.priority.strip():
            raise ValidationException("priority must be a non-empty string")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException("description must be string or None")
        if self.start_date is not None and not isinstance(self.start_date, datetime):
            raise ValidationException("start_date must be datetime or None")
        if self.end_date is not None and not isinstance(self.end_date, datetime):
            raise ValidationException("end_date must be datetime or None")
        if self.created_at is not None and not isinstance(self.created_at, datetime):
            raise ValidationException("created_at must be datetime or None")
        if self.updated_at is not None and not isinstance(self.updated_at, datetime):
            raise ValidationException("updated_at must be datetime or None")
        if self.archived_at is not None and not isinstance(self.archived_at, datetime):
            raise ValidationException("archived_at must be datetime or None")
        if not isinstance(self.milestones, tuple):
            raise ValidationException("milestones must be tuple")
        if not isinstance(self.activities, tuple):
            raise ValidationException("activities must be tuple")
        if not isinstance(self.assignments, tuple):
            raise ValidationException("assignments must be tuple")
        if not isinstance(self.references, tuple):
            raise ValidationException("references must be tuple")

        for index, milestone in enumerate(self.milestones):
            milestone.validate(field_name=f"milestones[{index}]")
        for index, activity in enumerate(self.activities):
            activity.validate(field_name=f"activities[{index}]")
        for index, assignment in enumerate(self.assignments):
            assignment.validate(field_name=f"assignments[{index}]")
        for index, reference in enumerate(self.references):
            reference.validate(field_name=f"references[{index}]")


@dataclass(frozen=True, slots=True)
class CreateProjectResponse:
    project: ProjectResponse


class CreateProjectUseCase:
    """Create project aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateProjectRequest) -> CreateProjectResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: ProjectRepository = uow.project_repository

                normalized_number = ProjectNumber(request.project_number)
                existing = repository.get_by_number(normalized_number)
                if existing is not None:
                    raise BusinessRuleViolation(
                        f"Project number {normalized_number.value} already exists"
                    )

                project_id = (
                    ProjectId(request.project_id)
                    if request.project_id is not None
                    else repository.next_identity()
                )

                project = Project(
                    id=project_id,
                    project_number=normalized_number,
                    project_name=ProjectName(request.project_name),
                    status=ProjectStatus(request.status.strip().upper()),
                    priority=ProjectPriority(request.priority.strip().upper()),
                    description=request.description,
                    start_date=request.start_date,
                    end_date=request.end_date,
                    created_at=request.created_at,
                    updated_at=request.updated_at,
                    archived_at=request.archived_at,
                    milestones=[to_project_milestone(item) for item in request.milestones],
                    activities=[to_project_activity(item) for item in request.activities],
                    assignments=[to_project_assignment(item) for item in request.assignments],
                    references=[to_external_reference(item) for item in request.references],
                )
                repository.add(project)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except ProjectError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create project failed") from exc

        return CreateProjectResponse(project=to_project_response(project))


def to_project_milestone(value: ProjectMilestoneInput) -> ProjectMilestone:
    create_kwargs: dict[str, object] = {}
    if value.milestone_id is not None:
        create_kwargs["id"] = value.milestone_id
    return ProjectMilestone(
        name=value.name,
        sequence=value.sequence,
        status=value.status,
        description=value.description,
        due_date=value.due_date,
        completed_date=value.completed_date,
        **create_kwargs,
    )


def to_project_activity(value: ProjectActivityInput) -> ProjectActivity:
    create_kwargs: dict[str, object] = {}
    if value.activity_id is not None:
        create_kwargs["id"] = value.activity_id
    return ProjectActivity(
        title=value.title,
        status=value.status,
        description=value.description,
        planned_start=value.planned_start,
        planned_finish=value.planned_finish,
        actual_start=value.actual_start,
        actual_finish=value.actual_finish,
        priority=ProjectPriority(value.priority.strip().upper()),
        estimated_hours=value.estimated_hours,
        actual_hours=value.actual_hours,
        **create_kwargs,
    )


def to_project_assignment(value: ProjectAssignmentInput) -> ProjectAssignment:
    create_kwargs: dict[str, object] = {}
    if value.assignment_id is not None:
        create_kwargs["id"] = value.assignment_id
    return ProjectAssignment(
        organisation_id=value.organisation_id,
        contact_id=value.contact_id,
        role=value.role,
        assigned_from=value.assigned_from,
        assigned_until=value.assigned_until,
        **create_kwargs,
    )


def to_external_reference(value: ExternalReferenceInput) -> ExternalReference:
    create_kwargs: dict[str, object] = {}
    if value.reference_id is not None:
        create_kwargs["id"] = value.reference_id
    if value.created_at is not None:
        create_kwargs["created_at"] = value.created_at
    return ExternalReference(
        reference_type=ReferenceType(value.reference_type.strip().upper()),
        external_id=value.external_id,
        description=value.description,
        **create_kwargs,
    )


def to_project_milestone_response(value: ProjectMilestone) -> ProjectMilestoneResponse:
    return ProjectMilestoneResponse(
        milestone_id=value.id,
        name=value.name,
        sequence=value.sequence,
        status=value.status,
        description=value.description,
        due_date=value.due_date,
        completed_date=value.completed_date,
    )


def to_project_activity_response(value: ProjectActivity) -> ProjectActivityResponse:
    return ProjectActivityResponse(
        activity_id=value.id,
        title=value.title,
        status=value.status,
        description=value.description,
        planned_start=value.planned_start,
        planned_finish=value.planned_finish,
        actual_start=value.actual_start,
        actual_finish=value.actual_finish,
        priority=value.priority.value,
        estimated_hours=value.estimated_hours,
        actual_hours=value.actual_hours,
    )


def to_project_assignment_response(value: ProjectAssignment) -> ProjectAssignmentResponse:
    return ProjectAssignmentResponse(
        assignment_id=value.id,
        organisation_id=value.organisation_id,
        contact_id=value.contact_id,
        role=value.role,
        assigned_from=value.assigned_from,
        assigned_until=value.assigned_until,
    )


def to_external_reference_response(value: ExternalReference) -> ExternalReferenceResponse:
    return ExternalReferenceResponse(
        reference_id=value.id,
        reference_type=value.reference_type.value,
        external_id=value.external_id,
        description=value.description,
        created_at=value.created_at,
    )


def to_project_response(value: Project) -> ProjectResponse:
    return ProjectResponse(
        project_id=value.id.value,
        project_number=value.project_number.value,
        project_name=value.project_name.value,
        status=value.status.value,
        priority=value.priority.value,
        description=value.description,
        start_date=value.start_date,
        end_date=value.end_date,
        created_at=value.created_at,
        updated_at=value.updated_at,
        archived_at=value.archived_at,
        version=value.version,
        milestones=tuple(
            to_project_milestone_response(item) for item in value.milestones
        ),
        activities=tuple(to_project_activity_response(item) for item in value.activities),
        assignments=tuple(
            to_project_assignment_response(item) for item in value.assignments
        ),
        references=tuple(to_external_reference_response(item) for item in value.references),
    )


def _as_string(value: Any) -> str:
    if hasattr(value, "value"):
        return str(value.value)
    return str(value)


def to_project_search_result_response(
    value: Mapping[str, Any],
) -> ProjectSearchResultResponse:
    return ProjectSearchResultResponse(
        project_id=UUID(str(value["id"])),
        project_number=str(value["project_number"]),
        project_name=str(value["project_name"]),
        status=_as_string(value["status"]),
        priority=_as_string(value["priority"]),
    )
