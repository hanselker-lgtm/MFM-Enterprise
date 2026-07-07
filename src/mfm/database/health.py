"""
Database health checks.
"""

from sqlalchemy import text
from sqlalchemy.engine import Engine


def check_database(engine: Engine) -> bool:
    """
    Returns True if the database connection is working.
    """

    try:

        with engine.connect() as connection:

            connection.execute(text("SELECT 1"))

        return True

    except Exception:

        return False