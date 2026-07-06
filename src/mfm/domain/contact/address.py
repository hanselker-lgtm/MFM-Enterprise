"""
Address entity.
"""

from __future__ import annotations

import uuid
from datetime import date

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.domain.common.entity import Entity
from mfm.domain.common.enums import AddressType


class Address(Entity):
    """
    Postal address belonging to a Contact.
    """

    __tablename__ = "ADDRESS"

    address_id: Mapped[str] = mapped_column(
        "AddressID",
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    contact_id: Mapped[str] = mapped_column(
        "ContactID",
        ForeignKey("CONTACT.ContactID"),
        nullable=False,
        index=True,
    )

    address_type: Mapped[AddressType] = mapped_column(
        "AddressType",
        Enum(AddressType),
        nullable=False,
    )

    street: Mapped[str] = mapped_column(
        "Street",
        String(200),
        nullable=False,
    )

    postal_code: Mapped[str] = mapped_column(
        "PostalCode",
        String(20),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        "City",
        String(100),
        nullable=False,
    )

    country: Mapped[str] = mapped_column(
        "Country",
        String(100),
        nullable=False,
        default="Danmark",
    )

    valid_from: Mapped[date] = mapped_column(
        "ValidFrom",
        Date,
        nullable=False,
    )

    valid_to: Mapped[date | None] = mapped_column(
        "ValidTo",
        Date,
        nullable=True,
    )

    is_current: Mapped[bool] = mapped_column(
        "IsCurrent",
        Boolean,
        default=True,
        nullable=False,
    )

    contact = relationship(
        "Contact",
        back_populates="addresses",
    )