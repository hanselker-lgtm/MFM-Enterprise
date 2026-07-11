"""Update vessel dimensions feature facade following Public API Standard."""

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
from mfm.application.fleet.update_vessel_dimensions import (
    UpdateVesselDimensionsRequest as ServiceRequest,
)
from mfm.application.fleet.update_vessel_dimensions import (
    UpdateVesselDimensionsResponse as ServiceResponse,
)
from mfm.application.fleet.update_vessel_dimensions import (
    UpdateVesselDimensionsUseCase,
)


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class UpdateVesselDimensionsRequest:
    vessel_id: UUID
    length: float
    beam: float
    draft: float

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.length, (int, float)):
            raise ValidationException("length must be numeric")
        if not isinstance(self.beam, (int, float)):
            raise ValidationException("beam must be numeric")
        if not isinstance(self.draft, (int, float)):
            raise ValidationException("draft must be numeric")


@dataclass(frozen=True, slots=True)
class UpdateVesselDimensionsResponse:
    vessel_id: UUID
    length: float
    beam: float
    draft: float


class UpdateVesselDimensionsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateVesselDimensionsFeature:
    """Feature facade for vessel dimension updates."""

    def __init__(self, *, service: UpdateVesselDimensionsService) -> None:
        self._service = service

    def execute(
        self, request: UpdateVesselDimensionsRequest
    ) -> UpdateVesselDimensionsResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    vessel_id=request.vessel_id,
                    length=request.length,
                    beam=request.beam,
                    draft=request.draft,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update vessel dimensions feature failed") from exc

        return UpdateVesselDimensionsResponse(
            vessel_id=service_response.vessel_id,
            length=service_response.length,
            beam=service_response.beam,
            draft=service_response.draft,
        )
