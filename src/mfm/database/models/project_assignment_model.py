"""SQLAlchemy ORM model for project assignments."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.project_model import ProjectModel


class ProjectAssignmentModel(BaseModel):
    """Persistence model for project assignments."""

    __tablename__ = "project_assignment"

    project_id: Mapped[UUID] = mapped_column(
        ForeignKey("project.id"),
        nullable=False,
        index=True,
    )

    organisation_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    contact_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    role: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    assigned_from: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    assigned_until: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    project: Mapped["ProjectModel"] = relationship(
        "ProjectModel",
        back_populates="assignments",
    )
