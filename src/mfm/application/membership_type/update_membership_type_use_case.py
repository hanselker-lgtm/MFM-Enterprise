"""Update MembershipType use case."""

from __future__ import annotations

from mfm.domain.membership.exceptions import (
    DuplicateMembershipTypeCodeError,
    MembershipTypeNotFoundError,
)
from mfm.domain.membership.membership_type import MembershipType
from mfm.repositories.membership_type_repository import MembershipTypeRepository


class UpdateMembershipTypeUseCase:
    """Update an existing membership type."""

    def __init__(self, repository: MembershipTypeRepository) -> None:
        self._repository = repository

    def execute(self, membership_type: MembershipType) -> MembershipType:
        if not isinstance(membership_type, MembershipType):
            raise TypeError("membership_type must be a MembershipType")

        existing = self._repository.get(membership_type.id)
        if existing is None:
            raise MembershipTypeNotFoundError(
                f"Membership type {membership_type.id} was not found"
            )

        normalized_code = membership_type.code.strip().upper()
        has_duplicate_code = any(
            item.id != membership_type.id and item.code == normalized_code
            for item in self._repository.list()
        )
        if has_duplicate_code:
            raise DuplicateMembershipTypeCodeError(
                f"Membership type code {normalized_code} already exists"
            )

        membership_type.code = normalized_code
        self._repository.update(membership_type)
        return membership_type
