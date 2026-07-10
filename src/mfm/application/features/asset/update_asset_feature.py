"""Update asset feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.asset.create_asset import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.asset.create_asset import RepositoryException as ServiceRepositoryException
from mfm.application.asset.create_asset import ValidationException as ServiceValidationException
from mfm.application.asset.update_asset import UpdateAssetRequest as ServiceRequest
from mfm.application.asset.update_asset import UpdateAssetResponse as ServiceResponse
from mfm.application.asset.update_asset import UpdateAssetUseCase


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


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
    status: str


class UpdateAssetService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateAssetFeature:
    """Feature facade for asset updates with standardized API behavior."""

    def __init__(self, *, service: UpdateAssetService) -> None:
        self._service = service

    def execute(self, request: UpdateAssetRequest) -> UpdateAssetResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    asset_id=request.asset_id,
                    name=request.name,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update asset feature failed") from exc

        return UpdateAssetResponse(
            asset_id=service_response.asset_id,
            name=service_response.name,
            status=service_response.status.value,
        )
