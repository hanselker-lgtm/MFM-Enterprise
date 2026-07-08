from mfm.domain.contact.organisation import Organisation


def test_display_name():

    company = Organisation(

        name="MFM Marine ApS",

    )

    assert company.display_name == "MFM Marine ApS"


def test_trim():

    company = Organisation(

        name="  MFM Marine ApS  ",

    )

    assert company.name == "MFM Marine ApS"