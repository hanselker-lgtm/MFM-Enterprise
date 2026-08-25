"""Composition root: wires the real database and GUI shell together.

Prior to this module, ``Application.start()`` only initialized config
and logging and never built or showed the Qt application shell -- the
program never actually displayed a window in production, even though
the full GUI (``build_application_shell``) existed and was exercised
by tests. This module closes that gap.

Scope, deliberately bounded:

- The 4 mandatory dashboard report loaders (organization, active
  projects, project status, budget vs actual) are wired to the real
  database via ``SQLAlchemyUnitOfWork`` and the corresponding feature
  facades.
- The "About" route is wired to :mod:`mfm.presentation.about_dialog`
  with real version/build/diagnostics content instead of a
  placeholder.
- Operational data-entry workspaces (Memberships, Contact
  Communication, Membership Billing, Events, Document Archive,
  Organization Roles, Settings, Logs) are intentionally left as the
  existing placeholder pages. Wiring those is new feature work, not a
  known-gap closure, and is out of scope here.

Because this is a single-association deployment (see README), the
dashboard report loaders need a "current" organization and project to
bind to even though the underlying services are written to be
multi-tenant. On first run, if no organization/project exists yet, a
default one is seeded so the dashboards have something valid to show
instead of raising. This mirrors the existing bootstrap pattern in
``ConfigManager`` (default.toml copied to user.toml on first run).
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Callable
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from PySide6.QtWidgets import QApplication

from mfm.application.about.about_info_service import AboutInfoService
from mfm.application.features.accounting.list_fiscal_years_feature import (
    ListFiscalYearsFeature,
)
from mfm.application.features.accounting.search_journals_feature import (
    SearchJournalsFeature,
)
from mfm.application.features.documents.list_documents_feature import (
    ListDocumentsFeature,
)
from mfm.application.features.documents.create_document_feature import (
    CreateDocumentFeature,
)
from mfm.application.features.organization.update_organization_feature import (
    UpdateOrganizationFeature,
)
from mfm.application.features.projects.get_project_feature import GetProjectFeature
from mfm.application.features.projects.list_projects_feature import ListProjectsFeature
from mfm.application.features.projects.search_projects_feature import SearchProjectsFeature
from mfm.application.features.projects.create_project_feature import CreateProjectFeature
from mfm.application.features.projects.update_project_feature import UpdateProjectFeature
from mfm.application.features.reporting.budget_vs_actual_feature import (
    BudgetVsActualFeature as ReportingBudgetVsActualFeature,
)
from mfm.application.features.reporting.project_status_feature import (
    ProjectStatusFeature as ReportingProjectStatusFeature,
)
from mfm.application.accounting.list_fiscal_years import ListFiscalYearsUseCase
from mfm.application.accounting.search_journals import SearchJournalsUseCase
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.organization.update_organization import UpdateOrganizationUseCase
from mfm.application.projects.create_project import CreateProjectUseCase
from mfm.application.projects.get_project import GetProjectUseCase
from mfm.application.projects.list_projects import ListProjectsUseCase
from mfm.application.projects.search_projects import SearchProjectsUseCase
from mfm.application.projects.update_project import UpdateProjectUseCase
from mfm.application.workflows.complete_project_creation_workflow import (
    CompleteProjectCreationWorkflow,
)
from mfm.application.workflows.project_accounting_workflow import ProjectAccountingWorkflow
from mfm.application.features.accounting.create_journal_feature import CreateJournalFeature
from mfm.application.features.accounting.get_journal_feature import GetJournalFeature
from mfm.application.features.accounting.list_journals_feature import ListJournalsFeature
from mfm.application.features.accounting.post_journal_feature import PostJournalFeature
from mfm.application.features.onboarding.project_accounting_feature import (
    ProjectAccountingFeature,
)
from mfm.application.accounting.create_journal import CreateJournalUseCase
from mfm.application.accounting.get_journal import GetJournalUseCase
from mfm.application.accounting.list_journals import ListJournalsUseCase
from mfm.application.accounting.post_journal import PostJournalUseCase
from mfm.application.features.documents.get_document_feature import GetDocumentFeature
from mfm.application.features.documents.search_documents_feature import (
    SearchDocumentsFeature,
)
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionFeature,
)
from mfm.application.features.documents.archive_document_feature import (
    ArchiveDocumentFeature,
)
from mfm.application.documents.get_document import GetDocumentUseCase
from mfm.application.documents.search_documents import SearchDocumentsUseCase
from mfm.application.documents.register_document_version import (
    RegisterDocumentVersionUseCase,
)
from mfm.application.documents.archive_document import ArchiveDocumentUseCase
from mfm.application.features.members import (
    CreateMemberFeature,
    GetMemberFeature as MembersGetMemberFeature,
    ListMembersFeature,
)
from mfm.application.features.membership.manage_membership_feature import ManageMembershipFeature
from mfm.application.features.membership_billing import ListFeeSchedulesFeature
from mfm.application.features.membership_billing import ManageMembershipBillingFeature
from mfm.application.features.membership_type import (
    ListMembershipTypesFeature as MembershipTypesListFeature,
)
from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.features.annual_contingent_generation import (
    AnnualContingentGenerationFeature,
)
from mfm.application.membership.membership_management_service import MembershipManagementService
from mfm.application.membership_billing.membership_billing_service import MembershipBillingService
from mfm.application.features.organization.create_organization_feature import (
    CreateOrganizationFeature,
)
from mfm.application.features.organization.update_organization_feature import (
    UpdateOrganizationFeature as OrgUpdateOrganizationFeature,
)
from mfm.application.features.organizations import (
    CreateOrganizationStringFeature,
    GetOrganizationFeature,
    ListOrganizationsFeature as OrganizationsListFeature,
    UpdateOrganizationStringFeature,
)
from mfm.application.organization.create_organization import CreateOrganizationUseCase
from mfm.application.reporting.active_projects_service import (
    ActiveProjectsDashboardRequest,
    ActiveProjectsService,
)
from mfm.application.reporting.budget_vs_actual_service import (
    BudgetVsActualRequest,
    BudgetVsActualService,
)
from mfm.application.reporting.organization_dashboard_service import (
    OrganizationDashboardRequest,
    OrganizationDashboardService,
)
from mfm.application.reporting.project_status_service import (
    ProjectStatusRequest,
    ProjectStatusService,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.uow.sqlalchemy_unit_of_work import SQLAlchemyUnitOfWork
from mfm.database.repositories.sqlite_membership_repository import SQLiteMembershipRepository
from mfm.database.repositories.sqlite_contingent_plan_repository import (
    SQLiteContingentPlanRepository,
)
from mfm.infrastructure.persistence.accounting.sqlite_accounting_repository import (
    SQLiteFiscalYearRepository,
)
from mfm.infrastructure.persistence.finance.sqlalchemy_annual_contingent_journal_repository import (
    SqlAlchemyAnnualContingentJournalRepository,
)
from mfm.infrastructure.persistence.finance.sqlalchemy_invoice_repository import (
    SqlAlchemyInvoiceRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork as SessionUnitOfWork
from mfm.config.models import Config
from mfm.database.base import Base
from mfm.database.engine import EngineFactory
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.projects.project import Project
from mfm.domain.projects.project_name import ProjectName
from mfm.domain.projects.project_number import ProjectNumber
from mfm.domain.projects.project_status import ProjectStatus
from mfm.presentation.about_dialog import build_about_page
from mfm.presentation.application_shell import ApplicationShell
from mfm.presentation.application_shell import build_application_shell
from mfm.presentation.accounting.accounting_controller import AccountingController
from mfm.presentation.accounting.accounting_controller import AccountingNavigationCallbacks
from mfm.presentation.accounting.accounting_workspace import AccountingWorkspace
from mfm.presentation.documents.documents_controller import DocumentsController
from mfm.presentation.documents.documents_controller import DocumentsNavigationCallbacks
from mfm.presentation.documents.documents_workspace import DocumentsWorkspace
from mfm.presentation.membership_billing.membership_billing_controller import (
    MembershipBillingController,
)
from mfm.presentation.membership_billing.membership_billing_workspace import (
    MembershipBillingWorkspace,
)
from mfm.presentation.memberships.membership_controller import MembershipController
from mfm.presentation.memberships.membership_workspace import MembershipWorkspace
from mfm.presentation.organizations.organization_controller import OrganizationController
from mfm.presentation.organizations.organization_workspace import OrganizationWorkspace
from mfm.presentation.projects.project_controller import ProjectController
from mfm.presentation.projects.project_controller import ProjectNavigationCallbacks
from mfm.presentation.projects.project_workspace import ProjectWorkspace

import mfm.database.metadata  # noqa: F401  (registers ORM models on Base.metadata)


class _AnnualContingentUnitOfWork(AbstractUnitOfWork):
    """UnitOfWork tailored to AnnualContingentGenerationFeature's needs.

    That feature reads ``uow.journal_repository``, ``uow.invoice_repository``,
    ``uow.contingent_repository``, ``uow.fiscal_year_repository``, and
    ``uow.membership_repository`` by fixed attribute name. Its
    ``journal_repository`` must satisfy ``add(journal: JournalEntry)``
    -- a different aggregate from the ``Journal`` the Accounting
    workspace's own ``uow.journal_repository`` handles -- so this
    can't just reuse :class:`SQLAlchemyUnitOfWork` directly without
    the two colliding on the same attribute name.
    """

    def __init__(self, session_factory: Callable[[], Session]) -> None:
        super().__init__()
        self._session_factory = session_factory
        self._session: Session | None = None

    @property
    def session(self) -> Session:
        if self._session is None:
            raise RuntimeError("Session is not initialized; enter UnitOfWork scope first")
        return self._session

    def _start_scope(self) -> None:
        self._session = self._session_factory()
        session_uow = SessionUnitOfWork(self._session)

        self.membership_repository = SQLiteMembershipRepository(self.session)
        self.contingent_repository = SQLiteContingentPlanRepository(self.session)
        self.invoice_repository = SqlAlchemyInvoiceRepository(self.session)
        self.journal_repository = SqlAlchemyAnnualContingentJournalRepository(self.session)
        self.fiscal_year_repository = SQLiteFiscalYearRepository(session_uow)

    def _commit_impl(self) -> None:
        self.session.commit()

    def _rollback_impl(self) -> None:
        self.session.rollback()

    def _flush_impl(self) -> None:
        self.session.flush()

    def _close_impl(self) -> None:
        if self._session is None:
            return
        self._session.close()
        self._session = None


class CompositionRoot:
    """Builds the real, database-backed application shell."""

    def __init__(self, *, config: Config, project_root: Path) -> None:
        self._config = config
        self._project_root = project_root

    def build_shell(self) -> ApplicationShell:
        # A QApplication must exist before any QWidget (DashboardHost,
        # MainWindow, ...) is constructed. Tests get this for free from
        # the session-scoped `qapp` fixture; the real entrypoint did not
        # create one anywhere, which is part of why it never worked.
        application = QApplication.instance() or QApplication([])

        session_factory = self._build_session_factory()

        self._ensure_seed_data(session_factory)
        organization_id, project_id, owner_contact_id = self._resolve_current_ids(session_factory)

        report_loaders = {
            "dashboard.organization": self._organization_dashboard_loader(
                session_factory, organization_id
            ),
            "dashboard.active-projects": self._active_projects_loader(
                session_factory, organization_id
            ),
            "dashboard.project-status": self._project_status_loader(
                session_factory, project_id
            ),
            "dashboard.budget-vs-actual": self._budget_vs_actual_loader(
                session_factory, project_id
            ),
        }

        about_service = AboutInfoService(
            config=self._config, config_directory=self._config_directory()
        )
        widget_loaders = {
            "administration.about": lambda: build_about_page(
                about_info=about_service.get_about_info()
            ),
            "operations.organizations": self._organizations_workspace_loader(session_factory),
        }

        return build_application_shell(
            report_loaders=report_loaders,
            widget_loaders=widget_loaders,
            projects_workspace_loader=self._projects_workspace_loader(
                session_factory, organization_id=organization_id, owner_contact_id=owner_contact_id
            ),
            accounting_workspace_loader=self._accounting_workspace_loader(session_factory),
            documents_workspace_loader=self._documents_workspace_loader(session_factory),
            memberships_workspace_loader=self._memberships_workspace_loader(session_factory),
            membership_billing_workspace_loader=self._membership_billing_workspace_loader(
                session_factory
            ),
            application=application,
        )

    # -- database bootstrap -------------------------------------------------

    def _config_directory(self) -> Path:
        return self._project_root / "config"

    def _database_path(self) -> Path:
        path = Path(self._config.database.path)
        if not path.is_absolute():
            path = self._project_root / path
        return path

    def _build_session_factory(self) -> sessionmaker[Session]:
        database_path = self._database_path()
        database_path.parent.mkdir(parents=True, exist_ok=True)

        self._run_migrations(database_path)

        engine = EngineFactory.create(f"sqlite:///{database_path}")
        return sessionmaker(bind=engine, expire_on_commit=False)

    def _run_migrations(self, database_path: Path) -> None:
        """Bring the database schema up to date using the Alembic baseline.

        Falls back to ``Base.metadata.create_all`` only if Alembic's
        own configuration cannot be found (e.g. a stripped-down
        deployment layout) -- that keeps the app usable, but the
        supported production path is the migration history under
        ``migrations/versions``.
        """

        alembic_ini = self._project_root / "alembic.ini"
        if not alembic_ini.exists():
            Base.metadata.create_all(bind=EngineFactory.create(f"sqlite:///{database_path}"))
            return

        from alembic import command
        from alembic.config import Config as AlembicConfig

        alembic_config = AlembicConfig(str(alembic_ini))
        alembic_config.set_main_option(
            "script_location", str(self._project_root / "migrations")
        )
        alembic_config.set_main_option("sqlalchemy.url", f"sqlite:///{database_path}")
        command.upgrade(alembic_config, "head")

    def _ensure_seed_data(self, session_factory: sessionmaker[Session]) -> None:
        """Seed default organization/project/owner-contact records on first run.

        The reporting services are written for a multi-tenant model
        (organization_id / project_id required per call), but this
        deployment manages exactly one association. Rather than fail
        the dashboards on an empty database, a default organization,
        project, and owner contact are created so there is always
        something valid to report on and to bind new projects to. All
        are ordinary records and can be renamed or replaced once
        Organizations/Contacts data-entry workspaces exist.

        The owner contact is an organisation-type Contact representing
        the association itself (not a person) -- it exists so the
        "Create Project" workflow, which requires a real
        organization_owner_contact_id, has a valid one to use instead
        of a nonexistent placeholder UUID.
        """

        uow = SQLAlchemyUnitOfWork(session_factory)
        with uow:
            organizations = uow.organization_repository.list()
            if not organizations:
                from uuid import uuid4

                organization = Organization(
                    organization_number=OrganizationNumber(f"ORG-{uuid4().hex[:8].upper()}"),
                    name=self._config.application.name,
                )
                uow.organization_repository.add(organization)
            else:
                organization = organizations[0]

            projects = uow.project_repository.list()
            if not projects:
                project = Project(
                    project_number=ProjectNumber("PRJ-0001"),
                    project_name=ProjectName("General"),
                    status=ProjectStatus.ACTIVE,
                )
                uow.project_repository.add(project)

            contacts = uow.contact_repository.list()
            owner_contact = next(
                (c for c in contacts if c.contact_number == "CONTACT-ORG-0001"), None
            )
            if owner_contact is None:
                from mfm.domain.contact.contact import Contact
                from mfm.domain.contact.organisation import Organisation

                owner_contact = Contact(
                    party=Organisation(name=self._config.application.name),
                    contact_number="CONTACT-ORG-0001",
                )
                uow.contact_repository.add(owner_contact)

            fiscal_years = uow.fiscal_year_repository.list()
            current_year = date.today().year
            if not any(fy.year == current_year for fy in fiscal_years):
                from mfm.domain.accounting.exceptions import MultipleOpenFiscalYearsError
                from mfm.domain.accounting.fiscal_period import FiscalPeriod
                from mfm.domain.accounting.fiscal_year import FiscalYear
                from mfm.domain.accounting.fiscal_year_status import FiscalYearStatus

                periods = [
                    FiscalPeriod(
                        number=month,
                        start_date=date(current_year, month, 1),
                        end_date=(
                            date(current_year, month, 28)
                            if month == 2
                            else date(
                                current_year,
                                month,
                                30 if month in (4, 6, 9, 11) else 31,
                            )
                        ),
                    )
                    for month in range(1, 13)
                ]
                try:
                    fiscal_year = FiscalYear(
                        year=current_year,
                        start_date=date(current_year, 1, 1),
                        end_date=date(current_year, 12, 31),
                        periods=periods,
                    )
                except MultipleOpenFiscalYearsError:
                    # FiscalYear enforces "only one open year" via a
                    # process-lifetime class attribute, not a database
                    # query -- it can already be claimed by another
                    # CompositionRoot in this same process (e.g. tests
                    # running against different databases). This
                    # database still needs its own fiscal year record;
                    # it just can't be OPEN, so posting journals to a
                    # freshly-seeded database in that situation will
                    # need the year re-opened once the other one closes.
                    fiscal_year = FiscalYear(
                        year=current_year,
                        start_date=date(current_year, 1, 1),
                        end_date=date(current_year, 12, 31),
                        periods=periods,
                        status=FiscalYearStatus.CLOSED,
                    )
                uow.fiscal_year_repository.add(fiscal_year)

            uow.commit()

    def _resolve_current_ids(
        self, session_factory: sessionmaker[Session]
    ) -> tuple[UUID, UUID, UUID]:
        uow = SQLAlchemyUnitOfWork(session_factory)
        with uow:
            organization = uow.organization_repository.list()[0]
            project = uow.project_repository.list()[0]
            owner_contact = next(
                c
                for c in uow.contact_repository.list()
                if c.contact_number == "CONTACT-ORG-0001"
            )
            return organization.id.value, project.id.value, owner_contact.id

    # -- generic UoW-scoped feature wrapper -----------------------------

    def _scoped_feature(self, session_factory, build_feature):
        """Wrap a feature so each call opens/commits its own UnitOfWork.

        Workspace widgets are long-lived and call their features
        repeatedly in response to user actions, unlike the report
        loaders above which are single-call closures. Each call here
        gets its own short-lived transaction instead of holding one
        session open for the widget's entire lifetime.
        """

        class _Scoped:
            def execute(self, request):
                uow = SQLAlchemyUnitOfWork(session_factory)
                with uow:
                    feature = build_feature(uow)
                    result = feature.execute(request)
                    uow.session.commit()
                    return result

        return _Scoped()

    # -- Projects workspace -----------------------------------------------

    def _projects_workspace_loader(self, session_factory, *, organization_id: UUID, owner_contact_id: UUID):
        def load() -> ProjectWorkspace:
            list_projects_feature = self._scoped_feature(
                session_factory,
                lambda uow: ListProjectsFeature(service=ListProjectsUseCase(unit_of_work=uow)),
            )
            search_projects_feature = self._scoped_feature(
                session_factory,
                lambda uow: SearchProjectsFeature(
                    service=SearchProjectsUseCase(unit_of_work=uow)
                ),
            )
            get_project_feature = self._scoped_feature(
                session_factory,
                lambda uow: GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow)),
            )

            def build_project_status_service(uow):
                from mfm.application.reporting.project_status_service import (
                    ProjectStatusService,
                )

                return ProjectStatusService(
                    get_project_feature=GetProjectFeature(
                        service=GetProjectUseCase(unit_of_work=uow)
                    ),
                    list_documents_feature=ListDocumentsFeature(
                        service=ListDocumentsUseCase(unit_of_work=uow)
                    ),
                    search_journals_feature=SearchJournalsFeature(
                        service=SearchJournalsUseCase(unit_of_work=uow)
                    ),
                    list_fiscal_years_feature=ListFiscalYearsFeature(
                        service=ListFiscalYearsUseCase(unit_of_work=uow)
                    ),
                )

            project_status_feature = self._scoped_feature(
                session_factory,
                lambda uow: ReportingProjectStatusFeature(
                    service=build_project_status_service(uow)
                ),
            )

            def build_budget_vs_actual_service(uow):
                from mfm.application.accounting.get_journal import GetJournalUseCase
                from mfm.application.features.accounting.get_journal_feature import (
                    GetJournalFeature,
                )
                from mfm.application.reporting.budget_vs_actual_service import (
                    BudgetVsActualService,
                )

                return BudgetVsActualService(
                    get_project_feature=GetProjectFeature(
                        service=GetProjectUseCase(unit_of_work=uow)
                    ),
                    search_journals_feature=SearchJournalsFeature(
                        service=SearchJournalsUseCase(unit_of_work=uow)
                    ),
                    get_journal_feature=GetJournalFeature(
                        service=GetJournalUseCase(unit_of_work=uow)
                    ),
                    list_fiscal_years_feature=ListFiscalYearsFeature(
                        service=ListFiscalYearsUseCase(unit_of_work=uow)
                    ),
                )

            budget_vs_actual_feature = self._scoped_feature(
                session_factory,
                lambda uow: ReportingBudgetVsActualFeature(
                    service=build_budget_vs_actual_service(uow)
                ),
            )

            create_project_workflow_feature = CompleteProjectCreationWorkflow(
                update_organization_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: UpdateOrganizationFeature(
                        service=UpdateOrganizationUseCase(
                            unit_of_work=uow, dispatcher=DomainEventDispatcher()
                        )
                    ),
                ),
                create_project_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: CreateProjectFeature(
                        service=CreateProjectUseCase(unit_of_work=uow)
                    ),
                ),
                update_project_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: UpdateProjectFeature(
                        service=UpdateProjectUseCase(unit_of_work=uow)
                    ),
                ),
                get_project_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow)),
                ),
                create_document_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: CreateDocumentFeature(
                        service=CreateDocumentUseCase(unit_of_work=uow)
                    ),
                ),
                list_documents_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: ListDocumentsFeature(
                        service=ListDocumentsUseCase(unit_of_work=uow)
                    ),
                ),
            )

            controller = ProjectController(
                list_projects_feature=list_projects_feature,
                search_projects_feature=search_projects_feature,
                get_project_feature=get_project_feature,
                project_status_feature=project_status_feature,
                budget_vs_actual_feature=budget_vs_actual_feature,
                create_project_workflow_feature=create_project_workflow_feature,
                navigation=ProjectNavigationCallbacks(),
            )
            return ProjectWorkspace(
                controller=controller,
                default_organization_id=organization_id,
                default_owner_contact_id=owner_contact_id,
            )

        return load

    # -- Accounting workspace -----------------------------------------------

    def _accounting_workspace_loader(self, session_factory):
        def load() -> AccountingWorkspace:
            list_journals_feature = self._scoped_feature(
                session_factory,
                lambda uow: ListJournalsFeature(service=ListJournalsUseCase(unit_of_work=uow)),
            )
            search_journals_feature = self._scoped_feature(
                session_factory,
                lambda uow: SearchJournalsFeature(
                    service=SearchJournalsUseCase(unit_of_work=uow)
                ),
            )
            get_journal_feature = self._scoped_feature(
                session_factory,
                lambda uow: GetJournalFeature(service=GetJournalUseCase(unit_of_work=uow)),
            )
            post_journal_feature = self._scoped_feature(
                session_factory,
                lambda uow: PostJournalFeature(service=PostJournalUseCase(unit_of_work=uow)),
            )
            list_fiscal_years_feature = self._scoped_feature(
                session_factory,
                lambda uow: ListFiscalYearsFeature(
                    service=ListFiscalYearsUseCase(unit_of_work=uow)
                ),
            )

            project_accounting_service = ProjectAccountingWorkflow(
                get_project_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: GetProjectFeature(service=GetProjectUseCase(unit_of_work=uow)),
                ),
                update_project_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: UpdateProjectFeature(
                        service=UpdateProjectUseCase(unit_of_work=uow)
                    ),
                ),
                create_journal_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: CreateJournalFeature(
                        service=CreateJournalUseCase(unit_of_work=uow)
                    ),
                ),
                list_fiscal_years_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: ListFiscalYearsFeature(
                        service=ListFiscalYearsUseCase(unit_of_work=uow)
                    ),
                ),
                post_journal_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: PostJournalFeature(service=PostJournalUseCase(unit_of_work=uow)),
                ),
                get_journal_feature=self._scoped_feature(
                    session_factory,
                    lambda uow: GetJournalFeature(service=GetJournalUseCase(unit_of_work=uow)),
                ),
            )

            project_accounting_workflow_feature = ProjectAccountingFeature(
                service=project_accounting_service
            )

            def build_project_status_service(uow):
                from mfm.application.reporting.project_status_service import (
                    ProjectStatusService,
                )

                return ProjectStatusService(
                    get_project_feature=GetProjectFeature(
                        service=GetProjectUseCase(unit_of_work=uow)
                    ),
                    list_documents_feature=ListDocumentsFeature(
                        service=ListDocumentsUseCase(unit_of_work=uow)
                    ),
                    search_journals_feature=SearchJournalsFeature(
                        service=SearchJournalsUseCase(unit_of_work=uow)
                    ),
                    list_fiscal_years_feature=ListFiscalYearsFeature(
                        service=ListFiscalYearsUseCase(unit_of_work=uow)
                    ),
                )

            project_status_feature = self._scoped_feature(
                session_factory,
                lambda uow: ReportingProjectStatusFeature(
                    service=build_project_status_service(uow)
                ),
            )

            def build_budget_vs_actual_service(uow):
                from mfm.application.reporting.budget_vs_actual_service import (
                    BudgetVsActualService,
                )

                return BudgetVsActualService(
                    get_project_feature=GetProjectFeature(
                        service=GetProjectUseCase(unit_of_work=uow)
                    ),
                    search_journals_feature=SearchJournalsFeature(
                        service=SearchJournalsUseCase(unit_of_work=uow)
                    ),
                    get_journal_feature=GetJournalFeature(
                        service=GetJournalUseCase(unit_of_work=uow)
                    ),
                    list_fiscal_years_feature=ListFiscalYearsFeature(
                        service=ListFiscalYearsUseCase(unit_of_work=uow)
                    ),
                )

            budget_vs_actual_feature = self._scoped_feature(
                session_factory,
                lambda uow: ReportingBudgetVsActualFeature(
                    service=build_budget_vs_actual_service(uow)
                ),
            )

            controller = AccountingController(
                list_journals_feature=list_journals_feature,
                search_journals_feature=search_journals_feature,
                get_journal_feature=get_journal_feature,
                post_journal_feature=post_journal_feature,
                list_fiscal_years_feature=list_fiscal_years_feature,
                project_accounting_workflow_feature=project_accounting_workflow_feature,
                project_status_feature=project_status_feature,
                budget_vs_actual_feature=budget_vs_actual_feature,
                navigation=AccountingNavigationCallbacks(),
            )
            return AccountingWorkspace(controller=controller)

        return load

    # -- Documents workspace -----------------------------------------------

    def _documents_workspace_loader(self, session_factory):
        def load() -> DocumentsWorkspace:
            list_documents_feature = self._scoped_feature(
                session_factory,
                lambda uow: ListDocumentsFeature(service=ListDocumentsUseCase(unit_of_work=uow)),
            )
            search_documents_feature = self._scoped_feature(
                session_factory,
                lambda uow: SearchDocumentsFeature(
                    service=SearchDocumentsUseCase(unit_of_work=uow)
                ),
            )
            get_document_feature = self._scoped_feature(
                session_factory,
                lambda uow: GetDocumentFeature(service=GetDocumentUseCase(unit_of_work=uow)),
            )
            create_document_feature = self._scoped_feature(
                session_factory,
                lambda uow: CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow)),
            )
            register_document_version_feature = self._scoped_feature(
                session_factory,
                lambda uow: RegisterDocumentVersionFeature(
                    service=RegisterDocumentVersionUseCase(unit_of_work=uow)
                ),
            )
            archive_document_feature = self._scoped_feature(
                session_factory,
                lambda uow: ArchiveDocumentFeature(
                    service=ArchiveDocumentUseCase(unit_of_work=uow)
                ),
            )

            controller = DocumentsController(
                list_documents_feature=list_documents_feature,
                search_documents_feature=search_documents_feature,
                get_document_feature=get_document_feature,
                create_document_feature=create_document_feature,
                register_document_version_feature=register_document_version_feature,
                archive_document_feature=archive_document_feature,
                navigation=DocumentsNavigationCallbacks(),
            )
            return DocumentsWorkspace(controller=controller)

        return load

    # -- Memberships workspace -----------------------------------------------

    def _memberships_workspace_loader(self, session_factory):
        def load() -> MembershipWorkspace:
            create_member_feature = self._scoped_feature(
                session_factory,
                lambda uow: CreateMemberFeature(unit_of_work=uow),
            )
            list_members_feature = self._scoped_feature(
                session_factory,
                lambda uow: ListMembersFeature(unit_of_work=uow),
            )
            get_member_feature = self._scoped_feature(
                session_factory,
                lambda uow: MembersGetMemberFeature(unit_of_work=uow),
            )
            list_membership_types_feature = self._scoped_feature(
                session_factory,
                lambda uow: MembershipTypesListFeature(unit_of_work=uow),
            )
            manage_membership_feature = self._scoped_feature(
                session_factory,
                lambda uow: ManageMembershipFeature(
                    service=MembershipManagementService(
                        membership_repository=uow.membership_repository,
                        membership_type_repository=uow.membership_type_repository,
                    )
                ),
            )

            controller = MembershipController(
                create_member_feature=create_member_feature,
                list_members_feature=list_members_feature,
                get_member_feature=get_member_feature,
                list_membership_types_feature=list_membership_types_feature,
                manage_membership_feature=manage_membership_feature,
            )
            return MembershipWorkspace(controller=controller)

        return load

    # -- Membership Billing workspace -----------------------------------------------

    def _membership_billing_workspace_loader(self, session_factory):
        def load() -> MembershipBillingWorkspace:
            annual_contingent_feature = self._scoped_feature(
                session_factory,
                lambda uow: AnnualContingentGenerationFeature(
                    unit_of_work=_AnnualContingentUnitOfWork(session_factory),
                    dispatcher=DomainEventDispatcher(),
                ),
            )

            manage_membership_billing_feature = self._scoped_feature(
                session_factory,
                lambda uow: ManageMembershipBillingFeature(
                    service=MembershipBillingService(
                        repository=uow.membership_billing_repository,
                        annual_contingent_feature=annual_contingent_feature,
                    )
                ),
            )
            list_fee_schedules_feature = self._scoped_feature(
                session_factory,
                lambda uow: ListFeeSchedulesFeature(unit_of_work=uow),
            )
            list_membership_types_feature = self._scoped_feature(
                session_factory,
                lambda uow: MembershipTypesListFeature(unit_of_work=uow),
            )

            controller = MembershipBillingController(
                manage_membership_billing_feature=manage_membership_billing_feature,
                list_fee_schedules_feature=list_fee_schedules_feature,
                list_membership_types_feature=list_membership_types_feature,
            )
            return MembershipBillingWorkspace(controller=controller)

        return load

    # -- Organizations workspace -----------------------------------------------

    def _organizations_workspace_loader(self, session_factory):
        def load() -> OrganizationWorkspace:
            create_organization_feature = self._scoped_feature(
                session_factory,
                lambda uow: CreateOrganizationStringFeature(
                    feature=CreateOrganizationFeature(
                        service=CreateOrganizationUseCase(
                            unit_of_work=uow, dispatcher=DomainEventDispatcher()
                        )
                    )
                ),
            )
            update_organization_feature = self._scoped_feature(
                session_factory,
                lambda uow: UpdateOrganizationStringFeature(
                    feature=OrgUpdateOrganizationFeature(
                        service=UpdateOrganizationUseCase(
                            unit_of_work=uow, dispatcher=DomainEventDispatcher()
                        )
                    )
                ),
            )
            list_organizations_feature = self._scoped_feature(
                session_factory,
                lambda uow: OrganizationsListFeature(unit_of_work=uow),
            )

            controller = OrganizationController(
                create_organization_feature=create_organization_feature,
                update_organization_feature=update_organization_feature,
                list_organizations_feature=list_organizations_feature,
            )
            return OrganizationWorkspace(controller=controller)

        return load

    def _organization_dashboard_loader(self, session_factory, organization_id: UUID):
        def load():
            uow = SQLAlchemyUnitOfWork(session_factory)
            with uow:
                service = OrganizationDashboardService(
                    list_projects_feature=ListProjectsFeature(
                        service=ListProjectsUseCase(unit_of_work=uow)
                    ),
                    list_documents_feature=ListDocumentsFeature(
                        service=ListDocumentsUseCase(unit_of_work=uow)
                    ),
                    search_journals_feature=SearchJournalsFeature(
                        service=SearchJournalsUseCase(unit_of_work=uow)
                    ),
                    list_fiscal_years_feature=ListFiscalYearsFeature(
                        service=ListFiscalYearsUseCase(unit_of_work=uow)
                    ),
                )
                return service.execute(
                    OrganizationDashboardRequest(organization_id=organization_id)
                )

        return load

    def _active_projects_loader(self, session_factory, organization_id: UUID):
        def load():
            uow = SQLAlchemyUnitOfWork(session_factory)
            with uow:
                service = ActiveProjectsService(
                    list_projects_feature=ListProjectsFeature(
                        service=ListProjectsUseCase(unit_of_work=uow)
                    ),
                    list_documents_feature=ListDocumentsFeature(
                        service=ListDocumentsUseCase(unit_of_work=uow)
                    ),
                    search_journals_feature=SearchJournalsFeature(
                        service=SearchJournalsUseCase(unit_of_work=uow)
                    ),
                )
                return service.execute(
                    ActiveProjectsDashboardRequest(organization_id=organization_id)
                )

        return load

    def _project_status_loader(self, session_factory, project_id: UUID):
        def load():
            uow = SQLAlchemyUnitOfWork(session_factory)
            with uow:
                service = ProjectStatusService(
                    get_project_feature=GetProjectFeature(
                        service=GetProjectUseCase(unit_of_work=uow)
                    ),
                    list_documents_feature=ListDocumentsFeature(
                        service=ListDocumentsUseCase(unit_of_work=uow)
                    ),
                    search_journals_feature=SearchJournalsFeature(
                        service=SearchJournalsUseCase(unit_of_work=uow)
                    ),
                    list_fiscal_years_feature=ListFiscalYearsFeature(
                        service=ListFiscalYearsUseCase(unit_of_work=uow)
                    ),
                )
                return service.execute(ProjectStatusRequest(project_id=project_id))

        return load

    def _budget_vs_actual_loader(self, session_factory, project_id: UUID):
        def load():
            from mfm.application.accounting.get_journal import GetJournalUseCase
            from mfm.application.features.accounting.get_journal_feature import (
                GetJournalFeature,
            )

            uow = SQLAlchemyUnitOfWork(session_factory)
            with uow:
                service = BudgetVsActualService(
                    get_project_feature=GetProjectFeature(
                        service=GetProjectUseCase(unit_of_work=uow)
                    ),
                    search_journals_feature=SearchJournalsFeature(
                        service=SearchJournalsUseCase(unit_of_work=uow)
                    ),
                    get_journal_feature=GetJournalFeature(
                        service=GetJournalUseCase(unit_of_work=uow)
                    ),
                    list_fiscal_years_feature=ListFiscalYearsFeature(
                        service=ListFiscalYearsUseCase(unit_of_work=uow)
                    ),
                )
                return service.execute(BudgetVsActualRequest(project_id=project_id))

        return load
