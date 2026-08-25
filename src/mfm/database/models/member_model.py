"""SQLAlchemy ORM model for members."""

from __future__ import annotations

from datetime import date
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from mfm.database.models.base_model import BaseModel
from mfm.domain.member.member_status import MemberStatus


class MemberModel(BaseModel):
    """Persistence model for members."""

    __tablename__ = "member"

    contact_id: Mapped[UUID] = mapped_column(
        ForeignKey("contact.id"),
        nullable=False,
        index=True,
    )

    member_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    status: Mapped[MemberStatus] = mapped_column(
        Enum(MemberStatus, native_enum=False, length=20),
        nullable=False,
        default=MemberStatus.ACTIVE,
    )

    join_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    leave_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )
