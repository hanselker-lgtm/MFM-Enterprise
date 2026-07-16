"""
Search Contacts use case.
"""

from __future__ import annotations

from mfm.domain.contact.contact import Contact
from mfm.repositories.contact_repository import ContactRepository


class SearchContactsUseCase:
    """
    Search contacts across name, organisation, email and phone fields.
    """

    def __init__(self, repository: ContactRepository) -> None:
        self._repository = repository

    def execute(
        self,
        query: str,
        *,
        offset: int = 0,
        limit: int | None = None,
        sort_by: str = "contact_number",
        descending: bool = False,
    ) -> list[Contact]:
        if not isinstance(query, str):
            raise TypeError("query must be a string")
        if offset < 0:
            raise ValueError("offset cannot be negative")
        if limit is not None and limit < 0:
            raise ValueError("limit cannot be negative")

        normalized = query.strip().lower()
        if not normalized:
            return []

        contacts = self._repository.list()

        def matches(contact: Contact) -> bool:
            haystacks = [
                contact.display_name.lower(),
                contact.contact_number.lower(),
                getattr(contact.party, "name", "").lower(),
            ]

            haystacks.extend(email.address.lower() for email in contact.emails)
            haystacks.extend(phone.number.lower() for phone in contact.phones)

            return any(normalized in value for value in haystacks)

        filtered = [contact for contact in contacts if matches(contact)]
        sorted_contacts = _sort_contacts(filtered, sort_by=sort_by, descending=descending)

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
