"""
Unit of Work implementation.

Responsible for transaction handling.
"""

from __future__ import annotations

from typing import Protocol


class SessionLike(Protocol):
    def commit(self) -> None: ...

    def rollback(self) -> None: ...

    def close(self) -> None: ...


class UnitOfWork:
    """
    Coordinates database transactions.
    """

    def __init__(self, session: SessionLike):
        self._session = session

    @property
    def session(self) -> SessionLike:
        return self._session

    def commit(self) -> None:
        """Commit current transaction."""
        self._session.commit()

    def rollback(self) -> None:
        """Rollback current transaction."""
        self._session.rollback()

    def close(self) -> None:
        """Close session."""
        self._session.close()

    def __enter__(self) -> "UnitOfWork":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is None:
            self.commit()
        else:
            self.rollback()

        self.close()