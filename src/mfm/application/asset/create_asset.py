"""Create Asset use case."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from typing import Protocol
from uuid import UUID
from uuid import uuid4

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_location import AssetLocation
from mfm.domain.asset.asset_number import AssetNumber
from mfm.domain.asset.asset_status import AssetStatus


class ApplicationException(Exception):
    """Base exception for asset application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository/persistence failures."""


@dataclass(frozen=True, slots=True)
class CreateAssetRequest:
    asset_number: str
    name: str
    description: str
    category: AssetCategory
    owner_id: UUID | None
    location: str
    acquisition_date: date | None = None

    def validate(self) -> None:
        if not isinstance(self.asset_number, str) or not self.asset_number.strip():
            raise ValidationException("asset_number must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.description, str):
            raise ValidationException("description must be a string")
        if not isinstance(self.category, AssetCategory):
            raise ValidationException("category must be AssetCategory")
        if self.owner_id is not None and not isinstance(self.owner_id, UUID):
            raise ValidationException("owner_id must be UUID or None")
        if not isinstance(self.location, str) or not self.location.strip():
            raise ValidationException("location must be a non-empty string")
        if self.acquisition_date is not None and not isinstance(self.acquisition_date, date):
            raise ValidationException("acquisition_date must be date or None")


@dataclass(frozen=True, slots=True)
class CreateAssetResponse:
    asset_id: UUID
    asset_number: str
    name: str
    status: AssetStatus


@dataclass(slots=True)
class AssetCreatedEvent(DomainEvent):
    asset_id: UUID = field(default_factory=uuid4)
    asset_number: str = ""


class AssetRepository(Protocol):
    def add(self, asset: Asset) -> None: ...

    def get_by_asset_number(self, asset_number: str) -> Asset | None: ...


class CreateAssetUseCase:
    """Create asset aggregate in one transactional boundary."""

    def __init__(
        self,
        *,
        unit_of_work: AbstractUnitOfWork,
        dispatcher: DomainEventDispatcher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._dispatcher = dispatcher

    def execute(self, request: CreateAssetRequest) -> CreateAssetResponse:
        request.validate()

        number = AssetNumber(request.asset_number)

        try:
            with self._unit_of_work as uow:
                repository: AssetRepository = uow.asset_repository

                if repository.get_by_asset_number(number.value) is not None:
                    raise BusinessRuleViolation(
                        f"Asset number {number.value} already exists"
                    )

                asset = Asset(
                    asset_number=number,
                    name=request.name,
                    description=request.description,
                    category=request.category,
                    owner_id=request.owner_id,
                    location=AssetLocation(request.location),
                    acquisition_date=request.acquisition_date,
                )

                repository.add(asset)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except Exception as exc:
            raise RepositoryException("Create asset failed") from exc

        self._dispatcher.dispatch(
            AssetCreatedEvent(
                asset_id=asset.id.value,
                asset_number=asset.asset_number.value,
            )
        )

        return CreateAssetResponse(
            asset_id=asset.id.value,
            asset_number=asset.asset_number.value,
            name=asset.name,
            status=asset.status,
        )
