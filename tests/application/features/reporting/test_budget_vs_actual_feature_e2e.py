from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
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
from mfm.application.accounting.get_journal import GetJournalUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.search_journals import SearchJournalsUseCase
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.features.accounting import CreateFiscalYearFeature
from mfm.application.features.accounting import CreateFiscalYearRequest
from mfm.application.features.accounting import CreateJournalFeature
from mfm.application.features.accounting import CreateJournalRequest
from mfm.application.features.accounting import FiscalPeriodInput
from mfm.application.features.accounting import JournalLineInput
from mfm.application.features.accounting import GetJournalFeature
from mfm.application.features.accounting import ListFiscalYearsFeature
from mfm.application.features.accounting import SearchJournalsFeature
from mfm.application.features.documents import CreateDocumentFeature
from mfm.application.features.documents import CreateDocumentRequest
from mfm.application.features.documents import DocumentReferenceInput
from mfm.application.features.documents import DocumentVersionInput
from mfm.application.features.projects import CreateProjectFeature
from mfm.application.features.projects import CreateProjectRequest
from mfm.application.features.projects import ExternalReferenceInput
from mfm.application.features.projects import GetProjectFeature
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.features.reporting import BudgetVsActualFeature
from mfm.application.features.reporting import BudgetVsActualRequest
from mfm.application.reporting.budget_vs_actual_service import BudgetVsActualService
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
    create_document: CreateDocumentFeature
    create_fiscal_year: CreateFiscalYearFeature
    create_journal: CreateJournalFeature
    budget_vs_actual: BudgetVsActualFeature


@pytest.fixture(autouse=True)
def _reset_fiscal_year_state() -> None:
    FiscalYear._open_year_id = None
    try:
        yield
    finally:
        FiscalYear._open_year_id = None


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "budget_vs_actual_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_stack(session: Session) -> _FeatureStack:
    uow = SQLiteReportingUnitOfWork(session)

    get_project = GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow))
    search_journals = SearchJournalsFeature(service=SearchJournalsUseCase(unit_of_work=uow))
    list_fiscal_years = ListFiscalYearsFeature(service=ListFiscalYearsUseCase(unit_of_work=uow))

    report_service = BudgetVsActualService(
        get_project_feature=get_project,
        search_journals_feature=search_journals,
        get_journal_feature=GetJournalFeature(service=GetJournalUseCase(unit_of_work=uow)),
        list_fiscal_years_feature=list_fiscal_years,
    )

    return _FeatureStack(
        create_project=CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow)),
        create_document=CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow)),
        create_fiscal_year=CreateFiscalYearFeature(service=CreateFiscalYearUseCase(unit_of_work=uow)),
        create_journal=CreateJournalFeature(service=CreateJournalUseCase(unit_of_work=uow)),
        budget_vs_actual=BudgetVsActualFeature(service=report_service),
    )


def _aware_utc(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, tzinfo=UTC)


def test_budget_vs_actual_feature_e2e_reports_limited_budget_confidence(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_stack(session)

        project = stack.create_project.execute(
            CreateProjectRequest(
                project_number="PRJ-REP004-001",
                project_name="REP-004 Budget Check",
                status="ACTIVE",
                references=(
                    ExternalReferenceInput(
                        reference_type="ORGANISATION",
                        external_id=UUID("00000000-0000-0000-0000-00000000AA41"),
                        description="Organization link",
                        created_at=_aware_utc(2040, 1, 2, 8),
                    ),
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=UUID("00000000-0000-0000-0000-00000000BB41"),
                        description="BUDGET_STATUS:READY",
                        created_at=_aware_utc(2040, 1, 3, 8),
                    ),
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=UUID("00000000-0000-0000-0000-00000000BB42"),
                        description="BUDGET_CATEGORY:CAPEX",
                        created_at=_aware_utc(2040, 1, 4, 8),
                    ),
                ),
                created_at=_aware_utc(2040, 1, 1, 8),
            )
        ).project

        stack.create_document.execute(
            CreateDocumentRequest(
                document_number="DOC-REP004-001",
                document_title="Budget worksheet",
                document_type="PROJECT_DOCUMENT",
                status="ACTIVE",
                created_at=_aware_utc(2040, 2, 10, 8),
                versions=(
                    DocumentVersionInput(
                        version_number=1,
                        storage_key="docs/rep004/1",
                        created_at=_aware_utc(2040, 2, 10, 8),
                    ),
                ),
                references=(
                    DocumentReferenceInput(
                        target_capability="PROJECTS",
                        target_aggregate_type="PROJECT",
                        target_aggregate_id=str(project.project_id),
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=_aware_utc(2040, 2, 10, 8),
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
                journal_number="JRN-REP004-001",
                posting_date=date(2040, 4, 1),
                description="Posted journal",
                reference=f"PROJECT:{project.project_id}",
                status="POSTED",
                lines=(
                    JournalLineInput(
                        account_id=UUID("00000000-0000-0000-0000-00000000CC41"),
                        side="DEBIT",
                        amount=Decimal("125.50"),
                    ),
                    JournalLineInput(
                        account_id=UUID("00000000-0000-0000-0000-00000000CC42"),
                        side="CREDIT",
                        amount=Decimal("125.50"),
                    ),
                ),
            )
        )

        response = stack.budget_vs_actual.execute(BudgetVsActualRequest(project_id=project.project_id))

        assert response.project.project_name == "REP-004 Budget Check"
        assert response.budget.budget_ready is True
        assert response.budget.planned_budget_total is None
        assert response.budget.budget_categories == ("CAPEX",)
        assert response.accounting.actual_total == Decimal("125.50")
        assert response.status.reporting_confidence == "LIMITED_BUDGET_METADATA"
    finally:
        session.close()
