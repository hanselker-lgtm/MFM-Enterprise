"""Domain exceptions for Membership."""


class MembershipError(Exception):
    """Base exception for membership domain errors."""


class InvalidMembershipReferenceError(MembershipError):
    """Raised when member or membership type references are invalid."""


class InvalidMembershipTypeError(MembershipError):
    """Raised when membership type definition is invalid."""


class DuplicateMembershipTypeCodeError(MembershipError):
    """Raised when a membership type code already exists."""


class MembershipTypeNotFoundError(MembershipError):
    """Raised when a membership type cannot be found."""


class InvalidMembershipDatesError(MembershipError):
    """Raised when membership dates are inconsistent."""


class InvalidMembershipStatusTransitionError(MembershipError):
    """Raised when a membership status transition is invalid."""


class MultipleActiveMembershipsError(MembershipError):
    """Raised when more than one active membership exists for a member."""
