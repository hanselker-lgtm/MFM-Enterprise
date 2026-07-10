"""Role assignment entity."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any
from typing import Mapping
from uuid import UUID

from mfm.domain.organization.exceptions import InvalidRoleAssignmentPeriodError
from mfm.domain.organization.role_id import RoleId


@dataclass(slots=True)
class RoleAssignment:
    """Assignment of a role to an assignee in an organization over a period."""

    role_id: RoleId
    assignee_id: UUID
    organization_id: UUID
    valid_from: date
    valid_to: date | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.role_id, RoleId):
            self.role_id = RoleId(self.role_id)

        if not isinstance(self.assignee_id, UUID):
            raise InvalidRoleAssignmentPeriodError("assignee_id must be UUID")

        if not isinstance(self.organization_id, UUID):
            raise InvalidRoleAssignmentPeriodError("organization_id must be UUID")

        if not isinstance(self.valid_from, date):
            raise InvalidRoleAssignmentPeriodError("valid_from must be date")

        if self.valid_to is not None:
            if not isinstance(self.valid_to, date):
                raise InvalidRoleAssignmentPeriodError("valid_to must be date or None")
            if self.valid_to < self.valid_from:
                raise InvalidRoleAssignmentPeriodError(
                    "valid_from must be <= valid_to"
                )

    def overlaps(self, start: date, end: date | None) -> bool:
        own_end = self.valid_to
        target_end = end
        if own_end is None and target_end is None:
            return True
        if own_end is None:
            return target_end >= self.valid_from
        if target_end is None:
            return own_end >= start
        return self.valid_from <= target_end and own_end >= start

    def to_dict(self) -> dict[str, Any]:
        return {
            "role_id": str(self.role_id),
            "assignee_id": str(self.assignee_id),
            "organization_id": str(self.organization_id),
            "valid_from": self.valid_from.isoformat(),
            "valid_to": self.valid_to.isoformat() if self.valid_to is not None else None,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "RoleAssignment":
        if not isinstance(data, Mapping):
            raise InvalidRoleAssignmentPeriodError("assignment must be mapping")

        required = {"role_id", "assignee_id", "organization_id", "valid_from", "valid_to"}
        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise InvalidRoleAssignmentPeriodError(
                f"assignment missing keys: {', '.join(missing)}"
            )

        return cls(
            role_id=RoleId(data["role_id"]),
            assignee_id=UUID(str(data["assignee_id"])),
            organization_id=UUID(str(data["organization_id"])),
            valid_from=date.fromisoformat(str(data["valid_from"])),
            valid_to=(
                date.fromisoformat(str(data["valid_to"]))
                if data["valid_to"] is not None
                else None
            ),
        )
