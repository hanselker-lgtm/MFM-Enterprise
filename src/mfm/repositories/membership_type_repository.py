"""MembershipType Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.membership.membership_type import MembershipType


class MembershipTypeRepository(ABC):
    """Repository contract for MembershipType aggregates."""

    @abstractmethod
    def add(self, membership_type: MembershipType) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, membership_type: MembershipType) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, membership_type_id: UUID) -> MembershipType | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_code(self, code: str) -> MembershipType | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[MembershipType]:
        raise NotImplementedError

    @abstractmethod
    def exists(self, membership_type_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, membership_type_id: UUID) -> None:
        raise NotImplementedError
