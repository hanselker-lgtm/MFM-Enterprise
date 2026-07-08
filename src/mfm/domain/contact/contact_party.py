"""
Common protocol for all contact parties.
"""

from __future__ import annotations

from typing import Protocol


class ContactParty(Protocol):

    @property
    def display_name(self) -> str:
        """Return the name shown throughout the application."""
        ...