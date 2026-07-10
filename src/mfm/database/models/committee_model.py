"""SQLAlchemy ORM model for committees."""

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
from mfm.domain.organization.committee_status import CommitteeStatus

if TYPE_CHECKING:
    from mfm.database.models.committee_member_model import CommitteeMemberModel
    from mfm.database.models.organization_model import OrganizationModel


class CommitteeModel(BaseModel):
    """Persistence model for committees."""

    __tablename__ = "committee"

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organization.id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    purpose: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
        default="",
    )

    status: Mapped[CommitteeStatus] = mapped_column(
        Enum(CommitteeStatus, native_enum=False, length=20),
        nullable=False,
        default=CommitteeStatus.ACTIVE,
    )

    organization: Mapped["OrganizationModel"] = relationship(
        "OrganizationModel",
        back_populates="committees",
    )

    members: Mapped[list["CommitteeMemberModel"]] = relationship(
        "CommitteeMemberModel",
        back_populates="committee",
        cascade="all, delete-orphan",
    )
