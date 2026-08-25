"""Membership status enum."""

from enum import Enum


class MembershipStatus(str, Enum):
    """Lifecycle status for a membership."""

    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    ENDED = "ENDED"
    EXPIRED = "EXPIRED"
