import pytest

from mfm.domain.contact.email import Email
from mfm.common.enums import EmailType


def test_email_is_normalized():

    email = Email(" Hans@Example.COM ")

    assert email.address == "hans@example.com"


def test_domain():

    email = Email("abc@test.dk")

    assert email.domain == "test.dk"


def test_local_part():

    email = Email("abc@test.dk")

    assert email.local_part == "abc"


def test_invalid_email():

    with pytest.raises(ValueError):

        Email("abc")


def test_email_type():

    email = Email(
        "abc@test.dk",
        EmailType.WORK,
    )

    assert email.email_type == EmailType.WORK