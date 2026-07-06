"""
Organisation domain model.
"
rom .base_model import Entity

from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.domain.base import Base


class Organisation(Entity):

    __tablename__ = "ORGANISATION"

    contact_id: Mapped[str] = mapped_column(
        "ContactID",
        ForeignKey("CONTACT.id"),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        "Name",
        String(200),
        nullable=False,
    )

    cvr: Mapped[str | None] = mapped_column(
        "CVR",
        String(20),
        nullable=True,
    )

    country: Mapped[str] = mapped_column(
        "Country",
        String(100),
        default="Danmark",
        nullable=False,
    )

    contact = relationship(
        "Contact",
        back_populates="organisation",
    )