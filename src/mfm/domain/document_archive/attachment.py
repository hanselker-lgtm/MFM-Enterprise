"""Attachment reference entity for document archive capability."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Attachment:
    """Cross-capability attachment reference."""

    target_capability: str
    target_aggregate_type: str
    target_aggregate_id: str
    description: str | None = None

    def __post_init__(self) -> None:
        self.target_capability = str(self.target_capability).strip().upper()
        if not self.target_capability:
            raise ValueError("target_capability cannot be empty")

        self.target_aggregate_type = str(self.target_aggregate_type).strip().upper()
        if not self.target_aggregate_type:
            raise ValueError("target_aggregate_type cannot be empty")

        self.target_aggregate_id = str(self.target_aggregate_id).strip()
        if not self.target_aggregate_id:
            raise ValueError("target_aggregate_id cannot be empty")

        if self.description is not None:
            self.description = str(self.description).strip() or None
