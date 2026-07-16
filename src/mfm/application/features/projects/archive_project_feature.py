"""Archive project feature facade following Public API Standard."""

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
from mfm.application.projects.archive_project import ArchiveProjectRequest as ServiceRequest
from mfm.application.projects.archive_project import ArchiveProjectResponse as ServiceResponse
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
class ArchiveProjectRequest:
    project_id: UUID
    archived_at: datetime

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")
        if not isinstance(self.archived_at, datetime):
            raise ValidationException("archived_at must be datetime")


@dataclass(frozen=True, slots=True)
class ArchiveProjectResponse:
    project: ProjectResponse


class ArchiveProjectService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ArchiveProjectFeature:
    """Feature facade for project archiving."""

    def __init__(self, *, service: ArchiveProjectService) -> None:
        self._service = service

    def execute(self, request: ArchiveProjectRequest) -> ArchiveProjectResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    project_id=request.project_id,
                    archived_at=request.archived_at,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Archive project feature failed") from exc

        return ArchiveProjectResponse(
            project=to_feature_project_response(service_response.project)
        )
