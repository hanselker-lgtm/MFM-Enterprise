"""Supporting value objects for technical configuration domain."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class ManufacturerName(ValueObject):
    """Canonical manufacturer name value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("manufacturer must be a string")
        normalized = self.value.strip()
        if not normalized:
            raise ValueError("manufacturer cannot be empty")
        object.__setattr__(self, "value", normalized)


@dataclass(frozen=True, slots=True)
class ComponentModelName(ValueObject):
    """Canonical component model value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("model must be a string")
        normalized = self.value.strip()
        if not normalized:
            raise ValueError("model cannot be empty")
        object.__setattr__(self, "value", normalized)


@dataclass(frozen=True, slots=True)
class SerialNumber(ValueObject):
    """Canonical serial number value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("serial_number must be a string")
        normalized = self.value.strip().upper()
        if not normalized:
            raise ValueError("serial_number cannot be empty")
        object.__setattr__(self, "value", normalized)


@dataclass(frozen=True, slots=True)
class BuildYear(ValueObject):
    """Build year value object."""

    value: int

    def __post_init__(self) -> None:
        if not isinstance(self.value, int):
            raise TypeError("build_year must be an integer")
        if self.value <= 0:
            raise ValueError("build_year must be positive")


@dataclass(frozen=True, slots=True)
class ComponentNotes(ValueObject):
    """Technical component notes value object."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("notes must be a string")
        object.__setattr__(self, "value", self.value.strip())


@dataclass(frozen=True, slots=True)
class ReplacementReason(ValueObject):
    """Reason text for component replacement."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("reason must be a string")
        normalized = self.value.strip()
        if not normalized:
            raise ValueError("reason cannot be empty")
        object.__setattr__(self, "value", normalized)
