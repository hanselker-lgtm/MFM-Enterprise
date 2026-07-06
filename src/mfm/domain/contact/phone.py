"""
Phone entity.
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
from mfm.domain.common.enums import PhoneType


class Phone(Entity):

    __tablename__ = "PHONE"

    phone_id: Mapped[str] = mapped_column(
        "PhoneID",
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

    phone: Mapped[str] = mapped_column(
        "Phone",
        String(30),
        nullable=False,
    )

    phone_type: Mapped[PhoneType] = mapped_column(
        "PhoneType",
        Enum(PhoneType),
        nullable=False,
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
        back_populates="phones",
    )