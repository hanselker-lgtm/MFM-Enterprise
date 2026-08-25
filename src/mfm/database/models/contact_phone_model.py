"""
SQLAlchemy ORM model for contact phones.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.common.enums import PhoneType
from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.contact_model import ContactModel


class ContactPhoneModel(BaseModel):
    """
    Persistence model for contact phones.
    """

    __tablename__ = "contact_phone"

    contact_id: Mapped[UUID] = mapped_column(
        ForeignKey("contact.id"),
        nullable=False,
        index=True,
    )

    number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    phone_type: Mapped[PhoneType] = mapped_column(
        Enum(PhoneType, native_enum=False, length=20),
        nullable=False,
        default=PhoneType.MOBILE,
    )

    primary: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    contact: Mapped["ContactModel"] = relationship(
        "ContactModel",
        back_populates="phones",
    )
