"""
Update Contact use case.
"""

from __future__ import annotations

from datetime import UTC, datetime

from mfm.domain.contact.contact import Contact
from mfm.domain.contact.exceptions import ContactNotFoundError
from mfm.repositories.contact_repository import ContactRepository


class UpdateContactUseCase:
    """
    Update an existing contact and persist the changes.
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

        existing = self._repository.get(contact.id)
        if existing is None:
            raise ContactNotFoundError(f"Contact {contact.id} was not found")

        existing.party = contact.party
        existing.contact_number = contact_number
        existing.status = contact.status
        existing.emails = list(contact.emails)
        existing.phones = list(contact.phones)
        existing.addresses = list(contact.addresses)
        existing.updated_at = datetime.now(UTC)

        self._repository.update(existing)
        return existing
