"""SQLAlchemy ORM model for technical component replacement history."""

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
    from mfm.database.models.technical_configuration_model import TechnicalConfigurationModel


class TechnicalComponentReplacementModel(BaseModel):
    """Persistence model for historical component replacement record."""

    __tablename__ = "technical_component_replacement"

    technical_configuration_id: Mapped[UUID] = mapped_column(
        ForeignKey("technical_configuration.id"),
        nullable=False,
        index=True,
    )

    replaced_component_id: Mapped[UUID] = mapped_column(
        ForeignKey("technical_component.id"),
        nullable=False,
        index=True,
    )

    replacement_component_id: Mapped[UUID] = mapped_column(
        ForeignKey("technical_component.id"),
        nullable=False,
        index=True,
    )

    replaced_on: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    reason: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    configuration: Mapped["TechnicalConfigurationModel"] = relationship(
        "TechnicalConfigurationModel",
        back_populates="replacements",
    )
