"""Reporting service for CAP-006 document archive capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol

from mfm.application.reporting.models.document_archive_summary_dto import (
    DocumentArchiveIntegrationDTO,
)
from mfm.application.reporting.models.document_archive_summary_dto import (
    DocumentArchiveSummaryItemDTO,
)
from mfm.application.reporting.models.document_archive_summary_dto import (
    DocumentArchiveSummaryResponse,
)
from mfm.domain.document_archive.document import Document


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when repository dependencies fail."""


@dataclass(frozen=True, slots=True)
class DocumentArchiveSummaryRequest:
    include_archived: bool = True

    def validate(self) -> None:
        if not isinstance(self.include_archived, bool):
            raise ValidationException("include_archived must be bool")


class DocumentArchiveRepositoryPort(Protocol):
    def list(self) -> list[Document]: ...


class DocumentArchiveSummaryService:
    """Build summary metrics from document archive aggregates."""

    def __init__(self, *, repository: DocumentArchiveRepositoryPort) -> None:
        self._repository = repository

    def execute(self, request: DocumentArchiveSummaryRequest) -> DocumentArchiveSummaryResponse:
        request.validate()

        try:
            documents = self._repository.list()
        except ValidationException:
            raise
        except Exception as exc:
            raise RepositoryException("Document archive summary retrieval failed") from exc

        items: list[DocumentArchiveSummaryItemDTO] = []
        integration_counts = {
            "MEMBERSHIP": 0,
            "ORGANIZATION": 0,
            "EVENTS": 0,
            "BILLING": 0,
            "PROJECTS": 0,
        }

        for document in documents:
            if not request.include_archived and document.archive is not None:
                continue

            items.append(
                DocumentArchiveSummaryItemDTO(
                    category_code=document.category.code,
                    folder_path=document.folder.path,
                    status=document.status,
                    versions_count=len(document.versions),
                    attachments_count=len(document.attachments),
                )
            )

            for attachment in document.attachments:
                if attachment.target_capability in integration_counts:
                    integration_counts[attachment.target_capability] += 1

        return DocumentArchiveSummaryResponse(
            documents=tuple(items),
            integration=DocumentArchiveIntegrationDTO(
                membership_links=integration_counts["MEMBERSHIP"],
                organization_links=integration_counts["ORGANIZATION"],
                events_links=integration_counts["EVENTS"],
                billing_links=integration_counts["BILLING"],
                projects_links=integration_counts["PROJECTS"],
            ),
            generated_at=datetime.now(UTC),
        )
