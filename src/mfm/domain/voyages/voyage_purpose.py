"""Voyage purpose value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.voyages.exceptions import InvalidVoyagePurposeError
from mfm.domain.voyages.voyage_purpose_code import VoyagePurposeCode


@dataclass(frozen=True, slots=True)
class VoyagePurpose(ValueObject):
    """Controlled voyage purpose with optional detail text."""

    purpose_code: VoyagePurposeCode
    purpose_detail: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.purpose_code, VoyagePurposeCode):
            try:
                normalized_code = VoyagePurposeCode(str(self.purpose_code).upper())
            except Exception as exc:
                raise InvalidVoyagePurposeError("purpose_code is invalid") from exc
            object.__setattr__(self, "purpose_code", normalized_code)

        if self.purpose_detail is not None:
            if not isinstance(self.purpose_detail, str):
                raise InvalidVoyagePurposeError(
                    "purpose_detail must be string or None"
                )
            normalized_detail = self.purpose_detail.strip() or None
            object.__setattr__(self, "purpose_detail", normalized_detail)