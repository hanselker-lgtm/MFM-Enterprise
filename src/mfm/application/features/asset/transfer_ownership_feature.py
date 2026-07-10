"""Transfer ownership feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.asset.create_asset import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.asset.create_asset import RepositoryException as ServiceRepositoryException
from mfm.application.asset.create_asset import ValidationException as ServiceValidationException
from mfm.application.asset.transfer_asset import TransferAssetRequest as ServiceRequest
from mfm.application.asset.transfer_asset import TransferAssetResponse as ServiceResponse
from mfm.application.asset.transfer_asset import TransferAssetUseCase


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class TransferOwnershipRequest:
    asset_id: UUID
    owner_id: UUID | None

    def validate(self) -> None:
        if not isinstance(self.asset_id, UUID):
            raise ValidationException("asset_id must be UUID")
        if self.owner_id is not None and not isinstance(self.owner_id, UUID):
            raise ValidationException("owner_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class TransferOwnershipResponse:
    asset_id: UUID
    owner_id: UUID | None


class TransferOwnershipService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class TransferOwnershipFeature:
    """Feature facade for ownership transfers with standardized API behavior."""

    def __init__(self, *, service: TransferOwnershipService) -> None:
        self._service = service

    def execute(self, request: TransferOwnershipRequest) -> TransferOwnershipResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    asset_id=request.asset_id,
                    owner_id=request.owner_id,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Transfer ownership feature failed") from exc

        return TransferOwnershipResponse(
            asset_id=service_response.asset_id,
            owner_id=service_response.owner_id,
        )
