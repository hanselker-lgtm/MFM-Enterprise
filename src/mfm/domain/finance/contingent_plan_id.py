"""Identifier value object for finance contingent plans."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject
from mfm.domain.finance.exceptions import InvalidContingentPlanReferenceError


@dataclass(frozen=True, slots=True)
class ContingentPlanId(ValueObject):
    """Strongly typed identity for ContingentPlan aggregate."""

    value: UUID | str

    def __post_init__(self) -> None:
        raw_value = self.value

        if isinstance(raw_value, UUID):
            normalized = raw_value
        elif isinstance(raw_value, str):
            try:
                normalized = UUID(raw_value)
            except ValueError as exc:
                raise InvalidContingentPlanReferenceError(
                    "id must be a valid UUID"
                ) from exc
        else:
            raise InvalidContingentPlanReferenceError("id must be a UUID or UUID string")

        object.__setattr__(self, "value", normalized)

    @classmethod
    def new(cls) -> "ContingentPlanId":
        return cls(value=uuid4())

    def __str__(self) -> str:
        return str(self.value)
