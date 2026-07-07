"""
Base class for aggregate roots.
"""

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from mfm.database.base import Base


class AggregateRoot(Base):

    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        "CreatedAt",
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        "UpdatedAt",
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )

    created_by: Mapped[str | None] = mapped_column(
        "CreatedBy",
        String(100),
        nullable=True,
    )

    updated_by: Mapped[str | None] = mapped_column(
        "UpdatedBy",
        String(100),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        default=True,
        nullable=False,
    )