"""SQLAlchemy ORM model for work orders."""

from __future__ import annotations

from datetime import date
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.maintenance.performer_reference_type import PerformerReferenceType
from mfm.domain.maintenance.work_order_status import WorkOrderStatus
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType

if TYPE_CHECKING:
    from mfm.database.models.maintenance_record_model import MaintenanceRecordModel


class WorkOrderModel(BaseModel):
    """Persistence model for work order aggregate."""

    __tablename__ = "work_order"

    maintenance_requirement_id: Mapped[UUID | None] = mapped_column(
        nullable=True,
        index=True,
    )

    target_type: Mapped[MaintenanceTargetType] = mapped_column(
        Enum(MaintenanceTargetType, native_enum=False, length=40),
        nullable=False,
    )
    target_id: Mapped[UUID] = mapped_column(nullable=False, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)

    status: Mapped[WorkOrderStatus] = mapped_column(
        Enum(WorkOrderStatus, native_enum=False, length=20),
        nullable=False,
        default=WorkOrderStatus.PLANNED,
    )

    planned_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    performer_type: Mapped[PerformerReferenceType | None] = mapped_column(
        Enum(PerformerReferenceType, native_enum=False, length=40),
        nullable=True,
    )
    performer_id_or_external_key: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    performer_display_name_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(String(4000), nullable=True)

    records: Mapped[list["MaintenanceRecordModel"]] = relationship(
        "MaintenanceRecordModel",
        back_populates="work_order",
        cascade="all, delete-orphan",
        single_parent=True,
    )
