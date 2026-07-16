"""Create project feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import UUID

from mfm.application.projects.create_project import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.projects.create_project import (
    CreateProjectRequest as ServiceRequest,
)
from mfm.application.projects.create_project import (
    CreateProjectResponse as ServiceResponse,
)
from mfm.application.projects.create_project import (
    ExternalReferenceInput as ServiceExternalReferenceInput,
)
from mfm.application.projects.create_project import (
    ExternalReferenceResponse as ServiceExternalReferenceResponse,
)
from mfm.application.projects.create_project import (
    ProjectActivityInput as ServiceProjectActivityInput,
)
from mfm.application.projects.create_project import (
    ProjectActivityResponse as ServiceProjectActivityResponse,
)
from mfm.application.projects.create_project import (
    ProjectAssignmentInput as ServiceProjectAssignmentInput,
)
from mfm.application.projects.create_project import (
    ProjectAssignmentResponse as ServiceProjectAssignmentResponse,
)
from mfm.application.projects.create_project import (
    ProjectMilestoneInput as ServiceProjectMilestoneInput,
)
from mfm.application.projects.create_project import (
    ProjectMilestoneResponse as ServiceProjectMilestoneResponse,
)
from mfm.application.projects.create_project import (
    ProjectResponse as ServiceProjectResponse,
)
from mfm.application.projects.create_project import (
    ProjectSearchResultResponse as ServiceProjectSearchResultResponse,
)
from mfm.application.projects.create_project import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.projects.create_project import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for projects feature failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


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
            raise ValidationException(f"{field_name}.estimated_hours must not be bool/float")
        if self.actual_hours is not None and (
            isinstance(self.actual_hours, bool) or isinstance(self.actual_hours, float)
        ):
            raise ValidationException(f"{field_name}.actual_hours must not be bool/float")
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


class CreateProjectService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_service_project_milestone_input(value: ProjectMilestoneInput) -> ServiceProjectMilestoneInput:
    return ServiceProjectMilestoneInput(
        name=value.name,
        sequence=value.sequence,
        status=value.status,
        description=value.description,
        due_date=value.due_date,
        completed_date=value.completed_date,
        milestone_id=value.milestone_id,
    )


def to_service_project_activity_input(value: ProjectActivityInput) -> ServiceProjectActivityInput:
    return ServiceProjectActivityInput(
        title=value.title,
        status=value.status,
        description=value.description,
        planned_start=value.planned_start,
        planned_finish=value.planned_finish,
        actual_start=value.actual_start,
        actual_finish=value.actual_finish,
        priority=value.priority,
        estimated_hours=value.estimated_hours,
        actual_hours=value.actual_hours,
        activity_id=value.activity_id,
    )


def to_service_project_assignment_input(value: ProjectAssignmentInput) -> ServiceProjectAssignmentInput:
    return ServiceProjectAssignmentInput(
        organisation_id=value.organisation_id,
        contact_id=value.contact_id,
        role=value.role,
        assigned_from=value.assigned_from,
        assigned_until=value.assigned_until,
        assignment_id=value.assignment_id,
    )


def to_service_external_reference_input(value: ExternalReferenceInput) -> ServiceExternalReferenceInput:
    return ServiceExternalReferenceInput(
        reference_type=value.reference_type,
        external_id=value.external_id,
        description=value.description,
        created_at=value.created_at,
        reference_id=value.reference_id,
    )


def to_feature_project_milestone_response(
    response: ServiceProjectMilestoneResponse,
) -> ProjectMilestoneResponse:
    return ProjectMilestoneResponse(
        milestone_id=response.milestone_id,
        name=response.name,
        sequence=response.sequence,
        status=response.status,
        description=response.description,
        due_date=response.due_date,
        completed_date=response.completed_date,
    )


def to_feature_project_activity_response(
    response: ServiceProjectActivityResponse,
) -> ProjectActivityResponse:
    return ProjectActivityResponse(
        activity_id=response.activity_id,
        title=response.title,
        status=response.status,
        description=response.description,
        planned_start=response.planned_start,
        planned_finish=response.planned_finish,
        actual_start=response.actual_start,
        actual_finish=response.actual_finish,
        priority=response.priority,
        estimated_hours=response.estimated_hours,
        actual_hours=response.actual_hours,
    )


def to_feature_project_assignment_response(
    response: ServiceProjectAssignmentResponse,
) -> ProjectAssignmentResponse:
    return ProjectAssignmentResponse(
        assignment_id=response.assignment_id,
        organisation_id=response.organisation_id,
        contact_id=response.contact_id,
        role=response.role,
        assigned_from=response.assigned_from,
        assigned_until=response.assigned_until,
    )


def to_feature_external_reference_response(
    response: ServiceExternalReferenceResponse,
) -> ExternalReferenceResponse:
    return ExternalReferenceResponse(
        reference_id=response.reference_id,
        reference_type=response.reference_type,
        external_id=response.external_id,
        description=response.description,
        created_at=response.created_at,
    )


def to_feature_project_response(response: ServiceProjectResponse) -> ProjectResponse:
    return ProjectResponse(
        project_id=response.project_id,
        project_number=response.project_number,
        project_name=response.project_name,
        status=response.status,
        priority=response.priority,
        description=response.description,
        start_date=response.start_date,
        end_date=response.end_date,
        created_at=response.created_at,
        updated_at=response.updated_at,
        archived_at=response.archived_at,
        version=response.version,
        milestones=tuple(
            to_feature_project_milestone_response(item)
            for item in response.milestones
        ),
        activities=tuple(
            to_feature_project_activity_response(item)
            for item in response.activities
        ),
        assignments=tuple(
            to_feature_project_assignment_response(item)
            for item in response.assignments
        ),
        references=tuple(
            to_feature_external_reference_response(item)
            for item in response.references
        ),
    )


def to_feature_project_search_result_response(
    response: ServiceProjectSearchResultResponse,
) -> ProjectSearchResultResponse:
    return ProjectSearchResultResponse(
        project_id=response.project_id,
        project_number=response.project_number,
        project_name=response.project_name,
        status=response.status,
        priority=response.priority,
    )


class CreateProjectFeature:
    """Feature facade for project creation."""

    def __init__(self, *, service: CreateProjectService) -> None:
        self._service = service

    def execute(self, request: CreateProjectRequest) -> CreateProjectResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    project_number=request.project_number,
                    project_name=request.project_name,
                    project_id=request.project_id,
                    status=request.status,
                    priority=request.priority,
                    description=request.description,
                    start_date=request.start_date,
                    end_date=request.end_date,
                    created_at=request.created_at,
                    updated_at=request.updated_at,
                    archived_at=request.archived_at,
                    milestones=tuple(
                        to_service_project_milestone_input(item)
                        for item in request.milestones
                    ),
                    activities=tuple(
                        to_service_project_activity_input(item)
                        for item in request.activities
                    ),
                    assignments=tuple(
                        to_service_project_assignment_input(item)
                        for item in request.assignments
                    ),
                    references=tuple(
                        to_service_external_reference_input(item)
                        for item in request.references
                    ),
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create project feature failed") from exc

        return CreateProjectResponse(
            project=to_feature_project_response(service_response.project)
        )
