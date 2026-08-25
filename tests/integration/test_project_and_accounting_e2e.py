"""End-to-end business-flow tests through the real composition root.

Unlike most of the test suite (which exercises use cases against
in-memory fakes), these tests drive the actual wiring in
:mod:`mfm.composition_root` end to end against a real, on-disk SQLite
database -- the same code path the running application uses. This is
where two real integration bugs were caught that no per-unit test
could have found:

- ``CompleteProjectCreationWorkflow`` and ``ProjectAccountingWorkflow``
  were composed by earlier revisions of ``CompositionRoot`` from a
  single *shared* ``UnitOfWork`` per multi-step workflow. Several of
  the underlying use cases (``CreateProjectUseCase``,
  ``UpdateOrganizationUseCase``, ``CreateJournalUseCase``, ...) call
  ``uow.commit()`` internally, and ``AbstractUnitOfWork.commit()``
  only allows one commit per scope -- so the second step's internal
  commit always raised. Each workflow step now gets its own
  independently-scoped UnitOfWork, matching how the use cases are
  actually written (a saga of independently-committed steps, not one
  shared transaction).
- ``CompleteProjectCreationWorkflow`` never attached the
  ``BUDGET_STATUS:READY`` project reference that
  ``ProjectAccountingWorkflow`` requires before allowing any journal
  to be posted against a project -- meaning no project created
  through the normal creation workflow could ever have accounting
  entries posted to it.
"""

from __future__ import annotations

from datetime import UTC, date, datetime
from decimal import Decimal
from pathlib import Path

import pytest

from mfm.composition_root import CompositionRoot, SQLAlchemyUnitOfWork
from mfm.config.models import ApplicationConfig
from mfm.config.models import Config
from mfm.config.models import DatabaseConfig
from mfm.config.models import GuiConfig
from mfm.config.models import LoggingConfig
from mfm.domain.accounting.account_number import AccountNumber
from mfm.domain.accounting.account_type import AccountType
from mfm.domain.accounting.ledger_account import LedgerAccount
from mfm.domain.accounting.normal_balance import NormalBalance
from mfm.domain.accounting.fiscal_year import FiscalYear
from mfm.domain.organization.organization import Organization
from mfm.presentation.projects.project_viewmodels import CreateProjectCommandViewModel


@pytest.fixture(autouse=True)
def _reset_process_lifetime_uniqueness_registries() -> None:
    """Reset in-memory uniqueness registries shared across test instances.

    ``FiscalYear`` and ``Organization`` track "only one open fiscal
    year" / "unique organization number" via process-lifetime class
    attributes rather than a database query. That's fine for a single
    real application process, but multiple ``CompositionRoot``
    instances built in the same pytest process (as these tests do)
    would otherwise collide with each other's seeded records.
    """

    FiscalYear._open_year_id = None
    Organization._number_registry = {}
    try:
        yield
    finally:
        FiscalYear._open_year_id = None
        Organization._number_registry = {}


def _config(*, database_path: str) -> Config:
    return Config(
        application=ApplicationConfig(
            name="MFM Enterprise", version="0.3.0-rc1", language="da", theme="system"
        ),
        database=DatabaseConfig(provider="sqlite", path=database_path),
        logging=LoggingConfig(level="INFO", directory="logs", filename="mfm.log"),
        gui=GuiConfig(style="Fusion"),
    )


def test_create_project_through_real_workspace_succeeds(qapp, tmp_path: Path) -> None:
    """The Projects workspace's 'Create Project' action must actually work."""

    root = CompositionRoot(
        config=_config(database_path="data/database/mfm.db"), project_root=tmp_path
    )
    shell = root.build_shell()
    window = shell.main_window
    window.navigate_to("operations.projects")
    workspace = window.centralWidget().currentWidget()

    created_id = workspace._controller.create_project(
        CreateProjectCommandViewModel(
            organization_id=workspace._default_organization_id,
            organization_owner_contact_id=workspace._default_owner_contact_id,
            project_number="PRJ-E2E-001",
            project_name="End to End Test Project",
            project_start_date=datetime.now(UTC),
        )
    )

    assert created_id is not None

    from mfm.application.features.projects import ListProjectsRequest

    projects = workspace._controller._list_projects.execute(ListProjectsRequest()).projects
    assert any(p.project_name == "End to End Test Project" for p in projects)


