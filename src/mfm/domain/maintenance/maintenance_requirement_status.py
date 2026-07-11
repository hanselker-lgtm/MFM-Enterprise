"""Maintenance requirement status enum."""

from enum import Enum


class MaintenanceRequirementStatus(str, Enum):
    """Lifecycle of a maintenance requirement within a plan."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
