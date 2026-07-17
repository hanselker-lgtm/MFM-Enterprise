"""Feature API entry point for organization dashboard reporting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardDTO,
)
from mfm.application.reporting.organization_dashboard_service import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reporting.organization_dashboard_service import (
    OrganizationDashboardRequest as ServiceRequest,
)
from mfm.application.reporting.organization_dashboard_service import (
    OrganizationDashboardService as ReportingOrganizationDashboardService,
)
from mfm.application.reporting.organization_dashboard_service import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reporting.organization_dashboard_service import (
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
class OrganizationDashboardRequest:
    organization_id: UUID
    organization_name: str | None = None
    organization_status: str | None = None
    period_start: date | None = None
    period_end: date | None = None

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        for field_name, value in (
            ("organization_name", self.organization_name),
            ("organization_status", self.organization_status),
        ):
            if value is None:
                continue
            if not isinstance(value, str) or not value.strip():
                raise ValidationException(f"{field_name} must be a non-empty string when provided")
        if self.period_start is not None and not isinstance(self.period_start, date):
            raise ValidationException("period_start must be date or None")
        if self.period_end is not None and not isinstance(self.period_end, date):
            raise ValidationException("period_end must be date or None")
        if self.period_start is not None and self.period_end is not None and self.period_start > self.period_end:
            raise ValidationException("period_start must be on or before period_end")


OrganizationDashboardService = ReportingOrganizationDashboardService


class OrganizationDashboardFeature:
    """Feature facade for organization dashboard reporting."""

    def __init__(self, *, service: ReportingOrganizationDashboardService) -> None:
        self._service = service

    def execute(self, request: OrganizationDashboardRequest) -> OrganizationDashboardDTO:
        request.validate()

        try:
            return self._service.execute(
                ServiceRequest(
                    organization_id=request.organization_id,
                    organization_name=request.organization_name,
                    organization_status=request.organization_status,
                    period_start=request.period_start,
                    period_end=request.period_end,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except ServiceApplicationException as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Organization dashboard feature failed") from exc


def organization_dashboard(
    *,
    service: ReportingOrganizationDashboardService,
    request: OrganizationDashboardRequest,
) -> OrganizationDashboardDTO:
    return OrganizationDashboardFeature(service=service).execute(request)