def test_post_journal_to_project_through_real_workspace_succeeds(qapp, tmp_path: Path) -> None:
    """A project created through the normal flow must accept accounting entries."""

    root = CompositionRoot(
        config=_config(database_path="data/database/mfm.db"), project_root=tmp_path
    )
    shell = root.build_shell()
    window = shell.main_window

    window.navigate_to("operations.projects")
    project_workspace = window.centralWidget().currentWidget()
    project_id = project_workspace._controller.create_project(
        CreateProjectCommandViewModel(
            organization_id=project_workspace._default_organization_id,
            organization_owner_contact_id=project_workspace._default_owner_contact_id,
            project_number="PRJ-E2E-002",
            project_name="Accounting End to End Project",
            project_start_date=datetime.now(UTC),
        )
    )

    window.navigate_to("operations.accounting")
    accounting_workspace = window.centralWidget().currentWidget()

    session_factory = root._build_session_factory()
    uow = SQLAlchemyUnitOfWork(session_factory)
    with uow:
        debit = LedgerAccount(
            account_number=AccountNumber("1000"),
            name="Cash",
            account_type=AccountType.ASSET,
            normal_balance=NormalBalance.DEBIT,
        )
        credit = LedgerAccount(
            account_number=AccountNumber("3000"),
            name="Revenue",
            account_type=AccountType.LIABILITY,
            normal_balance=NormalBalance.CREDIT,
        )
        uow.ledger_account_repository.add(debit)
        uow.ledger_account_repository.add(credit)
        uow.session.commit()
        debit_id, credit_id = debit.id, credit.id

    from mfm.application.features.onboarding.project_accounting_feature import (
        ProjectAccountingRequest,
    )

    response = accounting_workspace._controller._project_accounting_workflow.execute(
        ProjectAccountingRequest(
            project_id=project_id,
            journal_number="J-E2E-001",
            posting_date=date.today(),
            transaction_description="End to end test posting",
            debit_account_id=debit_id,
            credit_account_id=credit_id,
            amount=Decimal("100.00"),
        )
    )

    assert response.journal_status == "POSTED"

    from mfm.application.features.accounting import ListJournalsRequest

    journals = accounting_workspace._controller._list_journals.execute(
        ListJournalsRequest()
    ).journals
    assert any(j.journal_number == "J-E2E-001" for j in journals)


def test_setup_fee_schedule_through_real_workspace_persists_across_sessions(
    qapp, tmp_path: Path
) -> None:
    """Fee schedule setup must actually persist (the old repo silently didn't)."""

    root = CompositionRoot(
        config=_config(database_path="data/database/mfm.db"), project_root=tmp_path
    )
    shell = root.build_shell()
    window = shell.main_window

    window.navigate_to("operations.memberships")
    membership_workspace = window.centralWidget().currentWidget()

    from mfm.application.features.membership_type import (
        CreateMembershipTypeFeature,
        CreateMembershipTypeRequest,
    )

    session_factory = root._build_session_factory()
    uow = SQLAlchemyUnitOfWork(session_factory)
    with uow:
        membership_type = CreateMembershipTypeFeature(unit_of_work=uow).execute(
            CreateMembershipTypeRequest(code="STD", name="Standard")
        ).membership_type
        uow.commit()

    window.navigate_to("operations.membership-billing")
    billing_workspace = window.centralWidget().currentWidget()

    from mfm.presentation.membership_billing.membership_billing_viewmodels import (
        SetupFeeScheduleCommandViewModel,
    )

    billing_workspace._controller.setup_fee_schedule(
        SetupFeeScheduleCommandViewModel(
            membership_type_id=membership_type.membership_type_id,
            membership_type_code="STD",
            membership_type_name="Standard",
            amount="250.00",
            currency="DKK",
            due_days=30,
        )
    )

    # Verify persistence with a brand new session, not the one that wrote it --
    # this is exactly what the old process-lifetime-dict repository would fail.
    fresh_uow = SQLAlchemyUnitOfWork(root._build_session_factory())
    with fresh_uow:
        profiles = fresh_uow.membership_billing_repository.list()

    assert len(profiles) == 1
    assert profiles[0].fee_schedule.membership_fee.amount == Decimal("250.00")


