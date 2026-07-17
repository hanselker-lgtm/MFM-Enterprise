from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import mfm.database.models.external_reference_model  # noqa: F401
import mfm.database.models.project_activity_model  # noqa: F401
import mfm.database.models.project_assignment_model  # noqa: F401
import mfm.database.models.project_milestone_model  # noqa: F401
import mfm.database.models.project_model  # noqa: F401
import mfm.infrastructure.persistence.accounting.fiscal_period_model  # noqa: F401
import mfm.infrastructure.persistence.accounting.fiscal_year_model  # noqa: F401
import mfm.infrastructure.persistence.accounting.journal_entry_model  # noqa: F401
import mfm.infrastructure.persistence.accounting.journal_model  # noqa: F401
import mfm.infrastructure.persistence.documents.document_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.accounting.create_fiscal_year import CreateFiscalYearUseCase
from mfm.application.accounting.create_journal import CreateJournalUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.search_journals import SearchJournalsUseCase
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.features.accounting import CreateFiscalYearFeature
from mfm.application.features.accounting import CreateFiscalYearRequest
from mfm.application.features.accounting import CreateJournalFeature
from mfm.application.features.accounting import CreateJournalRequest
from mfm.application.features.accounting import FiscalPeriodInput
from mfm.application.features.accounting import JournalLineInput
from mfm.application.features.accounting import ListFiscalYearsFeature
from mfm.application.features.accounting import SearchJournalsFeature
from mfm.application.features.documents import CreateDocumentFeature
from mfm.application.features.documents import CreateDocumentRequest
from mfm.application.features.documents import DocumentReferenceInput
from mfm.application.features.documents import ListDocumentsFeature
from mfm.application.features.documents import DocumentVersionInput
from mfm.application.features.projects import CreateProjectFeature
from mfm.application.features.projects import CreateProjectRequest
from mfm.application.features.projects import ExternalReferenceInput
from mfm.application.features.projects import ListProjectsFeature
from mfm.application.features.reporting import OrganizationDashboardFeature
from mfm.application.features.reporting import OrganizationDashboardRequest
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.list_projects import ListProjectsUseCase
from mfm.application.reporting.organization_dashboard_service import (
    OrganizationDashboardService,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteFiscalYearRepository,
)
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteJournalRepository,
)
from mfm.infrastructure.persistence.documents.sqlite_document_repository import (
    SQLiteDocumentRepository,
)
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteReportingUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.project_repository = SQLiteProjectRepository(self._persistence_uow)
        self.document_repository = SQLiteDocumentRepository(self._persistence_uow)
        self.fiscal_year_repository = SQLiteFiscalYearRepository(self._persistence_uow)
        self.journal_repository = SQLiteJournalRepository(self._persistence_uow)

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None

    def _commit_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.commit()

    def _rollback_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        return None


@dataclass(frozen=True, slots=True)
class _FeatureStack:
    create_project: CreateProjectFeature
    list_projects: ListProjectsFeature
    create_document: CreateDocumentFeature
    list_documents: ListDocumentsFeature
    create_fiscal_year: CreateFiscalYearFeature
    create_journal: CreateJournalFeature
    list_fiscal_years: ListFiscalYearsFeature
    search_journals: SearchJournalsFeature
    dashboard: OrganizationDashboardFeature


@pytest.fixture(autouse=True)
def _reset_fiscal_year_state() -> None:
    FiscalYear._open_year_id = None
    try:
        yield
    finally:
        FiscalYear._open_year_id = None


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "organization_dashboard_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_stack(session: Session) -> _FeatureStack:
    uow = SQLiteReportingUnitOfWork(session)

    list_projects = ListProjectsFeature(service=ListProjectsUseCase(unit_of_work=uow))
    list_documents = ListDocumentsFeature(service=ListDocumentsUseCase(unit_of_work=uow))
    search_journals = SearchJournalsFeature(service=SearchJournalsUseCase(unit_of_work=uow))
    list_fiscal_years = ListFiscalYearsFeature(service=ListFiscalYearsUseCase(unit_of_work=uow))

    report_service = OrganizationDashboardService(
        list_projects_feature=list_projects,
        list_documents_feature=list_documents,
        search_journals_feature=search_journals,
        list_fiscal_years_feature=list_fiscal_years,
    )

    return _FeatureStack(
        create_project=CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow)),
        list_projects=list_projects,
        create_document=CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow)),
        list_documents=list_documents,
        create_fiscal_year=CreateFiscalYearFeature(service=CreateFiscalYearUseCase(unit_of_work=uow)),
        create_journal=CreateJournalFeature(service=CreateJournalUseCase(unit_of_work=uow)),
        list_fiscal_years=list_fiscal_years,
        search_journals=search_journals,
        dashboard=OrganizationDashboardFeature(service=report_service),
    )


def _aware_utc(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, tzinfo=UTC)


