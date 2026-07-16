"""Get project feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
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
from mfm.application.projects.create_project import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.projects.create_project import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.projects.create_project import (
    ValidationException as ServiceValidationException,
)
from mfm.application.projects.get_project import GetProjectRequest as ServiceRequest
from mfm.application.projects.get_project import GetProjectResponse as ServiceResponse


@dataclass(frozen=True, slots=True)
class GetProjectRequest:
    project_id: UUID

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetProjectResponse:
    project: ProjectResponse


class GetProjectService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetProjectFeature:
    """Feature facade for project retrieval."""

    def __init__(self, *, service: GetProjectService) -> None:
        self._service = service

    def execute(self, request: GetProjectRequest) -> GetProjectResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(project_id=request.project_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get project feature failed") from exc

        return GetProjectResponse(
            project=to_feature_project_response(service_response.project)
        )
