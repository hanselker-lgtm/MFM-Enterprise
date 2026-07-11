"""Arrive voyage feature facade following Public API Standard."""

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
from mfm.application.voyages.arrive_voyage import ArriveVoyageRequest as ServiceRequest
from mfm.application.voyages.arrive_voyage import ArriveVoyageResponse as ServiceResponse
from mfm.application.voyages.arrive_voyage import ArriveVoyageUseCase
from mfm.application.voyages.create_voyage import VoyageLocationInput as ServiceLocationInput


@dataclass(frozen=True, slots=True)
class ArriveVoyageRequest:
    voyage_id: UUID
    arrived_at: datetime
    actual_arrival_location: VoyageLocationInput

    def validate(self) -> None:
        if not isinstance(self.voyage_id, UUID):
            raise ValidationException("voyage_id must be UUID")
        if not isinstance(self.arrived_at, datetime):
            raise ValidationException("arrived_at must be datetime")
        self.actual_arrival_location.validate(field_name="actual_arrival_location")


@dataclass(frozen=True, slots=True)
class ArriveVoyageResponse:
    voyage: VoyageResponse


class ArriveVoyageService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ArriveVoyageFeature:
    """Feature facade for voyage arrival."""

    def __init__(self, *, service: ArriveVoyageService) -> None:
        self._service = service

    def execute(self, request: ArriveVoyageRequest) -> ArriveVoyageResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    voyage_id=request.voyage_id,
                    arrived_at=request.arrived_at,
                    actual_arrival_location=ServiceLocationInput(
                        name_snapshot=request.actual_arrival_location.name_snapshot,
                        location_external_id=(
                            request.actual_arrival_location.location_external_id
                        ),
                        locality_snapshot=request.actual_arrival_location.locality_snapshot,
                        country_snapshot=request.actual_arrival_location.country_snapshot,
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
            raise RepositoryException("Arrive voyage feature failed") from exc

        return ArriveVoyageResponse(
            voyage=to_feature_voyage_response(service_response.voyage)
        )
