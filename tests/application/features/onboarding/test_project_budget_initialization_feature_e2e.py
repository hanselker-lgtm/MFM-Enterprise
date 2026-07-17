from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import date
from datetime import datetime
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
from mfm.application.accounting.create_ledger_account import CreateLedgerAccountUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.list_ledger_accounts import ListLedgerAccountsUseCase
from mfm.application.features.accounting import CreateFiscalYearFeature
from mfm.application.features.accounting import CreateFiscalYearRequest
from mfm.application.features.accounting import CreateLedgerAccountFeature
from mfm.application.features.accounting import CreateLedgerAccountRequest
from mfm.application.features.accounting import FiscalPeriodInput
from mfm.application.features.accounting import ListFiscalYearsFeature
from mfm.application.features.accounting import ListLedgerAccountsFeature
from mfm.application.features.onboarding.project_budget_initialization_feature import (
    ProjectBudgetInitializationFeature,
)
from mfm.application.features.onboarding.project_budget_initialization_feature import (
    ProjectBudgetInitializationRequest,
)
from mfm.application.features.projects import CreateProjectFeature
from mfm.application.features.projects import CreateProjectRequest
from mfm.application.features.projects import GetProjectFeature
from mfm.application.features.projects import GetProjectRequest
from mfm.application.features.projects import UpdateProjectFeature
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.projects.update_project import UpdateProjectUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.workflows.project_budget_initialization_workflow import (
    ProjectBudgetInitializationWorkflow,
)
from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteFiscalYearRepository,
)
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteLedgerAccountRepository,
)
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteProjectBudgetInitializationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.project_repository = SQLiteProjectRepository(self._persistence_uow)
        self.fiscal_year_repository = SQLiteFiscalYearRepository(self._persistence_uow)
        self.ledger_account_repository = SQLiteLedgerAccountRepository(self._persistence_uow)

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

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
    list_fiscal_years: ListFiscalYearsFeature
    create_ledger_account: CreateLedgerAccountFeature
    list_ledger_accounts: ListLedgerAccountsFeature


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
    db_path = tmp_path / "project_budget_initialization_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_stack(session: Session) -> _FeatureStack:
    uow = SQLiteProjectBudgetInitializationUnitOfWork(session)

    return _FeatureStack(
        create_project=CreateProjectFeature(service=CreateProjectUseCase(unit_of_work=uow)),
        get_project=GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow)),
        update_project=UpdateProjectFeature(service=UpdateProjectUseCase(unit_of_work=uow)),
        create_fiscal_year=CreateFiscalYearFeature(service=CreateFiscalYearUseCase(unit_of_work=uow)),
        list_fiscal_years=ListFiscalYearsFeature(service=ListFiscalYearsUseCase(unit_of_work=uow)),
        create_ledger_account=CreateLedgerAccountFeature(
            service=CreateLedgerAccountUseCase(unit_of_work=uow)
        ),
        list_ledger_accounts=ListLedgerAccountsFeature(
            service=ListLedgerAccountsUseCase(unit_of_work=uow)
        ),
    )


def test_project_budget_initialization_e2e(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_stack(session)

        created_project = stack.create_project.execute(
            CreateProjectRequest(
                project_number="PRJ-WF004-001",
                project_name="WF-004 Project",
                status="ACTIVE",
                priority="HIGH",
                created_at=datetime(2039, 1, 2, 8, 0, tzinfo=UTC),
            )
        )

        stack.create_fiscal_year.execute(
            CreateFiscalYearRequest(
                year=2039,
                start_date=date(2039, 1, 1),
                end_date=date(2039, 12, 31),
                periods=(
                    FiscalPeriodInput(
                        number=1,
                        start_date=date(2039, 1, 1),
                        end_date=date(2039, 12, 31),
                    ),
                ),
            )
        )

        stack.create_ledger_account.execute(
            CreateLedgerAccountRequest(
                account_number="5000-EXP",
                name="Operating Expense",
                account_type="EXPENSE",
                normal_balance="DEBIT",
            )
        )

        workflow = ProjectBudgetInitializationWorkflow(
            get_project_feature=stack.get_project,
            update_project_feature=stack.update_project,
            list_fiscal_years_feature=stack.list_fiscal_years,
            list_ledger_accounts_feature=stack.list_ledger_accounts,
        )
        feature = ProjectBudgetInitializationFeature(service=workflow)

        response = feature.execute(
            ProjectBudgetInitializationRequest(
                project_id=created_project.project.project_id,
                fiscal_year=2039,
            )
        )

        assert response.project_id == created_project.project.project_id
        assert response.budget_status == "READY"
        assert len(response.budget_category_ids) == 5
        assert response.completed_steps == (
            "STEP-001",
            "STEP-002",
            "STEP-003",
            "STEP-004",
            "STEP-005",
            "STEP-006",
            "STEP-007",
        )

        persisted_project = stack.get_project.execute(
            GetProjectRequest(project_id=response.project_id)
        ).project

        reference_keys = {
            (ref.reference_type, ref.external_id, (ref.description or "").strip().upper())
            for ref in persisted_project.references
        }
        assert (
            "DOCUMENT",
            response.budget_container_id,
            "BUDGET_CONTAINER:PROJECT_BUDGET",
        ) in reference_keys
        assert (
            "DOCUMENT",
            response.fiscal_year_id,
            "BUDGET_FISCAL_YEAR:FY2039",
        ) in reference_keys
        for category_id in response.budget_category_ids:
            assert any(
                ref_type == "DOCUMENT"
                and external_id == category_id
                and description.startswith("BUDGET_CATEGORY:")
                for ref_type, external_id, description in reference_keys
            )

        status_refs = [
            ref
            for ref in persisted_project.references
            if ref.reference_type == "DOCUMENT"
            and (ref.description or "").strip().upper() == "BUDGET_STATUS:READY"
        ]
        assert status_refs
        assert status_refs[-1].description == "BUDGET_STATUS:READY"
    finally:
        session.close()
