"""SQLite repository for Committee aggregates."""

from __future__ import annotations

from typing import cast
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.organization_mapper import OrganizationMapper
from mfm.database.models.committee_member_model import CommitteeMemberModel
from mfm.database.models.committee_model import CommitteeModel
from mfm.domain.organization.committee import Committee
from mfm.repositories.committee_repository import CommitteeRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteCommitteeRepository(CommitteeRepository):
    """SQLAlchemy-backed repository for Committee aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, committee: Committee) -> None:
        self._session.add(OrganizationMapper.to_orm_committee(committee))
        self._session.flush()

    def get_by_id(self, committee_id: UUID) -> Committee | None:
        orm = self._session.scalar(
            select(CommitteeModel).where(CommitteeModel.id == committee_id)
        )
        if orm is None:
            return None
        return OrganizationMapper.to_domain_committee(orm)

    def update(self, committee: Committee) -> None:
        orm = self._session.get(CommitteeModel, committee.id.value)
        if orm is None:
            raise ValueError(f"Committee {committee.id.value} does not exist")

        orm.organization_id = committee.organization_id.value
        orm.name = committee.name
        orm.purpose = committee.purpose
        orm.status = committee.status
        orm.created_at = committee.created_at
        orm.updated_at = committee.updated_at
        orm.members = [
            CommitteeMemberModel(
                committee_id=committee.id.value,
                reference_id=member.reference_id,
                function_title=member.function_title,
                joined_at=member.joined_at,
                left_at=member.left_at,
            )
            for member in committee.members
        ]
        self._session.flush()

    def delete(self, committee_id: UUID) -> None:
        orm = self._session.get(CommitteeModel, committee_id)
        if orm is None:
            return
        self._session.delete(orm)
        self._session.flush()

    def exists(self, committee_id: UUID) -> bool:
        return self._session.get(CommitteeModel, committee_id) is not None

    def list(self) -> list[Committee]:
        orm_entities = self._session.scalars(select(CommitteeModel)).all()
        return [OrganizationMapper.to_domain_committee(orm) for orm in orm_entities]

    def search(self, text: str) -> list[Committee]:
        query = f"%{text}%"
        orm_entities = self._session.scalars(
            select(CommitteeModel).where(
                or_(
                    CommitteeModel.name.ilike(query),
                    CommitteeModel.purpose.ilike(query),
                )
            )
        ).all()
        return [OrganizationMapper.to_domain_committee(orm) for orm in orm_entities]
