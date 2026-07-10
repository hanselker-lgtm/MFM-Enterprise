"""Committee Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.organization.committee import Committee


class CommitteeRepository(ABC):
    """Repository contract for Committee aggregates."""

    @abstractmethod
    def add(self, committee: Committee) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, committee_id: UUID) -> Committee | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, committee: Committee) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, committee_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, committee_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Committee]:
        raise NotImplementedError

    @abstractmethod
    def search(self, text: str) -> list[Committee]:
        raise NotImplementedError
