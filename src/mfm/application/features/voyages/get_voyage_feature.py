"""Get voyage feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
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
from mfm.application.voyages.get_voyage import GetVoyageRequest as ServiceRequest
from mfm.application.voyages.get_voyage import GetVoyageResponse as ServiceResponse
from mfm.application.voyages.get_voyage import GetVoyageUseCase


@dataclass(frozen=True, slots=True)
class GetVoyageRequest:
    voyage_id: UUID

    def validate(self) -> None:
        if not isinstance(self.voyage_id, UUID):
            raise ValidationException("voyage_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetVoyageResponse:
    voyage: VoyageResponse


class GetVoyageService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetVoyageFeature:
    """Feature facade for voyage retrieval."""

    def __init__(self, *, service: GetVoyageService) -> None:
        self._service = service

    def execute(self, request: GetVoyageRequest) -> GetVoyageResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(voyage_id=request.voyage_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get voyage feature failed") from exc

        return GetVoyageResponse(
            voyage=to_feature_voyage_response(service_response.voyage)
        )
