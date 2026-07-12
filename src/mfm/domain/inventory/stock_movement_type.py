"""Inventory stock movement type enum."""

from enum import StrEnum


class StockMovementType(StrEnum):
    """Supported stock movement types for CAP-12 first scope."""

    RECEIPT = "RECEIPT"
    ISSUE = "ISSUE"
    ADJUSTMENT_INCREASE = "ADJUSTMENT_INCREASE"
    ADJUSTMENT_DECREASE = "ADJUSTMENT_DECREASE"