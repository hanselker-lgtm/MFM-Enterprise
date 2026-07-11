"""Vessel Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.fleet.vessel import Vessel


class VesselRepository(ABC):
    """Repository contract for Vessel aggregates."""

    @abstractmethod
    def add(self, vessel: Vessel) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, vessel_id: UUID) -> Vessel | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_registration(self, registration: str) -> Vessel | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, vessel: Vessel) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, vessel_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, vessel_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Vessel]:
        raise NotImplementedError

    @abstractmethod
    def search(self, text: str) -> list[Vessel]:
        raise NotImplementedError
