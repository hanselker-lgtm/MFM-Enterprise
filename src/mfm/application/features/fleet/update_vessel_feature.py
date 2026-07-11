"""Update vessel feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.fleet.create_vessel import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.fleet.create_vessel import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.fleet.create_vessel import (
    ValidationException as ServiceValidationException,
)
from mfm.application.fleet.update_vessel import UpdateVesselRequest as ServiceRequest
from mfm.application.fleet.update_vessel import UpdateVesselResponse as ServiceResponse
from mfm.application.fleet.update_vessel import UpdateVesselUseCase
from mfm.domain.fleet.vessel_material import VesselMaterial


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class UpdateVesselRequest:
    vessel_id: UUID
    shipyard: str
    build_year: int | None
    construction_material: VesselMaterial

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.shipyard, str):
            raise ValidationException("shipyard must be a string")
        if self.build_year is not None and (
            not isinstance(self.build_year, int) or self.build_year <= 0
        ):
            raise ValidationException("build_year must be positive int or None")
        if not isinstance(self.construction_material, VesselMaterial):
            raise ValidationException("construction_material must be VesselMaterial")


@dataclass(frozen=True, slots=True)
class UpdateVesselResponse:
    vessel_id: UUID
    shipyard: str
    build_year: int | None
    construction_material: str


class UpdateVesselService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateVesselFeature:
    """Feature facade for vessel updates with standardized API behavior."""

    def __init__(self, *, service: UpdateVesselService) -> None:
        self._service = service

    def execute(self, request: UpdateVesselRequest) -> UpdateVesselResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    vessel_id=request.vessel_id,
                    shipyard=request.shipyard,
                    build_year=request.build_year,
                    construction_material=request.construction_material,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update vessel feature failed") from exc

        return UpdateVesselResponse(
            vessel_id=service_response.vessel_id,
            shipyard=service_response.shipyard,
            build_year=service_response.build_year,
            construction_material=service_response.construction_material,
        )
