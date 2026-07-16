from __future__ import annotations

from dataclasses import FrozenInstanceError
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from importlib import import_module
from uuid import UUID

import pytest

from mfm.application.documents.archive_document import ArchiveDocumentUseCase
from mfm.application.documents.attach_reference import AttachReferenceUseCase
from mfm.application.documents.create_document import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.documents.create_document import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.documents.create_document import (
    ValidationException as ServiceValidationException,
)
from mfm.application.documents.create_document import CreateDocumentUseCase
from mfm.application.documents.delete_document import DeleteDocumentUseCase
from mfm.application.documents.get_document import GetDocumentUseCase
from mfm.application.documents.list_documents import ListDocumentsUseCase
from mfm.application.documents.register_document_version import RegisterDocumentVersionUseCase
from mfm.application.documents.remove_reference import RemoveReferenceUseCase
from mfm.application.documents.search_documents import SearchDocumentsUseCase
from mfm.application.documents.update_document_metadata import UpdateDocumentMetadataUseCase
from mfm.application.features.documents import archive_document
from mfm.application.features.documents import attach_reference
from mfm.application.features.documents import create_document
from mfm.application.features.documents import delete_document
from mfm.application.features.documents import get_document
from mfm.application.features.documents import list_documents
from mfm.application.features.documents import register_document_version
from mfm.application.features.documents import remove_reference
from mfm.application.features.documents import search_documents
from mfm.application.features.documents import update_document_metadata
from mfm.application.features.documents.archive_document_feature import ArchiveDocumentFeature
from mfm.application.features.documents.archive_document_feature import ArchiveDocumentRequest
from mfm.application.features.documents.attach_reference_feature import AttachReferenceFeature
from mfm.application.features.documents.attach_reference_feature import AttachReferenceRequest
from mfm.application.features.documents.create_document_feature import (
    BusinessRuleViolation as FeatureBusinessRuleViolation,
)
from mfm.application.features.documents.create_document_feature import (
    CreateDocumentFeature,
)
from mfm.application.features.documents.create_document_feature import (
    CreateDocumentRequest,
)
from mfm.application.features.documents.create_document_feature import (
    DocumentReferenceInput,
)
from mfm.application.features.documents.create_document_feature import (
    DocumentVersionInput,
)
from mfm.application.features.documents.create_document_feature import (
    RepositoryException as FeatureRepositoryException,
)
from mfm.application.features.documents.create_document_feature import (
    ValidationException as FeatureValidationException,
)
from mfm.application.features.documents.delete_document_feature import DeleteDocumentFeature
from mfm.application.features.documents.delete_document_feature import DeleteDocumentRequest
from mfm.application.features.documents.get_document_feature import GetDocumentFeature
from mfm.application.features.documents.get_document_feature import GetDocumentRequest
from mfm.application.features.documents.list_documents_feature import ListDocumentsFeature
from mfm.application.features.documents.list_documents_feature import ListDocumentsRequest
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionFeature,
)
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionRequest,
)
from mfm.application.features.documents.remove_reference_feature import (
    RemoveReferenceFeature,
)
from mfm.application.features.documents.remove_reference_feature import (
    RemoveReferenceRequest,
)
from mfm.application.features.documents.search_documents_feature import (
    SearchDocumentsFeature,
)
from mfm.application.features.documents.search_documents_feature import (
    SearchDocumentsRequest,
)
from mfm.application.features.documents.update_document_metadata_feature import (
    UpdateDocumentMetadataFeature,
)
from mfm.application.features.documents.update_document_metadata_feature import (
    UpdateDocumentMetadataRequest,
)
from tests.application.documents.test_document_use_cases import FakeDocumentsUnitOfWork


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        if self._error is not None:
            raise self._error
        return self._response


def _aware(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, 0, tzinfo=UTC)


def _version(number: int) -> DocumentVersionInput:
    return DocumentVersionInput(
        version_number=number,
        storage_key=f"documents/doc-feat/v{number}.pdf",
        file_name=f"v{number}.pdf",
        mime_type="application/pdf",
        checksum=f"sha256:{number:02d}",
        size_bytes=1024 * number,
        created_at=_aware(2032, 2, number, 8),
    )


def _reference(index: int) -> DocumentReferenceInput:
    return DocumentReferenceInput(
        target_capability="PROJECTS",
        target_aggregate_type="PROJECT",
        target_aggregate_id=f"00000000-0000-0000-0000-00000000F{index:03d}",
        exists=True,
        authorized=True,
        is_soft_deleted=False,
        is_archived=False,
        checked_at=_aware(2032, 2, index, 9),
        description=f"Reference {index}",
    )


def _create_document(uow: FakeDocumentsUnitOfWork, *, number: str = "DOC-FEAT-001") -> UUID:
    response = CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow)).execute(
        CreateDocumentRequest(
            document_number=number,
            document_title="Inspection package",
            document_type="MAINTENANCE_REPORT",
            status="DRAFT",
            description="Feature flow",
            created_at=_aware(2032, 2, 1, 8),
            versions=(_version(1),),
            references=(_reference(1),),
        )
    )
    return response.document.document_id


