"""Activate Member use case."""

from __future__ import annotations

from uuid import UUID

from mfm.domain.member.exceptions import MemberNotFoundError
from mfm.domain.member.member import Member
from mfm.repositories.member_repository import MemberRepository


class ActivateMemberUseCase:
    """Activate an existing member."""

    def __init__(self, repository: MemberRepository) -> None:
        self._repository = repository

    def execute(self, member_id: UUID) -> Member:
        if not isinstance(member_id, UUID):
            raise TypeError("member_id must be a UUID")

        member = self._repository.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member {member_id} was not found")

        member.activate()
        self._repository.update(member)
        return member
