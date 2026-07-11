"""Repository contract for Voyage aggregates."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.voyages.voyage import Voyage


class VoyageRepository(ABC):
    """Persistence contract for Voyage aggregate roots."""

    @abstractmethod
    def add(self, voyage: Voyage) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, voyage_id: UUID) -> Voyage | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, voyage: Voyage) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, voyage_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Voyage]:
        raise NotImplementedError

    @abstractmethod
    def get_by_vessel(self, vessel_id: UUID) -> list[Voyage]:
        raise NotImplementedError
