"""
SQLAlchemy ORM models.

This package contains all persistence models used by MFM Enterprise.

Only ORM models belong here.
Domain models must never be imported into the persistence layer.
"""

from mfm.database.models.base_model import BaseModel

__all__ = [
    "BaseModel",
]