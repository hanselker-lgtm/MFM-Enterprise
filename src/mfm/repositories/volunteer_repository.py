"""Volunteer Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.organization.volunteer import Volunteer


class VolunteerRepository(ABC):
    """Repository contract for Volunteer aggregates."""

    @abstractmethod
    def add(self, volunteer: Volunteer) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, volunteer_id: UUID) -> Volunteer | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, volunteer: Volunteer) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, volunteer_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, volunteer_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Volunteer]:
        raise NotImplementedError

    @abstractmethod
    def search(self, text: str) -> list[Volunteer]:
        raise NotImplementedError
