"""
Base class for immutable Value Objects.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ValueObject:
    """
    Base class for immutable value objects.

    Value objects are compared by value rather than identity.
    """