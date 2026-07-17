from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from types import SimpleNamespace
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.reporting.active_projects_service import (
    ActiveProjectsDashboardRequest,
)
from mfm.application.reporting.active_projects_service import ActiveProjectsService
from mfm.application.reporting.active_projects_service import RepositoryException
from mfm.application.reporting.active_projects_service import ValidationException


@dataclass(frozen=True, slots=True)
class _ProjectAssignment:
    organisation_id: UUID


@dataclass(frozen=True, slots=True)
class _ProjectReference:
    reference_type: str
    external_id: UUID
    description: str | None = None


@dataclass(frozen=True, slots=True)
class _Project:
    project_id: UUID
    project_name: str
    status: str
    created_at: datetime
    updated_at: datetime | None = None
    references: tuple[_ProjectReference, ...] = ()
    assignments: tuple[_ProjectAssignment, ...] = ()


@dataclass(frozen=True, slots=True)
class _DocumentReference:
    target_capability: str
    target_aggregate_type: str
    target_aggregate_id: str


@dataclass(frozen=True, slots=True)
class _Document:
    references: tuple[_DocumentReference, ...]
    created_at: datetime
    updated_at: datetime | None = None


@dataclass(frozen=True, slots=True)
class _Journal:
    posting_date: date
    status: str
    journal_number: str
    reference: str | None


@dataclass
class _ResultStub:
    value: object

    def execute(self, request):
        _ = request
        return self.value


@dataclass
class _ErrorStub:
    error: Exception

    def execute(self, request):
        _ = request
        raise self.error


def _build_service(*, organization_id: UUID, other_organization_id: UUID) -> ActiveProjectsService:
    project_healthy = uuid4()
    project_at_risk = uuid4()
    project_critical = uuid4()
    project_other_org = uuid4()

    projects = (
        _Project(
            project_id=project_healthy,
            project_name="Alpha",
            status="ACTIVE",
            created_at=datetime(2040, 1, 1, 8, 0, tzinfo=UTC),
            references=(
                _ProjectReference("ORGANISATION", organization_id),
                _ProjectReference("DOCUMENT", uuid4(), "BUDGET_STATUS:READY"),
            ),
        ),
        _Project(
            project_id=project_at_risk,
            project_name="Beta",
            status="ACTIVE",
            created_at=datetime(2040, 1, 2, 8, 0, tzinfo=UTC),
            references=(
                _ProjectReference("ORGANISATION", organization_id),
                _ProjectReference("DOCUMENT", uuid4(), "BUDGET_STATUS:READY"),
            ),
        ),
        _Project(
            project_id=project_critical,
            project_name="Gamma",
            status="ACTIVE",
            created_at=datetime(2040, 1, 3, 8, 0, tzinfo=UTC),
            references=(_ProjectReference("ORGANISATION", organization_id),),
        ),
        _Project(
            project_id=project_other_org,
            project_name="Other",
            status="ACTIVE",
            created_at=datetime(2040, 1, 4, 8, 0, tzinfo=UTC),
            references=(_ProjectReference("ORGANISATION", other_organization_id),),
        ),
    )

    documents = (
        _Document(
            references=(
                _DocumentReference("PROJECTS", "PROJECT", str(project_healthy)),
            ),
            created_at=datetime(2040, 2, 1, 8, 0, tzinfo=UTC),
            updated_at=datetime(2040, 2, 4, 8, 0, tzinfo=UTC),
        ),
        _Document(
            references=(
                _DocumentReference("PROJECTS", "PROJECT", str(project_at_risk)),
            ),
            created_at=datetime(2040, 2, 2, 8, 0, tzinfo=UTC),
        ),
    )

    journals = (
        _Journal(date(2040, 3, 1), "POSTED", "JRN-001", f"PROJECT:{project_healthy}"),
        _Journal(date(2040, 3, 2), "POSTED", "JRN-002", f"PROJECT:{project_at_risk}"),
        _Journal(date(2040, 3, 3), "DRAFT", "JRN-003", f"PROJECT:{project_at_risk}"),
    )

    return ActiveProjectsService(
        list_projects_feature=_ResultStub(SimpleNamespace(projects=projects)),
        list_documents_feature=_ResultStub(SimpleNamespace(documents=documents)),
        search_journals_feature=_ResultStub(SimpleNamespace(journals=journals)),
    )


def test_service_happy_path_composes_dashboard() -> None:
    organization_id = uuid4()
    service = _build_service(organization_id=organization_id, other_organization_id=uuid4())

    response = service.execute(ActiveProjectsDashboardRequest(organization_id=organization_id))

    assert response.totals.active_project_count == 3
    assert response.totals.projects_missing_budget == 1
    assert response.totals.projects_missing_documentation == 1
    assert response.totals.projects_missing_accounting == 2
    assert response.totals.projects_ready_for_closure == 1

    alpha = next(project for project in response.projects if project.name == "Alpha")
    assert alpha.budget_status == "READY"
    assert alpha.accounting_status == "COMPLETE"
    assert alpha.documentation_status == "COMPLETE"
    assert alpha.archive_status == "READY_FOR_CLOSURE"
    assert alpha.health_indicator == "HEALTHY"

    beta = next(project for project in response.projects if project.name == "Beta")
    assert beta.accounting_status == "IN_PROGRESS"
    assert beta.health_indicator == "AT_RISK"

    gamma = next(project for project in response.projects if project.name == "Gamma")
    assert gamma.budget_status == "MISSING"
    assert gamma.documentation_status == "MISSING"
    assert gamma.accounting_status == "MISSING"
    assert gamma.health_indicator == "CRITICAL"


def test_service_validates_request() -> None:
    service = _build_service(organization_id=uuid4(), other_organization_id=uuid4())

    with pytest.raises(ValidationException, match="organization_id"):
        service.execute(
            ActiveProjectsDashboardRequest(organization_id="not-a-uuid")  # type: ignore[arg-type]
        )


def test_service_wraps_dependency_failures() -> None:
    service = ActiveProjectsService(
        list_projects_feature=_ErrorStub(RuntimeError("db unavailable")),
        list_documents_feature=_ResultStub(SimpleNamespace(documents=())),
        search_journals_feature=_ResultStub(SimpleNamespace(journals=())),
    )

    with pytest.raises(RepositoryException, match="data retrieval failed"):
        service.execute(ActiveProjectsDashboardRequest(organization_id=uuid4()))
