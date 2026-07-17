from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
from decimal import Decimal
from pathlib import Path

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
from mfm.application.accounting.get_journal import GetJournalUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.post_journal import PostJournalUseCase
from mfm.application.features.accounting import CreateFiscalYearFeature
from mfm.application.features.accounting import CreateFiscalYearRequest
from mfm.application.features.accounting import CreateLedgerAccountFeature
from mfm.application.features.accounting import CreateLedgerAccountRequest
from mfm.application.features.accounting import FiscalPeriodInput
from mfm.application.features.accounting import ListFiscalYearsFeature
from mfm.application.features.accounting import PostJournalFeature
from mfm.application.features.accounting.create_journal_feature import CreateJournalFeature
from mfm.application.features.accounting.get_journal_feature import GetJournalFeature
from mfm.application.features.accounting.get_journal_feature import GetJournalRequest
from mfm.application.features.onboarding.project_accounting_feature import (
    ProjectAccountingFeature,
)
from mfm.application.features.onboarding.project_accounting_feature import (
    ProjectAccountingRequest,
)
from mfm.application.features.projects import CreateProjectFeature
from mfm.application.features.projects import CreateProjectRequest
from mfm.application.features.projects import ExternalReferenceInput
from mfm.application.features.projects import GetProjectFeature
from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import UpdateProjectFeature
from mfm.application.features.projects import UpdateProjectRequest
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.projects.update_project import UpdateProjectUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.workflows.project_accounting_workflow import ProjectAccountingWorkflow
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
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteProjectAccountingUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.project_repository = SQLiteProjectRepository(self._persistence_uow)
        self.fiscal_year_repository = SQLiteFiscalYearRepository(self._persistence_uow)
        self.ledger_account_repository = SQLiteLedgerAccountRepository(self._persistence_uow)
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
    get_project: GetProjectFeature
    update_project: UpdateProjectFeature
    create_fiscal_year: CreateFiscalYearFeature
    create_ledger_account: CreateLedgerAccountFeature
    create_journal: CreateJournalFeature
    list_fiscal_years: ListFiscalYearsFeature
    post_journal: PostJournalFeature
    get_journal: GetJournalFeature


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
    db_path = tmp_path / "project_accounting_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_stack(session: Session) -> _FeatureStack:
    uow = SQLiteProjectAccountingUnitOfWork(session)

    return _FeatureStack(
        create_project=CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow)),
        get_project=GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow)),
        update_project=UpdateProjectFeature(service=UpdateProjectUseCase(unit_of_work=uow)),
        create_fiscal_year=CreateFiscalYearFeature(service=CreateFiscalYearUseCase(unit_of_work=uow)),
        create_ledger_account=CreateLedgerAccountFeature(
            service=CreateLedgerAccountUseCase(unit_of_work=uow)
        ),
        create_journal=CreateJournalFeature(service=CreateJournalUseCase(unit_of_work=uow)),
        list_fiscal_years=ListFiscalYearsFeature(service=ListFiscalYearsUseCase(unit_of_work=uow)),
        post_journal=PostJournalFeature(service=PostJournalUseCase(unit_of_work=uow)),
        get_journal=GetJournalFeature(service=GetJournalUseCase(unit_of_work=uow)),
    )


def test_project_accounting_e2e(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_stack(session)

        created_project = stack.create_project.execute(
            CreateProjectRequest(
                project_number="PRJ-WF005-001",
                project_name="WF-005 Project",
                status="ACTIVE",
                priority="HIGH",
                created_at=datetime(2040, 1, 2, 8, 0, tzinfo=UTC),
            )
        )

        stack.update_project.execute(
            UpdateProjectRequest(
                project_id=created_project.project.project_id,
                references=(
                    ExternalReferenceInput(
                        reference_type="DOCUMENT",
                        external_id=created_project.project.project_id,
                        description="BUDGET_STATUS:READY",
                        created_at=datetime.now(UTC),
                    ),
                ),
                updated_at=datetime.now(UTC),
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

        workflow = ProjectAccountingWorkflow(
            get_project_feature=stack.get_project,
            update_project_feature=stack.update_project,
            create_journal_feature=stack.create_journal,
            list_fiscal_years_feature=stack.list_fiscal_years,
            post_journal_feature=stack.post_journal,
            get_journal_feature=stack.get_journal,
        )
        feature = ProjectAccountingFeature(service=workflow)

        response = feature.execute(
            ProjectAccountingRequest(
                project_id=created_project.project.project_id,
                journal_number="JRN-WF005-001",
                posting_date=date(2040, 6, 15),
                transaction_description="WF-005 transaction",
                debit_account_id=debit_account.account.account_id,
                credit_account_id=credit_account.account.account_id,
                amount=Decimal("250.00"),
                transaction_reference="TXN-WF005-001",
            )
        )

        assert response.project_id == created_project.project.project_id
        assert response.journal_number == "JRN-WF005-001"
        assert response.journal_status == "POSTED"
        assert response.completed_steps == (
            "STEP-001",
            "STEP-002",
            "STEP-003",
            "STEP-004",
            "STEP-005",
            "STEP-006",
            "STEP-007",
        )

        journal = stack.get_journal.execute(
            GetJournalRequest(journal_id=response.journal_id)
        ).journal
        assert journal.status == "POSTED"
        assert journal.reference is not None
        assert f"PROJECT:{created_project.project.project_id}" in journal.reference

        persisted_project = stack.get_project.execute(
            GetProjectRequest(project_id=response.project_id)
        ).project
        assert any(
            ref.reference_type == "DOCUMENT"
            and ref.external_id == response.journal_id
            and (ref.description or "").strip().upper() == "PROJECT_ACCOUNTING_JOURNAL:JRN-WF005-001"
            for ref in persisted_project.references
        )
    finally:
        session.close()
