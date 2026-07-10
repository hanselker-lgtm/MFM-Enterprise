"""SQLAlchemy ORM model for volunteers."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.organization.volunteer_status import VolunteerStatus

if TYPE_CHECKING:
    from mfm.database.models.contact_model import ContactModel
    from mfm.database.models.member_model import MemberModel


class VolunteerModel(BaseModel):
    """Persistence model for volunteers."""

    __tablename__ = "volunteer"

    contact_id: Mapped[UUID] = mapped_column(
        ForeignKey("contact.id"),
        nullable=False,
        index=True,
    )

    member_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("member.id"),
        nullable=True,
        index=True,
    )

    status: Mapped[VolunteerStatus] = mapped_column(
        Enum(VolunteerStatus, native_enum=False, length=20),
        nullable=False,
        default=VolunteerStatus.ACTIVE,
    )

    joined_at: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    left_at: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    max_hours_per_week: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    preferred_days: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
        default="",
    )

    skills: Mapped[str] = mapped_column(
        String(2000),
        nullable=False,
        default="",
    )

    certificates: Mapped[str] = mapped_column(
        String(4000),
        nullable=False,
        default="",
    )

    contact: Mapped["ContactModel"] = relationship("ContactModel")
    member: Mapped["MemberModel | None"] = relationship("MemberModel")
