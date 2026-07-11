"""Change vessel registration feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.fleet.change_vessel_registration import (
    ChangeVesselRegistrationRequest as ServiceRequest,
)
from mfm.application.fleet.change_vessel_registration import (
    ChangeVesselRegistrationResponse as ServiceResponse,
)
from mfm.application.fleet.change_vessel_registration import (
    ChangeVesselRegistrationUseCase,
)
from mfm.application.fleet.create_vessel import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.fleet.create_vessel import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.fleet.create_vessel import (
    ValidationException as ServiceValidationException,
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
class ChangeVesselRegistrationRequest:
    vessel_id: UUID
    registration: str

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.registration, str) or not self.registration.strip():
            raise ValidationException("registration must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ChangeVesselRegistrationResponse:
    vessel_id: UUID
    registration: str


class ChangeVesselRegistrationService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ChangeVesselRegistrationFeature:
    """Feature facade for vessel registration changes."""

    def __init__(self, *, service: ChangeVesselRegistrationService) -> None:
        self._service = service

    def execute(
        self, request: ChangeVesselRegistrationRequest
    ) -> ChangeVesselRegistrationResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    vessel_id=request.vessel_id,
                    registration=request.registration,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException(
                "Change vessel registration feature failed"
            ) from exc

        return ChangeVesselRegistrationResponse(
            vessel_id=service_response.vessel_id,
            registration=service_response.registration,
        )
