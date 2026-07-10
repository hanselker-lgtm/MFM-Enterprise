"""Asset category enum."""

from enum import Enum


class AssetCategory(str, Enum):
    """Taxonomy for generic asset categories."""

    VESSEL = "VESSEL"
    ENGINE = "ENGINE"
    EQUIPMENT = "EQUIPMENT"
    BUILDING = "BUILDING"
    TOOL = "TOOL"
    OTHER = "OTHER"
