"""SQLAlchemy ORM model for technical components."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)

if TYPE_CHECKING:
    from mfm.database.models.technical_configuration_model import TechnicalConfigurationModel


class TechnicalComponentModel(BaseModel):
    """Persistence model for technical component entity."""

    __tablename__ = "technical_component"

    technical_configuration_id: Mapped[UUID] = mapped_column(
        ForeignKey("technical_configuration.id"),
        nullable=False,
        index=True,
    )

    component_type: Mapped[TechnicalComponentType] = mapped_column(
        Enum(TechnicalComponentType, native_enum=False, length=40),
        nullable=False,
        default=TechnicalComponentType.OTHER,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    manufacturer: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    model: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    serial_number: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    build_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    installed_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    removed_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[TechnicalComponentStatus] = mapped_column(
        Enum(TechnicalComponentStatus, native_enum=False, length=20),
        nullable=False,
        default=TechnicalComponentStatus.PLANNED,
    )

    notes: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    specification_schema_key: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="GENERIC_V1",
    )

    specification_entries: Mapped[list[dict[str, object]]] = mapped_column(
        JSON,
        nullable=False,
        default=list,
    )

    replacement_successor_component_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("technical_component.id"),
        nullable=True,
        index=True,
    )

    configuration: Mapped["TechnicalConfigurationModel"] = relationship(
        "TechnicalConfigurationModel",
        back_populates="components",
    )
