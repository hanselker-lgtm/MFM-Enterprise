"""Billing period enum for finance contingent plans."""

from enum import Enum


class BillingPeriod(str, Enum):
    """Allowed billing frequencies for contingent plans."""

    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    HALF_YEARLY = "HALF_YEARLY"
    YEARLY = "YEARLY"
    LIFETIME = "LIFETIME"
