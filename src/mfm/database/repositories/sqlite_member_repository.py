"""SQLite repository for Member aggregates."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.member_mapper import MemberMapper
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.member_model import MemberModel
from mfm.domain.member.member import Member
from mfm.repositories.member_repository import MemberRepository


class SQLiteMemberRepository(MemberRepository):
    """SQLAlchemy-backed repository for Member aggregates."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, member: Member) -> None:
        if self.get_by_number(member.member_number) is not None:
            raise ValueError(f"Member number {member.member_number} already exists")

        orm_member = MemberMapper.to_orm(member)
        self._session.add(orm_member)
        self._session.flush()

    def update(self, member: Member) -> None:
        orm_member = self._session.get(MemberModel, member.id)
        if orm_member is None:
            raise ValueError(f"Member {member.id} does not exist")

        if member.member_number != orm_member.member_number:
            other = self.get_by_number(member.member_number)
            if other is not None and other.id != member.id:
                raise ValueError(f"Member number {member.member_number} already exists")

        orm_member.contact_id = member.contact_id
        orm_member.member_number = member.member_number
        orm_member.status = member.status
        orm_member.join_date = member.join_date
        orm_member.leave_date = member.leave_date
        self._session.flush()

    def get(self, member_id: UUID) -> Member | None:
        statement = select(MemberModel).where(MemberModel.id == member_id)
        orm_member = self._session.scalar(statement)
        if orm_member is None:
            return None
        return MemberMapper.to_domain(orm_member)

    def get_by_number(self, member_number: str) -> Member | None:
        statement = select(MemberModel).where(MemberModel.member_number == member_number)
        orm_member = self._session.scalar(statement)
        if orm_member is None:
            return None
        return MemberMapper.to_domain(orm_member)

    def list(self) -> list[Member]:
        statement = select(MemberModel)
        orm_members = self._session.scalars(statement).all()
        return [MemberMapper.to_domain(orm_member) for orm_member in orm_members]

    def exists(self, member_id: UUID) -> bool:
        return self._session.get(MemberModel, member_id) is not None

    def delete(self, member_id: UUID) -> None:
        orm_member = self._session.get(MemberModel, member_id)
        if orm_member is None:
            return

        self._session.delete(orm_member)
        self._session.flush()

    def contact_exists(self, contact_id: UUID) -> bool:
        return self._session.get(ContactModel, contact_id) is not None
