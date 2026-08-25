"""Create MembershipType use case."""

from __future__ import annotations

from mfm.domain.membership.exceptions import DuplicateMembershipTypeCodeError
from mfm.domain.membership.membership_type import MembershipType
from mfm.repositories.membership_type_repository import MembershipTypeRepository


class CreateMembershipTypeUseCase:
    """Create a new membership type if code is unique."""

    def __init__(self, repository: MembershipTypeRepository) -> None:
        self._repository = repository

    def execute(self, membership_type: MembershipType) -> MembershipType:
        if not isinstance(membership_type, MembershipType):
            raise TypeError("membership_type must be a MembershipType")

        if self._repository.get_by_code(membership_type.code) is not None:
            raise DuplicateMembershipTypeCodeError(
                f"Membership type code {membership_type.code} already exists"
            )

        self._repository.add(membership_type)
        return membership_type
