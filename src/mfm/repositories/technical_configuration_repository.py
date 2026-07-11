"""Technical Configuration repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.technical_configuration.technical_configuration import (
    TechnicalConfiguration,
)


class TechnicalConfigurationRepository(ABC):
    """Repository contract for TechnicalConfiguration aggregates."""

    @abstractmethod
    def add(self, configuration: TechnicalConfiguration) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, configuration_id: UUID) -> TechnicalConfiguration | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_vessel_id(self, vessel_id: UUID) -> TechnicalConfiguration | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, configuration: TechnicalConfiguration) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, configuration_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, configuration_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[TechnicalConfiguration]:
        raise NotImplementedError

    @abstractmethod
    def search(self, text: str) -> list[TechnicalConfiguration]:
        raise NotImplementedError
