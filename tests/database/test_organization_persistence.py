from __future__ import annotations

from datetime import date
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.common.enums import ContactStatus
from mfm.database.models.base_model import BaseModel
from mfm.database.models.board_member_model import BoardMemberModel
from mfm.database.models.board_model import BoardModel
from mfm.database.models.committee_member_model import CommitteeMemberModel
from mfm.database.models.committee_model import CommitteeModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.member_model import MemberModel
from mfm.database.models.organization_model import OrganizationModel
from mfm.database.models.role_assignment_model import RoleAssignmentModel
from mfm.database.models.role_model import RoleModel
from mfm.database.models.volunteer_model import VolunteerModel
from mfm.domain.member.member_status import MemberStatus
from mfm.domain.organization.board_status import BoardStatus
from mfm.domain.organization.committee_status import CommitteeStatus
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType
from mfm.domain.organization.role_status import RoleStatus
from mfm.domain.organization.role_type import RoleType
from mfm.domain.organization.volunteer_status import VolunteerStatus


def _create_session() -> tuple[object, Session]:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def test_organization_model_create_load_update_delete() -> None:
    engine, session = _create_session()
    try:
        organization = OrganizationModel(
            organization_number="ORG-1000",
            name="MFM Org",
            organization_type=OrganizationType.ASSOCIATION,
            status=OrganizationStatus.ACTIVE,
        )
        session.add(organization)
        session.commit()

        loaded = session.get(OrganizationModel, organization.id)
        assert loaded is not None
        assert loaded.organization_number == "ORG-1000"

        loaded.name = "MFM Org Updated"
        loaded.status = OrganizationStatus.INACTIVE
        session.commit()

        loaded_again = session.get(OrganizationModel, organization.id)
        assert loaded_again is not None
        assert loaded_again.name == "MFM Org Updated"
        assert loaded_again.status is OrganizationStatus.INACTIVE

        session.delete(loaded_again)
        session.commit()

        assert session.get(OrganizationModel, organization.id) is None
    finally:
        session.close()
        engine.dispose()


def test_board_and_members_relations_and_cascade() -> None:
    engine, session = _create_session()
    try:
        organization = OrganizationModel(
            organization_number="ORG-1001",
            name="Board Org",
            organization_type=OrganizationType.ASSOCIATION,
        )
        board = BoardModel(
            organization=organization,
            name="Main Board",
            term_start=date(2026, 1, 1),
            term_end=date(2026, 12, 31),
            status=BoardStatus.ACTIVE,
        )
        board.members.append(
            BoardMemberModel(
                member_id=uuid4(),
                role="CHAIR",
                appointed_on=date(2026, 1, 1),
                is_chair=True,
            )
        )

        session.add(organization)
        session.commit()

        loaded_board = session.get(BoardModel, board.id)
        assert loaded_board is not None
        assert loaded_board.organization_id == organization.id
        assert len(loaded_board.members) == 1

        session.delete(loaded_board)
        session.commit()

        assert session.get(BoardModel, board.id) is None
        member_count = session.query(BoardMemberModel).count()
        assert member_count == 0
    finally:
        session.close()
        engine.dispose()


def test_committee_and_members_relations_and_cascade() -> None:
    engine, session = _create_session()
    try:
        organization = OrganizationModel(
            organization_number="ORG-1002",
            name="Committee Org",
            organization_type=OrganizationType.ASSOCIATION,
        )
        committee = CommitteeModel(
            organization=organization,
            name="Safety Committee",
            purpose="Safety",
            status=CommitteeStatus.ACTIVE,
        )
        committee.members.append(
            CommitteeMemberModel(
                reference_id=uuid4(),
                function_title="Lead",
                joined_at=date(2026, 1, 1),
            )
        )

        session.add(organization)
        session.commit()

        loaded_committee = session.get(CommitteeModel, committee.id)
        assert loaded_committee is not None
        assert loaded_committee.organization_id == organization.id
        assert len(loaded_committee.members) == 1

        session.delete(loaded_committee)
        session.commit()

        assert session.get(CommitteeModel, committee.id) is None
        member_count = session.query(CommitteeMemberModel).count()
        assert member_count == 0
    finally:
        session.close()
        engine.dispose()


def test_role_and_assignments_relations_and_cascade() -> None:
    engine, session = _create_session()
    try:
        organization = OrganizationModel(
            organization_number="ORG-1003",
            name="Role Org",
            organization_type=OrganizationType.ASSOCIATION,
        )
        role = RoleModel(
            organization=organization,
            role_code="ROLE-OPS",
            name="Ops",
            category=RoleType.OPERATIONAL,
            status=RoleStatus.ACTIVE,
        )
        role.assignments.append(
            RoleAssignmentModel(
                assignee_id=uuid4(),
                organization=organization,
                valid_from=date(2026, 1, 1),
            )
        )

        session.add(organization)
        session.commit()

        loaded_role = session.get(RoleModel, role.id)
        assert loaded_role is not None
        assert loaded_role.organization_id == organization.id
        assert len(loaded_role.assignments) == 1

        assignment_id = loaded_role.assignments[0].id
        session.delete(loaded_role)
        session.commit()

        assert session.get(RoleModel, role.id) is None
        assert session.get(RoleAssignmentModel, assignment_id) is None
    finally:
        session.close()
        engine.dispose()


def test_volunteer_model_create_load_update_delete() -> None:
    engine, session = _create_session()
    try:
        contact = ContactModel(
            contact_number="C-ORG-001",
            status=ContactStatus.ACTIVE,
        )
        session.add(contact)
        session.commit()

        member = MemberModel(
            contact_id=contact.id,
            member_number="M-ORG-001",
            status=MemberStatus.ACTIVE,
            join_date=date(2026, 1, 1),
        )
        volunteer = VolunteerModel(
            contact=contact,
            member=member,
            status=VolunteerStatus.ACTIVE,
            joined_at=date(2026, 1, 1),
            is_available=True,
            max_hours_per_week=6,
            preferred_days="MONDAY,WEDNESDAY",
            skills="FIRST AID,NAVIGATION",
            certificates='[{"name":"CPR","expires_at":"2027-01-01"}]',
        )

        session.add(member)
        session.add(volunteer)
        session.commit()

        loaded = session.get(VolunteerModel, volunteer.id)
        assert loaded is not None
        assert loaded.contact_id == contact.id
        assert loaded.member_id == member.id

        loaded.status = VolunteerStatus.INACTIVE
        loaded.left_at = date(2026, 12, 31)
        session.commit()

        updated = session.get(VolunteerModel, volunteer.id)
        assert updated is not None
        assert updated.status is VolunteerStatus.INACTIVE
        assert updated.left_at == date(2026, 12, 31)

        session.delete(updated)
        session.commit()

        assert session.get(VolunteerModel, volunteer.id) is None
    finally:
        session.close()
        engine.dispose()
