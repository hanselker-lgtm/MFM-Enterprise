"""Membership domain model."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from uuid import UUID, uuid4

from mfm.domain.membership.exceptions import (
    InvalidMembershipDatesError,
    InvalidMembershipReferenceError,
    InvalidMembershipStatusTransitionError,
    MultipleActiveMembershipsError,
)
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.domain.membership.membership_type import MembershipType


@dataclass(slots=True)
class Membership:
    """Pure domain model representing a member's membership period."""

    member_id: UUID
    membership_type: MembershipType
    start_date: date = field(default_factory=lambda: datetime.now(UTC).date())
    end_date: date | None = None
    status: MembershipStatus = MembershipStatus.ACTIVE
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.member_id, UUID):
            raise InvalidMembershipReferenceError("member_id must be a UUID")

        if not isinstance(self.membership_type, MembershipType):
            raise InvalidMembershipReferenceError(
                "membership_type must be a MembershipType"
            )

        if self.end_date is not None and self.end_date < self.start_date:
            raise InvalidMembershipDatesError(
                "end_date cannot be before start_date"
            )

        if self.status is MembershipStatus.ACTIVE and self.end_date is not None:
            raise InvalidMembershipDatesError(
                "active membership cannot have end_date"
            )

    @property
    def membership_type_id(self) -> UUID:
        """Convenience id for persistence/application integration."""

        return self.membership_type.id

    def end(self, end_date: date | None = None) -> None:
        if self.status in (MembershipStatus.ENDED, MembershipStatus.EXPIRED):
            raise InvalidMembershipStatusTransitionError(
                "Cannot end an already ended membership"
            )

        final_date = end_date or datetime.now(UTC).date()
        if final_date < self.start_date:
            raise InvalidMembershipDatesError(
                "end_date cannot be before start_date"
            )

        self.status = MembershipStatus.ENDED
        self.end_date = final_date

    def expire(self, expiration_date: date | None = None) -> None:
        """Backward compatible alias for ending a membership."""

        self.end(expiration_date)

    def suspend(self) -> None:
        if self.status is not MembershipStatus.ACTIVE:
            raise InvalidMembershipStatusTransitionError(
                f"Cannot suspend membership from status {self.status.value}"
            )

        self.status = MembershipStatus.SUSPENDED

    def reactivate(self) -> None:
        if self.status not in (
            MembershipStatus.SUSPENDED,
            MembershipStatus.ENDED,
            MembershipStatus.EXPIRED,
        ):
            raise InvalidMembershipStatusTransitionError(
                f"Cannot reactivate membership from status {self.status.value}"
            )

        self.status = MembershipStatus.ACTIVE
        self.end_date = None

    @staticmethod
    def ensure_single_active(memberships: list["Membership"], member_id: UUID) -> None:
        active_count = sum(
            1
            for membership in memberships
            if membership.member_id == member_id
            and membership.status is MembershipStatus.ACTIVE
        )

        if active_count > 1:
            raise MultipleActiveMembershipsError(
                f"Member {member_id} cannot have more than one active membership"
            )
