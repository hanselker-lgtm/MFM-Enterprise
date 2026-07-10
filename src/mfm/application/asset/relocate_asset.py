"""Relocate Asset use case."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Protocol
from uuid import UUID
from uuid import uuid4

from mfm.application.asset.create_asset import ApplicationException
from mfm.application.asset.create_asset import BusinessRuleViolation
from mfm.application.asset.create_asset import RepositoryException
from mfm.application.asset.create_asset import ValidationException
from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_location import AssetLocation


@dataclass(frozen=True, slots=True)
class RelocateAssetRequest:
    asset_id: UUID
    location: str

    def validate(self) -> None:
        if not isinstance(self.asset_id, UUID):
            raise ValidationException("asset_id must be UUID")
        if not isinstance(self.location, str) or not self.location.strip():
            raise ValidationException("location must be a non-empty string")


@dataclass(frozen=True, slots=True)
class RelocateAssetResponse:
    asset_id: UUID
    location: str


@dataclass(slots=True)
class AssetRelocatedEvent(DomainEvent):
    asset_id: UUID = field(default_factory=uuid4)
    location: str = ""


class AssetRepository(Protocol):
    def get_by_id(self, asset_id: UUID) -> Asset | None: ...

    def update(self, asset: Asset) -> None: ...


class RelocateAssetUseCase:
    """Relocate asset aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: RelocateAssetRequest) -> RelocateAssetResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: AssetRepository = uow.asset_repository

                asset = repository.get_by_id(request.asset_id)
                if asset is None:
                    raise BusinessRuleViolation(f"Asset {request.asset_id} does not exist")

                asset.change_location(AssetLocation(request.location))
                repository.update(asset)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Relocate asset failed") from exc

        self._dispatcher.dispatch(
            AssetRelocatedEvent(asset_id=asset.id.value, location=asset.location.value)
        )

        return RelocateAssetResponse(asset_id=asset.id.value, location=asset.location.value)
