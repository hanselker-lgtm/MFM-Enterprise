"""
Organisation Entity.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Organisation:
    """
    Represents an organisation.
    """

    name: str

    cvr: str = ""

    vat: str = ""

    ean: str = ""

    industry: str = ""

    def __post_init__(self):

        self.name = self.name.strip()

        self.cvr = self.cvr.strip()

        self.vat = self.vat.strip()

        self.ean = self.ean.strip()

        self.industry = self.industry.strip()

    @property
    def display_name(self) -> str:

        return self.name

    def __str__(self):

        return self.name