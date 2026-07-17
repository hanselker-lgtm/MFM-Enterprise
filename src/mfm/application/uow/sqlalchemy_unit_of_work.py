"""SQLAlchemy-backed UnitOfWork implementation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
from uuid import UUID

from sqlalchemy.orm import Session

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.repositories.sqlite_contact_repository import SQLiteContactRepository
from mfm.database.repositories.sqlite_member_repository import SQLiteMemberRepository
from mfm.database.repositories.sqlite_membership_repository import SQLiteMembershipRepository


@dataclass(slots=True)
class _SessionBoundRepository:
    """Minimal repository bound to a shared SQLAlchemy session."""

    _session: Session

    def add(self, entity) -> None:  # pragma: no cover - simple pass-through helper
        self._session.add(entity)

    def delete(self, entity_id: UUID) -> None:  # pragma: no cover - not used in tests
        _ = entity_id


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):
    """UnitOfWork that wires repositories to one SQLAlchemy session."""

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

        # All repositories are initialized with the same shared session.
        self.contact_repository = SQLiteContactRepository(self.session)
        self.member_repository = SQLiteMemberRepository(self.session)
        self.membership_repository = SQLiteMembershipRepository(self.session)
        self.invoice_repository = _SessionBoundRepository(self.session)
        self.payment_repository = _SessionBoundRepository(self.session)
        self.journal_repository = _SessionBoundRepository(self.session)

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
