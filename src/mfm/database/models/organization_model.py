"""SQLAlchemy ORM model for organizations."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType

if TYPE_CHECKING:
    from mfm.database.models.board_model import BoardModel
    from mfm.database.models.committee_model import CommitteeModel
    from mfm.database.models.role_assignment_model import RoleAssignmentModel
    from mfm.database.models.role_model import RoleModel


class OrganizationModel(BaseModel):
    """Persistence model for organizations."""

    __tablename__ = "organization"

    organization_number: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    organization_type: Mapped[OrganizationType] = mapped_column(
        Enum(OrganizationType, native_enum=False, length=30),
        nullable=False,
        default=OrganizationType.OTHER,
    )

    status: Mapped[OrganizationStatus] = mapped_column(
        Enum(OrganizationStatus, native_enum=False, length=20),
        nullable=False,
        default=OrganizationStatus.ACTIVE,
    )

    boards: Mapped[list["BoardModel"]] = relationship(
        "BoardModel",
        back_populates="organization",
        cascade="all, delete-orphan",
    )

    committees: Mapped[list["CommitteeModel"]] = relationship(
        "CommitteeModel",
        back_populates="organization",
        cascade="all, delete-orphan",
    )

    roles: Mapped[list["RoleModel"]] = relationship(
        "RoleModel",
        back_populates="organization",
        cascade="all, delete-orphan",
    )

    role_assignments: Mapped[list["RoleAssignmentModel"]] = relationship(
        "RoleAssignmentModel",
        back_populates="organization",
        cascade="all, delete-orphan",
    )
