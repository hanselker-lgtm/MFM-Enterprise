"""Depart voyage feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.features.voyages.create_voyage_feature import BusinessRuleViolation
from mfm.application.features.voyages.create_voyage_feature import RepositoryException
from mfm.application.features.voyages.create_voyage_feature import ValidationException
from mfm.application.features.voyages.create_voyage_feature import VoyageLocationInput
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
from mfm.application.voyages.depart_voyage import DepartVoyageRequest as ServiceRequest
from mfm.application.voyages.depart_voyage import DepartVoyageResponse as ServiceResponse
from mfm.application.voyages.depart_voyage import DepartVoyageUseCase
from mfm.application.voyages.create_voyage import VoyageLocationInput as ServiceLocationInput


@dataclass(frozen=True, slots=True)
class DepartVoyageRequest:
    voyage_id: UUID
    departed_at: datetime
    actual_departure_location: VoyageLocationInput

    def validate(self) -> None:
        if not isinstance(self.voyage_id, UUID):
            raise ValidationException("voyage_id must be UUID")
        if not isinstance(self.departed_at, datetime):
            raise ValidationException("departed_at must be datetime")
        self.actual_departure_location.validate(field_name="actual_departure_location")


@dataclass(frozen=True, slots=True)
class DepartVoyageResponse:
    voyage: VoyageResponse


class DepartVoyageService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class DepartVoyageFeature:
    """Feature facade for voyage departure."""

    def __init__(self, *, service: DepartVoyageService) -> None:
        self._service = service

    def execute(self, request: DepartVoyageRequest) -> DepartVoyageResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    voyage_id=request.voyage_id,
                    departed_at=request.departed_at,
                    actual_departure_location=ServiceLocationInput(
                        name_snapshot=request.actual_departure_location.name_snapshot,
                        location_external_id=(
                            request.actual_departure_location.location_external_id
                        ),
                        locality_snapshot=request.actual_departure_location.locality_snapshot,
                        country_snapshot=request.actual_departure_location.country_snapshot,
                    ),
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Depart voyage feature failed") from exc

        return DepartVoyageResponse(
            voyage=to_feature_voyage_response(service_response.voyage)
        )
