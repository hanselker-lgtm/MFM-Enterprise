"""Replace technical component feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
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
from mfm.application.technical_configuration.replace_technical_component import (
    ReplaceTechnicalComponentRequest as ServiceRequest,
)
from mfm.application.technical_configuration.replace_technical_component import (
    ReplaceTechnicalComponentResponse as ServiceResponse,
)
from mfm.application.technical_configuration.replace_technical_component import (
    ReplaceTechnicalComponentUseCase,
)
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)


@dataclass(frozen=True, slots=True)
class ReplaceTechnicalComponentRequest:
    configuration_id: UUID
    component_id: UUID
    replaced_on: date
    reason: str
    replacement_component_type: str
    replacement_name: str
    replacement_manufacturer: str | None = None
    replacement_model: str | None = None
    replacement_serial_number: str | None = None
    replacement_build_year: int | None = None
    replacement_notes: str | None = None
    replacement_status: str = TechnicalComponentStatus.PLANNED.value
    replacement_specification_schema_key: str = "GENERIC_V1"
    replacement_specification_entries: tuple[SpecificationEntryInput, ...] = ()
    replacement_component_id: UUID | None = None

    def validate(self) -> None:
        if not isinstance(self.configuration_id, UUID):
            raise ValidationException("configuration_id must be UUID")
        if not isinstance(self.component_id, UUID):
            raise ValidationException("component_id must be UUID")
        if not isinstance(self.replaced_on, date):
            raise ValidationException("replaced_on must be date")
        if not isinstance(self.reason, str) or not self.reason.strip():
            raise ValidationException("reason must be a non-empty string")
        if (
            not isinstance(self.replacement_component_type, str)
            or not self.replacement_component_type.strip()
        ):
            raise ValidationException("replacement_component_type must be a non-empty string")
        if (
            not isinstance(self.replacement_name, str)
            or not self.replacement_name.strip()
        ):
            raise ValidationException("replacement_name must be a non-empty string")
        if (
            self.replacement_manufacturer is not None
            and not isinstance(self.replacement_manufacturer, str)
        ):
            raise ValidationException("replacement_manufacturer must be string or None")
        if self.replacement_model is not None and not isinstance(
            self.replacement_model, str
        ):
            raise ValidationException("replacement_model must be string or None")
        if self.replacement_serial_number is not None and not isinstance(
            self.replacement_serial_number, str
        ):
            raise ValidationException("replacement_serial_number must be string or None")
        if self.replacement_build_year is not None and (
            not isinstance(self.replacement_build_year, int)
            or self.replacement_build_year <= 0
        ):
            raise ValidationException(
                "replacement_build_year must be positive int or None"
            )
        if self.replacement_notes is not None and not isinstance(
            self.replacement_notes, str
        ):
            raise ValidationException("replacement_notes must be string or None")
        if not isinstance(self.replacement_status, str) or not self.replacement_status.strip():
            raise ValidationException("replacement_status must be a non-empty string")
        if (
            not isinstance(self.replacement_specification_schema_key, str)
            or not self.replacement_specification_schema_key.strip()
        ):
            raise ValidationException(
                "replacement_specification_schema_key must be a non-empty string"
            )
        for entry in self.replacement_specification_entries:
            if not isinstance(entry, SpecificationEntryInput):
                raise ValidationException(
                    "replacement_specification_entries must contain SpecificationEntryInput"
                )
            entry.validate()
        if self.replacement_component_id is not None and not isinstance(
            self.replacement_component_id, UUID
        ):
            raise ValidationException("replacement_component_id must be UUID or None")


@dataclass(frozen=True, slots=True)
class ReplaceTechnicalComponentResponse:
    configuration: TechnicalConfigurationResponse


class ReplaceTechnicalComponentService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ReplaceTechnicalComponentFeature:
    """Feature facade for component replacement."""

    def __init__(self, *, service: ReplaceTechnicalComponentService) -> None:
        self._service = service

    def execute(
        self,
        request: ReplaceTechnicalComponentRequest,
    ) -> ReplaceTechnicalComponentResponse:
        request.validate()

        try:
            replacement_component_type = TechnicalComponentType(
                request.replacement_component_type.strip().upper()
            )
        except Exception as exc:
            raise ValidationException("replacement_component_type is invalid") from exc

        try:
            replacement_status = TechnicalComponentStatus(
                request.replacement_status.strip().upper()
            )
        except Exception as exc:
            raise ValidationException("replacement_status is invalid") from exc

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    configuration_id=request.configuration_id,
                    component_id=request.component_id,
                    replaced_on=request.replaced_on,
                    reason=request.reason,
                    replacement_component_type=replacement_component_type,
                    replacement_name=request.replacement_name,
                    replacement_manufacturer=request.replacement_manufacturer,
                    replacement_model=request.replacement_model,
                    replacement_serial_number=request.replacement_serial_number,
                    replacement_build_year=request.replacement_build_year,
                    replacement_notes=request.replacement_notes,
                    replacement_status=replacement_status,
                    replacement_specification_schema_key=request.replacement_specification_schema_key,
                    replacement_specification_entries=tuple(
                        ServiceSpecificationEntryInput(
                            key=entry.key,
                            value=entry.value,
                            unit=entry.unit,
                        )
                        for entry in request.replacement_specification_entries
                    ),
                    replacement_component_id=request.replacement_component_id,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Replace technical component feature failed") from exc

        return ReplaceTechnicalComponentResponse(
            configuration=to_feature_configuration_response(service_response.configuration)
        )