def test_create_feature_request_mapping_response_mapping_and_immutability() -> None:
    uow = FakeDocumentsUnitOfWork()
    feature = CreateDocumentFeature(service=CreateDocumentUseCase(unit_of_work=uow))

    request = CreateDocumentRequest(
        document_number="DOC-FEAT-100",
        document_title="Feature Document",
        document_type="PROJECT_EVIDENCE",
        status="DRAFT",
        versions=(_version(1),),
        references=(_reference(1),),
    )

    response = feature.execute(request)

    assert response.document.document_number == "DOC-FEAT-100"
    assert response.document.status == "DRAFT"
    assert response.document.versions[0].storage_key.endswith("v1.pdf")
    assert response.document.references[0].target_capability == "PROJECTS"
    assert is_dataclass(response.document)

    with pytest.raises(FrozenInstanceError):
        request.document_title = "Changed"  # type: ignore[misc]


def test_create_feature_error_mapping() -> None:
    invalid = CreateDocumentFeature(
        service=StubService(error=ServiceValidationException("invalid"))
    )
    with pytest.raises(FeatureValidationException):
        invalid.execute(
            CreateDocumentRequest(
                document_number="DOC-FEAT-ERR-1",
                document_title="x",
                document_type="REPORT",
            )
        )

    duplicate = CreateDocumentFeature(
        service=StubService(error=ServiceBusinessRuleViolation("duplicate"))
    )
    with pytest.raises(FeatureBusinessRuleViolation):
        duplicate.execute(
            CreateDocumentRequest(
                document_number="DOC-FEAT-ERR-2",
                document_title="x",
                document_type="REPORT",
            )
        )

    failing = CreateDocumentFeature(
        service=StubService(error=ServiceRepositoryException("failed"))
    )
    with pytest.raises(FeatureRepositoryException):
        failing.execute(
            CreateDocumentRequest(
                document_number="DOC-FEAT-ERR-3",
                document_title="x",
                document_type="REPORT",
            )
        )


def test_get_feature_existing_and_missing_mapping() -> None:
    uow = FakeDocumentsUnitOfWork()
    document_id = _create_document(uow, number="DOC-FEAT-GET")

    get_feature = GetDocumentFeature(service=GetDocumentUseCase(unit_of_work=uow))
    existing = get_feature.execute(GetDocumentRequest(document_id=document_id))
    assert existing.document.document_id == document_id

    with pytest.raises(FeatureBusinessRuleViolation):
        get_feature.execute(
            GetDocumentRequest(document_id=UUID("00000000-0000-0000-0000-00000000F404"))
        )


def test_update_register_archive_attach_remove_and_delete_features_end_to_end() -> None:
    uow = FakeDocumentsUnitOfWork()
    document_id = _create_document(uow, number="DOC-FEAT-LIFE")

    updated = UpdateDocumentMetadataFeature(
        service=UpdateDocumentMetadataUseCase(unit_of_work=uow)
    ).execute(
        UpdateDocumentMetadataRequest(
            document_id=document_id,
            document_title="Lifecycle Document",
            description="Updated",
            updated_at=_aware(2032, 2, 2, 8),
        )
    )
    assert updated.document.document_title == "Lifecycle Document"

    versioned = RegisterDocumentVersionFeature(
        service=RegisterDocumentVersionUseCase(unit_of_work=uow)
    ).execute(
        RegisterDocumentVersionRequest(
            document_id=document_id,
            version=_version(2),
            registered_at=_aware(2032, 2, 3, 8),
        )
    )
    assert len(versioned.document.versions) == 2

    attached = AttachReferenceFeature(service=AttachReferenceUseCase(unit_of_work=uow)).execute(
        AttachReferenceRequest(
            document_id=document_id,
            reference=_reference(2),
            attached_at=_aware(2032, 2, 4, 8),
        )
    )
    assert len(attached.document.references) == 2

    archived = ArchiveDocumentFeature(service=ArchiveDocumentUseCase(unit_of_work=uow)).execute(
        ArchiveDocumentRequest(document_id=document_id, archived_at=_aware(2032, 2, 5, 8))
    )
    assert archived.document.status == "ARCHIVED"

    reference_id = attached.document.references[0].reference_id
    removed = RemoveReferenceFeature(service=RemoveReferenceUseCase(unit_of_work=uow)).execute(
        RemoveReferenceRequest(document_id=document_id, reference_id=reference_id)
    )
    assert len(removed.document.references) == 1

    deleted = DeleteDocumentFeature(service=DeleteDocumentUseCase(unit_of_work=uow)).execute(
        DeleteDocumentRequest(document_id=document_id)
    )
    assert deleted.document_id == document_id


