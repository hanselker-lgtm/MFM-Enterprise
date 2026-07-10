"""Vessel aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar
from uuid import UUID

from mfm.domain.fleet.exceptions import DuplicateVesselRegistrationError
from mfm.domain.fleet.exceptions import InvalidVesselAssetIdError
from mfm.domain.fleet.exceptions import InvalidVesselNameError
from mfm.domain.fleet.exceptions import InvalidVesselStatusTransitionError
from mfm.domain.fleet.vessel_dimensions import VesselDimensions
from mfm.domain.fleet.vessel_id import VesselId
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.domain.fleet.vessel_status import VesselStatus


@dataclass(slots=True)
class Vessel:
    """Aggregate root for vessel identity and lifecycle."""

    _registration_registry: ClassVar[dict[str, VesselId]] = {}

    id: VesselId = field(default_factory=VesselId.new)
    asset_id: UUID = field(default_factory=UUID)
    registration: VesselRegistration = field(
        default_factory=lambda: VesselRegistration("UNSET")
    )
    name: str = ""
    shipyard: str = ""
    build_year: int | None = None
    construction_material: VesselMaterial = VesselMaterial.OTHER
    length: float = 1.0
    beam: float = 1.0
    draft: float = 1.0
    status: VesselStatus = VesselStatus.ACTIVE

    def __post_init__(self) -> None:
        if not isinstance(self.id, VesselId):
            self.id = VesselId(self.id)

        if not isinstance(self.asset_id, UUID):
            raise InvalidVesselAssetIdError("asset_id must be UUID")

        if not isinstance(self.registration, VesselRegistration):
            self.registration = VesselRegistration(str(self.registration))

        self.name = self._normalize_name(self.name)

        if not isinstance(self.shipyard, str):
            raise TypeError("shipyard must be a string")
        self.shipyard = self.shipyard.strip()

        if self.build_year is not None and (
            not isinstance(self.build_year, int) or self.build_year <= 0
        ):
            raise ValueError("build_year must be a positive integer or None")

        if not isinstance(self.construction_material, VesselMaterial):
            self.construction_material = VesselMaterial(
                str(self.construction_material).upper()
            )

        dimensions = VesselDimensions(
            length=float(self.length),
            beam=float(self.beam),
            draft=float(self.draft),
        )
        self.length = dimensions.length
        self.beam = dimensions.beam
        self.draft = dimensions.draft

        if not isinstance(self.status, VesselStatus):
            self.status = VesselStatus(str(self.status).upper())

        self._register_registration()

    @staticmethod
    def _normalize_name(value: str) -> str:
        if not isinstance(value, str):
            raise InvalidVesselNameError("name must be a string")

        normalized = value.strip()
        if not normalized:
            raise InvalidVesselNameError("name cannot be empty")

        return normalized

    def _register_registration(self) -> None:
        existing = self._registration_registry.get(self.registration.value)
        if existing is not None and existing != self.id:
            raise DuplicateVesselRegistrationError(
                f"registration {self.registration.value} already exists"
            )

        self._registration_registry[self.registration.value] = self.id

    def rename(self, name: str) -> None:
        normalized = self._normalize_name(name)
        if normalized == self.name:
            return
        self.name = normalized

    def change_registration(self, registration: VesselRegistration | str) -> None:
        updated = (
            registration
            if isinstance(registration, VesselRegistration)
            else VesselRegistration(str(registration))
        )

        if updated == self.registration:
            return

        existing = self._registration_registry.get(updated.value)
        if existing is not None and existing != self.id:
            raise DuplicateVesselRegistrationError(
                f"registration {updated.value} already exists"
            )

        self._registration_registry.pop(self.registration.value, None)
        self.registration = updated
        self._registration_registry[self.registration.value] = self.id

    def update_dimensions(self, dimensions: VesselDimensions) -> None:
        if not isinstance(dimensions, VesselDimensions):
            raise TypeError("dimensions must be VesselDimensions")

        self.length = dimensions.length
        self.beam = dimensions.beam
        self.draft = dimensions.draft

    def change_status(self, status: VesselStatus) -> None:
        if not isinstance(status, VesselStatus):
            status = VesselStatus(str(status).upper())

        if self.status is VesselStatus.RETIRED and status is not VesselStatus.RETIRED:
            raise InvalidVesselStatusTransitionError(
                "Retired vessel cannot be reactivated"
            )

        self.status = status

    @classmethod
    def _clear_registry_for_tests(cls) -> None:
        cls._registration_registry.clear()
