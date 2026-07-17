"""Aggregate root for Organization & Roles capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID

from mfm.domain.organization_roles.assignment import Assignment
from mfm.domain.organization_roles.board import Board
from mfm.domain.organization_roles.committee import Committee
from mfm.domain.organization_roles.election_period import ElectionPeriod
from mfm.domain.organization_roles.role import Role


@dataclass(slots=True)
class OrganizationRolesFoundation:
    """Aggregate root for organization role governance foundation."""

    organization_id: UUID
    roles: list[Role] = field(default_factory=list)
    assignments: list[Assignment] = field(default_factory=list)
    committees: list[Committee] = field(default_factory=list)
    election_periods: list[ElectionPeriod] = field(default_factory=list)
    board: Board | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.organization_id, UUID):
            raise ValueError("organization_id must be UUID")
        self.roles = list(self.roles)
        self.assignments = list(self.assignments)
        self.committees = list(self.committees)
        self.election_periods = list(self.election_periods)

    def add_role(self, role: Role) -> None:
        if any(item.name.casefold() == role.name.casefold() for item in self.roles):
            raise ValueError(f"Role {role.name} already exists")
        self.roles.append(role)

    def assign_role(self, assignment: Assignment) -> None:
        if not self.role_exists(assignment.role_id):
            raise ValueError(f"Role {assignment.role_id} does not exist")

        overlapping = [
            item
            for item in self.assignments
            if item.assignee_id == assignment.assignee_id and item.overlaps(assignment)
        ]
        if overlapping:
            raise ValueError(
                f"Assignee {assignment.assignee_id} already has overlapping assignment"
            )

        self.assignments.append(assignment)

    def add_committee(self, committee: Committee) -> None:
        if any(item.name.casefold() == committee.name.casefold() for item in self.committees):
            raise ValueError(f"Committee {committee.name} already exists")
        self._ensure_roles_exist(committee.role_ids)
        self.committees.append(committee)

    def set_board(self, board: Board) -> None:
        self._ensure_roles_exist(board.role_ids)
        if board.election_period_id is not None and not self.election_period_exists(
            board.election_period_id
        ):
            raise ValueError(
                f"Election period {board.election_period_id} does not exist"
            )
        self.board = board

    def add_election_period(self, election_period: ElectionPeriod) -> None:
        if any(
            item.name.casefold() == election_period.name.casefold()
            for item in self.election_periods
        ):
            raise ValueError(f"Election period {election_period.name} already exists")
        self.election_periods.append(election_period)

    def role_exists(self, role_id: UUID) -> bool:
        return any(item.id == role_id for item in self.roles)

    def election_period_exists(self, election_period_id: UUID) -> bool:
        return any(item.id == election_period_id for item in self.election_periods)

    def _ensure_roles_exist(self, role_ids: tuple[UUID, ...]) -> None:
        missing = [role_id for role_id in role_ids if not self.role_exists(role_id)]
        if missing:
            joined = ", ".join(str(item) for item in missing)
            raise ValueError(f"Unknown role IDs: {joined}")
