from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import uuid4

from mfm.presentation.documents.documents_viewmodels import DocumentDetailViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentListFilterViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentListItemViewModel
from mfm.presentation.documents.documents_viewmodels import DocumentListViewModel
from mfm.presentation.documents.documents_viewmodels import PaginationViewModel
from mfm.presentation.documents.documents_workspace import DocumentsWorkspace


class _WorkspaceControllerStub:
    def __init__(self) -> None:
        self.load_calls = 0
        self.last_filters: DocumentListFilterViewModel | None = None

    @property
    def last_selected_document_id(self):
        return None

    def load_document_list(self, *, filters: DocumentListFilterViewModel) -> DocumentListViewModel:
        self.load_calls += 1
        self.last_filters = filters
        return DocumentListViewModel(
            filters=filters,
            items=(
                DocumentListItemViewModel(
                    document_id=uuid4(),
                    document_number="DOC-777",
                    document_title="Workspace Document",
                    document_type="REPORT",
                    status="DRAFT",
                    created_at=datetime(2025, 1, 1, tzinfo=UTC),
                ),
            ),
            pagination=PaginationViewModel(
                page=filters.page,
                page_size=filters.page_size,
                total_items=1,
                total_pages=1,
                has_previous=False,
                has_next=False,
            ),
        )

    def refresh(self):
        return self.load_document_list(filters=self.last_filters or DocumentListFilterViewModel()), None

    def open_document(self, document_id):
        _ = document_id
        return DocumentDetailViewModel(
            document_id=uuid4(),
            document_number="DOC-777",
            document_title="Workspace Document",
            document_type="REPORT",
            status="DRAFT",
            description=None,
            created_at=datetime(2025, 1, 1, tzinfo=UTC),
            updated_at=None,
            archived_at=None,
            disposed_at=None,
            version=1,
            versions=(),
            references=(),
            project_id=None,
        )

    def create_document(self, command):
        _ = command
        return uuid4()

    def register_document_version(self, command):
        _ = command
        return uuid4()

    def archive_document(self, document_id):
        _ = document_id
        return uuid4()

    def open_project(self, project_id):
        _ = project_id


def test_documents_workspace_performs_initial_lazy_load(qapp) -> None:
    controller = _WorkspaceControllerStub()

    _ = DocumentsWorkspace(controller=controller)

    assert controller.load_calls == 1
