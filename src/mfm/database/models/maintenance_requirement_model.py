"""SQLAlchemy ORM model for maintenance requirements."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.maintenance.maintenance_due_basis import MaintenanceDueBasis
from mfm.domain.maintenance.maintenance_interval_type import MaintenanceIntervalType
from mfm.domain.maintenance.maintenance_requirement_status import (
    MaintenanceRequirementStatus,
)
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType
from mfm.domain.maintenance.maintenance_type import MaintenanceType

if TYPE_CHECKING:
    from mfm.database.models.maintenance_plan_model import MaintenancePlanModel


class MaintenanceRequirementModel(BaseModel):
    """Persistence model for maintenance requirement entity."""

    __tablename__ = "maintenance_requirement"

    maintenance_plan_id: Mapped[UUID] = mapped_column(
        ForeignKey("maintenance_plan.id"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)

    target_type: Mapped[MaintenanceTargetType] = mapped_column(
        Enum(MaintenanceTargetType, native_enum=False, length=40),
        nullable=False,
    )
    target_id: Mapped[UUID] = mapped_column(nullable=False, index=True)

    maintenance_type: Mapped[MaintenanceType] = mapped_column(
        Enum(MaintenanceType, native_enum=False, length=40),
        nullable=False,
    )

    interval_type: Mapped[MaintenanceIntervalType] = mapped_column(
        Enum(MaintenanceIntervalType, native_enum=False, length=40),
        nullable=False,
    )
    interval_value: Mapped[int] = mapped_column(Integer, nullable=False)

    due_basis: Mapped[MaintenanceDueBasis] = mapped_column(
        Enum(MaintenanceDueBasis, native_enum=False, length=30),
        nullable=False,
    )

    last_completed_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    last_completed_running_hours: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    next_due_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    next_due_running_hours: Mapped[int | None] = mapped_column(Integer, nullable=True)

    status: Mapped[MaintenanceRequirementStatus] = mapped_column(
        Enum(MaintenanceRequirementStatus, native_enum=False, length=20),
        nullable=False,
        default=MaintenanceRequirementStatus.ACTIVE,
    )

    instructions: Mapped[str | None] = mapped_column(String(4000), nullable=True)
    notes: Mapped[str | None] = mapped_column(String(4000), nullable=True)

    plan: Mapped["MaintenancePlanModel"] = relationship(
        "MaintenancePlanModel",
        back_populates="requirements",
    )
