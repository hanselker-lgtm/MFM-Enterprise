"""Repository contract for MaintenancePlan aggregates."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.maintenance.maintenance_plan import MaintenancePlan
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget


class MaintenancePlanRepository(ABC):
    """Persistence contract for MaintenancePlan aggregate roots."""

    @abstractmethod
    def add(self, plan: MaintenancePlan) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, plan_id: UUID) -> MaintenancePlan | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, plan: MaintenancePlan) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, plan_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, plan_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[MaintenancePlan]:
        raise NotImplementedError

    @abstractmethod
    def get_by_target(self, target: MaintenanceTarget) -> list[MaintenancePlan]:
        raise NotImplementedError
