from mfm.domain.finance.billing_period import BillingPeriod


def test_billing_period_contains_required_values():
    assert BillingPeriod.MONTHLY.value == "MONTHLY"
    assert BillingPeriod.QUARTERLY.value == "QUARTERLY"
    assert BillingPeriod.HALF_YEARLY.value == "HALF_YEARLY"
    assert BillingPeriod.YEARLY.value == "YEARLY"
    assert BillingPeriod.LIFETIME.value == "LIFETIME"
