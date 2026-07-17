"""SQLite repository for Membership aggregates."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.database.mappers.membership_mapper import MembershipMapper
from mfm.database.models.member_model import MemberModel
from mfm.database.models.membership_model import MembershipModel
from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_status import MembershipStatus
from mfm.repositories.membership_repository import MembershipRepository


class SQLiteMembershipRepository(MembershipRepository):
    """SQLAlchemy-backed repository for Membership aggregates."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, membership: Membership) -> None:
        if not self.member_exists(membership.member_id):
            raise ValueError(f"Member {membership.member_id} does not exist")

        if not self.membership_type_exists(membership.membership_type_id):
            raise ValueError(
                f"Membership type {membership.membership_type_id} does not exist"
            )

        active_memberships = [
            item
            for item in self.list_by_member(membership.member_id)
            if item.status is MembershipStatus.ACTIVE
        ]
        if membership.status is MembershipStatus.ACTIVE and active_memberships:
            raise ValueError(
                f"Member {membership.member_id} already has an active membership"
            )

        orm_membership = MembershipMapper.to_orm(membership)
        self._session.add(orm_membership)
        self._session.flush()

    def update(self, membership: Membership) -> None:
        orm_membership = self._session.get(MembershipModel, membership.id)
        if orm_membership is None:
            raise ValueError(f"Membership {membership.id} does not exist")

        if not self.member_exists(membership.member_id):
            raise ValueError(f"Member {membership.member_id} does not exist")

        if not self.membership_type_exists(membership.membership_type_id):
            raise ValueError(
                f"Membership type {membership.membership_type_id} does not exist"
            )

        if membership.status is MembershipStatus.ACTIVE:
            active_memberships = [
                item
                for item in self.list_by_member(membership.member_id)
                if item.status is MembershipStatus.ACTIVE and item.id != membership.id
            ]
            if active_memberships:
                raise ValueError(
                    f"Member {membership.member_id} already has an active membership"
                )

        orm_membership.member_id = membership.member_id
        orm_membership.membership_type_id = membership.membership_type_id
        orm_membership.status = membership.status
        orm_membership.start_date = membership.start_date
        orm_membership.end_date = membership.end_date
        self._session.flush()

    def get(self, membership_id: UUID) -> Membership | None:
        statement = (
            select(MembershipModel)
            .options(joinedload(MembershipModel.membership_type))
            .where(MembershipModel.id == membership_id)
        )
        orm_membership = self._session.scalar(statement)
        if orm_membership is None:
            return None
        return MembershipMapper.to_domain(orm_membership)

    def list(self) -> list[Membership]:
        statement = select(MembershipModel).options(
            joinedload(MembershipModel.membership_type)
        )
        orm_memberships = self._session.scalars(statement).all()
        return [MembershipMapper.to_domain(orm_membership) for orm_membership in orm_memberships]

    def list_by_member(self, member_id: UUID) -> list[Membership]:
        statement = (
            select(MembershipModel)
            .options(joinedload(MembershipModel.membership_type))
            .where(MembershipModel.member_id == member_id)
        )
        orm_memberships = self._session.scalars(statement).all()
        return [MembershipMapper.to_domain(orm_membership) for orm_membership in orm_memberships]

    def list_active(self) -> list[Membership]:
        statement = (
            select(MembershipModel)
            .options(joinedload(MembershipModel.membership_type))
            .where(MembershipModel.status == MembershipStatus.ACTIVE)
        )
        orm_memberships = self._session.scalars(statement).all()
        return [MembershipMapper.to_domain(orm_membership) for orm_membership in orm_memberships]

    def exists(self, membership_id: UUID) -> bool:
        return self._session.get(MembershipModel, membership_id) is not None

    def delete(self, membership_id: UUID) -> None:
        orm_membership = self._session.get(MembershipModel, membership_id)
        if orm_membership is None:
            return

        self._session.delete(orm_membership)
        self._session.flush()

    def member_exists(self, member_id: UUID) -> bool:
        return self._session.get(MemberModel, member_id) is not None

    def membership_type_exists(self, membership_type_id: UUID) -> bool:
        return self._session.get(MembershipTypeModel, membership_type_id) is not None
