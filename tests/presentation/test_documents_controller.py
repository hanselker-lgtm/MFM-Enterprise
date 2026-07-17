from __future__ import annotations

from datetime import UTC
from datetime import datetime
from types import SimpleNamespace
from uuid import UUID
from uuid import uuid4

from mfm.presentation.documents import CreateDocumentCommandViewModel
from mfm.presentation.documents import DocumentListFilterViewModel
from mfm.presentation.documents import DocumentsController
from mfm.presentation.documents import DocumentsNavigationCallbacks
from mfm.presentation.documents import DocumentSortField
from mfm.presentation.documents import RegisterDocumentVersionCommandViewModel


class _StubPort:
    def __init__(self, response: object) -> None:
        self.response = response
        self.requests: list[object] = []

    def execute(self, request: object) -> object:
        self.requests.append(request)
        return self.response


def _document_list_item(number: str, created_at: datetime) -> SimpleNamespace:
    return SimpleNamespace(
        document_id=uuid4(),
        document_number=number,
        document_title=f"Title {number}",
        document_type="REPORT",
        status="ACTIVE",
        created_at=created_at,
    )


def test_documents_controller_loads_and_paginates_document_list() -> None:
    list_port = _StubPort(
        SimpleNamespace(
            documents=(
                _document_list_item("DOC-2", datetime(2025, 2, 1, tzinfo=UTC)),
                _document_list_item("DOC-1", datetime(2025, 1, 1, tzinfo=UTC)),
            )
        )
    )

    controller = DocumentsController(
        list_documents_feature=list_port,
        search_documents_feature=_StubPort(SimpleNamespace(documents=())),
        get_document_feature=_StubPort(None),
        create_document_feature=_StubPort(None),
        register_document_version_feature=_StubPort(None),
        archive_document_feature=_StubPort(None),
    )

    vm = controller.load_document_list(
        filters=DocumentListFilterViewModel(
            sort_by=DocumentSortField.DOCUMENT_NUMBER,
            descending=False,
            page=1,
            page_size=1,
        )
    )

    assert len(list_port.requests) == 1
    assert vm.items[0].document_number == "DOC-1"
    assert vm.pagination.total_items == 2
    assert vm.pagination.total_pages == 2


def test_documents_controller_uses_search_when_filtering() -> None:
    search_port = _StubPort(
        SimpleNamespace(
            documents=(
                SimpleNamespace(
                    document_id=uuid4(),
                    document_number="DOC-S",
                    document_title="Search",
                    document_type="EVIDENCE",
                    status="DRAFT",
                ),
            )
        )
    )

    controller = DocumentsController(
        list_documents_feature=_StubPort(SimpleNamespace(documents=())),
        search_documents_feature=search_port,
        get_document_feature=_StubPort(None),
        create_document_feature=_StubPort(None),
        register_document_version_feature=_StubPort(None),
        archive_document_feature=_StubPort(None),
    )

    vm = controller.load_document_list(filters=DocumentListFilterViewModel(text="s"))

    assert len(search_port.requests) == 1
    assert vm.items[0].document_number == "DOC-S"


def test_documents_controller_maps_detail_and_navigation_callback() -> None:
    document_id = uuid4()
    project_id = uuid4()
    navigation_calls: list[UUID] = []

    get_port = _StubPort(
        SimpleNamespace(
            document=SimpleNamespace(
                document_id=document_id,
                document_number="DOC-100",
                document_title="Detail",
                document_type="REPORT",
                status="ACTIVE",
                description="desc",
                created_at=datetime(2025, 1, 1, tzinfo=UTC),
                updated_at=None,
                archived_at=None,
                disposed_at=None,
                version=2,
                versions=(
                    SimpleNamespace(
                        version_number=1,
                        storage_key="doc/v1.pdf",
                        file_name="v1.pdf",
                        mime_type="application/pdf",
                        size_bytes=10,
                        created_at=datetime(2025, 1, 1, tzinfo=UTC),
                    ),
                ),
                references=(
                    SimpleNamespace(
                        reference_id=uuid4(),
                        target_capability="PROJECTS",
                        target_aggregate_type="PROJECT",
                        target_aggregate_id=str(project_id),
                        exists=True,
                        authorized=True,
                        is_soft_deleted=False,
                        is_archived=False,
                        checked_at=datetime(2025, 1, 1, tzinfo=UTC),
                        description="link",
                    ),
                ),
            )
        )
    )

    controller = DocumentsController(
        list_documents_feature=_StubPort(SimpleNamespace(documents=())),
        search_documents_feature=_StubPort(SimpleNamespace(documents=())),
        get_document_feature=get_port,
        create_document_feature=_StubPort(None),
        register_document_version_feature=_StubPort(None),
        archive_document_feature=_StubPort(None),
        navigation=DocumentsNavigationCallbacks(to_project=lambda value: navigation_calls.append(value)),
    )

    detail = controller.open_document(document_id)
    controller.open_project(project_id)

    assert detail.document_number == "DOC-100"
    assert detail.project_id == project_id
    assert navigation_calls == [project_id]


def test_documents_controller_create_register_and_archive_operations() -> None:
    document_id = uuid4()
    create_port = _StubPort(SimpleNamespace(document=SimpleNamespace(document_id=document_id)))
    register_port = _StubPort(SimpleNamespace(document=SimpleNamespace(document_id=document_id)))
    archive_port = _StubPort(SimpleNamespace(document=SimpleNamespace(document_id=document_id)))

    controller = DocumentsController(
        list_documents_feature=_StubPort(SimpleNamespace(documents=())),
        search_documents_feature=_StubPort(SimpleNamespace(documents=())),
        get_document_feature=_StubPort(None),
        create_document_feature=create_port,
        register_document_version_feature=register_port,
        archive_document_feature=archive_port,
    )

    created_id = controller.create_document(
        CreateDocumentCommandViewModel(
            document_number="DOC-500",
            document_title="Created",
            document_type="MANUAL",
        )
    )
    registered_id = controller.register_document_version(
        RegisterDocumentVersionCommandViewModel(
            document_id=created_id,
            version_number=2,
            storage_key="doc/v2.pdf",
        )
    )
    archived_id = controller.archive_document(created_id)

    assert created_id == document_id
    assert registered_id == document_id
    assert archived_id == document_id
    assert controller.last_selected_document_id == document_id
    assert len(create_port.requests) == 1
    assert len(register_port.requests) == 1
    assert len(archive_port.requests) == 1
