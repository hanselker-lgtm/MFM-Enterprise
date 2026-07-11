"""Update technical component details feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.features.technical_configuration.add_technical_component_feature import (
    SpecificationEntryInput,
)
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
from mfm.application.technical_configuration.update_technical_component_details import (
    UpdateTechnicalComponentDetailsRequest as ServiceRequest,
)
from mfm.application.technical_configuration.update_technical_component_details import (
    UpdateTechnicalComponentDetailsResponse as ServiceResponse,
)
from mfm.application.technical_configuration.update_technical_component_details import (
    UpdateTechnicalComponentDetailsUseCase,
)


@dataclass(frozen=True, slots=True)
class UpdateTechnicalComponentDetailsRequest:
    configuration_id: UUID
    component_id: UUID
    name: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    serial_number: str | None = None
    build_year: int | None = None
    notes: str | None = None
    specification_schema_key: str | None = None
    specification_entries: tuple[SpecificationEntryInput, ...] | None = None

    def validate(self) -> None:
        if not isinstance(self.configuration_id, UUID):
            raise ValidationException("configuration_id must be UUID")
        if not isinstance(self.component_id, UUID):
            raise ValidationException("component_id must be UUID")
        if self.name is not None and (not isinstance(self.name, str) or not self.name.strip()):
            raise ValidationException("name must be a non-empty string or None")
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
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")
        if self.specification_schema_key is not None and (
            not isinstance(self.specification_schema_key, str)
            or not self.specification_schema_key.strip()
        ):
            raise ValidationException(
                "specification_schema_key must be a non-empty string or None"
            )
        if self.specification_entries is not None:
            for entry in self.specification_entries:
                if not isinstance(entry, SpecificationEntryInput):
                    raise ValidationException(
                        "specification_entries must contain SpecificationEntryInput"
                    )
                entry.validate()


@dataclass(frozen=True, slots=True)
class UpdateTechnicalComponentDetailsResponse:
    configuration: TechnicalConfigurationResponse


class UpdateTechnicalComponentDetailsService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class UpdateTechnicalComponentDetailsFeature:
    """Feature facade for updating technical component details."""

    def __init__(self, *, service: UpdateTechnicalComponentDetailsService) -> None:
        self._service = service

    def execute(
        self,
        request: UpdateTechnicalComponentDetailsRequest,
    ) -> UpdateTechnicalComponentDetailsResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    configuration_id=request.configuration_id,
                    component_id=request.component_id,
                    name=request.name,
                    manufacturer=request.manufacturer,
                    model=request.model,
                    serial_number=request.serial_number,
                    build_year=request.build_year,
                    notes=request.notes,
                    specification_schema_key=request.specification_schema_key,
                    specification_entries=(
                        None
                        if request.specification_entries is None
                        else tuple(
                            ServiceSpecificationEntryInput(
                                key=entry.key,
                                value=entry.value,
                                unit=entry.unit,
                            )
                            for entry in request.specification_entries
                        )
                    ),
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
                "Update technical component details feature failed"
            ) from exc

        return UpdateTechnicalComponentDetailsResponse(
            configuration=to_feature_configuration_response(service_response.configuration)
        )
