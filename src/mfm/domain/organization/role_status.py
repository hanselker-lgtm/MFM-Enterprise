"""Role status enum."""

from enum import Enum


class RoleStatus(str, Enum):
    """Lifecycle status for a role."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ARCHIVED = "ARCHIVED"
