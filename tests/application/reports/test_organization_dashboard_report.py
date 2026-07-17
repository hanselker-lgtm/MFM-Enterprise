from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from types import SimpleNamespace
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.reports.organization_dashboard_report import (
    OrganizationDashboardReportRequest,
)
from mfm.application.reports.organization_dashboard_report import (
    OrganizationDashboardReportService,
)
from mfm.application.reports.organization_dashboard_report import RepositoryException
from mfm.application.reports.organization_dashboard_report import ValidationException


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
    status: str
    references: tuple[_ProjectReference, ...]
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
    reference: str | None


@dataclass(frozen=True, slots=True)
class _FiscalYear:
    status: str


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


def _build_service(*, organization_id: UUID, other_organization_id: UUID) -> OrganizationDashboardReportService:
    project_active = uuid4()
    project_completed = uuid4()
    project_archived = uuid4()
    project_other_org = uuid4()

    projects = (
        _Project(
            project_id=project_active,
            status="ACTIVE",
            references=(
                _ProjectReference(
                    reference_type="ORGANISATION",
                    external_id=organization_id,
                    description="Org link",
                ),
                _ProjectReference(
                    reference_type="DOCUMENT",
                    external_id=uuid4(),
                    description="BUDGET_STATUS:READY",
                ),
            ),
        ),
        _Project(
            project_id=project_completed,
            status="COMPLETED",
            references=(
                _ProjectReference(
                    reference_type="ORGANISATION",
                    external_id=organization_id,
                    description="Org link",
                ),
                _ProjectReference(
                    reference_type="DOCUMENT",
                    external_id=uuid4(),
                    description="PROJECT_CLOSURE_STATUS:CLOSED",
                ),
            ),
        ),
        _Project(
            project_id=project_archived,
            status="ARCHIVED",
            references=(
                _ProjectReference(
                    reference_type="ORGANISATION",
                    external_id=organization_id,
                    description="Org link",
                ),
            ),
        ),
        _Project(
            project_id=project_other_org,
            status="ACTIVE",
            references=(
                _ProjectReference(
                    reference_type="ORGANISATION",
                    external_id=other_organization_id,
                    description="Other org link",
                ),
            ),
        ),
    )

    documents = (
        _Document(
            references=(
                _DocumentReference(
                    target_capability="PROJECTS",
                    target_aggregate_type="PROJECT",
                    target_aggregate_id=str(project_active),
                ),
            ),
            created_at=datetime(2040, 5, 1, 8, 0, tzinfo=UTC),
            updated_at=datetime(2040, 5, 7, 8, 0, tzinfo=UTC),
        ),
        _Document(
            references=(
                _DocumentReference(
                    target_capability="PROJECTS",
                    target_aggregate_type="PROJECT",
                    target_aggregate_id=str(project_completed),
                ),
            ),
            created_at=datetime(2040, 5, 5, 8, 0, tzinfo=UTC),
        ),
        _Document(
            references=(
                _DocumentReference(
                    target_capability="PROJECTS",
                    target_aggregate_type="PROJECT",
                    target_aggregate_id=str(project_other_org),
                ),
            ),
            created_at=datetime(2040, 5, 10, 8, 0, tzinfo=UTC),
        ),
    )

    journals = (
        _Journal(
            posting_date=date(2040, 6, 1),
            status="POSTED",
            reference=f"PROJECT:{project_active}",
        ),
        _Journal(
            posting_date=date(2040, 6, 3),
            status="DRAFT",
            reference=f"PROJECT:{project_active}",
        ),
        _Journal(
            posting_date=date(2040, 6, 4),
            status="POSTED",
            reference=f"PROJECT:{project_other_org}",
        ),
    )

    fiscal_years = (_FiscalYear(status="OPEN"), _FiscalYear(status="CLOSED"))

    return OrganizationDashboardReportService(
        list_projects_feature=_ResultStub(SimpleNamespace(projects=projects)),
        list_documents_feature=_ResultStub(SimpleNamespace(documents=documents)),
        search_journals_feature=_ResultStub(SimpleNamespace(journals=journals)),
        list_fiscal_years_feature=_ResultStub(SimpleNamespace(fiscal_years=fiscal_years)),
    )


def test_service_happy_path_composes_dashboard() -> None:
    organization_id = uuid4()
    service = _build_service(organization_id=organization_id, other_organization_id=uuid4())

    response = service.execute(
        OrganizationDashboardReportRequest(
            organization_id=organization_id,
            organization_number="ORG-001",
            organization_name="Acme Maritime",
            organization_type="MEMBER",
            organization_status="ACTIVE",
        )
    )

    assert response.organization.organization_id == organization_id
    assert response.organization.organization_number == "ORG-001"
    assert response.organization.organization_type == "MEMBER"
    assert response.active_projects == 1
    assert response.closed_projects == 1
    assert response.archived_projects == 1
    assert response.project_documents == 2
    assert response.accounting_journals == 2
    assert response.open_fiscal_years == 1
    assert response.last_accounting_activity == date(2040, 6, 3)
    assert response.last_document_activity == datetime(2040, 5, 7, 8, 0, tzinfo=UTC)
    assert response.health_indicators.healthy_projects == 0
    assert response.health_indicators.at_risk_projects == 1
    assert response.health_indicators.projects_with_budget_ready == 1
    assert response.health_indicators.projects_with_unposted_journals == 1
    assert response.health_indicators.overall_health_status == "CRITICAL"


def test_service_applies_time_period_filters() -> None:
    organization_id = uuid4()
    service = _build_service(organization_id=organization_id, other_organization_id=uuid4())

    response = service.execute(
        OrganizationDashboardReportRequest(
            organization_id=organization_id,
            period_start=date(2040, 6, 2),
            period_end=date(2040, 6, 2),
        )
    )

    assert response.project_documents == 0
    assert response.accounting_journals == 0
    assert response.last_accounting_activity is None
    assert response.last_document_activity is None


def test_service_validates_request() -> None:
    service = _build_service(organization_id=uuid4(), other_organization_id=uuid4())

    with pytest.raises(ValidationException, match="period_start"):
        service.execute(
            OrganizationDashboardReportRequest(
                organization_id=uuid4(),
                period_start=date(2040, 6, 3),
                period_end=date(2040, 6, 2),
            )
        )


def test_service_wraps_dependency_failures() -> None:
    service = OrganizationDashboardReportService(
        list_projects_feature=_ErrorStub(RuntimeError("db unavailable")),
        list_documents_feature=_ResultStub(SimpleNamespace(documents=())),
        search_journals_feature=_ResultStub(SimpleNamespace(journals=())),
        list_fiscal_years_feature=_ResultStub(SimpleNamespace(fiscal_years=())),
    )

    with pytest.raises(RepositoryException, match="data retrieval failed"):
        service.execute(OrganizationDashboardReportRequest(organization_id=uuid4()))
