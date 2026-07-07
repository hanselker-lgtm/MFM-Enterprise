"""
SQLAlchemy declarative base.

All ORM models in MFM Enterprise inherit, directly or indirectly,
from this shared DeclarativeBase.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""

    pass