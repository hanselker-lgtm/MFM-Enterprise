"""
List Contacts use case.
"""

from __future__ import annotations

from mfm.domain.contact.contact import Contact
from mfm.repositories.contact_repository import ContactRepository


class ListContactsUseCase:
    """
    List all contacts with paging-ready options and sorting.
    """

    def __init__(self, repository: ContactRepository) -> None:
        self._repository = repository

    def execute(
        self,
        *,
        offset: int = 0,
        limit: int | None = None,
        sort_by: str = "contact_number",
        descending: bool = False,
    ) -> list[Contact]:
        if offset < 0:
            raise ValueError("offset cannot be negative")
        if limit is not None and limit < 0:
            raise ValueError("limit cannot be negative")

        contacts = self._repository.list()
        sorted_contacts = _sort_contacts(contacts, sort_by=sort_by, descending=descending)

        if limit is None:
            return sorted_contacts[offset:]

        return sorted_contacts[offset : offset + limit]


def _sort_contacts(
    contacts: list[Contact], *, sort_by: str, descending: bool
) -> list[Contact]:
    if sort_by == "display_name":
        def key_fn(contact: Contact):
            return contact.display_name.lower()
    elif sort_by == "created_at":
        def key_fn(contact: Contact):
            return contact.created_at
    elif sort_by == "updated_at":
        def key_fn(contact: Contact):
            return contact.updated_at
    else:
        def key_fn(contact: Contact):
            return contact.contact_number.lower()

    return sorted(contacts, key=key_fn, reverse=descending)
