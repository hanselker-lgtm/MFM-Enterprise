"""
Database engine factory.
"""

from __future__ import annotations

from sqlalchemy import Engine
from sqlalchemy import create_engine


class EngineFactory:
    """Creates SQLAlchemy database engines."""

    @staticmethod
    def create(
        database_url: str,
        *,
        echo: bool = False,
    ) -> Engine:
        """
        Create a SQLAlchemy Engine.

        Args:
            database_url:
                SQLAlchemy database URL.

            echo:
                Enable SQL logging.

        Returns:
            Configured SQLAlchemy Engine.
        """

        return create_engine(
            database_url,
            echo=echo,
            future=True,
            pool_pre_ping=True,
        )