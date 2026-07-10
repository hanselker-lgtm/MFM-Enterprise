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


class InvalidRoleIdentityMutationError(RoleError):
    """Raised when role identity fields are mutated after creation."""


class RoleSerializationError(RoleError):
    """Raised when serialized role payload is invalid."""


class BoardError(Exception):
    """Base exception for board domain errors."""


class InvalidBoardNameError(BoardError):
    """Raised when board name is missing or invalid."""


class InvalidBoardTermError(BoardError):
    """Raised when board term boundaries are invalid."""


class DuplicateBoardRoleError(BoardError):
    """Raised when the same role overlaps in the same term period."""


class BoardChairRequirementError(BoardError):
    """Raised when board has no chair."""


class BoardMemberNotFoundError(BoardError):
    """Raised when target board member assignment does not exist."""


class InvalidBoardStatusTransitionError(BoardError):
    """Raised when board transition is not allowed."""


class InvalidBoardMemberOperationError(BoardError):
    """Raised when board member operation is invalid."""


class CommitteeError(Exception):
    """Base exception for committee domain errors."""


class InvalidCommitteeNameError(CommitteeError):
    """Raised when committee name is missing or invalid."""


class DuplicateCommitteeMemberError(CommitteeError):
    """Raised when committee member appears as duplicate active assignment."""


class CommitteeMemberNotFoundError(CommitteeError):
    """Raised when committee member assignment does not exist."""


class InvalidCommitteeStatusTransitionError(CommitteeError):
    """Raised when committee transition is not allowed."""


class InvalidCommitteeMemberOperationError(CommitteeError):
    """Raised when committee member operation is invalid."""


class CommitteeSerializationError(CommitteeError):
    """Raised when serialized committee payload is invalid."""
