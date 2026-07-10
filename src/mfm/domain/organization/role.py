"""Generic Role aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date
from typing import Any
from typing import ClassVar
from typing import Mapping
from uuid import UUID

from mfm.domain.organization.exceptions import ArchivedRoleAssignmentError
from mfm.domain.organization.exceptions import DuplicateRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleAssignmentPeriodError
from mfm.domain.organization.exceptions import InvalidRoleNameError
from mfm.domain.organization.exceptions import RoleAssignmentNotFoundError
from mfm.domain.organization.exceptions import RoleAssignmentOverlapError
from mfm.domain.organization.exceptions import RoleSerializationError
from mfm.domain.organization.role_assignment import RoleAssignment
from mfm.domain.organization.role_code import RoleCode
from mfm.domain.organization.role_id import RoleId
from mfm.domain.organization.role_status import RoleStatus
from mfm.domain.organization.role_type import RoleType


@dataclass(slots=True)
class Role:
    """Aggregate root for generic role definition and assignments."""

    _code_registry: ClassVar[dict[str, RoleId]] = {}

    role_code: RoleCode
    name: str
    category: RoleType
    id: RoleId = field(default_factory=RoleId.new)
    description: str | None = None
    status: RoleStatus = RoleStatus.ACTIVE
    assignments: list[RoleAssignment] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not isinstance(self.id, RoleId):
            self.id = RoleId(self.id)

        if not isinstance(self.role_code, RoleCode):
            self.role_code = RoleCode(str(self.role_code))

        self.name = self._normalize_name(self.name)

        if self.description is not None:
            self.description = self._normalize_description(self.description)

        if not isinstance(self.category, RoleType):
            self.category = RoleType(str(self.category).upper())

        if not isinstance(self.status, RoleStatus):
            self.status = RoleStatus(str(self.status).upper())

        self.assignments = list(self.assignments)
        for assignment in self.assignments:
            if assignment.role_id != self.id:
                raise InvalidRoleAssignmentPeriodError(
                    "assignment.role_id must match role.id"
                )
        self._assert_no_assignment_overlap()
        self._register_role_code()

    @staticmethod
    def _normalize_name(value: str) -> str:
        if not isinstance(value, str):
            raise InvalidRoleNameError("name must be a string")
        normalized = value.strip()
        if not normalized:
            raise InvalidRoleNameError("name cannot be empty")
        return normalized

    @staticmethod
    def _normalize_description(value: str) -> str | None:
        if not isinstance(value, str):
            raise TypeError("description must be a string")
        normalized = value.strip()
        return normalized or None

    def _register_role_code(self) -> None:
        existing = self._code_registry.get(self.role_code.value)
        if existing is not None and existing != self.id:
            raise DuplicateRoleCodeError(f"role_code {self.role_code.value} already exists")
        self._code_registry[self.role_code.value] = self.id

    def _assert_no_assignment_overlap(self) -> None:
        grouped: dict[UUID, list[RoleAssignment]] = {}
        for assignment in self.assignments:
            grouped.setdefault(assignment.assignee_id, []).append(assignment)

        for values in grouped.values():
            ordered = sorted(values, key=lambda item: item.valid_from)
            for index, left in enumerate(ordered):
                for right in ordered[index + 1 :]:
                    if left.overlaps(right.valid_from, right.valid_to):
                        raise RoleAssignmentOverlapError(
                            "assignment periods may not overlap"
                        )

    def assign(
        self,
        *,
        assignee_id: UUID,
        organization_id: UUID,
        valid_from: date,
        valid_to: date | None = None,
    ) -> RoleAssignment:
        if self.status is RoleStatus.ARCHIVED:
            raise ArchivedRoleAssignmentError("archived roles cannot be assigned")

        assignment = RoleAssignment(
            role_id=self.id,
            assignee_id=assignee_id,
            organization_id=organization_id,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        for existing in self.assignments:
            if existing.assignee_id != assignment.assignee_id:
                continue
            if existing.overlaps(assignment.valid_from, assignment.valid_to):
                raise RoleAssignmentOverlapError("assignment periods may not overlap")

        self.assignments.append(assignment)
        return assignment

    def revoke(self, assignee_id: UUID, revoked_on: date) -> None:
        target = next(
            (
                assignment
                for assignment in self.assignments
                if assignment.assignee_id == assignee_id and assignment.valid_to is None
            ),
            None,
        )
        if target is None:
            raise RoleAssignmentNotFoundError("active assignment not found")

        if revoked_on < target.valid_from:
            raise InvalidRoleAssignmentPeriodError(
                "revoked_on cannot be before valid_from"
            )

        target.valid_to = revoked_on

    def rename(self, new_name: str) -> None:
        normalized = self._normalize_name(new_name)
        if normalized == self.name:
            return
        self.name = normalized

    def archive(self) -> None:
        self.status = RoleStatus.ARCHIVED

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "role_code": str(self.role_code),
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "status": self.status.value,
            "assignments": [assignment.to_dict() for assignment in self.assignments],
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "Role":
        if not isinstance(data, Mapping):
            raise RoleSerializationError("data must be a mapping")

        required = {
            "id",
            "role_code",
            "name",
            "description",
            "category",
            "status",
            "assignments",
        }
        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise RoleSerializationError(
                f"data is missing required keys: {', '.join(missing)}"
            )

        try:
            assignments_payload = data["assignments"]
            if not isinstance(assignments_payload, list):
                raise RoleSerializationError("assignments must be a list")

            description_value = data["description"]
            return cls(
                id=RoleId(data["id"]),
                role_code=RoleCode(str(data["role_code"])),
                name=str(data["name"]),
                description=(None if description_value is None else str(description_value)),
                category=RoleType(str(data["category"]).upper()),
                status=RoleStatus(str(data["status"]).upper()),
                assignments=[
                    RoleAssignment.from_dict(item) for item in assignments_payload
                ],
            )
        except RoleSerializationError:
            raise
        except Exception as exc:
            raise RoleSerializationError("Invalid serialized role") from exc

    @classmethod
    def _clear_registry_for_tests(cls) -> None:
        cls._code_registry.clear()
