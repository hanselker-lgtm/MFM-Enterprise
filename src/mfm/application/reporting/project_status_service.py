"""Application reporting service for REP-003 project status dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.accounting import ListFiscalYearsRequest
from mfm.application.features.accounting import SearchJournalsRequest
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.projects import GetProjectRequest
from mfm.application.reporting.models.project_status_dto import (
    ProjectStatusAccountingResponse,
)
from mfm.application.reporting.models.project_status_dto import ProjectStatusArchiveResponse
from mfm.application.reporting.models.project_status_dto import ProjectStatusBudgetResponse
from mfm.application.reporting.models.project_status_dto import (
    ProjectStatusDTO,
)
from mfm.application.reporting.models.project_status_dto import (
    ProjectStatusDocumentsResponse,
)
from mfm.application.reporting.models.project_status_dto import ProjectStatusHealthResponse
from mfm.application.reporting.models.project_status_dto import (
    ProjectStatusOrganizationResponse,
)
from mfm.application.reporting.models.project_status_dto import (
    ProjectStatusProjectResponse,
)


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when dashboard request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when dependent feature APIs fail."""


@dataclass(frozen=True, slots=True)
class ProjectStatusRequest:
    project_id: UUID

    def validate(self) -> None:
        if not isinstance(self.project_id, UUID):
            raise ValidationException("project_id must be UUID")


class GetProjectFeaturePort(Protocol):
    def execute(self, request: GetProjectRequest): ...


class ListDocumentsFeaturePort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class SearchJournalsFeaturePort(Protocol):
    def execute(self, request: SearchJournalsRequest): ...


class ListFiscalYearsFeaturePort(Protocol):
    def execute(self, request: ListFiscalYearsRequest): ...


