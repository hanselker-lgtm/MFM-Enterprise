"""SQLAlchemy ORM model for asset locations."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.asset_model import AssetModel


class AssetLocationModel(BaseModel):
    """Persistence model for current asset location."""

    __tablename__ = "asset_location"

    asset_id: Mapped[UUID] = mapped_column(
        ForeignKey("asset.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    value: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    asset: Mapped["AssetModel"] = relationship(
        "AssetModel",
        back_populates="location",
    )
