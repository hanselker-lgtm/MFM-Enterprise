"""Reactivate inventory item feature facade following Public API Standard."""

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
from mfm.application.inventory.reactivate_inventory_item import (
    ReactivateInventoryItemRequest as ServiceRequest,
)
from mfm.application.inventory.reactivate_inventory_item import (
    ReactivateInventoryItemResponse as ServiceResponse,
)
from mfm.application.inventory.reactivate_inventory_item import ReactivateInventoryItemUseCase


@dataclass(frozen=True, slots=True)
class ReactivateInventoryItemRequest:
    inventory_item_id: UUID

    def validate(self) -> None:
        if not isinstance(self.inventory_item_id, UUID):
            raise ValidationException("inventory_item_id must be UUID")


@dataclass(frozen=True, slots=True)
class ReactivateInventoryItemResponse:
    inventory_item: InventoryItemResponse


class ReactivateInventoryItemService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ReactivateInventoryItemFeature:
    """Feature facade for inventory item reactivation."""

    def __init__(self, *, service: ReactivateInventoryItemService) -> None:
        self._service = service

    def execute(
        self,
        request: ReactivateInventoryItemRequest,
    ) -> ReactivateInventoryItemResponse:
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
            raise RepositoryException("Reactivate inventory item feature failed") from exc

        return ReactivateInventoryItemResponse(
            inventory_item=to_feature_inventory_item_response(service_response.inventory_item)
        )
