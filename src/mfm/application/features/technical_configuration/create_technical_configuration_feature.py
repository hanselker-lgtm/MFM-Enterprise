"""Create technical configuration feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.technical_configuration.create_technical_configuration import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    ComponentReplacementRecordResponse as ServiceReplacementResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationRequest as ServiceRequest,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationResponse as ServiceResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationUseCase,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    TechnicalComponentResponse as ServiceComponentResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    TechnicalConfigurationResponse as ServiceConfigurationResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    TechnicalSpecificationEntryResponse as ServiceSpecificationEntryResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
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


PublicSpecificationValue = str | int | float | bool


@dataclass(frozen=True, slots=True)
class TechnicalSpecificationEntryResponse:
    key: str
    value: PublicSpecificationValue
    unit: str | None


@dataclass(frozen=True, slots=True)
class TechnicalComponentResponse:
    id: UUID
    component_type: str
    name: str
    manufacturer: str | None
    model: str | None
    serial_number: str | None
    build_year: int | None
    status: str
    installed_date: date | None
    removed_date: date | None
    notes: str | None
    specification_schema_key: str
    specification_entries: tuple[TechnicalSpecificationEntryResponse, ...]
    replacement_successor_id: UUID | None


@dataclass(frozen=True, slots=True)
class ComponentReplacementRecordResponse:
    id: UUID
    replaced_component_id: UUID
    replacement_component_id: UUID
    replaced_on: date
    reason: str
    notes: str | None


@dataclass(frozen=True, slots=True)
class TechnicalConfigurationResponse:
    id: UUID
    vessel_id: UUID
    status: str
    components: tuple[TechnicalComponentResponse, ...]
    replacement_history: tuple[ComponentReplacementRecordResponse, ...]


@dataclass(frozen=True, slots=True)
class CreateTechnicalConfigurationRequest:
    vessel_id: UUID

    def validate(self) -> None:
        if not isinstance(self.vessel_id, UUID):
            raise ValidationException("vessel_id must be UUID")


@dataclass(frozen=True, slots=True)
class CreateTechnicalConfigurationResponse:
    configuration: TechnicalConfigurationResponse


class CreateTechnicalConfigurationService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class CreateTechnicalConfigurationFeature:
    """Feature facade for technical configuration creation."""

    def __init__(self, *, service: CreateTechnicalConfigurationService) -> None:
        self._service = service

    def execute(
        self,
        request: CreateTechnicalConfigurationRequest,
    ) -> CreateTechnicalConfigurationResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(vessel_id=request.vessel_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create technical configuration feature failed") from exc

        return CreateTechnicalConfigurationResponse(
            configuration=to_feature_configuration_response(service_response.configuration)
        )


def to_feature_configuration_response(
    response: ServiceConfigurationResponse,
) -> TechnicalConfigurationResponse:
    return TechnicalConfigurationResponse(
        id=response.id,
        vessel_id=response.vessel_id,
        status=response.status,
        components=tuple(
            to_feature_component_response(component)
            for component in response.components
        ),
        replacement_history=tuple(
            to_feature_replacement_response(item)
            for item in response.replacement_history
        ),
    )


def to_feature_component_response(
    response: ServiceComponentResponse,
) -> TechnicalComponentResponse:
    return TechnicalComponentResponse(
        id=response.id,
        component_type=response.component_type,
        name=response.name,
        manufacturer=response.manufacturer,
        model=response.model,
        serial_number=response.serial_number,
        build_year=response.build_year,
        status=response.status,
        installed_date=response.installed_date,
        removed_date=response.removed_date,
        notes=response.notes,
        specification_schema_key=response.specification_schema_key,
        specification_entries=tuple(
            to_feature_specification_entry_response(entry)
            for entry in response.specification_entries
        ),
        replacement_successor_id=response.replacement_successor_id,
    )


def to_feature_specification_entry_response(
    response: ServiceSpecificationEntryResponse,
) -> TechnicalSpecificationEntryResponse:
    return TechnicalSpecificationEntryResponse(
        key=response.key,
        value=response.value,
        unit=response.unit,
    )


def to_feature_replacement_response(
    response: ServiceReplacementResponse,
) -> ComponentReplacementRecordResponse:
    return ComponentReplacementRecordResponse(
        id=response.id,
        replaced_component_id=response.replaced_component_id,
        replacement_component_id=response.replacement_component_id,
        replaced_on=response.replaced_on,
        reason=response.reason,
        notes=response.notes,
    )
