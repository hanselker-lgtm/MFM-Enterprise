"""SQLite repository for Organization aggregates."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.organization_mapper import OrganizationMapper
from mfm.database.models.organization_model import OrganizationModel
from mfm.domain.organization.organization import Organization
from mfm.repositories.organization_repository import OrganizationRepository


class SQLiteOrganizationRepository(OrganizationRepository):
    """SQLAlchemy-backed repository for Organization aggregates."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, organization: Organization) -> None:
        if self._session.scalar(
            select(OrganizationModel).where(
                OrganizationModel.organization_number
                == organization.organization_number.value
            )
        ) is not None:
            raise ValueError(
                f"Organization number {organization.organization_number.value} already exists"
            )

        self._session.add(OrganizationMapper.to_orm_organization(organization))
        self._session.flush()

    def get_by_id(self, organization_id: UUID) -> Organization | None:
        orm = self._session.scalar(
            select(OrganizationModel).where(OrganizationModel.id == organization_id)
        )
        if orm is None:
            return None
        return OrganizationMapper.to_domain_organization(orm)

    def update(self, organization: Organization) -> None:
        orm = self._session.get(OrganizationModel, organization.id.value)
        if orm is None:
            raise ValueError(f"Organization {organization.id.value} does not exist")

        if orm.organization_number != organization.organization_number.value:
            duplicate = self._session.scalar(
                select(OrganizationModel).where(
                    OrganizationModel.organization_number
                    == organization.organization_number.value,
                    OrganizationModel.id != organization.id.value,
                )
            )
            if duplicate is not None:
                raise ValueError(
                    f"Organization number {organization.organization_number.value} already exists"
                )

        orm.organization_number = organization.organization_number.value
        orm.name = organization.name
        orm.organization_type = organization.organization_type
        orm.status = organization.status
        orm.created_at = organization.created_at
        orm.updated_at = organization.updated_at
        self._session.flush()

    def delete(self, organization_id: UUID) -> None:
        orm = self._session.get(OrganizationModel, organization_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, organization_id: UUID) -> bool:
        return self._session.get(OrganizationModel, organization_id) is not None

    def list(self) -> list[Organization]:
        orm_entities = self._session.scalars(select(OrganizationModel)).all()
        return [OrganizationMapper.to_domain_organization(orm) for orm in orm_entities]

    def search(self, text: str) -> list[Organization]:
        query = f"%{text}%"
        orm_entities = self._session.scalars(
            select(OrganizationModel).where(
                or_(
                    OrganizationModel.organization_number.ilike(query),
                    OrganizationModel.name.ilike(query),
                )
            )
        ).all()
        return [OrganizationMapper.to_domain_organization(orm) for orm in orm_entities]
