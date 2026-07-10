"""SQLAlchemy ORM model for roles."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.organization.role_status import RoleStatus
from mfm.domain.organization.role_type import RoleType

if TYPE_CHECKING:
    from mfm.database.models.organization_model import OrganizationModel
    from mfm.database.models.role_assignment_model import RoleAssignmentModel


class RoleModel(BaseModel):
    """Persistence model for roles."""

    __tablename__ = "role"

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organization.id"),
        nullable=False,
        index=True,
    )

    role_code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    category: Mapped[RoleType] = mapped_column(
        Enum(RoleType, native_enum=False, length=30),
        nullable=False,
    )

    status: Mapped[RoleStatus] = mapped_column(
        Enum(RoleStatus, native_enum=False, length=20),
        nullable=False,
        default=RoleStatus.ACTIVE,
    )

    organization: Mapped["OrganizationModel"] = relationship(
        "OrganizationModel",
        back_populates="roles",
    )

    assignments: Mapped[list["RoleAssignmentModel"]] = relationship(
        "RoleAssignmentModel",
        back_populates="role",
        cascade="all, delete-orphan",
    )
