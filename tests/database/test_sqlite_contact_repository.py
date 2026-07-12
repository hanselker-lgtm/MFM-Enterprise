from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.common.enums import AddressType, ContactStatus, EmailType, PhoneType
from mfm.database.mappers.contact_mapper import ContactMapper
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.database.repositories.sqlite_contact_repository import SQLiteContactRepository
from mfm.domain.contact.address import Address
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.email import Email
from mfm.domain.contact.organisation import Organisation
from mfm.domain.contact.person import Person
from mfm.domain.contact.phone import Phone


def _create_test_contact(*, contact_number: str = "C-000001", party=None, emails=None, phones=None, addresses=None) -> Contact:
    if party is None:
        party = Person(first_name="Hans", last_name="Hansen")

    return Contact(
        party=party,
        contact_number=contact_number,
        status=ContactStatus.ACTIVE,
        emails=emails or [],
        phones=phones or [],
        addresses=addresses or [],
    )


def _create_session():
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def test_repository_persists_and_reads_contact():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        contact = _create_test_contact(
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

        repository.add(contact)
        session.commit()

        stored = repository.get_by_id(contact.id)
        assert stored is not None
        assert stored.contact_number == "C-000001"
        assert stored.party.display_name == "Hans Hansen"
        assert stored.emails[0].address == "a@test.dk"
        assert stored.phones[0].number == "+4520304050"
        assert stored.addresses[0].city == "Svendborg"

        by_number = repository.get_by_contact_number("C-000001")
        assert by_number is not None
        assert by_number.id == contact.id

        assert repository.exists(contact.id) is True

        repository.delete(contact.id)
        session.commit()

        assert repository.get_by_id(contact.id) is None
    finally:
        session.close()
        engine.dispose()


def test_repository_supports_crud_operations():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        contact = _create_test_contact(contact_number="C-000010")
        repository.add(contact)
        session.commit()

        assert repository.get_by_id(contact.id) is not None
        assert repository.get_by_contact_number("C-000010") is not None
        assert repository.exists(contact.id) is True

        updated_contact = Contact(
            id=contact.id,
            party=Person(first_name="Hans", last_name="Hansen"),
            contact_number="C-000011",
            status=ContactStatus.INACTIVE,
        )
        repository.update(updated_contact)
        session.commit()

        stored = repository.get_by_id(contact.id)
        assert stored is not None
        assert stored.contact_number == "C-000011"
        assert stored.status == ContactStatus.INACTIVE

        repository.delete(contact.id)
        session.commit()
        assert repository.get_by_id(contact.id) is None
        assert repository.exists(contact.id) is False
    finally:
        session.close()
        engine.dispose()


def test_repository_returns_none_for_unknown_values():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        assert repository.get_by_id(uuid4()) is None
        assert repository.get_by_contact_number("MISSING") is None
        assert repository.exists(uuid4()) is False
    finally:
        session.close()
        engine.dispose()


def test_repository_rejects_duplicate_contact_number():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        first = _create_test_contact(contact_number="C-000020")
        second = _create_test_contact(contact_number="C-000020")

        repository.add(first)
        session.commit()

        with pytest.raises(ValueError):
            repository.add(second)
    finally:
        session.close()
        engine.dispose()


def test_repository_handles_empty_child_collections():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        contact = _create_test_contact(contact_number="C-000030")
        repository.add(contact)
        session.commit()

        stored = repository.get_by_id(contact.id)
        assert stored is not None
        assert stored.emails == []
        assert stored.phones == []
        assert stored.addresses == []
    finally:
        session.close()
        engine.dispose()


def test_repository_supports_person_and_organisation_contacts():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        person_contact = _create_test_contact(contact_number="C-000040", party=Person(first_name="Maja", last_name="Mikkelsen"))
        organisation_contact = _create_test_contact(contact_number="C-000041", party=Organisation(name="MFM"))

        repository.add(person_contact)
        repository.add(organisation_contact)
        session.commit()

        person_stored = repository.get_by_id(person_contact.id)
        organisation_stored = repository.get_by_id(organisation_contact.id)

        assert person_stored is not None and isinstance(person_stored.party, Person)
        assert organisation_stored is not None and isinstance(organisation_stored.party, Organisation)
    finally:
        session.close()
        engine.dispose()


def test_repository_persists_relationships_and_cascade_delete():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        contact = _create_test_contact(
            contact_number="C-000050",
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

        repository.add(contact)
        session.commit()

        stored = repository.get_by_id(contact.id)
        assert stored is not None
        assert len(stored.emails) == 1
        assert len(stored.phones) == 1
        assert len(stored.addresses) == 1

        repository.delete(contact.id)
        session.commit()

        assert repository.get_by_id(contact.id) is None
    finally:
        session.close()
        engine.dispose()


def test_repository_updates_child_collections():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        contact = _create_test_contact(contact_number="C-000060")
        repository.add(contact)
        session.commit()

        contact.emails = [Email("new@test.dk", email_type=EmailType.PRIVATE, primary=True)]
        contact.phones = [Phone("+4512345678", phone_type=PhoneType.MOBILE, primary=True)]
        contact.addresses = [
            Address(
                line1="Nyvej 3",
                postal_code="1000",
                city="København",
                country="Danmark",
                address_type=AddressType.HOME,
                primary=True,
            )
        ]

        repository.update(contact)
        session.commit()

        stored = repository.get_by_id(contact.id)
        assert stored is not None
        assert len(stored.emails) == 1
        assert stored.emails[0].address == "new@test.dk"
        assert len(stored.phones) == 1
        assert stored.phones[0].number == "+4512345678"
        assert len(stored.addresses) == 1
        assert stored.addresses[0].city == "København"
    finally:
        session.close()
        engine.dispose()


def test_repository_round_trip_via_mapper():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        contact = _create_test_contact(
            contact_number="C-000070",
            party=Organisation(name="MFM Enterprise"),
            emails=[Email("org@test.dk", email_type=EmailType.WORK, primary=True)],
        )

        repository.add(contact)
        session.commit()

        stored = repository.get_by_id(contact.id)
        assert stored is not None

        round_tripped = ContactMapper.to_domain(ContactMapper.to_orm(stored))
        assert round_tripped.contact_number == contact.contact_number
        assert isinstance(round_tripped.party, Organisation)
        assert round_tripped.emails[0].address == "org@test.dk"
    finally:
        session.close()
        engine.dispose()


def test_repository_round_trip_through_repository():
    engine, session = _create_session()
    try:
        repository = SQLiteContactRepository(session)

        contact = _create_test_contact(contact_number="C-000080")
        repository.add(contact)
        session.commit()

        stored = repository.get_by_id(contact.id)
        assert stored is not None
        assert stored.contact_number == contact.contact_number
        assert repository.get_by_contact_number(contact.contact_number) is not None
    finally:
        session.close()
        engine.dispose()
