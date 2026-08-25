"""Aging bucket value object for accounts receivable analysis."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.domain.finance.money import Money


@dataclass(frozen=True, slots=True)
class AgingBucket:
    """Represents one aging interval with aggregated outstanding amount."""

    label: str
    amount: Money
    invoice_count: int
