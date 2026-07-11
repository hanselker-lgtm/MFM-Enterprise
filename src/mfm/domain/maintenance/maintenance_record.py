"""Immutable maintenance completion record."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from mfm.domain.maintenance.identifiers import MaintenanceRecordId
from mfm.domain.maintenance.identifiers import MaintenanceRequirementId
from mfm.domain.maintenance.identifiers import WorkOrderId
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.domain.maintenance.performer_reference import PerformerReference


@dataclass(frozen=True, slots=True)
class MaintenanceRecord:
    """Permanent immutable completion record owned by WorkOrder."""

    id: MaintenanceRecordId
    work_order_id: WorkOrderId
    maintenance_requirement_id: MaintenanceRequirementId | None
    maintenance_target: MaintenanceTarget
    completed_at: datetime
    performed_by: PerformerReference | None = None
    notes: str | None = None
    finding: str | None = None
    replacement_may_be_required: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.id, MaintenanceRecordId):
            object.__setattr__(self, "id", MaintenanceRecordId(self.id))

        if not isinstance(self.work_order_id, WorkOrderId):
            object.__setattr__(self, "work_order_id", WorkOrderId(self.work_order_id))

        if (
            self.maintenance_requirement_id is not None
            and not isinstance(self.maintenance_requirement_id, MaintenanceRequirementId)
        ):
            object.__setattr__(
                self,
                "maintenance_requirement_id",
                MaintenanceRequirementId(self.maintenance_requirement_id),
            )

        if not isinstance(self.maintenance_target, MaintenanceTarget):
            raise TypeError("maintenance_target must be MaintenanceTarget")

        if not isinstance(self.completed_at, datetime):
            raise TypeError("completed_at must be datetime")

        if self.performed_by is not None and not isinstance(
            self.performed_by, PerformerReference
        ):
            raise TypeError("performed_by must be PerformerReference or None")

        if self.notes is not None and not isinstance(self.notes, str):
            raise TypeError("notes must be string or None")
        if self.finding is not None and not isinstance(self.finding, str):
            raise TypeError("finding must be string or None")
        if not isinstance(self.replacement_may_be_required, bool):
            raise TypeError("replacement_may_be_required must be bool")
