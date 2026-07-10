from __future__ import annotations

from datetime import date
from uuid import uuid4

import pytest

from mfm.domain.organization.board import Board
from mfm.domain.organization.board_member import BoardMember
from mfm.domain.organization.board_status import BoardStatus
from mfm.domain.organization.exceptions import BoardChairRequirementError
from mfm.domain.organization.exceptions import BoardMemberNotFoundError
from mfm.domain.organization.exceptions import DuplicateBoardRoleError
from mfm.domain.organization.exceptions import InvalidBoardStatusTransitionError
from mfm.domain.organization.exceptions import InvalidBoardTermError
from mfm.domain.organization.organization_id import OrganizationId


def _board_member(
    *,
    role: str,
    is_chair: bool = False,
    appointed_on: date = date(2026, 1, 1),
    resigned_on: date | None = None,
):
    return BoardMember(
        member_id=uuid4(),
        role=role,
        is_chair=is_chair,
        appointed_on=appointed_on,
        resigned_on=resigned_on,
    )


def _board(members: list[BoardMember]) -> Board:
    return Board(
        organization_id=OrganizationId.new(),
        name="Main Board",
        term_start=date(2026, 1, 1),
        term_end=date(2026, 12, 31),
        members=members,
    )


def test_create_board_with_valid_term_and_chair() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    board = _board([chair])

    assert board.status is BoardStatus.ACTIVE
    assert board.members[0].is_chair is True


def test_create_board_requires_chair() -> None:
    member = _board_member(role="SECRETARY", is_chair=False)

    with pytest.raises(BoardChairRequirementError):
        _board([member])


def test_create_board_rejects_invalid_term() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)

    with pytest.raises(InvalidBoardTermError):
        Board(
            organization_id=OrganizationId.new(),
            name="Main Board",
            term_start=date(2026, 12, 31),
            term_end=date(2026, 1, 1),
            members=[chair],
        )


def test_add_member() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    board = _board([chair])

    secretary = _board_member(role="SECRETARY", is_chair=False)
    board.add_member(secretary)

    assert secretary in board.members


def test_add_member_rejects_duplicate_role_overlap() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    board = _board([chair])

    with pytest.raises(DuplicateBoardRoleError):
        board.add_member(_board_member(role="CHAIR", is_chair=False))


def test_remove_member_keeps_history() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    secretary = _board_member(role="SECRETARY", is_chair=False)
    board = _board([chair, secretary])

    board.remove_member(secretary.member_id, on_date=date(2026, 6, 1))

    assert len(board.members) == 2
    assert secretary.resigned_on == date(2026, 6, 1)


def test_remove_last_chair_rejected() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    board = _board([chair])

    with pytest.raises(BoardChairRequirementError):
        board.remove_member(chair.member_id, on_date=date(2026, 6, 1))


def test_appoint_chair() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    treasurer = _board_member(role="TREASURER", is_chair=False)
    board = _board([chair, treasurer])

    board.appoint_chair(treasurer.member_id, on_date=date(2026, 5, 1))

    assert treasurer.is_chair is True


def test_calculate_quorum() -> None:
    board = _board(
        [
            _board_member(role="CHAIR", is_chair=True),
            _board_member(role="SECRETARY"),
            _board_member(role="TREASURER"),
            _board_member(role="MEMBER-1"),
            _board_member(role="MEMBER-2"),
        ]
    )

    assert board.calculate_quorum(as_of=date(2026, 6, 1)) == 3


def test_close_term() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    secretary = _board_member(role="SECRETARY", is_chair=False)
    board = _board([chair, secretary])

    board.close_term(on_date=date(2026, 12, 31))

    assert board.status is BoardStatus.CLOSED
    assert chair.resigned_on == date(2026, 12, 31)
    assert secretary.resigned_on == date(2026, 12, 31)


def test_invalid_transition_when_board_not_active() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    board = _board([chair])
    board.close_term(on_date=date(2026, 12, 31))

    with pytest.raises(InvalidBoardStatusTransitionError):
        board.add_member(_board_member(role="SECRETARY"))


def test_remove_member_not_found() -> None:
    chair = _board_member(role="CHAIR", is_chair=True)
    board = _board([chair])

    with pytest.raises(BoardMemberNotFoundError):
        board.remove_member(uuid4(), on_date=date(2026, 6, 1))
