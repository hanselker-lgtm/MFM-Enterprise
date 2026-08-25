
from mfm.common.enums import AddressType, ContactStatus, EmailType, PhoneType
from mfm.database.mappers.contact_mapper import ContactMapper
from mfm.database.models.contact_address_model import ContactAddressModel
from mfm.database.models.contact_email_model import ContactEmailModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.contact_organisation_model import ContactOrganisationModel
from mfm.database.models.contact_person_model import ContactPersonModel
from mfm.database.models.contact_phone_model import ContactPhoneModel
from mfm.domain.contact.address import Address
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.email import Email
from mfm.domain.contact.organisation import Organisation
from mfm.domain.contact.person import Person
from mfm.domain.contact.phone import Phone


def test_domain_to_orm_and_back_preserves_person_contact():
    person = Person(first_name="Hans", last_name="Hansen")
    contact = Contact(
        party=person,
        contact_number="C-000001",
        status=ContactStatus.ACTIVE,
        emails=[Email("a@test.dk", email_type=EmailType.WORK, primary=True)],
        phones=[Phone("+4520304050", phone_type=PhoneType.WORK, primary=True)],
        addresses=[
            Address(
                line1="Havnevej 12",
                postal_code="5700",
                city="Svendborg",
                country="Danmark",
                address_type=AddressType.WORK,
                primary=True,
            )
        ],
    )

    orm = ContactMapper.to_orm(contact)

    assert isinstance(orm, ContactModel)
    assert orm.contact_number == contact.contact_number
    assert orm.status == contact.status
    assert isinstance(orm.contact_person, ContactPersonModel)
    assert orm.contact_person.first_name == "Hans"
    assert isinstance(orm.emails[0], ContactEmailModel)
    assert orm.emails[0].address == "a@test.dk"
    assert isinstance(orm.phones[0], ContactPhoneModel)
    assert orm.phones[0].number == "+4520304050"
    assert isinstance(orm.addresses[0], ContactAddressModel)
    assert orm.addresses[0].city == "Svendborg"

    round_tripped = ContactMapper.to_domain(orm)

    assert round_tripped.contact_number == contact.contact_number
    assert isinstance(round_tripped.party, Person)
    assert round_tripped.party.full_name == "Hans Hansen"
    assert round_tripped.emails[0].address == "a@test.dk"
    assert round_tripped.phones[0].number == "+4520304050"
    assert round_tripped.addresses[0].city == "Svendborg"


def test_domain_to_orm_and_back_preserves_organisation_contact():
    organisation = Organisation(name="MFM", cvr="12345678")
    contact = Contact(
        party=organisation,
        contact_number="C-000002",
        status=ContactStatus.INACTIVE,
    )

    orm = ContactMapper.to_orm(contact)

    assert isinstance(orm.contact_organisation, ContactOrganisationModel)
    assert orm.contact_number == "C-000002"
    assert orm.status == ContactStatus.INACTIVE

    round_tripped = ContactMapper.to_domain(orm)

    assert isinstance(round_tripped.party, Organisation)
    assert round_tripped.party.name == "MFM"
    assert round_tripped.party.cvr == "12345678"
