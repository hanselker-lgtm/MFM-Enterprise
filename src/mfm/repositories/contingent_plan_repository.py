"""ContingentPlan Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.contingent.contingent_plan import ContingentPlan


class ContingentPlanRepository(ABC):
    """Repository contract for ContingentPlan aggregates."""

    @abstractmethod
    def add(self, plan: ContingentPlan) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, plan: ContingentPlan) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, plan_id: UUID) -> ContingentPlan | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[ContingentPlan]:
        raise NotImplementedError

    @abstractmethod
    def list_by_membership_type(self, membership_type_id: UUID) -> list[ContingentPlan]:
        raise NotImplementedError

    @abstractmethod
    def exists(self, plan_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, plan_id: UUID) -> None:
        raise NotImplementedError
