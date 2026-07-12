from datetime import date
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.common.enums import ContactStatus
from mfm.database.models.base_model import BaseModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.repositories.sqlite_member_repository import SQLiteMemberRepository
from mfm.domain.member.member import Member
from mfm.domain.member.member_status import MemberStatus


def _create_session():
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def _create_contact(session: Session, contact_number: str = "C-900001") -> ContactModel:
    contact = ContactModel(
        id=uuid4(),
        contact_number=contact_number,
        status=ContactStatus.ACTIVE,
    )
    session.add(contact)
    session.flush()
    return contact


def test_member_repository_persists_and_reads_member():
    engine, session = _create_session()
    try:
        contact = _create_contact(session)
        repository = SQLiteMemberRepository(session)

        member = Member(
            contact_id=contact.id,
            member_number="M-200001",
            status=MemberStatus.ACTIVE,
            join_date=date(2026, 1, 1),
        )

        repository.add(member)
        session.commit()

        stored = repository.get(member.id)
        assert stored is not None
        assert stored.member_number == "M-200001"
        assert stored.contact_id == contact.id

        by_number = repository.get_by_number("M-200001")
        assert by_number is not None
        assert by_number.id == member.id
    finally:
        session.close()
        engine.dispose()


def test_member_repository_supports_list_exists_delete_and_contact_exists():
    engine, session = _create_session()
    try:
        contact = _create_contact(session, contact_number="C-900002")
        repository = SQLiteMemberRepository(session)

        member = Member(contact_id=contact.id, member_number="M-200002")
        repository.add(member)
        session.commit()

        assert repository.exists(member.id) is True
        assert repository.contact_exists(contact.id) is True
        assert len(repository.list()) == 1

        repository.delete(member.id)
        session.commit()

        assert repository.exists(member.id) is False
        assert repository.get(member.id) is None
    finally:
        session.close()
        engine.dispose()


def test_member_repository_rejects_duplicate_member_number():
    engine, session = _create_session()
    try:
        contact1 = _create_contact(session, contact_number="C-900003")
        contact2 = _create_contact(session, contact_number="C-900004")
        repository = SQLiteMemberRepository(session)

        first = Member(contact_id=contact1.id, member_number="M-200003")
        second = Member(contact_id=contact2.id, member_number="M-200003")

        repository.add(first)
        session.commit()

        with pytest.raises(ValueError):
            repository.add(second)
    finally:
        session.close()
        engine.dispose()


def test_member_repository_updates_member_status_and_leave_date():
    engine, session = _create_session()
    try:
        contact = _create_contact(session, contact_number="C-900005")
        repository = SQLiteMemberRepository(session)

        member = Member(
            contact_id=contact.id,
            member_number="M-200004",
            status=MemberStatus.ACTIVE,
            join_date=date(2026, 1, 1),
        )
        repository.add(member)
        session.commit()

        member.status = MemberStatus.TERMINATED
        member.leave_date = date(2026, 3, 1)

        repository.update(member)
        session.commit()

        stored = repository.get(member.id)
        assert stored is not None
        assert stored.status == MemberStatus.TERMINATED
        assert stored.leave_date == date(2026, 3, 1)
    finally:
        session.close()
        engine.dispose()
