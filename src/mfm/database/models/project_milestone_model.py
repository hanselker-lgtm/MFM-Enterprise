"""SQLAlchemy ORM model for project milestones."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.project_model import ProjectModel


class ProjectMilestoneModel(BaseModel):
    """Persistence model for project milestones."""

    __tablename__ = "project_milestone"
    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "sequence",
            name="uq_project_milestone_sequence",
        ),
    )

    project_id: Mapped[UUID] = mapped_column(
        ForeignKey("project.id"),
        nullable=False,
        index=True,
    )

    sequence: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
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

    due_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    completed_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    project: Mapped["ProjectModel"] = relationship(
        "ProjectModel",
        back_populates="milestones",
    )
