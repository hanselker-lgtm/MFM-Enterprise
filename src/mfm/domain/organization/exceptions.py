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


class InvalidRoleAssignmentPeriodError(RoleError):
    """Raised when assignment period boundaries are invalid."""


class RoleAssignmentOverlapError(RoleError):
    """Raised when assignment periods overlap for same assignee."""


class ArchivedRoleAssignmentError(RoleError):
    """Raised when assignment is attempted for archived role."""


class RoleAssignmentNotFoundError(RoleError):
    """Raised when target role assignment does not exist."""


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


class VolunteerError(Exception):
    """Base exception for volunteer domain errors."""


class InvalidVolunteerReferenceError(VolunteerError):
    """Raised when volunteer contact/member references are invalid."""


class InvalidVolunteerStatusTransitionError(VolunteerError):
    """Raised when volunteer status transition is not allowed."""


class InvalidVolunteerSkillError(VolunteerError):
    """Raised when volunteer skill input is invalid."""


class DuplicateVolunteerSkillError(VolunteerError):
    """Raised when duplicate volunteer skill is added."""


class VolunteerSkillNotFoundError(VolunteerError):
    """Raised when volunteer skill is not found."""


class InvalidVolunteerAvailabilityError(VolunteerError):
    """Raised when volunteer availability input is invalid."""


class DuplicateVolunteerCertificateError(VolunteerError):
    """Raised when duplicate certificate is added."""


class VolunteerCertificateNotFoundError(VolunteerError):
    """Raised when volunteer certificate is not found."""


class VolunteerSerializationError(VolunteerError):
    """Raised when serialized volunteer payload is invalid."""
