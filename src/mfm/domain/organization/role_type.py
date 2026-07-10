"""Role type enum."""

from enum import Enum


class RoleType(str, Enum):
    """Taxonomy for role category."""

    BOARD = "BOARD"
    COMMITTEE = "COMMITTEE"
    OPERATIONAL = "OPERATIONAL"
    VOLUNTEER = "VOLUNTEER"
    CREW = "CREW"
    ADMINISTRATIVE = "ADMINISTRATIVE"
