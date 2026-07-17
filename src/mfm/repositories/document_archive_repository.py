"""Repository contract for CAP-006 document archive capability."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.document_archive.document import Document


class DocumentArchiveRepository(ABC):
    """Persistence contract for archive document aggregates."""

    @abstractmethod
    def get(self, document_id: UUID) -> Document | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, document: Document) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Document]:
        raise NotImplementedError
