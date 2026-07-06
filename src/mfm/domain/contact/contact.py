"""
Contact aggregate root.
"""

from __future__ import annotations

import uuid

from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base_model import AggregateRoot
from .enums import ContactType


class Contact(AggregateRoot):

    __tablename__ = "CONTACT"

    contact_id: Mapped[str] = mapped_column(
        "ContactID",
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    contact_type: Mapped[ContactType] = mapped_column(
        "ContactType",
        Enum(ContactType),
        nullable=False,
    )

    person = relationship(
        "Person",
        back_populates="contact",
        uselist=False,
        cascade="all, delete-orphan",
    )

    organisation = relationship(
        "Organisation",
        back_populates="contact",
        uselist=False,
        cascade="all, delete-orphan",
    )

    addresses = relationship(
        "Address",
        back_populates="contact",
        cascade="all, delete-orphan",
    )

    emails = relationship(
        "Email",
        back_populates="contact",
        cascade="all, delete-orphan",
    )

    phones = relationship(
        "Phone",
        back_populates="contact",
        cascade="all, delete-orphan",
    )

    outgoing_relations = relationship(
        "ContactRelation",
        foreign_keys="ContactRelation.from_contact_id",
        back_populates="from_contact",
    )

    incoming_relations = relationship(
        "ContactRelation",
        foreign_keys="ContactRelation.to_contact_id",
        back_populates="to_contact",
    )

    def archive(self) -> None:
        """Archive the contact."""
        self.is_active = False

    def activate(self) -> None:
        """Reactivate the contact."""
        self.is_active = True