def test_list_and_search_features_delegate_and_preserve_order() -> None:
    uow = FakeDocumentsUnitOfWork()
    _create_document(uow, number="DOC-FEAT-A")
    second_id = _create_document(uow, number="DOC-FEAT-B")

    ArchiveDocumentFeature(service=ArchiveDocumentUseCase(unit_of_work=uow)).execute(
        ArchiveDocumentRequest(document_id=second_id, archived_at=_aware(2032, 2, 8, 8))
    )

    listed = ListDocumentsFeature(service=ListDocumentsUseCase(unit_of_work=uow)).execute(
        ListDocumentsRequest()
    )
    assert [item.document_number for item in listed.documents] == ["DOC-FEAT-A", "DOC-FEAT-B"]

    searched_text = SearchDocumentsFeature(
        service=SearchDocumentsUseCase(unit_of_work=uow)
    ).execute(SearchDocumentsRequest(text="FEAT-B"))
    assert [item.document_number for item in searched_text.documents] == ["DOC-FEAT-B"]

    searched_status = SearchDocumentsFeature(
        service=SearchDocumentsUseCase(unit_of_work=uow)
    ).execute(SearchDocumentsRequest(status="ARCHIVED"))
    assert [item.document_number for item in searched_status.documents] == ["DOC-FEAT-B"]

    searched_capability = SearchDocumentsFeature(
        service=SearchDocumentsUseCase(unit_of_work=uow)
    ).execute(SearchDocumentsRequest(target_capability="PROJECTS"))
    assert [item.document_number for item in searched_capability.documents] == [
        "DOC-FEAT-A",
        "DOC-FEAT-B",
    ]


def test_package_entrypoint_helpers_delegate_to_feature_execute() -> None:
    uow = FakeDocumentsUnitOfWork()

    created = create_document(
        service=CreateDocumentUseCase(unit_of_work=uow),
        request=CreateDocumentRequest(
            document_number="DOC-FEAT-API-1",
            document_title="API Doc",
            document_type="REPORT",
            versions=(_version(1),),
            references=(_reference(1),),
        ),
    )
    document_id = created.document.document_id

    updated = update_document_metadata(
        service=UpdateDocumentMetadataUseCase(unit_of_work=uow),
        request=UpdateDocumentMetadataRequest(
            document_id=document_id,
            document_title="API Doc Updated",
        ),
    )
    assert updated.document.document_title == "API Doc Updated"

    versioned = register_document_version(
        service=RegisterDocumentVersionUseCase(unit_of_work=uow),
        request=RegisterDocumentVersionRequest(document_id=document_id, version=_version(2)),
    )
    assert len(versioned.document.versions) == 2

    attached = attach_reference(
        service=AttachReferenceUseCase(unit_of_work=uow),
        request=AttachReferenceRequest(document_id=document_id, reference=_reference(2)),
    )
    assert len(attached.document.references) == 2

    loaded = get_document(
        service=GetDocumentUseCase(unit_of_work=uow),
        request=GetDocumentRequest(document_id=document_id),
    )
    assert loaded.document.document_id == document_id

    listed = list_documents(
        service=ListDocumentsUseCase(unit_of_work=uow),
        request=ListDocumentsRequest(),
    )
    assert any(item.document_id == document_id for item in listed.documents)

    searched = search_documents(
        service=SearchDocumentsUseCase(unit_of_work=uow),
        request=SearchDocumentsRequest(text="API Doc"),
    )
    assert any(item.document_id == document_id for item in searched.documents)

    archived = archive_document(
        service=ArchiveDocumentUseCase(unit_of_work=uow),
        request=ArchiveDocumentRequest(document_id=document_id, archived_at=_aware(2032, 2, 9, 8)),
    )
    assert archived.document.status == "ARCHIVED"

    removed = remove_reference(
        service=RemoveReferenceUseCase(unit_of_work=uow),
        request=RemoveReferenceRequest(
            document_id=document_id,
            reference_id=attached.document.references[0].reference_id,
        ),
    )
    assert len(removed.document.references) == 1

    deleted = delete_document(
        service=DeleteDocumentUseCase(unit_of_work=uow),
        request=DeleteDocumentRequest(document_id=document_id),
    )
    assert deleted.document_id == document_id


def test_feature_modules_do_not_reference_sqlalchemy_or_sqlite_repo() -> None:
    modules = [
        import_module("mfm.application.features.documents.create_document_feature"),
        import_module("mfm.application.features.documents.update_document_metadata_feature"),
        import_module("mfm.application.features.documents.register_document_version_feature"),
        import_module("mfm.application.features.documents.archive_document_feature"),
        import_module("mfm.application.features.documents.delete_document_feature"),
        import_module("mfm.application.features.documents.get_document_feature"),
        import_module("mfm.application.features.documents.list_documents_feature"),
        import_module("mfm.application.features.documents.search_documents_feature"),
        import_module("mfm.application.features.documents.attach_reference_feature"),
        import_module("mfm.application.features.documents.remove_reference_feature"),
    ]

    for module in modules:
        text = (module.__doc__ or "") + "\n" + "\n".join(sorted(module.__dict__.keys()))
        lowered = text.lower()
        assert "sqlalchemy" not in lowered
        assert "sqlitedocumentrepository" not in lowered
        assert "session" not in lowered
