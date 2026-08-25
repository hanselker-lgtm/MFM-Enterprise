from __future__ import annotations
from uuid import UUID, uuid4

import pytest

from mfm.application.contact.delete_contact_use_case import DeleteContactUseCase
from mfm.common.enums import AddressType, EmailType, PhoneType
from mfm.domain.contact.address import Address
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.email import Email
from mfm.domain.contact.exceptions import ContactNotFoundException
from mfm.domain.contact.organisation import Organisation
from mfm.domain.contact.person import Person
from mfm.domain.contact.phone import Phone
from mfm.repositories.contact_repository import ContactRepository


class InMemoryContactRepository(ContactRepository):
    def __init__(self) -> None:
        self._contacts: dict[UUID, Contact] = {}
        self._emails_by_contact: dict[UUID, list[Email]] = {}
        self._phones_by_contact: dict[UUID, list[Phone]] = {}
        self._addresses_by_contact: dict[UUID, list[Address]] = {}
        self._person_by_contact: dict[UUID, Person] = {}
        self._organisation_by_contact: dict[UUID, Organisation] = {}

    def add(self, contact: Contact) -> None:
        self._contacts[contact.id] = contact
        self._emails_by_contact[contact.id] = list(contact.emails)
        self._phones_by_contact[contact.id] = list(contact.phones)
        self._addresses_by_contact[contact.id] = list(contact.addresses)

        if isinstance(contact.party, Person):
            self._person_by_contact[contact.id] = contact.party
            self._organisation_by_contact.pop(contact.id, None)
        elif isinstance(contact.party, Organisation):
            self._organisation_by_contact[contact.id] = contact.party
            self._person_by_contact.pop(contact.id, None)

    def update(self, contact: Contact) -> None:
        self.add(contact)

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
        self._emails_by_contact.pop(contact_id, None)
        self._phones_by_contact.pop(contact_id, None)
        self._addresses_by_contact.pop(contact_id, None)
        self._person_by_contact.pop(contact_id, None)
        self._organisation_by_contact.pop(contact_id, None)


def _build_contact_with_children(*, party, contact_number: str) -> Contact:
    return Contact(
        party=party,
        contact_number=contact_number,
        emails=[Email("delete@test.dk", email_type=EmailType.WORK, primary=True)],
        phones=[Phone("+4512345678", phone_type=PhoneType.MOBILE, primary=True)],
        addresses=[
            Address(
                line1="Deletevej 1",
                postal_code="8000",
                city="Aarhus",
                country="Danmark",
                address_type=AddressType.HOME,
                primary=True,
            )
        ],
    )


def test_delete_contact_successful_delete():
    repository = InMemoryContactRepository()
    use_case = DeleteContactUseCase(repository)
    contact = _build_contact_with_children(
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number="C-300001",
    )
    repository.add(contact)

    result = use_case.execute(contact.id)

    assert result is True
    assert repository.get(contact.id) is None


def test_delete_contact_unknown_contact():
    repository = InMemoryContactRepository()
    use_case = DeleteContactUseCase(repository)

    with pytest.raises(ContactNotFoundException):
        use_case.execute(uuid4())


def test_delete_contact_cascade_delete_emails():
    repository = InMemoryContactRepository()
    use_case = DeleteContactUseCase(repository)
    contact = _build_contact_with_children(
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number="C-300002",
    )
    repository.add(contact)

    use_case.execute(contact.id)

    assert contact.id not in repository._emails_by_contact


def test_delete_contact_cascade_delete_phones():
    repository = InMemoryContactRepository()
    use_case = DeleteContactUseCase(repository)
    contact = _build_contact_with_children(
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number="C-300003",
    )
    repository.add(contact)

    use_case.execute(contact.id)

    assert contact.id not in repository._phones_by_contact


def test_delete_contact_cascade_delete_addresses():
    repository = InMemoryContactRepository()
    use_case = DeleteContactUseCase(repository)
    contact = _build_contact_with_children(
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number="C-300004",
    )
    repository.add(contact)

    use_case.execute(contact.id)

    assert contact.id not in repository._addresses_by_contact


def test_delete_contact_cascade_delete_person():
    repository = InMemoryContactRepository()
    use_case = DeleteContactUseCase(repository)
    contact = _build_contact_with_children(
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number="C-300005",
    )
    repository.add(contact)

    use_case.execute(contact.id)

    assert contact.id not in repository._person_by_contact


def test_delete_contact_cascade_delete_organisation():
    repository = InMemoryContactRepository()
    use_case = DeleteContactUseCase(repository)
    contact = _build_contact_with_children(
        party=Organisation(name="Delete Organisation"),
        contact_number="C-300006",
    )
    repository.add(contact)

    use_case.execute(contact.id)

    assert contact.id not in repository._organisation_by_contact
