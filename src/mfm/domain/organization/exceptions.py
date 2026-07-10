"""Domain exceptions for Organization."""


class OrganizationError(Exception):
    """Base exception for organization domain errors."""


class InvalidOrganizationNameError(OrganizationError):
    """Raised when organization name is missing or invalid."""


class InvalidOrganizationNumberError(OrganizationError):
    """Raised when organization number is missing or invalid."""


class DuplicateOrganizationNumberError(OrganizationError):
    """Raised when organization number uniqueness is violated."""


class InvalidOrganizationStatusTransitionError(OrganizationError):
    """Raised when organization status transition is not allowed."""


class OrganizationSerializationError(OrganizationError):
    """Raised when serialized organization payload is invalid."""
