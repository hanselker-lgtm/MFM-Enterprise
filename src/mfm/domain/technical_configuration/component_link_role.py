"""Technical component link role enum."""

from enum import Enum


class ComponentLinkRole(str, Enum):
    """Describes structural relationship between two components."""

    DRIVES = "DRIVES"
    COUPLED_TO = "COUPLED_TO"
    FEEDS = "FEEDS"
    CONTROLS = "CONTROLS"
    CONNECTS_TO = "CONNECTS_TO"
