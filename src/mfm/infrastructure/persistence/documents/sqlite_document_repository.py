"""SQLite repository for Document aggregates."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any
from typing import cast

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.domain.document.document import Document
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_repository import DocumentRepository
from mfm.domain.document.document_status import DocumentStatus
from mfm.infrastructure.persistence.documents.document_mapper import DocumentMapper
from mfm.infrastructure.persistence.documents.document_model import DocumentModel
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteDocumentRepository(DocumentRepository):
    """SQLAlchemy-backed repository for Document aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, document: Document) -> None:
        number = document.document_number.value
        if self._session.scalar(
            select(DocumentModel.id).where(DocumentModel.document_number == number)
        ) is not None:
            raise ValueError(f"Document number {number} already exists")

        self._session.add(DocumentMapper.to_orm_document(document))
        self._session.flush()

    def get(self, document_id: DocumentId) -> Document | None:
        normalized_id = self._normalize_document_id(document_id).value
        orm = self._session.scalar(self._base_query().where(DocumentModel.id == normalized_id))
        if orm is None:
            return None
        return DocumentMapper.to_domain_document(orm)

    def update(self, document: Document) -> None:
        existing = self._session.scalar(
            self._base_query().where(DocumentModel.id == document.id.value)
        )
        if existing is None:
            raise ValueError(f"Document {document.id.value} does not exist")

        duplicate = self._session.scalar(
            select(DocumentModel.id).where(
                DocumentModel.document_number == document.document_number.value,
                DocumentModel.id != document.id.value,
            )
        )
        if duplicate is not None:
            raise ValueError(f"Document number {document.document_number.value} already exists")

        if existing.version != document.version:
            raise ValueError(
                f"Document {document.id.value} version conflict: expected {existing.version}, got {document.version}"
            )

        existing.references.clear()
        self._session.flush()

        updated = DocumentMapper.to_orm_document(document)
        updated.version = document.version + 1
        self._session.merge(updated)
        self._session.flush()

    def remove(self, document_id: DocumentId) -> None:
        normalized_id = self._normalize_document_id(document_id).value
        orm = self._session.get(DocumentModel, normalized_id)
        if orm is None:
            raise ValueError(f"Document {normalized_id} does not exist")
        self._session.delete(orm)
        self._session.flush()

    def exists(self, document_id: DocumentId) -> bool:
        normalized_id = self._normalize_document_id(document_id).value
        return self._session.get(DocumentModel, normalized_id) is not None

    def get_by_number(self, document_number: DocumentNumber) -> Document | None:
        normalized = self._normalize_document_number(document_number).value
        orm = self._session.scalar(
            self._base_query().where(DocumentModel.document_number == normalized)
        )
        if orm is None:
            return None
        return DocumentMapper.to_domain_document(orm)

    def list(self, filters: Any | None = None) -> list[Document]:
        query = self._base_query()
        if isinstance(filters, Mapping):
            if "status" in filters and filters["status"] is not None:
                query = query.where(
                    DocumentModel.status == self._normalize_status(filters["status"])
                )

        orm_entities = self._session.scalars(
            query.order_by(DocumentModel.document_number, DocumentModel.document_created_at)
        ).unique().all()
        return [DocumentMapper.to_domain_document(orm) for orm in orm_entities]

    def search(self, criteria: Any) -> list[Any]:
        if isinstance(criteria, str):
            text = criteria.strip()
            filters: dict[str, Any] = {"text": text} if text else {}
        elif isinstance(criteria, Mapping):
            filters = dict(criteria)
        else:
            filters = {}

        query = select(DocumentModel)

        text = str(filters.get("text", "")).strip()
        if text:
            like_pattern = f"%{text}%"
            query = query.where(
                or_(
                    DocumentModel.document_number.ilike(like_pattern),
                    DocumentModel.document_title.ilike(like_pattern),
                    DocumentModel.document_type.ilike(like_pattern),
                    DocumentModel.description.ilike(like_pattern),
                )
            )

        status = filters.get("status")
        if status is not None:
            query = query.where(DocumentModel.status == self._normalize_status(status))

        target_capability = filters.get("target_capability")
        if target_capability is not None:
            normalized_target = str(target_capability).strip().upper()
            query = query.where(
                DocumentModel.references.any(target_capability=normalized_target)
            )

        entities = self._session.scalars(
            query.order_by(DocumentModel.document_number, DocumentModel.document_created_at)
        ).unique().all()

        return [
            {
                "id": orm.id,
                "document_number": orm.document_number,
                "document_title": orm.document_title,
                "document_type": orm.document_type,
                "status": orm.status,
            }
            for orm in entities
        ]

    def next_identity(self) -> DocumentId:
        return DocumentId.new()

    def list_by_status(self, status: DocumentStatus) -> list[Document]:
        normalized_status = self._normalize_status(status)
        orm_entities = self._session.scalars(
            self._base_query()
            .where(DocumentModel.status == normalized_status)
            .order_by(DocumentModel.document_number, DocumentModel.document_created_at)
        ).unique().all()
        return [DocumentMapper.to_domain_document(orm) for orm in orm_entities]

    @staticmethod
    def _normalize_document_id(document_id: DocumentId) -> DocumentId:
        if isinstance(document_id, DocumentId):
            return document_id
        return DocumentId(document_id)

    @staticmethod
    def _normalize_document_number(document_number: DocumentNumber | str) -> DocumentNumber:
        if isinstance(document_number, DocumentNumber):
            return document_number
        return DocumentNumber(document_number)

    @staticmethod
    def _normalize_status(status: DocumentStatus | str) -> DocumentStatus:
        if isinstance(status, DocumentStatus):
            return status
        return DocumentStatus(str(status).upper())

    @staticmethod
    def _base_query():
        return select(DocumentModel).options(
            joinedload(DocumentModel.references),
        )
