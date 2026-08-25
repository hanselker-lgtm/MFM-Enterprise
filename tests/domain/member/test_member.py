from datetime import date
from uuid import uuid4

import pytest

from mfm.domain.contact.contact import Contact
from mfm.domain.member.exceptions import (
    InvalidMemberNumberError,
    InvalidMemberReferenceError,
    InvalidMembershipDatesError,
)
from mfm.domain.member.member import Member
from mfm.domain.member.member_status import MemberStatus


def test_member_defaults_and_fields():
    contact_id = uuid4()

    member = Member(
        contact_id=contact_id,
        member_number="M-0001",
    )

    assert member.contact_id == contact_id
    assert member.member_number == "M-0001"
    assert member.status == MemberStatus.ACTIVE
    assert isinstance(member.id, type(uuid4()))
    assert member.leave_date is None


def test_member_strips_member_number():
    member = Member(
        contact_id=uuid4(),
        member_number="  M-0002  ",
    )

    assert member.member_number == "M-0002"


def test_member_rejects_empty_member_number():
    with pytest.raises(InvalidMemberNumberError):
        Member(
            contact_id=uuid4(),
            member_number="   ",
        )


def test_member_rejects_invalid_contact_reference():
    with pytest.raises(InvalidMemberReferenceError):
        Member(
            contact_id="not-a-uuid",  # type: ignore[arg-type]
            member_number="M-0003",
        )


def test_member_rejects_leave_date_before_join_date():
    with pytest.raises(InvalidMembershipDatesError):
        Member(
            contact_id=uuid4(),
            member_number="M-0004",
            join_date=date(2026, 1, 10),
            leave_date=date(2026, 1, 9),
        )


def test_member_allows_leave_date_after_join_date():
    member = Member(
        contact_id=uuid4(),
        member_number="M-0005",
        join_date=date(2026, 1, 10),
        leave_date=date(2026, 2, 1),
        status=MemberStatus.INACTIVE,
    )

    assert member.join_date == date(2026, 1, 10)
    assert member.leave_date == date(2026, 2, 1)
    assert member.status == MemberStatus.INACTIVE


def test_member_is_not_contact_inheritance():
    member = Member(
        contact_id=uuid4(),
        member_number="M-0006",
    )

    assert not isinstance(member, Contact)
