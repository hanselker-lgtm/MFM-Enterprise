"""Domain exceptions for Member."""


class MemberError(Exception):
    """Base exception for member domain errors."""


class InvalidMemberNumberError(MemberError):
    """Raised when member_number is missing or invalid."""


class InvalidMemberReferenceError(MemberError):
    """Raised when contact reference is invalid."""


class InvalidMembershipDatesError(MemberError):
    """Raised when membership dates are inconsistent."""


class DuplicateMemberNumberError(MemberError):
    """Raised when a member_number already exists."""


class ContactReferenceNotFoundError(MemberError):
    """Raised when the referenced contact does not exist."""


class MemberNotFoundError(MemberError):
    """Raised when a member could not be found."""


class InvalidMemberStatusTransitionError(MemberError):
    """Raised when a member status transition is not allowed."""
