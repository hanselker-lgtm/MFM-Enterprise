"""Technical component type enum."""

from enum import Enum


class TechnicalComponentType(str, Enum):
    """Supported component types in technical configuration."""

    PROPULSION_ENGINE = "PROPULSION_ENGINE"
    AUXILIARY_ENGINE = "AUXILIARY_ENGINE"
    GEARBOX = "GEARBOX"
    SHAFT = "SHAFT"
    PROPELLER = "PROPELLER"
    GENERATOR = "GENERATOR"
    PUMP = "PUMP"
    STEERING_GEAR = "STEERING_GEAR"
    TANK = "TANK"
    OTHER = "OTHER"
