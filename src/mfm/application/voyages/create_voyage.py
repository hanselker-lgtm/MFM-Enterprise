"""Create Voyage use case and shared voyage application DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.voyages.exceptions import VoyageError
from mfm.domain.voyages.location_snapshot import LocationSnapshot
from mfm.domain.voyages.voyage import Voyage
from mfm.domain.voyages.voyage_purpose import VoyagePurpose
from mfm.domain.voyages.voyage_purpose_code import VoyagePurposeCode
from mfm.repositories.voyage_repository import VoyageRepository


class ApplicationException(Exception):
    """Base exception for voyage application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository and persistence failures."""


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


def to_location_snapshot(value: VoyageLocationInput) -> LocationSnapshot:
    return LocationSnapshot(
        name_snapshot=value.name_snapshot,
        location_external_id=value.location_external_id,
        locality_snapshot=value.locality_snapshot,
        country_snapshot=value.country_snapshot,
    )


def to_location_response(value: LocationSnapshot) -> VoyageLocationResponse:
    return VoyageLocationResponse(
        name_snapshot=value.name_snapshot,
        location_external_id=value.location_external_id,
        locality_snapshot=value.locality_snapshot,
        country_snapshot=value.country_snapshot,
    )


def to_voyage_response(voyage: Voyage) -> VoyageResponse:
    return VoyageResponse(
        voyage_id=voyage.id.value,
        vessel_id=voyage.vessel_id,
        status=voyage.status.value,
        voyage_reference=voyage.voyage_reference,
        planned_departure_location=to_location_response(voyage.planned_departure_location),
        planned_arrival_location=to_location_response(voyage.planned_arrival_location),
        planned_departure_at=voyage.planned_departure_at,
        planned_arrival_at=voyage.planned_arrival_at,
        actual_departure_location=(
            None
            if voyage.actual_departure_location is None
            else to_location_response(voyage.actual_departure_location)
        ),
        actual_arrival_location=(
            None
            if voyage.actual_arrival_location is None
            else to_location_response(voyage.actual_arrival_location)
        ),
        departed_at=voyage.departed_at,
        arrived_at=voyage.arrived_at,
        voyage_purpose=(
            None
            if voyage.voyage_purpose is None
            else VoyagePurposeResponse(
                purpose_code=voyage.voyage_purpose.purpose_code.value,
                purpose_detail=voyage.voyage_purpose.purpose_detail,
            )
        ),
        notes=voyage.notes,
        cancellation_reason=voyage.cancellation_reason,
        cancelled_at=voyage.cancelled_at,
        cancelled_by_reference=voyage.cancelled_by_reference,
        document_reference=voyage.document_reference,
    )


def to_voyage_purpose(
    *,
    purpose_code: str | None,
    purpose_detail: str | None,
) -> VoyagePurpose | None:
    if purpose_code is None:
        return None

    try:
        code = VoyagePurposeCode(purpose_code.strip().upper())
    except Exception as exc:
        raise ValidationException("purpose_code is invalid") from exc

    return VoyagePurpose(purpose_code=code, purpose_detail=purpose_detail)


@dataclass(frozen=True, slots=True)
class CreateVoyageResponse:
    voyage: VoyageResponse


class CreateVoyageUseCase:
    """Create voyage aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateVoyageRequest) -> CreateVoyageResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: VoyageRepository = uow.voyage_repository

                create_kwargs: dict[str, object] = {}
                if request.voyage_id is not None:
                    create_kwargs["id"] = request.voyage_id

                voyage = Voyage(
                    vessel_id=request.vessel_id,
                    planned_departure_location=to_location_snapshot(
                        request.planned_departure_location
                    ),
                    planned_arrival_location=to_location_snapshot(
                        request.planned_arrival_location
                    ),
                    planned_departure_at=request.planned_departure_at,
                    planned_arrival_at=request.planned_arrival_at,
                    voyage_reference=request.voyage_reference,
                    voyage_purpose=to_voyage_purpose(
                        purpose_code=request.purpose_code,
                        purpose_detail=request.purpose_detail,
                    ),
                    notes=request.notes,
                    document_reference=request.document_reference,
                    **create_kwargs,
                )

                repository.add(voyage)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except VoyageError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create voyage failed") from exc

        return CreateVoyageResponse(voyage=to_voyage_response(voyage))
