"""Create asset feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.asset.create_asset import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.asset.create_asset import CreateAssetRequest as ServiceRequest
from mfm.application.asset.create_asset import CreateAssetResponse as ServiceResponse
from mfm.application.asset.create_asset import CreateAssetUseCase
from mfm.application.asset.create_asset import RepositoryException as ServiceRepositoryException
from mfm.application.asset.create_asset import ValidationException as ServiceValidationException
from mfm.domain.asset.asset_category import AssetCategory


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


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
    status: str


class CreateAssetService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CreateAssetFeature:
    """Feature facade for asset creation with standardized API behavior."""

    def __init__(self, *, service: CreateAssetService) -> None:
        self._service = service

    def execute(self, request: CreateAssetRequest) -> CreateAssetResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    asset_number=request.asset_number,
                    name=request.name,
                    description=request.description,
                    category=request.category,
                    owner_id=request.owner_id,
                    location=request.location,
                    acquisition_date=request.acquisition_date,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create asset feature failed") from exc

        return CreateAssetResponse(
            asset_id=service_response.asset_id,
            asset_number=service_response.asset_number,
            name=service_response.name,
            status=service_response.status.value,
        )
