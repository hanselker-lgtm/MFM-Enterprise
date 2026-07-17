"""Controller for documents workspace."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Callable
from typing import Protocol
from uuid import UUID

from mfm.application.features.documents import ArchiveDocumentRequest
from mfm.application.features.documents import CreateDocumentRequest
from mfm.application.features.documents import DocumentReferenceInput
from mfm.application.features.documents import DocumentVersionInput
from mfm.application.features.documents import GetDocumentRequest
from mfm.application.features.documents import ListDocumentsRequest
from mfm.application.features.documents import RegisterDocumentVersionRequest
from mfm.application.features.documents import SearchDocumentsRequest
from mfm.presentation.documents.documents_viewmodels import CreateDocumentCommandViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentDetailViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentListFilterViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentListItemViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentListViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentReferenceViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentSortField
from mfm.presentation.documents.documents_viewmodels import DocumentVersionViewModel
from mfm.presentation.documents.documents_viewmodels import PaginationViewModel
from mfm.presentation.documents.documents_viewmodels import RegisterDocumentVersionCommandViewModel


class ListDocumentsPort(Protocol):
    def execute(self, request: ListDocumentsRequest): ...


class SearchDocumentsPort(Protocol):
    def execute(self, request: SearchDocumentsRequest): ...


class GetDocumentPort(Protocol):
    def execute(self, request: GetDocumentRequest): ...


class CreateDocumentPort(Protocol):
    def execute(self, request: CreateDocumentRequest): ...


class RegisterDocumentVersionPort(Protocol):
    def execute(self, request: RegisterDocumentVersionRequest): ...


class ArchiveDocumentPort(Protocol):
    def execute(self, request: ArchiveDocumentRequest): ...


@dataclass(frozen=True, slots=True)
class DocumentsNavigationCallbacks:
    to_project: Callable[[UUID], None] | None = None


class DocumentsController:
    """UI controller that orchestrates document features only."""

    def __init__(
        self,
        *,
        list_documents_feature: ListDocumentsPort,
        search_documents_feature: SearchDocumentsPort,
        get_document_feature: GetDocumentPort,
        create_document_feature: CreateDocumentPort,
        register_document_version_feature: RegisterDocumentVersionPort,
        archive_document_feature: ArchiveDocumentPort,
        navigation: DocumentsNavigationCallbacks | None = None,
    ) -> None:
        self._list_documents = list_documents_feature
        self._search_documents = search_documents_feature
        self._get_document = get_document_feature
        self._create_document = create_document_feature
        self._register_document_version = register_document_version_feature
        self._archive_document = archive_document_feature
        self._navigation = navigation or DocumentsNavigationCallbacks()
        self._last_filters = DocumentListFilterViewModel()
        self._last_selected_document_id: UUID | None = None

    @property
    def last_selected_document_id(self) -> UUID | None:
        return self._last_selected_document_id

    def load_document_list(self, *, filters: DocumentListFilterViewModel) -> DocumentListViewModel:
        self._last_filters = filters

        use_search = (
            bool(filters.text.strip())
            or filters.status != "ALL"
            or filters.target_capability != "ALL"
        )

        if use_search:
            status = None if filters.status == "ALL" else filters.status
            target_capability = None if filters.target_capability == "ALL" else filters.target_capability
            response = self._search_documents.execute(
                SearchDocumentsRequest(
                    text=filters.text.strip() or None,
                    status=status,
                    target_capability=target_capability,
                )
            )
            items = tuple(
                DocumentListItemViewModel(
                    document_id=item.document_id,
                    document_number=item.document_number,
                    document_title=item.document_title,
                    document_type=item.document_type,
                    status=item.status,
                    created_at=None,
                )
                for item in response.documents
            )
        else:
            response = self._list_documents.execute(ListDocumentsRequest(status=None))
            items = tuple(
                DocumentListItemViewModel(
                    document_id=item.document_id,
                    document_number=item.document_number,
                    document_title=item.document_title,
                    document_type=item.document_type,
                    status=item.status,
                    created_at=item.created_at,
                )
                for item in response.documents
            )

        sorted_items = self._sort_items(items, filters)
        paged_items, pagination = self._paginate(sorted_items, filters)
        return DocumentListViewModel(filters=filters, items=paged_items, pagination=pagination)

    def open_document(self, document_id: UUID) -> DocumentDetailViewModel:
        self._last_selected_document_id = document_id
        document = self._get_document.execute(GetDocumentRequest(document_id=document_id)).document
        project_id = self._extract_project_id(document.references)

        return DocumentDetailViewModel(
            document_id=document.document_id,
            document_number=document.document_number,
            document_title=document.document_title,
            document_type=document.document_type,
            status=document.status,
            description=document.description,
            created_at=document.created_at,
            updated_at=document.updated_at,
            archived_at=document.archived_at,
            disposed_at=document.disposed_at,
            version=document.version,
            versions=tuple(
                DocumentVersionViewModel(
                    version_number=item.version_number,
                    storage_key=item.storage_key,
                    file_name=item.file_name,
                    mime_type=item.mime_type,
                    size_bytes=item.size_bytes,
                    created_at=item.created_at,
                )
                for item in document.versions
            ),
            references=tuple(
                DocumentReferenceViewModel(
                    reference_id=item.reference_id,
                    target_capability=item.target_capability,
                    target_aggregate_type=item.target_aggregate_type,
                    target_aggregate_id=item.target_aggregate_id,
                    exists=item.exists,
                    authorized=item.authorized,
                    is_soft_deleted=item.is_soft_deleted,
                    is_archived=item.is_archived,
                    checked_at=item.checked_at,
                    description=item.description,
                )
                for item in document.references
            ),
            project_id=project_id,
        )

    def create_document(self, command: CreateDocumentCommandViewModel) -> UUID:
        references: tuple[DocumentReferenceInput, ...] = ()
        if command.project_id is not None:
            references = (
                DocumentReferenceInput(
                    target_capability="PROJECTS",
                    target_aggregate_type="PROJECT",
                    target_aggregate_id=str(command.project_id),
                    exists=True,
                    authorized=True,
                    is_soft_deleted=False,
                    is_archived=False,
                    checked_at=datetime.now(UTC),
                    description="Linked from Documents workspace",
                ),
            )

        response = self._create_document.execute(
            CreateDocumentRequest(
                document_number=command.document_number,
                document_title=command.document_title,
                document_type=command.document_type,
                status=command.status,
                description=command.description,
                created_at=datetime.now(UTC),
                references=references,
            )
        )
        self._last_selected_document_id = response.document.document_id
        return response.document.document_id

    def register_document_version(self, command: RegisterDocumentVersionCommandViewModel) -> UUID:
        response = self._register_document_version.execute(
            RegisterDocumentVersionRequest(
                document_id=command.document_id,
                registered_at=datetime.now(UTC),
                version=DocumentVersionInput(
                    version_number=command.version_number,
                    storage_key=command.storage_key,
                    file_name=command.file_name,
                    mime_type=command.mime_type,
                    checksum=command.checksum,
                    size_bytes=command.size_bytes,
                    created_at=datetime.now(UTC),
                ),
            )
        )
        self._last_selected_document_id = response.document.document_id
        return response.document.document_id

    def archive_document(self, document_id: UUID) -> UUID:
        response = self._archive_document.execute(
            ArchiveDocumentRequest(document_id=document_id, archived_at=datetime.now(UTC))
        )
        self._last_selected_document_id = response.document.document_id
        return response.document.document_id

    def refresh(self) -> tuple[DocumentListViewModel, DocumentDetailViewModel | None]:
        list_vm = self.load_document_list(filters=self._last_filters)
        detail_vm = None
        if self._last_selected_document_id is not None:
            detail_vm = self.open_document(self._last_selected_document_id)
        return list_vm, detail_vm

    def open_project(self, project_id: UUID) -> None:
        if self._navigation.to_project is not None:
            self._navigation.to_project(project_id)

    @staticmethod
    def _sort_items(
        items: tuple[DocumentListItemViewModel, ...],
        filters: DocumentListFilterViewModel,
    ) -> tuple[DocumentListItemViewModel, ...]:
        key_map = {
            DocumentSortField.DOCUMENT_NUMBER: lambda value: value.document_number,
            DocumentSortField.CREATED_AT: lambda value: value.created_at or datetime.min.replace(tzinfo=UTC),
            DocumentSortField.STATUS: lambda value: value.status,
            DocumentSortField.DOCUMENT_TYPE: lambda value: value.document_type,
        }
        return tuple(sorted(items, key=key_map[filters.sort_by], reverse=filters.descending))

    @staticmethod
    def _paginate(
        items: tuple[DocumentListItemViewModel, ...],
        filters: DocumentListFilterViewModel,
    ) -> tuple[tuple[DocumentListItemViewModel, ...], PaginationViewModel]:
        total_items = len(items)
        page_size = max(filters.page_size, 1)
        total_pages = max((total_items + page_size - 1) // page_size, 1)
        page = min(max(filters.page, 1), total_pages)
        start = (page - 1) * page_size
        end = start + page_size

        pagination = PaginationViewModel(
            page=page,
            page_size=page_size,
            total_items=total_items,
            total_pages=total_pages,
            has_previous=page > 1,
            has_next=page < total_pages,
        )
        return tuple(items[start:end]), pagination

    @staticmethod
    def _extract_project_id(references: tuple[object, ...]) -> UUID | None:
        for reference in references:
            target_capability = getattr(reference, "target_capability", None)
            target_aggregate_id = getattr(reference, "target_aggregate_id", None)
            if target_capability != "PROJECTS":
                continue
            try:
                return UUID(str(target_aggregate_id).strip())
            except (TypeError, ValueError, AttributeError):
                continue
        return None
