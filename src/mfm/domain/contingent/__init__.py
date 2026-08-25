"""Contingent domain package."""

from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.currency import Currency
from mfm.domain.contingent.invoice_rule import InvoiceRule
from mfm.domain.contingent.money import Money
from mfm.domain.contingent.exceptions import (
    ContingentPlanNotFoundError,
    ContingentError,
    InvalidContingentAmountError,
    InvalidContingentDatesError,
    InvalidContingentReferenceError,
    MultipleActiveContingentPlansError,
    OverlappingContingentPlanError,
)

__all__ = [
    "BillingPeriod",
    "ContingentPlanNotFoundError",
    "ContingentError",
    "ContingentPlan",
    "Currency",
    "InvoiceRule",
    "InvalidContingentAmountError",
    "InvalidContingentDatesError",
    "InvalidContingentReferenceError",
    "Money",
    "MultipleActiveContingentPlansError",
    "OverlappingContingentPlanError",
]
