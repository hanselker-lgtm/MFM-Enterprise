"""Member domain model."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from uuid import UUID, uuid4

from mfm.domain.member.exceptions import (
    InvalidMemberStatusTransitionError,
    InvalidMemberNumberError,
    InvalidMemberReferenceError,
    InvalidMembershipDatesError,
)
from mfm.domain.member.member_status import MemberStatus


@dataclass(slots=True)
class Member:
    """Pure domain model representing a membership linked to a contact."""

    contact_id: UUID
    member_number: str
    status: MemberStatus = MemberStatus.ACTIVE
    join_date: date = field(default_factory=lambda: datetime.now(UTC).date())
    leave_date: date | None = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.contact_id, UUID):
            raise InvalidMemberReferenceError("contact_id must be a UUID")

        if not isinstance(self.member_number, str):
            raise InvalidMemberNumberError("member_number must be a string")

        self.member_number = self.member_number.strip()
        if not self.member_number:
            raise InvalidMemberNumberError("member_number cannot be empty")

        if self.leave_date is not None and self.leave_date < self.join_date:
            raise InvalidMembershipDatesError(
                "leave_date cannot be before join_date"
            )

    def activate(self) -> None:
        if self.status not in (MemberStatus.INACTIVE, MemberStatus.SUSPENDED):
            raise InvalidMemberStatusTransitionError(
                f"Cannot activate member from status {self.status.value}"
            )

        self.status = MemberStatus.ACTIVE
        self.leave_date = None

    def deactivate(self) -> None:
        if self.status is not MemberStatus.ACTIVE:
            raise InvalidMemberStatusTransitionError(
                f"Cannot deactivate member from status {self.status.value}"
            )

        self.status = MemberStatus.INACTIVE

    def resign(self, resign_date: date | None = None) -> None:
        if self.status is MemberStatus.TERMINATED:
            raise InvalidMemberStatusTransitionError(
                "Cannot resign a terminated member"
            )

        final_date = resign_date or datetime.now(UTC).date()
        if final_date < self.join_date:
            raise InvalidMembershipDatesError(
                "leave_date cannot be before join_date"
            )

        self.status = MemberStatus.TERMINATED
        self.leave_date = final_date
