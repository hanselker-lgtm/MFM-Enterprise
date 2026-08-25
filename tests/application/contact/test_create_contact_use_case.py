from __future__ import annotations
from uuid import UUID

import pytest

from mfm.application.contact.create_contact_use_case import CreateContactUseCase
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.exceptions import DuplicateContactNumberError
from mfm.domain.contact.person import Person
from mfm.repositories.contact_repository import ContactRepository


class InMemoryContactRepository(ContactRepository):
    def __init__(self) -> None:
        self._contacts: dict[str, Contact] = {}

    def add(self, contact: Contact) -> None:
        self._contacts[contact.contact_number] = contact

    def update(self, contact: Contact) -> None:
        self._contacts[contact.contact_number] = contact

    def get(self, contact_id: UUID) -> Contact | None:
        for contact in self._contacts.values():
            if contact.id == contact_id:
                return contact
        return None

    def get_by_number(self, contact_number: str) -> Contact | None:
        return self._contacts.get(contact_number)

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
        return self.get(contact_id) is not None

    def delete(self, contact_id: UUID) -> None:
        for number, contact in list(self._contacts.items()):
            if contact.id == contact_id:
                del self._contacts[number]
                return


def _build_contact(*, contact_number: str = "C-100000") -> Contact:
    return Contact(
        party=Person(first_name="Hans", last_name="Hansen"),
        contact_number=contact_number,
    )


def test_create_contact_successful_creation():
    repository = InMemoryContactRepository()
    use_case = CreateContactUseCase(repository)
    contact = _build_contact(contact_number="C-100001")

    created = use_case.execute(contact)

    assert created is contact
    assert repository.get_by_number("C-100001") is contact


def test_create_contact_duplicate_contact_number():
    repository = InMemoryContactRepository()
    use_case = CreateContactUseCase(repository)
    first = _build_contact(contact_number="C-100002")
    second = _build_contact(contact_number="C-100002")

    use_case.execute(first)

    with pytest.raises(DuplicateContactNumberError):
        use_case.execute(second)

    assert repository.list() == [first]


def test_create_contact_invalid_input_not_contact():
    repository = InMemoryContactRepository()
    use_case = CreateContactUseCase(repository)

    with pytest.raises(TypeError):
        use_case.execute("not-a-contact")  # type: ignore[arg-type]


def test_create_contact_invalid_input_empty_contact_number():
    repository = InMemoryContactRepository()
    use_case = CreateContactUseCase(repository)
    contact = _build_contact(contact_number="   ")

    with pytest.raises(ValueError):
        use_case.execute(contact)


def test_create_contact_invalid_input_missing_party():
    repository = InMemoryContactRepository()
    use_case = CreateContactUseCase(repository)
    contact = Contact(party=None, contact_number="C-100003")  # type: ignore[arg-type]

    with pytest.raises(ValueError):
        use_case.execute(contact)
