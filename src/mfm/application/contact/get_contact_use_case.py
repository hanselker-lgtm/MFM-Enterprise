"""
Get Contact use case.
"""

from __future__ import annotations

from uuid import UUID

from mfm.domain.contact.contact import Contact
from mfm.domain.contact.exceptions import ContactNotFoundException
from mfm.repositories.contact_repository import ContactRepository


class GetContactUseCase:
    """
    Retrieve contacts by id or contact number.
    """

    def __init__(self, repository: ContactRepository) -> None:
        self._repository = repository

    def execute_by_id(self, contact_id: UUID) -> Contact:
        if not isinstance(contact_id, UUID):
            raise TypeError("contact_id must be a UUID")

        contact = self._repository.get(contact_id)
        if contact is None:
            raise ContactNotFoundException(f"Contact {contact_id} was not found")

        return contact

    def execute_by_contact_number(self, contact_number: str) -> Contact:
        if not isinstance(contact_number, str):
            raise TypeError("contact_number must be a string")

        normalized = contact_number.strip()
        if not normalized:
            raise ValueError("contact_number cannot be empty")

        contact = self._repository.get_by_number(normalized)
        if contact is None:
            raise ContactNotFoundException(
                f"Contact with number {normalized} was not found"
            )

        return contact
