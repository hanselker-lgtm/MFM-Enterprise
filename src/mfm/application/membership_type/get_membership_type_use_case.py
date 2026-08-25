"""Get MembershipType use case."""

from __future__ import annotations

from uuid import UUID

from mfm.domain.membership.exceptions import MembershipTypeNotFoundError
from mfm.domain.membership.membership_type import MembershipType
from mfm.repositories.membership_type_repository import MembershipTypeRepository


class GetMembershipTypeUseCase:
    """Retrieve membership types by id or code."""

    def __init__(self, repository: MembershipTypeRepository) -> None:
        self._repository = repository

    def execute_by_id(self, membership_type_id: UUID) -> MembershipType:
        if not isinstance(membership_type_id, UUID):
            raise TypeError("membership_type_id must be a UUID")

        membership_type = self._repository.get(membership_type_id)
        if membership_type is None:
            raise MembershipTypeNotFoundError(
                f"Membership type {membership_type_id} was not found"
            )

        return membership_type

    def execute_by_code(self, code: str) -> MembershipType:
        if not isinstance(code, str):
            raise TypeError("code must be a string")

        normalized = code.strip().upper()
        if not normalized:
            raise ValueError("code cannot be empty")

        membership_type = self._repository.get_by_code(normalized)
        if membership_type is None:
            raise MembershipTypeNotFoundError(
                f"Membership type with code {normalized} was not found"
            )

        return membership_type
