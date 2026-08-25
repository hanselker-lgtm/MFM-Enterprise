from mfm.domain.contingent.billing_period import BillingPeriod


def test_billing_period_values():
    assert BillingPeriod.MONTHLY.value == "MONTHLY"
    assert BillingPeriod.QUARTERLY.value == "QUARTERLY"
    assert BillingPeriod.YEARLY.value == "YEARLY"
