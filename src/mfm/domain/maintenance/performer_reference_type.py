"""Performer reference type enum."""

from enum import Enum


class PerformerReferenceType(str, Enum):
    """Identity source for a work performer."""

    MEMBER = "MEMBER"
    VOLUNTEER = "VOLUNTEER"
    EXTERNAL_PERSON = "EXTERNAL_PERSON"
    EXTERNAL_COMPANY = "EXTERNAL_COMPANY"
