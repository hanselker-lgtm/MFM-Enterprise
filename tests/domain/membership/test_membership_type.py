from uuid import UUID

import pytest

from mfm.domain.membership.exceptions import InvalidMembershipTypeError
from mfm.domain.membership.membership_category import MembershipCategory
from mfm.domain.membership.membership_type import MembershipType


def test_membership_type_accepts_valid_values():
    membership_type = MembershipType(
        code=" standard ",
        name=" Standard ",
        category=MembershipCategory.FAMILY,
        description=" Base membership ",
    )

    assert isinstance(membership_type.id, UUID)
    assert membership_type.code == "STANDARD"
    assert membership_type.name == "Standard"
    assert membership_type.category is MembershipCategory.FAMILY
    assert membership_type.description == "Base membership"
    assert membership_type.is_active is True


def test_membership_type_rejects_invalid_category():
    with pytest.raises(InvalidMembershipTypeError):
        MembershipType(code="STANDARD", name="Standard", category="BAD")  # type: ignore[arg-type]


def test_membership_type_rejects_blank_code():
    with pytest.raises(InvalidMembershipTypeError):
        MembershipType(code="   ", name="Standard")


def test_membership_type_rejects_blank_name():
    with pytest.raises(InvalidMembershipTypeError):
        MembershipType(code="STANDARD", name="")


def test_membership_type_rename_and_activation_state():
    membership_type = MembershipType(code="TRIAL", name="Trial")

    membership_type.rename(name="Trial Plus", description="30 days")
    membership_type.deactivate()

    assert membership_type.name == "Trial Plus"
    assert membership_type.description == "30 days"
    assert membership_type.is_active is False

    membership_type.activate()
    assert membership_type.is_active is True


def test_membership_type_rename_rejects_invalid_name():
    membership_type = MembershipType(code="TRIAL", name="Trial")

    with pytest.raises(InvalidMembershipTypeError):
        membership_type.rename(name="  ")
