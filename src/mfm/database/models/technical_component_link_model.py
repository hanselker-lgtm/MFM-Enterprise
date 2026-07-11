"""SQLAlchemy ORM model for technical component links."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.technical_configuration.component_link_role import ComponentLinkRole

if TYPE_CHECKING:
    from mfm.database.models.technical_configuration_model import TechnicalConfigurationModel


class TechnicalComponentLinkModel(BaseModel):
    """Persistence model for component structure links."""

    __tablename__ = "technical_component_link"

    technical_configuration_id: Mapped[UUID] = mapped_column(
        ForeignKey("technical_configuration.id"),
        nullable=False,
        index=True,
    )

    upstream_component_id: Mapped[UUID] = mapped_column(
        ForeignKey("technical_component.id"),
        nullable=False,
        index=True,
    )

    downstream_component_id: Mapped[UUID] = mapped_column(
        ForeignKey("technical_component.id"),
        nullable=False,
        index=True,
    )

    role: Mapped[ComponentLinkRole] = mapped_column(
        Enum(ComponentLinkRole, native_enum=False, length=30),
        nullable=False,
        default=ComponentLinkRole.CONNECTS_TO,
    )

    effective_from: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    effective_to: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    configuration: Mapped["TechnicalConfigurationModel"] = relationship(
        "TechnicalConfigurationModel",
        back_populates="links",
    )
