"""Organization domain package."""

from mfm.domain.organization.exceptions import DuplicateOrganizationNumberError
from mfm.domain.organization.exceptions import InvalidOrganizationNameError
from mfm.domain.organization.exceptions import InvalidOrganizationNumberError
from mfm.domain.organization.exceptions import InvalidOrganizationStatusTransitionError
from mfm.domain.organization.exceptions import DuplicateRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleIdentityMutationError
from mfm.domain.organization.exceptions import InvalidRoleNameError
from mfm.domain.organization.exceptions import InvalidRoleStatusTransitionError
from mfm.domain.organization.exceptions import InvalidRoleValidityPeriodError
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
from mfm.domain.organization.role_id import RoleCode
from mfm.domain.organization.role_id import RoleId
from mfm.domain.organization.role_status import RoleStatus
from mfm.domain.organization.role_type import RoleType

__all__ = [
    "DuplicateOrganizationNumberError",
    "DuplicateRoleCodeError",
    "InvalidOrganizationNameError",
    "InvalidOrganizationNumberError",
    "InvalidOrganizationStatusTransitionError",
    "InvalidRoleCodeError",
    "InvalidRoleIdentityMutationError",
    "InvalidRoleNameError",
    "InvalidRoleStatusTransitionError",
    "InvalidRoleValidityPeriodError",
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
]
