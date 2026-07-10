"""Asset status enum."""

from enum import Enum


class AssetStatus(str, Enum):
    """Lifecycle status for an asset."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    RETIRED = "RETIRED"
    DISPOSED = "DISPOSED"
