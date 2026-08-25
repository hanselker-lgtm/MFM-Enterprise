"""
SQLAlchemy ORM model for contacts.
"""

from __future__ import annotations

from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.common.enums import ContactStatus
from mfm.database.models.base_model import BaseModel
from mfm.database.models.contact_address_model import ContactAddressModel
from mfm.database.models.contact_email_model import ContactEmailModel
from mfm.database.models.contact_organisation_model import ContactOrganisationModel
from mfm.database.models.contact_person_model import ContactPersonModel
from mfm.database.models.contact_phone_model import ContactPhoneModel


class ContactModel(BaseModel):
    """
    Persistence model for contact aggregates.
    """

    __tablename__ = "contact"

    contact_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    status: Mapped[ContactStatus] = mapped_column(
        Enum(ContactStatus, native_enum=False, length=20),
        nullable=False,
        default=ContactStatus.ACTIVE,
    )

    contact_person: Mapped[ContactPersonModel | None] = relationship(
        ContactPersonModel,
        primaryjoin="ContactModel.id == ContactPersonModel.contact_id",
        foreign_keys="ContactPersonModel.contact_id",
        back_populates="contact",
        uselist=False,
    )

    contact_organisation: Mapped[ContactOrganisationModel | None] = relationship(
        ContactOrganisationModel,
        primaryjoin="ContactModel.id == ContactOrganisationModel.contact_id",
        foreign_keys="ContactOrganisationModel.contact_id",
        back_populates="contact",
        uselist=False,
    )

    emails: Mapped[list[ContactEmailModel]] = relationship(
        ContactEmailModel,
        back_populates="contact",
        cascade="all, delete-orphan",
    )

    phones: Mapped[list[ContactPhoneModel]] = relationship(
        ContactPhoneModel,
        back_populates="contact",
        cascade="all, delete-orphan",
    )

    addresses: Mapped[list[ContactAddressModel]] = relationship(
        ContactAddressModel,
        back_populates="contact",
        cascade="all, delete-orphan",
    )
