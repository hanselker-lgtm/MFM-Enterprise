"""Member Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.member.member import Member


class MemberRepository(ABC):
    """Repository contract for Member aggregates."""

    @abstractmethod
    def add(self, member: Member) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, member: Member) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, member_id: UUID) -> Member | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_number(self, member_number: str) -> Member | None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Member]:
        raise NotImplementedError

    @abstractmethod
    def exists(self, member_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete(self, member_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def contact_exists(self, contact_id: UUID) -> bool:
        raise NotImplementedError
