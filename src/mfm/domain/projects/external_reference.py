"""Project external reference entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from uuid import UUID
from uuid import uuid4

from mfm.domain.projects.reference_type import ReferenceType


@dataclass(slots=True)
class ExternalReference:
    """Cross-capability reference owned by the Project aggregate."""

    reference_type: ReferenceType
    external_id: UUID
    description: str | None = None
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(tz=UTC))

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            self.id = UUID(str(self.id))

        if not isinstance(self.reference_type, ReferenceType):
            self.reference_type = ReferenceType(str(self.reference_type).upper())

        if not isinstance(self.external_id, UUID):
            self.external_id = UUID(str(self.external_id))

        if self.description is not None:
            self.description = str(self.description).strip() or None

        if self.created_at.tzinfo is None:
            self.created_at = self.created_at.replace(tzinfo=UTC)
        else:
            self.created_at = self.created_at.astimezone(UTC)
