"""Identity value objects for technical configuration domain."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class TechnicalConfigurationId(ValueObject):
    """Identity value object for TechnicalConfiguration aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("TechnicalConfigurationId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "TechnicalConfigurationId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class TechnicalComponentId(ValueObject):
    """Identity value object for TechnicalComponent entity."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("TechnicalComponentId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "TechnicalComponentId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class ComponentLinkId(ValueObject):
    """Identity value object for component link entity."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("ComponentLinkId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "ComponentLinkId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class ComponentReplacementRecordId(ValueObject):
    """Identity value object for replacement record entity."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError(
                "ComponentReplacementRecordId value must be UUID or UUID string"
            )

    @classmethod
    def new(cls) -> "ComponentReplacementRecordId":
        return cls(uuid4())
