from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import mfm.database.models  # noqa: F401
import mfm.database.models.asset_location_model  # noqa: F401
import mfm.database.models.asset_model  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.accounting.create_fiscal_year import CreateFiscalYearUseCase
from mfm.application.accounting.create_ledger_account import CreateLedgerAccountUseCase
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.list_ledger_accounts import ListLedgerAccountsUseCase
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.features.accounting import CreateFiscalYearFeature
from mfm.application.features.accounting import CreateLedgerAccountFeature
from mfm.application.features.accounting import ListFiscalYearsFeature
from mfm.application.features.accounting import ListLedgerAccountsFeature
from mfm.application.features.documents import CreateDocumentFeature
from mfm.application.features.documents import ListDocumentsFeature
from mfm.application.features.onboarding import CompleteOrganizationOnboardingFeature
from mfm.application.features.onboarding import CompleteOrganizationOnboardingRequest
from mfm.application.features.organization import CreateOrganizationFeature
from mfm.application.features.organization import UpdateOrganizationFeature
from mfm.application.organization.create_organization import CreateOrganizationUseCase
from mfm.application.organization.update_organization import UpdateOrganizationUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.workflows.complete_organization_onboarding_workflow import (
    CompleteOrganizationOnboardingWorkflow,
)
from mfm.database.models.base_model import BaseModel
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_type import OrganizationType
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteFiscalYearRepository,
)
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteLedgerAccountRepository,
)
from mfm.infrastructure.persistence.documents.sqlite_document_repository import (
    SQLiteDocumentRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_organization_repository import (
    SQLiteOrganizationRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteOnboardingApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)

        self.organization_repository = SQLiteOrganizationRepository(self._persistence_uow)
        self.document_repository = SQLiteDocumentRepository(self._persistence_uow)
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
    create_organization: CreateOrganizationFeature
    update_organization: UpdateOrganizationFeature
    create_document: CreateDocumentFeature
    list_documents: ListDocumentsFeature
    create_fiscal_year: CreateFiscalYearFeature
    list_fiscal_years: ListFiscalYearsFeature
    create_ledger_account: CreateLedgerAccountFeature
    list_ledger_accounts: ListLedgerAccountsFeature


@pytest.fixture(autouse=True)
def _clear_class_state() -> None:
    Organization._clear_registry_for_tests()
    LedgerAccount._registered_numbers.clear()
    FiscalYear._open_year_id = None
    try:
        yield
    finally:
        Organization._clear_registry_for_tests()
        LedgerAccount._registered_numbers.clear()
        FiscalYear._open_year_id = None


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "onboarding_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

    try:
        yield factory
    finally:
        engine.dispose()


def _build_stack(session: Session) -> _FeatureStack:
    dispatcher = DomainEventDispatcher()
    uow = SQLiteOnboardingApplicationUnitOfWork(session)

    return _FeatureStack(
        create_organization=CreateOrganizationFeature(
            service=CreateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)
        ),
        update_organization=UpdateOrganizationFeature(
            service=UpdateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)
        ),
        create_document=CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow)),
        list_documents=ListDocumentsFeature(service=ListDocumentsUseCase(unit_of_work=uow)),
        create_fiscal_year=CreateFiscalYearFeature(service=CreateFiscalYearUseCase(unit_of_work=uow)),
        list_fiscal_years=ListFiscalYearsFeature(service=ListFiscalYearsUseCase(unit_of_work=uow)),
        create_ledger_account=CreateLedgerAccountFeature(
            service=CreateLedgerAccountUseCase(unit_of_work=uow)
        ),
        list_ledger_accounts=ListLedgerAccountsFeature(
            service=ListLedgerAccountsUseCase(unit_of_work=uow)
        ),
    )


def test_complete_organization_onboarding_e2e(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_stack(session)
        workflow = CompleteOrganizationOnboardingWorkflow(
            create_organization_feature=stack.create_organization,
            update_organization_feature=stack.update_organization,
            create_document_feature=stack.create_document,
            list_documents_feature=stack.list_documents,
            create_fiscal_year_feature=stack.create_fiscal_year,
            list_fiscal_years_feature=stack.list_fiscal_years,
            create_ledger_account_feature=stack.create_ledger_account,
            list_ledger_accounts_feature=stack.list_ledger_accounts,
        )
        feature = CompleteOrganizationOnboardingFeature(service=workflow)

        response = feature.execute(
            CompleteOrganizationOnboardingRequest(
                organization_number="ORG-WF001-001",
                organization_name="WF-001 Organization",
                organization_type=OrganizationType.ASSOCIATION,
                fiscal_year=2035,
            )
        )

        assert response.organization_status == "ACTIVE"
        assert response.completed_steps == (
            "STEP-001",
            "STEP-002",
            "STEP-003",
            "STEP-004",
            "STEP-005",
            "STEP-006",
            "STEP-007",
        )
        assert len(response.ledger_account_ids) == 6
    finally:
        session.close()
