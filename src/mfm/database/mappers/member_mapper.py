"""Mapper between domain members and persistence member models."""

from __future__ import annotations

from mfm.database.models.member_model import MemberModel
from mfm.domain.member.member import Member


class MemberMapper:
    """Map between Member domain entities and MemberModel rows."""

    @staticmethod
    def to_orm(member: Member) -> MemberModel:
        return MemberModel(
            id=member.id,
            contact_id=member.contact_id,
            member_number=member.member_number,
            status=member.status,
            join_date=member.join_date,
            leave_date=member.leave_date,
        )

    @staticmethod
    def to_domain(orm: MemberModel) -> Member:
        return Member(
            id=orm.id,
            contact_id=orm.contact_id,
            member_number=orm.member_number,
            status=orm.status,
            join_date=orm.join_date,
            leave_date=orm.leave_date,
        )
