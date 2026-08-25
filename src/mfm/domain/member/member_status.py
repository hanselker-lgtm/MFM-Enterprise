"""Member status enum."""

from enum import Enum


class MemberStatus(str, Enum):
    """Lifecycle status for a member."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
