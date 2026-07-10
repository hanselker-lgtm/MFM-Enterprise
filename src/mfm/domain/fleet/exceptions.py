"""Domain exceptions for Vessel aggregate."""


class VesselError(Exception):
    """Base exception for vessel domain errors."""


class InvalidVesselAssetIdError(VesselError):
    """Raised when vessel asset_id is missing or invalid."""


class InvalidVesselNameError(VesselError):
    """Raised when vessel name is missing or invalid."""


class InvalidVesselRegistrationError(VesselError):
    """Raised when vessel registration is missing or invalid."""


class DuplicateVesselRegistrationError(VesselError):
    """Raised when vessel registration uniqueness is violated."""


class InvalidVesselDimensionsError(VesselError):
    """Raised when vessel dimensions are invalid."""


class InvalidVesselStatusTransitionError(VesselError):
    """Raised when vessel status transition is not allowed."""
