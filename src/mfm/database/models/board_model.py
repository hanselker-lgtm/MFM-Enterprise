"""SQLAlchemy ORM model for boards."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.organization.board_status import BoardStatus

if TYPE_CHECKING:
    from mfm.database.models.board_member_model import BoardMemberModel
    from mfm.database.models.organization_model import OrganizationModel


class BoardModel(BaseModel):
    """Persistence model for boards."""

    __tablename__ = "board"

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey("organization.id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    term_start: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    term_end: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[BoardStatus] = mapped_column(
        Enum(BoardStatus, native_enum=False, length=20),
        nullable=False,
        default=BoardStatus.ACTIVE,
    )

    organization: Mapped["OrganizationModel"] = relationship(
        "OrganizationModel",
        back_populates="boards",
    )

    members: Mapped[list["BoardMemberModel"]] = relationship(
        "BoardMemberModel",
        back_populates="board",
        cascade="all, delete-orphan",
    )
