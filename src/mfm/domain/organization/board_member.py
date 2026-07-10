"""Board member entity."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.domain.organization.exceptions import InvalidBoardMemberOperationError


@dataclass(slots=True)
class BoardMember:
    """Member participation in a board term with role and chair flag."""

    member_id: UUID
    role: str
    appointed_on: date
    resigned_on: date | None = None
    is_chair: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.member_id, UUID):
            raise InvalidBoardMemberOperationError("member_id must be UUID")
        if not isinstance(self.role, str) or not self.role.strip():
            raise InvalidBoardMemberOperationError("role must be a non-empty string")
        if not isinstance(self.appointed_on, date):
            raise InvalidBoardMemberOperationError("appointed_on must be a date")
        if self.resigned_on is not None:
            if not isinstance(self.resigned_on, date):
                raise InvalidBoardMemberOperationError("resigned_on must be date or None")
            if self.resigned_on < self.appointed_on:
                raise InvalidBoardMemberOperationError(
                    "resigned_on cannot be before appointed_on"
                )
        self.role = self.role.strip().upper()

    def is_active_on(self, at_date: date) -> bool:
        return self.appointed_on <= at_date and (
            self.resigned_on is None or self.resigned_on >= at_date
        )

    def overlaps(self, start: date, end: date | None) -> bool:
        own_end = self.resigned_on
        target_end = end
        if own_end is None and target_end is None:
            return True
        if own_end is None:
            return target_end >= self.appointed_on
        if target_end is None:
            return own_end >= start
        return self.appointed_on <= target_end and own_end >= start

    def close_membership(self, on_date: date) -> None:
        if on_date < self.appointed_on:
            raise InvalidBoardMemberOperationError(
                "resignation date cannot be before appointed_on"
            )
        if self.resigned_on is not None and on_date > self.resigned_on:
            raise InvalidBoardMemberOperationError(
                "resignation date cannot be after existing resigned_on"
            )
        self.resigned_on = on_date
