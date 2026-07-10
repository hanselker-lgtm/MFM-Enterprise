"""Committee member entity."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.domain.organization.exceptions import InvalidCommitteeMemberOperationError


@dataclass(slots=True)
class CommitteeMember:
    """Represents committee assignment for a contact/member reference."""

    reference_id: UUID
    function_title: str
    joined_at: date
    left_at: date | None = None

    def __post_init__(self) -> None:
        if isinstance(self.reference_id, str):
            self.reference_id = UUID(self.reference_id)

        if not isinstance(self.reference_id, UUID):
            raise InvalidCommitteeMemberOperationError("reference_id must be UUID")
        if not isinstance(self.function_title, str) or not self.function_title.strip():
            raise InvalidCommitteeMemberOperationError(
                "function_title must be a non-empty string"
            )
        if not isinstance(self.joined_at, date):
            raise InvalidCommitteeMemberOperationError("joined_at must be a date")
        if self.left_at is not None:
            if not isinstance(self.left_at, date):
                raise InvalidCommitteeMemberOperationError("left_at must be date or None")
            if self.left_at < self.joined_at:
                raise InvalidCommitteeMemberOperationError(
                    "left_at cannot be before joined_at"
                )

        self.function_title = self.function_title.strip()

    def is_active_on(self, at_date: date) -> bool:
        return self.joined_at <= at_date and (
            self.left_at is None or self.left_at >= at_date
        )

    def close_membership(self, on_date: date) -> None:
        if on_date < self.joined_at:
            raise InvalidCommitteeMemberOperationError(
                "left_at cannot be before joined_at"
            )
        if self.left_at is not None and on_date > self.left_at:
            raise InvalidCommitteeMemberOperationError(
                "left_at cannot be after existing left_at"
            )
        self.left_at = on_date
