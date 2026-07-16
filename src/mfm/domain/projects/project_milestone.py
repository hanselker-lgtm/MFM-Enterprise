"""Project milestone entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class ProjectMilestone:
    """Milestone tracked inside the Project aggregate."""

    name: str
    sequence: int
    status: str = "PLANNED"
    description: str | None = None
    due_date: datetime | None = None
    completed_date: datetime | None = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        self.name = str(self.name).strip()
        if not self.name:
            raise ValueError("milestone name cannot be empty")

        self.sequence = int(self.sequence)
        if self.sequence < 1:
            raise ValueError("milestone sequence must be >= 1")

        self.status = str(self.status).strip().upper()
        if not self.status:
            raise ValueError("milestone status cannot be empty")

        if self.description is not None:
            self.description = str(self.description).strip() or None

        if not isinstance(self.id, UUID):
            self.id = UUID(str(self.id))
