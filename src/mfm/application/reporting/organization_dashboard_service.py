"""Application reporting service for REP-001 organization dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import Protocol
from uuid import UUID

from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import SearchJournalsRequest
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.projects import ListProjectsRequest
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardAccountingDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardDocumentsDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardHealthIndicatorsDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardOperationsDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardOrganizationDTO,
)
from mfm.application.reporting.models.organization_dashboard_dto import (
    OrganizationDashboardProjectsDTO,
)


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when dashboard request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when dependent feature APIs fail."""


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


class ListProjectsFeaturePort(Protocol):
    def execute(self, request: ListProjectsRequest): ...


class ListDocumentsFeaturePort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class SearchJournalsFeaturePort(Protocol):
    def execute(self, request: SearchJournalsRequest): ...


class ListFiscalYearsFeaturePort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class OrganizationDashboardService:
    """Compose the organization dashboard from existing feature APIs only."""

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

    def execute(self, request: OrganizationDashboardRequest) -> OrganizationDashboardDTO:
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
        organization_project_ids = {project.project_id for project in organization_projects}

        active_projects = sum(
            1 for project in organization_projects if str(project.status).upper() == "ACTIVE"
        )
        closed_projects = sum(
            1 for project in organization_projects if str(project.status).upper() == "COMPLETED"
        )
        archived_projects = sum(
            1 for project in organization_projects if str(project.status).upper() == "ARCHIVED"
        )

        project_documents = tuple(
            document
            for document in documents
            if any(
                reference.target_capability == "PROJECTS"
                and reference.target_aggregate_type == "PROJECT"
                and self._parse_uuid(reference.target_aggregate_id) in organization_project_ids
                for reference in document.references
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
            1 for fiscal_year in fiscal_years if str(fiscal_year.status).upper() == "OPEN"
        )
        closed_fiscal_years = sum(
            1 for fiscal_year in fiscal_years if str(fiscal_year.status).upper() == "CLOSED"
        )

        last_accounting_activity = (
            max(journal.posting_date for journal in organization_journals)
            if organization_journals
            else None
        )
        last_document_activity = (
            max((document.updated_at or document.created_at) for document in project_documents)
            if project_documents
            else None
        )

        last_posted = [
            journal
            for journal in organization_journals
            if str(journal.status).upper() == "POSTED"
        ]
        last_posted_journal = (
            max(last_posted, key=lambda item: item.posting_date).journal_number
            if last_posted
            else None
        )

        now_utc = datetime.now(UTC)
        thirty_days_ago = now_utc - timedelta(days=30)
        documents_added_last_30_days = sum(
            1
            for document in project_documents
            if (document.created_at >= thirty_days_ago)
        )

        projects_with_budget_ready = sum(
            1
            for project in organization_projects
            if any(
                reference.reference_type == "DOCUMENT"
                and (reference.description or "").strip().upper() == "BUDGET_STATUS:READY"
                for reference in project.references
            )
        )
        budget_coverage = (
            round(projects_with_budget_ready / active_projects, 4)
            if active_projects > 0
            else 0.0
        )

        accounting_status = self._derive_accounting_status(
            journal_count=len(organization_journals),
            open_fiscal_years=open_fiscal_years,
            closed_fiscal_years=closed_fiscal_years,
            has_unposted=any(str(journal.status).upper() != "POSTED" for journal in organization_journals),
        )
        documentation_status = self._derive_documentation_status(
            total_documents=len(project_documents),
            active_projects=active_projects,
        )
        archive_status = self._derive_archive_status(
            archived_projects=archived_projects,
            closed_projects=closed_projects,
            total_projects=len(organization_projects),
        )

        return OrganizationDashboardDTO(
            organization=OrganizationDashboardOrganizationDTO(
                organization_id=request.organization_id,
                name=(
                    None
                    if request.organization_name is None
                    else request.organization_name.strip()
                ),
                status=(
                    None
                    if request.organization_status is None
                    else request.organization_status.strip().upper()
                ),
            ),
            projects=OrganizationDashboardProjectsDTO(
                active_projects=active_projects,
                closed_projects=closed_projects,
                archived_projects=archived_projects,
                total_projects=len(organization_projects),
            ),
            documents=OrganizationDashboardDocumentsDTO(
                total_documents=len(project_documents),
                documents_added_last_30_days=documents_added_last_30_days,
            ),
            accounting=OrganizationDashboardAccountingDTO(
                journal_count=len(organization_journals),
                last_posted_journal=last_posted_journal,
                open_fiscal_years=open_fiscal_years,
                closed_fiscal_years=closed_fiscal_years,
            ),
            operations=OrganizationDashboardOperationsDTO(
                last_accounting_activity=last_accounting_activity,
                last_document_activity=last_document_activity,
            ),
            health_indicators=OrganizationDashboardHealthIndicatorsDTO(
                budget_coverage=budget_coverage,
                accounting_status=accounting_status,
                documentation_status=documentation_status,
                archive_status=archive_status,
            ),
        )

    @staticmethod
    def _derive_accounting_status(
        *,
        journal_count: int,
        open_fiscal_years: int,
        closed_fiscal_years: int,
        has_unposted: bool,
    ) -> str:
        if journal_count == 0:
            return "NO_ACTIVITY"
        if open_fiscal_years == 0 and closed_fiscal_years > 0:
            return "PERIOD_CLOSED"
        if has_unposted:
            return "AT_RISK"
        return "HEALTHY"

    @staticmethod
    def _derive_documentation_status(*, total_documents: int, active_projects: int) -> str:
        if active_projects == 0:
            return "NO_ACTIVE_PROJECTS"
        if total_documents == 0:
            return "MISSING"
        if total_documents < active_projects:
            return "PARTIAL"
        return "COMPLETE"

    @staticmethod
    def _derive_archive_status(
        *,
        archived_projects: int,
        closed_projects: int,
        total_projects: int,
    ) -> str:
        if total_projects == 0:
            return "NO_PROJECTS"
        if closed_projects == 0:
            return "NOT_READY"
        if archived_projects >= closed_projects:
            return "ON_TRACK"
        return "PENDING"

    @staticmethod
    def _project_belongs_to_organization(*, project, organization_id: UUID) -> bool:
        has_assignment = any(
            assignment.organisation_id == organization_id
            for assignment in project.assignments
        )
        has_reference = any(
            reference.reference_type == "ORGANISATION"
            and reference.external_id == organization_id
            for reference in project.references
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
