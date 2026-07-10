"""Transfer Asset ownership use case."""

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


@dataclass(frozen=True, slots=True)
class TransferAssetRequest:
    asset_id: UUID
    owner_id: UUID | None

    def validate(self) -> None:
        if not isinstance(self.asset_id, UUID):
            raise ValidationException("asset_id must be UUID")
        if self.owner_id is not None and not isinstance(self.owner_id, UUID):
            raise ValidationException("owner_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class TransferAssetResponse:
    asset_id: UUID
    owner_id: UUID | None


@dataclass(slots=True)
class AssetTransferredEvent(DomainEvent):
    asset_id: UUID = field(default_factory=uuid4)
    owner_id: UUID | None = None


class AssetRepository(Protocol):
    def get_by_id(self, asset_id: UUID) -> Asset | None: ...

    def update(self, asset: Asset) -> None: ...


class TransferAssetUseCase:
    """Transfer asset ownership in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: TransferAssetRequest) -> TransferAssetResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: AssetRepository = uow.asset_repository

                asset = repository.get_by_id(request.asset_id)
                if asset is None:
                    raise BusinessRuleViolation(f"Asset {request.asset_id} does not exist")

                asset.change_owner(request.owner_id)
                repository.update(asset)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except Exception as exc:
            raise RepositoryException("Transfer asset failed") from exc

        self._dispatcher.dispatch(
            AssetTransferredEvent(asset_id=asset.id.value, owner_id=asset.owner_id)
        )

        return TransferAssetResponse(asset_id=asset.id.value, owner_id=asset.owner_id)
