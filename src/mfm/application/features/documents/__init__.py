"""Documents public feature API."""

from mfm.application.features.documents.archive_document_feature import ArchiveDocumentFeature
from mfm.application.features.documents.archive_document_feature import ArchiveDocumentRequest
from mfm.application.features.documents.archive_document_feature import ArchiveDocumentResponse
from mfm.application.features.documents.archive_document_feature import ArchiveDocumentService
from mfm.application.features.documents.attach_reference_feature import AttachReferenceFeature
from mfm.application.features.documents.attach_reference_feature import AttachReferenceRequest
from mfm.application.features.documents.attach_reference_feature import AttachReferenceResponse
from mfm.application.features.documents.attach_reference_feature import AttachReferenceService
from mfm.application.features.documents.create_document_feature import ApplicationException
from mfm.application.features.documents.create_document_feature import BusinessRuleViolation
from mfm.application.features.documents.create_document_feature import CreateDocumentFeature
from mfm.application.features.documents.create_document_feature import CreateDocumentRequest
from mfm.application.features.documents.create_document_feature import CreateDocumentResponse
from mfm.application.features.documents.create_document_feature import CreateDocumentService
from mfm.application.features.documents.create_document_feature import DocumentReferenceInput
from mfm.application.features.documents.create_document_feature import (
    DocumentReferenceResponse,
)
from mfm.application.features.documents.create_document_feature import DocumentResponse
from mfm.application.features.documents.create_document_feature import (
    DocumentSearchResultResponse,
)
from mfm.application.features.documents.create_document_feature import DocumentVersionInput
from mfm.application.features.documents.create_document_feature import DocumentVersionResponse
from mfm.application.features.documents.create_document_feature import RepositoryException
from mfm.application.features.documents.create_document_feature import ValidationException
from mfm.application.features.documents.delete_document_feature import DeleteDocumentFeature
from mfm.application.features.documents.delete_document_feature import DeleteDocumentRequest
from mfm.application.features.documents.delete_document_feature import DeleteDocumentResponse
from mfm.application.features.documents.delete_document_feature import DeleteDocumentService
from mfm.application.features.documents.get_document_feature import GetDocumentFeature
from mfm.application.features.documents.get_document_feature import GetDocumentRequest
from mfm.application.features.documents.get_document_feature import GetDocumentResponse
from mfm.application.features.documents.get_document_feature import GetDocumentService
from mfm.application.features.documents.list_documents_feature import ListDocumentsFeature
from mfm.application.features.documents.list_documents_feature import ListDocumentsRequest
from mfm.application.features.documents.list_documents_feature import ListDocumentsResponse
from mfm.application.features.documents.list_documents_feature import ListDocumentsService
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionFeature,
)
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionRequest,
)
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionResponse,
)
from mfm.application.features.documents.register_document_version_feature import (
    RegisterDocumentVersionService,
)
from mfm.application.features.documents.remove_reference_feature import RemoveReferenceFeature
from mfm.application.features.documents.remove_reference_feature import RemoveReferenceRequest
from mfm.application.features.documents.remove_reference_feature import (
    RemoveReferenceResponse,
)
from mfm.application.features.documents.remove_reference_feature import RemoveReferenceService
from mfm.application.features.documents.search_documents_feature import SearchDocumentsFeature
from mfm.application.features.documents.search_documents_feature import SearchDocumentsRequest
from mfm.application.features.documents.search_documents_feature import SearchDocumentsResponse
from mfm.application.features.documents.search_documents_feature import SearchDocumentsService
from mfm.application.features.documents.update_document_metadata_feature import (
    UpdateDocumentMetadataFeature,
)
from mfm.application.features.documents.update_document_metadata_feature import (
    UpdateDocumentMetadataRequest,
)
from mfm.application.features.documents.update_document_metadata_feature import (
    UpdateDocumentMetadataResponse,
)
from mfm.application.features.documents.update_document_metadata_feature import (
    UpdateDocumentMetadataService,
)


