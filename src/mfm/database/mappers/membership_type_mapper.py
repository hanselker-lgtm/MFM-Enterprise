"""Mapper between domain membership types and persistence rows."""

from __future__ import annotations

from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.domain.membership.membership_type import MembershipType


class MembershipTypeMapper:
    """Map between MembershipType domain entities and ORM rows."""

    @staticmethod
    def to_orm(membership_type: MembershipType) -> MembershipTypeModel:
        return MembershipTypeModel(
            id=membership_type.id,
            code=membership_type.code,
            name=membership_type.name,
            category=membership_type.category,
            description=membership_type.description,
            is_active=membership_type.is_active,
        )

    @staticmethod
    def to_domain(orm: MembershipTypeModel) -> MembershipType:
        return MembershipType(
            id=orm.id,
            code=orm.code,
            name=orm.name,
            category=orm.category,
            description=orm.description,
            is_active=orm.is_active,
        )
