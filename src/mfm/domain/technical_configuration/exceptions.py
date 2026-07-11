"""Domain exceptions for Technical Configuration aggregate."""


class TechnicalConfigurationError(Exception):
    """Base exception for technical configuration domain errors."""


class InvalidTechnicalConfigurationVesselIdError(TechnicalConfigurationError):
    """Raised when vessel_id reference is missing or invalid."""


class InvalidTechnicalConfigurationStatusTransitionError(TechnicalConfigurationError):
    """Raised when configuration lifecycle transition is not allowed."""


class InvalidTechnicalComponentNameError(TechnicalConfigurationError):
    """Raised when component name is missing or invalid."""


class InvalidTechnicalComponentTypeError(TechnicalConfigurationError):
    """Raised when component type is missing or invalid."""


class InvalidTechnicalComponentStatusError(TechnicalConfigurationError):
    """Raised when component lifecycle status is missing or invalid."""


class DuplicateTechnicalComponentError(TechnicalConfigurationError):
    """Raised when duplicate component identity/rules are violated."""


class TechnicalComponentNotFoundError(TechnicalConfigurationError):
    """Raised when a component cannot be found in the aggregate."""


class InvalidTechnicalComponentLifecycleError(TechnicalConfigurationError):
    """Raised when a component lifecycle transition is not allowed."""


class TechnicalComponentAlreadyInstalledError(TechnicalConfigurationError):
    """Raised when install is attempted for an already installed component."""


class InvalidChronologyError(TechnicalConfigurationError):
    """Raised when chronological date ordering is invalid."""


class InvalidTechnicalSpecificationError(TechnicalConfigurationError):
    """Raised when technical specification payload is invalid."""


class InvalidComponentLinkError(TechnicalConfigurationError):
    """Raised when component link data is invalid."""


class ComponentLinkNotFoundError(TechnicalConfigurationError):
    """Raised when a component link cannot be found."""


class InvalidReplacementRelationError(TechnicalConfigurationError):
    """Raised when replacement relationship rules are violated."""
