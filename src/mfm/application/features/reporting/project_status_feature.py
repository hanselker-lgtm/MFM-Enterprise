"""Feature API entry point for REP-003 project status reporting."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.reporting.models.project_status_dto import ProjectStatusDTO
from mfm.application.reporting.project_status_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.project_status_service import (
    ProjectStatusRequest as ServiceRequest,
)
from mfm.application.reporting.project_status_service import (
    ProjectStatusService as ReportingProjectStatusService,
)
from mfm.application.reporting.project_status_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.project_status_service import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when report business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository/persistence operations fail."""


@dataclass(frozen=True, slots=True)
class ProjectStatusRequest:
    project_id: UUID

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")


ProjectStatusService = ReportingProjectStatusService


class ProjectStatusFeature:
    """Feature facade for project status reporting."""

    def __init__(self, *, service: ReportingProjectStatusService) -> None:
        self._service = service

    def execute(self, request: ProjectStatusRequest) -> ProjectStatusDTO:
        request.validate()

        try:
            return self._service.execute(ServiceRequest(project_id=request.project_id))
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Project status feature failed") from exc


def project_status_dashboard(
    *,
    service: ReportingProjectStatusService,
    request: ProjectStatusRequest,
) -> ProjectStatusDTO:
    return ProjectStatusFeature(service=service).execute(request)