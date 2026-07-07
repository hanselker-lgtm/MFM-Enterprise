"""
Database session management.

Provides a configurable SQLAlchemy session factory.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


class SessionFactory:
    """
    Factory responsible for creating SQLAlchemy sessions.
    """

    def __init__(self, engine: Engine) -> None:
        self._session_factory = sessionmaker(
            bind=engine,
            autoflush=False,
            expire_on_commit=False,
            class_=Session,
        )

    def create(self) -> Session:
        """
        Create a new database session.
        """
        return self._session_factory()

    @contextmanager
    def session_scope(self) -> Iterator[Session]:
        """
        Provide a transactional scope around a series of operations.
        """

        session = self.create()

        try:
            yield session
            session.commit()

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()