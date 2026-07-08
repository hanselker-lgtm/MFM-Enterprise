from mfm.domain.contact.contact import Contact
from mfm.domain.contact.person import Person
from mfm.domain.contact.email import Email


def test_contact_display_name():

    person = Person(

        first_name="Hans",

        last_name="Hansen",

    )

    contact = Contact(

        party=person,

        contact_number="C-000001",

    )

    assert contact.display_name == "Hans Hansen"


def test_only_one_primary_email():

    person = Person(

        first_name="Hans",

        last_name="Hansen",

    )

    contact = Contact(

        party=person,

        contact_number="C-000001",

    )

    contact.add_email(

        Email(

            "a@test.dk",

            primary=True,

        )

    )

    contact.add_email(

        Email(

            "b@test.dk",

            primary=True,

        )

    )

    assert sum(

        e.primary for e in contact.emails

    ) == 1