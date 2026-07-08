"""
Contact Aggregate Root.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from mfm.common.aggregate_root import AggregateRoot
from mfm.common.enums import ContactStatus

from mfm.domain.contact.contact_party import ContactParty
from mfm.domain.contact.email import Email
from mfm.domain.contact.phone import Phone
from mfm.domain.contact.address import Address


@dataclass(slots=True)
class Contact(AggregateRoot):
    """
    Aggregate Root representing a Contact.
    """

    party: ContactParty

    contact_number: str

    status: ContactStatus = ContactStatus.ACTIVE

    id: UUID = field(default_factory=uuid4)

    created: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    modified: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    emails: list[Email] = field(default_factory=list)

    phones: list[Phone] = field(default_factory=list)

    addresses: list[Address] = field(default_factory=list)

    def __post_init__(self):

        AggregateRoot.__init__(self)

    @property
    def display_name(self) -> str:

        return self.party.display_name

    def add_email(self, email: Email):

        if email.primary:

            self.emails = [
                Email(
                    address=e.address,
                    email_type=e.email_type,
                    primary=False,
                    verified=e.verified,
                )
                for e in self.emails
            ]

        self.emails.append(email)

        self.modified = datetime.now(UTC)

    def add_phone(self, phone: Phone):

        if phone.primary:

            self.phones = [
                Phone(
                    number=p.number,
                    phone_type=p.phone_type,
                    primary=False,
                    verified=p.verified,
                )
                for p in self.phones
            ]

        self.phones.append(phone)

        self.modified = datetime.now(UTC)

    def add_address(self, address: Address):

        if address.primary:

            self.addresses = [
                Address(
                    line1=a.line1,
                    postal_code=a.postal_code,
                    city=a.city,
                    country=a.country,
                    address_type=a.address_type,
                    primary=False,
                    line2=a.line2,
                    state=a.state,
                )
                for a in self.addresses
            ]

        self.addresses.append(address)

        self.modified = datetime.now(UTC)