def test_run_billing_through_real_workspaces_creates_invoice_and_journal(
    qapp, tmp_path: Path
) -> None:
    """The full billing chain: member -> contingent plan -> fee schedule -> run billing.

    Proves the real gap this closed: previously there was no working
    ContingentRepository.get_active_for_membership_type, no Invoice
    persistence at all, and no FiscalYearRepository.ensure_posting_allowed
    -- so AnnualContingentGenerationFeature could never actually run.
    """

    root = CompositionRoot(
        config=_config(database_path="data/database/mfm.db"), project_root=tmp_path
    )
    shell = root.build_shell()
    window = shell.main_window

    from mfm.application.features.membership_type import (
        CreateMembershipTypeFeature,
        CreateMembershipTypeRequest,
    )

    session_factory = root._build_session_factory()
    uow = SQLAlchemyUnitOfWork(session_factory)
    with uow:
        membership_type = CreateMembershipTypeFeature(unit_of_work=uow).execute(
            CreateMembershipTypeRequest(code="STD", name="Standard")
        ).membership_type
        uow.commit()

    window.navigate_to("operations.memberships")
    membership_workspace = window.centralWidget().currentWidget()

    from mfm.presentation.memberships.membership_viewmodels import (
        CreateMemberCommandViewModel,
        RegisterMembershipCommandViewModel,
    )

    member_id = membership_workspace._controller.create_member(
        CreateMemberCommandViewModel(
            contact_number="C-BILL-E2E",
            member_number="M-BILL-E2E",
            first_name="Billing",
            last_name="E2E",
            join_date=date.today(),
        )
    )
    membership_workspace._controller.register_membership(
        RegisterMembershipCommandViewModel(
            member_id=member_id, membership_type_id=membership_type.membership_type_id
        )
    )

    from mfm.domain.contingent.billing_period import BillingPeriod
    from mfm.domain.contingent.contingent_plan import ContingentPlan
    from mfm.domain.contingent.currency import Currency as ContingentCurrency
    from mfm.domain.contingent.invoice_rule import InvoiceRule
    from mfm.domain.contingent.money import Money as ContingentMoney
    from mfm.domain.membership.membership_type import MembershipType as DomainMembershipType

    uow2 = SQLAlchemyUnitOfWork(session_factory)
    with uow2:
        domain_membership_type = DomainMembershipType(
            id=membership_type.membership_type_id,
            code=membership_type.code,
            name=membership_type.name,
        )
        uow2.contingent_repository.add(
            ContingentPlan(
                membership_type=domain_membership_type,
                price=ContingentMoney(amount=Decimal("250.00"), currency=ContingentCurrency.DKK),
                invoice_rule=InvoiceRule(billing_period=BillingPeriod.YEARLY, due_days=30),
                valid_from=date(date.today().year, 1, 1),
            )
        )
        uow2.commit()

    window.navigate_to("operations.membership-billing")
    billing_workspace = window.centralWidget().currentWidget()

    from mfm.presentation.membership_billing.membership_billing_viewmodels import (
        RunBillingCommandViewModel,
        SetupFeeScheduleCommandViewModel,
    )

    billing_workspace._controller.setup_fee_schedule(
        SetupFeeScheduleCommandViewModel(
            membership_type_id=membership_type.membership_type_id,
            membership_type_code=membership_type.code,
            membership_type_name=membership_type.name,
            amount="250.00",
            currency="DKK",
            due_days=30,
        )
    )

    result = billing_workspace._controller.run_billing(
        RunBillingCommandViewModel(
            membership_type_id=membership_type.membership_type_id,
            fiscal_year=date.today().year,
            billing_date=date.today(),
            dry_run=False,
        )
    )

    assert result.processed == 1
    assert result.invoices_created == 1

    fresh_uow = SQLAlchemyUnitOfWork(root._build_session_factory())
    with fresh_uow:
        invoices = fresh_uow.invoice_repository.list_for_member(member_id)

    assert len(invoices) == 1
    assert invoices[0].lines[0].unit_price.amount == Decimal("250.00")