class ProjectStatusService:
    """Compose a single-project operational view from existing feature APIs only."""

    def __init__(
        self,
        *,
        get_project_feature: GetProjectFeaturePort,
        list_documents_feature: ListDocumentsFeaturePort,
        search_journals_feature: SearchJournalsFeaturePort,
        list_fiscal_years_feature: ListFiscalYearsFeaturePort,
    ) -> None:
        self._get_project = get_project_feature
        self._list_documents = list_documents_feature
        self._search_journals = search_journals_feature
        self._list_fiscal_years = list_fiscal_years_feature

    def execute(self, request: ProjectStatusRequest) -> ProjectStatusDTO:
        request.validate()

        try:
            project = self._get_project.execute(GetProjectRequest(project_id=request.project_id)).project
            documents = self._list_documents.execute(ListDocumentsRequest()).documents
            journals = self._search_journals.execute(
                SearchJournalsRequest(text=str(request.project_id))
            ).journals
            fiscal_years = self._list_fiscal_years.execute(ListFiscalYearsRequest()).fiscal_years
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Project status data retrieval failed") from exc

        linked_documents = tuple(
            document
            for document in documents
            if any(
                reference.target_capability == "PROJECTS"
                and reference.target_aggregate_type == "PROJECT"
                and reference.target_aggregate_id == str(project.project_id)
                for reference in document.references
            )
        )

        finalized_documents = tuple(
            document
            for document in linked_documents
            if str(document.status).upper() == "ACTIVE" and len(document.versions) > 0
        )
        outstanding_documents = tuple(
            document for document in linked_documents if document not in finalized_documents
        )

        budget_categories = tuple(self._budget_categories(project.references))
        budget_ready = any(
            ref.reference_type == "DOCUMENT"
            and (ref.description or "").strip().upper() == "BUDGET_STATUS:READY"
            for ref in project.references
        )
        budget_status = (
            "READY"
            if budget_ready
            else "IN_PROGRESS"
            if budget_categories
            else "MISSING"
        )

        project_journals = tuple(
            journal
            for journal in journals
            if journal.reference is not None
            and str(project.project_id) in journal.reference
        )
        journal_count = len(project_journals)
        last_journal = (
            max(project_journals, key=lambda item: item.posting_date).journal_number
            if project_journals
            else None
        )
        fiscal_year = (
            max(journal.posting_date.year for journal in project_journals)
            if project_journals
            else next((item.year for item in fiscal_years if str(item.status).upper() == "OPEN"), None)
        )
        if journal_count == 0:
            accounting_status = "MISSING"
        elif any(str(journal.status).upper() != "POSTED" for journal in project_journals):
            accounting_status = "IN_PROGRESS"
        else:
            accounting_status = "COMPLETE"

        archive_status, closure_status = self._derive_archive_state(project=project, finalized_documents=finalized_documents, accounting_status=accounting_status, budget_ready=budget_ready)

        missing_requirements = self._derive_missing_requirements(
            budget_ready=budget_ready,
            finalized_documents=finalized_documents,
            accounting_status=accounting_status,
            archive_status=archive_status,
        )
        ready_for_closure = archive_status == "READY_FOR_ARCHIVE"
        if ready_for_closure and closure_status == "CLOSED":
            ready_for_closure = False

        overall_health_indicator = (
            "HEALTHY"
            if not missing_requirements
            else "AT_RISK"
            if len(missing_requirements) <= 2
            else "CRITICAL"
        )

        return ProjectStatusDTO(
            project=ProjectStatusProjectResponse(
                project_id=project.project_id,
                name=project.project_name,
                status=str(project.status).upper(),
                created_date=self._normalize_datetime(project.created_at).date(),
                last_updated=project.updated_at,
                organization=self._project_organization(project.references),
            ),
            documents=ProjectStatusDocumentsResponse(
                total_documents=len(linked_documents),
                finalized_documents=len(finalized_documents),
                outstanding_documents=len(outstanding_documents),
            ),
            budget=ProjectStatusBudgetResponse(
                budget_status=budget_status,
                budget_categories=budget_categories,
                budget_ready=budget_ready,
            ),
            accounting=ProjectStatusAccountingResponse(
                journal_count=journal_count,
                last_journal=last_journal,
                fiscal_year=fiscal_year,
                accounting_status=accounting_status,
            ),
            archive=ProjectStatusArchiveResponse(
                archive_status=archive_status,
                closure_status=closure_status,
            ),
            health=ProjectStatusHealthResponse(
                overall_health_indicator=overall_health_indicator,
                missing_requirements=tuple(missing_requirements),
                ready_for_closure=ready_for_closure,
            ),
        )

    @staticmethod
    def _project_organization(references) -> ProjectStatusOrganizationResponse:
        organization_reference = next(
            (
                ref
                for ref in references
                if ref.reference_type == "ORGANISATION"
            ),
            None,
        )
        return ProjectStatusOrganizationResponse(
            organization_id=(None if organization_reference is None else organization_reference.external_id),
            name=None,
            status=None,
        )

    @staticmethod
    def _budget_categories(references) -> list[str]:
        categories: list[str] = []
        for ref in references:
            description = (ref.description or "").strip().upper()
            if ref.reference_type != "DOCUMENT" or not description.startswith("BUDGET_CATEGORY:"):
                continue
            categories.append(description.split(":", 1)[1])
        return categories

    @staticmethod
    def _derive_archive_state(
        *,
        project,
        finalized_documents,
        accounting_status: str,
        budget_ready: bool,
    ) -> tuple[str, str]:
        closure_status = (
            "CLOSED"
            if str(project.status).upper() in {"COMPLETED", "ARCHIVED"}
            or any(
                ref.reference_type == "DOCUMENT"
                and (ref.description or "").strip().upper() == "PROJECT_CLOSURE_STATUS:CLOSED"
                for ref in project.references
            )
            else "OPEN"
        )
        if str(project.status).upper() == "ARCHIVED":
            return "ARCHIVED", closure_status
        if budget_ready and accounting_status == "COMPLETE" and finalized_documents:
            return "READY_FOR_ARCHIVE", closure_status
        return "NOT_READY", closure_status

    @staticmethod
    def _derive_missing_requirements(
        *,
        budget_ready: bool,
        finalized_documents,
        accounting_status: str,
        archive_status: str,
    ) -> list[str]:
        missing: list[str] = []
        if not budget_ready:
            missing.append("BUDGET")
        if not finalized_documents:
            missing.append("DOCUMENTATION")
        if accounting_status != "COMPLETE":
            missing.append("ACCOUNTING")
        if archive_status != "READY_FOR_ARCHIVE" and archive_status != "ARCHIVED":
            missing.append("ARCHIVE")
        return missing

    @staticmethod
    def _normalize_datetime(value: datetime | date) -> datetime:
        if isinstance(value, date) and not isinstance(value, datetime):
            return datetime(value.year, value.month, value.day, tzinfo=UTC)
        assert isinstance(value, datetime)
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)