"""Feature API entry point for organization dashboard reporting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.reports.organization_dashboard_report import (
    ApplicationException as ServiceApplicationException,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationDashboardReportRequest as ServiceRequest,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationDashboardReportResponse as ServiceResponse,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationDashboardReportService,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationHealthIndicatorsView as ServiceHealthIndicatorsView,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationInfoView as ServiceOrganizationInfoView,
)
from mfm.application.reports.organization_dashboard_report import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.reports.organization_dashboard_report import (
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
class OrganizationInfoView:
    organization_id: UUID
    organization_number: str | None
    organization_name: str | None
    organization_type: str | None
    organization_status: str | None


@dataclass(frozen=True, slots=True)
class OrganizationHealthIndicatorsView:
    healthy_projects: int
    at_risk_projects: int
    projects_with_budget_ready: int
    projects_with_unposted_journals: int
    overall_health_status: str


@dataclass(frozen=True, slots=True)
class OrganizationDashboardRequest:
    organization_id: UUID
    organization_number: str | None = None
    organization_name: str | None = None
    organization_type: str | None = None
    organization_status: str | None = None
    period_start: date | None = None
    period_end: date | None = None

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")
        for field_name, value in (
            ("organization_number", self.organization_number),
            ("organization_name", self.organization_name),
            ("organization_type", self.organization_type),
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


@dataclass(frozen=True, slots=True)
class OrganizationDashboardResponse:
    organization: OrganizationInfoView
    active_projects: int
    closed_projects: int
    archived_projects: int
    project_documents: int
    accounting_journals: int
    open_fiscal_years: int
    last_accounting_activity: date | None
    last_document_activity: datetime | None
    health_indicators: OrganizationHealthIndicatorsView


class OrganizationDashboardService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def _to_feature_organization_info(value: ServiceOrganizationInfoView) -> OrganizationInfoView:
    return OrganizationInfoView(
        organization_id=value.organization_id,
        organization_number=value.organization_number,
        organization_name=value.organization_name,
        organization_type=value.organization_type,
        organization_status=value.organization_status,
    )


def _to_feature_health_indicators(
    value: ServiceHealthIndicatorsView,
) -> OrganizationHealthIndicatorsView:
    return OrganizationHealthIndicatorsView(
        healthy_projects=value.healthy_projects,
        at_risk_projects=value.at_risk_projects,
        projects_with_budget_ready=value.projects_with_budget_ready,
        projects_with_unposted_journals=value.projects_with_unposted_journals,
        overall_health_status=value.overall_health_status,
    )


class OrganizationDashboardFeature:
    """Feature facade for organization dashboard reporting."""

    def __init__(self, *, service: OrganizationDashboardService) -> None:
        self._service = service

    def execute(self, request: OrganizationDashboardRequest) -> OrganizationDashboardResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    organization_id=request.organization_id,
                    organization_number=request.organization_number,
                    organization_name=request.organization_name,
                    organization_type=request.organization_type,
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

        return OrganizationDashboardResponse(
            organization=_to_feature_organization_info(service_response.organization),
            active_projects=service_response.active_projects,
            closed_projects=service_response.closed_projects,
            archived_projects=service_response.archived_projects,
            project_documents=service_response.project_documents,
            accounting_journals=service_response.accounting_journals,
            open_fiscal_years=service_response.open_fiscal_years,
            last_accounting_activity=service_response.last_accounting_activity,
            last_document_activity=service_response.last_document_activity,
            health_indicators=_to_feature_health_indicators(service_response.health_indicators),
        )


def organization_dashboard(
    *,
    service: OrganizationDashboardReportService,
    request: OrganizationDashboardRequest,
) -> OrganizationDashboardResponse:
    return OrganizationDashboardFeature(service=service).execute(request)
