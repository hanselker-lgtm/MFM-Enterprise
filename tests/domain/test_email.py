import pytest

from mfm.domain.contact.email import Email


def test_email_is_lowercase():

    email = Email("Hans@Example.dk")

    assert email.address == "hans@example.dk"


def test_invalid_email():

    with pytest.raises(ValueError):

        Email("abc")