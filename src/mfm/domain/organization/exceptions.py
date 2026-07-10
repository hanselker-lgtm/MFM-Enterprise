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


class RoleError(Exception):
    """Base exception for role domain errors."""


class InvalidRoleNameError(RoleError):
    """Raised when role name is missing or invalid."""


class InvalidRoleCodeError(RoleError):
    """Raised when role code is missing or invalid."""


class DuplicateRoleCodeError(RoleError):
    """Raised when role code uniqueness is violated."""


class InvalidRoleStatusTransitionError(RoleError):
    """Raised when role status transition is not allowed."""


class InvalidRoleValidityPeriodError(RoleError):
    """Raised when role validity period is inconsistent."""


class InvalidRoleIdentityMutationError(RoleError):
    """Raised when role identity fields are mutated after creation."""


class RoleSerializationError(RoleError):
    """Raised when serialized role payload is invalid."""
