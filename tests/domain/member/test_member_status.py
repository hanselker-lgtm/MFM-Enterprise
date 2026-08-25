from mfm.domain.member.member_status import MemberStatus


def test_member_status_values():
    assert MemberStatus.ACTIVE.value == "ACTIVE"
    assert MemberStatus.INACTIVE.value == "INACTIVE"
    assert MemberStatus.SUSPENDED.value == "SUSPENDED"
    assert MemberStatus.TERMINATED.value == "TERMINATED"
