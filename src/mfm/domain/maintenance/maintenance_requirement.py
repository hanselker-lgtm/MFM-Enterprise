"""Maintenance requirement entity."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from datetime import timedelta
from uuid import UUID

from mfm.domain.maintenance.exceptions import InvalidMaintenanceDueCalculationError
from mfm.domain.maintenance.exceptions import InvalidMaintenanceRequirementError
from mfm.domain.maintenance.identifiers import MaintenanceRequirementId
from mfm.domain.maintenance.maintenance_due_basis import MaintenanceDueBasis
from mfm.domain.maintenance.maintenance_interval import MaintenanceInterval
from mfm.domain.maintenance.maintenance_interval_type import MaintenanceIntervalType
from mfm.domain.maintenance.maintenance_requirement_status import (
    MaintenanceRequirementStatus,
)
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.domain.maintenance.maintenance_type import MaintenanceType


def _add_months(base: date, months: int) -> date:
    month_index = base.month - 1 + months
    year = base.year + month_index // 12
    month = month_index % 12 + 1

    month_days = [
        31,
        29
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]
    day = min(base.day, month_days[month - 1])
    return date(year, month, day)


def _add_years(base: date, years: int) -> date:
    try:
        return base.replace(year=base.year + years)
    except ValueError:
        return base.replace(month=2, day=28, year=base.year + years)


@dataclass(slots=True)
class MaintenanceRequirement:
    """Long-lived maintenance requirement under MaintenancePlan."""

    id: MaintenanceRequirementId
    title: str
    description: str
    maintenance_target: MaintenanceTarget
    maintenance_type: MaintenanceType
    interval: MaintenanceInterval
    due_basis: MaintenanceDueBasis
    last_completed: date | int | None = None
    next_due: date | int | None = None
    status: MaintenanceRequirementStatus = MaintenanceRequirementStatus.ACTIVE
    instructions: str | None = None
    notes: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.id, MaintenanceRequirementId):
            self.id = MaintenanceRequirementId(self.id)

        self.title = self._normalize_text(self.title, "title")
        self.description = self._normalize_text(self.description, "description")

        if not isinstance(self.maintenance_target, MaintenanceTarget):
            raise InvalidMaintenanceRequirementError(
                "maintenance_target must be MaintenanceTarget"
            )

        if not isinstance(self.maintenance_type, MaintenanceType):
            try:
                self.maintenance_type = MaintenanceType(str(self.maintenance_type).upper())
            except Exception as exc:
                raise InvalidMaintenanceRequirementError(
                    "maintenance_type is invalid"
                ) from exc

        if not isinstance(self.interval, MaintenanceInterval):
            raise InvalidMaintenanceRequirementError("interval must be MaintenanceInterval")

        if not isinstance(self.due_basis, MaintenanceDueBasis):
            try:
                self.due_basis = MaintenanceDueBasis(str(self.due_basis).upper())
            except Exception as exc:
                raise InvalidMaintenanceRequirementError("due_basis is invalid") from exc

        self.interval.validate_due_basis(self.due_basis)

        if not isinstance(self.status, MaintenanceRequirementStatus):
            try:
                self.status = MaintenanceRequirementStatus(str(self.status).upper())
            except Exception as exc:
                raise InvalidMaintenanceRequirementError("status is invalid") from exc

        if self.instructions is not None:
            self.instructions = self._normalize_optional_text(
                self.instructions,
                "instructions",
            )

        if self.notes is not None:
            self.notes = self._normalize_optional_text(self.notes, "notes")

        self._validate_due_state()
        if self.last_completed is not None:
            self.next_due = self._compute_next_due_from_last()

    @staticmethod
    def _normalize_text(value: str, field_name: str) -> str:
        if not isinstance(value, str):
            raise InvalidMaintenanceRequirementError(f"{field_name} must be string")
        normalized = value.strip()
        if not normalized:
            raise InvalidMaintenanceRequirementError(
                f"{field_name} must be a non-empty string"
            )
        return normalized

    @staticmethod
    def _normalize_optional_text(value: str, field_name: str) -> str | None:
        if not isinstance(value, str):
            raise InvalidMaintenanceRequirementError(
                f"{field_name} must be string or None"
            )
        return value.strip() or None

    def _validate_due_state(self) -> None:
        if self.due_basis is MaintenanceDueBasis.CALENDAR_DATE:
            if self.last_completed is not None and not isinstance(self.last_completed, date):
                raise InvalidMaintenanceRequirementError(
                    "last_completed must be date for CALENDAR_DATE due basis"
                )
            if self.next_due is not None and not isinstance(self.next_due, date):
                raise InvalidMaintenanceRequirementError(
                    "next_due must be date for CALENDAR_DATE due basis"
                )
            return

        if self.last_completed is not None:
            if not isinstance(self.last_completed, int) or self.last_completed < 0:
                raise InvalidMaintenanceRequirementError(
                    "last_completed must be non-negative int for RUNNING_HOURS due basis"
                )
        if self.next_due is not None:
            if not isinstance(self.next_due, int) or self.next_due < 0:
                raise InvalidMaintenanceRequirementError(
                    "next_due must be non-negative int for RUNNING_HOURS due basis"
                )

    def _compute_next_due_from_last(self) -> date | int:
        if self.last_completed is None:
            raise InvalidMaintenanceDueCalculationError(
                "last_completed is required before next_due can be computed"
            )

        if self.due_basis is MaintenanceDueBasis.RUNNING_HOURS:
            if not isinstance(self.last_completed, int):
                raise InvalidMaintenanceDueCalculationError(
                    "last_completed must be running hours integer"
                )
            return self.last_completed + self.interval.interval_value

        if not isinstance(self.last_completed, date):
            raise InvalidMaintenanceDueCalculationError(
                "last_completed must be date for calendar due basis"
            )

        if self.interval.interval_type is MaintenanceIntervalType.CALENDAR_DAYS:
            return self.last_completed + timedelta(days=self.interval.interval_value)
        if self.interval.interval_type is MaintenanceIntervalType.CALENDAR_MONTHS:
            return _add_months(self.last_completed, self.interval.interval_value)
        if self.interval.interval_type is MaintenanceIntervalType.CALENDAR_YEARS:
            return _add_years(self.last_completed, self.interval.interval_value)

        raise InvalidMaintenanceDueCalculationError(
            "calendar due basis is incompatible with non-calendar interval"
        )

    def update(
        self,
        *,
        title: str | None = None,
        description: str | None = None,
        maintenance_type: MaintenanceType | None = None,
        interval: MaintenanceInterval | None = None,
        due_basis: MaintenanceDueBasis | None = None,
        instructions: str | None = None,
        notes: str | None = None,
    ) -> None:
        if title is not None:
            self.title = self._normalize_text(title, "title")
        if description is not None:
            self.description = self._normalize_text(description, "description")
        if maintenance_type is not None:
            if not isinstance(maintenance_type, MaintenanceType):
                maintenance_type = MaintenanceType(str(maintenance_type).upper())
            self.maintenance_type = maintenance_type

        if due_basis is not None:
            if not isinstance(due_basis, MaintenanceDueBasis):
                due_basis = MaintenanceDueBasis(str(due_basis).upper())
            self.due_basis = due_basis

        if interval is not None:
            if not isinstance(interval, MaintenanceInterval):
                raise InvalidMaintenanceRequirementError(
                    "interval must be MaintenanceInterval"
                )
            self.interval = interval

        self.interval.validate_due_basis(self.due_basis)

        if instructions is not None:
            self.instructions = self._normalize_optional_text(instructions, "instructions")
        if notes is not None:
            self.notes = self._normalize_optional_text(notes, "notes")

        self._validate_due_state()
        if self.last_completed is not None:
            self.next_due = self._compute_next_due_from_last()

    def record_completion(
        self,
        *,
        completed_on: date | None = None,
        completed_running_hours: int | None = None,
    ) -> None:
        if self.due_basis is MaintenanceDueBasis.CALENDAR_DATE:
            if not isinstance(completed_on, date):
                raise InvalidMaintenanceDueCalculationError(
                    "completed_on date is required for CALENDAR_DATE due basis"
                )
            self.last_completed = completed_on
            self.next_due = self._compute_next_due_from_last()
            return

        if completed_running_hours is None:
            raise InvalidMaintenanceDueCalculationError(
                "completed_running_hours is required for RUNNING_HOURS due basis"
            )
        if not isinstance(completed_running_hours, int) or completed_running_hours < 0:
            raise InvalidMaintenanceDueCalculationError(
                "completed_running_hours must be non-negative int"
            )

        self.last_completed = completed_running_hours
        self.next_due = self._compute_next_due_from_last()

    def is_due(
        self,
        *,
        as_of_date: date | None = None,
        current_running_hours: int | None = None,
    ) -> bool:
        if self.next_due is None:
            return False

        if self.due_basis is MaintenanceDueBasis.CALENDAR_DATE:
            if not isinstance(as_of_date, date):
                raise InvalidMaintenanceDueCalculationError(
                    "as_of_date is required for CALENDAR_DATE due basis"
                )
            return as_of_date >= self.next_due

        if current_running_hours is None:
            raise InvalidMaintenanceDueCalculationError(
                "current_running_hours is required for RUNNING_HOURS due basis"
            )
        if not isinstance(current_running_hours, int) or current_running_hours < 0:
            raise InvalidMaintenanceDueCalculationError(
                "current_running_hours must be non-negative int"
            )
        return current_running_hours >= self.next_due

    def is_overdue(
        self,
        *,
        as_of_date: date | None = None,
        current_running_hours: int | None = None,
    ) -> bool:
        if self.next_due is None:
            return False

        if self.due_basis is MaintenanceDueBasis.CALENDAR_DATE:
            if not isinstance(as_of_date, date):
                raise InvalidMaintenanceDueCalculationError(
                    "as_of_date is required for CALENDAR_DATE due basis"
                )
            return as_of_date > self.next_due

        if current_running_hours is None:
            raise InvalidMaintenanceDueCalculationError(
                "current_running_hours is required for RUNNING_HOURS due basis"
            )
        if not isinstance(current_running_hours, int) or current_running_hours < 0:
            raise InvalidMaintenanceDueCalculationError(
                "current_running_hours must be non-negative int"
            )
        return current_running_hours > self.next_due

    def signature(self) -> tuple[str, MaintenanceType, UUID, MaintenanceInterval]:
        """Signature used for duplicate requirement guard inside one plan."""
        return (
            self.title.casefold(),
            self.maintenance_type,
            self.maintenance_target.target_id,
            self.interval,
        )
