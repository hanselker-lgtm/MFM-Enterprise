"""Domain exceptions for the Voyages capability."""


class VoyageError(Exception):
    """Base exception for voyages domain errors."""


class InvalidVoyageStateError(VoyageError):
    """Raised when voyage aggregate invariants are violated."""


class InvalidVoyageLifecycleError(VoyageError):
    """Raised when voyage lifecycle transition is invalid."""


class InvalidVoyageChronologyError(VoyageError):
    """Raised when voyage chronology or timestamps are invalid."""


class InvalidVoyageLocationError(VoyageError):
    """Raised when location snapshot data is invalid."""


class InvalidVoyagePurposeError(VoyageError):
    """Raised when voyage purpose data is invalid."""