"""Mapper between asset domain aggregate and persistence models."""

from __future__ import annotations

from mfm.database.models.asset_location_model import AssetLocationModel
from mfm.database.models.asset_model import AssetModel
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_id import AssetId
from mfm.domain.asset.asset_location import AssetLocation
from mfm.domain.asset.asset_number import AssetNumber
from mfm.domain.asset.asset_status import AssetStatus


class AssetMapper:
    """Map between asset domain aggregate and SQLAlchemy models."""

    @staticmethod
    def to_orm_asset(asset: Asset) -> AssetModel:
        orm = AssetModel(
            id=asset.id.value,
            asset_number=asset.asset_number.value,
            name=asset.name,
            description=asset.description,
            category=asset.category,
            status=asset.status,
            owner_id=asset.owner_id,
            acquisition_date=asset.acquisition_date,
            retired_date=asset.retired_date,
            created_at=asset.created_at,
            updated_at=asset.updated_at,
        )
        orm.location = AssetLocationModel(
            asset_id=asset.id.value,
            value=asset.location.value,
        )
        return orm

    @staticmethod
    def to_domain_asset(orm: AssetModel) -> Asset:
        return Asset(
            id=AssetId(orm.id),
            asset_number=AssetNumber(orm.asset_number),
            name=orm.name,
            description=orm.description,
            category=AssetCategory(orm.category),
            status=AssetStatus(orm.status),
            owner_id=orm.owner_id,
            location=AssetLocation(orm.location.value),
            acquisition_date=orm.acquisition_date,
            retired_date=orm.retired_date,
            created_at=orm.created_at,
            updated_at=orm.updated_at,
        )
