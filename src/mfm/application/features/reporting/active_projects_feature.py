"""Feature API entry point for REP-002 active projects dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.application.reporting.models.active_projects_dto import (
    ActiveProjectsDashboardResponse,
)
from mfm.application.reporting.active_projects_service import (
    ActiveProjectsDashboardRequest as ServiceRequest,
)
from mfm.application.reporting.active_projects_service import (
    ActiveProjectsService as ReportingActiveProjectsService,
)
from mfm.application.reporting.active_projects_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.active_projects_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.active_projects_service import (
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
class ActiveProjectsDashboardRequest:
    organization_id: UUID

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")


ActiveProjectsService = ReportingActiveProjectsService


class ActiveProjectsFeature:
    """Feature facade for active projects dashboard reporting."""

    def __init__(self, *, service: ReportingActiveProjectsService) -> None:
        self._service = service

    def execute(self, request: ActiveProjectsDashboardRequest) -> ActiveProjectsDashboardResponse:
        request.validate()

        try:
            return self._service.execute(
                ServiceRequest(organization_id=request.organization_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Active projects feature failed") from exc


def active_projects_dashboard(
    *,
    service: ReportingActiveProjectsService,
    request: ActiveProjectsDashboardRequest,
) -> ActiveProjectsDashboardResponse:
    return ActiveProjectsFeature(service=service).execute(request)
