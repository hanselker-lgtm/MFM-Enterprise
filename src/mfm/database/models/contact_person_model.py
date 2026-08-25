"""
SQLAlchemy ORM model for contact persons.
"""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.contact_model import ContactModel


class ContactPersonModel(BaseModel):
    """
    Persistence model for a person contact.
    """

    __tablename__ = "contact_person"

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    middle_name: Mapped[str] = mapped_column(
        String(100),
        default="",
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(50),
        default="",
        nullable=False,
    )

    birth_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    contact_id: Mapped[UUID] = mapped_column(
        ForeignKey("contact.id"),
        unique=True,
        nullable=False,
    )

    contact: Mapped["ContactModel"] = relationship(
        "ContactModel",
        back_populates="contact_person",
        uselist=False,
    )
