"""Board term value object."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from mfm.common.value_object import ValueObject
from mfm.domain.organization.exceptions import InvalidBoardTermError


@dataclass(frozen=True, slots=True)
class BoardTerm(ValueObject):
    """Value object representing a board election period."""

    term_start: date
    term_end: date

    def __post_init__(self) -> None:
        if not isinstance(self.term_start, date) or not isinstance(self.term_end, date):
            raise InvalidBoardTermError("term_start and term_end must be date values")
        if self.term_start > self.term_end:
            raise InvalidBoardTermError("term_start must be <= term_end")

    def includes(self, value: date) -> bool:
        return self.term_start <= value <= self.term_end

    def overlaps(self, start: date, end: date | None) -> bool:
        effective_end = end or self.term_end
        return start <= self.term_end and effective_end >= self.term_start
