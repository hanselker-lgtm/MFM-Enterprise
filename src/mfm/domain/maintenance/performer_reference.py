"""Performer reference value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.maintenance.exceptions import InvalidPerformerReferenceError
from mfm.domain.maintenance.performer_reference_type import PerformerReferenceType


@dataclass(frozen=True, slots=True)
class PerformerReference(ValueObject):
    """Identity-only performer reference for work orders."""

    performer_type: PerformerReferenceType
    performer_id_or_external_key: str
    display_name_snapshot: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.performer_type, PerformerReferenceType):
            try:
                normalized = PerformerReferenceType(str(self.performer_type).upper())
            except Exception as exc:
                raise InvalidPerformerReferenceError("performer_type is invalid") from exc
            object.__setattr__(self, "performer_type", normalized)

        if (
            not isinstance(self.performer_id_or_external_key, str)
            or not self.performer_id_or_external_key.strip()
        ):
            raise InvalidPerformerReferenceError(
                "performer_id_or_external_key must be a non-empty string"
            )

        object.__setattr__(
            self,
            "performer_id_or_external_key",
            self.performer_id_or_external_key.strip(),
        )

        if self.display_name_snapshot is not None:
            if not isinstance(self.display_name_snapshot, str):
                raise InvalidPerformerReferenceError(
                    "display_name_snapshot must be string or None"
                )
            object.__setattr__(
                self,
                "display_name_snapshot",
                self.display_name_snapshot.strip() or None,
            )
