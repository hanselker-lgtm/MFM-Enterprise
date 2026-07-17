from mfm.domain.membership.membership_category import MembershipCategory


def test_membership_category_values_are_stable():
    assert MembershipCategory.GENERAL.value == "GENERAL"
    assert MembershipCategory.YOUTH.value == "YOUTH"
    assert MembershipCategory.SENIOR.value == "SENIOR"
    assert MembershipCategory.FAMILY.value == "FAMILY"
    assert MembershipCategory.CORPORATE.value == "CORPORATE"
