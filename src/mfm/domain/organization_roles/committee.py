"""Committee entity for organization roles capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class Committee:
    """Committee with linked role members."""

    name: str
    mandate: str
    role_ids: tuple[UUID, ...] = ()
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(self.mandate, str) or not self.mandate.strip():
            raise ValueError("mandate must be a non-empty string")

        self.name = self.name.strip()
        self.mandate = self.mandate.strip()

        normalized_role_ids: list[UUID] = []
        for role_id in self.role_ids:
            if not isinstance(role_id, UUID):
                raise ValueError("role_ids must contain UUID values")
            normalized_role_ids.append(role_id)
        self.role_ids = tuple(dict.fromkeys(normalized_role_ids))
