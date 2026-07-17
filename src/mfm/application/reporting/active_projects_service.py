"""Application reporting service for REP-002 active projects dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.accounting import SearchJournalsRequest
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.projects import ListProjectsRequest
from mfm.application.reporting.models.active_projects_dto import (
    ActiveProjectDashboardProjectDTO,
)
from mfm.application.reporting.models.active_projects_dto import (
    ActiveProjectsDashboardResponse,
)
from mfm.application.reporting.models.active_projects_dto import (
    ActiveProjectsDashboardTotalsDTO,
)


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when dashboard request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when dependent feature APIs fail."""


@dataclass(frozen=True, slots=True)
class ActiveProjectsDashboardRequest:
    organization_id: UUID

    def validate(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValidationException("organization_id must be UUID")


class ListProjectsFeaturePort(Protocol):
    def execute(self, request: ListProjectsRequest): ...


class ListDocumentsFeaturePort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class SearchJournalsFeaturePort(Protocol):
    def execute(self, request: SearchJournalsRequest): ...


class ActiveProjectsService:
    """Compose active-project reporting data from feature APIs only."""

    def __init__(
        self,
        *,
        list_projects_feature: ListProjectsFeaturePort,
        list_documents_feature: ListDocumentsFeaturePort,
        search_journals_feature: SearchJournalsFeaturePort,
    ) -> None:
        self._list_projects = list_projects_feature
        self._list_documents = list_documents_feature
        self._search_journals = search_journals_feature

    def execute(self, request: ActiveProjectsDashboardRequest) -> ActiveProjectsDashboardResponse:
        request.validate()

        try:
            projects = self._list_projects.execute(ListProjectsRequest()).projects
            documents = self._list_documents.execute(ListDocumentsRequest()).documents
            journals = self._search_journals.execute(SearchJournalsRequest()).journals
        except ApplicationException:
            raise
        except Exception as exc:
            raise RepositoryException("Active projects dashboard data retrieval failed") from exc

        active_projects = tuple(
            project
            for project in projects
            if str(project.status).upper() == "ACTIVE"
            and self._project_belongs_to_organization(
                project=project,
                organization_id=request.organization_id,
            )
        )
        active_project_ids = {project.project_id for project in active_projects}

        documents_by_project: dict[UUID, list] = {project_id: [] for project_id in active_project_ids}
        for document in documents:
            linked_project_ids = {
                self._parse_uuid(reference.target_aggregate_id)
                for reference in document.references
                if reference.target_capability == "PROJECTS"
                and reference.target_aggregate_type == "PROJECT"
            }
            for project_id in linked_project_ids:
                if project_id is None or project_id not in documents_by_project:
                    continue
                documents_by_project[project_id].append(document)

        journals_by_project: dict[UUID, list] = {project_id: [] for project_id in active_project_ids}
        for journal in journals:
            if journal.reference is None:
                continue
            for project_id in active_project_ids:
                if str(project_id) in journal.reference:
                    journals_by_project[project_id].append(journal)

        project_rows: list[ActiveProjectDashboardProjectDTO] = []
        projects_missing_budget = 0
        projects_missing_documentation = 0
        projects_missing_accounting = 0
        projects_ready_for_closure = 0

        for project in sorted(active_projects, key=lambda item: (item.project_name, str(item.project_id))):
            project_documents = tuple(documents_by_project.get(project.project_id, ()))
            project_journals = tuple(journals_by_project.get(project.project_id, ()))

            budget_status = self._budget_status(project)
            accounting_status = self._accounting_status(project_journals)
            documentation_status = self._documentation_status(project_documents)
            archive_status = self._archive_status(
                budget_status=budget_status,
                accounting_status=accounting_status,
                documentation_status=documentation_status,
                project_status=str(project.status).upper(),
            )
            health_indicator = self._health_indicator(
                budget_status=budget_status,
                accounting_status=accounting_status,
                documentation_status=documentation_status,
            )

            if budget_status != "READY":
                projects_missing_budget += 1
            if documentation_status != "COMPLETE":
                projects_missing_documentation += 1
            if accounting_status != "COMPLETE":
                projects_missing_accounting += 1
            if archive_status == "READY_FOR_CLOSURE":
                projects_ready_for_closure += 1

            project_rows.append(
                ActiveProjectDashboardProjectDTO(
                    project_id=project.project_id,
                    name=project.project_name,
                    status=str(project.status).upper(),
                    created_date=self._normalize_datetime(project.created_at).date(),
                    budget_status=budget_status,
                    accounting_status=accounting_status,
                    documentation_status=documentation_status,
                    archive_status=archive_status,
                    last_activity=self._last_activity(
                        project=project,
                        documents=project_documents,
                        journals=project_journals,
                    ),
                    health_indicator=health_indicator,
                )
            )

        return ActiveProjectsDashboardResponse(
            projects=tuple(project_rows),
            totals=ActiveProjectsDashboardTotalsDTO(
                active_project_count=len(project_rows),
                projects_missing_budget=projects_missing_budget,
                projects_missing_documentation=projects_missing_documentation,
                projects_missing_accounting=projects_missing_accounting,
                projects_ready_for_closure=projects_ready_for_closure,
            ),
        )

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
    def _budget_status(project) -> str:
        return (
            "READY"
            if any(
                reference.reference_type == "DOCUMENT"
                and (reference.description or "").strip().upper() == "BUDGET_STATUS:READY"
                for reference in project.references
            )
            else "MISSING"
        )

    @staticmethod
    def _accounting_status(journals: tuple) -> str:
        if not journals:
            return "MISSING"
        if any(str(journal.status).upper() != "POSTED" for journal in journals):
            return "IN_PROGRESS"
        return "COMPLETE"

    @staticmethod
    def _documentation_status(documents: tuple) -> str:
        return "COMPLETE" if documents else "MISSING"

    @staticmethod
    def _archive_status(
        *,
        budget_status: str,
        accounting_status: str,
        documentation_status: str,
        project_status: str,
    ) -> str:
        if project_status == "ARCHIVED":
            return "ARCHIVED"
        if (
            budget_status == "READY"
            and accounting_status == "COMPLETE"
            and documentation_status == "COMPLETE"
        ):
            return "READY_FOR_CLOSURE"
        return "NOT_READY"

    @staticmethod
    def _health_indicator(
        *,
        budget_status: str,
        accounting_status: str,
        documentation_status: str,
    ) -> str:
        if (
            budget_status == "READY"
            and accounting_status == "COMPLETE"
            and documentation_status == "COMPLETE"
        ):
            return "HEALTHY"

        missing = 0
        if budget_status != "READY":
            missing += 1
        if accounting_status != "COMPLETE":
            missing += 1
        if documentation_status != "COMPLETE":
            missing += 1

        if missing >= 2:
            return "CRITICAL"
        return "AT_RISK"

    def _last_activity(self, *, project, documents: tuple, journals: tuple) -> datetime | None:
        candidates: list[datetime] = [
            self._normalize_datetime(project.updated_at or project.created_at),
        ]

        candidates.extend(
            self._normalize_datetime(document.updated_at or document.created_at)
            for document in documents
        )
        candidates.extend(self._normalize_datetime(journal.posting_date) for journal in journals)

        if not candidates:
            return None
        return max(candidates)

    @staticmethod
    def _normalize_datetime(value: datetime | date) -> datetime:
        if isinstance(value, date) and not isinstance(value, datetime):
            return datetime(value.year, value.month, value.day, tzinfo=UTC)
        assert isinstance(value, datetime)
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

    @staticmethod
    def _parse_uuid(value: str) -> UUID | None:
        try:
            return UUID(value)
        except Exception:
            return None
