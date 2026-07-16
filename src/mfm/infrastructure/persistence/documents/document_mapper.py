"""Mapper between document domain and persistence models."""

from __future__ import annotations

from datetime import UTC
from datetime import datetime

from mfm.domain.document.document import Document
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_reference import DocumentReference
from mfm.domain.document.document_title import DocumentTitle
from mfm.domain.document.document_type import DocumentType
from mfm.domain.document.document_version import DocumentVersion
from mfm.infrastructure.persistence.documents.document_model import DocumentModel
from mfm.infrastructure.persistence.documents.document_reference_model import (
    DocumentReferenceModel,
)


class DocumentMapper:
    """Map Document aggregate to/from SQLAlchemy models."""

    @staticmethod
    def to_orm_document(document: Document) -> DocumentModel:
        orm = DocumentModel(
            id=document.id.value,
            document_number=document.document_number.value,
            document_title=document.document_title.value,
            document_type=document.document_type.value,
            description=document.description,
            status=document.status,
            document_created_at=document.created_at,
            document_updated_at=document.updated_at,
            archived_at=document.archived_at,
            disposed_at=document.disposed_at,
            version=document.version,
        )

        for version_order, version in enumerate(document.versions):
            orm.references.append(
                DocumentReferenceModel(
                    document_id=document.id.value,
                    reference_order=None,
                    version_order=version_order,
                    has_version=True,
                    has_reference=False,
                    version_number=version.version_number,
                    storage_key=version.storage_key,
                    file_name=version.file_name,
                    mime_type=version.mime_type,
                    checksum=version.checksum,
                    size_bytes=version.size_bytes,
                    version_created_at=version.created_at,
                    target_capability=None,
                    target_aggregate_type=None,
                    target_aggregate_id=None,
                    exists=None,
                    authorized=None,
                    is_soft_deleted=None,
                    is_archived=None,
                    checked_at=None,
                    description=None,
                )
            )

        for reference_order, reference in enumerate(document.references):
            orm.references.append(
                DocumentReferenceModel(
                    id=reference.id,
                    document_id=document.id.value,
                    reference_order=reference_order,
                    version_order=None,
                    has_version=False,
                    has_reference=True,
                    version_number=None,
                    storage_key=None,
                    file_name=None,
                    mime_type=None,
                    checksum=None,
                    size_bytes=None,
                    version_created_at=None,
                    target_capability=reference.target_capability,
                    target_aggregate_type=reference.target_aggregate_type,
                    target_aggregate_id=reference.target_aggregate_id,
                    exists=reference.exists,
                    authorized=reference.authorized,
                    is_soft_deleted=reference.is_soft_deleted,
                    is_archived=reference.is_archived,
                    checked_at=reference.checked_at,
                    description=reference.description,
                )
            )

        return orm

    @staticmethod
    def to_domain_document(orm: DocumentModel) -> Document:
        version_rows = sorted(
            [item for item in orm.references if item.has_version],
            key=lambda item: (item.version_order is None, item.version_order, item.version_number),
        )
        reference_rows = sorted(
            [item for item in orm.references if item.has_reference],
            key=lambda item: (item.reference_order is None, item.reference_order),
        )

        versions = [
            DocumentVersion(
                version_number=version_orm.version_number,
                storage_key=version_orm.storage_key,
                file_name=version_orm.file_name,
                mime_type=version_orm.mime_type,
                checksum=version_orm.checksum,
                size_bytes=version_orm.size_bytes,
                created_at=DocumentMapper._normalize_timestamp(version_orm.version_created_at),
            )
            for version_orm in version_rows
        ]

        references = [
            DocumentReference(
                id=reference_orm.id,
                target_capability=reference_orm.target_capability,
                target_aggregate_type=reference_orm.target_aggregate_type,
                target_aggregate_id=reference_orm.target_aggregate_id,
                exists=reference_orm.exists,
                authorized=reference_orm.authorized,
                is_soft_deleted=reference_orm.is_soft_deleted,
                is_archived=reference_orm.is_archived,
                checked_at=DocumentMapper._normalize_timestamp(reference_orm.checked_at),
                description=reference_orm.description,
            )
            for reference_orm in reference_rows
        ]

        document = Document(
            id=DocumentId(orm.id),
            document_number=DocumentNumber(orm.document_number),
            document_title=DocumentTitle(orm.document_title),
            document_type=DocumentType(orm.document_type),
            status=orm.status,
            description=orm.description,
            created_at=DocumentMapper._normalize_timestamp(orm.document_created_at),
            updated_at=DocumentMapper._normalize_timestamp_or_none(orm.document_updated_at),
            archived_at=DocumentMapper._normalize_timestamp_or_none(orm.archived_at),
            disposed_at=DocumentMapper._normalize_timestamp_or_none(orm.disposed_at),
            versions=versions,
            references=references,
        )
        document.version = orm.version
        document.pull_events()
        return document

    @staticmethod
    def _normalize_timestamp(value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

    @staticmethod
    def _normalize_timestamp_or_none(value: datetime | None) -> datetime | None:
        if value is None:
            return None
        return DocumentMapper._normalize_timestamp(value)
