"""SQLAlchemy ORM model for vessel dimensions."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.vessel_model import VesselModel


class VesselDimensionsModel(BaseModel):
    """Persistence model for vessel dimensions."""

    __tablename__ = "vessel_dimensions"

    vessel_id: Mapped[UUID] = mapped_column(
        ForeignKey("vessel.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    length: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    beam: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    draft: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    vessel: Mapped["VesselModel"] = relationship(
        "VesselModel",
        back_populates="dimensions",
    )
