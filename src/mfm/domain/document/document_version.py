"""Document version entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime

from mfm.domain.document.exceptions import InvalidDocumentVersionError


@dataclass(slots=True)
class DocumentVersion:
    """Immutable version metadata owned by the Document aggregate."""

    version_number: int
    storage_key: str
    file_name: str | None = None
    mime_type: str | None = None
    checksum: str | None = None
    size_bytes: int | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(tz=UTC))

    def __post_init__(self) -> None:
        if int(self.version_number) < 1:
            raise InvalidDocumentVersionError("version_number must be greater than zero")
        self.version_number = int(self.version_number)

        self.storage_key = str(self.storage_key).strip()
        if not self.storage_key:
            raise InvalidDocumentVersionError("storage_key cannot be empty")

        if self.file_name is not None:
            self.file_name = str(self.file_name).strip() or None

        if self.mime_type is not None:
            self.mime_type = str(self.mime_type).strip() or None

        if self.checksum is not None:
            self.checksum = str(self.checksum).strip() or None

        if self.size_bytes is not None:
            self.size_bytes = int(self.size_bytes)
            if self.size_bytes < 0:
                raise InvalidDocumentVersionError("size_bytes cannot be negative")

        if self.created_at.tzinfo is None:
            raise InvalidDocumentVersionError("created_at must be timezone-aware")
        self.created_at = self.created_at.astimezone(UTC)
