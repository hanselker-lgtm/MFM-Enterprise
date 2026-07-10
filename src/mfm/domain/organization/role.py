"""Role aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import date
from datetime import datetime
from typing import Any
from typing import ClassVar
from typing import Mapping

from mfm.domain.organization.exceptions import DuplicateRoleCodeError
from mfm.domain.organization.exceptions import InvalidRoleIdentityMutationError
from mfm.domain.organization.exceptions import InvalidRoleNameError
from mfm.domain.organization.exceptions import InvalidRoleStatusTransitionError
from mfm.domain.organization.exceptions import InvalidRoleValidityPeriodError
from mfm.domain.organization.exceptions import RoleSerializationError
from mfm.domain.organization.role_id import RoleCode
from mfm.domain.organization.role_id import RoleId
from mfm.domain.organization.role_status import RoleStatus


@dataclass(slots=True)
class Role:
    """Aggregate root for role identity and lifecycle."""

    _code_registry: ClassVar[dict[str, RoleId]] = {}

    id: RoleId = field(default_factory=RoleId.new)
    role_code: RoleCode = field(default_factory=lambda: RoleCode("ROLE-UNSET"))
    name: str = ""
    description: str | None = None
    status: RoleStatus = RoleStatus.ACTIVE
    valid_from: date = field(default_factory=lambda: datetime.now(UTC).date())
    valid_to: date | None = None
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

        if not isinstance(self.status, RoleStatus):
            self.status = RoleStatus(str(self.status).upper())

        if not isinstance(self.valid_from, date):
            raise TypeError("valid_from must be date")

        if self.valid_to is not None and not isinstance(self.valid_to, date):
            raise TypeError("valid_to must be date or None")

        if self.valid_to is not None and self.valid_from > self.valid_to:
            raise InvalidRoleValidityPeriodError("valid_from must be <= valid_to")

        self._register_role_code()
        self._identity_locked = True

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

    def rename(self, new_name: str) -> None:
        normalized = self._normalize_name(new_name)
        if normalized == self.name:
            return

        self.name = normalized

    def activate(self) -> None:
        if self.status is RoleStatus.ARCHIVED:
            raise InvalidRoleStatusTransitionError("Archived role cannot be activated")

        if self.status is RoleStatus.ACTIVE:
            return

        self.status = RoleStatus.ACTIVE

    def deactivate(self) -> None:
        if self.status is RoleStatus.ARCHIVED:
            raise InvalidRoleStatusTransitionError("Archived role cannot be deactivated")

        if self.status is RoleStatus.INACTIVE:
            return

        self.status = RoleStatus.INACTIVE

    def archive(self) -> None:
        if self.status is RoleStatus.ARCHIVED:
            return

        self.status = RoleStatus.ARCHIVED

    def change_description(self, description: str | None) -> None:
        if description is None:
            self.description = None
            return

        self.description = self._normalize_description(description)

    def to_dict(self) -> dict[str, str | None]:
        return {
            "id": str(self.id),
            "role_code": str(self.role_code),
            "name": self.name,
            "description": self.description,
            "status": self.status.value,
            "valid_from": self.valid_from.isoformat(),
            "valid_to": self.valid_to.isoformat() if self.valid_to is not None else None,
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
            "status",
            "valid_from",
            "valid_to",
        }
        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise RoleSerializationError(
                f"data is missing required keys: {', '.join(missing)}"
            )

        try:
            valid_to_value = data["valid_to"]
            description_value = data["description"]
            return cls(
                id=RoleId(data["id"]),
                role_code=RoleCode(str(data["role_code"])),
                name=str(data["name"]),
                description=(None if description_value is None else str(description_value)),
                status=RoleStatus(str(data["status"]).upper()),
                valid_from=date.fromisoformat(str(data["valid_from"])),
                valid_to=(
                    date.fromisoformat(str(valid_to_value))
                    if valid_to_value is not None
                    else None
                ),
            )
        except Exception as exc:
            raise RoleSerializationError("Invalid serialized role") from exc

    @classmethod
    def _clear_registry_for_tests(cls) -> None:
        cls._code_registry.clear()
