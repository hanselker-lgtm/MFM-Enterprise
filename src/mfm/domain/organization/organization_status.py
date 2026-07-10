"""Organization status enum."""

from enum import Enum


class OrganizationStatus(str, Enum):
    """Lifecycle status for an organization."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ARCHIVED = "ARCHIVED"
