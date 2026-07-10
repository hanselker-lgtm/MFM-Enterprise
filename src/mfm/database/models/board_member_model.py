"""SQLAlchemy ORM model for board members."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.board_model import BoardModel


class BoardMemberModel(BaseModel):
    """Persistence model for board members."""

    __tablename__ = "board_member"

    board_id: Mapped[UUID] = mapped_column(
        ForeignKey("board.id"),
        nullable=False,
        index=True,
    )

    member_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    role: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    appointed_on: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    resigned_on: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    is_chair: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    board: Mapped["BoardModel"] = relationship(
        "BoardModel",
        back_populates="members",
    )
