from mfm.domain.membership.membership_status import MembershipStatus


def test_membership_status_values():
    assert MembershipStatus.ACTIVE.value == "ACTIVE"
    assert MembershipStatus.SUSPENDED.value == "SUSPENDED"
    assert MembershipStatus.ENDED.value == "ENDED"
    assert MembershipStatus.EXPIRED.value == "EXPIRED"
