"""
SQLAlchemy ORM model for contact emails.
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

from mfm.common.enums import EmailType
from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.contact_model import ContactModel


class ContactEmailModel(BaseModel):
    """
    Persistence model for contact emails.
    """

    __tablename__ = "contact_email"

    contact_id: Mapped[UUID] = mapped_column(
        ForeignKey("contact.id"),
        nullable=False,
        index=True,
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    email_type: Mapped[EmailType] = mapped_column(
        Enum(EmailType, native_enum=False, length=20),
        nullable=False,
        default=EmailType.PRIVATE,
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
        back_populates="emails",
    )
