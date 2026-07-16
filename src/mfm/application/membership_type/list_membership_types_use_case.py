"""List MembershipType use case."""

from __future__ import annotations

from mfm.domain.membership.membership_type import MembershipType
from mfm.repositories.membership_type_repository import MembershipTypeRepository


class ListMembershipTypesUseCase:
    """List all membership types with paging-ready options and sorting."""

    def __init__(self, repository: MembershipTypeRepository) -> None:
        self._repository = repository

    def execute(
        self,
        *,
        offset: int = 0,
        limit: int | None = None,
        sort_by: str = "code",
        descending: bool = False,
        active_only: bool = False,
    ) -> list[MembershipType]:
        if offset < 0:
            raise ValueError("offset cannot be negative")
        if limit is not None and limit < 0:
            raise ValueError("limit cannot be negative")

        membership_types = self._repository.list()
        if active_only:
            membership_types = [item for item in membership_types if item.is_active]

        sorted_items = _sort_membership_types(
            membership_types,
            sort_by=sort_by,
            descending=descending,
        )

        if limit is None:
            return sorted_items[offset:]

        return sorted_items[offset : offset + limit]


def _sort_membership_types(
    membership_types: list[MembershipType], *, sort_by: str, descending: bool
) -> list[MembershipType]:
    if sort_by == "name":
        def key_fn(membership_type: MembershipType):
            return membership_type.name.lower()
    elif sort_by == "active":
        def key_fn(membership_type: MembershipType):
            return membership_type.is_active
    else:
        def key_fn(membership_type: MembershipType):
            return membership_type.code.lower()

    return sorted(membership_types, key=key_fn, reverse=descending)
