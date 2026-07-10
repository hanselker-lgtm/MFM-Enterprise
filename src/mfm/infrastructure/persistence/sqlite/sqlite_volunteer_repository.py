"""SQLite repository for Volunteer aggregates."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.organization_mapper import OrganizationMapper
from mfm.database.models.volunteer_model import VolunteerModel
from mfm.domain.organization.volunteer import Volunteer
from mfm.repositories.volunteer_repository import VolunteerRepository


class SQLiteVolunteerRepository(VolunteerRepository):
    """SQLAlchemy-backed repository for Volunteer aggregates."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, volunteer: Volunteer) -> None:
        self._session.add(OrganizationMapper.to_orm_volunteer(volunteer))
        self._session.flush()

    def get_by_id(self, volunteer_id: UUID) -> Volunteer | None:
        orm = self._session.scalar(
            select(VolunteerModel).where(VolunteerModel.id == volunteer_id)
        )
        if orm is None:
            return None
        return OrganizationMapper.to_domain_volunteer(orm)

    def update(self, volunteer: Volunteer) -> None:
        orm = self._session.get(VolunteerModel, volunteer.id.value)
        if orm is None:
            raise ValueError(f"Volunteer {volunteer.id.value} does not exist")

        mapped = OrganizationMapper.to_orm_volunteer(volunteer)

        orm.contact_id = mapped.contact_id
        orm.member_id = mapped.member_id
        orm.status = mapped.status
        orm.joined_at = mapped.joined_at
        orm.left_at = mapped.left_at
        orm.is_available = mapped.is_available
        orm.max_hours_per_week = mapped.max_hours_per_week
        orm.preferred_days = mapped.preferred_days
        orm.skills = mapped.skills
        orm.certificates = mapped.certificates
        self._session.flush()

    def delete(self, volunteer_id: UUID) -> None:
        orm = self._session.get(VolunteerModel, volunteer_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, volunteer_id: UUID) -> bool:
        return self._session.get(VolunteerModel, volunteer_id) is not None

    def list(self) -> list[Volunteer]:
        orm_entities = self._session.scalars(select(VolunteerModel)).all()
        return [OrganizationMapper.to_domain_volunteer(orm) for orm in orm_entities]

    def search(self, text: str) -> list[Volunteer]:
        query = f"%{text}%"
        orm_entities = self._session.scalars(
            select(VolunteerModel).where(
                or_(
                    VolunteerModel.preferred_days.ilike(query),
                    VolunteerModel.skills.ilike(query),
                    VolunteerModel.certificates.ilike(query),
                )
            )
        ).all()
        return [OrganizationMapper.to_domain_volunteer(orm) for orm in orm_entities]
