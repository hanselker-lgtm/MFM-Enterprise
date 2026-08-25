"""
Create Contact use case.
"""

from __future__ import annotations

from mfm.domain.contact.contact import Contact
from mfm.domain.contact.exceptions import DuplicateContactNumberError
from mfm.repositories.contact_repository import ContactRepository


class CreateContactUseCase:
    """
    Create a new contact if input is valid and contact number is unique.
    """

    def __init__(self, repository: ContactRepository) -> None:
        self._repository = repository

    def execute(self, contact: Contact) -> Contact:
        if not isinstance(contact, Contact):
            raise TypeError("contact must be a Contact")

        if not isinstance(contact.contact_number, str):
            raise ValueError("contact_number must be a string")

        contact_number = contact.contact_number.strip()
        if not contact_number:
            raise ValueError("contact_number cannot be empty")

        if contact.party is None:
            raise ValueError("contact must include a party")

        existing = self._repository.get_by_number(contact_number)
        if existing is not None:
            raise DuplicateContactNumberError(
                f"Contact number {contact_number} already exists"
            )

        contact.contact_number = contact_number
        self._repository.add(contact)
        return contact
