"""WorkOrder aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from datetime import datetime
from uuid import UUID

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.maintenance.events import MaintenanceRecordCreated
from mfm.domain.maintenance.events import WorkOrderCancelled
from mfm.domain.maintenance.events import WorkOrderCompleted
from mfm.domain.maintenance.events import WorkOrderCreated
from mfm.domain.maintenance.events import WorkOrderStarted
from mfm.domain.maintenance.exceptions import InvalidWorkOrderChronologyError
from mfm.domain.maintenance.exceptions import InvalidWorkOrderLifecycleError
from mfm.domain.maintenance.identifiers import MaintenanceRecordId
from mfm.domain.maintenance.identifiers import MaintenanceRequirementId
from mfm.domain.maintenance.identifiers import WorkOrderId
from mfm.domain.maintenance.maintenance_record import MaintenanceRecord
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.domain.maintenance.performer_reference import PerformerReference
from mfm.domain.maintenance.work_order_status import WorkOrderStatus


@dataclass(slots=True)
class WorkOrder(AggregateRoot):
    """Aggregate root for maintenance work execution lifecycle."""

    maintenance_target: MaintenanceTarget
    id: WorkOrderId = field(default_factory=WorkOrderId.new)
    maintenance_requirement_id: MaintenanceRequirementId | None = None
    title: str = ""
    description: str = ""
    status: WorkOrderStatus = WorkOrderStatus.PLANNED
    planned_date: date | None = None
    started_at: datetime | None = None
    completed_at: datetime | None = None
    performed_by: PerformerReference | None = None
    notes: str | None = None
    _record: MaintenanceRecord | None = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, WorkOrderId):
            self.id = WorkOrderId(self.id)

        if self.maintenance_requirement_id is not None and not isinstance(
            self.maintenance_requirement_id,
            MaintenanceRequirementId,
        ):
            self.maintenance_requirement_id = MaintenanceRequirementId(
                self.maintenance_requirement_id
            )

        if not isinstance(self.maintenance_target, MaintenanceTarget):
            raise TypeError("maintenance_target must be MaintenanceTarget")

        self.title = self._normalize_text(self.title, "title")
        self.description = self._normalize_text(self.description, "description")

        if not isinstance(self.status, WorkOrderStatus):
            self.status = WorkOrderStatus(str(self.status).upper())

        if self.planned_date is not None and not isinstance(self.planned_date, date):
            raise InvalidWorkOrderChronologyError("planned_date must be date or None")

        if self.started_at is not None and not isinstance(self.started_at, datetime):
            raise InvalidWorkOrderChronologyError("started_at must be datetime or None")
        if self.completed_at is not None and not isinstance(self.completed_at, datetime):
            raise InvalidWorkOrderChronologyError("completed_at must be datetime or None")

        if self.started_at is not None and self.completed_at is not None:
            if self.completed_at < self.started_at:
                raise InvalidWorkOrderChronologyError(
                    "completed_at cannot be before started_at"
                )

        if self.performed_by is not None and not isinstance(
            self.performed_by,
            PerformerReference,
        ):
            raise TypeError("performed_by must be PerformerReference or None")

        if self.notes is not None and not isinstance(self.notes, str):
            raise TypeError("notes must be string or None")
        if isinstance(self.notes, str):
            self.notes = self.notes.strip() or None

        self._validate_initial_state()

        self.add_event(WorkOrderCreated(work_order_id=self.id.value))

    @staticmethod
    def _normalize_text(value: str, field_name: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be string")
        normalized = value.strip()
        if not normalized:
            raise ValueError(f"{field_name} must be a non-empty string")
        return normalized

    def _validate_initial_state(self) -> None:
        if self.status is WorkOrderStatus.PLANNED:
            if self.started_at is not None or self.completed_at is not None:
                raise InvalidWorkOrderLifecycleError(
                    "planned work order cannot have started/completed timestamps"
                )
            return

        if self.status is WorkOrderStatus.OPEN:
            if self.started_at is not None or self.completed_at is not None:
                raise InvalidWorkOrderLifecycleError(
                    "open work order cannot have started/completed timestamps"
                )
            return

        if self.status is WorkOrderStatus.IN_PROGRESS:
            if self.started_at is None:
                raise InvalidWorkOrderLifecycleError(
                    "in progress work order requires started_at"
                )
            if self.completed_at is not None:
                raise InvalidWorkOrderLifecycleError(
                    "in progress work order cannot have completed_at"
                )
            return

        if self.status is WorkOrderStatus.COMPLETED:
            if self.started_at is None or self.completed_at is None:
                raise InvalidWorkOrderLifecycleError(
                    "completed work order requires started_at and completed_at"
                )
            return

        if self.status is WorkOrderStatus.CANCELLED:
            if self.completed_at is not None:
                raise InvalidWorkOrderLifecycleError(
                    "cancelled work order cannot have completed_at"
                )

    @property
    def maintenance_record(self) -> MaintenanceRecord | None:
        return self._record

    def open(self) -> None:
        if self.status is not WorkOrderStatus.PLANNED:
            raise InvalidWorkOrderLifecycleError("only planned work order can be opened")
        self.status = WorkOrderStatus.OPEN

    def start(self, started_at: datetime) -> None:
        if self.status is not WorkOrderStatus.OPEN:
            raise InvalidWorkOrderLifecycleError("only open work order can be started")
        if not isinstance(started_at, datetime):
            raise InvalidWorkOrderChronologyError("started_at must be datetime")

        self.started_at = started_at
        self.status = WorkOrderStatus.IN_PROGRESS
        self.add_event(WorkOrderStarted(work_order_id=self.id.value, started_at=started_at))

    def complete(
        self,
        *,
        completed_at: datetime,
        performed_by: PerformerReference | None = None,
        notes: str | None = None,
        finding: str | None = None,
        replacement_may_be_required: bool = False,
    ) -> MaintenanceRecord:
        if self.status is WorkOrderStatus.CANCELLED:
            raise InvalidWorkOrderLifecycleError(
                "cancelled work order cannot be completed"
            )
        if self.status is not WorkOrderStatus.IN_PROGRESS:
            raise InvalidWorkOrderLifecycleError(
                "only in-progress work order can be completed"
            )
        if self.started_at is None:
            raise InvalidWorkOrderLifecycleError("started_at is required before completion")
        if not isinstance(completed_at, datetime):
            raise InvalidWorkOrderChronologyError("completed_at must be datetime")
        if completed_at < self.started_at:
            raise InvalidWorkOrderChronologyError(
                "completed_at cannot be before started_at"
            )

        self.completed_at = completed_at
        self.status = WorkOrderStatus.COMPLETED
        self.performed_by = performed_by
        if notes is not None:
            if not isinstance(notes, str):
                raise TypeError("notes must be string or None")
            self.notes = notes.strip() or None

        record = MaintenanceRecord(
            id=MaintenanceRecordId.new(),
            work_order_id=self.id,
            maintenance_requirement_id=self.maintenance_requirement_id,
            maintenance_target=self.maintenance_target,
            completed_at=completed_at,
            performed_by=performed_by,
            notes=self.notes,
            finding=(finding.strip() if isinstance(finding, str) and finding.strip() else None),
            replacement_may_be_required=replacement_may_be_required,
        )
        self._record = record

        self.add_event(WorkOrderCompleted(work_order_id=self.id.value, completed_at=completed_at))
        self.add_event(
            MaintenanceRecordCreated(
                maintenance_record_id=record.id.value,
                work_order_id=self.id.value,
            )
        )
        return record

    def cancel(self, *, notes: str | None = None) -> None:
        if self.status in {WorkOrderStatus.COMPLETED, WorkOrderStatus.CANCELLED}:
            raise InvalidWorkOrderLifecycleError(
                "completed or cancelled work order cannot be cancelled"
            )
        if self.status not in {WorkOrderStatus.PLANNED, WorkOrderStatus.OPEN}:
            raise InvalidWorkOrderLifecycleError(
                "only planned or open work order can be cancelled"
            )

        if notes is not None:
            if not isinstance(notes, str):
                raise TypeError("notes must be string or None")
            self.notes = notes.strip() or None

        self.status = WorkOrderStatus.CANCELLED
        self.add_event(WorkOrderCancelled(work_order_id=self.id.value))
