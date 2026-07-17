"""Postal address value object for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostalAddress:
    """Immutable postal address."""

    line1: str
    postal_code: str
    city: str
    country: str
    line2: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.line1, str) or not self.line1.strip():
            raise ValueError("line1 must be a non-empty string")
        if not isinstance(self.postal_code, str) or not self.postal_code.strip():
            raise ValueError("postal_code must be a non-empty string")
        if not isinstance(self.city, str) or not self.city.strip():
            raise ValueError("city must be a non-empty string")
        if not isinstance(self.country, str) or not self.country.strip():
            raise ValueError("country must be a non-empty string")
        if not isinstance(self.line2, str):
            raise ValueError("line2 must be a string")

        object.__setattr__(self, "line1", self.line1.strip())
        object.__setattr__(self, "postal_code", self.postal_code.strip())
        object.__setattr__(self, "city", self.city.strip())
        object.__setattr__(self, "country", self.country.strip())
        object.__setattr__(self, "line2", self.line2.strip())
