import pytest

from mfm.domain.contingent.billing_period import BillingPeriod
from mfm.domain.contingent.exceptions import InvalidContingentReferenceError
from mfm.domain.contingent.invoice_rule import InvoiceRule


def test_invoice_rule_accepts_valid_values():
    rule = InvoiceRule(
        billing_period=BillingPeriod.MONTHLY,
        due_days=14,
        prorate_on_start=True,
    )

    assert rule.billing_period == BillingPeriod.MONTHLY
    assert rule.due_days == 14
    assert rule.prorate_on_start is True


def test_invoice_rule_rejects_invalid_billing_period():
    with pytest.raises(InvalidContingentReferenceError):
        InvoiceRule(billing_period="MONTHLY")  # type: ignore[arg-type]


def test_invoice_rule_rejects_negative_due_days():
    with pytest.raises(InvalidContingentReferenceError):
        InvoiceRule(billing_period=BillingPeriod.YEARLY, due_days=-1)
