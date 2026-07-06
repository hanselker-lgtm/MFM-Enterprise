"""
Repository for Contact aggregate.
"""

from __future__ import annotations

from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from mfm.domain.contact.contact import Contact


class ContactRepository:
    """
    Repository for Contact aggregate.
    """

    def __init__(self, session: Session):
        self._session = session

    def add(self, contact: Contact) -> None:
        """Add a new contact."""
        self._session.add(contact)

    def get_by_id(self, contact_id: str) -> Contact | None:
        """Return one Contact aggregate."""

        stmt = (
            select(Contact)
            .options(
                joinedload(Contact.person),
                joinedload(Contact.organisation),
                joinedload(Contact.addresses),
                joinedload(Contact.emails),
                joinedload(Contact.phones),
                joinedload(Contact.outgoing_relations),
                joinedload(Contact.incoming_relations),
            )
            .where(Contact.contact_id == contact_id)
        )

        return self._session.scalar(stmt)

    def list_active(self) -> Sequence[Contact]:
        """Return all active contacts."""

        stmt = (
            select(Contact)
            .where(Contact.is_active.is_(True))
            .order_by(Contact.created_at)
        )

        return self._session.scalars(stmt).all()

    def list_all(self) -> Sequence[Contact]:
        """Return all contacts."""

        stmt = (
            select(Contact)
            .order_by(Contact.created_at)
        )

        return self._session.scalars(stmt).all()

    def remove(self, contact: Contact) -> None:
        """
        Physical delete.

        Must ONLY be used by maintenance tools.
        """
        self._session.delete(contact)