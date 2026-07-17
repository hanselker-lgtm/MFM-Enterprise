from __future__ import annotations

from datetime import date
from uuid import uuid4

import pytest

from mfm.domain.organization_roles.assignment import Assignment
from mfm.domain.organization_roles.board import Board
from mfm.domain.organization_roles.committee import Committee
from mfm.domain.organization_roles.election_period import ElectionPeriod
from mfm.domain.organization_roles.organization_roles_foundation import (
    OrganizationRolesFoundation,
)
from mfm.domain.organization_roles.permission import Permission
from mfm.domain.organization_roles.responsibility import Responsibility
from mfm.domain.organization_roles.role import Role


def test_foundation_supports_role_assignment_committee_board_and_election_period() -> None:
    organization_id = uuid4()
    foundation = OrganizationRolesFoundation(organization_id=organization_id)

    election_period = ElectionPeriod(
        name="General Election 2026",
        starts_on=date(2026, 1, 1),
        ends_on=date(2026, 12, 31),
    )
    foundation.add_election_period(election_period)

    role = Role(
        name="Board Chair",
        permissions=(Permission.ASSIGN_ROLES, Permission.VIEW_REPORTS),
        responsibilities=(
            Responsibility(
                title="Leadership",
                description="Lead governance and board execution.",
            ),
        ),
    )
    foundation.add_role(role)

    foundation.assign_role(
        Assignment(
            role_id=role.id,
            assignee_id=organization_id,
            starts_on=date(2026, 1, 1),
        )
    )

    foundation.add_committee(
        Committee(
            name="Governance Committee",
            mandate="Oversee governance quality and compliance.",
            role_ids=(role.id,),
        )
    )

    foundation.set_board(
        Board(
            name="Main Board",
            role_ids=(role.id,),
            election_period_id=election_period.id,
        )
    )

    assert len(foundation.roles) == 1
    assert len(foundation.assignments) == 1
    assert len(foundation.committees) == 1
    assert foundation.board is not None
    assert len(foundation.election_periods) == 1


def test_foundation_rejects_duplicate_role_names() -> None:
    foundation = OrganizationRolesFoundation(organization_id=uuid4())
    foundation.add_role(Role(name="Secretary"))

    with pytest.raises(ValueError, match="already exists"):
        foundation.add_role(Role(name="secretary"))


def test_foundation_rejects_overlapping_assignment_for_same_assignee() -> None:
    organization_id = uuid4()
    foundation = OrganizationRolesFoundation(organization_id=organization_id)
    role = Role(name="Operations")
    foundation.add_role(role)

    foundation.assign_role(
        Assignment(
            role_id=role.id,
            assignee_id=organization_id,
            starts_on=date(2026, 1, 1),
            ends_on=date(2026, 6, 1),
        )
    )

    with pytest.raises(ValueError, match="overlapping assignment"):
        foundation.assign_role(
            Assignment(
                role_id=role.id,
                assignee_id=organization_id,
                starts_on=date(2026, 4, 1),
                ends_on=date(2026, 10, 1),
            )
        )
