"""Identity value objects for maintenance domain."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class MaintenancePlanId(ValueObject):
    """Identity for maintenance plan aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("MaintenancePlanId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "MaintenancePlanId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class MaintenanceRequirementId(ValueObject):
    """Identity for maintenance requirement entity."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError(
                "MaintenanceRequirementId value must be UUID or UUID string"
            )

    @classmethod
    def new(cls) -> "MaintenanceRequirementId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class WorkOrderId(ValueObject):
    """Identity for work order aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("WorkOrderId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "WorkOrderId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class MaintenanceRecordId(ValueObject):
    """Identity for immutable maintenance completion record."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("MaintenanceRecordId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "MaintenanceRecordId":
        return cls(uuid4())
