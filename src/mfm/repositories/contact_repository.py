"""
Contact Repository interface.

This module defines the repository contract used by the
application layer.

Infrastructure implementations (SQLite, PostgreSQL, etc.)
must implement this interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.contact.contact import Contact


class ContactRepository(ABC):
    """
    Repository contract for Contact aggregates.

    Implementations are responsible only for persistence.
    No business logic belongs here.
    """

    @abstractmethod
    def add(self, contact: Contact) -> None:
        """
        Persist a new Contact.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, contact_id: UUID) -> Contact | None:
        """
        Return a Contact by UUID.

        Returns None if not found.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_number(
        self,
        contact_number: str,
    ) -> Contact | None:
        """
        Return a Contact by contact number.

        Returns None if not found.
        """
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Contact]:
        """
        Return all contacts.
        """
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        text: str,
    ) -> list[Contact]:
        """
        Search contacts.

        Implementation decides how searching is performed.
        """
        raise NotImplementedError

    @abstractmethod
    def exists(
        self,
        contact_id: UUID,
    ) -> bool:
        """
        Check whether a Contact exists.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(
        self,
        contact_id: UUID,
    ) -> None:
        """
        Delete a Contact.
        """
        raise NotImplementedError