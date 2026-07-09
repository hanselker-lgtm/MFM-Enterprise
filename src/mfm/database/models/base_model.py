"""
Shared SQLAlchemy ORM base model.

All persistence models inherit from BaseModel.

Business logic belongs in the domain layer.
Persistence logic belongs in the database layer.
"""

from __future__ import annotations

from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from mfm.database.base import Base


class BaseModel(Base):
    """
    Abstract base class for all ORM models.

    Provides:

    - UUID primary key
    - Created timestamp
    - Modified timestamp
    """

    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )