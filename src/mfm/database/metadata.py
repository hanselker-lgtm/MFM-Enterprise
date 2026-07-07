"""
Database metadata.

Imports all ORM models so SQLAlchemy metadata
and Alembic can discover them.
"""

# Contact module

from mfm.domain.contact.contact import Contact
from mfm.domain.contact.person import Person
from mfm.domain.contact.organisation import Organisation
from mfm.domain.contact.address import Address
from mfm.domain.contact.email import Email
from mfm.domain.contact.phone import Phone
from mfm.domain.contact.contact_relation import ContactRelation


__all__ = [
    "Contact",
    "Person",
    "Organisation",
    "Address",
    "Email",
    "Phone",
    "ContactRelation",
]