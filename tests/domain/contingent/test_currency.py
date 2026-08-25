from mfm.domain.contingent.currency import Currency


def test_currency_values():
    assert Currency.DKK.value == "DKK"
    assert Currency.EUR.value == "EUR"
    assert Currency.USD.value == "USD"
