from __future__ import annotations

from datetime import date
from uuid import UUID

import pytest

from mfm.domain.organization.exceptions import DuplicateRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleIdentityMutationError
from mfm.domain.organization.exceptions import InvalidRoleNameError
from mfm.domain.organization.exceptions import InvalidRoleStatusTransitionError
from mfm.domain.organization.exceptions import InvalidRoleValidityPeriodError
from mfm.domain.organization.exceptions import RoleSerializationError
from mfm.domain.organization.role import Role
from mfm.domain.organization.role_id import RoleCode
from mfm.domain.organization.role_id import RoleId
from mfm.domain.organization.role_status import RoleStatus


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Role._clear_registry_for_tests()


def test_create_role() -> None:
    role = Role(
        role_code=RoleCode(" board-chair "),
        name="  Board Chair  ",
        description="  Leads board meetings  ",
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 12, 31),
    )

    assert isinstance(role.id, RoleId)
    assert isinstance(role.id.value, UUID)
    assert role.role_code == RoleCode("BOARD-CHAIR")
    assert role.name == "Board Chair"
    assert role.description == "Leads board meetings"
    assert role.status is RoleStatus.ACTIVE
    assert role.valid_from == date(2026, 1, 1)
    assert role.valid_to == date(2026, 12, 31)


def test_duplicate_code() -> None:
    _ = Role(
        role_code=RoleCode("ROLE-01"),
        name="Role A",
        valid_from=date(2026, 1, 1),
    )

    with pytest.raises(DuplicateRoleCodeError):
        Role(
            role_code=RoleCode("role-01"),
            name="Role B",
            valid_from=date(2026, 1, 1),
        )


def test_rename() -> None:
    role = Role(
        role_code=RoleCode("ROLE-02"),
        name="Old Role Name",
        valid_from=date(2026, 1, 1),
    )

    role.rename("  New Role Name  ")

    assert role.name == "New Role Name"


def test_activate() -> None:
    role = Role(
        role_code=RoleCode("ROLE-03"),
        name="Activatable",
        status=RoleStatus.INACTIVE,
        valid_from=date(2026, 1, 1),
    )

    role.activate()

    assert role.status is RoleStatus.ACTIVE


def test_deactivate() -> None:
    role = Role(
        role_code=RoleCode("ROLE-04"),
        name="Deactivatable",
        status=RoleStatus.ACTIVE,
        valid_from=date(2026, 1, 1),
    )

    role.deactivate()

    assert role.status is RoleStatus.INACTIVE


def test_archive() -> None:
    role = Role(
        role_code=RoleCode("ROLE-05"),
        name="Archivable",
        valid_from=date(2026, 1, 1),
    )

    role.archive()

    assert role.status is RoleStatus.ARCHIVED


def test_validity_period() -> None:
    with pytest.raises(InvalidRoleValidityPeriodError):
        Role(
            role_code=RoleCode("ROLE-06"),
            name="Invalid Period",
            valid_from=date(2026, 2, 1),
            valid_to=date(2026, 1, 31),
        )


def test_invalid_name() -> None:
    with pytest.raises(InvalidRoleNameError):
        Role(
            role_code=RoleCode("ROLE-07"),
            name="   ",
            valid_from=date(2026, 1, 1),
        )


def test_invalid_transition_archived_cannot_activate() -> None:
    role = Role(
        role_code=RoleCode("ROLE-08"),
        name="Archived",
        status=RoleStatus.ARCHIVED,
        valid_from=date(2026, 1, 1),
    )

    with pytest.raises(InvalidRoleStatusTransitionError):
        role.activate()


def test_invalid_transition_archived_cannot_deactivate() -> None:
    role = Role(
        role_code=RoleCode("ROLE-09"),
        name="Archived 2",
        status=RoleStatus.ARCHIVED,
        valid_from=date(2026, 1, 1),
    )

    with pytest.raises(InvalidRoleStatusTransitionError):
        role.deactivate()


def test_identity_is_immutable() -> None:
    role = Role(
        role_code=RoleCode("ROLE-10"),
        name="Immutable Identity",
        valid_from=date(2026, 1, 1),
    )

    with pytest.raises(InvalidRoleIdentityMutationError):
        role.id = RoleId.new()  # type: ignore[misc]

    with pytest.raises(InvalidRoleIdentityMutationError):
        role.role_code = RoleCode("ROLE-10B")  # type: ignore[misc]


def test_change_description() -> None:
    role = Role(
        role_code=RoleCode("ROLE-11"),
        name="Description Role",
        description="Initial",
        valid_from=date(2026, 1, 1),
    )

    role.change_description("  Updated Description  ")
    assert role.description == "Updated Description"

    role.change_description(None)
    assert role.description is None


def test_equality() -> None:
    role_id = RoleId.new()

    left = Role(
        id=role_id,
        role_code=RoleCode("ROLE-12"),
        name="Equal Role",
        description="Same",
        status=RoleStatus.INACTIVE,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 12, 31),
    )
    right = Role(
        id=role_id,
        role_code=RoleCode("ROLE-12"),
        name="Equal Role",
        description="Same",
        status=RoleStatus.INACTIVE,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 12, 31),
    )

    assert left == right


def test_serialization_round_trip() -> None:
    role = Role(
        role_code=RoleCode("ROLE-13"),
        name="Serializable Role",
        description="Serializable",
        status=RoleStatus.INACTIVE,
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 12, 31),
    )

    payload = role.to_dict()
    restored = Role.from_dict(payload)

    assert restored == role
    assert restored.role_code == RoleCode("ROLE-13")


def test_serialization_rejects_invalid_data() -> None:
    with pytest.raises(RoleSerializationError):
        Role.from_dict({"name": "missing fields"})
