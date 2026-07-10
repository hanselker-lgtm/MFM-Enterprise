"""Vessel construction material enum."""

from enum import Enum


class VesselMaterial(str, Enum):
    """Construction material categories for vessels."""

    STEEL = "STEEL"
    ALUMINUM = "ALUMINUM"
    WOOD = "WOOD"
    FIBERGLASS = "FIBERGLASS"
    COMPOSITE = "COMPOSITE"
    OTHER = "OTHER"
