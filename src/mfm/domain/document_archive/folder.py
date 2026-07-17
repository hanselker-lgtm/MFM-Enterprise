"""Folder entity for document archive capability."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class Folder:
    """Represents one logical archive folder."""

    name: str
    path: str
    folder_id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        self.name = str(self.name).strip()
        if not self.name:
            raise ValueError("folder name cannot be empty")

        self.path = str(self.path).strip()
        if not self.path:
            raise ValueError("folder path cannot be empty")

        if not isinstance(self.folder_id, UUID):
            self.folder_id = UUID(str(self.folder_id))
