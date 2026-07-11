"""Maintenance due basis enum."""

from enum import Enum


class MaintenanceDueBasis(str, Enum):
    """Basis used to evaluate when requirement is due."""

    CALENDAR_DATE = "CALENDAR_DATE"
    RUNNING_HOURS = "RUNNING_HOURS"
