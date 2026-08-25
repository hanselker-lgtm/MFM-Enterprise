"""Create Member use case."""

from __future__ import annotations

from mfm.domain.member.exceptions import (
    ContactReferenceNotFoundError,
    DuplicateMemberNumberError,
)
from mfm.domain.member.member import Member
from mfm.repositories.member_repository import MemberRepository


class CreateMemberUseCase:
    """Create a new member if rules are satisfied."""

    def __init__(self, repository: MemberRepository) -> None:
        self._repository = repository

    def execute(self, member: Member) -> Member:
        if not isinstance(member, Member):
            raise TypeError("member must be a Member")

        if self._repository.get_by_number(member.member_number) is not None:
            raise DuplicateMemberNumberError(
                f"Member number {member.member_number} already exists"
            )

        if not self._repository.contact_exists(member.contact_id):
            raise ContactReferenceNotFoundError(
                f"Contact {member.contact_id} does not exist"
            )

        self._repository.add(member)
        return member
