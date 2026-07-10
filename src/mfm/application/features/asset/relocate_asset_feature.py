"""Relocate asset feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.asset.create_asset import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.asset.create_asset import RepositoryException as ServiceRepositoryException
from mfm.application.asset.create_asset import ValidationException as ServiceValidationException
from mfm.application.asset.relocate_asset import RelocateAssetRequest as ServiceRequest
from mfm.application.asset.relocate_asset import RelocateAssetResponse as ServiceResponse
from mfm.application.asset.relocate_asset import RelocateAssetUseCase


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


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


class RelocateAssetService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class RelocateAssetFeature:
    """Feature facade for asset relocation with standardized API behavior."""

    def __init__(self, *, service: RelocateAssetService) -> None:
        self._service = service

    def execute(self, request: RelocateAssetRequest) -> RelocateAssetResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    asset_id=request.asset_id,
                    location=request.location,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Relocate asset feature failed") from exc

        return RelocateAssetResponse(
            asset_id=service_response.asset_id,
            location=service_response.location,
        )
