from datetime import date
from uuid import uuid4

import pytest

from mfm.domain.membership.exceptions import (
    InvalidMembershipDatesError,
    InvalidMembershipReferenceError,
    InvalidMembershipStatusTransitionError,
    MultipleActiveMembershipsError,
)
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.domain.membership.membership_type import MembershipType


def _type_standard() -> MembershipType:
    return MembershipType(code="STANDARD", name="Standard")


def test_membership_defaults_and_fields():
    member_id = uuid4()
    membership_type = _type_standard()

    membership = Membership(
        member_id=member_id,
        membership_type=membership_type,
    )

    assert membership.member_id == member_id
    assert membership.membership_type == membership_type
    assert membership.membership_type_id == membership_type.id
    assert membership.status == MembershipStatus.ACTIVE
    assert membership.end_date is None


def test_membership_rejects_invalid_member_reference():
    with pytest.raises(InvalidMembershipReferenceError):
        Membership(
            member_id="not-a-uuid",  # type: ignore[arg-type]
            membership_type=_type_standard(),
        )


def test_membership_rejects_invalid_membership_type_reference():
    with pytest.raises(InvalidMembershipReferenceError):
        Membership(
            member_id=uuid4(),
            membership_type="not-a-membership-type",  # type: ignore[arg-type]
        )


def test_membership_rejects_end_date_before_start_date():
    with pytest.raises(InvalidMembershipDatesError):
        Membership(
            member_id=uuid4(),
            membership_type=_type_standard(),
            start_date=date(2026, 1, 10),
            end_date=date(2026, 1, 9),
            status=MembershipStatus.EXPIRED,
        )


def test_membership_can_be_suspended_from_active():
    membership = Membership(member_id=uuid4(), membership_type=_type_standard())

    membership.suspend()

    assert membership.status == MembershipStatus.SUSPENDED


def test_membership_can_be_reactivated_from_suspended():
    membership = Membership(member_id=uuid4(), membership_type=_type_standard())
    membership.suspend()

    membership.reactivate()

    assert membership.status == MembershipStatus.ACTIVE
    assert membership.end_date is None


def test_membership_can_be_ended():
    membership = Membership(
        member_id=uuid4(),
        membership_type=_type_standard(),
        start_date=date(2026, 1, 1),
    )

    membership.end(date(2026, 3, 1))

    assert membership.status == MembershipStatus.ENDED
    assert membership.end_date == date(2026, 3, 1)


def test_membership_expire_alias_ends_membership():
    membership = Membership(
        member_id=uuid4(),
        membership_type=_type_standard(),
        start_date=date(2026, 1, 1),
    )

    membership.expire(date(2026, 2, 1))

    assert membership.status == MembershipStatus.ENDED
    assert membership.end_date == date(2026, 2, 1)


def test_membership_rejects_invalid_suspend_transition():
    membership = Membership(
        member_id=uuid4(),
        membership_type=_type_standard(),
        status=MembershipStatus.SUSPENDED,
    )

    with pytest.raises(InvalidMembershipStatusTransitionError):
        membership.suspend()


def test_membership_rejects_invalid_reactivate_transition():
    membership = Membership(
        member_id=uuid4(),
        membership_type=_type_standard(),
        status=MembershipStatus.ACTIVE,
    )

    with pytest.raises(InvalidMembershipStatusTransitionError):
        membership.reactivate()


def test_membership_rejects_invalid_end_transition():
    membership = Membership(
        member_id=uuid4(),
        membership_type=_type_standard(),
        status=MembershipStatus.ENDED,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 2, 1),
    )

    with pytest.raises(InvalidMembershipStatusTransitionError):
        membership.end(date(2026, 3, 1))


def test_membership_can_be_reactivated_after_end():
    membership = Membership(
        member_id=uuid4(),
        membership_type=_type_standard(),
        start_date=date(2026, 1, 1),
    )
    membership.end(date(2026, 2, 1))

    membership.reactivate()

    assert membership.status == MembershipStatus.ACTIVE
    assert membership.end_date is None


def test_member_can_have_multiple_historical_memberships_but_only_one_active():
    member_id = uuid4()
    membership_type = _type_standard()

    historical = Membership(
        member_id=member_id,
        membership_type=membership_type,
        status=MembershipStatus.ENDED,
        start_date=date(2025, 1, 1),
        end_date=date(2025, 12, 31),
    )
    active = Membership(
        member_id=member_id,
        membership_type=membership_type,
        status=MembershipStatus.ACTIVE,
        start_date=date(2026, 1, 1),
    )

    Membership.ensure_single_active([historical, active], member_id)


def test_member_rejects_more_than_one_active_membership():
    member_id = uuid4()
    membership_type = _type_standard()

    first_active = Membership(
        member_id=member_id,
        membership_type=membership_type,
        status=MembershipStatus.ACTIVE,
    )
    second_active = Membership(
        member_id=member_id,
        membership_type=membership_type,
        status=MembershipStatus.ACTIVE,
    )

    with pytest.raises(MultipleActiveMembershipsError):
        Membership.ensure_single_active([first_active, second_active], member_id)
