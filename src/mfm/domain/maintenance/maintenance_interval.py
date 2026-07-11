"""Maintenance interval value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.maintenance.exceptions import InvalidMaintenanceIntervalError
from mfm.domain.maintenance.maintenance_due_basis import MaintenanceDueBasis
from mfm.domain.maintenance.maintenance_interval_type import MaintenanceIntervalType


@dataclass(frozen=True, slots=True)
class MaintenanceInterval(ValueObject):
    """Controlled interval model for maintenance requirements."""

    interval_type: MaintenanceIntervalType
    interval_value: int

    def __post_init__(self) -> None:
        if not isinstance(self.interval_type, MaintenanceIntervalType):
            try:
                normalized = MaintenanceIntervalType(str(self.interval_type).upper())
            except Exception as exc:
                raise InvalidMaintenanceIntervalError("interval_type is invalid") from exc
            object.__setattr__(self, "interval_type", normalized)

        if not isinstance(self.interval_value, int) or self.interval_value <= 0:
            raise InvalidMaintenanceIntervalError(
                "interval_value must be a positive integer"
            )

    def validate_due_basis(self, due_basis: MaintenanceDueBasis) -> None:
        if not isinstance(due_basis, MaintenanceDueBasis):
            try:
                due_basis = MaintenanceDueBasis(str(due_basis).upper())
            except Exception as exc:
                raise InvalidMaintenanceIntervalError("due_basis is invalid") from exc

        if self.interval_type is MaintenanceIntervalType.RUNNING_HOURS:
            if due_basis is not MaintenanceDueBasis.RUNNING_HOURS:
                raise InvalidMaintenanceIntervalError(
                    "RUNNING_HOURS interval requires RUNNING_HOURS due basis"
                )
            return

        if due_basis is not MaintenanceDueBasis.CALENDAR_DATE:
            raise InvalidMaintenanceIntervalError(
                "calendar interval types require CALENDAR_DATE due basis"
            )
