"""In-process repository adapter for document archive aggregates."""

from __future__ import annotations

from copy import deepcopy
from uuid import UUID

from mfm.domain.document_archive.document import Document
from mfm.repositories.document_archive_repository import DocumentArchiveRepository


class SQLiteDocumentArchiveRepository(DocumentArchiveRepository):
    """Repository adapter preserving archive documents for process lifetime."""

    _store: dict[UUID, Document] = {}

    def get(self, document_id: UUID) -> Document | None:
        document = self._store.get(document_id)
        if document is None:
            return None
        return deepcopy(document)

    def save(self, document: Document) -> None:
        self._store[document.document_id] = deepcopy(document)

    def list(self) -> list[Document]:
        return [deepcopy(item) for item in self._store.values()]

    @classmethod
    def clear(cls) -> None:
        cls._store.clear()
