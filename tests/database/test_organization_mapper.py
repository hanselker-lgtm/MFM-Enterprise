from __future__ import annotations

from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import uuid4

from mfm.database.mappers.organization_mapper import OrganizationMapper
from mfm.database.models.board_model import BoardModel
from mfm.database.models.committee_model import CommitteeModel
from mfm.database.models.organization_model import OrganizationModel
from mfm.database.models.role_model import RoleModel
from mfm.database.models.volunteer_model import VolunteerModel
from mfm.domain.organization.board import Board
from mfm.domain.organization.board_member import BoardMember
from mfm.domain.organization.committee import Committee
from mfm.domain.organization.committee_member import CommitteeMember
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.organization_type import OrganizationType
from mfm.domain.organization.role import Role
from mfm.domain.organization.role_code import RoleCode
from mfm.domain.organization.role_type import RoleType
from mfm.domain.organization.volunteer import Volunteer
from mfm.domain.organization.volunteer import VolunteerCertificate
from mfm.domain.organization.volunteer_availability import VolunteerAvailability
from mfm.domain.organization.volunteer_skill import VolunteerSkill


def test_organization_mapper_roundtrip() -> None:
    organization = Organization(
        id=OrganizationId.new(),
        organization_number=OrganizationNumber("ORG-9000"),
        name="MFM Organization",
        organization_type=OrganizationType.ASSOCIATION,
        created_at=datetime(2026, 1, 1, tzinfo=UTC),
        updated_at=datetime(2026, 1, 2, tzinfo=UTC),
    )

    orm = OrganizationMapper.to_orm_organization(organization)

    assert isinstance(orm, OrganizationModel)
    assert orm.id == organization.id.value
    assert orm.organization_number == "ORG-9000"

    round_tripped = OrganizationMapper.to_domain_organization(orm)

    assert round_tripped == organization


def test_board_mapper_roundtrip() -> None:
    board = Board(
        organization_id=OrganizationId.new(),
        name="Main Board",
        term_start=date(2026, 1, 1),
        term_end=date(2026, 12, 31),
        members=[
            BoardMember(
                member_id=uuid4(),
                role="CHAIR",
                appointed_on=date(2026, 1, 1),
                is_chair=True,
            )
        ],
    )

    orm = OrganizationMapper.to_orm_board(board)

    assert isinstance(orm, BoardModel)
    assert orm.id == board.id
    assert len(orm.members) == 1

    round_tripped = OrganizationMapper.to_domain_board(orm)

    assert round_tripped.id == board.id
    assert round_tripped.organization_id == board.organization_id
    assert round_tripped.members[0].role == "CHAIR"


def test_committee_mapper_roundtrip() -> None:
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="Safety Committee",
        purpose="Safety",
        members=[
            CommitteeMember(
                reference_id=uuid4(),
                function_title="Lead",
                joined_at=date(2026, 1, 1),
            )
        ],
    )

    orm = OrganizationMapper.to_orm_committee(committee)

    assert isinstance(orm, CommitteeModel)
    assert orm.id == committee.id.value
    assert len(orm.members) == 1

    round_tripped = OrganizationMapper.to_domain_committee(orm)

    assert round_tripped.id == committee.id
    assert round_tripped.organization_id == committee.organization_id
    assert round_tripped.members[0].function_title == "Lead"


def test_volunteer_mapper_roundtrip() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        member_id=uuid4(),
        availability=VolunteerAvailability(
            is_available=True,
            max_hours_per_week=8,
            preferred_days=("MONDAY", "WEDNESDAY"),
        ),
        skills=[VolunteerSkill("FIRST AID")],
        certificates=[VolunteerCertificate(name="CPR", expires_at=date(2027, 1, 1))],
        joined_at=date(2026, 1, 1),
    )

    orm = OrganizationMapper.to_orm_volunteer(volunteer)

    assert isinstance(orm, VolunteerModel)
    assert orm.id == volunteer.id.value
    assert orm.preferred_days == "MONDAY,WEDNESDAY"

    round_tripped = OrganizationMapper.to_domain_volunteer(orm)

    assert round_tripped.id == volunteer.id
    assert round_tripped.contact_id == volunteer.contact_id
    assert round_tripped.availability.preferred_days == ("MONDAY", "WEDNESDAY")
    assert str(round_tripped.skills[0]) == "FIRST AID"
    assert round_tripped.certificates[0].name == "CPR"


def test_role_mapper_roundtrip() -> None:
    organization_id = uuid4()
    role = Role(
        role_code=RoleCode("OPS-LEAD"),
        name="Operations Lead",
        description="Coordinates operations",
        category=RoleType.OPERATIONAL,
    )
    role.assign(
        assignee_id=uuid4(),
        organization_id=organization_id,
        valid_from=date(2026, 1, 1),
    )

    orm = OrganizationMapper.to_orm_role(role, organization_id=organization_id)

    assert isinstance(orm, RoleModel)
    assert orm.id == role.id.value
    assert len(orm.assignments) == 1

    round_tripped = OrganizationMapper.to_domain_role(orm)

    assert round_tripped.id == role.id
    assert round_tripped.role_code == role.role_code
    assert round_tripped.name == role.name
    assert len(round_tripped.assignments) == 1
    assert round_tripped.assignments[0].organization_id == organization_id
