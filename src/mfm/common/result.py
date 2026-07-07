"""
Generic Result type.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class Result(Generic[T]):
    success: bool
    value: T | None = None
    message: str = ""

    @classmethod
    def ok(cls, value: T | None = None) -> "Result[T]":
        return cls(True, value=value)

    @classmethod
    def fail(cls, message: str) -> "Result[T]":
        return cls(False, message=message)