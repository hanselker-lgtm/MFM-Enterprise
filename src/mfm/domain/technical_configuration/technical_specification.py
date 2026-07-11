"""Technical specification value objects."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeAlias

from mfm.common.value_object import ValueObject
from mfm.domain.technical_configuration.exceptions import InvalidTechnicalSpecificationError

SpecificationValue: TypeAlias = str | int | float | bool


@dataclass(frozen=True, slots=True)
class SpecificationEntry(ValueObject):
    """Single typed specification entry."""

    key: str
    value: SpecificationValue
    unit: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.key, str):
            raise InvalidTechnicalSpecificationError("specification key must be a string")
        normalized_key = self.key.strip()
        if not normalized_key:
            raise InvalidTechnicalSpecificationError("specification key cannot be empty")

        if not isinstance(self.value, (str, int, float, bool)):
            raise InvalidTechnicalSpecificationError(
                "specification value must be str/int/float/bool"
            )

        normalized_unit = None
        if self.unit is not None:
            if not isinstance(self.unit, str):
                raise InvalidTechnicalSpecificationError("specification unit must be string or None")
            normalized_unit = self.unit.strip() or None

        object.__setattr__(self, "key", normalized_key)
        object.__setattr__(self, "unit", normalized_unit)


@dataclass(frozen=True, slots=True)
class TechnicalSpecification(ValueObject):
    """Schema-bound and typed technical specification container."""

    schema_key: str
    entries: tuple[SpecificationEntry, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.schema_key, str):
            raise InvalidTechnicalSpecificationError("schema_key must be a string")
        normalized_schema = self.schema_key.strip().upper()
        if not normalized_schema:
            raise InvalidTechnicalSpecificationError("schema_key cannot be empty")

        normalized_entries: list[SpecificationEntry] = []
        seen_keys: set[str] = set()
        for entry in self.entries:
            normalized_entry = entry
            if not isinstance(entry, SpecificationEntry):
                try:
                    normalized_entry = SpecificationEntry(**entry)
                except Exception as exc:  # pragma: no cover - defensive conversion
                    raise InvalidTechnicalSpecificationError(
                        "entries must contain SpecificationEntry values"
                    ) from exc

            lowered = normalized_entry.key.casefold()
            if lowered in seen_keys:
                raise InvalidTechnicalSpecificationError(
                    f"duplicate specification key: {normalized_entry.key}"
                )
            seen_keys.add(lowered)
            normalized_entries.append(normalized_entry)

        object.__setattr__(self, "schema_key", normalized_schema)
        object.__setattr__(self, "entries", tuple(normalized_entries))

    def get(self, key: str) -> SpecificationValue | None:
        for entry in self.entries:
            if entry.key.casefold() == key.casefold():
                return entry.value
        return None
