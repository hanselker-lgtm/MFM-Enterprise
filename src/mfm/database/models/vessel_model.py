"""SQLAlchemy ORM model for vessels."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_status import VesselStatus

if TYPE_CHECKING:
    from mfm.database.models.asset_model import AssetModel
    from mfm.database.models.vessel_dimensions_model import VesselDimensionsModel


class VesselModel(BaseModel):
    """Persistence model for vessels."""

    __tablename__ = "vessel"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("asset.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    registration: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    shipyard: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        default="",
    )

    build_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    construction_material: Mapped[VesselMaterial] = mapped_column(
        Enum(VesselMaterial, native_enum=False, length=30),
        nullable=False,
        default=VesselMaterial.OTHER,
    )

    status: Mapped[VesselStatus] = mapped_column(
        Enum(VesselStatus, native_enum=False, length=20),
        nullable=False,
        default=VesselStatus.ACTIVE,
    )

    asset: Mapped["AssetModel"] = relationship(
        "AssetModel",
        back_populates="vessel",
    )

    dimensions: Mapped["VesselDimensionsModel"] = relationship(
        "VesselDimensionsModel",
        back_populates="vessel",
        cascade="all, delete-orphan",
        single_parent=True,
        uselist=False,
    )
