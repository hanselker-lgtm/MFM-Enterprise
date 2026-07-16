"""Complete project feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.projects.create_project_feature import (
    BusinessRuleViolation,
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
from mfm.application.projects.complete_project import CompleteProjectRequest as ServiceRequest
from mfm.application.projects.complete_project import CompleteProjectResponse as ServiceResponse
from mfm.application.projects.create_project import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.projects.create_project import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.projects.create_project import (
    ValidationException as ServiceValidationException,
)


@dataclass(frozen=True, slots=True)
class CompleteProjectRequest:
    project_id: UUID
    completed_at: datetime

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")
        if not isinstance(self.completed_at, datetime):
            raise ValidationException("completed_at must be datetime")


@dataclass(frozen=True, slots=True)
class CompleteProjectResponse:
    project: ProjectResponse


class CompleteProjectService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CompleteProjectFeature:
    """Feature facade for project completion."""

    def __init__(self, *, service: CompleteProjectService) -> None:
        self._service = service

    def execute(self, request: CompleteProjectRequest) -> CompleteProjectResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    project_id=request.project_id,
                    completed_at=request.completed_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Complete project feature failed") from exc

        return CompleteProjectResponse(
            project=to_feature_project_response(service_response.project)
        )
