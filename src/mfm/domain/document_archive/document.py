"""Document aggregate for CAP-006 document archive capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID

from mfm.domain.document_archive.archive import Archive
from mfm.domain.document_archive.attachment import Attachment
from mfm.domain.document_archive.category import Category
from mfm.domain.document_archive.folder import Folder
from mfm.domain.document_archive.version import Version


@dataclass(slots=True)
class Document:
    """Archive document aggregate root."""

    document_id: UUID
    document_number: str
    document_title: str
    document_type: str
    status: str
    folder: Folder
    category: Category
    versions: list[Version] = field(default_factory=list)
    attachments: list[Attachment] = field(default_factory=list)
    archive: Archive | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.document_id, UUID):
            self.document_id = UUID(str(self.document_id))

        self.document_number = str(self.document_number).strip().upper()
        if not self.document_number:
            raise ValueError("document_number cannot be empty")

        self.document_title = str(self.document_title).strip()
        if not self.document_title:
            raise ValueError("document_title cannot be empty")

        self.document_type = str(self.document_type).strip().upper()
        if not self.document_type:
            raise ValueError("document_type cannot be empty")

        self.status = str(self.status).strip().upper()
        if not self.status:
            raise ValueError("status cannot be empty")

        if not isinstance(self.folder, Folder):
            raise ValueError("folder must be Folder")
        if not isinstance(self.category, Category):
            raise ValueError("category must be Category")

        self.versions = list(self.versions)
        self.attachments = list(self.attachments)

    def add_version(self, version: Version) -> None:
        if any(item.version_number == version.version_number for item in self.versions):
            raise ValueError(f"Version {version.version_number} already exists")
        self.versions.append(version)

    def add_attachment(self, attachment: Attachment) -> None:
        duplicate = any(
            item.target_capability == attachment.target_capability
            and item.target_aggregate_type == attachment.target_aggregate_type
            and item.target_aggregate_id == attachment.target_aggregate_id
            for item in self.attachments
        )
        if duplicate:
            raise ValueError("attachment target already exists")
        self.attachments.append(attachment)

    def mark_archived(self, archive: Archive) -> None:
        self.archive = archive
        self.status = "ARCHIVED"
