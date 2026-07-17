"""ViewModels for documents workspace presentation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from uuid import UUID


class DocumentSortField(StrEnum):
    DOCUMENT_NUMBER = "document_number"
    CREATED_AT = "created_at"
    STATUS = "status"
    DOCUMENT_TYPE = "document_type"


@dataclass(frozen=True, slots=True)
class DocumentListFilterViewModel:
    text: str = ""
    status: str = "ALL"
    target_capability: str = "ALL"
    sort_by: DocumentSortField = DocumentSortField.CREATED_AT
    descending: bool = True
    page: int = 1
    page_size: int = 25


@dataclass(frozen=True, slots=True)
class PaginationViewModel:
    page: int
    page_size: int
    total_items: int
    total_pages: int
    has_previous: bool
    has_next: bool


@dataclass(frozen=True, slots=True)
class DocumentListItemViewModel:
    document_id: UUID
    document_number: str
    document_title: str
    document_type: str
    status: str
    created_at: datetime | None


@dataclass(frozen=True, slots=True)
class DocumentListViewModel:
    filters: DocumentListFilterViewModel
    items: tuple[DocumentListItemViewModel, ...]
    pagination: PaginationViewModel


@dataclass(frozen=True, slots=True)
class DocumentVersionViewModel:
    version_number: int
    storage_key: str
    file_name: str | None
    mime_type: str | None
    size_bytes: int | None
    created_at: datetime


@dataclass(frozen=True, slots=True)
class DocumentReferenceViewModel:
    reference_id: UUID
    target_capability: str
    target_aggregate_type: str
    target_aggregate_id: str
    exists: bool
    authorized: bool
    is_soft_deleted: bool
    is_archived: bool
    checked_at: datetime
    description: str | None


@dataclass(frozen=True, slots=True)
class DocumentDetailViewModel:
    document_id: UUID
    document_number: str
    document_title: str
    document_type: str
    status: str
    description: str | None
    created_at: datetime
    updated_at: datetime | None
    archived_at: datetime | None
    disposed_at: datetime | None
    version: int
    versions: tuple[DocumentVersionViewModel, ...]
    references: tuple[DocumentReferenceViewModel, ...]
    project_id: UUID | None


@dataclass(frozen=True, slots=True)
class CreateDocumentCommandViewModel:
    document_number: str
    document_title: str
    document_type: str
    status: str = "DRAFT"
    description: str | None = None
    project_id: UUID | None = None


@dataclass(frozen=True, slots=True)
class RegisterDocumentVersionCommandViewModel:
    document_id: UUID
    version_number: int
    storage_key: str
    file_name: str | None = None
    mime_type: str | None = None
    checksum: str | None = None
    size_bytes: int | None = None
