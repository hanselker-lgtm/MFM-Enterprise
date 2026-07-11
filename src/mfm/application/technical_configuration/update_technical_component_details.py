"""Update Technical Component Details use case."""

from __future__ import annotations

from dataclasses import dataclass
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
    to_configuration_response,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.technical_configuration.exceptions import TechnicalConfigurationError
from mfm.domain.technical_configuration.technical_specification import (
    SpecificationEntry,
)
from mfm.domain.technical_configuration.technical_specification import (
    TechnicalSpecification,
)
from mfm.repositories.technical_configuration_repository import (
    TechnicalConfigurationRepository,
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


class UpdateTechnicalComponentDetailsUseCase:
    """Update component details in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: UpdateTechnicalComponentDetailsRequest,
    ) -> UpdateTechnicalComponentDetailsResponse:
        request.validate()

        specification = None
        if (
            request.specification_schema_key is not None
            and request.specification_entries is not None
        ):
            specification = TechnicalSpecification(
                schema_key=request.specification_schema_key,
                entries=tuple(
                    SpecificationEntry(
                        key=entry.key,
                        value=entry.value,
                        unit=entry.unit,
                    )
                    for entry in request.specification_entries
                ),
            )

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

                configuration.update_component_details(
                    request.component_id,
                    name=request.name,
                    manufacturer=request.manufacturer,
                    model=request.model,
                    serial_number=request.serial_number,
                    build_year=request.build_year,
                    notes=request.notes,
                    specification=specification,
                )
                repository.update(configuration)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except TechnicalConfigurationError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Update technical component details failed") from exc

        return UpdateTechnicalComponentDetailsResponse(
            configuration=to_configuration_response(configuration)
        )
