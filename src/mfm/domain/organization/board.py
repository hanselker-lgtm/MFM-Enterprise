"""Board aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import UUID
from uuid import uuid4

from mfm.domain.organization.board_member import BoardMember
from mfm.domain.organization.board_status import BoardStatus
from mfm.domain.organization.board_term import BoardTerm
from mfm.domain.organization.exceptions import BoardChairRequirementError
from mfm.domain.organization.exceptions import BoardMemberNotFoundError
from mfm.domain.organization.exceptions import DuplicateBoardRoleError
from mfm.domain.organization.exceptions import InvalidBoardNameError
from mfm.domain.organization.exceptions import InvalidBoardStatusTransitionError
from mfm.domain.organization.organization_id import OrganizationId


@dataclass(slots=True)
class Board:
    """Aggregate root for board term, members and governance rules."""

    organization_id: OrganizationId
    name: str
    term_start: date
    term_end: date
    members: list[BoardMember]
    status: BoardStatus = BoardStatus.ACTIVE
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise TypeError("id must be UUID")

        if not isinstance(self.organization_id, OrganizationId):
            self.organization_id = OrganizationId(self.organization_id)

        self.name = self._normalize_name(self.name)

        if not isinstance(self.status, BoardStatus):
            self.status = BoardStatus(str(self.status).upper())

        _ = BoardTerm(self.term_start, self.term_end)

        self.members = list(self.members)
        self._assert_no_duplicate_roles()
        self._assert_has_chair()

    @staticmethod
    def _normalize_name(value: str) -> str:
        if not isinstance(value, str):
            raise InvalidBoardNameError("name must be a string")
        normalized = value.strip()
        if not normalized:
            raise InvalidBoardNameError("name cannot be empty")
        return normalized

    def _assert_active(self) -> None:
        if self.status is not BoardStatus.ACTIVE:
            raise InvalidBoardStatusTransitionError("Board is not active")

    def _assert_term_date(self, value: date) -> None:
        if not BoardTerm(self.term_start, self.term_end).includes(value):
            raise InvalidBoardStatusTransitionError(
                "date must be within board term"
            )

    def _assert_no_duplicate_roles(self) -> None:
        for index, left in enumerate(self.members):
            for right in self.members[index + 1 :]:
                if left.role != right.role:
                    continue
                if left.overlaps(right.appointed_on, right.resigned_on):
                    raise DuplicateBoardRoleError(
                        f"Role {left.role} overlaps in same period"
                    )

    def _assert_has_chair(self) -> None:
        if any(member.is_chair for member in self.members):
            return
        raise BoardChairRequirementError("Board must have at least one chair")

    def add_member(self, member: BoardMember) -> None:
        self._assert_active()
        self._assert_term_date(member.appointed_on)
        if member.resigned_on is not None:
            self._assert_term_date(member.resigned_on)

        for existing in self.members:
            if existing.role == member.role and existing.overlaps(
                member.appointed_on,
                member.resigned_on,
            ):
                raise DuplicateBoardRoleError(
                    f"Role {member.role} overlaps in same period"
                )

        self.members.append(member)
        self._assert_has_chair()

    def remove_member(self, member_id: UUID, on_date: date | None = None) -> None:
        self._assert_active()
        effective_date = on_date or datetime.now(UTC).date()
        self._assert_term_date(effective_date)

        target = self._find_active_member(member_id, effective_date)
        if target is None:
            raise BoardMemberNotFoundError("Active board member not found")

        target.close_membership(effective_date)

        if target.is_chair:
            if not self._has_other_chair(target, effective_date):
                target.resigned_on = None
                raise BoardChairRequirementError("Board must have at least one chair")

    def appoint_chair(self, member_id: UUID, on_date: date | None = None) -> None:
        self._assert_active()
        effective_date = on_date or datetime.now(UTC).date()
        self._assert_term_date(effective_date)

        target = self._find_active_member(member_id, effective_date)
        if target is None:
            raise BoardMemberNotFoundError("Active board member not found")

        target.is_chair = True

    def calculate_quorum(self, as_of: date | None = None) -> int:
        effective_date = as_of or datetime.now(UTC).date()
        active_count = sum(
            1 for member in self.members if member.is_active_on(effective_date)
        )
        if active_count == 0:
            return 0
        return (active_count // 2) + 1

    def close_term(self, on_date: date | None = None) -> None:
        self._assert_active()
        effective_date = on_date or self.term_end
        self._assert_term_date(effective_date)

        for member in self.members:
            if member.is_active_on(effective_date):
                member.close_membership(effective_date)

        self.status = BoardStatus.CLOSED

    def _find_active_member(self, member_id: UUID, at_date: date) -> BoardMember | None:
        for member in self.members:
            if member.member_id == member_id and member.is_active_on(at_date):
                return member
        return None

    def _has_other_chair(self, removed: BoardMember, at_date: date) -> bool:
        for member in self.members:
            if member is removed:
                continue
            if member.is_chair and member.is_active_on(at_date):
                return True
        return False
