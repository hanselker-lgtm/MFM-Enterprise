"""Maintenance domain events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class MaintenanceRequirementCreated(DomainEvent):
    requirement_id: UUID | None = None
    maintenance_plan_id: UUID | None = None


@dataclass(slots=True)
class MaintenanceBecameDue(DomainEvent):
    requirement_id: UUID | None = None
    maintenance_plan_id: UUID | None = None


@dataclass(slots=True)
class WorkOrderCreated(DomainEvent):
    work_order_id: UUID | None = None


@dataclass(slots=True)
class WorkOrderStarted(DomainEvent):
    work_order_id: UUID | None = None
    started_at: datetime | None = None


@dataclass(slots=True)
class WorkOrderCompleted(DomainEvent):
    work_order_id: UUID | None = None
    completed_at: datetime | None = None


@dataclass(slots=True)
class WorkOrderCancelled(DomainEvent):
    work_order_id: UUID | None = None


@dataclass(slots=True)
class MaintenanceRecordCreated(DomainEvent):
    maintenance_record_id: UUID | None = None
    work_order_id: UUID | None = None
