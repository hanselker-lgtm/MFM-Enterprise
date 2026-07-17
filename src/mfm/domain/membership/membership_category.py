"""Membership category enum."""

from enum import Enum


class MembershipCategory(str, Enum):
    """Classify membership types for management and reporting."""

    GENERAL = "GENERAL"
    YOUTH = "YOUTH"
    SENIOR = "SENIOR"
    FAMILY = "FAMILY"
    CORPORATE = "CORPORATE"
