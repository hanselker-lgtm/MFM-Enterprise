"""Project activity entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from uuid import uuid4

from mfm.domain.projects.project_priority import ProjectPriority


@dataclass(slots=True)
class ProjectActivity:
    """Activity tracked inside the Project aggregate."""

    title: str
    status: str = "PLANNED"
    description: str | None = None
    planned_start: datetime | None = None
    planned_finish: datetime | None = None
    actual_start: datetime | None = None
    actual_finish: datetime | None = None
    priority: ProjectPriority = ProjectPriority.NORMAL
    estimated_hours: Decimal | int | str | None = None
    actual_hours: Decimal | int | str | None = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        self.title = str(self.title).strip()
        if not self.title:
            raise ValueError("activity title cannot be empty")

        self.status = str(self.status).strip().upper()
        if not self.status:
            raise ValueError("activity status cannot be empty")

        if not isinstance(self.priority, ProjectPriority):
            self.priority = ProjectPriority(str(self.priority).upper())

        if self.description is not None:
            self.description = str(self.description).strip() or None

        if self.estimated_hours is not None:
            self.estimated_hours = Decimal(str(self.estimated_hours))

        if self.actual_hours is not None:
            self.actual_hours = Decimal(str(self.actual_hours))

        if not isinstance(self.id, UUID):
            self.id = UUID(str(self.id))
