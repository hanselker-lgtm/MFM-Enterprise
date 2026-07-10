"""Committee aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import date
from datetime import datetime
from typing import Any
from typing import Mapping

from mfm.domain.organization.committee_id import CommitteeId
from mfm.domain.organization.committee_member import CommitteeMember
from mfm.domain.organization.committee_status import CommitteeStatus
from mfm.domain.organization.exceptions import CommitteeMemberNotFoundError
from mfm.domain.organization.exceptions import CommitteeSerializationError
from mfm.domain.organization.exceptions import DuplicateCommitteeMemberError
from mfm.domain.organization.exceptions import InvalidCommitteeNameError
from mfm.domain.organization.exceptions import InvalidCommitteeStatusTransitionError
from mfm.domain.organization.organization_id import OrganizationId


@dataclass(slots=True)
class Committee:
    """Aggregate root for committee membership and lifecycle."""

    organization_id: OrganizationId
    name: str
    purpose: str
    members: list[CommitteeMember]
    status: CommitteeStatus = CommitteeStatus.ACTIVE
    id: CommitteeId = field(default_factory=CommitteeId.new)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not isinstance(self.id, CommitteeId):
            self.id = CommitteeId(self.id)

        if not isinstance(self.organization_id, OrganizationId):
            self.organization_id = OrganizationId(self.organization_id)

        self.name = self._normalize_name(self.name)
        self.purpose = self._normalize_text(self.purpose)

        if not isinstance(self.status, CommitteeStatus):
            self.status = CommitteeStatus(str(self.status).upper())

        if not isinstance(self.created_at, datetime):
            raise TypeError("created_at must be datetime")
        if not isinstance(self.updated_at, datetime):
            raise TypeError("updated_at must be datetime")

        self.created_at = self._as_utc(self.created_at)
        self.updated_at = self._as_utc(self.updated_at)
        if self.updated_at < self.created_at:
            self.updated_at = self.created_at

        self.members = list(self.members)
        self._assert_no_duplicate_members()

    @staticmethod
    def _as_utc(value: datetime) -> datetime:
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

    @staticmethod
    def _normalize_name(value: str) -> str:
        if not isinstance(value, str):
            raise InvalidCommitteeNameError("name must be a string")
        normalized = value.strip()
        if not normalized:
            raise InvalidCommitteeNameError("name cannot be empty")
        return normalized

    @staticmethod
    def _normalize_text(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("purpose/description must be a string")
        return value.strip()

    def _touch(self) -> None:
        self.updated_at = datetime.now(UTC)

    def _assert_active(self) -> None:
        if self.status is not CommitteeStatus.ACTIVE:
            raise InvalidCommitteeStatusTransitionError("Committee is not active")

    def _assert_no_duplicate_members(self) -> None:
        active_ids: set[Any] = set()
        for member in self.members:
            if member.left_at is not None:
                continue
            if member.reference_id in active_ids:
                raise DuplicateCommitteeMemberError(
                    f"Duplicate active member {member.reference_id}"
                )
            active_ids.add(member.reference_id)

    def rename(self, new_name: str) -> None:
        normalized = self._normalize_name(new_name)
        if normalized == self.name:
            return
        self.name = normalized
        self._touch()

    def change_purpose(self, new_purpose: str) -> None:
        normalized = self._normalize_text(new_purpose)
        if normalized == self.purpose:
            return
        self.purpose = normalized
        self._touch()

    def add_member(self, member: CommitteeMember) -> None:
        self._assert_active()
        if any(m.reference_id == member.reference_id and m.left_at is None for m in self.members):
            raise DuplicateCommitteeMemberError(
                f"Duplicate active member {member.reference_id}"
            )
        self.members.append(member)
        self._touch()

    def remove_member(self, reference_id, on_date: date | None = None) -> None:
        self._assert_active()
        effective = on_date or datetime.now(UTC).date()
        target = next(
            (
                m
                for m in self.members
                if m.reference_id == reference_id and m.left_at is None
            ),
            None,
        )
        if target is None:
            raise CommitteeMemberNotFoundError("Active committee member not found")
        target.close_membership(effective)
        self._touch()

    def activate(self) -> None:
        if self.status is CommitteeStatus.ACTIVE:
            return
        self.status = CommitteeStatus.ACTIVE
        self._touch()

    def deactivate(self) -> None:
        if self.status is CommitteeStatus.INACTIVE:
            return
        self.status = CommitteeStatus.INACTIVE
        self._touch()

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "organization_id": str(self.organization_id),
            "name": self.name,
            "purpose": self.purpose,
            "status": self.status.value,
            "members": [
                {
                    "reference_id": str(member.reference_id),
                    "function_title": member.function_title,
                    "joined_at": member.joined_at.isoformat(),
                    "left_at": member.left_at.isoformat() if member.left_at is not None else None,
                }
                for member in self.members
            ],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "Committee":
        if not isinstance(data, Mapping):
            raise CommitteeSerializationError("data must be a mapping")

        required = {
            "id",
            "organization_id",
            "name",
            "purpose",
            "status",
            "members",
            "created_at",
            "updated_at",
        }
        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise CommitteeSerializationError(
                f"data is missing required keys: {', '.join(missing)}"
            )

        try:
            members_payload = data["members"]
            if not isinstance(members_payload, list):
                raise CommitteeSerializationError("members must be a list")

            members = [
                CommitteeMember(
                    reference_id=item["reference_id"],
                    function_title=str(item["function_title"]),
                    joined_at=date.fromisoformat(str(item["joined_at"])),
                    left_at=(
                        date.fromisoformat(str(item["left_at"]))
                        if item.get("left_at") is not None
                        else None
                    ),
                )
                for item in members_payload
            ]

            return cls(
                id=CommitteeId(data["id"]),
                organization_id=OrganizationId(data["organization_id"]),
                name=str(data["name"]),
                purpose=str(data["purpose"]),
                status=CommitteeStatus(str(data["status"]).upper()),
                members=members,
                created_at=datetime.fromisoformat(str(data["created_at"])),
                updated_at=datetime.fromisoformat(str(data["updated_at"])),
            )
        except CommitteeSerializationError:
            raise
        except Exception as exc:
            raise CommitteeSerializationError("Invalid serialized committee") from exc
