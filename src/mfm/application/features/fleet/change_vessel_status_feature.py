"""Change vessel status feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.fleet.change_vessel_status import (
    ChangeVesselStatusRequest as ServiceRequest,
)
from mfm.application.fleet.change_vessel_status import (
    ChangeVesselStatusResponse as ServiceResponse,
)
from mfm.application.fleet.change_vessel_status import ChangeVesselStatusUseCase
from mfm.application.fleet.create_vessel import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.fleet.create_vessel import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.fleet.create_vessel import (
    ValidationException as ServiceValidationException,
)
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
class ChangeVesselStatusRequest:
    vessel_id: UUID
    status: VesselStatus

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.status, VesselStatus):
            raise ValidationException("status must be VesselStatus")


@dataclass(frozen=True, slots=True)
class ChangeVesselStatusResponse:
    vessel_id: UUID
    status: str


class ChangeVesselStatusService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ChangeVesselStatusFeature:
    """Feature facade for vessel status changes."""

    def __init__(self, *, service: ChangeVesselStatusService) -> None:
        self._service = service

    def execute(self, request: ChangeVesselStatusRequest) -> ChangeVesselStatusResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(vessel_id=request.vessel_id, status=request.status)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Change vessel status feature failed") from exc

        return ChangeVesselStatusResponse(
            vessel_id=service_response.vessel_id,
            status=service_response.status,
        )
