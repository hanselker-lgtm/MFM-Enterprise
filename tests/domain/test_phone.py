import pytest

from mfm.common.enums import PhoneType
from mfm.domain.contact.exceptions import InvalidPhoneError
from mfm.domain.contact.phone import Phone


def test_phone_is_normalized():

    phone = Phone("+45 20 30 40 50")

    assert phone.number == "+4520304050"


def test_invalid_phone():

    with pytest.raises(InvalidPhoneError):

        Phone("ABCDEF")


def test_phone_type():

    phone = Phone(
        "+4520304050",
        PhoneType.WORK,
    )

    assert phone.phone_type == PhoneType.WORK