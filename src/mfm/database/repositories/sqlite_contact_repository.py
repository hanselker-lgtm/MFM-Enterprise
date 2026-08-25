"""
SQLite repository for Contact aggregates.
"""

from __future__ import annotations

from uuid import UUID, uuid4

from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.contact_mapper import ContactMapper
from mfm.database.models.contact_address_model import ContactAddressModel
from mfm.database.models.contact_email_model import ContactEmailModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.contact_organisation_model import ContactOrganisationModel
from mfm.database.models.contact_person_model import ContactPersonModel
from mfm.database.models.contact_phone_model import ContactPhoneModel
from mfm.domain.contact.contact import Contact
from mfm.domain.contact.organisation import Organisation
from mfm.domain.contact.person import Person
from mfm.repositories.contact_repository import ContactRepository


class SQLiteContactRepository(ContactRepository):
    """
    SQLAlchemy-backed repository for Contact aggregates.
    """

    def __init__(self, session: Session):
        self._session = session

    def add(self, contact: Contact) -> None:
        existing = self.get_by_contact_number(contact.contact_number)
        if existing is not None:
            raise ValueError(f"Contact number {contact.contact_number} already exists")

        orm_contact = ContactMapper.to_orm(contact)
        self._session.add(orm_contact)
        self._session.flush()

    def get(self, contact_id: UUID) -> Contact | None:
        return self.get_by_id(contact_id)

    def get_by_id(self, contact_id: UUID) -> Contact | None:
        statement = select(ContactModel).where(ContactModel.id == contact_id)
        orm_contact = self._session.scalar(statement)
        if orm_contact is None:
            return None
        return ContactMapper.to_domain(orm_contact)

    def get_by_contact_number(self, contact_number: str) -> Contact | None:
        statement = select(ContactModel).where(
            ContactModel.contact_number == contact_number
        )
        orm_contact = self._session.scalar(statement)
        if orm_contact is None:
            return None
        return ContactMapper.to_domain(orm_contact)

    def get_by_number(self, contact_number: str) -> Contact | None:
        return self.get_by_contact_number(contact_number)

    def list(self) -> list[Contact]:
        statement = select(ContactModel)
        orm_contacts = self._session.scalars(statement).all()
        return [ContactMapper.to_domain(orm_contact) for orm_contact in orm_contacts]

    def search(self, text: str) -> list[Contact]:
        query = f"%{text}%"
        statement = (
            select(ContactModel)
            .join(ContactPersonModel, ContactModel.contact_person, isouter=True)
            .join(ContactOrganisationModel, ContactModel.contact_organisation, isouter=True)
            .where(
                or_(
                    ContactModel.contact_number.ilike(query),
                    ContactPersonModel.first_name.ilike(query),
                    ContactPersonModel.last_name.ilike(query),
                    ContactOrganisationModel.name.ilike(query),
                )
            )
        )

        orm_contacts = self._session.scalars(statement).all()
        return [ContactMapper.to_domain(orm_contact) for orm_contact in orm_contacts]

    def update(self, contact: Contact) -> None:
        existing = self.get_by_id(contact.id)
        if existing is None:
            raise ValueError(f"Contact {contact.id} does not exist")

        orm_contact = self._session.get(ContactModel, contact.id)
        if orm_contact is None:
            raise ValueError(f"Contact {contact.id} does not exist")

        if contact.contact_number != existing.contact_number:
            other = self.get_by_contact_number(contact.contact_number)
            if other is not None and other.id != contact.id:
                raise ValueError(f"Contact number {contact.contact_number} already exists")

        with self._session.no_autoflush:
            orm_contact.contact_number = contact.contact_number
            orm_contact.status = contact.status
            orm_contact.updated_at = contact.updated_at

            if contact.id is not None:
                self._session.query(ContactPersonModel).filter(
                    ContactPersonModel.contact_id == contact.id
                ).delete(synchronize_session=False)
                self._session.query(ContactOrganisationModel).filter(
                    ContactOrganisationModel.contact_id == contact.id
                ).delete(synchronize_session=False)
                self._session.query(ContactEmailModel).filter(
                    ContactEmailModel.contact_id == contact.id
                ).delete(synchronize_session=False)
                self._session.query(ContactPhoneModel).filter(
                    ContactPhoneModel.contact_id == contact.id
                ).delete(synchronize_session=False)
                self._session.query(ContactAddressModel).filter(
                    ContactAddressModel.contact_id == contact.id
                ).delete(synchronize_session=False)

                self._session.flush()

                if isinstance(contact.party, Person):
                    self._session.add(
                        ContactPersonModel(
                            id=uuid4(),
                            first_name=contact.party.first_name,
                            last_name=contact.party.last_name,
                            middle_name=contact.party.middle_name,
                            title=contact.party.title,
                            birth_date=contact.party.birth_date,
                            contact_id=contact.id,
                        )
                    )
                elif isinstance(contact.party, Organisation):
                    self._session.add(
                        ContactOrganisationModel(
                            id=uuid4(),
                            name=contact.party.name,
                            cvr=contact.party.cvr,
                            vat=contact.party.vat,
                            ean=contact.party.ean,
                            industry=contact.party.industry,
                            contact_id=contact.id,
                        )
                    )

                self._session.add_all(
                    [
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
                )
                self._session.add_all(
                    [
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
                )
                self._session.add_all(
                    [
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
                )

                self._session.flush()

    def delete(self, contact_id: UUID) -> None:
        orm_contact = self._session.get(ContactModel, contact_id)
        if orm_contact is None:
            return

        if orm_contact.contact_person is not None:
            self._session.delete(orm_contact.contact_person)

        if orm_contact.contact_organisation is not None:
            self._session.delete(orm_contact.contact_organisation)

        self._session.delete(orm_contact)
        self._session.flush()

    def exists(self, contact_id: UUID) -> bool:
        return self._session.get(ContactModel, contact_id) is not None
