from datetime import date
from uuid import uuid4

import pytest

from mfm.domain.member.exceptions import (
    InvalidMemberStatusTransitionError,
    InvalidMembershipDatesError,
)
from mfm.domain.member.member import Member
from mfm.domain.member.member_status import MemberStatus


def test_member_can_activate_from_inactive():
    member = Member(
        contact_id=uuid4(),
        member_number="M-400001",
        status=MemberStatus.INACTIVE,
        join_date=date(2026, 1, 1),
        leave_date=date(2026, 2, 1),
    )

    member.activate()

    assert member.status == MemberStatus.ACTIVE
    assert member.leave_date is None


def test_member_can_deactivate_from_active():
    member = Member(
        contact_id=uuid4(),
        member_number="M-400002",
        status=MemberStatus.ACTIVE,
    )

    member.deactivate()

    assert member.status == MemberStatus.INACTIVE


def test_member_can_resign_and_sets_leave_date():
    member = Member(
        contact_id=uuid4(),
        member_number="M-400003",
        status=MemberStatus.ACTIVE,
        join_date=date(2026, 1, 1),
    )

    member.resign(date(2026, 3, 1))

    assert member.status == MemberStatus.TERMINATED
    assert member.leave_date == date(2026, 3, 1)


def test_member_rejects_invalid_activate_transition():
    member = Member(
        contact_id=uuid4(),
        member_number="M-400004",
        status=MemberStatus.TERMINATED,
    )

    with pytest.raises(InvalidMemberStatusTransitionError):
        member.activate()


def test_member_rejects_invalid_deactivate_transition():
    member = Member(
        contact_id=uuid4(),
        member_number="M-400005",
        status=MemberStatus.INACTIVE,
    )

    with pytest.raises(InvalidMemberStatusTransitionError):
        member.deactivate()


def test_member_rejects_resign_before_join_date():
    member = Member(
        contact_id=uuid4(),
        member_number="M-400006",
        status=MemberStatus.ACTIVE,
        join_date=date(2026, 1, 10),
    )

    with pytest.raises(InvalidMembershipDatesError):
        member.resign(date(2026, 1, 9))
