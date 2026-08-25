"""
SQLAlchemy ORM model for contact addresses.
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

from mfm.common.enums import AddressType
from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.contact_model import ContactModel


class ContactAddressModel(BaseModel):
    """
    Persistence model for contact addresses.
    """

    __tablename__ = "contact_address"

    contact_id: Mapped[UUID] = mapped_column(
        ForeignKey("contact.id"),
        nullable=False,
        index=True,
    )

    line1: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    line2: Mapped[str] = mapped_column(
        String(200),
        default="",
        nullable=False,
    )

    postal_code: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    state: Mapped[str] = mapped_column(
        String(100),
        default="",
        nullable=False,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    address_type: Mapped[AddressType] = mapped_column(
        Enum(AddressType, native_enum=False, length=20),
        nullable=False,
        default=AddressType.HOME,
    )

    primary: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    contact: Mapped["ContactModel"] = relationship(
        "ContactModel",
        back_populates="addresses",
    )
