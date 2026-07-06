"""
Person entity.
"""

from __future__ import annotations

from datetime import date

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base_model import Entity


class Person(Entity):

    __tablename__ = "PERSON"

    contact_id: Mapped[str] = mapped_column(
        "ContactID",
        ForeignKey("CONTACT.ContactID"),
        primary_key=True,
    )

    first_name: Mapped[str] = mapped_column(
        "FirstName",
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        "LastName",
        String(100),
        nullable=False,
    )

    birth_date: Mapped[date | None] = mapped_column(
        "BirthDate",
        Date,
        nullable=True,
    )

    contact = relationship(
        "Contact",
        back_populates="person",
    )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()