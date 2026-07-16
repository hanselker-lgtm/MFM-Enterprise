"""Update project feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.projects.create_project_feature import (
    BusinessRuleViolation,
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
    ProjectResponse,
)
from mfm.application.features.projects.create_project_feature import (
    RepositoryException,
)
from mfm.application.features.projects.create_project_feature import (
    ValidationException,
)
from mfm.application.features.projects.create_project_feature import (
    to_feature_project_response,
)
from mfm.application.features.projects.create_project_feature import (
    to_service_external_reference_input,
)
from mfm.application.features.projects.create_project_feature import (
    to_service_project_activity_input,
)
from mfm.application.features.projects.create_project_feature import (
    to_service_project_assignment_input,
)
from mfm.application.features.projects.create_project_feature import (
    to_service_project_milestone_input,
)
from mfm.application.projects.create_project import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.projects.create_project import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.projects.create_project import (
    ValidationException as ServiceValidationException,
)
from mfm.application.projects.update_project import UpdateProjectRequest as ServiceRequest
from mfm.application.projects.update_project import UpdateProjectResponse as ServiceResponse


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


class UpdateProjectService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateProjectFeature:
    """Feature facade for project updates."""

    def __init__(self, *, service: UpdateProjectService) -> None:
        self._service = service

    def execute(self, request: UpdateProjectRequest) -> UpdateProjectResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    project_id=request.project_id,
                    project_name=request.project_name,
                    description=request.description,
                    priority=request.priority,
                    start_date=request.start_date,
                    end_date=request.end_date,
                    updated_at=request.updated_at,
                    milestones=(
                        None
                        if request.milestones is None
                        else tuple(
                            to_service_project_milestone_input(item)
                            for item in request.milestones
                        )
                    ),
                    activities=(
                        None
                        if request.activities is None
                        else tuple(
                            to_service_project_activity_input(item)
                            for item in request.activities
                        )
                    ),
                    assignments=(
                        None
                        if request.assignments is None
                        else tuple(
                            to_service_project_assignment_input(item)
                            for item in request.assignments
                        )
                    ),
                    references=(
                        None
                        if request.references is None
                        else tuple(
                            to_service_external_reference_input(item)
                            for item in request.references
                        )
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
            raise RepositoryException("Update project feature failed") from exc

        return UpdateProjectResponse(
            project=to_feature_project_response(service_response.project)
        )