def test_organization_dashboard_e2e(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_stack(session)

        organization_id = UUID("00000000-0000-0000-0000-00000000AA11")
        other_organization_id = UUID("00000000-0000-0000-0000-00000000AA12")

        active_project = stack.create_project.execute(
            CreateProjectRequest(
                project_number="PRJ-REP001-001",
                project_name="REP-001 Active",
                status="ACTIVE",
                references=(
                    ExternalReferenceInput(
                        reference_type="ORGANISATION",
                        external_id=organization_id,
                        description="Organization link",
                        created_at=_aware_utc(2040, 1, 2, 8),
                    ),
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=UUID("00000000-0000-0000-0000-00000000BB01"),
                        description="BUDGET_STATUS:READY",
                        created_at=_aware_utc(2040, 1, 3, 8),
                    ),
                ),
                created_at=_aware_utc(2040, 1, 1, 8),
            )
        ).project

        completed_project = stack.create_project.execute(
            CreateProjectRequest(
                project_number="PRJ-REP001-002",
                project_name="REP-001 Completed",
                status="COMPLETED",
                references=(
                    ExternalReferenceInput(
                        reference_type="ORGANISATION",
                        external_id=organization_id,
                        description="Organization link",
                        created_at=_aware_utc(2040, 1, 5, 8),
                    ),
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=UUID("00000000-0000-0000-0000-00000000BB02"),
                        description="PROJECT_CLOSURE_STATUS:CLOSED",
                        created_at=_aware_utc(2040, 3, 1, 8),
                    ),
                ),
                created_at=_aware_utc(2040, 1, 4, 8),
            )
        ).project

        stack.create_project.execute(
            CreateProjectRequest(
                project_number="PRJ-REP001-003",
                project_name="REP-001 Other Org",
                status="ACTIVE",
                references=(
                    ExternalReferenceInput(
                        reference_type="ORGANISATION",
                        external_id=other_organization_id,
                        description="Other organization",
                        created_at=_aware_utc(2040, 1, 8, 8),
                    ),
                ),
                created_at=_aware_utc(2040, 1, 7, 8),
            )
        )

        stack.create_document.execute(
            CreateDocumentRequest(
                document_number="DOC-REP001-001",
                document_title="Organization project contract",
                document_type="PROJECT_DOCUMENT",
                status="ACTIVE",
                created_at=_aware_utc(2040, 2, 10, 8),
                versions=(
                    DocumentVersionInput(
                        version_number=1,
                        storage_key="docs/rep001/1",
                        created_at=_aware_utc(2040, 2, 10, 8),
                    ),
                ),
                references=(
                    DocumentReferenceInput(
                        target_capability="PROJECTS",
                        target_aggregate_type="PROJECT",
                        target_aggregate_id=str(active_project.project_id),
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=_aware_utc(2040, 2, 10, 8),
                    ),
                ),
            )
        )

        stack.create_document.execute(
            CreateDocumentRequest(
                document_number="DOC-REP001-002",
                document_title="Project closure memo",
                document_type="PROJECT_DOCUMENT",
                status="ACTIVE",
                created_at=_aware_utc(2040, 3, 10, 8),
                versions=(
                    DocumentVersionInput(
                        version_number=1,
                        storage_key="docs/rep001/2",
                        created_at=_aware_utc(2040, 3, 10, 8),
                    ),
                ),
                references=(
                    DocumentReferenceInput(
                        target_capability="PROJECTS",
                        target_aggregate_type="PROJECT",
                        target_aggregate_id=str(completed_project.project_id),
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=_aware_utc(2040, 3, 10, 8),
                    ),
                ),
            )
        )

        stack.create_fiscal_year.execute(
            CreateFiscalYearRequest(
                year=2040,
                start_date=date(2040, 1, 1),
                end_date=date(2040, 12, 31),
                periods=(
                    FiscalPeriodInput(
                        number=1,
                        start_date=date(2040, 1, 1),
                        end_date=date(2040, 12, 31),
                    ),
                ),
            )
        )

        stack.create_journal.execute(
            CreateJournalRequest(
                journal_number="JRN-REP001-001",
                posting_date=date(2040, 4, 1),
                description="Posted journal",
                reference=f"PROJECT:{active_project.project_id}",
                status="POSTED",
                lines=(
                    JournalLineInput(
                        account_id=UUID("00000000-0000-0000-0000-00000000CC01"),
                        side="DEBIT",
                        amount="100.00",
                    ),
                    JournalLineInput(
                        account_id=UUID("00000000-0000-0000-0000-00000000CC02"),
                        side="CREDIT",
                        amount="100.00",
                    ),
                ),
            )
        )

        stack.create_journal.execute(
            CreateJournalRequest(
                journal_number="JRN-REP001-002",
                posting_date=date(2040, 4, 2),
                description="Unposted journal",
                reference=f"PROJECT:{active_project.project_id}",
                status="DRAFT",
                lines=(
                    JournalLineInput(
                        account_id=UUID("00000000-0000-0000-0000-00000000CC01"),
                        side="DEBIT",
                        amount="80.00",
                    ),
                    JournalLineInput(
                        account_id=UUID("00000000-0000-0000-0000-00000000CC02"),
                        side="CREDIT",
                        amount="80.00",
                    ),
                ),
            )
        )

        response = stack.dashboard.execute(
            OrganizationDashboardRequest(
                organization_id=organization_id,
                organization_name="REP-001 Organization",
                organization_status="ACTIVE",
            )
        )

        assert response.organization.organization_id == organization_id
        assert response.organization.name == "REP-001 Organization"
        assert response.projects.active_projects == 1
        assert response.projects.closed_projects == 1
        assert response.projects.archived_projects == 0
        assert response.projects.total_projects == 2
        assert response.documents.total_documents == 2
        assert response.accounting.journal_count == 2
        assert response.accounting.open_fiscal_years == 1
        assert response.accounting.closed_fiscal_years == 0
        assert response.accounting.last_posted_journal == "JRN-REP001-001"
        assert response.operations.last_accounting_activity == date(2040, 4, 2)
        assert response.health_indicators.budget_coverage == 1.0
        assert response.health_indicators.accounting_status == "AT_RISK"
    finally:
        session.close()
