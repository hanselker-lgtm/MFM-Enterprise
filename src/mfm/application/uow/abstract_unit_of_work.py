"""Abstract UnitOfWork contract for application workflows."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class AbstractUnitOfWork(ABC):
    """Coordinates repositories in one transactional boundary."""

    contact_repository: Any
    member_repository: Any
    membership_repository: Any
    invoice_repository: Any
    payment_repository: Any
    journal_repository: Any

    def __init__(self) -> None:
        self._depth = 0
        self._committed = False
        self._rolled_back = False

    def __enter__(self) -> "AbstractUnitOfWork":
        if self._depth == 0:
            self._start_scope()
            self._committed = False
            self._rolled_back = False
        self._depth += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._depth -= 1

        if exc_type is not None and not self._rolled_back:
            self.rollback()
            self._rolled_back = True

        if self._depth == 0:
            self.close()

    @abstractmethod
    def _start_scope(self) -> None:
        """Initialize transactional scope and repositories."""

    @abstractmethod
    def _commit_impl(self) -> None:
        """Commit underlying transaction."""

    @abstractmethod
    def _rollback_impl(self) -> None:
        """Rollback underlying transaction."""

    @abstractmethod
    def _flush_impl(self) -> None:
        """Flush pending changes to transaction."""

    @abstractmethod
    def _close_impl(self) -> None:
        """Close underlying transactional resources."""

    def commit(self) -> None:
        """Commit transaction exactly once per scope."""

        if self._committed:
            raise RuntimeError("UnitOfWork commit can only be called once per scope")
        self._commit_impl()
        self._committed = True

    def rollback(self) -> None:
        """Rollback transaction."""

        self._rollback_impl()

    def flush(self) -> None:
        """Flush transaction state."""

        self._flush_impl()

    def close(self) -> None:
        """Close session/resources."""

        self._close_impl()
