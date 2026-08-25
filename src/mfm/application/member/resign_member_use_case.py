"""Resign Member use case."""

from __future__ import annotations

from datetime import date
from uuid import UUID

from mfm.domain.member.exceptions import MemberNotFoundError
from mfm.domain.member.member import Member
from mfm.repositories.member_repository import MemberRepository


class ResignMemberUseCase:
    """Terminate an existing member by resignation."""

    def __init__(self, repository: MemberRepository) -> None:
        self._repository = repository

    def execute(self, member_id: UUID, resign_date: date | None = None) -> Member:
        if not isinstance(member_id, UUID):
            raise TypeError("member_id must be a UUID")

        member = self._repository.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member {member_id} was not found")

        member.resign(resign_date)
        self._repository.update(member)
        return member
