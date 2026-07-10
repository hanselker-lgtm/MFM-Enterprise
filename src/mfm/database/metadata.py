"""
Database metadata.

Imports all ORM models so SQLAlchemy metadata
and Alembic can discover them.
"""

# Contact module

from mfm.database.models.contact_model import ContactModel
from mfm.database.models.contact_person_model import ContactPersonModel
from mfm.database.models.contact_organisation_model import ContactOrganisationModel
from mfm.database.models.contact_email_model import ContactEmailModel
from mfm.database.models.contact_phone_model import ContactPhoneModel
from mfm.database.models.contact_address_model import ContactAddressModel
from mfm.database.models.member_model import MemberModel
from mfm.database.models.organization_model import OrganizationModel
from mfm.database.models.board_model import BoardModel
from mfm.database.models.board_member_model import BoardMemberModel
from mfm.database.models.committee_model import CommitteeModel
from mfm.database.models.committee_member_model import CommitteeMemberModel
from mfm.database.models.volunteer_model import VolunteerModel
from mfm.database.models.role_model import RoleModel
from mfm.database.models.role_assignment_model import RoleAssignmentModel
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.person import Person
from mfm.domain.contact.organisation import Organisation
from mfm.domain.contact.address import Address
from mfm.domain.contact.email import Email
from mfm.domain.contact.phone import Phone
from mfm.domain.contact.contact_relation import ContactRelation
from mfm.domain.member.member import Member
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.board import Board
from mfm.domain.organization.committee import Committee
from mfm.domain.organization.volunteer import Volunteer
from mfm.domain.organization.role import Role


__all__ = [
    "Contact",
    "Person",
    "Organisation",
    "Address",
    "Email",
    "Phone",
    "ContactRelation",
    "ContactModel",
    "ContactPersonModel",
    "ContactOrganisationModel",
    "ContactEmailModel",
    "ContactPhoneModel",
    "ContactAddressModel",
    "MemberModel",
    "Member",
    "OrganizationModel",
    "BoardModel",
    "BoardMemberModel",
    "CommitteeModel",
    "CommitteeMemberModel",
    "VolunteerModel",
    "RoleModel",
    "RoleAssignmentModel",
    "Organization",
    "Board",
    "Committee",
    "Volunteer",
    "Role",
]