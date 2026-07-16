"""Document cross-capability reference entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

from mfm.domain.document.exceptions import InvalidDocumentReferenceError


@dataclass(slots=True)
class DocumentReference:
    """Reference metadata aligned to the cross-capability reference contract."""

    target_capability: str
    target_aggregate_type: str
    target_aggregate_id: str
    exists: bool
    authorized: bool
    is_soft_deleted: bool
    is_archived: bool
    checked_at: datetime = field(default_factory=lambda: datetime.now(tz=UTC))
    description: str | None = None
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            self.id = UUID(str(self.id))

        self.target_capability = str(self.target_capability).strip().upper()
        if not self.target_capability:
            raise InvalidDocumentReferenceError("target_capability cannot be empty")

        self.target_aggregate_type = str(self.target_aggregate_type).strip().upper()
        if not self.target_aggregate_type:
            raise InvalidDocumentReferenceError("target_aggregate_type cannot be empty")

        self.target_aggregate_id = str(self.target_aggregate_id).strip()
        if not self.target_aggregate_id:
            raise InvalidDocumentReferenceError("target_aggregate_id cannot be empty")

        if self.description is not None:
            self.description = str(self.description).strip() or None

        if self.checked_at.tzinfo is None:
            raise InvalidDocumentReferenceError("checked_at must be timezone-aware")
        self.checked_at = self.checked_at.astimezone(UTC)

        if not self.exists:
            raise InvalidDocumentReferenceError("target reference does not exist")
        if not self.authorized:
            raise InvalidDocumentReferenceError("target reference is not authorized")
        if self.is_soft_deleted:
            raise InvalidDocumentReferenceError("target reference is soft-deleted")
        if self.is_archived:
            raise InvalidDocumentReferenceError("target reference is archived")
