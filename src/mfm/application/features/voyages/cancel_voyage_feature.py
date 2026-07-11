"""Cancel voyage feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.voyages.create_voyage_feature import BusinessRuleViolation
from mfm.application.features.voyages.create_voyage_feature import RepositoryException
from mfm.application.features.voyages.create_voyage_feature import ValidationException
from mfm.application.features.voyages.create_voyage_feature import VoyageResponse
from mfm.application.features.voyages.create_voyage_feature import to_feature_voyage_response
from mfm.application.voyages.create_voyage import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.voyages.create_voyage import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.voyages.create_voyage import (
    ValidationException as ServiceValidationException,
)
from mfm.application.voyages.cancel_voyage import CancelVoyageRequest as ServiceRequest
from mfm.application.voyages.cancel_voyage import CancelVoyageResponse as ServiceResponse
from mfm.application.voyages.cancel_voyage import CancelVoyageUseCase


@dataclass(frozen=True, slots=True)
class CancelVoyageRequest:
    voyage_id: UUID
    cancellation_reason: str
    cancelled_at: datetime
    cancelled_by_reference: str | None = None

    def validate(self) -> None:
        if not isinstance(self.voyage_id, UUID):
            raise ValidationException("voyage_id must be UUID")
        if not isinstance(self.cancellation_reason, str) or not self.cancellation_reason.strip():
            raise ValidationException("cancellation_reason must be a non-empty string")
        if not isinstance(self.cancelled_at, datetime):
            raise ValidationException("cancelled_at must be datetime")
        if self.cancelled_by_reference is not None and not isinstance(
            self.cancelled_by_reference,
            str,
        ):
            raise ValidationException("cancelled_by_reference must be string or None")


@dataclass(frozen=True, slots=True)
class CancelVoyageResponse:
    voyage: VoyageResponse


class CancelVoyageService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CancelVoyageFeature:
    """Feature facade for voyage cancellation."""

    def __init__(self, *, service: CancelVoyageService) -> None:
        self._service = service

    def execute(self, request: CancelVoyageRequest) -> CancelVoyageResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    voyage_id=request.voyage_id,
                    cancellation_reason=request.cancellation_reason,
                    cancelled_at=request.cancelled_at,
                    cancelled_by_reference=request.cancelled_by_reference,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Cancel voyage feature failed") from exc

        return CancelVoyageResponse(
            voyage=to_feature_voyage_response(service_response.voyage)
        )
