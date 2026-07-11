"""Maintenance target value object."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.common.value_object import ValueObject
from mfm.domain.maintenance.exceptions import InvalidMaintenanceTargetError
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType


@dataclass(frozen=True, slots=True)
class MaintenanceTarget(ValueObject):
    """Identity reference to external maintenance target."""

    target_type: MaintenanceTargetType
    target_id: UUID

    def __post_init__(self) -> None:
        if not isinstance(self.target_type, MaintenanceTargetType):
            try:
                normalized = MaintenanceTargetType(str(self.target_type).upper())
            except Exception as exc:
                raise InvalidMaintenanceTargetError("target_type is invalid") from exc
            object.__setattr__(self, "target_type", normalized)

        if isinstance(self.target_id, str):
            try:
                normalized_id = UUID(self.target_id)
            except Exception as exc:
                raise InvalidMaintenanceTargetError("target_id must be UUID") from exc
            object.__setattr__(self, "target_id", normalized_id)
            return

        if not isinstance(self.target_id, UUID):
            raise InvalidMaintenanceTargetError("target_id must be UUID")
