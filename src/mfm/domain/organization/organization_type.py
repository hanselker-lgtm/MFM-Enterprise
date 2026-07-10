"""Organization type enum."""

from enum import Enum


class OrganizationType(str, Enum):
    """Taxonomy for organization category."""

    ASSOCIATION = "ASSOCIATION"
    FOUNDATION = "FOUNDATION"
    COMPANY = "COMPANY"
    COMMITTEE = "COMMITTEE"
    OTHER = "OTHER"
