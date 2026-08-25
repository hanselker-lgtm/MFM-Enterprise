"""
SQLAlchemy ORM model for contact organisations.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.contact_model import ContactModel


class ContactOrganisationModel(BaseModel):
    """
    Persistence model for an organisation contact.
    """

    __tablename__ = "contact_organisation"

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    cvr: Mapped[str] = mapped_column(
        String(50),
        default="",
        nullable=False,
    )

    vat: Mapped[str] = mapped_column(
        String(50),
        default="",
        nullable=False,
    )

    ean: Mapped[str] = mapped_column(
        String(50),
        default="",
        nullable=False,
    )

    industry: Mapped[str] = mapped_column(
        String(100),
        default="",
        nullable=False,
    )

    contact_id: Mapped[UUID] = mapped_column(
        ForeignKey("contact.id"),
        unique=True,
        nullable=False,
    )

    contact: Mapped["ContactModel"] = relationship(
        "ContactModel",
        back_populates="contact_organisation",
        uselist=False,
    )
