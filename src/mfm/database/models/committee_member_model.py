"""SQLAlchemy ORM model for committee members."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.committee_model import CommitteeModel


class CommitteeMemberModel(BaseModel):
    """Persistence model for committee members."""

    __tablename__ = "committee_member"

    committee_id: Mapped[UUID] = mapped_column(
        ForeignKey("committee.id"),
        nullable=False,
        index=True,
    )

    reference_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    function_title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    joined_at: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    left_at: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    committee: Mapped["CommitteeModel"] = relationship(
        "CommitteeModel",
        back_populates="members",
    )
