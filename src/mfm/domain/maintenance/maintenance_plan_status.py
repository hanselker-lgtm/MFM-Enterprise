"""Maintenance plan status enum."""

from enum import Enum


class MaintenancePlanStatus(str, Enum):
    """Lifecycle of maintenance plan aggregate."""

    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
