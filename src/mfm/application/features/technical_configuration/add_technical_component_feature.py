"""Add technical component feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    RepositoryException,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    TechnicalConfigurationResponse,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    ValidationException,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    to_feature_configuration_response,
)
from mfm.application.technical_configuration.add_technical_component import (
    AddTechnicalComponentRequest as ServiceRequest,
)
from mfm.application.technical_configuration.add_technical_component import (
    AddTechnicalComponentResponse as ServiceResponse,
)
from mfm.application.technical_configuration.add_technical_component import (
    AddTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    SpecificationEntryInput as ServiceSpecificationEntryInput,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    ValidationException as ServiceValidationException,
)
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)


@dataclass(frozen=True, slots=True)
class SpecificationEntryInput:
    key: str
    value: str | int | float | bool
    unit: str | None = None

    def validate(self) -> None:
        if not isinstance(self.key, str) or not self.key.strip():
            raise ValidationException("specification key must be a non-empty string")
        if not isinstance(self.value, (str, int, float, bool)):
            raise ValidationException("specification value must be str/int/float/bool")
        if self.unit is not None and not isinstance(self.unit, str):
            raise ValidationException("specification unit must be string or None")


@dataclass(frozen=True, slots=True)
class AddTechnicalComponentRequest:
    configuration_id: UUID
    component_type: str
    name: str
    manufacturer: str | None = None
    model: str | None = None
    serial_number: str | None = None
    build_year: int | None = None
    installed_date: date | None = None
    removed_date: date | None = None
    status: str = TechnicalComponentStatus.PLANNED.value
    notes: str | None = None
    specification_schema_key: str = "GENERIC_V1"
    specification_entries: tuple[SpecificationEntryInput, ...] = ()
    component_id: UUID | None = None

    def validate(self) -> None:
        if not isinstance(self.configuration_id, UUID):
            raise ValidationException("configuration_id must be UUID")
        if not isinstance(self.component_type, str) or not self.component_type.strip():
            raise ValidationException("component_type must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValidationException("name must be a non-empty string")
        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            raise ValidationException("manufacturer must be string or None")
        if self.model is not None and not isinstance(self.model, str):
            raise ValidationException("model must be string or None")
        if self.serial_number is not None and not isinstance(self.serial_number, str):
            raise ValidationException("serial_number must be string or None")
        if self.build_year is not None and (
            not isinstance(self.build_year, int) or self.build_year <= 0
        ):
            raise ValidationException("build_year must be positive int or None")
        if self.installed_date is not None and not isinstance(self.installed_date, date):
            raise ValidationException("installed_date must be date or None")
        if self.removed_date is not None and not isinstance(self.removed_date, date):
            raise ValidationException("removed_date must be date or None")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValidationException("status must be a non-empty string")
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")
        if (
            not isinstance(self.specification_schema_key, str)
            or not self.specification_schema_key.strip()
        ):
            raise ValidationException(
                "specification_schema_key must be a non-empty string"
            )
        for entry in self.specification_entries:
            if not isinstance(entry, SpecificationEntryInput):
                raise ValidationException(
                    "specification_entries must contain SpecificationEntryInput"
                )
            entry.validate()
        if self.component_id is not None and not isinstance(self.component_id, UUID):
            raise ValidationException("component_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class AddTechnicalComponentResponse:
    configuration: TechnicalConfigurationResponse


class AddTechnicalComponentService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class AddTechnicalComponentFeature:
    """Feature facade for adding components to technical configuration."""

    def __init__(self, *, service: AddTechnicalComponentService) -> None:
        self._service = service

    def execute(self, request: AddTechnicalComponentRequest) -> AddTechnicalComponentResponse:
        request.validate()

        try:
            component_type = TechnicalComponentType(request.component_type.strip().upper())
        except Exception as exc:
            raise ValidationException("component_type is invalid") from exc

        try:
            status = TechnicalComponentStatus(request.status.strip().upper())
        except Exception as exc:
            raise ValidationException("status is invalid") from exc

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    configuration_id=request.configuration_id,
                    component_type=component_type,
                    name=request.name,
                    manufacturer=request.manufacturer,
                    model=request.model,
                    serial_number=request.serial_number,
                    build_year=request.build_year,
                    installed_date=request.installed_date,
                    removed_date=request.removed_date,
                    status=status,
                    notes=request.notes,
                    specification_schema_key=request.specification_schema_key,
                    specification_entries=tuple(
                        ServiceSpecificationEntryInput(
                            key=entry.key,
                            value=entry.value,
                            unit=entry.unit,
                        )
                        for entry in request.specification_entries
                    ),
                    component_id=request.component_id,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Add technical component feature failed") from exc

        return AddTechnicalComponentResponse(
            configuration=to_feature_configuration_response(service_response.configuration)
        )
