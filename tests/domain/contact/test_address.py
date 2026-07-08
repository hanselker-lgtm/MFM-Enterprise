from mfm.domain.contact.address import Address
from mfm.common.enums import AddressType


def test_address():

    address = Address(

        line1="Havnevej 12",

        postal_code="5700",

        city="Svendborg",

        country="Danmark",

    )

    assert address.city == "Svendborg"


def test_single_line():

    address = Address(

        line1="Havnevej 12",

        postal_code="5700",

        city="Svendborg",

        country="Danmark",

    )

    assert "5700" in address.single_line


def test_address_type():

    address = Address(

        line1="Havnevej 12",

        postal_code="5700",

        city="Svendborg",

        country="Danmark",

        address_type=AddressType.WORK,

    )

    assert address.address_type == AddressType.WORK