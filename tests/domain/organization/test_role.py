from __future__ import annotations

from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.organization.exceptions import ArchivedRoleAssignmentError
from mfm.domain.organization.exceptions import DuplicateRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleAssignmentPeriodError
from mfm.domain.organization.exceptions import InvalidRoleNameError
from mfm.domain.organization.exceptions import RoleAssignmentNotFoundError
from mfm.domain.organization.exceptions import RoleAssignmentOverlapError
from mfm.domain.organization.exceptions import RoleSerializationError
from mfm.domain.organization.role import Role
from mfm.domain.organization.role_assignment import RoleAssignment
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
        category=RoleType.BOARD,
    )

    assert isinstance(role.id, RoleId)
    assert isinstance(role.id.value, UUID)
    assert role.role_code == RoleCode("BOARD-CHAIR")
    assert role.name == "Board Chair"
    assert role.description == "Leads board meetings"
    assert role.category is RoleType.BOARD
    assert role.status is RoleStatus.ACTIVE
    assert role.assignments == []


def test_invalid_name() -> None:
    with pytest.raises(InvalidRoleNameError):
        Role(
            role_code=RoleCode("ROLE-00"),
            name="   ",
            category=RoleType.OPERATIONAL,
        )


def test_duplicate_code() -> None:
    _ = Role(
        role_code=RoleCode("ROLE-01"),
        name="Role A",
        category=RoleType.COMMITTEE,
    )

    with pytest.raises(DuplicateRoleCodeError):
        Role(
            role_code=RoleCode("role-01"),
            name="Role B",
            category=RoleType.OPERATIONAL,
        )


def test_rename() -> None:
    role = Role(
        role_code=RoleCode("ROLE-02"),
        name="Old Role Name",
        category=RoleType.VOLUNTEER,
    )

    role.rename("  New Role Name  ")

    assert role.name == "New Role Name"
def test_assign() -> None:
    role = Role(
        role_code=RoleCode("ROLE-03"),
        name="Assign Role",
        category=RoleType.OPERATIONAL,
    )

    assignment = role.assign(
        assignee_id=uuid4(),
        organization_id=uuid4(),
        valid_from=date(2026, 1, 1),
    )

    assert assignment in role.assignments
    assert assignment.valid_to is None


def test_assignment_period_may_not_overlap() -> None:
    assignee_id = uuid4()
    role = Role(
        role_code=RoleCode("ROLE-04"),
        name="Overlap Role",
        category=RoleType.COMMITTEE,
    )

    role.assign(
        assignee_id=assignee_id,
        organization_id=uuid4(),
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 3, 1),
    )

    with pytest.raises(RoleAssignmentOverlapError):
        role.assign(
            assignee_id=assignee_id,
            organization_id=uuid4(),
            valid_from=date(2026, 2, 1),
            valid_to=date(2026, 4, 1),
        )


def test_archive_role_cannot_be_assigned() -> None:
    role = Role(
        role_code=RoleCode("ROLE-05"),
        name="Archived Role",
        category=RoleType.ADMINISTRATIVE,
    )
    role.archive()

    assert role.status is RoleStatus.ARCHIVED

    with pytest.raises(ArchivedRoleAssignmentError):
        role.assign(
            assignee_id=uuid4(),
            organization_id=uuid4(),
            valid_from=date(2026, 1, 1),
        )


def test_revoke_preserves_history() -> None:
    assignee_id = uuid4()
    role = Role(
        role_code=RoleCode("ROLE-06"),
        name="History Role",
        category=RoleType.VOLUNTEER,
    )

    role.assign(
        assignee_id=assignee_id,
        organization_id=uuid4(),
        valid_from=date(2026, 1, 1),
    )

    role.revoke(assignee_id=assignee_id, revoked_on=date(2026, 2, 1))

    assert len(role.assignments) == 1
    assert role.assignments[0].valid_to == date(2026, 2, 1)


def test_revoke_not_found() -> None:
    role = Role(
        role_code=RoleCode("ROLE-07"),
        name="No Assignment",
        category=RoleType.BOARD,
    )

    with pytest.raises(RoleAssignmentNotFoundError):
        role.revoke(assignee_id=uuid4(), revoked_on=date(2026, 2, 1))


def test_revoke_invalid_period() -> None:
    assignee_id = uuid4()
    role = Role(
        role_code=RoleCode("ROLE-08"),
        name="Invalid Revoke",
        category=RoleType.COMMITTEE,
    )

    role.assign(
        assignee_id=assignee_id,
        organization_id=uuid4(),
        valid_from=date(2026, 2, 1),
    )

    with pytest.raises(InvalidRoleAssignmentPeriodError):
        role.revoke(assignee_id=assignee_id, revoked_on=date(2026, 1, 1))


def test_assignment_entity_rejects_invalid_period() -> None:
    with pytest.raises(InvalidRoleAssignmentPeriodError):
        RoleAssignment(
            role_id=RoleId.new(),
            assignee_id=uuid4(),
            organization_id=uuid4(),
            valid_from=date(2026, 2, 1),
            valid_to=date(2026, 1, 1),
        )


def test_archive() -> None:
    role = Role(
        role_code=RoleCode("ROLE-09"),
        name="Archivable",
        category=RoleType.BOARD,
    )

    role.archive()
    assert role.status is RoleStatus.ARCHIVED


def test_equality() -> None:
    role_id = RoleId.new()
    assignment = RoleAssignment(
        role_id=role_id,
        assignee_id=uuid4(),
        organization_id=uuid4(),
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 2, 1),
    )

    left = Role(
        id=role_id,
        role_code=RoleCode("ROLE-10"),
        name="Equal Role",
        description="Same",
        category=RoleType.VOLUNTEER,
        status=RoleStatus.INACTIVE,
        assignments=[assignment],
    )
    right = Role(
        id=role_id,
        role_code=RoleCode("ROLE-10"),
        name="Equal Role",
        description="Same",
        category=RoleType.VOLUNTEER,
        status=RoleStatus.INACTIVE,
        assignments=[
            RoleAssignment(
                role_id=role_id,
                assignee_id=assignment.assignee_id,
                organization_id=assignment.organization_id,
                valid_from=assignment.valid_from,
                valid_to=assignment.valid_to,
            )
        ],
    )

    assert left == right


def test_serialization_round_trip() -> None:
    role = Role(
        role_code=RoleCode("ROLE-11"),
        name="Serializable Role",
        description="Serializable",
        category=RoleType.ADMINISTRATIVE,
        status=RoleStatus.INACTIVE,
    )

    role.assign(
        assignee_id=uuid4(),
        organization_id=uuid4(),
        valid_from=date(2026, 1, 1),
        valid_to=date(2026, 3, 1),
    )

    payload = role.to_dict()
    restored = Role.from_dict(payload)

    assert restored == role
    assert restored.role_code == RoleCode("ROLE-11")

def test_serialization_rejects_invalid_data() -> None:
    with pytest.raises(RoleSerializationError):
        Role.from_dict({"name": "missing fields"})
