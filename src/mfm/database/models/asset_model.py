"""SQLAlchemy ORM model for assets."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_status import AssetStatus

if TYPE_CHECKING:
    from mfm.database.models.asset_location_model import AssetLocationModel
    from mfm.database.models.vessel_model import VesselModel


class AssetModel(BaseModel):
    """Persistence model for generic assets."""

    __tablename__ = "asset"

    asset_number: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(2000),
        nullable=False,
        default="",
    )

    category: Mapped[AssetCategory] = mapped_column(
        Enum(AssetCategory, native_enum=False, length=30),
        nullable=False,
        default=AssetCategory.OTHER,
    )

    status: Mapped[AssetStatus] = mapped_column(
        Enum(AssetStatus, native_enum=False, length=20),
        nullable=False,
        default=AssetStatus.ACTIVE,
    )

    owner_id: Mapped[UUID | None] = mapped_column(
        nullable=True,
        index=True,
    )

    acquisition_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    retired_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    location: Mapped["AssetLocationModel"] = relationship(
        "AssetLocationModel",
        back_populates="asset",
        cascade="all, delete-orphan",
        single_parent=True,
        uselist=False,
    )

    vessel: Mapped["VesselModel | None"] = relationship(
        "VesselModel",
        back_populates="asset",
        cascade="all, delete-orphan",
        single_parent=True,
        uselist=False,
    )
