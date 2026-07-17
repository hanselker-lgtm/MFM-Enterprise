from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from types import SimpleNamespace
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.reporting.project_status_service import ProjectStatusRequest
from mfm.application.reporting.project_status_service import ProjectStatusService
from mfm.application.reporting.project_status_service import RepositoryException
from mfm.application.reporting.project_status_service import ValidationException


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
class _DocumentVersion:
    version_number: int


@dataclass(frozen=True, slots=True)
class _Document:
    document_id: UUID
    document_number: str
    document_title: str
    document_type: str
    status: str
    created_at: datetime
    updated_at: datetime | None = None
    archived_at: datetime | None = None
    disposed_at: datetime | None = None
    version: int = 1
    versions: tuple[_DocumentVersion, ...] = ()
    references: tuple[_DocumentReference, ...] = ()


@dataclass(frozen=True, slots=True)
class _Journal:
    journal_number: str
    posting_date: date
    status: str
    reference: str | None


@dataclass(frozen=True, slots=True)
class _FiscalYear:
    year: int
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


def _build_service(*, project_id: UUID, organization_id: UUID) -> ProjectStatusService:
    project = _Project(
        project_id=project_id,
        project_name="Project Alpha",
        status="ACTIVE",
        created_at=datetime(2040, 1, 1, 8, 0, tzinfo=UTC),
        updated_at=datetime(2040, 2, 1, 9, 0, tzinfo=UTC),
        references=(
            _ProjectReference("ORGANISATION", organization_id),
            _ProjectReference("DOCUMENT", uuid4(), "BUDGET_CATEGORY:LABOR"),
            _ProjectReference("DOCUMENT", uuid4(), "BUDGET_CATEGORY:MATERIALS"),
            _ProjectReference("DOCUMENT", uuid4(), "BUDGET_STATUS:READY"),
        ),
    )

    documents = (
        _Document(
            document_id=uuid4(),
            document_number="DOC-001",
            document_title="Finalized scope",
            document_type="PROJECT_DOCUMENT",
            status="ACTIVE",
            created_at=datetime(2040, 2, 1, 8, 0, tzinfo=UTC),
            updated_at=datetime(2040, 2, 2, 8, 0, tzinfo=UTC),
            versions=(_DocumentVersion(version_number=1),),
            references=(
                _DocumentReference("PROJECTS", "PROJECT", str(project_id)),
            ),
        ),
        _Document(
            document_id=uuid4(),
            document_number="DOC-002",
            document_title="Draft note",
            document_type="PROJECT_DOCUMENT",
            status="DRAFT",
            created_at=datetime(2040, 2, 3, 8, 0, tzinfo=UTC),
            references=(
                _DocumentReference("PROJECTS", "PROJECT", str(project_id)),
            ),
        ),
    )

    journals = (
        _Journal("JRN-001", date(2040, 3, 1), "POSTED", f"PROJECT:{project_id}"),
        _Journal("JRN-002", date(2040, 3, 15), "POSTED", f"PROJECT:{project_id}"),
    )

    fiscal_years = (_FiscalYear(2040, "OPEN"), _FiscalYear(2039, "CLOSED"))

    return ProjectStatusService(
        get_project_feature=_ResultStub(SimpleNamespace(project=project)),
        list_documents_feature=_ResultStub(SimpleNamespace(documents=documents)),
        search_journals_feature=_ResultStub(SimpleNamespace(journals=journals)),
        list_fiscal_years_feature=_ResultStub(SimpleNamespace(fiscal_years=fiscal_years)),
    )


def test_service_happy_path_composes_project_status() -> None:
    project_id = uuid4()
    organization_id = uuid4()
    service = _build_service(project_id=project_id, organization_id=organization_id)

    result = service.execute(ProjectStatusRequest(project_id=project_id))

    assert result.project.project_id == project_id
    assert result.project.organization.organization_id == organization_id
    assert result.documents.total_documents == 2
    assert result.documents.finalized_documents == 1
    assert result.documents.outstanding_documents == 1
    assert result.budget.budget_status == "READY"
    assert result.budget.budget_categories == ("LABOR", "MATERIALS")
    assert result.budget.budget_ready is True
    assert result.accounting.journal_count == 2
    assert result.accounting.last_journal == "JRN-002"
    assert result.accounting.fiscal_year == 2040
    assert result.accounting.accounting_status == "COMPLETE"
    assert result.archive.archive_status == "READY_FOR_ARCHIVE"
    assert result.archive.closure_status == "OPEN"
    assert result.health.overall_health_indicator == "HEALTHY"
    assert result.health.missing_requirements == ()
    assert result.health.ready_for_closure is True


def test_service_validates_request() -> None:
    service = _build_service(project_id=uuid4(), organization_id=uuid4())

    with pytest.raises(ValidationException, match="project_id"):
        service.execute(ProjectStatusRequest(project_id="bad"))  # type: ignore[arg-type]


def test_service_wraps_dependency_failures() -> None:
    service = ProjectStatusService(
        get_project_feature=_ErrorStub(RuntimeError("db unavailable")),
        list_documents_feature=_ResultStub(SimpleNamespace(documents=())),
        search_journals_feature=_ResultStub(SimpleNamespace(journals=())),
        list_fiscal_years_feature=_ResultStub(SimpleNamespace(fiscal_years=())),
    )

    with pytest.raises(RepositoryException, match="data retrieval failed"):
        service.execute(ProjectStatusRequest(project_id=uuid4()))
