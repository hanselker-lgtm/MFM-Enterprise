"""Billing period enum for contingent plans."""

from enum import Enum


class BillingPeriod(str, Enum):
    """Frequency for contingent billing."""

    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    YEARLY = "YEARLY"
