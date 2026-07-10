"""SQLAlchemy ORM model for role assignments."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.organization_model import OrganizationModel
    from mfm.database.models.role_model import RoleModel


class RoleAssignmentModel(BaseModel):
    """Persistence model for role assignments."""

    __tablename__ = "role_assignment"

    role_id: Mapped[UUID] = mapped_column(
        ForeignKey("role.id"),
        nullable=False,
        index=True,
    )

    assignee_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organization.id"),
        nullable=False,
        index=True,
    )

    valid_from: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    valid_to: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    role: Mapped["RoleModel"] = relationship(
        "RoleModel",
        back_populates="assignments",
    )

    organization: Mapped["OrganizationModel"] = relationship(
        "OrganizationModel",
        back_populates="role_assignments",
    )
