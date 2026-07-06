"""
Shared SQLAlchemy base class.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Root Declarative Base for the entire application.
    """

    pass