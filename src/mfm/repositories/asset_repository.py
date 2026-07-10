"""Asset Repository interface."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.asset.asset import Asset


class AssetRepository(ABC):
    """Repository contract for Asset aggregates."""

    @abstractmethod
    def add(self, asset: Asset) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, asset_id: UUID) -> Asset | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_asset_number(self, asset_number: str) -> Asset | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, asset: Asset) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, asset_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, asset_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Asset]:
        raise NotImplementedError

    @abstractmethod
    def search(self, text: str) -> list[Asset]:
        raise NotImplementedError
