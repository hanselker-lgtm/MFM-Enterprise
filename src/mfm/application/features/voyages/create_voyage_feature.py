"""Create voyage feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.voyages.create_voyage import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.voyages.create_voyage import CreateVoyageRequest as ServiceRequest
from mfm.application.voyages.create_voyage import CreateVoyageResponse as ServiceResponse
from mfm.application.voyages.create_voyage import CreateVoyageUseCase
from mfm.application.voyages.create_voyage import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.voyages.create_voyage import (
    ValidationException as ServiceValidationException,
)
from mfm.application.voyages.create_voyage import VoyageLocationInput as ServiceLocationInput
from mfm.application.voyages.create_voyage import VoyageLocationResponse as ServiceLocationResponse
from mfm.application.voyages.create_voyage import VoyagePurposeResponse as ServicePurposeResponse
from mfm.application.voyages.create_voyage import VoyageResponse as ServiceVoyageResponse


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class VoyageLocationInput:
    name_snapshot: str
    location_external_id: str | None = None
    locality_snapshot: str | None = None
    country_snapshot: str | None = None

    def validate(self, *, field_name: str) -> None:
        if not isinstance(self.name_snapshot, str) or not self.name_snapshot.strip():
            raise ValidationException(f"{field_name}.name_snapshot must be a non-empty string")
        for attribute in (
            "location_external_id",
            "locality_snapshot",
            "country_snapshot",
        ):
            value = getattr(self, attribute)
            if value is not None and not isinstance(value, str):
                raise ValidationException(f"{field_name}.{attribute} must be string or None")


@dataclass(frozen=True, slots=True)
class VoyageLocationResponse:
    name_snapshot: str
    location_external_id: str | None
    locality_snapshot: str | None
    country_snapshot: str | None


@dataclass(frozen=True, slots=True)
class VoyagePurposeResponse:
    purpose_code: str
    purpose_detail: str | None


@dataclass(frozen=True, slots=True)
class VoyageResponse:
    voyage_id: UUID
    vessel_id: UUID
    status: str
    voyage_reference: str | None
    planned_departure_location: VoyageLocationResponse
    planned_arrival_location: VoyageLocationResponse
    planned_departure_at: datetime
    planned_arrival_at: datetime
    actual_departure_location: VoyageLocationResponse | None
    actual_arrival_location: VoyageLocationResponse | None
    departed_at: datetime | None
    arrived_at: datetime | None
    voyage_purpose: VoyagePurposeResponse | None
    notes: str | None
    cancellation_reason: str | None
    cancelled_at: datetime | None
    cancelled_by_reference: str | None
    document_reference: str | None


@dataclass(frozen=True, slots=True)
class CreateVoyageRequest:
    vessel_id: UUID
    planned_departure_location: VoyageLocationInput
    planned_arrival_location: VoyageLocationInput
    planned_departure_at: datetime
    planned_arrival_at: datetime
    voyage_id: UUID | None = None
    voyage_reference: str | None = None
    purpose_code: str | None = None
    purpose_detail: str | None = None
    notes: str | None = None
    document_reference: str | None = None

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.planned_departure_at, datetime):
            raise ValidationException("planned_departure_at must be datetime")
        if not isinstance(self.planned_arrival_at, datetime):
            raise ValidationException("planned_arrival_at must be datetime")
        if self.voyage_id is not None and not isinstance(self.voyage_id, UUID):
            raise ValidationException("voyage_id must be UUID or None")
        if self.voyage_reference is not None and not isinstance(self.voyage_reference, str):
            raise ValidationException("voyage_reference must be string or None")
        if self.purpose_code is not None and not isinstance(self.purpose_code, str):
            raise ValidationException("purpose_code must be string or None")
        if self.purpose_detail is not None and not isinstance(self.purpose_detail, str):
            raise ValidationException("purpose_detail must be string or None")
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")
        if self.document_reference is not None and not isinstance(self.document_reference, str):
            raise ValidationException("document_reference must be string or None")

        self.planned_departure_location.validate(field_name="planned_departure_location")
        self.planned_arrival_location.validate(field_name="planned_arrival_location")


@dataclass(frozen=True, slots=True)
class CreateVoyageResponse:
    voyage: VoyageResponse


class CreateVoyageService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_feature_location_response(
    response: ServiceLocationResponse,
) -> VoyageLocationResponse:
    return VoyageLocationResponse(
        name_snapshot=response.name_snapshot,
        location_external_id=response.location_external_id,
        locality_snapshot=response.locality_snapshot,
        country_snapshot=response.country_snapshot,
    )


def to_feature_purpose_response(
    response: ServicePurposeResponse | None,
) -> VoyagePurposeResponse | None:
    if response is None:
        return None
    return VoyagePurposeResponse(
        purpose_code=response.purpose_code,
        purpose_detail=response.purpose_detail,
    )


def to_feature_voyage_response(response: ServiceVoyageResponse) -> VoyageResponse:
    return VoyageResponse(
        voyage_id=response.voyage_id,
        vessel_id=response.vessel_id,
        status=response.status,
        voyage_reference=response.voyage_reference,
        planned_departure_location=to_feature_location_response(
            response.planned_departure_location
        ),
        planned_arrival_location=to_feature_location_response(
            response.planned_arrival_location
        ),
        planned_departure_at=response.planned_departure_at,
        planned_arrival_at=response.planned_arrival_at,
        actual_departure_location=(
            None
            if response.actual_departure_location is None
            else to_feature_location_response(response.actual_departure_location)
        ),
        actual_arrival_location=(
            None
            if response.actual_arrival_location is None
            else to_feature_location_response(response.actual_arrival_location)
        ),
        departed_at=response.departed_at,
        arrived_at=response.arrived_at,
        voyage_purpose=to_feature_purpose_response(response.voyage_purpose),
        notes=response.notes,
        cancellation_reason=response.cancellation_reason,
        cancelled_at=response.cancelled_at,
        cancelled_by_reference=response.cancelled_by_reference,
        document_reference=response.document_reference,
    )


class CreateVoyageFeature:
    """Feature facade for voyage creation."""

    def __init__(self, *, service: CreateVoyageService) -> None:
        self._service = service

    def execute(self, request: CreateVoyageRequest) -> CreateVoyageResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    vessel_id=request.vessel_id,
                    planned_departure_location=ServiceLocationInput(
                        name_snapshot=request.planned_departure_location.name_snapshot,
                        location_external_id=(
                            request.planned_departure_location.location_external_id
                        ),
                        locality_snapshot=request.planned_departure_location.locality_snapshot,
                        country_snapshot=request.planned_departure_location.country_snapshot,
                    ),
                    planned_arrival_location=ServiceLocationInput(
                        name_snapshot=request.planned_arrival_location.name_snapshot,
                        location_external_id=(
                            request.planned_arrival_location.location_external_id
                        ),
                        locality_snapshot=request.planned_arrival_location.locality_snapshot,
                        country_snapshot=request.planned_arrival_location.country_snapshot,
                    ),
                    planned_departure_at=request.planned_departure_at,
                    planned_arrival_at=request.planned_arrival_at,
                    voyage_id=request.voyage_id,
                    voyage_reference=request.voyage_reference,
                    purpose_code=request.purpose_code,
                    purpose_detail=request.purpose_detail,
                    notes=request.notes,
                    document_reference=request.document_reference,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create voyage feature failed") from exc

        return CreateVoyageResponse(
            voyage=to_feature_voyage_response(service_response.voyage)
        )
