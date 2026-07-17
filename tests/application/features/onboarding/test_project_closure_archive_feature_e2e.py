from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from uuid import uuid4

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import mfm.database.models.external_reference_model  # noqa: F401
import mfm.database.models.project_activity_model  # noqa: F401
import mfm.database.models.project_assignment_model  # noqa: F401
import mfm.database.models.project_milestone_model  # noqa: F401
import mfm.database.models.project_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.accounting.create_fiscal_year import CreateFiscalYearUseCase
from mfm.application.accounting.create_journal import CreateJournalUseCase
from mfm.application.accounting.create_ledger_account import CreateLedgerAccountUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.post_journal import PostJournalUseCase
from mfm.application.accounting.search_journals import SearchJournalsUseCase
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.features.accounting import CreateFiscalYearFeature
from mfm.application.features.accounting import CreateFiscalYearRequest
from mfm.application.features.accounting import FiscalPeriodInput
from mfm.application.features.accounting import ListFiscalYearsFeature
from mfm.application.features.accounting import SearchJournalsFeature
from mfm.application.features.accounting.create_journal_feature import CreateJournalFeature
from mfm.application.features.accounting.create_journal_feature import CreateJournalRequest
from mfm.application.features.accounting.create_journal_feature import JournalLineInput
from mfm.application.features.accounting.create_ledger_account_feature import (
    CreateLedgerAccountFeature,
)
from mfm.application.features.accounting.create_ledger_account_feature import (
    CreateLedgerAccountRequest,
)
from mfm.application.features.accounting.post_journal_feature import PostJournalFeature
from mfm.application.features.accounting.post_journal_feature import PostJournalRequest
from mfm.application.features.documents import CreateDocumentFeature
from mfm.application.features.documents import CreateDocumentRequest
from mfm.application.features.documents import DocumentReferenceInput
from mfm.application.features.documents import DocumentVersionInput
from mfm.application.features.documents import ListDocumentsFeature
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.onboarding.project_closure_archive_feature import (
    ProjectClosureArchiveFeature,
)
from mfm.application.features.onboarding.project_closure_archive_feature import (
    ProjectClosureArchiveRequest,
)
from mfm.application.features.projects import ArchiveProjectFeature
from mfm.application.features.projects import CreateProjectFeature
from mfm.application.features.projects import CreateProjectRequest
from mfm.application.features.projects import ExternalReferenceInput
from mfm.application.features.projects import GetProjectFeature
from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import UpdateProjectFeature
from mfm.application.features.projects import UpdateProjectRequest
from mfm.application.projects.archive_project import ArchiveProjectUseCase
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.projects.update_project import UpdateProjectUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.workflows.project_closure_archive_workflow import (
    ProjectClosureArchiveWorkflow,
)
from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteFiscalYearRepository,
)
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteJournalRepository,
)
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteLedgerAccountRepository,
)
from mfm.infrastructure.persistence.documents.sqlite_document_repository import (
    SQLiteDocumentRepository,
)
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteProjectClosureArchiveUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.project_repository = SQLiteProjectRepository(self._persistence_uow)
        self.document_repository = SQLiteDocumentRepository(self._persistence_uow)
        self.journal_repository = SQLiteJournalRepository(self._persistence_uow)
        self.fiscal_year_repository = SQLiteFiscalYearRepository(self._persistence_uow)
        self.ledger_account_repository = SQLiteLedgerAccountRepository(self._persistence_uow)

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
    get_project: GetProjectFeature
    update_project: UpdateProjectFeature
    archive_project: ArchiveProjectFeature
    create_document: CreateDocumentFeature
    list_documents: ListDocumentsFeature
    create_fiscal_year: CreateFiscalYearFeature
    create_ledger_account: CreateLedgerAccountFeature
    create_journal: CreateJournalFeature
    post_journal: PostJournalFeature
    search_journals: SearchJournalsFeature
    list_fiscal_years: ListFiscalYearsFeature


@pytest.fixture(autouse=True)
def _clear_class_state() -> None:
    LedgerAccount._registered_numbers.clear()
    FiscalYear._open_year_id = None
    try:
        yield
    finally:
        LedgerAccount._registered_numbers.clear()
        FiscalYear._open_year_id = None


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "project_closure_archive_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_stack(session: Session) -> _FeatureStack:
    uow = SQLiteProjectClosureArchiveUnitOfWork(session)

    return _FeatureStack(
        create_project=CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow)),
        get_project=GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow)),
        update_project=UpdateProjectFeature(service=UpdateProjectUseCase(unit_of_work=uow)),
        archive_project=ArchiveProjectFeature(service=ArchiveProjectUseCase(unit_of_work=uow)),
        create_document=CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow)),
        list_documents=ListDocumentsFeature(service=ListDocumentsUseCase(unit_of_work=uow)),
        create_fiscal_year=CreateFiscalYearFeature(service=CreateFiscalYearUseCase(unit_of_work=uow)),
        create_ledger_account=CreateLedgerAccountFeature(
            service=CreateLedgerAccountUseCase(unit_of_work=uow)
        ),
        create_journal=CreateJournalFeature(service=CreateJournalUseCase(unit_of_work=uow)),
        post_journal=PostJournalFeature(service=PostJournalUseCase(unit_of_work=uow)),
        search_journals=SearchJournalsFeature(service=SearchJournalsUseCase(unit_of_work=uow)),
        list_fiscal_years=ListFiscalYearsFeature(service=ListFiscalYearsUseCase(unit_of_work=uow)),
    )


