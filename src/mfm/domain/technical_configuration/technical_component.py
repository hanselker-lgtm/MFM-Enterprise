"""Technical component entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date

from mfm.domain.technical_configuration.exceptions import InvalidChronologyError
from mfm.domain.technical_configuration.exceptions import (
    InvalidTechnicalComponentLifecycleError,
)
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalComponentNameError
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalComponentStatusError
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalComponentTypeError
from mfm.domain.technical_configuration.exceptions import TechnicalComponentAlreadyInstalledError
from mfm.domain.technical_configuration.identifiers import TechnicalComponentId
from mfm.domain.technical_configuration.technical_component_status import (
    TechnicalComponentStatus,
)
from mfm.domain.technical_configuration.technical_component_type import (
    TechnicalComponentType,
)
from mfm.domain.technical_configuration.technical_specification import (
    TechnicalSpecification,
)
from mfm.domain.technical_configuration.value_objects import BuildYear
from mfm.domain.technical_configuration.value_objects import ComponentModelName
from mfm.domain.technical_configuration.value_objects import ComponentNotes
from mfm.domain.technical_configuration.value_objects import ManufacturerName
from mfm.domain.technical_configuration.value_objects import SerialNumber


@dataclass(slots=True)
class TechnicalComponent:
    """Entity representing one technical component in a configuration."""

    id: TechnicalComponentId = field(default_factory=TechnicalComponentId.new)
    component_type: TechnicalComponentType = TechnicalComponentType.OTHER
    name: str = ""
    manufacturer: ManufacturerName | None = None
    model: ComponentModelName | None = None
    serial_number: SerialNumber | None = None
    build_year: BuildYear | None = None
    installed_date: date | None = None
    removed_date: date | None = None
    status: TechnicalComponentStatus = TechnicalComponentStatus.PLANNED
    notes: ComponentNotes | None = None
    specification: TechnicalSpecification = field(
        default_factory=lambda: TechnicalSpecification(schema_key="GENERIC_V1")
    )
    replacement_successor_id: TechnicalComponentId | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.id, TechnicalComponentId):
            self.id = TechnicalComponentId(self.id)

        if not isinstance(self.component_type, TechnicalComponentType):
            try:
                self.component_type = TechnicalComponentType(str(self.component_type).upper())
            except Exception as exc:
                raise InvalidTechnicalComponentTypeError("component_type is invalid") from exc

        self.name = self._normalize_name(self.name)

        if self.manufacturer is not None and not isinstance(
            self.manufacturer, ManufacturerName
        ):
            self.manufacturer = ManufacturerName(str(self.manufacturer))

        if self.model is not None and not isinstance(self.model, ComponentModelName):
            self.model = ComponentModelName(str(self.model))

        if self.serial_number is not None and not isinstance(self.serial_number, SerialNumber):
            self.serial_number = SerialNumber(str(self.serial_number))

        if self.build_year is not None and not isinstance(self.build_year, BuildYear):
            self.build_year = BuildYear(int(self.build_year))

        if self.installed_date is not None and not isinstance(self.installed_date, date):
            raise InvalidChronologyError("installed_date must be date or None")

        if self.removed_date is not None and not isinstance(self.removed_date, date):
            raise InvalidChronologyError("removed_date must be date or None")

        if self.installed_date is not None and self.removed_date is not None:
            if self.removed_date < self.installed_date:
                raise InvalidChronologyError(
                    "removed_date cannot be before installed_date"
                )

        if not isinstance(self.status, TechnicalComponentStatus):
            try:
                self.status = TechnicalComponentStatus(str(self.status).upper())
            except Exception as exc:
                raise InvalidTechnicalComponentStatusError("component status is invalid") from exc

        if self.notes is not None and not isinstance(self.notes, ComponentNotes):
            self.notes = ComponentNotes(str(self.notes))

        if not isinstance(self.specification, TechnicalSpecification):
            raise TypeError("specification must be TechnicalSpecification")

        if (
            self.replacement_successor_id is not None
            and not isinstance(self.replacement_successor_id, TechnicalComponentId)
        ):
            self.replacement_successor_id = TechnicalComponentId(
                self.replacement_successor_id
            )

        self._validate_lifecycle_consistency()

    @staticmethod
    def _normalize_name(value: str) -> str:
        if not isinstance(value, str):
            raise InvalidTechnicalComponentNameError("name must be a string")
        normalized = value.strip()
        if not normalized:
            raise InvalidTechnicalComponentNameError("name cannot be empty")
        return normalized

    def _validate_lifecycle_consistency(self) -> None:
        if self.status is TechnicalComponentStatus.PLANNED:
            if self.installed_date is not None or self.removed_date is not None:
                raise InvalidTechnicalComponentLifecycleError(
                    "planned component cannot have installed/removed dates"
                )

        if self.status is TechnicalComponentStatus.INSTALLED:
            if self.installed_date is None:
                raise InvalidTechnicalComponentLifecycleError(
                    "installed component must have installed_date"
                )
            if self.removed_date is not None:
                raise InvalidTechnicalComponentLifecycleError(
                    "installed component cannot have removed_date"
                )

        if self.status in {
            TechnicalComponentStatus.REMOVED,
            TechnicalComponentStatus.RETIRED,
        }:
            if self.installed_date is None:
                raise InvalidTechnicalComponentLifecycleError(
                    "removed/retired component must have installed_date"
                )
            if self.removed_date is None:
                raise InvalidTechnicalComponentLifecycleError(
                    "removed/retired component must have removed_date"
                )

    @property
    def is_current(self) -> bool:
        return (
            self.status is TechnicalComponentStatus.INSTALLED
            and self.removed_date is None
            and self.replacement_successor_id is None
        )

    def install(self, installed_on: date) -> None:
        if not isinstance(installed_on, date):
            raise InvalidChronologyError("installed_on must be date")

        if self.status is TechnicalComponentStatus.INSTALLED and self.removed_date is None:
            raise TechnicalComponentAlreadyInstalledError(
                "component is already installed"
            )

        if self.status in {
            TechnicalComponentStatus.REMOVED,
            TechnicalComponentStatus.RETIRED,
        }:
            raise InvalidTechnicalComponentLifecycleError(
                "removed/retired component cannot be reinstalled"
            )

        self.installed_date = installed_on
        self.removed_date = None
        self.status = TechnicalComponentStatus.INSTALLED

    def remove(self, removed_on: date, *, retired: bool = False) -> None:
        if not isinstance(removed_on, date):
            raise InvalidChronologyError("removed_on must be date")

        if self.status is not TechnicalComponentStatus.INSTALLED:
            raise InvalidTechnicalComponentLifecycleError(
                "only installed component can be removed"
            )
        if self.installed_date is None:
            raise InvalidTechnicalComponentLifecycleError(
                "installed_date is required before remove"
            )
        if removed_on < self.installed_date:
            raise InvalidChronologyError("removed_on cannot be before installed_date")

        self.removed_date = removed_on
        self.status = (
            TechnicalComponentStatus.RETIRED
            if retired
            else TechnicalComponentStatus.REMOVED
        )

    def mark_replaced_by(self, successor_id: TechnicalComponentId) -> None:
        if not isinstance(successor_id, TechnicalComponentId):
            successor_id = TechnicalComponentId(successor_id)

        if not self.is_current:
            raise InvalidTechnicalComponentLifecycleError(
                "only current component can be marked as replaced"
            )
        if successor_id == self.id:
            raise InvalidTechnicalComponentLifecycleError(
                "component cannot replace itself"
            )

        self.replacement_successor_id = successor_id

    def update_details(
        self,
        *,
        name: str | None = None,
        manufacturer: ManufacturerName | str | None = None,
        model: ComponentModelName | str | None = None,
        serial_number: SerialNumber | str | None = None,
        build_year: BuildYear | int | None = None,
        notes: ComponentNotes | str | None = None,
        specification: TechnicalSpecification | None = None,
    ) -> None:
        if name is not None:
            self.name = self._normalize_name(name)
        if manufacturer is not None:
            self.manufacturer = (
                manufacturer
                if isinstance(manufacturer, ManufacturerName)
                else ManufacturerName(str(manufacturer))
            )
        if model is not None:
            self.model = (
                model if isinstance(model, ComponentModelName) else ComponentModelName(str(model))
            )
        if serial_number is not None:
            self.serial_number = (
                serial_number
                if isinstance(serial_number, SerialNumber)
                else SerialNumber(str(serial_number))
            )
        if build_year is not None:
            self.build_year = (
                build_year if isinstance(build_year, BuildYear) else BuildYear(int(build_year))
            )
        if notes is not None:
            self.notes = notes if isinstance(notes, ComponentNotes) else ComponentNotes(str(notes))
        if specification is not None:
            if not isinstance(specification, TechnicalSpecification):
                raise TypeError("specification must be TechnicalSpecification")
            self.specification = specification
