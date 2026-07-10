"""Volunteer status enum."""

from enum import Enum


class VolunteerStatus(str, Enum):
    """Lifecycle status for a volunteer aggregate."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    RETIRED = "RETIRED"
