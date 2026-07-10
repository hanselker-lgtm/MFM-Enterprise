"""Mapper between organization domain aggregates and persistence models."""

from __future__ import annotations

import json
from datetime import date
from uuid import UUID

from mfm.database.models.board_member_model import BoardMemberModel
from mfm.database.models.board_model import BoardModel
from mfm.database.models.committee_member_model import CommitteeMemberModel
from mfm.database.models.committee_model import CommitteeModel
from mfm.database.models.organization_model import OrganizationModel
from mfm.database.models.role_assignment_model import RoleAssignmentModel
from mfm.database.models.role_model import RoleModel
from mfm.database.models.volunteer_model import VolunteerModel
from mfm.domain.organization.board import Board
from mfm.domain.organization.board_member import BoardMember
from mfm.domain.organization.committee import Committee
from mfm.domain.organization.committee_id import CommitteeId
from mfm.domain.organization.committee_member import CommitteeMember
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.role import Role
from mfm.domain.organization.role_assignment import RoleAssignment
from mfm.domain.organization.role_code import RoleCode
from mfm.domain.organization.role_id import RoleId
from mfm.domain.organization.volunteer import Volunteer
from mfm.domain.organization.volunteer import VolunteerCertificate
from mfm.domain.organization.volunteer_availability import VolunteerAvailability
from mfm.domain.organization.volunteer_id import VolunteerId
from mfm.domain.organization.volunteer_skill import VolunteerSkill


