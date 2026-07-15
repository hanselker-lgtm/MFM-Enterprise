"""Deactivate inventory item feature facade following Public API Standard."""

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
from mfm.application.inventory.deactivate_inventory_item import (
    DeactivateInventoryItemRequest as ServiceRequest,
)
from mfm.application.inventory.deactivate_inventory_item import (
    DeactivateInventoryItemResponse as ServiceResponse,
)
from mfm.application.inventory.deactivate_inventory_item import DeactivateInventoryItemUseCase


@dataclass(frozen=True, slots=True)
class DeactivateInventoryItemRequest:
    inventory_item_id: UUID

    def validate(self) -> None:
        if not isinstance(self.inventory_item_id, UUID):
            raise ValidationException("inventory_item_id must be UUID")


@dataclass(frozen=True, slots=True)
class DeactivateInventoryItemResponse:
    inventory_item: InventoryItemResponse


class DeactivateInventoryItemService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class DeactivateInventoryItemFeature:
    """Feature facade for inventory item deactivation."""

    def __init__(self, *, service: DeactivateInventoryItemService) -> None:
        self._service = service

    def execute(
        self,
        request: DeactivateInventoryItemRequest,
    ) -> DeactivateInventoryItemResponse:
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
            raise RepositoryException("Deactivate inventory item feature failed") from exc

        return DeactivateInventoryItemResponse(
            inventory_item=to_feature_inventory_item_response(service_response.inventory_item)
        )
