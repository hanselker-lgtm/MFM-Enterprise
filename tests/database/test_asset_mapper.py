from __future__ import annotations

from datetime import date
from uuid import uuid4

from mfm.database.mappers.asset_mapper import AssetMapper
from mfm.database.models.asset_location_model import AssetLocationModel
from mfm.database.models.asset_model import AssetModel
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_location import AssetLocation
from mfm.domain.asset.asset_number import AssetNumber
from mfm.domain.asset.asset_status import AssetStatus


def test_asset_mapper_roundtrip() -> None:
    asset = Asset(
        asset_number=AssetNumber("ASSET-M-001"),
        name="Mapper Asset",
        description="Roundtrip",
        category=AssetCategory.ENGINE,
        status=AssetStatus.ACTIVE,
        owner_id=uuid4(),
        location=AssetLocation("Engine Hall"),
        acquisition_date=date(2024, 6, 1),
    )

    orm = AssetMapper.to_orm_asset(asset)

    assert isinstance(orm, AssetModel)
    assert orm.id == asset.id.value
    assert orm.asset_number == "ASSET-M-001"
    assert isinstance(orm.location, AssetLocationModel)
    assert orm.location.value == "Engine Hall"

    restored = AssetMapper.to_domain_asset(orm)

    assert restored == asset
    assert restored.location == AssetLocation("Engine Hall")
