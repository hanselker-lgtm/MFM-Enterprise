"""Replace Technical Component use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.application.technical_configuration.create_technical_configuration import (
    ApplicationException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    BusinessRuleViolation,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    RepositoryException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    SpecificationEntryInput,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    TechnicalConfigurationResponse,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    ValidationException,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    to_component_notes,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    to_configuration_response,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    to_replacement_reason,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    to_technical_component,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.technical_configuration.exceptions import TechnicalConfigurationError
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)
from mfm.repositories.technical_configuration_repository import (
    TechnicalConfigurationRepository,
)


@dataclass(frozen=True, slots=True)
class ReplaceTechnicalComponentRequest:
    configuration_id: UUID
    component_id: UUID
    replaced_on: date
    reason: str
    replacement_component_type: TechnicalComponentType
    replacement_name: str
    replacement_manufacturer: str | None = None
    replacement_model: str | None = None
    replacement_serial_number: str | None = None
    replacement_build_year: int | None = None
    replacement_notes: str | None = None
    replacement_status: TechnicalComponentStatus = TechnicalComponentStatus.PLANNED
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
        if not isinstance(self.replacement_component_type, TechnicalComponentType):
            raise ValidationException(
                "replacement_component_type must be TechnicalComponentType"
            )
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
        if not isinstance(self.replacement_status, TechnicalComponentStatus):
            raise ValidationException(
                "replacement_status must be TechnicalComponentStatus"
            )
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


class ReplaceTechnicalComponentUseCase:
    """Replace component in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: ReplaceTechnicalComponentRequest,
    ) -> ReplaceTechnicalComponentResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: TechnicalConfigurationRepository = (
                    uow.technical_configuration_repository
                )

                configuration = repository.get_by_id(request.configuration_id)
                if configuration is None:
                    raise BusinessRuleViolation(
                        f"Technical configuration {request.configuration_id} does not exist"
                    )

                replacement_component = to_technical_component(
                    component_id=request.replacement_component_id,
                    component_type=request.replacement_component_type,
                    name=request.replacement_name,
                    manufacturer=request.replacement_manufacturer,
                    model=request.replacement_model,
                    serial_number=request.replacement_serial_number,
                    build_year=request.replacement_build_year,
                    installed_date=None,
                    removed_date=None,
                    status=request.replacement_status,
                    notes=request.replacement_notes,
                    specification_schema_key=request.replacement_specification_schema_key,
                    specification_entries=request.replacement_specification_entries,
                )

                configuration.replace_component(
                    request.component_id,
                    replacement_component,
                    request.replaced_on,
                    reason=to_replacement_reason(request.reason),
                    notes=to_component_notes(request.replacement_notes),
                )
                repository.update(configuration)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except TechnicalConfigurationError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Replace technical component failed") from exc

        return ReplaceTechnicalComponentResponse(
            configuration=to_configuration_response(configuration)
        )
