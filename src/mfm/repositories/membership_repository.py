"""Membership Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.membership.membership import Membership


class MembershipRepository(ABC):
    """Repository contract for Membership aggregates."""

    @abstractmethod
    def add(self, membership: Membership) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, membership: Membership) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, membership_id: UUID) -> Membership | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Membership]:
        raise NotImplementedError

    @abstractmethod
    def list_by_member(self, member_id: UUID) -> list[Membership]:
        raise NotImplementedError

    @abstractmethod
    def list_active(self) -> list[Membership]:
        raise NotImplementedError

    @abstractmethod
    def exists(self, membership_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, membership_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def member_exists(self, member_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def membership_type_exists(self, membership_type_id: UUID) -> bool:
        raise NotImplementedError