def test_project_closure_archive_e2e(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_stack(session)

        created_project = stack.create_project.execute(
            CreateProjectRequest(
                project_number="PRJ-WF006-001",
                project_name="WF-006 Project",
                status="ACTIVE",
                priority="HIGH",
                created_at=datetime(2041, 1, 2, 8, 0, tzinfo=UTC),
            )
        )

        organization_id = uuid4()
        stack.update_project.execute(
            UpdateProjectRequest(
                project_id=created_project.project.project_id,
                references=(
                    ExternalReferenceInput(
                        reference_type="ORGANISATION",
                        external_id=organization_id,
                        description="Owning organization",
                        created_at=datetime.now(UTC),
                    ),
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=uuid4(),
                        description="BUDGET_RECONCILIATION:COMPLETED",
                        created_at=datetime.now(UTC),
                    ),
                ),
                updated_at=datetime.now(UTC),
            )
        )

        stack.create_document.execute(
            CreateDocumentRequest(
                document_number="DOC-WF006-001",
                document_title="Completion Report",
                document_type="PROJECT_REPORT",
                status="ACTIVE",
                created_at=datetime.now(UTC),
                versions=(
                    DocumentVersionInput(
                        version_number=1,
                        storage_key="docs/completion-report-v1",
                        created_at=datetime.now(UTC),
                    ),
                ),
                references=(
                    DocumentReferenceInput(
                        target_capability="PROJECTS",
                        target_aggregate_type="PROJECT",
                        target_aggregate_id=str(created_project.project.project_id),
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=datetime.now(UTC),
                        description="Required document",
                    ),
                ),
            )
        )

        stack.create_fiscal_year.execute(
            CreateFiscalYearRequest(
                year=2041,
                start_date=date(2041, 1, 1),
                end_date=date(2041, 12, 31),
                periods=(
                    FiscalPeriodInput(
                        number=1,
                        start_date=date(2041, 1, 1),
                        end_date=date(2041, 12, 31),
                    ),
                ),
            )
        )

        debit_account = stack.create_ledger_account.execute(
            CreateLedgerAccountRequest(
                account_number="1300-PROJ-AR",
                name="Project Receivable",
                account_type="ASSET",
                normal_balance="DEBIT",
            )
        )
        credit_account = stack.create_ledger_account.execute(
            CreateLedgerAccountRequest(
                account_number="4300-PROJ-REV",
                name="Project Revenue",
                account_type="INCOME",
                normal_balance="CREDIT",
            )
        )

        created_journal = stack.create_journal.execute(
            CreateJournalRequest(
                journal_number="JRN-WF006-001",
                posting_date=date(2041, 6, 15),
                description="WF-006 posted journal",
                reference=f"PROJECT:{created_project.project.project_id}",
                lines=(
                    JournalLineInput(
                        account_id=debit_account.account.account_id,
                        side="DEBIT",
                        amount=Decimal("500.00"),
                    ),
                    JournalLineInput(
                        account_id=credit_account.account.account_id,
                        side="CREDIT",
                        amount=Decimal("500.00"),
                    ),
                ),
            )
        )
        stack.post_journal.execute(
            PostJournalRequest(journal_id=created_journal.journal.journal_id)
        )

        workflow = ProjectClosureArchiveWorkflow(
            get_project_feature=stack.get_project,
            update_project_feature=stack.update_project,
            archive_project_feature=stack.archive_project,
            list_documents_feature=stack.list_documents,
            create_document_feature=stack.create_document,
            search_journals_feature=stack.search_journals,
            list_fiscal_years_feature=stack.list_fiscal_years,
        )
        feature = ProjectClosureArchiveFeature(service=workflow)

        response = feature.execute(
            ProjectClosureArchiveRequest(project_id=created_project.project.project_id)
        )

        assert response.project_id == created_project.project.project_id
        assert response.project_status == "ARCHIVED"
        assert response.closure_status == "CLOSED"
        assert response.completed_steps == (
            "STEP-001",
            "STEP-002",
            "STEP-003",
            "STEP-004",
            "STEP-005",
            "STEP-006",
            "STEP-007",
            "STEP-008",
        )

        archived_project = stack.get_project.execute(
            GetProjectRequest(project_id=response.project_id)
        ).project
        assert archived_project.status == "ARCHIVED"
        assert any(
            ref.reference_type == "DOCUMENT"
            and ref.external_id == response.archive_manifest_id
            and (ref.description or "").strip().upper() == "PROJECT_ARCHIVE_MANIFEST"
            for ref in archived_project.references
        )
        assert any(
            ref.reference_type == "DOCUMENT"
            and (ref.description or "").strip().upper() == "PROJECT_CLOSURE_STATUS:CLOSED"
            for ref in archived_project.references
        )

        documents = stack.list_documents.execute(ListDocumentsRequest()).documents
        manifest = next(item for item in documents if item.document_id == response.archive_manifest_id)
        assert manifest.document_type == "PROJECT_ARCHIVE_MANIFEST"

        manifest_caps = {ref.target_capability for ref in manifest.references}
        assert "PROJECTS" in manifest_caps
        assert "ORGANIZATION" in manifest_caps
        assert "DOCUMENTS" in manifest_caps
        assert "ACCOUNTING" in manifest_caps
        assert "AUDIT" in manifest_caps
    finally:
        session.close()
