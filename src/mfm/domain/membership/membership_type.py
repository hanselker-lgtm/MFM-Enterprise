"""Membership type domain model."""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from mfm.domain.membership.exceptions import InvalidMembershipTypeError
from mfm.domain.membership.membership_category import MembershipCategory


@dataclass(slots=True)
class MembershipType:
    """Domain entity describing an administrable membership category."""

    code: str
    name: str
    category: MembershipCategory = MembershipCategory.GENERAL
    description: str | None = None
    is_active: bool = True
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise InvalidMembershipTypeError("id must be a UUID")

        if not isinstance(self.code, str) or not self.code.strip():
            raise InvalidMembershipTypeError("code must be a non-empty string")

        if not isinstance(self.name, str) or not self.name.strip():
            raise InvalidMembershipTypeError("name must be a non-empty string")

        if not isinstance(self.category, MembershipCategory):
            raise InvalidMembershipTypeError(
                "category must be MembershipCategory"
            )

        self.code = self.code.strip().upper()
        self.name = self.name.strip()

        if self.description is not None:
            if not isinstance(self.description, str):
                raise InvalidMembershipTypeError("description must be a string")
            description = self.description.strip()
            self.description = description or None

    def rename(self, *, name: str, description: str | None = None) -> None:
        if not isinstance(name, str) or not name.strip():
            raise InvalidMembershipTypeError("name must be a non-empty string")

        self.name = name.strip()

        if description is None:
            self.description = None
            return

        if not isinstance(description, str):
            raise InvalidMembershipTypeError("description must be a string")

        normalized_description = description.strip()
        self.description = normalized_description or None

    def deactivate(self) -> None:
        self.is_active = False

    def activate(self) -> None:
        self.is_active = True
