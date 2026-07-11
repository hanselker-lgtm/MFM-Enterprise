"""SQLAlchemy ORM model for technical configurations."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.technical_configuration.technical_configuration_status import (
    TechnicalConfigurationStatus,
)

if TYPE_CHECKING:
    from mfm.database.models.technical_component_link_model import (
        TechnicalComponentLinkModel,
    )
    from mfm.database.models.technical_component_model import TechnicalComponentModel
    from mfm.database.models.technical_component_replacement_model import (
        TechnicalComponentReplacementModel,
    )


class TechnicalConfigurationModel(BaseModel):
    """Persistence model for technical configuration aggregate."""

    __tablename__ = "technical_configuration"

    vessel_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    status: Mapped[TechnicalConfigurationStatus] = mapped_column(
        Enum(TechnicalConfigurationStatus, native_enum=False, length=20),
        nullable=False,
        default=TechnicalConfigurationStatus.DRAFT,
    )

    components: Mapped[list["TechnicalComponentModel"]] = relationship(
        "TechnicalComponentModel",
        back_populates="configuration",
        cascade="all, delete-orphan",
        single_parent=True,
    )

    links: Mapped[list["TechnicalComponentLinkModel"]] = relationship(
        "TechnicalComponentLinkModel",
        back_populates="configuration",
        cascade="all, delete-orphan",
        single_parent=True,
    )

    replacements: Mapped[list["TechnicalComponentReplacementModel"]] = relationship(
        "TechnicalComponentReplacementModel",
        back_populates="configuration",
        cascade="all, delete-orphan",
        single_parent=True,
    )
