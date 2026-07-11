"""Certificate compliance observation value object."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from mfm.common.value_object import ValueObject
from mfm.domain.certificates.exceptions import InvalidComplianceObservationError


@dataclass(frozen=True, slots=True)
class ComplianceObservation(ValueObject):
    """Certificate-scoped compliance/inspection observation."""

    summary: str
    observed_on: date
    requires_maintenance_work: bool = False

    def __post_init__(self) -> None:
        if not isinstance(self.summary, str):
            raise InvalidComplianceObservationError("summary must be string")
        normalized_summary = self.summary.strip()
        if not normalized_summary:
            raise InvalidComplianceObservationError("summary must be non-empty")
        object.__setattr__(self, "summary", normalized_summary)

        if not isinstance(self.observed_on, date):
            raise InvalidComplianceObservationError("observed_on must be date")

        if not isinstance(self.requires_maintenance_work, bool):
            raise InvalidComplianceObservationError(
                "requires_maintenance_work must be bool"
            )
