"""SQLAlchemy ORM model for membership types."""

from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from mfm.database.models.base_model import BaseModel
from mfm.domain.membership.membership_category import MembershipCategory


class MembershipTypeModel(BaseModel):
    """Persistence model for membership types."""

    __tablename__ = "membership_type"

    code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    category: Mapped[MembershipCategory] = mapped_column(
        Enum(MembershipCategory, native_enum=False, length=20),
        nullable=False,
        default=MembershipCategory.GENERAL,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )
