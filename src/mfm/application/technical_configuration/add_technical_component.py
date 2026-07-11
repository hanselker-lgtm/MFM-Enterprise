"""Add Technical Component use case."""

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
    to_configuration_response,
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
class AddTechnicalComponentRequest:
    configuration_id: UUID
    component_type: TechnicalComponentType
    name: str
    manufacturer: str | None = None
    model: str | None = None
    serial_number: str | None = None
    build_year: int | None = None
    installed_date: date | None = None
    removed_date: date | None = None
    status: TechnicalComponentStatus = TechnicalComponentStatus.PLANNED
    notes: str | None = None
    specification_schema_key: str = "GENERIC_V1"
    specification_entries: tuple[SpecificationEntryInput, ...] = ()
    component_id: UUID | None = None

    def validate(self) -> None:
        if not isinstance(self.configuration_id, UUID):
            raise ValidationException("configuration_id must be UUID")
        if not isinstance(self.component_type, TechnicalComponentType):
            raise ValidationException("component_type must be TechnicalComponentType")
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
        if not isinstance(self.status, TechnicalComponentStatus):
            raise ValidationException("status must be TechnicalComponentStatus")
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


class AddTechnicalComponentUseCase:
    """Add component to technical configuration in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: AddTechnicalComponentRequest) -> AddTechnicalComponentResponse:
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

                component = to_technical_component(
                    component_id=request.component_id,
                    component_type=request.component_type,
                    name=request.name,
                    manufacturer=request.manufacturer,
                    model=request.model,
                    serial_number=request.serial_number,
                    build_year=request.build_year,
                    installed_date=request.installed_date,
                    removed_date=request.removed_date,
                    status=request.status,
                    notes=request.notes,
                    specification_schema_key=request.specification_schema_key,
                    specification_entries=request.specification_entries,
                )
                configuration.add_component(component)
                repository.update(configuration)
                uow.commit()
        except (ValidationException, BusinessRuleViolation, ApplicationException):
            raise
        except TechnicalConfigurationError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Add technical component failed") from exc

        return AddTechnicalComponentResponse(
            configuration=to_configuration_response(configuration)
        )
