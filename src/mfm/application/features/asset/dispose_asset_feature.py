"""Dispose asset feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.asset.create_asset import BusinessRuleViolation as ServiceBusinessRuleViolation
from mfm.application.asset.create_asset import RepositoryException as ServiceRepositoryException
from mfm.application.asset.create_asset import ValidationException as ServiceValidationException
from mfm.application.asset.dispose_asset import DisposeAssetRequest as ServiceRequest
from mfm.application.asset.dispose_asset import DisposeAssetResponse as ServiceResponse
from mfm.application.asset.dispose_asset import DisposeAssetUseCase


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class DisposeAssetRequest:
    asset_id: UUID
    disposed_on: date | None = None

    def validate(self) -> None:
        if not isinstance(self.asset_id, UUID):
            raise ValidationException("asset_id must be UUID")
        if self.disposed_on is not None and not isinstance(self.disposed_on, date):
            raise ValidationException("disposed_on must be date or None")


@dataclass(frozen=True, slots=True)
class DisposeAssetResponse:
    asset_id: UUID
    status: str
    retired_date: date | None


class DisposeAssetService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class DisposeAssetFeature:
    """Feature facade for asset disposal with standardized API behavior."""

    def __init__(self, *, service: DisposeAssetService) -> None:
        self._service = service

    def execute(self, request: DisposeAssetRequest) -> DisposeAssetResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    asset_id=request.asset_id,
                    disposed_on=request.disposed_on,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Dispose asset feature failed") from exc

        return DisposeAssetResponse(
            asset_id=service_response.asset_id,
            status=service_response.status.value,
            retired_date=service_response.retired_date,
        )
