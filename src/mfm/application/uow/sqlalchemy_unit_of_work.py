"""SQLAlchemy-backed UnitOfWork implementation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
from uuid import UUID

from sqlalchemy.orm import Session

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.repositories.sqlite_contact_repository import SQLiteContactRepository
from mfm.database.repositories.sqlite_contingent_plan_repository import (
    SQLiteContingentPlanRepository,
)
from mfm.database.repositories.sqlite_member_repository import SQLiteMemberRepository
from mfm.database.repositories.sqlite_membership_repository import SQLiteMembershipRepository
from mfm.database.repositories.sqlite_membership_type_repository import (
    SQLiteMembershipTypeRepository,
)
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
from mfm.infrastructure.persistence.finance.sqlalchemy_invoice_repository import (
    SqlAlchemyInvoiceRepository,
)
from mfm.infrastructure.persistence.membership_billing.sqlalchemy_membership_billing_repository import (
    SqlAlchemyMembershipBillingRepository,
)
from mfm.infrastructure.persistence.projects.sqlite_project_repository import (
    SQLiteProjectRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_organization_repository import (
    SQLiteOrganizationRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork as SessionUnitOfWork


@dataclass(slots=True)
class _SessionBoundRepository:
    """Minimal repository bound to a shared SQLAlchemy session."""

    _session: Session

    def add(self, entity) -> None:  # pragma: no cover - simple pass-through helper
        self._session.add(entity)

    def delete(self, entity_id: UUID) -> None:  # pragma: no cover - not used in tests
        _ = entity_id


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    """UnitOfWork that wires repositories to one SQLAlchemy session.

    Two repository construction styles exist in this codebase: some
    repositories take a raw SQLAlchemy ``Session`` directly (contact,
    member, membership), while others take the lightweight
    ``mfm.repositories.unit_of_work.UnitOfWork`` session wrapper
    (project, document, accounting, organization). Both are backed by
    the same shared session created below, so they participate in the
    same transaction.
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

        # All repositories are initialized with the same shared session.
        self.contact_repository = SQLiteContactRepository(self.session)
        self.member_repository = SQLiteMemberRepository(self.session)
        self.membership_repository = SQLiteMembershipRepository(self.session)
        self.membership_type_repository = SQLiteMembershipTypeRepository(self.session)
        self.contingent_repository = SQLiteContingentPlanRepository(self.session)
        self.invoice_repository = SqlAlchemyInvoiceRepository(self.session)
        self.payment_repository = _SessionBoundRepository(self.session)

        self.project_repository = SQLiteProjectRepository(session_uow)
        self.document_repository = SQLiteDocumentRepository(session_uow)
        self.journal_repository = SQLiteJournalRepository(session_uow)
        self.ledger_account_repository = SQLiteLedgerAccountRepository(session_uow)
        self.fiscal_year_repository = SQLiteFiscalYearRepository(session_uow)
        self.organization_repository = SQLiteOrganizationRepository(session_uow)
        self.membership_billing_repository = SqlAlchemyMembershipBillingRepository(self.session)

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
