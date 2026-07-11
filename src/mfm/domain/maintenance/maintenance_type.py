"""Maintenance type enum."""

from enum import Enum


class MaintenanceType(str, Enum):
    """Supported maintenance categories."""

    PREVENTIVE = "PREVENTIVE"
    CORRECTIVE = "CORRECTIVE"
    INSPECTION = "INSPECTION"
    CONDITION_BASED = "CONDITION_BASED"
    RESTORATION = "RESTORATION"
