from __future__ import annotations

from datetime import UTC
from datetime import date
from datetime import datetime
import weakref
from uuid import UUID
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.common.enums import ContactStatus
from mfm.database.models.base_model import BaseModel
from mfm.database.models.board_member_model import BoardMemberModel
from mfm.database.models.committee_member_model import CommitteeMemberModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.member_model import MemberModel
from mfm.database.models.role_assignment_model import RoleAssignmentModel
from mfm.domain.member.member_status import MemberStatus
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
from mfm.infrastructure.persistence.sqlite.sqlite_board_repository import (
    SQLiteBoardRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_committee_repository import (
    SQLiteCommitteeRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_organization_repository import (
    SQLiteOrganizationRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_role_repository import (
    SQLiteRoleRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_volunteer_repository import (
    SQLiteVolunteerRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


def _create_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return engine, session


def _create_uow(session: Session) -> UnitOfWork:
    return UnitOfWork(session)


def _create_contact_and_member(session: Session) -> tuple[UUID, UUID]:
    contact = ContactModel(
        contact_number=f"C-{uuid4().hex[:6].upper()}",
        status=ContactStatus.ACTIVE,
    )
    session.add(contact)
    session.flush()

    member = MemberModel(
        contact_id=contact.id,
        member_number=f"M-{uuid4().hex[:6].upper()}",
        status=MemberStatus.ACTIVE,
        join_date=date(2026, 1, 1),
    )
    session.add(member)
    session.flush()
    return contact.id, member.id


def _create_organization(repo: SQLiteOrganizationRepository) -> Organization:
    organization = Organization(
        id=OrganizationId.new(),
        organization_number=OrganizationNumber(f"ORG-{uuid4().hex[:6].upper()}"),
        name="Maritime Federation",
        organization_type=OrganizationType.ASSOCIATION,
        created_at=datetime(2026, 1, 1, tzinfo=UTC),
        updated_at=datetime(2026, 1, 1, tzinfo=UTC),
    )
    repo.add(organization)
    return organization


def test_organization_repository_crud_list_search_and_mapper_roundtrip() -> None:
    _, session = _create_session()
    uow = _create_uow(session)
    repo = SQLiteOrganizationRepository(uow)

    organization = _create_organization(repo)
    uow.commit()

    loaded = repo.get_by_id(organization.id.value)
    assert loaded is not None
    assert isinstance(loaded, Organization)
    assert loaded == organization

    organization.rename("Maritime Federation Updated")
    repo.update(organization)
    uow.commit()

    updated = repo.get_by_id(organization.id.value)
    assert updated is not None
    assert updated.name == "Maritime Federation Updated"

    assert repo.exists(organization.id.value) is True
    assert any(item.id == organization.id for item in repo.list())

    search_hits = repo.search("Maritime")
    assert any(item.id == organization.id for item in search_hits)

    repo.delete(organization.id.value)
    uow.commit()

    assert repo.get_by_id(organization.id.value) is None
    assert repo.exists(organization.id.value) is False


def test_board_repository_crud_list_search_mapper_and_cascade_relations() -> None:
    _, session = _create_session()
    uow = _create_uow(session)
    org_repo = SQLiteOrganizationRepository(uow)
    board_repo = SQLiteBoardRepository(uow)

    organization = _create_organization(org_repo)

    board = Board(
        organization_id=organization.id,
        name="National Board",
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

    board_repo.add(board)
    uow.commit()

    loaded = board_repo.get_by_id(board.id)
    assert loaded is not None
    assert isinstance(loaded, Board)
    assert loaded.id == board.id
    assert len(loaded.members) == 1

    board.name = "Updated Board"
    board_repo.update(board)
    uow.commit()

    updated = board_repo.get_by_id(board.id)
    assert updated is not None
    assert updated.name == "Updated Board"

    assert board_repo.exists(board.id) is True
    assert any(item.id == board.id for item in board_repo.list())
    assert any(item.id == board.id for item in board_repo.search("Updated"))

    board_repo.delete(board.id)
    uow.commit()

    assert board_repo.get_by_id(board.id) is None
    assert board_repo.exists(board.id) is False
    assert session.query(BoardMemberModel).count() == 0


def test_committee_repository_crud_list_search_mapper_and_cascade_relations() -> None:
    _, session = _create_session()
    uow = _create_uow(session)
    org_repo = SQLiteOrganizationRepository(uow)
    committee_repo = SQLiteCommitteeRepository(uow)

    organization = _create_organization(org_repo)

    committee = Committee(
        organization_id=organization.id,
        name="Safety Committee",
        purpose="Handle safety procedures",
        members=[
            CommitteeMember(
                reference_id=uuid4(),
                function_title="Coordinator",
                joined_at=date(2026, 1, 1),
            )
        ],
    )

    committee_repo.add(committee)
    uow.commit()

    loaded = committee_repo.get_by_id(committee.id.value)
    assert loaded is not None
    assert isinstance(loaded, Committee)
    assert loaded.id == committee.id
    assert len(loaded.members) == 1

    committee.rename("Safety and Training Committee")
    committee_repo.update(committee)
    uow.commit()

    updated = committee_repo.get_by_id(committee.id.value)
    assert updated is not None
    assert updated.name == "Safety and Training Committee"

    assert committee_repo.exists(committee.id.value) is True
    assert any(item.id == committee.id for item in committee_repo.list())
    assert any(item.id == committee.id for item in committee_repo.search("Training"))

    committee_repo.delete(committee.id.value)
    uow.commit()

    assert committee_repo.get_by_id(committee.id.value) is None
    assert committee_repo.exists(committee.id.value) is False
    assert session.query(CommitteeMemberModel).count() == 0


def test_volunteer_repository_crud_list_search_and_mapper_roundtrip() -> None:
    _, session = _create_session()
    uow = _create_uow(session)
    volunteer_repo = SQLiteVolunteerRepository(uow)

    contact_id, member_id = _create_contact_and_member(session)

    volunteer = Volunteer(
        contact_id=contact_id,
        member_id=member_id,
        availability=VolunteerAvailability(
            is_available=True,
            max_hours_per_week=8,
            preferred_days=("MONDAY", "THURSDAY"),
        ),
        skills=[VolunteerSkill("FIRST AID")],
        certificates=[VolunteerCertificate(name="CPR", expires_at=date(2027, 1, 1))],
        joined_at=date(2026, 1, 1),
    )

    volunteer_repo.add(volunteer)
    uow.commit()

    loaded = volunteer_repo.get_by_id(volunteer.id.value)
    assert loaded is not None
    assert isinstance(loaded, Volunteer)
    assert loaded.id == volunteer.id
    assert loaded.availability.preferred_days == ("MONDAY", "THURSDAY")

    volunteer.deactivate(on_date=date(2026, 2, 1))
    volunteer_repo.update(volunteer)
    uow.commit()

    updated = volunteer_repo.get_by_id(volunteer.id.value)
    assert updated is not None
    assert updated.left_at == date(2026, 2, 1)

    assert volunteer_repo.exists(volunteer.id.value) is True
    assert any(item.id == volunteer.id for item in volunteer_repo.list())
    assert any(item.id == volunteer.id for item in volunteer_repo.search("FIRST AID"))

    volunteer_repo.delete(volunteer.id.value)
    uow.commit()

    assert volunteer_repo.get_by_id(volunteer.id.value) is None
    assert volunteer_repo.exists(volunteer.id.value) is False


def test_role_repository_crud_list_search_mapper_and_cascade_relations() -> None:
    _, session = _create_session()
    uow = _create_uow(session)
    org_repo = SQLiteOrganizationRepository(uow)
    role_repo = SQLiteRoleRepository(uow)

    organization = _create_organization(org_repo)

    role = Role(
        role_code=RoleCode(f"OPS-{uuid4().hex[:5].upper()}"),
        name="Operations Lead",
        description="Coordinates operations",
        category=RoleType.OPERATIONAL,
    )
    role.assign(
        assignee_id=uuid4(),
        organization_id=organization.id.value,
        valid_from=date(2026, 1, 1),
    )

    role_repo.add(role)
    uow.commit()

    loaded = role_repo.get_by_id(role.id.value)
    assert loaded is not None
    assert isinstance(loaded, Role)
    assert loaded.id == role.id
    assert len(loaded.assignments) == 1

    role.rename("Operations Director")
    role_repo.update(role)
    uow.commit()

    updated = role_repo.get_by_id(role.id.value)
    assert updated is not None
    assert updated.name == "Operations Director"

    assert role_repo.exists(role.id.value) is True
    assert any(item.id == role.id for item in role_repo.list())
    assert any(item.id == role.id for item in role_repo.search("Director"))

    role_repo.delete(role.id.value)
    uow.commit()

    assert role_repo.get_by_id(role.id.value) is None
    assert role_repo.exists(role.id.value) is False
    assert session.query(RoleAssignmentModel).count() == 0
