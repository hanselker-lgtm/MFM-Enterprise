from __future__ import annotations

from dataclasses import FrozenInstanceError
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.fleet.exceptions import DuplicateVesselRegistrationError
from mfm.domain.fleet.exceptions import InvalidVesselAssetIdError
from mfm.domain.fleet.exceptions import InvalidVesselDimensionsError
from mfm.domain.fleet.exceptions import InvalidVesselNameError
from mfm.domain.fleet.exceptions import InvalidVesselStatusTransitionError
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_dimensions import VesselDimensions
from mfm.domain.fleet.vessel_id import VesselId
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.domain.fleet.vessel_status import VesselStatus


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Vessel._clear_registry_for_tests()


def _create_vessel(registration: str = "OY-FLEET-001") -> Vessel:
    return Vessel(
        asset_id=uuid4(),
        registration=VesselRegistration(registration),
        name="Northern Star",
        shipyard="Odense",
        build_year=2005,
        construction_material=VesselMaterial.STEEL,
        length=32.5,
        beam=7.2,
        draft=2.6,
        status=VesselStatus.ACTIVE,
    )


def test_create_vessel() -> None:
    vessel = _create_vessel()

    assert isinstance(vessel.id, VesselId)
    assert isinstance(vessel.id.value, UUID)
    assert isinstance(vessel.asset_id, UUID)
    assert vessel.registration == VesselRegistration("OY-FLEET-001")
    assert vessel.name == "Northern Star"
    assert vessel.shipyard == "Odense"
    assert vessel.build_year == 2005
    assert vessel.construction_material is VesselMaterial.STEEL
    assert vessel.length == 32.5
    assert vessel.beam == 7.2
    assert vessel.draft == 2.6
    assert vessel.status is VesselStatus.ACTIVE


def test_asset_id_is_required() -> None:
    with pytest.raises(InvalidVesselAssetIdError):
        Vessel(
            asset_id="bad",  # type: ignore[arg-type]
            registration=VesselRegistration("OY-FLEET-010"),
            name="Invalid",
            shipyard="Yard",
            build_year=2001,
            construction_material=VesselMaterial.OTHER,
            length=10.0,
            beam=3.0,
            draft=1.2,
            status=VesselStatus.ACTIVE,
        )


def test_registration_must_be_unique() -> None:
    _ = _create_vessel("OY-FLEET-002")

    with pytest.raises(DuplicateVesselRegistrationError):
        _ = _create_vessel("oy-fleet-002")


def test_name_must_not_be_empty() -> None:
    with pytest.raises(InvalidVesselNameError):
        Vessel(
            asset_id=uuid4(),
            registration=VesselRegistration("OY-FLEET-011"),
            name="   ",
            shipyard="Yard",
            build_year=2001,
            construction_material=VesselMaterial.OTHER,
            length=10.0,
            beam=3.0,
            draft=1.2,
            status=VesselStatus.ACTIVE,
        )


def test_dimensions_must_be_positive() -> None:
    with pytest.raises(InvalidVesselDimensionsError):
        VesselDimensions(length=0.0, beam=4.0, draft=1.0)

    with pytest.raises(InvalidVesselDimensionsError):
        _ = Vessel(
            asset_id=uuid4(),
            registration=VesselRegistration("OY-FLEET-012"),
            name="Bad Dimensions",
            shipyard="Yard",
            build_year=2001,
            construction_material=VesselMaterial.OTHER,
            length=10.0,
            beam=-1.0,
            draft=1.2,
            status=VesselStatus.ACTIVE,
        )


def test_rename() -> None:
    vessel = _create_vessel("OY-FLEET-003")

    vessel.rename("  Northern Queen  ")

    assert vessel.name == "Northern Queen"


def test_change_registration() -> None:
    vessel = _create_vessel("OY-FLEET-004")

    vessel.change_registration("oy-fleet-050")

    assert vessel.registration == VesselRegistration("OY-FLEET-050")


def test_change_registration_rejects_duplicates() -> None:
    _ = _create_vessel("OY-FLEET-005")
    vessel = _create_vessel("OY-FLEET-006")

    with pytest.raises(DuplicateVesselRegistrationError):
        vessel.change_registration("OY-FLEET-005")


def test_update_dimensions() -> None:
    vessel = _create_vessel("OY-FLEET-007")

    vessel.update_dimensions(VesselDimensions(length=40.0, beam=8.5, draft=3.0))

    assert vessel.length == 40.0
    assert vessel.beam == 8.5
    assert vessel.draft == 3.0


def test_change_status() -> None:
    vessel = _create_vessel("OY-FLEET-008")

    vessel.change_status(VesselStatus.LAID_UP)
    assert vessel.status is VesselStatus.LAID_UP

    vessel.change_status(VesselStatus.RESTORATION)
    assert vessel.status is VesselStatus.RESTORATION

    vessel.change_status(VesselStatus.RETIRED)
    assert vessel.status is VesselStatus.RETIRED


def test_retired_cannot_be_activated_again() -> None:
    vessel = _create_vessel("OY-FLEET-009")
    vessel.change_status(VesselStatus.RETIRED)

    with pytest.raises(InvalidVesselStatusTransitionError):
        vessel.change_status(VesselStatus.ACTIVE)

    with pytest.raises(InvalidVesselStatusTransitionError):
        vessel.change_status(VesselStatus.LAID_UP)


def test_value_objects_are_immutable() -> None:
    vessel_id = VesselId.new()
    registration = VesselRegistration("OY-FLEET-200")
    dimensions = VesselDimensions(length=12.0, beam=4.0, draft=1.8)

    with pytest.raises(FrozenInstanceError):
        vessel_id.value = uuid4()  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        registration.value = "OY-FLEET-201"  # type: ignore[misc]

    with pytest.raises(FrozenInstanceError):
        dimensions.length = 20.0  # type: ignore[misc]
