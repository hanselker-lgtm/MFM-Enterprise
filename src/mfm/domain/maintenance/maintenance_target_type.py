"""Maintenance target type enum."""

from enum import Enum


class MaintenanceTargetType(str, Enum):
    """Supported maintenance target types."""

    VESSEL = "VESSEL"
    TECHNICAL_COMPONENT = "TECHNICAL_COMPONENT"
