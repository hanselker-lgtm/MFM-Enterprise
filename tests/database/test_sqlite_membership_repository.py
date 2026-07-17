from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.common.enums import ContactStatus
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.repositories.sqlite_member_repository import SQLiteMemberRepository
from mfm.database.repositories.sqlite_membership_repository import SQLiteMembershipRepository
from mfm.database.repositories.sqlite_membership_type_repository import SQLiteMembershipTypeRepository
from mfm.domain.member.member import Member
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_category import MembershipCategory
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.domain.membership.membership_type import MembershipType


def _create_session():
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def _create_contact(session: Session, contact_number: str) -> UUID:
    contact = ContactModel(
        id=uuid4(),
        contact_number=contact_number,
        status=ContactStatus.ACTIVE,
    )
    session.add(contact)
    session.flush()
    return contact.id


def _seed_member_and_type(session: Session) -> tuple[Member, MembershipType]:
    member_repository = SQLiteMemberRepository(session)
    membership_type_repository = SQLiteMembershipTypeRepository(session)

    contact_id = _create_contact(session, "C-990001")
    member = Member(contact_id=contact_id, member_number="M-990001")
    membership_type = MembershipType(
        code="STANDARD",
        name="Standard",
        category=MembershipCategory.GENERAL,
    )

    member_repository.add(member)
    membership_type_repository.add(membership_type)
    session.flush()
    return member, membership_type


def test_membership_repository_persists_and_reads_membership():
    engine, session = _create_session()
    try:
        member, membership_type = _seed_member_and_type(session)
        repository = SQLiteMembershipRepository(session)

        membership = Membership(
            member_id=member.id,
            membership_type=membership_type,
            start_date=date(2026, 1, 1),
        )

        repository.add(membership)
        session.commit()

        stored = repository.get(membership.id)
        assert stored is not None
        assert stored.member_id == member.id
        assert stored.membership_type_id == membership_type.id
        assert stored.status is MembershipStatus.ACTIVE
    finally:
        session.close()
        engine.dispose()


def test_membership_repository_supports_list_by_member_and_delete():
    engine, session = _create_session()
    try:
        member, membership_type = _seed_member_and_type(session)
        repository = SQLiteMembershipRepository(session)

        membership = Membership(member_id=member.id, membership_type=membership_type)
        repository.add(membership)
        session.commit()

        listed = repository.list_by_member(member.id)
        assert len(listed) == 1
        assert listed[0].id == membership.id
        assert repository.exists(membership.id) is True

        repository.delete(membership.id)
        session.commit()

        assert repository.get(membership.id) is None
        assert repository.exists(membership.id) is False
    finally:
        session.close()
        engine.dispose()


def test_membership_repository_rejects_second_active_membership_for_same_member():
    engine, session = _create_session()
    try:
        member, membership_type = _seed_member_and_type(session)
        repository = SQLiteMembershipRepository(session)

        first = Membership(member_id=member.id, membership_type=membership_type)
        second = Membership(member_id=member.id, membership_type=membership_type)

        repository.add(first)
        session.commit()

        with pytest.raises(ValueError):
            repository.add(second)
    finally:
        session.close()
        engine.dispose()


def test_membership_repository_allows_new_active_after_previous_is_ended():
    engine, session = _create_session()
    try:
        member, membership_type = _seed_member_and_type(session)
        repository = SQLiteMembershipRepository(session)

        ended = Membership(
            member_id=member.id,
            membership_type=membership_type,
            start_date=date(2026, 1, 1),
        )
        ended.end(date(2026, 2, 1))
        repository.add(ended)
        session.commit()

        active = Membership(
            member_id=member.id,
            membership_type=membership_type,
            start_date=date(2026, 2, 2),
        )
        repository.add(active)
        session.commit()

        active_memberships = repository.list_active()
        assert len(active_memberships) == 1
        assert active_memberships[0].id == active.id
    finally:
        session.close()
        engine.dispose()
