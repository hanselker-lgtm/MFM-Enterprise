from __future__ import annotations
from uuid import UUID, uuid4

import pytest

from mfm.application.contact.get_contact_use_case import GetContactUseCase
from mfm.application.contact.list_contacts_use_case import ListContactsUseCase
from mfm.application.contact.search_contacts_use_case import SearchContactsUseCase
from mfm.common.enums import AddressType, EmailType, PhoneType
from mfm.domain.contact.address import Address
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.exceptions import ContactNotFoundException
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


def _person_contact(
    *,
    contact_number: str,
    first_name: str,
    last_name: str,
    email: str,
    phone: str,
) -> Contact:
    return Contact(
        party=Person(first_name=first_name, last_name=last_name),
        contact_number=contact_number,
        emails=[Email(email, email_type=EmailType.WORK, primary=True)],
        phones=[Phone(phone, phone_type=PhoneType.MOBILE, primary=True)],
        addresses=[
            Address(
                line1="Testvej 1",
                postal_code="5000",
                city="Odense",
                country="Danmark",
                address_type=AddressType.HOME,
                primary=True,
            )
        ],
    )


def _organisation_contact(*, contact_number: str, name: str, email: str, phone: str) -> Contact:
    return Contact(
        party=Organisation(name=name),
        contact_number=contact_number,
        emails=[Email(email, email_type=EmailType.WORK, primary=True)],
        phones=[Phone(phone, phone_type=PhoneType.WORK, primary=True)],
    )


def _seed_contacts(repository: InMemoryContactRepository) -> list[Contact]:
    contacts = [
        _person_contact(
            contact_number="C-400010",
            first_name="Anna",
            last_name="Andersen",
            email="anna@northwind.dk",
            phone="+4511111111",
        ),
        _person_contact(
            contact_number="C-400020",
            first_name="Bjarne",
            last_name="Birk",
            email="bjarne@sealine.dk",
            phone="+4522222222",
        ),
        _organisation_contact(
            contact_number="C-400030",
            name="Marine Group",
            email="contact@marine-group.dk",
            phone="+4533333333",
        ),
    ]

    for contact in contacts:
        repository.add(contact)

    return contacts


def test_get_contact_by_id_success():
    repository = InMemoryContactRepository()
    contacts = _seed_contacts(repository)
    use_case = GetContactUseCase(repository)

    found = use_case.execute_by_id(contacts[0].id)

    assert found.id == contacts[0].id


def test_get_contact_by_number_success():
    repository = InMemoryContactRepository()
    contacts = _seed_contacts(repository)
    use_case = GetContactUseCase(repository)

    found = use_case.execute_by_contact_number(contacts[1].contact_number)

    assert found.id == contacts[1].id


def test_get_contact_not_found_by_id():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = GetContactUseCase(repository)

    with pytest.raises(ContactNotFoundException):
        use_case.execute_by_id(uuid4())


def test_get_contact_not_found_by_number():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = GetContactUseCase(repository)

    with pytest.raises(ContactNotFoundException):
        use_case.execute_by_contact_number("C-999999")


def test_search_contacts_by_name_partial_match():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = SearchContactsUseCase(repository)

    results = use_case.execute("ann")

    assert len(results) == 1
    assert results[0].display_name == "Anna Andersen"


def test_search_contacts_by_organisation_partial_match():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = SearchContactsUseCase(repository)

    results = use_case.execute("marine")

    assert len(results) == 1
    assert isinstance(results[0].party, Organisation)


def test_search_contacts_by_email_partial_match():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = SearchContactsUseCase(repository)

    results = use_case.execute("northwind")

    assert len(results) == 1
    assert results[0].emails[0].address == "anna@northwind.dk"


def test_search_contacts_by_phone_partial_match():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = SearchContactsUseCase(repository)

    results = use_case.execute("2222")

    assert len(results) == 1
    assert results[0].phones[0].number == "+4522222222"


def test_search_contacts_supports_paging_and_sorting():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = SearchContactsUseCase(repository)

    results = use_case.execute(
        "a",
        offset=1,
        limit=1,
        sort_by="display_name",
        descending=False,
    )

    assert len(results) == 1
    assert results[0].display_name == "Bjarne Birk"


def test_list_contacts_returns_all_contacts_sorted_by_number():
    repository = InMemoryContactRepository()
    contacts = _seed_contacts(repository)
    use_case = ListContactsUseCase(repository)

    listed = use_case.execute()

    assert len(listed) == len(contacts)
    assert [c.contact_number for c in listed] == [
        "C-400010",
        "C-400020",
        "C-400030",
    ]


def test_list_contacts_supports_sorting_by_display_name_desc():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = ListContactsUseCase(repository)

    listed = use_case.execute(sort_by="display_name", descending=True)

    assert [c.display_name for c in listed] == [
        "Marine Group",
        "Bjarne Birk",
        "Anna Andersen",
    ]


def test_list_contacts_supports_paging_ready_design():
    repository = InMemoryContactRepository()
    _seed_contacts(repository)
    use_case = ListContactsUseCase(repository)

    listed = use_case.execute(offset=1, limit=1)

    assert len(listed) == 1
    assert listed[0].contact_number == "C-400020"
