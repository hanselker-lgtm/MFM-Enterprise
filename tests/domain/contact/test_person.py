from mfm.domain.contact.person import Person


def test_full_name():

    person = Person(

        first_name="Hans",

        middle_name="Elker",

        last_name="Hansen",

    )

    assert person.full_name == "Hans Elker Hansen"


def test_initials():

    person = Person(

        first_name="Hans",

        middle_name="Elker",

        last_name="Hansen",

    )

    assert person.initials == "HEH"


def test_trim():

    person = Person(

        first_name=" Hans ",

        last_name=" Hansen ",

    )

    assert person.first_name == "Hans"

    assert person.last_name == "Hansen"