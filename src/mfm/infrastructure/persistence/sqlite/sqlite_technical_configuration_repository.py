"""SQLite repository for TechnicalConfiguration aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from mfm.database.mappers.technical_configuration_mapper import (
    TechnicalConfigurationMapper,
)
from mfm.database.models.technical_component_model import TechnicalComponentModel
from mfm.database.models.technical_configuration_model import TechnicalConfigurationModel
from mfm.domain.technical_configuration.technical_configuration import (
    TechnicalConfiguration,
)
from mfm.repositories.technical_configuration_repository import (
    TechnicalConfigurationRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteTechnicalConfigurationRepository(TechnicalConfigurationRepository):
    """SQLAlchemy-backed repository for TechnicalConfiguration aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, configuration: TechnicalConfiguration) -> None:
        if self._session.scalar(
            select(TechnicalConfigurationModel).where(
                TechnicalConfigurationModel.vessel_id == configuration.vessel_id
            )
        ) is not None:
            raise ValueError(
                f"Technical configuration for vessel {configuration.vessel_id} already exists"
            )

        self._session.add(TechnicalConfigurationMapper.to_orm_configuration(configuration))
        self._session.flush()

    def get_by_id(self, configuration_id: UUID) -> TechnicalConfiguration | None:
        orm = self._session.scalar(
            select(TechnicalConfigurationModel)
            .options(*self._children_load_options())
            .where(TechnicalConfigurationModel.id == configuration_id)
        )
        if orm is None:
            return None
        return TechnicalConfigurationMapper.to_domain_configuration(orm)

    def get_by_vessel_id(self, vessel_id: UUID) -> TechnicalConfiguration | None:
        orm = self._session.scalar(
            select(TechnicalConfigurationModel)
            .options(*self._children_load_options())
            .where(TechnicalConfigurationModel.vessel_id == vessel_id)
        )
        if orm is None:
            return None
        return TechnicalConfigurationMapper.to_domain_configuration(orm)

    def update(self, configuration: TechnicalConfiguration) -> None:
        orm = self._session.scalar(
            select(TechnicalConfigurationModel)
            .options(*self._children_load_options())
            .where(TechnicalConfigurationModel.id == configuration.id.value)
        )
        if orm is None:
            raise ValueError(
                f"TechnicalConfiguration {configuration.id.value} does not exist"
            )

        if orm.vessel_id != configuration.vessel_id:
            duplicate = self._session.scalar(
                select(TechnicalConfigurationModel).where(
                    TechnicalConfigurationModel.vessel_id == configuration.vessel_id,
                    TechnicalConfigurationModel.id != configuration.id.value,
                )
            )
            if duplicate is not None:
                raise ValueError(
                    f"Technical configuration for vessel {configuration.vessel_id} already exists"
                )

        self._session.merge(
            TechnicalConfigurationMapper.to_orm_configuration(configuration)
        )
        self._session.flush()

    def delete(self, configuration_id: UUID) -> None:
        orm = self._session.get(TechnicalConfigurationModel, configuration_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, configuration_id: UUID) -> bool:
        return self._session.get(TechnicalConfigurationModel, configuration_id) is not None

    def list(self) -> list[TechnicalConfiguration]:
        orm_entities = self._session.scalars(
            select(TechnicalConfigurationModel).options(*self._children_load_options())
        ).unique().all()
        return [
            TechnicalConfigurationMapper.to_domain_configuration(orm)
            for orm in orm_entities
        ]

    def search(self, text: str) -> list[TechnicalConfiguration]:
        query = f"%{text}%"
        orm_entities = self._session.scalars(
            select(TechnicalConfigurationModel)
            .outerjoin(
                TechnicalComponentModel,
                TechnicalComponentModel.technical_configuration_id
                == TechnicalConfigurationModel.id,
            )
            .options(*self._children_load_options())
            .where(
                or_(
                    TechnicalComponentModel.name.ilike(query),
                    TechnicalComponentModel.manufacturer.ilike(query),
                    TechnicalComponentModel.model.ilike(query),
                    TechnicalComponentModel.serial_number.ilike(query),
                    TechnicalComponentModel.specification_schema_key.ilike(query),
                )
            )
        ).unique().all()

        return [
            TechnicalConfigurationMapper.to_domain_configuration(orm)
            for orm in orm_entities
        ]

    @staticmethod
    def _children_load_options() -> tuple[object, ...]:
        return (
            selectinload(TechnicalConfigurationModel.components),
            selectinload(TechnicalConfigurationModel.links),
            selectinload(TechnicalConfigurationModel.replacements),
        )
