"""SQLite repository for MembershipType aggregates."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.membership_type_mapper import MembershipTypeMapper
from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.domain.membership.membership_type import MembershipType
from mfm.repositories.membership_type_repository import MembershipTypeRepository


class SQLiteMembershipTypeRepository(MembershipTypeRepository):
    """SQLAlchemy-backed repository for MembershipType aggregates."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, membership_type: MembershipType) -> None:
        if self.get_by_code(membership_type.code) is not None:
            raise ValueError(f"Membership type code {membership_type.code} already exists")

        orm = MembershipTypeMapper.to_orm(membership_type)
        self._session.add(orm)
        self._session.flush()

    def update(self, membership_type: MembershipType) -> None:
        orm = self._session.get(MembershipTypeModel, membership_type.id)
        if orm is None:
            raise ValueError(f"Membership type {membership_type.id} does not exist")

        normalized_code = membership_type.code.strip().upper()
        if normalized_code != orm.code:
            other = self.get_by_code(normalized_code)
            if other is not None and other.id != membership_type.id:
                raise ValueError(
                    f"Membership type code {normalized_code} already exists"
                )

        orm.code = normalized_code
        orm.name = membership_type.name
        orm.category = membership_type.category
        orm.description = membership_type.description
        orm.is_active = membership_type.is_active
        self._session.flush()

    def get(self, membership_type_id: UUID) -> MembershipType | None:
        statement = select(MembershipTypeModel).where(MembershipTypeModel.id == membership_type_id)
        orm = self._session.scalar(statement)
        if orm is None:
            return None
        return MembershipTypeMapper.to_domain(orm)

    def get_by_code(self, code: str) -> MembershipType | None:
        normalized_code = code.strip().upper()
        statement = select(MembershipTypeModel).where(MembershipTypeModel.code == normalized_code)
        orm = self._session.scalar(statement)
        if orm is None:
            return None
        return MembershipTypeMapper.to_domain(orm)

    def list(self) -> list[MembershipType]:
        statement = select(MembershipTypeModel)
        orm_rows = self._session.scalars(statement).all()
        return [MembershipTypeMapper.to_domain(orm) for orm in orm_rows]

    def exists(self, membership_type_id: UUID) -> bool:
        return self._session.get(MembershipTypeModel, membership_type_id) is not None

    def delete(self, membership_type_id: UUID) -> None:
        orm = self._session.get(MembershipTypeModel, membership_type_id)
        if orm is None:
            return

        self._session.delete(orm)
        self._session.flush()