class OrganizationMapper:
    """Map between organization domain entities and SQLAlchemy models."""

    @staticmethod
    def to_orm_organization(organization: Organization) -> OrganizationModel:
        return OrganizationModel(
            id=organization.id.value,
            organization_number=organization.organization_number.value,
            name=organization.name,
            organization_type=organization.organization_type,
            status=organization.status,
            created_at=organization.created_at,
            updated_at=organization.updated_at,
        )

    @staticmethod
    def to_domain_organization(orm: OrganizationModel) -> Organization:
        return Organization(
            id=OrganizationId(orm.id),
            organization_number=OrganizationNumber(orm.organization_number),
            name=orm.name,
            organization_type=orm.organization_type,
            status=orm.status,
            created_at=orm.created_at,
            updated_at=orm.updated_at,
        )

    @staticmethod
    def to_orm_board(board: Board) -> BoardModel:
        orm = BoardModel(
            id=board.id,
            organization_id=board.organization_id.value,
            name=board.name,
            term_start=board.term_start,
            term_end=board.term_end,
            status=board.status,
        )
        orm.members = [
            BoardMemberModel(
                board_id=board.id,
                member_id=member.member_id,
                role=member.role,
                appointed_on=member.appointed_on,
                resigned_on=member.resigned_on,
                is_chair=member.is_chair,
            )
            for member in board.members
        ]
        return orm

    @staticmethod
    def to_domain_board(orm: BoardModel) -> Board:
        return Board(
            id=orm.id,
            organization_id=OrganizationId(orm.organization_id),
            name=orm.name,
            term_start=orm.term_start,
            term_end=orm.term_end,
            status=orm.status,
            members=[
                BoardMember(
                    member_id=member.member_id,
                    role=member.role,
                    appointed_on=member.appointed_on,
                    resigned_on=member.resigned_on,
                    is_chair=member.is_chair,
                )
                for member in orm.members
            ],
        )

    @staticmethod
    def to_orm_committee(committee: Committee) -> CommitteeModel:
        orm = CommitteeModel(
            id=committee.id.value,
            organization_id=committee.organization_id.value,
            name=committee.name,
            purpose=committee.purpose,
            status=committee.status,
            created_at=committee.created_at,
            updated_at=committee.updated_at,
        )
        orm.members = [
            CommitteeMemberModel(
                committee_id=committee.id.value,
                reference_id=member.reference_id,
                function_title=member.function_title,
                joined_at=member.joined_at,
                left_at=member.left_at,
            )
            for member in committee.members
        ]
        return orm

    @staticmethod
    def to_domain_committee(orm: CommitteeModel) -> Committee:
        return Committee(
            id=CommitteeId(orm.id),
            organization_id=OrganizationId(orm.organization_id),
            name=orm.name,
            purpose=orm.purpose,
            status=orm.status,
            members=[
                CommitteeMember(
                    reference_id=member.reference_id,
                    function_title=member.function_title,
                    joined_at=member.joined_at,
                    left_at=member.left_at,
                )
                for member in orm.members
            ],
            created_at=orm.created_at,
            updated_at=orm.updated_at,
        )

    @staticmethod
    def to_orm_volunteer(volunteer: Volunteer) -> VolunteerModel:
        certificates_payload = [
            {
                "name": certificate.name,
                "expires_at": (
                    certificate.expires_at.isoformat()
                    if certificate.expires_at is not None
                    else None
                ),
            }
            for certificate in volunteer.certificates
        ]

        return VolunteerModel(
            id=volunteer.id.value,
            contact_id=volunteer.contact_id,
            member_id=volunteer.member_id,
            status=volunteer.status,
            joined_at=volunteer.joined_at,
            left_at=volunteer.left_at,
            is_available=volunteer.availability.is_available,
            max_hours_per_week=volunteer.availability.max_hours_per_week,
            preferred_days=",".join(volunteer.availability.preferred_days),
            skills=",".join(str(skill) for skill in volunteer.skills),
            certificates=json.dumps(certificates_payload, separators=(",", ":")),
        )

    @staticmethod
    def to_domain_volunteer(orm: VolunteerModel) -> Volunteer:
        preferred_days = tuple(
            value for value in orm.preferred_days.split(",") if value
        )
        skills = [
            VolunteerSkill(value)
            for value in orm.skills.split(",")
            if value
        ]

        certificates_raw = json.loads(orm.certificates) if orm.certificates else []
        certificates = [
            VolunteerCertificate(
                name=item["name"],
                expires_at=(
                    None
                    if item.get("expires_at") is None
                    else date.fromisoformat(item["expires_at"])
                ),
            )
            for item in certificates_raw
        ]

        return Volunteer(
            id=VolunteerId(orm.id),
            contact_id=orm.contact_id,
            member_id=orm.member_id,
            status=orm.status,
            joined_at=orm.joined_at,
            left_at=orm.left_at,
            availability=VolunteerAvailability(
                is_available=orm.is_available,
                max_hours_per_week=orm.max_hours_per_week,
                preferred_days=preferred_days,
            ),
            skills=skills,
            certificates=certificates,
        )

    @staticmethod
    def to_orm_role(role: Role, *, organization_id: UUID) -> RoleModel:
        orm = RoleModel(
            id=role.id.value,
            organization_id=organization_id,
            role_code=role.role_code.value,
            name=role.name,
            description=role.description,
            category=role.category,
            status=role.status,
        )
        orm.assignments = [
            RoleAssignmentModel(
                role_id=assignment.role_id.value,
                assignee_id=assignment.assignee_id,
                organization_id=assignment.organization_id,
                valid_from=assignment.valid_from,
                valid_to=assignment.valid_to,
            )
            for assignment in role.assignments
        ]
        return orm

    @staticmethod
    def to_domain_role(orm: RoleModel) -> Role:
        return Role(
            id=RoleId(orm.id),
            role_code=RoleCode(orm.role_code),
            name=orm.name,
            description=orm.description,
            category=orm.category,
            status=orm.status,
            assignments=[
                RoleAssignment(
                    role_id=RoleId(assignment.role_id),
                    assignee_id=assignment.assignee_id,
                    organization_id=assignment.organization_id,
                    valid_from=assignment.valid_from,
                    valid_to=assignment.valid_to,
                )
                for assignment in orm.assignments
            ],
        )
