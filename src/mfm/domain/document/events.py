"""Document domain events."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from mfm.common.domain_event import DomainEvent


@dataclass(slots=True)
class DocumentCreated(DomainEvent):
    document_id: UUID | None = None


@dataclass(slots=True)
class DocumentUpdated(DomainEvent):
    document_id: UUID | None = None


@dataclass(slots=True)
class DocumentStatusChanged(DomainEvent):
    document_id: UUID | None = None
    previous_status: str | None = None
    new_status: str | None = None


@dataclass(slots=True)
class DocumentArchived(DomainEvent):
    document_id: UUID | None = None
    archived_at: datetime | None = None


@dataclass(slots=True)
class DocumentDisposed(DomainEvent):
    document_id: UUID | None = None
    disposed_at: datetime | None = None


@dataclass(slots=True)
class DocumentVersionAdded(DomainEvent):
    document_id: UUID | None = None
    version_number: int | None = None


@dataclass(slots=True)
class DocumentReferenceAdded(DomainEvent):
    document_id: UUID | None = None
    target_capability: str | None = None
    target_aggregate_type: str | None = None
    target_aggregate_id: str | None = None
