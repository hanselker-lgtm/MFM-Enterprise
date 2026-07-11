"""SQLAlchemy ORM model for maintenance plans."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.maintenance.maintenance_plan_status import MaintenancePlanStatus
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType

if TYPE_CHECKING:
    from mfm.database.models.maintenance_requirement_model import (
        MaintenanceRequirementModel,
    )


class MaintenancePlanModel(BaseModel):
    """Persistence model for maintenance plan aggregate."""

    __tablename__ = "maintenance_plan"

    target_type: Mapped[MaintenanceTargetType] = mapped_column(
        Enum(MaintenanceTargetType, native_enum=False, length=40),
        nullable=False,
    )

    target_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    status: Mapped[MaintenancePlanStatus] = mapped_column(
        Enum(MaintenancePlanStatus, native_enum=False, length=20),
        nullable=False,
        default=MaintenancePlanStatus.DRAFT,
    )

    requirements: Mapped[list["MaintenanceRequirementModel"]] = relationship(
        "MaintenanceRequirementModel",
        back_populates="plan",
        cascade="all, delete-orphan",
        single_parent=True,
    )
