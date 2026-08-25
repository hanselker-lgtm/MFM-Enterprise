from mfm.domain.finance.currency import Currency


def test_currency_contains_required_iso_codes():
    assert Currency.DKK.value == "DKK"
    assert Currency.EUR.value == "EUR"
    assert Currency.USD.value == "USD"
    assert Currency.GBP.value == "GBP"
    assert Currency.NOK.value == "NOK"
    assert Currency.SEK.value == "SEK"
