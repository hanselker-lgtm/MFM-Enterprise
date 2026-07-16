"""Posting date value object for accounting."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from mfm.common.value_object import ValueObject
from mfm.domain.accounting.exceptions import InvalidJournalReferenceError


@dataclass(frozen=True, slots=True)
class PostingDate(ValueObject):
    """Immutable posting date wrapper."""

    value: date

    def __post_init__(self) -> None:
        if not isinstance(self.value, date):
            raise InvalidJournalReferenceError("posting_date must be a date")

    @property
    def year(self) -> int:
        return self.value.year
