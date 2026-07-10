"""Retire asset feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.asset.create_asset import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.asset.create_asset import RepositoryException as ServiceRepositoryException
from mfm.application.asset.create_asset import ValidationException as ServiceValidationException
from mfm.application.asset.retire_asset import RetireAssetRequest as ServiceRequest
from mfm.application.asset.retire_asset import RetireAssetResponse as ServiceResponse
from mfm.application.asset.retire_asset import RetireAssetUseCase


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class RetireAssetRequest:
    asset_id: UUID
    retired_on: date

    def validate(self) -> None:
        if not isinstance(self.asset_id, UUID):
            raise ValidationException("asset_id must be UUID")
        if not isinstance(self.retired_on, date):
            raise ValidationException("retired_on must be date")


@dataclass(frozen=True, slots=True)
class RetireAssetResponse:
    asset_id: UUID
    status: str
    retired_date: date | None


class RetireAssetService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class RetireAssetFeature:
    """Feature facade for asset retirement with standardized API behavior."""

    def __init__(self, *, service: RetireAssetService) -> None:
        self._service = service

    def execute(self, request: RetireAssetRequest) -> RetireAssetResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    asset_id=request.asset_id,
                    retired_on=request.retired_on,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Retire asset feature failed") from exc

        return RetireAssetResponse(
            asset_id=service_response.asset_id,
            status=service_response.status.value,
            retired_date=service_response.retired_date,
        )
