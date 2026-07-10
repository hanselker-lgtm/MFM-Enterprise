"""Board status enum."""

from enum import Enum


class BoardStatus(str, Enum):
    """Lifecycle status for a board aggregate."""

    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"
