"""SQLAlchemy ORM model for projects aggregate root."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.projects.project_priority import ProjectPriority
from mfm.domain.projects.project_status import ProjectStatus

if TYPE_CHECKING:
    from mfm.database.models.external_reference_model import ExternalReferenceModel
    from mfm.database.models.project_activity_model import ProjectActivityModel
    from mfm.database.models.project_assignment_model import ProjectAssignmentModel
    from mfm.database.models.project_milestone_model import ProjectMilestoneModel


class ProjectModel(BaseModel):
    """Persistence model for Project aggregate root."""

    __tablename__ = "project"

    project_number: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True,
        index=True,
    )

    project_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(4000),
        nullable=True,
    )

    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus, native_enum=False, length=20),
        nullable=False,
        default=ProjectStatus.DRAFT,
    )

    priority: Mapped[ProjectPriority] = mapped_column(
        Enum(ProjectPriority, native_enum=False, length=20),
        nullable=False,
        default=ProjectPriority.NORMAL,
    )

    start_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    end_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    project_created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    project_updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    archived_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    milestones: Mapped[list["ProjectMilestoneModel"]] = relationship(
        "ProjectMilestoneModel",
        back_populates="project",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="ProjectMilestoneModel.sequence",
    )

    activities: Mapped[list["ProjectActivityModel"]] = relationship(
        "ProjectActivityModel",
        back_populates="project",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="ProjectActivityModel.activity_order",
    )

    assignments: Mapped[list["ProjectAssignmentModel"]] = relationship(
        "ProjectAssignmentModel",
        back_populates="project",
        cascade="all, delete-orphan",
        single_parent=True,
    )

    references: Mapped[list["ExternalReferenceModel"]] = relationship(
        "ExternalReferenceModel",
        back_populates="project",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="ExternalReferenceModel.reference_order",
    )
