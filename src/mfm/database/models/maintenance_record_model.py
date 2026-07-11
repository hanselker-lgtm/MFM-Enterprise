"""SQLAlchemy ORM model for immutable maintenance completion records."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.maintenance.performer_reference_type import PerformerReferenceType
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType

if TYPE_CHECKING:
    from mfm.database.models.work_order_model import WorkOrderModel


class MaintenanceRecordModel(BaseModel):
    """Persistence model for completion records."""

    __tablename__ = "maintenance_record"

    work_order_id: Mapped[UUID] = mapped_column(
        ForeignKey("work_order.id"),
        nullable=False,
        index=True,
    )

    maintenance_requirement_id: Mapped[UUID | None] = mapped_column(
        nullable=True,
        index=True,
    )

    target_type: Mapped[MaintenanceTargetType] = mapped_column(
        Enum(MaintenanceTargetType, native_enum=False, length=40),
        nullable=False,
    )
    target_id: Mapped[UUID] = mapped_column(nullable=False, index=True)

    completed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
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
    finding: Mapped[str | None] = mapped_column(String(4000), nullable=True)
    replacement_may_be_required: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    work_order: Mapped["WorkOrderModel"] = relationship(
        "WorkOrderModel",
        back_populates="records",
    )
