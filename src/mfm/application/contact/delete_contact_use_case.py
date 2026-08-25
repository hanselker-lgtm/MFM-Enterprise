"""
Delete Contact use case.
"""

from __future__ import annotations

from uuid import UUID

from mfm.domain.contact.exceptions import ContactNotFoundException
from mfm.repositories.contact_repository import ContactRepository


class DeleteContactUseCase:
    """
    Delete an existing contact.
    """

    def __init__(self, repository: ContactRepository) -> None:
        self._repository = repository

    def execute(self, contact_id: UUID) -> bool:
        if not isinstance(contact_id, UUID):
            raise TypeError("contact_id must be a UUID")

        existing = self._repository.get(contact_id)
        if existing is None:
            raise ContactNotFoundException(f"Contact {contact_id} was not found")

        self._repository.delete(contact_id)
        return True
