"""Repository contract for WorkOrder aggregates."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.maintenance.work_order import WorkOrder


class WorkOrderRepository(ABC):
    """Persistence contract for WorkOrder aggregate roots."""

    @abstractmethod
    def add(self, work_order: WorkOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, work_order_id: UUID) -> WorkOrder | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, work_order: WorkOrder) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, work_order_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, work_order_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[WorkOrder]:
        raise NotImplementedError

    @abstractmethod
    def get_by_maintenance_requirement_id(
        self,
        maintenance_requirement_id: UUID,
    ) -> list[WorkOrder]:
        raise NotImplementedError
