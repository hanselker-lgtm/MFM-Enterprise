"""DTOs for document archive summary reporting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class DocumentArchiveSummaryItemDTO:
    category_code: str
    folder_path: str
    status: str
    versions_count: int
    attachments_count: int


@dataclass(frozen=True, slots=True)
class DocumentArchiveIntegrationDTO:
    membership_links: int
    organization_links: int
    events_links: int
    billing_links: int
    projects_links: int


@dataclass(frozen=True, slots=True)
class DocumentArchiveSummaryResponse:
    documents: tuple[DocumentArchiveSummaryItemDTO, ...]
    integration: DocumentArchiveIntegrationDTO
    generated_at: datetime
