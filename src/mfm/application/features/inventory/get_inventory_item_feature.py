"""Get inventory item feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.features.inventory.create_inventory_item_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    InventoryItemResponse,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    RepositoryException,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    ValidationException,
)
from mfm.application.features.inventory.create_inventory_item_feature import (
    to_feature_inventory_item_response,
)
from mfm.application.inventory.create_inventory_item import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.inventory.create_inventory_item import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.inventory.create_inventory_item import (
    ValidationException as ServiceValidationException,
)
from mfm.application.inventory.get_inventory_item import GetInventoryItemRequest as ServiceRequest
from mfm.application.inventory.get_inventory_item import GetInventoryItemResponse as ServiceResponse
from mfm.application.inventory.get_inventory_item import GetInventoryItemUseCase


@dataclass(frozen=True, slots=True)
class GetInventoryItemRequest:
    inventory_item_id: UUID

    def validate(self) -> None:
        if not isinstance(self.inventory_item_id, UUID):
            raise ValidationException("inventory_item_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetInventoryItemResponse:
    inventory_item: InventoryItemResponse


class GetInventoryItemService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetInventoryItemFeature:
    """Feature facade for inventory item retrieval."""

    def __init__(self, *, service: GetInventoryItemService) -> None:
        self._service = service

    def execute(self, request: GetInventoryItemRequest) -> GetInventoryItemResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(inventory_item_id=request.inventory_item_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get inventory item feature failed") from exc

        return GetInventoryItemResponse(
            inventory_item=to_feature_inventory_item_response(service_response.inventory_item)
        )
