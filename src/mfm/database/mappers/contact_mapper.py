"""
Mapper between domain contacts and persistence contact models.
"""

from __future__ import annotations

from uuid import uuid4
from mfm.database.models.contact_address_model import ContactAddressModel
from mfm.database.models.contact_email_model import ContactEmailModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.contact_organisation_model import ContactOrganisationModel
from mfm.database.models.contact_person_model import ContactPersonModel
from mfm.database.models.contact_phone_model import ContactPhoneModel
from mfm.domain.contact.address import Address
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.email import Email
from mfm.domain.contact.organisation import Organisation
from mfm.domain.contact.person import Person
from mfm.domain.contact.phone import Phone


class ContactMapper:
    """
    Map between domain Contact aggregates and persistence ContactModel rows.
    """

    @staticmethod
    def to_orm(contact: Contact) -> ContactModel:
        orm = ContactModel(
            id=contact.id,
            contact_number=contact.contact_number,
            status=contact.status,
            created_at=contact.created_at,
            updated_at=contact.updated_at,
        )

        if isinstance(contact.party, Person):
            contact_person = ContactPersonModel(
                id=uuid4(),
                first_name=contact.party.first_name,
                last_name=contact.party.last_name,
                middle_name=contact.party.middle_name,
                title=contact.party.title,
                birth_date=contact.party.birth_date,
                contact_id=contact.id,
            )
            orm.contact_person = contact_person
        elif isinstance(contact.party, Organisation):
            contact_organisation = ContactOrganisationModel(
                id=uuid4(),
                name=contact.party.name,
                cvr=contact.party.cvr,
                vat=contact.party.vat,
                ean=contact.party.ean,
                industry=contact.party.industry,
                contact_id=contact.id,
            )
            orm.contact_organisation = contact_organisation

        orm.emails = [
            ContactEmailModel(
                id=uuid4(),
                contact_id=contact.id,
                address=email.address,
                email_type=email.email_type,
                primary=email.primary,
                verified=email.verified,
                created_at=contact.created_at,
                updated_at=contact.updated_at,
            )
            for email in contact.emails
        ]

        orm.phones = [
            ContactPhoneModel(
                id=uuid4(),
                contact_id=contact.id,
                number=phone.number,
                phone_type=phone.phone_type,
                primary=phone.primary,
                verified=phone.verified,
                created_at=contact.created_at,
                updated_at=contact.updated_at,
            )
            for phone in contact.phones
        ]

        orm.addresses = [
            ContactAddressModel(
                id=uuid4(),
                contact_id=contact.id,
                line1=address.line1,
                line2=address.line2,
                postal_code=address.postal_code,
                city=address.city,
                state=address.state,
                country=address.country,
                address_type=address.address_type,
                primary=address.primary,
                created_at=contact.created_at,
                updated_at=contact.updated_at,
            )
            for address in contact.addresses
        ]

        return orm

    @staticmethod
    def to_domain(orm: ContactModel) -> Contact:
        if orm.contact_person is not None:
            party = Person(
                first_name=orm.contact_person.first_name,
                last_name=orm.contact_person.last_name,
                middle_name=orm.contact_person.middle_name,
                title=orm.contact_person.title,
                birth_date=orm.contact_person.birth_date,
            )
        elif orm.contact_organisation is not None:
            party = Organisation(
                name=orm.contact_organisation.name,
                cvr=orm.contact_organisation.cvr,
                vat=orm.contact_organisation.vat,
                ean=orm.contact_organisation.ean,
                industry=orm.contact_organisation.industry,
            )
        else:
            raise ValueError("ContactModel must contain a person or organisation")

        return Contact(
            id=orm.id,
            party=party,
            contact_number=orm.contact_number,
            status=orm.status,
            created_at=orm.created_at,
            updated_at=orm.updated_at,
            emails=[
                Email(
                    address=email.address,
                    email_type=email.email_type,
                    primary=email.primary,
                    verified=email.verified,
                )
                for email in orm.emails
            ],
            phones=[
                Phone(
                    number=phone.number,
                    phone_type=phone.phone_type,
                    primary=phone.primary,
                    verified=phone.verified,
                )
                for phone in orm.phones
            ],
            addresses=[
                Address(
                    line1=address.line1,
                    line2=address.line2,
                    postal_code=address.postal_code,
                    city=address.city,
                    state=address.state,
                    country=address.country,
                    address_type=address.address_type,
                    primary=address.primary,
                )
                for address in orm.addresses
            ],
        )
