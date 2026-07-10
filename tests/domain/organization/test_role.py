from __future__ import annotations

from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import UUID

import pytest

from mfm.domain.organization.exceptions import DuplicateRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleIdentityMutationError
from mfm.domain.organization.exceptions import InvalidRoleNameError
from mfm.domain.organization.exceptions import InvalidRoleStatusTransitionError
from mfm.domain.organization.exceptions import RoleSerializationError
from mfm.domain.organization.role import Role
from mfm.domain.organization.role_code import RoleCode
from mfm.domain.organization.role_id import RoleId
from mfm.domain.organization.role_status import RoleStatus
from mfm.domain.organization.role_type import RoleType


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Role._clear_registry_for_tests()


def test_create_role() -> None:
    role = Role(
        role_code=RoleCode(" board-chair "),
        name="  Board Chair  ",
        description="  Leads board meetings  ",
        role_type=RoleType.BOARD,
    )

    assert isinstance(role.id, RoleId)
    assert isinstance(role.id.value, UUID)
    assert role.role_code == RoleCode("BOARD-CHAIR")
    assert role.name == "Board Chair"
    assert role.description == "Leads board meetings"
    assert role.role_type is RoleType.BOARD
    assert role.status is RoleStatus.ACTIVE
    assert role.created_at.tzinfo == UTC
    assert role.updated_at.tzinfo == UTC
    assert role.created_at <= role.updated_at


def test_invalid_name() -> None:
    with pytest.raises(InvalidRoleNameError):
        Role(
            role_code=RoleCode("ROLE-00"),
            name="   ",
            role_type=RoleType.OPERATIONAL,
        )


def test_duplicate_code() -> None:
    _ = Role(
        role_code=RoleCode("ROLE-01"),
        name="Role A",
        role_type=RoleType.COMMITTEE,
    )

    with pytest.raises(DuplicateRoleCodeError):
        Role(
            role_code=RoleCode("role-01"),
            name="Role B",
            role_type=RoleType.OPERATIONAL,
        )


def test_rename() -> None:
    role = Role(
        role_code=RoleCode("ROLE-02"),
        name="Old Role Name",
        role_type=RoleType.VOLUNTEER,
    )

    before = role.updated_at
    role.rename("  New Role Name  ")

    assert role.name == "New Role Name"
    assert role.updated_at >= before


def test_change_description() -> None:
    role = Role(
        role_code=RoleCode("ROLE-11"),
        name="Description Role",
        description="Initial",
        role_type=RoleType.ADMINISTRATIVE,
    )

    before = role.updated_at
    role.change_description("  Updated Description  ")
    assert role.description == "Updated Description"
    assert role.updated_at >= before

    role.change_description(None)
    assert role.description is None


def test_activate() -> None:
    role = Role(
        role_code=RoleCode("ROLE-03"),
        name="Activatable",
        status=RoleStatus.INACTIVE,
        role_type=RoleType.CREW,
    )

    before = role.updated_at
    role.activate()

    assert role.status is RoleStatus.ACTIVE
    assert role.updated_at >= before


def test_deactivate() -> None:
    role = Role(
        role_code=RoleCode("ROLE-04"),
        name="Deactivatable",
        status=RoleStatus.ACTIVE,
        role_type=RoleType.OPERATIONAL,
    )

    before = role.updated_at
    role.deactivate()

    assert role.status is RoleStatus.INACTIVE
    assert role.updated_at >= before


def test_archive() -> None:
    role = Role(
        role_code=RoleCode("ROLE-05"),
        name="Archivable",
        role_type=RoleType.BOARD,
    )

    before = role.updated_at
    role.archive()

    assert role.status is RoleStatus.ARCHIVED
    assert role.updated_at >= before


def test_validity_period_created_at_before_or_equal_updated_at() -> None:
    role = Role(
        role_code=RoleCode("ROLE-06"),
        name="Validity Role",
        role_type=RoleType.COMMITTEE,
        created_at=datetime(2026, 1, 2, 0, 0, tzinfo=UTC),
        updated_at=datetime(2026, 1, 1, 0, 0, tzinfo=UTC),
    )

    assert role.created_at == datetime(2026, 1, 2, 0, 0, tzinfo=UTC)
    assert role.updated_at == role.created_at


def test_invalid_transition_archived_cannot_activate() -> None:
    role = Role(
        role_code=RoleCode("ROLE-08"),
        name="Archived",
        status=RoleStatus.ARCHIVED,
        role_type=RoleType.BOARD,
    )

    with pytest.raises(InvalidRoleStatusTransitionError):
        role.activate()


def test_invalid_transition_archived_cannot_deactivate() -> None:
    role = Role(
        role_code=RoleCode("ROLE-09"),
        name="Archived 2",
        status=RoleStatus.ARCHIVED,
        role_type=RoleType.BOARD,
    )

    with pytest.raises(InvalidRoleStatusTransitionError):
        role.deactivate()


def test_invalid_transition_activate_only_from_inactive() -> None:
    role = Role(
        role_code=RoleCode("ROLE-14"),
        name="Already Active",
        status=RoleStatus.ACTIVE,
        role_type=RoleType.COMMITTEE,
    )

    with pytest.raises(InvalidRoleStatusTransitionError):
        role.activate()


def test_invalid_transition_deactivate_only_from_active() -> None:
    role = Role(
        role_code=RoleCode("ROLE-15"),
        name="Already Inactive",
        status=RoleStatus.INACTIVE,
        role_type=RoleType.COMMITTEE,
    )

    with pytest.raises(InvalidRoleStatusTransitionError):
        role.deactivate()


def test_identity_is_immutable() -> None:
    role = Role(
        role_code=RoleCode("ROLE-10"),
        name="Immutable Identity",
        role_type=RoleType.CREW,
    )

    with pytest.raises(InvalidRoleIdentityMutationError):
        role.id = RoleId.new()  # type: ignore[misc]

    with pytest.raises(InvalidRoleIdentityMutationError):
        role.role_code = RoleCode("ROLE-10B")  # type: ignore[misc]

def test_equality() -> None:
    role_id = RoleId.new()
    created_at = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
    updated_at = datetime(2026, 1, 2, 0, 0, tzinfo=UTC)

    left = Role(
        id=role_id,
        role_code=RoleCode("ROLE-12"),
        name="Equal Role",
        description="Same",
        role_type=RoleType.VOLUNTEER,
        status=RoleStatus.INACTIVE,
        created_at=created_at,
        updated_at=updated_at,
    )
    right = Role(
        id=role_id,
        role_code=RoleCode("ROLE-12"),
        name="Equal Role",
        description="Same",
        role_type=RoleType.VOLUNTEER,
        status=RoleStatus.INACTIVE,
        created_at=created_at,
        updated_at=updated_at,
    )

    assert left == right


def test_serialization_round_trip() -> None:
    role = Role(
        role_code=RoleCode("ROLE-13"),
        name="Serializable Role",
        description="Serializable",
        role_type=RoleType.ADMINISTRATIVE,
        status=RoleStatus.INACTIVE,
    )

    payload = role.to_dict()
    restored = Role.from_dict(payload)

    assert restored == role
    assert restored.role_code == RoleCode("ROLE-13")


def test_serialization_rejects_invalid_data() -> None:
    with pytest.raises(RoleSerializationError):
        Role.from_dict({"name": "missing fields"})
