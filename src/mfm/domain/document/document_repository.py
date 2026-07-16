"""Repository contract for documents."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any

from mfm.domain.document.document import Document
from mfm.domain.document.document_id import DocumentId
from mfm.domain.document.document_number import DocumentNumber
from mfm.domain.document.document_status import DocumentStatus


class DocumentRepository(ABC):
    """Repository contract for persisting Document aggregates."""

    @abstractmethod
    def add(self, document: Document) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, document: Document) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove(self, document_id: DocumentId) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, document_id: DocumentId) -> Document | None:
        raise NotImplementedError

    @abstractmethod
    def exists(self, document_id: DocumentId) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_by_number(self, document_number: DocumentNumber) -> Document | None:
        raise NotImplementedError

    @abstractmethod
    def list(self, filters: Any | None = None) -> list[Document]:
        raise NotImplementedError

    @abstractmethod
    def search(self, criteria: Any) -> list[Any]:
        raise NotImplementedError

    @abstractmethod
    def next_identity(self) -> DocumentId:
        raise NotImplementedError

    @abstractmethod
    def list_by_status(self, status: DocumentStatus) -> list[Document]:
        raise NotImplementedError
