"""Role Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.organization.role import Role


class RoleRepository(ABC):
    """Repository contract for Role aggregates."""

    @abstractmethod
    def add(self, role: Role) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, role_id: UUID) -> Role | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, role: Role) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, role_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, role_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Role]:
        raise NotImplementedError

    @abstractmethod
    def search(self, text: str) -> list[Role]:
        raise NotImplementedError
