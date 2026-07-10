"""Role aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from typing import Any
from typing import ClassVar
from typing import Mapping

from mfm.domain.organization.exceptions import DuplicateRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleIdentityMutationError
from mfm.domain.organization.exceptions import InvalidRoleNameError
from mfm.domain.organization.exceptions import InvalidRoleStatusTransitionError
from mfm.domain.organization.exceptions import RoleSerializationError
from mfm.domain.organization.role_code import RoleCode
from mfm.domain.organization.role_id import RoleId
from mfm.domain.organization.role_status import RoleStatus
from mfm.domain.organization.role_type import RoleType


@dataclass(slots=True)
class Role:
    """Aggregate root for role identity and lifecycle."""

    _code_registry: ClassVar[dict[str, RoleId]] = {}

    id: RoleId = field(default_factory=RoleId.new)
    role_code: RoleCode = field(default_factory=lambda: RoleCode("ROLE-UNSET"))
    name: str = ""
    description: str | None = None
    role_type: RoleType = RoleType.OPERATIONAL
    status: RoleStatus = RoleStatus.ACTIVE
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    _identity_locked: bool = field(default=False, init=False, repr=False, compare=False)

    def __setattr__(self, name: str, value: Any) -> None:
        if (
            name in {"id", "role_code"}
            and getattr(self, "_identity_locked", False)
            and hasattr(self, name)
        ):
            current = getattr(self, name)
            if value != current:
                raise InvalidRoleIdentityMutationError(
                    f"{name} is immutable for Role identity"
                )
        super().__setattr__(name, value)

    def __post_init__(self) -> None:
        if not isinstance(self.id, RoleId):
            self.id = RoleId(self.id)

        if not isinstance(self.role_code, RoleCode):
            self.role_code = RoleCode(str(self.role_code))

        self.name = self._normalize_name(self.name)

        if self.description is not None:
            self.description = self._normalize_description(self.description)

        if not isinstance(self.role_type, RoleType):
            self.role_type = RoleType(str(self.role_type).upper())

        if not isinstance(self.status, RoleStatus):
            self.status = RoleStatus(str(self.status).upper())

        if not isinstance(self.created_at, datetime):
            raise TypeError("created_at must be datetime")

        if not isinstance(self.updated_at, datetime):
            raise TypeError("updated_at must be datetime")

        self.created_at = self._as_utc(self.created_at)
        self.updated_at = self._as_utc(self.updated_at)
        if self.updated_at < self.created_at:
            self.updated_at = self.created_at

        self._register_role_code()
        self._identity_locked = True

    @staticmethod
    def _as_utc(value: datetime) -> datetime:
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

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

    def _touch(self) -> None:
        self.updated_at = datetime.now(UTC)

    def rename(self, new_name: str) -> None:
        normalized = self._normalize_name(new_name)
        if normalized == self.name:
            return

        self.name = normalized
        self._touch()

    def activate(self) -> None:
        if self.status is RoleStatus.ARCHIVED:
            raise InvalidRoleStatusTransitionError("Archived role cannot be activated")
        if self.status is not RoleStatus.INACTIVE:
            raise InvalidRoleStatusTransitionError(
                f"Cannot activate role from status {self.status.value}"
            )

        self.status = RoleStatus.ACTIVE
        self._touch()

    def deactivate(self) -> None:
        if self.status is RoleStatus.ARCHIVED:
            raise InvalidRoleStatusTransitionError("Archived role cannot be deactivated")
        if self.status is not RoleStatus.ACTIVE:
            raise InvalidRoleStatusTransitionError(
                f"Cannot deactivate role from status {self.status.value}"
            )

        self.status = RoleStatus.INACTIVE
        self._touch()

    def archive(self) -> None:
        if self.status is RoleStatus.ARCHIVED:
            return

        self.status = RoleStatus.ARCHIVED
        self._touch()

    def change_description(self, description: str | None) -> None:
        if description is None:
            if self.description is None:
                return
            self.description = None
            self._touch()
            return

        normalized = self._normalize_description(description)
        if normalized == self.description:
            return

        self.description = normalized
        self._touch()

    def to_dict(self) -> dict[str, str | None]:
        return {
            "id": str(self.id),
            "role_code": str(self.role_code),
            "name": self.name,
            "description": self.description,
            "role_type": self.role_type.value,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
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
            "role_type",
            "status",
            "created_at",
            "updated_at",
        }
        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise RoleSerializationError(
                f"data is missing required keys: {', '.join(missing)}"
            )

        try:
            description_value = data["description"]
            return cls(
                id=RoleId(data["id"]),
                role_code=RoleCode(str(data["role_code"])),
                name=str(data["name"]),
                description=(None if description_value is None else str(description_value)),
                role_type=RoleType(str(data["role_type"]).upper()),
                status=RoleStatus(str(data["status"]).upper()),
                created_at=datetime.fromisoformat(str(data["created_at"])),
                updated_at=datetime.fromisoformat(str(data["updated_at"])),
            )
        except Exception as exc:
            raise RoleSerializationError("Invalid serialized role") from exc

    @classmethod
    def _clear_registry_for_tests(cls) -> None:
        cls._code_registry.clear()