def create_document(*, service: CreateDocumentService, request: CreateDocumentRequest) -> CreateDocumentResponse:
    return CreateDocumentFeature(service=service).execute(request)


def update_document_metadata(
    *,
    service: UpdateDocumentMetadataService,
    request: UpdateDocumentMetadataRequest,
) -> UpdateDocumentMetadataResponse:
    return UpdateDocumentMetadataFeature(service=service).execute(request)


def register_document_version(
    *,
    service: RegisterDocumentVersionService,
    request: RegisterDocumentVersionRequest,
) -> RegisterDocumentVersionResponse:
    return RegisterDocumentVersionFeature(service=service).execute(request)


def archive_document(*, service: ArchiveDocumentService, request: ArchiveDocumentRequest) -> ArchiveDocumentResponse:
    return ArchiveDocumentFeature(service=service).execute(request)


def delete_document(*, service: DeleteDocumentService, request: DeleteDocumentRequest) -> DeleteDocumentResponse:
    return DeleteDocumentFeature(service=service).execute(request)


def get_document(*, service: GetDocumentService, request: GetDocumentRequest) -> GetDocumentResponse:
    return GetDocumentFeature(service=service).execute(request)


def list_documents(*, service: ListDocumentsService, request: ListDocumentsRequest) -> ListDocumentsResponse:
    return ListDocumentsFeature(service=service).execute(request)


def search_documents(*, service: SearchDocumentsService, request: SearchDocumentsRequest) -> SearchDocumentsResponse:
    return SearchDocumentsFeature(service=service).execute(request)


def attach_reference(*, service: AttachReferenceService, request: AttachReferenceRequest) -> AttachReferenceResponse:
    return AttachReferenceFeature(service=service).execute(request)


def remove_reference(*, service: RemoveReferenceService, request: RemoveReferenceRequest) -> RemoveReferenceResponse:
    return RemoveReferenceFeature(service=service).execute(request)


__all__ = [
    "ApplicationException",
    "ArchiveDocumentFeature",
    "ArchiveDocumentRequest",
    "ArchiveDocumentResponse",
    "ArchiveDocumentService",
    "BusinessRuleViolation",
    "CreateDocumentFeature",
    "CreateDocumentRequest",
    "CreateDocumentResponse",
    "CreateDocumentService",
    "DeleteDocumentFeature",
    "DeleteDocumentRequest",
    "DeleteDocumentResponse",
    "DeleteDocumentService",
    "DocumentReferenceInput",
    "DocumentReferenceResponse",
    "DocumentResponse",
    "DocumentSearchResultResponse",
    "DocumentVersionInput",
    "DocumentVersionResponse",
    "GetDocumentFeature",
    "GetDocumentRequest",
    "GetDocumentResponse",
    "GetDocumentService",
    "ListDocumentsFeature",
    "ListDocumentsRequest",
    "ListDocumentsResponse",
    "ListDocumentsService",
    "RegisterDocumentVersionFeature",
    "RegisterDocumentVersionRequest",
    "RegisterDocumentVersionResponse",
    "RegisterDocumentVersionService",
    "RemoveReferenceFeature",
    "RemoveReferenceRequest",
    "RemoveReferenceResponse",
    "RemoveReferenceService",
    "RepositoryException",
    "SearchDocumentsFeature",
    "SearchDocumentsRequest",
    "SearchDocumentsResponse",
    "SearchDocumentsService",
    "UpdateDocumentMetadataFeature",
    "UpdateDocumentMetadataRequest",
    "UpdateDocumentMetadataResponse",
    "UpdateDocumentMetadataService",
    "ValidationException",
    "archive_document",
    "attach_reference",
    "create_document",
    "delete_document",
    "get_document",
    "list_documents",
    "register_document_version",
    "remove_reference",
    "search_documents",
    "update_document_metadata",
]
