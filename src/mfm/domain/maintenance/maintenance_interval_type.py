"""Maintenance interval type enum."""

from enum import Enum


class MaintenanceIntervalType(str, Enum):
    """Supported interval units for maintenance requirements."""

    CALENDAR_DAYS = "CALENDAR_DAYS"
    CALENDAR_MONTHS = "CALENDAR_MONTHS"
    CALENDAR_YEARS = "CALENDAR_YEARS"
    RUNNING_HOURS = "RUNNING_HOURS"
