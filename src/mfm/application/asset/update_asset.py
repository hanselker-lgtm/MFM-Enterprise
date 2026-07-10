"""Update Asset use case."""

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
from mfm.domain.asset.asset_status import AssetStatus


@dataclass(frozen=True, slots=True)
class UpdateAssetRequest:
    asset_id: UUID
    name: str

    def validate(self) -> None:
        if not isinstance(self.asset_id, UUID):
            raise ValidationException("asset_id must be UUID")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")


@dataclass(frozen=True, slots=True)
class UpdateAssetResponse:
    asset_id: UUID
    name: str
    status: AssetStatus


@dataclass(slots=True)
class AssetUpdatedEvent(DomainEvent):
    asset_id: UUID = field(default_factory=uuid4)


class AssetRepository(Protocol):
    def get_by_id(self, asset_id: UUID) -> Asset | None: ...

    def update(self, asset: Asset) -> None: ...


class UpdateAssetUseCase:
    """Update asset aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: UpdateAssetRequest) -> UpdateAssetResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: AssetRepository = uow.asset_repository

                asset = repository.get_by_id(request.asset_id)
                if asset is None:
                    raise BusinessRuleViolation(f"Asset {request.asset_id} does not exist")

                asset.rename(request.name)
                repository.update(asset)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Update asset failed") from exc

        self._dispatcher.dispatch(AssetUpdatedEvent(asset_id=asset.id.value))

        return UpdateAssetResponse(
            asset_id=asset.id.value,
            name=asset.name,
            status=asset.status,
        )
