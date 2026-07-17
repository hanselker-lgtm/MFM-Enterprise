"""SQLAlchemy ORM model for memberships."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.membership.membership_status import MembershipStatus

if TYPE_CHECKING:
    from mfm.database.models.membership_type_model import MembershipTypeModel


class MembershipModel(BaseModel):
    """Persistence model for memberships."""

    __tablename__ = "membership"

    member_id: Mapped[UUID] = mapped_column(
        ForeignKey("member.id"),
        nullable=False,
        index=True,
    )

    membership_type_id: Mapped[UUID] = mapped_column(
        ForeignKey("membership_type.id"),
        nullable=False,
        index=True,
    )

    status: Mapped[MembershipStatus] = mapped_column(
        Enum(MembershipStatus, native_enum=False, length=20),
        nullable=False,
        default=MembershipStatus.ACTIVE,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    membership_type: Mapped["MembershipTypeModel"] = relationship(
        "MembershipTypeModel",
    )
