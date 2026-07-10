"""Committee status enum."""

from enum import Enum


class CommitteeStatus(str, Enum):
    """Lifecycle status for a committee aggregate."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
