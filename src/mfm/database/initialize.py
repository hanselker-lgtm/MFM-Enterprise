"""
Database initialization.
"""

from __future__ import annotations

from sqlalchemy.engine import Engine

from mfm.database.base import Base
import mfm.database.metadata  # noqa: F401


def initialize_database(
    engine: Engine,
    *,
    development: bool = False,
) -> None:
    """
    Initialize the database.

    Parameters
    ----------
    engine:
        SQLAlchemy Engine.

    development:
        When True, tables are created automatically.
        Production environments must use Alembic.
    """

    if development:
        Base.metadata.create_all(bind=engine)