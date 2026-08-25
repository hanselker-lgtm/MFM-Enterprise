from __future__ import annotations
from uuid import UUID, uuid4

import pytest

from mfm.application.contact.update_contact_use_case import UpdateContactUseCase
from mfm.common.enums import AddressType, ContactStatus, EmailType, PhoneType
from mfm.domain.contact.address import Address
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.exceptions import ContactNotFoundError
from mfm.domain.contact.email import Email
from mfm.domain.contact.organisation import Organisation
from mfm.domain.contact.person import Person
from mfm.domain.contact.phone import Phone
from mfm.repositories.contact_repository import ContactRepository


class InMemoryContactRepository(ContactRepository):
    def __init__(self) -> None:
        self._contacts: dict[UUID, Contact] = {}

    def add(self, contact: Contact) -> None:
        self._contacts[contact.id] = contact

    def update(self, contact: Contact) -> None:
        self._contacts[contact.id] = contact

    def get(self, contact_id: UUID) -> Contact | None:
        return self._contacts.get(contact_id)

    def get_by_number(self, contact_number: str) -> Contact | None:
        for contact in self._contacts.values():
            if contact.contact_number == contact_number:
                return contact
        return None

    def list(self) -> list[Contact]:
        return list(self._contacts.values())

    def search(self, text: str) -> list[Contact]:
        lowered = text.lower()
        return [
            contact
            for contact in self._contacts.values()
            if lowered in contact.display_name.lower()
            or lowered in contact.contact_number.lower()
        ]

    def exists(self, contact_id: UUID) -> bool:
        return contact_id in self._contacts

    def delete(self, contact_id: UUID) -> None:
        self._contacts.pop(contact_id, None)


def _build_person_contact(*, contact_number: str = "C-200001") -> Contact:
    return Contact(
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number=contact_number,
        status=ContactStatus.ACTIVE,
    )


def test_update_contact_successful_update():
    repository = InMemoryContactRepository()
    use_case = UpdateContactUseCase(repository)

    original = _build_person_contact(contact_number="C-200010")
    repository.add(original)

    updated_input = Contact(
        id=original.id,
        party=Person(first_name="Maja", last_name="Mikkelsen"),
        contact_number="C-200011",
        status=ContactStatus.INACTIVE,
    )

    updated = use_case.execute(updated_input)

    assert updated.id == original.id
    assert updated.contact_number == "C-200011"
    assert updated.status == ContactStatus.INACTIVE
    assert isinstance(updated.party, Person)
    assert updated.party.display_name == "Maja Mikkelsen"


def test_update_contact_not_found():
    repository = InMemoryContactRepository()
    use_case = UpdateContactUseCase(repository)

    missing = Contact(
        id=uuid4(),
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number="C-200020",
    )

    with pytest.raises(ContactNotFoundError):
        use_case.execute(missing)


def test_update_contact_updates_emails():
    repository = InMemoryContactRepository()
    use_case = UpdateContactUseCase(repository)

    original = _build_person_contact(contact_number="C-200030")
    repository.add(original)

    updated_input = Contact(
        id=original.id,
        party=original.party,
        contact_number=original.contact_number,
        emails=[Email("updated@test.dk", email_type=EmailType.WORK, primary=True)],
    )

    updated = use_case.execute(updated_input)

    assert len(updated.emails) == 1
    assert updated.emails[0].address == "updated@test.dk"


def test_update_contact_updates_phones():
    repository = InMemoryContactRepository()
    use_case = UpdateContactUseCase(repository)

    original = _build_person_contact(contact_number="C-200040")
    repository.add(original)

    updated_input = Contact(
        id=original.id,
        party=original.party,
        contact_number=original.contact_number,
        phones=[Phone("+4511223344", phone_type=PhoneType.MOBILE, primary=True)],
    )

    updated = use_case.execute(updated_input)

    assert len(updated.phones) == 1
    assert updated.phones[0].number == "+4511223344"


def test_update_contact_updates_addresses():
    repository = InMemoryContactRepository()
    use_case = UpdateContactUseCase(repository)

    original = _build_person_contact(contact_number="C-200050")
    repository.add(original)

    updated_input = Contact(
        id=original.id,
        party=original.party,
        contact_number=original.contact_number,
        addresses=[
            Address(
                line1="Nyvej 10",
                postal_code="2100",
                city="Kobenhavn",
                country="Danmark",
                address_type=AddressType.HOME,
                primary=True,
            )
        ],
    )

    updated = use_case.execute(updated_input)

    assert len(updated.addresses) == 1
    assert updated.addresses[0].city == "Kobenhavn"


def test_update_contact_updates_person():
    repository = InMemoryContactRepository()
    use_case = UpdateContactUseCase(repository)

    original = _build_person_contact(contact_number="C-200060")
    repository.add(original)

    updated_input = Contact(
        id=original.id,
        party=Person(first_name="Lise", last_name="Larsen"),
        contact_number=original.contact_number,
    )

    updated = use_case.execute(updated_input)

    assert isinstance(updated.party, Person)
    assert updated.party.display_name == "Lise Larsen"


def test_update_contact_updates_organisation():
    repository = InMemoryContactRepository()
    use_case = UpdateContactUseCase(repository)

    original = Contact(
        party=Organisation(name="Old Org"),
        contact_number="C-200070",
    )
    repository.add(original)

    updated_input = Contact(
        id=original.id,
        party=Organisation(name="New Org"),
        contact_number=original.contact_number,
    )

    updated = use_case.execute(updated_input)

    assert isinstance(updated.party, Organisation)
    assert updated.party.display_name == "New Org"
