"""Asset aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import date
from datetime import datetime
from typing import Any
from typing import ClassVar
from typing import Mapping
from uuid import UUID

from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_id import AssetId
from mfm.domain.asset.asset_location import AssetLocation
from mfm.domain.asset.asset_number import AssetNumber
from mfm.domain.asset.asset_status import AssetStatus
from mfm.domain.asset.exceptions import AssetSerializationError
from mfm.domain.asset.exceptions import DuplicateAssetNumberError
from mfm.domain.asset.exceptions import InvalidAssetDateError
from mfm.domain.asset.exceptions import InvalidAssetNameError
from mfm.domain.asset.exceptions import InvalidAssetOwnerError
from mfm.domain.asset.exceptions import InvalidAssetStatusTransitionError


@dataclass(slots=True)
class Asset:
    """Aggregate root for a generic asset lifecycle."""

    _number_registry: ClassVar[dict[str, AssetId]] = {}

    id: AssetId = field(default_factory=AssetId.new)
    asset_number: AssetNumber = field(default_factory=lambda: AssetNumber("ASSET-UNSET"))
    name: str = ""
    description: str = ""
    category: AssetCategory = AssetCategory.OTHER
    status: AssetStatus = AssetStatus.ACTIVE
    owner_id: UUID | None = None
    location: AssetLocation = field(default_factory=lambda: AssetLocation("UNSPECIFIED"))
    acquisition_date: date | None = None
    retired_date: date | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not isinstance(self.id, AssetId):
            self.id = AssetId(self.id)

        if not isinstance(self.asset_number, AssetNumber):
            self.asset_number = AssetNumber(str(self.asset_number))

        self.name = self._normalize_name(self.name)

        if not isinstance(self.description, str):
            raise TypeError("description must be a string")
        self.description = self.description.strip()

        if not isinstance(self.category, AssetCategory):
            self.category = AssetCategory(str(self.category).upper())

        if not isinstance(self.status, AssetStatus):
            self.status = AssetStatus(str(self.status).upper())

        if self.owner_id is not None and not isinstance(self.owner_id, UUID):
            raise InvalidAssetOwnerError("owner_id must be UUID or None")

        if not isinstance(self.location, AssetLocation):
            self.location = AssetLocation(str(self.location))

        if self.acquisition_date is not None and not isinstance(self.acquisition_date, date):
            raise InvalidAssetDateError("acquisition_date must be date or None")

        if self.retired_date is not None and not isinstance(self.retired_date, date):
            raise InvalidAssetDateError("retired_date must be date or None")

        if self.retired_date is not None and self.acquisition_date is not None:
            if self.retired_date < self.acquisition_date:
                raise InvalidAssetDateError("retired_date cannot be before acquisition_date")

        if self.status is AssetStatus.RETIRED and self.retired_date is None:
            raise InvalidAssetDateError("retired assets must have retired_date")

        if not isinstance(self.created_at, datetime):
            raise TypeError("created_at must be datetime")

        if not isinstance(self.updated_at, datetime):
            raise TypeError("updated_at must be datetime")

        self.created_at = self._as_utc(self.created_at)
        self.updated_at = self._as_utc(self.updated_at)
        if self.updated_at < self.created_at:
            self.updated_at = self.created_at

        self._register_asset_number()

    @staticmethod
    def _normalize_name(value: str) -> str:
        if not isinstance(value, str):
            raise InvalidAssetNameError("name must be a string")

        normalized = value.strip()
        if not normalized:
            raise InvalidAssetNameError("name cannot be empty")

        return normalized

    @staticmethod
    def _as_utc(value: datetime) -> datetime:
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

    def _register_asset_number(self) -> None:
        existing = self._number_registry.get(self.asset_number.value)
        if existing is not None and existing != self.id:
            raise DuplicateAssetNumberError(
                f"asset_number {self.asset_number.value} already exists"
            )

        self._number_registry[self.asset_number.value] = self.id

    def _touch(self) -> None:
        self.updated_at = datetime.now(UTC)

    def rename(self, new_name: str) -> None:
        normalized = self._normalize_name(new_name)
        if normalized == self.name:
            return

        self.name = normalized
        self._touch()

    def change_location(self, new_location: AssetLocation | str) -> None:
        location = (
            new_location
            if isinstance(new_location, AssetLocation)
            else AssetLocation(str(new_location))
        )

        if location == self.location:
            return

        self.location = location
        self._touch()

    def change_owner(self, owner_id: UUID | None) -> None:
        if owner_id is not None and not isinstance(owner_id, UUID):
            raise InvalidAssetOwnerError("owner_id must be UUID or None")

        if owner_id == self.owner_id:
            return

        self.owner_id = owner_id
        self._touch()

    def retire(self, retired_on: date) -> None:
        if self.status is AssetStatus.DISPOSED:
            raise InvalidAssetStatusTransitionError("Disposed asset cannot be retired")

        if not isinstance(retired_on, date):
            raise InvalidAssetDateError("retired_on must be a date")

        if self.acquisition_date is not None and retired_on < self.acquisition_date:
            raise InvalidAssetDateError("retired_date cannot be before acquisition_date")

        if self.status is AssetStatus.RETIRED and self.retired_date == retired_on:
            return

        self.status = AssetStatus.RETIRED
        self.retired_date = retired_on
        self._touch()

    def dispose(self, disposed_on: date | None = None) -> None:
        if self.status is AssetStatus.DISPOSED:
            return

        effective = disposed_on or self.retired_date or datetime.now(UTC).date()
        if not isinstance(effective, date):
            raise InvalidAssetDateError("disposed_on must be a date")

        if self.acquisition_date is not None and effective < self.acquisition_date:
            raise InvalidAssetDateError("retired_date cannot be before acquisition_date")

        self.status = AssetStatus.DISPOSED
        self.retired_date = effective
        self._touch()

    def activate(self) -> None:
        if self.status is AssetStatus.DISPOSED:
            raise InvalidAssetStatusTransitionError("Disposed asset cannot be activated")

        if self.status is AssetStatus.ACTIVE:
            return

        self.status = AssetStatus.ACTIVE
        self.retired_date = None
        self._touch()

    def deactivate(self) -> None:
        if self.status is AssetStatus.DISPOSED:
            raise InvalidAssetStatusTransitionError("Disposed asset cannot be deactivated")

        if self.status is AssetStatus.INACTIVE:
            return

        self.status = AssetStatus.INACTIVE
        self._touch()

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "asset_number": str(self.asset_number),
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "status": self.status.value,
            "owner_id": str(self.owner_id) if self.owner_id is not None else None,
            "location": str(self.location),
            "acquisition_date": (
                self.acquisition_date.isoformat() if self.acquisition_date is not None else None
            ),
            "retired_date": (
                self.retired_date.isoformat() if self.retired_date is not None else None
            ),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "Asset":
        if not isinstance(data, Mapping):
            raise AssetSerializationError("data must be a mapping")

        required = {
            "id",
            "asset_number",
            "name",
            "description",
            "category",
            "status",
            "owner_id",
            "location",
            "acquisition_date",
            "retired_date",
            "created_at",
            "updated_at",
        }
        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise AssetSerializationError(
                f"data is missing required keys: {', '.join(missing)}"
            )

        try:
            owner_value = data["owner_id"]
            acquisition_value = data["acquisition_date"]
            retired_value = data["retired_date"]

            return cls(
                id=AssetId(data["id"]),
                asset_number=AssetNumber(str(data["asset_number"])),
                name=str(data["name"]),
                description=str(data["description"]),
                category=AssetCategory(str(data["category"]).upper()),
                status=AssetStatus(str(data["status"]).upper()),
                owner_id=(UUID(str(owner_value)) if owner_value is not None else None),
                location=AssetLocation(str(data["location"])),
                acquisition_date=(
                    date.fromisoformat(str(acquisition_value))
                    if acquisition_value is not None
                    else None
                ),
                retired_date=(
                    date.fromisoformat(str(retired_value))
                    if retired_value is not None
                    else None
                ),
                created_at=datetime.fromisoformat(str(data["created_at"])),
                updated_at=datetime.fromisoformat(str(data["updated_at"])),
            )
        except Exception as exc:
            raise AssetSerializationError("Invalid serialized asset") from exc

    @classmethod
    def _clear_registry_for_tests(cls) -> None:
        cls._number_registry.clear()
