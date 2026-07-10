"""Organization domain package."""

from mfm.domain.organization.exceptions import DuplicateOrganizationNumberError
from mfm.domain.organization.exceptions import InvalidOrganizationNameError
from mfm.domain.organization.exceptions import InvalidOrganizationNumberError
from mfm.domain.organization.exceptions import InvalidOrganizationStatusTransitionError
from mfm.domain.organization.exceptions import OrganizationError
from mfm.domain.organization.exceptions import OrganizationSerializationError
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType

__all__ = [
    "DuplicateOrganizationNumberError",
    "InvalidOrganizationNameError",
    "InvalidOrganizationNumberError",
    "InvalidOrganizationStatusTransitionError",
    "Organization",
    "OrganizationError",
    "OrganizationId",
    "OrganizationNumber",
    "OrganizationSerializationError",
    "OrganizationStatus",
    "OrganizationType",
]
