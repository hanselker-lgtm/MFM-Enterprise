"""Delete MembershipType use case."""

from __future__ import annotations

from uuid import UUID

from mfm.domain.membership.exceptions import MembershipTypeNotFoundError
from mfm.repositories.membership_type_repository import MembershipTypeRepository


class DeleteMembershipTypeUseCase:
    """Delete an existing membership type."""

    def __init__(self, repository: MembershipTypeRepository) -> None:
        self._repository = repository

    def execute(self, membership_type_id: UUID) -> bool:
        if not isinstance(membership_type_id, UUID):
            raise TypeError("membership_type_id must be a UUID")

        existing = self._repository.get(membership_type_id)
        if existing is None:
            raise MembershipTypeNotFoundError(
                f"Membership type {membership_type_id} was not found"
            )

        self._repository.delete(membership_type_id)
        return True
