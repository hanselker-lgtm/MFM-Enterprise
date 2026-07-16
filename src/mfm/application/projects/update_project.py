"""Update Project use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.projects.create_project import ApplicationException
from mfm.application.projects.create_project import BusinessRuleViolation
from mfm.application.projects.create_project import ExternalReferenceInput
from mfm.application.projects.create_project import ProjectActivityInput
from mfm.application.projects.create_project import ProjectAssignmentInput
from mfm.application.projects.create_project import ProjectMilestoneInput
from mfm.application.projects.create_project import ProjectResponse
from mfm.application.projects.create_project import RepositoryException
from mfm.application.projects.create_project import ValidationException
from mfm.application.projects.create_project import to_external_reference
from mfm.application.projects.create_project import to_project_activity
from mfm.application.projects.create_project import to_project_assignment
from mfm.application.projects.create_project import to_project_milestone
from mfm.application.projects.create_project import to_project_response
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.projects.exceptions import ProjectError
from mfm.domain.projects.project_id import ProjectId
from mfm.domain.projects.project_name import ProjectName
from mfm.domain.projects.project_priority import ProjectPriority
from mfm.domain.projects.project_repository import ProjectRepository


@dataclass(frozen=True, slots=True)
class UpdateProjectRequest:
    project_id: UUID
    project_name: str | None = None
    description: str | None = None
    priority: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None
    updated_at: datetime | None = None
    milestones: tuple[ProjectMilestoneInput, ...] | None = None
    activities: tuple[ProjectActivityInput, ...] | None = None
    assignments: tuple[ProjectAssignmentInput, ...] | None = None
    references: tuple[ExternalReferenceInput, ...] | None = None

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")
        if self.project_name is not None and (
            not isinstance(self.project_name, str) or not self.project_name.strip()
        ):
            raise ValidationException("project_name must be a non-empty string or None")
        if self.description is not None and not isinstance(self.description, str):
            raise ValidationException("description must be string or None")
        if self.priority is not None and (
            not isinstance(self.priority, str) or not self.priority.strip()
        ):
            raise ValidationException("priority must be a non-empty string or None")
        if self.start_date is not None and not isinstance(self.start_date, datetime):
            raise ValidationException("start_date must be datetime or None")
        if self.end_date is not None and not isinstance(self.end_date, datetime):
            raise ValidationException("end_date must be datetime or None")
        if self.updated_at is not None and not isinstance(self.updated_at, datetime):
            raise ValidationException("updated_at must be datetime or None")
        if self.milestones is not None and not isinstance(self.milestones, tuple):
            raise ValidationException("milestones must be tuple or None")
        if self.activities is not None and not isinstance(self.activities, tuple):
            raise ValidationException("activities must be tuple or None")
        if self.assignments is not None and not isinstance(self.assignments, tuple):
            raise ValidationException("assignments must be tuple or None")
        if self.references is not None and not isinstance(self.references, tuple):
            raise ValidationException("references must be tuple or None")

        for field_name, values in (
            ("milestones", self.milestones),
            ("activities", self.activities),
            ("assignments", self.assignments),
            ("references", self.references),
        ):
            if values is None:
                continue
            for index, value in enumerate(values):
                value.validate(field_name=f"{field_name}[{index}]")


@dataclass(frozen=True, slots=True)
class UpdateProjectResponse:
    project: ProjectResponse


class UpdateProjectUseCase:
    """Update mutable project details and child collections."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: UpdateProjectRequest) -> UpdateProjectResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: ProjectRepository = uow.project_repository
                project = repository.get(ProjectId(request.project_id))
                if project is None:
                    raise BusinessRuleViolation(
                        f"Project {request.project_id} does not exist"
                    )

                project.update_details(
                    project_name=(
                        ProjectName(request.project_name)
                        if request.project_name is not None
                        else None
                    ),
                    description=request.description,
                    priority=(
                        ProjectPriority(request.priority.strip().upper())
                        if request.priority is not None
                        else None
                    ),
                    start_date=request.start_date,
                    end_date=request.end_date,
                    updated_at=request.updated_at,
                )

                if request.milestones is not None:
                    project.milestones = [
                        to_project_milestone(item) for item in request.milestones
                    ]
                if request.activities is not None:
                    project.activities = [
                        to_project_activity(item) for item in request.activities
                    ]
                if request.assignments is not None:
                    project.assignments = [
                        to_project_assignment(item) for item in request.assignments
                    ]
                if request.references is not None:
                    project.references = [
                        to_external_reference(item) for item in request.references
                    ]

                repository.update(project)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except ProjectError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update project failed") from exc

        return UpdateProjectResponse(project=to_project_response(project))
