"""Mapper between domain memberships and persistence membership models."""

from __future__ import annotations

from mfm.database.models.membership_model import MembershipModel
from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.domain.membership.membership import Membership
from mfm.domain.membership.membership_type import MembershipType


class MembershipMapper:
    """Map between Membership domain entities and MembershipModel rows."""

    @staticmethod
    def to_orm(membership: Membership) -> MembershipModel:
        return MembershipModel(
            id=membership.id,
            member_id=membership.member_id,
            membership_type_id=membership.membership_type_id,
            status=membership.status,
            start_date=membership.start_date,
            end_date=membership.end_date,
        )

    @staticmethod
    def to_domain(orm: MembershipModel) -> Membership:
        membership_type_orm: MembershipTypeModel | None = orm.membership_type
        if membership_type_orm is None:
            raise ValueError("MembershipType relation must be loaded")

        membership_type = MembershipType(
            id=membership_type_orm.id,
            code=membership_type_orm.code,
            name=membership_type_orm.name,
            description=membership_type_orm.description,
            is_active=membership_type_orm.is_active,
        )

        return Membership(
            id=orm.id,
            member_id=orm.member_id,
            membership_type=membership_type,
            status=orm.status,
            start_date=orm.start_date,
            end_date=orm.end_date,
        )
