"""Organization Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.organization.organization import Organization


class OrganizationRepository(ABC):
    """Repository contract for Organization aggregates."""

    @abstractmethod
    def add(self, organization: Organization) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, organization_id: UUID) -> Organization | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, organization: Organization) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, organization_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, organization_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Organization]:
        raise NotImplementedError

    @abstractmethod
    def search(self, text: str) -> list[Organization]:
        raise NotImplementedError
