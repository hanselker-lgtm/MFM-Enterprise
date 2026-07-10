"""SQLite repository for Asset aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.database.mappers.asset_mapper import AssetMapper
from mfm.database.models.asset_location_model import AssetLocationModel
from mfm.database.models.asset_model import AssetModel
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_number import AssetNumber
from mfm.repositories.asset_repository import AssetRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteAssetRepository(AssetRepository):
    """SQLAlchemy-backed repository for Asset aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, asset: Asset) -> None:
        if self._session.scalar(
            select(AssetModel).where(AssetModel.asset_number == asset.asset_number.value)
        ) is not None:
            raise ValueError(f"Asset number {asset.asset_number.value} already exists")

        self._session.add(AssetMapper.to_orm_asset(asset))
        self._session.flush()

    def get_by_id(self, asset_id: UUID) -> Asset | None:
        orm = self._session.scalar(
            select(AssetModel)
            .options(joinedload(AssetModel.location))
            .where(AssetModel.id == asset_id)
        )
        if orm is None:
            return None
        return AssetMapper.to_domain_asset(orm)

    def get_by_asset_number(self, asset_number: str) -> Asset | None:
        normalized = AssetNumber(asset_number).value
        orm = self._session.scalar(
            select(AssetModel)
            .options(joinedload(AssetModel.location))
            .where(AssetModel.asset_number == normalized)
        )
        if orm is None:
            return None
        return AssetMapper.to_domain_asset(orm)

    def update(self, asset: Asset) -> None:
        orm = self._session.scalar(
            select(AssetModel)
            .options(joinedload(AssetModel.location))
            .where(AssetModel.id == asset.id.value)
        )
        if orm is None:
            raise ValueError(f"Asset {asset.id.value} does not exist")

        if orm.asset_number != asset.asset_number.value:
            duplicate = self._session.scalar(
                select(AssetModel).where(
                    AssetModel.asset_number == asset.asset_number.value,
                    AssetModel.id != asset.id.value,
                )
            )
            if duplicate is not None:
                raise ValueError(f"Asset number {asset.asset_number.value} already exists")

        orm.asset_number = asset.asset_number.value
        orm.name = asset.name
        orm.description = asset.description
        orm.category = asset.category
        orm.status = asset.status
        orm.owner_id = asset.owner_id
        orm.acquisition_date = asset.acquisition_date
        orm.retired_date = asset.retired_date
        orm.created_at = asset.created_at
        orm.updated_at = asset.updated_at

        if orm.location is None:
            orm.location = AssetLocationModel(asset_id=asset.id.value, value=asset.location.value)
        else:
            orm.location.value = asset.location.value

        self._session.flush()

    def delete(self, asset_id: UUID) -> None:
        orm = self._session.get(AssetModel, asset_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, asset_id: UUID) -> bool:
        return self._session.get(AssetModel, asset_id) is not None

    def list(self) -> list[Asset]:
        orm_entities = self._session.scalars(
            select(AssetModel).options(joinedload(AssetModel.location))
        ).unique().all()
        return [AssetMapper.to_domain_asset(orm) for orm in orm_entities]

    def search(self, text: str) -> list[Asset]:
        query = f"%{text}%"
        orm_entities = self._session.scalars(
            select(AssetModel)
            .outerjoin(AssetLocationModel, AssetLocationModel.asset_id == AssetModel.id)
            .options(joinedload(AssetModel.location))
            .where(
                or_(
                    AssetModel.asset_number.ilike(query),
                    AssetModel.name.ilike(query),
                    AssetModel.description.ilike(query),
                    AssetLocationModel.value.ilike(query),
                )
            )
        ).unique().all()
        return [AssetMapper.to_domain_asset(orm) for orm in orm_entities]
