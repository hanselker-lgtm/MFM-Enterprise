"""Rename vessel feature facade following Public API Standard."""

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
from mfm.application.fleet.rename_vessel import RenameVesselRequest as ServiceRequest
from mfm.application.fleet.rename_vessel import RenameVesselResponse as ServiceResponse
from mfm.application.fleet.rename_vessel import RenameVesselUseCase


class ApplicationException(Exception):
    """Base exception for feature-level failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class RenameVesselRequest:
    vessel_id: UUID
    name: str

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")


@dataclass(frozen=True, slots=True)
class RenameVesselResponse:
    vessel_id: UUID
    name: str


class RenameVesselService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class RenameVesselFeature:
    """Feature facade for vessel rename with standardized API behavior."""

    def __init__(self, *, service: RenameVesselService) -> None:
        self._service = service

    def execute(self, request: RenameVesselRequest) -> RenameVesselResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(vessel_id=request.vessel_id, name=request.name)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Rename vessel feature failed") from exc

        return RenameVesselResponse(
            vessel_id=service_response.vessel_id,
            name=service_response.name,
        )
