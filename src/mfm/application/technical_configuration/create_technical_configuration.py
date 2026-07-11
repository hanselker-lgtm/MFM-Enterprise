"""Create Technical Configuration use case."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.technical_configuration.exceptions import TechnicalConfigurationError
from mfm.domain.technical_configuration.technical_component import TechnicalComponent
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)
from mfm.domain.technical_configuration.technical_configuration import (
    TechnicalConfiguration,
)
from mfm.domain.technical_configuration.technical_specification import (
    SpecificationEntry,
)
from mfm.domain.technical_configuration.technical_specification import (
    TechnicalSpecification,
)
from mfm.domain.technical_configuration.value_objects import BuildYear
from mfm.domain.technical_configuration.value_objects import ComponentModelName
from mfm.domain.technical_configuration.value_objects import ComponentNotes
from mfm.domain.technical_configuration.value_objects import ManufacturerName
from mfm.domain.technical_configuration.value_objects import ReplacementReason
from mfm.domain.technical_configuration.value_objects import SerialNumber
from mfm.repositories.technical_configuration_repository import (
    TechnicalConfigurationRepository,
)


class ApplicationException(Exception):
    """Base exception for technical configuration application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository/persistence failures."""


PublicSpecificationValue = str | int | float | bool


@dataclass(frozen=True, slots=True)
class SpecificationEntryInput:
    key: str
    value: PublicSpecificationValue
    unit: str | None = None

    def validate(self) -> None:
        if not isinstance(self.key, str) or not self.key.strip():
            raise ValidationException("specification entry key must be a non-empty string")
        if not isinstance(self.value, (str, int, float, bool)):
            raise ValidationException("specification entry value must be str/int/float/bool")
        if self.unit is not None and not isinstance(self.unit, str):
            raise ValidationException("specification entry unit must be string or None")


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


class CreateTechnicalConfigurationUseCase:
    """Create technical configuration aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        request: CreateTechnicalConfigurationRequest,
    ) -> CreateTechnicalConfigurationResponse:
        request.validate()

        try:
            with self._unit_of_work as uow:
                repository: TechnicalConfigurationRepository = (
                    uow.technical_configuration_repository
                )

                if repository.get_by_vessel_id(request.vessel_id) is not None:
                    raise BusinessRuleViolation(
                        f"Technical configuration for vessel {request.vessel_id} already exists"
                    )

                configuration = TechnicalConfiguration(vessel_id=request.vessel_id)
                repository.add(configuration)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except TechnicalConfigurationError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create technical configuration failed") from exc

        return CreateTechnicalConfigurationResponse(
            configuration=to_configuration_response(configuration)
        )


def to_configuration_response(
    configuration: TechnicalConfiguration,
) -> TechnicalConfigurationResponse:
    return TechnicalConfigurationResponse(
        id=configuration.id.value,
        vessel_id=configuration.vessel_id,
        status=configuration.status.value,
        components=tuple(
            to_component_response(component)
            for component in configuration.list_components()
        ),
        replacement_history=tuple(
            ComponentReplacementRecordResponse(
                id=record.id.value,
                replaced_component_id=record.replaced_component_id.value,
                replacement_component_id=record.replacement_component_id.value,
                replaced_on=record.replaced_on,
                reason=record.reason.value,
                notes=record.notes.value if record.notes is not None else None,
            )
            for record in configuration.replacement_history()
        ),
    )


def to_component_response(component: TechnicalComponent) -> TechnicalComponentResponse:
    return TechnicalComponentResponse(
        id=component.id.value,
        component_type=component.component_type.value,
        name=component.name,
        manufacturer=(component.manufacturer.value if component.manufacturer else None),
        model=component.model.value if component.model else None,
        serial_number=(component.serial_number.value if component.serial_number else None),
        build_year=component.build_year.value if component.build_year else None,
        status=component.status.value,
        installed_date=component.installed_date,
        removed_date=component.removed_date,
        notes=component.notes.value if component.notes else None,
        specification_schema_key=component.specification.schema_key,
        specification_entries=tuple(
            TechnicalSpecificationEntryResponse(
                key=entry.key,
                value=entry.value,
                unit=entry.unit,
            )
            for entry in component.specification.entries
        ),
        replacement_successor_id=(
            component.replacement_successor_id.value
            if component.replacement_successor_id is not None
            else None
        ),
    )


def to_technical_component(
    *,
    component_id: UUID | None,
    component_type: TechnicalComponentType,
    name: str,
    manufacturer: str | None,
    model: str | None,
    serial_number: str | None,
    build_year: int | None,
    installed_date: date | None,
    removed_date: date | None,
    status: TechnicalComponentStatus,
    notes: str | None,
    specification_schema_key: str,
    specification_entries: tuple[SpecificationEntryInput, ...],
) -> TechnicalComponent:
    entries = tuple(
        SpecificationEntry(key=entry.key, value=entry.value, unit=entry.unit)
        for entry in specification_entries
    )

    kwargs: dict[str, object] = {}
    if component_id is not None:
        kwargs["id"] = component_id

    return TechnicalComponent(
        component_type=component_type,
        name=name,
        manufacturer=(
            ManufacturerName(manufacturer)
            if manufacturer is not None and manufacturer.strip()
            else None
        ),
        model=(
            ComponentModelName(model)
            if model is not None and model.strip()
            else None
        ),
        serial_number=(
            SerialNumber(serial_number)
            if serial_number is not None and serial_number.strip()
            else None
        ),
        build_year=BuildYear(build_year) if build_year is not None else None,
        installed_date=installed_date,
        removed_date=removed_date,
        status=status,
        notes=(
            ComponentNotes(notes)
            if notes is not None and notes.strip()
            else None
        ),
        specification=TechnicalSpecification(
            schema_key=specification_schema_key,
            entries=entries,
        ),
        **kwargs,
    )


def to_replacement_reason(value: str) -> ReplacementReason:
    return ReplacementReason(value)


def to_component_notes(value: str | None) -> ComponentNotes | None:
    if value is None or not value.strip():
        return None
    return ComponentNotes(value)
