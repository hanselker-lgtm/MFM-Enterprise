"""Create vessel feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.fleet.create_vessel import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.fleet.create_vessel import CreateVesselRequest as ServiceRequest
from mfm.application.fleet.create_vessel import CreateVesselResponse as ServiceResponse
from mfm.application.fleet.create_vessel import CreateVesselUseCase
from mfm.application.fleet.create_vessel import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.fleet.create_vessel import (
    ValidationException as ServiceValidationException,
)
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_status import VesselStatus


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class CreateVesselRequest:
    asset_id: UUID
    registration: str
    name: str
    shipyard: str
    build_year: int | None
    construction_material: VesselMaterial
    length: float
    beam: float
    draft: float
    status: VesselStatus = VesselStatus.ACTIVE

    def validate(self) -> None:
        if not isinstance(self.asset_id, UUID):
            raise ValidationException("asset_id must be UUID")
        if not isinstance(self.registration, str) or not self.registration.strip():
            raise ValidationException("registration must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if not isinstance(self.shipyard, str):
            raise ValidationException("shipyard must be a string")
        if self.build_year is not None and (
            not isinstance(self.build_year, int) or self.build_year <= 0
        ):
            raise ValidationException("build_year must be positive int or None")
        if not isinstance(self.construction_material, VesselMaterial):
            raise ValidationException("construction_material must be VesselMaterial")
        if not isinstance(self.length, (int, float)):
            raise ValidationException("length must be numeric")
        if not isinstance(self.beam, (int, float)):
            raise ValidationException("beam must be numeric")
        if not isinstance(self.draft, (int, float)):
            raise ValidationException("draft must be numeric")
        if not isinstance(self.status, VesselStatus):
            raise ValidationException("status must be VesselStatus")


@dataclass(frozen=True, slots=True)
class CreateVesselResponse:
    vessel_id: UUID
    asset_id: UUID
    registration: str
    name: str
    status: str


class CreateVesselService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CreateVesselFeature:
    """Feature facade for vessel creation with standardized API behavior."""

    def __init__(self, *, service: CreateVesselService) -> None:
        self._service = service

    def execute(self, request: CreateVesselRequest) -> CreateVesselResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    asset_id=request.asset_id,
                    registration=request.registration,
                    name=request.name,
                    shipyard=request.shipyard,
                    build_year=request.build_year,
                    construction_material=request.construction_material,
                    length=request.length,
                    beam=request.beam,
                    draft=request.draft,
                    status=request.status,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create vessel feature failed") from exc

        return CreateVesselResponse(
            vessel_id=service_response.vessel_id,
            asset_id=service_response.asset_id,
            registration=service_response.registration,
            name=service_response.name,
            status=service_response.status,
        )
