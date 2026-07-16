"""SQLAlchemy ORM model for project activities."""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.projects.project_priority import ProjectPriority

if TYPE_CHECKING:
    from mfm.database.models.project_model import ProjectModel


class ProjectActivityModel(BaseModel):
    """Persistence model for project activities."""

    __tablename__ = "project_activity"
    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "activity_order",
            name="uq_project_activity_order",
        ),
    )

    project_id: Mapped[UUID] = mapped_column(
        ForeignKey("project.id"),
        nullable=False,
        index=True,
    )

    activity_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )

    priority: Mapped[ProjectPriority] = mapped_column(
        Enum(ProjectPriority, native_enum=False, length=20),
        nullable=False,
        default=ProjectPriority.NORMAL,
    )

    estimated_hours: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 4),
        nullable=True,
    )

    actual_hours: Mapped[Decimal | None] = mapped_column(
        Numeric(24, 4),
        nullable=True,
    )

    planned_start: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    planned_finish: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    actual_start: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    actual_finish: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    project: Mapped["ProjectModel"] = relationship(
        "ProjectModel",
        back_populates="activities",
    )
