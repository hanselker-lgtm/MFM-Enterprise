"""Feature API for Organization & Roles summary reporting."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.reporting.models.organization_roles_summary_dto import (
    OrganizationRolesSummaryResponse,
)
from mfm.application.reporting.organization_roles_summary_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.organization_roles_summary_service import (
    OrganizationRolesSummaryRequest as ServiceRequest,
)
from mfm.application.reporting.organization_roles_summary_service import (
    OrganizationRolesSummaryService as ReportingOrganizationRolesSummaryService,
)
from mfm.application.reporting.organization_roles_summary_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.organization_roles_summary_service import (
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
class OrganizationRolesSummaryRequest:
    organization_id: UUID

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")


OrganizationRolesSummaryService = ReportingOrganizationRolesSummaryService


class OrganizationRolesSummaryServicePort(Protocol):
    def execute(self, request: ServiceRequest) -> OrganizationRolesSummaryResponse: ...


class OrganizationRolesSummaryFeature:
    """Feature facade for Organization & Roles summary reporting."""

    def __init__(self, *, service: OrganizationRolesSummaryServicePort) -> None:
        self._service = service

    def execute(self, request: OrganizationRolesSummaryRequest) -> OrganizationRolesSummaryResponse:
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
            raise RepositoryException("Organization roles summary feature failed") from exc
