"""Project assignment entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class ProjectAssignment:
    """Assignment tracked inside the Project aggregate."""

    organisation_id: UUID
    contact_id: UUID
    role: str
    assigned_from: datetime | None = None
    assigned_until: datetime | None = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.organisation_id, UUID):
            self.organisation_id = UUID(str(self.organisation_id))

        if not isinstance(self.contact_id, UUID):
            self.contact_id = UUID(str(self.contact_id))

        self.role = str(self.role).strip()
        if not self.role:
            raise ValueError("assignment role cannot be empty")

        if not isinstance(self.id, UUID):
            self.id = UUID(str(self.id))
