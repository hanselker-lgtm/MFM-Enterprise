"""SQLAlchemy ORM model for project external references."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.projects.reference_type import ReferenceType

if TYPE_CHECKING:
    from mfm.database.models.project_model import ProjectModel


class ExternalReferenceModel(BaseModel):
    """Persistence model for project external references."""

    __tablename__ = "project_reference"
    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "reference_order",
            name="uq_project_reference_order",
        ),
    )

    project_id: Mapped[UUID] = mapped_column(
        ForeignKey("project.id"),
        nullable=False,
        index=True,
    )

    reference_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    reference_type: Mapped[ReferenceType] = mapped_column(
        Enum(ReferenceType, native_enum=False, length=40),
        nullable=False,
    )

    external_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    reference_created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    project: Mapped["ProjectModel"] = relationship(
        "ProjectModel",
        back_populates="references",
    )
