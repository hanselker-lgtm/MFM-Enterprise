"""Organization dashboard reporting service."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import SearchJournalsRequest
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.projects import ListProjectsRequest


class ApplicationException(Exception):
    """Base exception for report failures."""


class ValidationException(ApplicationException):
    """Raised when report request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when report business constraints are violated."""


class RepositoryException(ApplicationException):
    """Raised when dependent feature APIs fail."""


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
class OrganizationDashboardReportRequest:
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
class OrganizationDashboardReportResponse:
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


class ListProjectsFeaturePort(Protocol):
    def execute(self, request: ListProjectsRequest): ...


class ListDocumentsFeaturePort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class SearchJournalsFeaturePort(Protocol):
    def execute(self, request: SearchJournalsRequest): ...


class ListFiscalYearsFeaturePort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class OrganizationDashboardReportService:
    """Composes organization dashboard metrics from existing feature APIs."""

    def __init__(
        self,
        *,
        list_projects_feature: ListProjectsFeaturePort,
        list_documents_feature: ListDocumentsFeaturePort,
        search_journals_feature: SearchJournalsFeaturePort,
        list_fiscal_years_feature: ListFiscalYearsFeaturePort,
    ) -> None:
        self._list_projects = list_projects_feature
        self._list_documents = list_documents_feature
        self._search_journals = search_journals_feature
        self._list_fiscal_years = list_fiscal_years_feature

    def execute(
        self,
        request: OrganizationDashboardReportRequest,
    ) -> OrganizationDashboardReportResponse:
        request.validate()

        try:
            projects = self._list_projects.execute(ListProjectsRequest()).projects
            documents = self._list_documents.execute(ListDocumentsRequest()).documents
            journals = self._search_journals.execute(SearchJournalsRequest()).journals
            fiscal_years = self._list_fiscal_years.execute(ListFiscalYearsRequest()).fiscal_years
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Organization dashboard data retrieval failed") from exc

        organization_projects = tuple(
            project
            for project in projects
            if self._project_belongs_to_organization(
                project=project,
                organization_id=request.organization_id,
            )
        )
        organization_project_ids = {item.project_id for item in organization_projects}

        active_projects = sum(
            1 for item in organization_projects if str(item.status).upper() == "ACTIVE"
        )
        closed_projects = sum(
            1
            for item in organization_projects
            if str(item.status).upper() == "COMPLETED"
            or any(
                ref.reference_type == "DOCUMENT"
                and (ref.description or "").strip().upper() == "PROJECT_CLOSURE_STATUS:CLOSED"
                for ref in item.references
            )
        )
        archived_projects = sum(
            1 for item in organization_projects if str(item.status).upper() == "ARCHIVED"
        )

        project_documents = tuple(
            document
            for document in documents
            if any(
                ref.target_capability == "PROJECTS"
                and ref.target_aggregate_type == "PROJECT"
                and self._parse_uuid(ref.target_aggregate_id) in organization_project_ids
                for ref in document.references
            )
            and self._is_in_period(
                value=(document.updated_at or document.created_at),
                period_start=request.period_start,
                period_end=request.period_end,
            )
        )

        organization_journals = tuple(
            journal
            for journal in journals
            if journal.reference is not None
            and any(str(project_id) in journal.reference for project_id in organization_project_ids)
            and self._is_in_period(
                value=journal.posting_date,
                period_start=request.period_start,
                period_end=request.period_end,
            )
        )

        open_fiscal_years = sum(
            1
            for item in fiscal_years
            if str(item.status).upper() == "OPEN"
        )

        last_accounting_activity = (
            max(item.posting_date for item in organization_journals)
            if organization_journals
            else None
        )

        last_document_activity = (
            max((item.updated_at or item.created_at) for item in project_documents)
            if project_documents
            else None
        )

        healthy_projects = 0
        at_risk_projects = 0
        projects_with_budget_ready = 0
        projects_with_unposted_journals = 0

        for project in organization_projects:
            if str(project.status).upper() != "ACTIVE":
                continue

            project_journals = tuple(
                journal
                for journal in organization_journals
                if journal.reference is not None and str(project.project_id) in journal.reference
            )
            has_unposted = any(str(item.status).upper() != "POSTED" for item in project_journals)
            has_budget_ready = any(
                ref.reference_type == "DOCUMENT"
                and (ref.description or "").strip().upper() == "BUDGET_STATUS:READY"
                for ref in project.references
            )

            if has_budget_ready:
                projects_with_budget_ready += 1
            if has_unposted:
                projects_with_unposted_journals += 1

            if has_budget_ready and not has_unposted:
                healthy_projects += 1
            else:
                at_risk_projects += 1

        if active_projects == 0:
            overall_health_status = "NO_ACTIVE_PROJECTS"
        elif at_risk_projects == 0:
            overall_health_status = "HEALTHY"
        elif healthy_projects == 0:
            overall_health_status = "CRITICAL"
        else:
            overall_health_status = "AT_RISK"

        return OrganizationDashboardReportResponse(
            organization=OrganizationInfoView(
                organization_id=request.organization_id,
                organization_number=(
                    None
                    if request.organization_number is None
                    else request.organization_number.strip()
                ),
                organization_name=(
                    None
                    if request.organization_name is None
                    else request.organization_name.strip()
                ),
                organization_type=(
                    None
                    if request.organization_type is None
                    else request.organization_type.strip().upper()
                ),
                organization_status=(
                    None
                    if request.organization_status is None
                    else request.organization_status.strip().upper()
                ),
            ),
            active_projects=active_projects,
            closed_projects=closed_projects,
            archived_projects=archived_projects,
            project_documents=len(project_documents),
            accounting_journals=len(organization_journals),
            open_fiscal_years=open_fiscal_years,
            last_accounting_activity=last_accounting_activity,
            last_document_activity=last_document_activity,
            health_indicators=OrganizationHealthIndicatorsView(
                healthy_projects=healthy_projects,
                at_risk_projects=at_risk_projects,
                projects_with_budget_ready=projects_with_budget_ready,
                projects_with_unposted_journals=projects_with_unposted_journals,
                overall_health_status=overall_health_status,
            ),
        )

    @staticmethod
    def _project_belongs_to_organization(*, project, organization_id: UUID) -> bool:
        has_assignment = any(
            assignment.organisation_id == organization_id
            for assignment in project.assignments
        )
        has_reference = any(
            ref.reference_type == "ORGANISATION"
            and ref.external_id == organization_id
            for ref in project.references
        )
        return has_assignment or has_reference

    @staticmethod
    def _is_in_period(
        *,
        value: date | datetime,
        period_start: date | None,
        period_end: date | None,
    ) -> bool:
        compare_date = value.date() if isinstance(value, datetime) else value
        if period_start is not None and compare_date < period_start:
            return False
        if period_end is not None and compare_date > period_end:
            return False
        return True

    @staticmethod
    def _parse_uuid(value: str) -> UUID | None:
        try:
            return UUID(value)
        except Exception:
            return None
