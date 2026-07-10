from __future__ import annotations

from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_id import AssetId
from mfm.domain.asset.asset_location import AssetLocation
from mfm.domain.asset.asset_number import AssetNumber
from mfm.domain.asset.asset_status import AssetStatus
from mfm.domain.asset.exceptions import AssetSerializationError
from mfm.domain.asset.exceptions import DuplicateAssetNumberError
from mfm.domain.asset.exceptions import InvalidAssetDateError
from mfm.domain.asset.exceptions import InvalidAssetNameError
from mfm.domain.asset.exceptions import InvalidAssetStatusTransitionError


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Asset._clear_registry_for_tests()


def test_create_asset() -> None:
    asset = Asset(
        asset_number=AssetNumber("asset-1000"),
        name="  Main Asset  ",
        description="  Generic asset  ",
        category=AssetCategory.OTHER,
        location=AssetLocation("HQ Warehouse"),
        acquisition_date=date(2026, 1, 1),
    )

    assert isinstance(asset.id, AssetId)
    assert isinstance(asset.id.value, UUID)
    assert asset.asset_number == AssetNumber("ASSET-1000")
    assert asset.name == "Main Asset"
    assert asset.description == "Generic asset"
    assert asset.category is AssetCategory.OTHER
    assert asset.status is AssetStatus.ACTIVE
    assert asset.retired_date is None
    assert asset.created_at.tzinfo == UTC
    assert asset.updated_at.tzinfo == UTC


def test_rename() -> None:
    asset = Asset(
        asset_number=AssetNumber("ASSET-1001"),
        name="Before",
        category=AssetCategory.TOOL,
        location=AssetLocation("Shed"),
    )

    before = asset.updated_at
    asset.rename("  After  ")

    assert asset.name == "After"
    assert asset.updated_at >= before


def test_relocate() -> None:
    asset = Asset(
        asset_number=AssetNumber("ASSET-1002"),
        name="Movable",
        category=AssetCategory.EQUIPMENT,
        location=AssetLocation("Site A"),
    )

    asset.change_location("Site B")

    assert asset.location == AssetLocation("Site B")


def test_transfer_ownership() -> None:
    asset = Asset(
        asset_number=AssetNumber("ASSET-1003"),
        name="Owned",
        category=AssetCategory.BUILDING,
        location=AssetLocation("Harbor"),
    )

    owner_id = uuid4()
    asset.change_owner(owner_id)

    assert asset.owner_id == owner_id

    asset.change_owner(None)
    assert asset.owner_id is None


def test_retire() -> None:
    asset = Asset(
        asset_number=AssetNumber("ASSET-1004"),
        name="To Retire",
        category=AssetCategory.ENGINE,
        location=AssetLocation("Dock"),
        acquisition_date=date(2020, 1, 1),
    )

    asset.retire(date(2026, 1, 15))

    assert asset.status is AssetStatus.RETIRED
    assert asset.retired_date == date(2026, 1, 15)


def test_dispose() -> None:
    asset = Asset(
        asset_number=AssetNumber("ASSET-1005"),
        name="To Dispose",
        category=AssetCategory.VESSEL,
        location=AssetLocation("Slipway"),
        acquisition_date=date(2018, 1, 1),
    )

    asset.dispose(date(2026, 2, 1))

    assert asset.status is AssetStatus.DISPOSED
    assert asset.retired_date == date(2026, 2, 1)


def test_invalid_transitions() -> None:
    with pytest.raises(InvalidAssetDateError):
        Asset(
            asset_number=AssetNumber("ASSET-1006"),
            name="Invalid Retired",
            category=AssetCategory.OTHER,
            status=AssetStatus.RETIRED,
            location=AssetLocation("HQ"),
            retired_date=None,
        )

    disposed = Asset(
        asset_number=AssetNumber("ASSET-1007"),
        name="Disposed",
        category=AssetCategory.OTHER,
        status=AssetStatus.DISPOSED,
        location=AssetLocation("Yard"),
        retired_date=date(2025, 1, 1),
    )

    with pytest.raises(InvalidAssetStatusTransitionError):
        disposed.activate()

    with pytest.raises(InvalidAssetStatusTransitionError):
        disposed.deactivate()



def test_asset_number_uniqueness() -> None:
    _ = Asset(
        asset_number=AssetNumber("ASSET-1008"),
        name="A",
        category=AssetCategory.OTHER,
        location=AssetLocation("HQ"),
    )

    with pytest.raises(DuplicateAssetNumberError):
        Asset(
            asset_number=AssetNumber("asset-1008"),
            name="B",
            category=AssetCategory.TOOL,
            location=AssetLocation("HQ"),
        )


def test_empty_name_is_invalid() -> None:
    with pytest.raises(InvalidAssetNameError):
        Asset(
            asset_number=AssetNumber("ASSET-1009"),
            name="   ",
            category=AssetCategory.OTHER,
            location=AssetLocation("HQ"),
        )


def test_equality() -> None:
    asset_id = AssetId.new()
    owner_id = uuid4()
    created_at = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
    updated_at = datetime(2026, 1, 2, 0, 0, tzinfo=UTC)

    left = Asset(
        id=asset_id,
        asset_number=AssetNumber("ASSET-1010"),
        name="Equal",
        description="Same",
        category=AssetCategory.EQUIPMENT,
        status=AssetStatus.INACTIVE,
        owner_id=owner_id,
        location=AssetLocation("A"),
        acquisition_date=date(2020, 1, 1),
        retired_date=None,
        created_at=created_at,
        updated_at=updated_at,
    )
    right = Asset(
        id=asset_id,
        asset_number=AssetNumber("ASSET-1010"),
        name="Equal",
        description="Same",
        category=AssetCategory.EQUIPMENT,
        status=AssetStatus.INACTIVE,
        owner_id=owner_id,
        location=AssetLocation("A"),
        acquisition_date=date(2020, 1, 1),
        retired_date=None,
        created_at=created_at,
        updated_at=updated_at,
    )

    assert left == right


def test_serialization_round_trip() -> None:
    asset = Asset(
        asset_number=AssetNumber("ASSET-1011"),
        name="Serializable",
        description="Round trip",
        category=AssetCategory.TOOL,
        status=AssetStatus.INACTIVE,
        owner_id=uuid4(),
        location=AssetLocation("Depot"),
        acquisition_date=date(2024, 1, 1),
    )

    payload = asset.to_dict()
    restored = Asset.from_dict(payload)

    assert restored == asset
    assert restored.asset_number == AssetNumber("ASSET-1011")



def test_serialization_rejects_invalid_data() -> None:
    with pytest.raises(AssetSerializationError):
        Asset.from_dict({"name": "missing fields"})
