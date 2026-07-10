"""Organization aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from typing import Any
from typing import ClassVar
from typing import Mapping

from mfm.domain.organization.exceptions import DuplicateOrganizationNumberError
from mfm.domain.organization.exceptions import InvalidOrganizationNameError
from mfm.domain.organization.exceptions import InvalidOrganizationStatusTransitionError
from mfm.domain.organization.exceptions import OrganizationSerializationError
from mfm.domain.organization.organization_id import OrganizationId
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType


@dataclass(slots=True)
class Organization:
    """Aggregate root for organizational identity and lifecycle."""

    _number_registry: ClassVar[dict[str, OrganizationId]] = {}

    id: OrganizationId = field(default_factory=OrganizationId.new)
    organization_number: OrganizationNumber = field(
        default_factory=lambda: OrganizationNumber("ORG-UNSET")
    )
    name: str = ""
    organization_type: OrganizationType = OrganizationType.OTHER
    status: OrganizationStatus = OrganizationStatus.ACTIVE
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if not isinstance(self.organization_number, OrganizationNumber):
            self.organization_number = OrganizationNumber(str(self.organization_number))

        self.name = self._normalize_name(self.name)

        if not isinstance(self.organization_type, OrganizationType):
            self.organization_type = OrganizationType(str(self.organization_type).upper())

        if not isinstance(self.status, OrganizationStatus):
            self.status = OrganizationStatus(str(self.status).upper())

        if not isinstance(self.created_at, datetime):
            raise TypeError("created_at must be datetime")

        if not isinstance(self.updated_at, datetime):
            raise TypeError("updated_at must be datetime")

        self.created_at = self._as_utc(self.created_at)
        self.updated_at = self._as_utc(self.updated_at)
        if self.updated_at < self.created_at:
            self.updated_at = self.created_at

        self._register_organization_number()

    @staticmethod
    def _normalize_name(value: str) -> str:
        if not isinstance(value, str):
            raise InvalidOrganizationNameError("name must be a string")

        normalized = value.strip()
        if not normalized:
            raise InvalidOrganizationNameError("name cannot be empty")

        return normalized

    @staticmethod
    def _as_utc(value: datetime) -> datetime:
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

    def _register_organization_number(self) -> None:
        existing = self._number_registry.get(self.organization_number.value)
        if existing is not None and existing != self.id:
            raise DuplicateOrganizationNumberError(
                f"organization_number {self.organization_number.value} already exists"
            )

        self._number_registry[self.organization_number.value] = self.id

    def _touch(self) -> None:
        self.updated_at = datetime.now(UTC)

    def rename(self, new_name: str) -> None:
        normalized = self._normalize_name(new_name)
        if normalized == self.name:
            return

        self.name = normalized
        self._touch()

    def activate(self) -> None:
        if self.status is OrganizationStatus.ARCHIVED:
            raise InvalidOrganizationStatusTransitionError(
                "Archived organization cannot be activated"
            )

        if self.status is OrganizationStatus.ACTIVE:
            return

        self.status = OrganizationStatus.ACTIVE
        self._touch()

    def deactivate(self) -> None:
        if self.status is OrganizationStatus.ARCHIVED:
            raise InvalidOrganizationStatusTransitionError(
                "Archived organization cannot be deactivated"
            )

        if self.status is OrganizationStatus.INACTIVE:
            return

        self.status = OrganizationStatus.INACTIVE
        self._touch()

    def archive(self) -> None:
        if self.status is OrganizationStatus.ARCHIVED:
            return

        self.status = OrganizationStatus.ARCHIVED
        self._touch()

    def to_dict(self) -> dict[str, str]:
        return {
            "id": str(self.id),
            "organization_number": str(self.organization_number),
            "name": self.name,
            "organization_type": self.organization_type.value,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "Organization":
        if not isinstance(data, Mapping):
            raise OrganizationSerializationError("data must be a mapping")

        required = {
            "id",
            "organization_number",
            "name",
            "organization_type",
            "status",
            "created_at",
            "updated_at",
        }

        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise OrganizationSerializationError(
                f"data is missing required keys: {', '.join(missing)}"
            )

        try:
            return cls(
                id=OrganizationId(data["id"]),
                organization_number=OrganizationNumber(str(data["organization_number"])),
                name=str(data["name"]),
                organization_type=OrganizationType(str(data["organization_type"]).upper()),
                status=OrganizationStatus(str(data["status"]).upper()),
                created_at=datetime.fromisoformat(str(data["created_at"])),
                updated_at=datetime.fromisoformat(str(data["updated_at"])),
            )
        except Exception as exc:
            raise OrganizationSerializationError("Invalid serialized organization") from exc

    @classmethod
    def _clear_registry_for_tests(cls) -> None:
        cls._number_registry.clear()
