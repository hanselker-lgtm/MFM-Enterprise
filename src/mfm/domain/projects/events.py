"""Projects domain events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class ProjectCreated(DomainEvent):
    project_id: UUID | None = None


@dataclass(slots=True)
class ProjectUpdated(DomainEvent):
    project_id: UUID | None = None


@dataclass(slots=True)
class ProjectStatusChanged(DomainEvent):
    project_id: UUID | None = None
    previous_status: str | None = None
    new_status: str | None = None


@dataclass(slots=True)
class ProjectArchived(DomainEvent):
    project_id: UUID | None = None
    archived_at: datetime | None = None