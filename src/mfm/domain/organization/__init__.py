"""Organization domain package."""

from mfm.domain.organization.board import Board
from mfm.domain.organization.board_member import BoardMember
from mfm.domain.organization.board_status import BoardStatus
from mfm.domain.organization.board_term import BoardTerm
from mfm.domain.organization.committee import Committee
from mfm.domain.organization.committee_id import CommitteeId
from mfm.domain.organization.committee_member import CommitteeMember
from mfm.domain.organization.committee_status import CommitteeStatus
from mfm.domain.organization.volunteer import Volunteer
from mfm.domain.organization.volunteer import VolunteerCertificate
from mfm.domain.organization.volunteer_availability import VolunteerAvailability
from mfm.domain.organization.volunteer_id import VolunteerId
from mfm.domain.organization.volunteer_skill import VolunteerSkill
from mfm.domain.organization.volunteer_status import VolunteerStatus
from mfm.domain.organization.exceptions import BoardChairRequirementError
from mfm.domain.organization.exceptions import BoardError
from mfm.domain.organization.exceptions import BoardMemberNotFoundError
from mfm.domain.organization.exceptions import CommitteeError
from mfm.domain.organization.exceptions import CommitteeMemberNotFoundError
from mfm.domain.organization.exceptions import CommitteeSerializationError
from mfm.domain.organization.exceptions import VolunteerCertificateNotFoundError
from mfm.domain.organization.exceptions import VolunteerError
from mfm.domain.organization.exceptions import VolunteerSerializationError
from mfm.domain.organization.exceptions import VolunteerSkillNotFoundError
from mfm.domain.organization.exceptions import DuplicateOrganizationNumberError
from mfm.domain.organization.exceptions import DuplicateCommitteeMemberError
from mfm.domain.organization.exceptions import DuplicateBoardRoleError
from mfm.domain.organization.exceptions import DuplicateVolunteerCertificateError
from mfm.domain.organization.exceptions import DuplicateVolunteerSkillError
from mfm.domain.organization.exceptions import InvalidOrganizationNameError
from mfm.domain.organization.exceptions import InvalidOrganizationNumberError
from mfm.domain.organization.exceptions import InvalidOrganizationStatusTransitionError
from mfm.domain.organization.exceptions import DuplicateRoleCodeError
from mfm.domain.organization.exceptions import InvalidCommitteeMemberOperationError
from mfm.domain.organization.exceptions import InvalidCommitteeNameError
from mfm.domain.organization.exceptions import InvalidCommitteeStatusTransitionError
from mfm.domain.organization.exceptions import InvalidVolunteerAvailabilityError
from mfm.domain.organization.exceptions import InvalidVolunteerReferenceError
from mfm.domain.organization.exceptions import InvalidVolunteerSkillError
from mfm.domain.organization.exceptions import InvalidVolunteerStatusTransitionError
from mfm.domain.organization.exceptions import InvalidBoardMemberOperationError
from mfm.domain.organization.exceptions import InvalidBoardNameError
from mfm.domain.organization.exceptions import InvalidBoardStatusTransitionError
from mfm.domain.organization.exceptions import InvalidBoardTermError
from mfm.domain.organization.exceptions import InvalidRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleIdentityMutationError
from mfm.domain.organization.exceptions import InvalidRoleNameError
from mfm.domain.organization.exceptions import InvalidRoleStatusTransitionError
from mfm.domain.organization.exceptions import OrganizationError
from mfm.domain.organization.exceptions import OrganizationSerializationError
from mfm.domain.organization.exceptions import RoleError
from mfm.domain.organization.exceptions import RoleSerializationError
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType
from mfm.domain.organization.role import Role
from mfm.domain.organization.role_code import RoleCode
from mfm.domain.organization.role_id import RoleId
from mfm.domain.organization.role_status import RoleStatus
from mfm.domain.organization.role_type import RoleType

__all__ = [
    "Board",
    "BoardChairRequirementError",
    "BoardError",
    "BoardMember",
    "BoardMemberNotFoundError",
    "BoardStatus",
    "BoardTerm",
    "DuplicateBoardRoleError",
    "Committee",
    "CommitteeError",
    "CommitteeId",
    "CommitteeMember",
    "CommitteeMemberNotFoundError",
    "CommitteeSerializationError",
    "CommitteeStatus",
    "DuplicateCommitteeMemberError",
    "DuplicateVolunteerCertificateError",
    "DuplicateVolunteerSkillError",
    "DuplicateOrganizationNumberError",
    "DuplicateRoleCodeError",
    "InvalidBoardMemberOperationError",
    "InvalidBoardNameError",
    "InvalidBoardStatusTransitionError",
    "InvalidBoardTermError",
    "InvalidCommitteeMemberOperationError",
    "InvalidCommitteeNameError",
    "InvalidCommitteeStatusTransitionError",
    "InvalidVolunteerAvailabilityError",
    "InvalidVolunteerReferenceError",
    "InvalidVolunteerSkillError",
    "InvalidVolunteerStatusTransitionError",
    "InvalidOrganizationNameError",
    "InvalidOrganizationNumberError",
    "InvalidOrganizationStatusTransitionError",
    "InvalidRoleCodeError",
    "InvalidRoleIdentityMutationError",
    "InvalidRoleNameError",
    "InvalidRoleStatusTransitionError",
    "Organization",
    "OrganizationError",
    "OrganizationId",
    "OrganizationNumber",
    "OrganizationSerializationError",
    "OrganizationStatus",
    "OrganizationType",
    "Role",
    "RoleCode",
    "RoleError",
    "RoleId",
    "RoleSerializationError",
    "RoleStatus",
    "RoleType",
    "Volunteer",
    "VolunteerAvailability",
    "VolunteerCertificate",
    "VolunteerCertificateNotFoundError",
    "VolunteerError",
    "VolunteerId",
    "VolunteerSerializationError",
    "VolunteerSkill",
    "VolunteerSkillNotFoundError",
    "VolunteerStatus",
]
