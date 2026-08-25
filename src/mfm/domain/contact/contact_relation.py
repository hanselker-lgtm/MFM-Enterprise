"""
Relationship between two contacts.
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

from mfm.common.entity import Entity
from mfm.common.enums import RelationType


class ContactRelation(Entity):

    __tablename__ = "CONTACT_RELATION"

    relation_id: Mapped[str] = mapped_column(
        "RelationID",
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    from_contact_id: Mapped[str] = mapped_column(
        "FromContactID",
        ForeignKey("contact.id"),
        nullable=False,
    )

    to_contact_id: Mapped[str] = mapped_column(
        "ToContactID",
        ForeignKey("contact.id"),
        nullable=False,
    )

    relation_type: Mapped[RelationType] = mapped_column(
        "RelationType",
        Enum(RelationType),
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

    # Note: bidirectional ORM relationships to ContactModel were removed here.
    # They referenced a mapped class name ("Contact") that does not exist
    # (the real ORM class is ContactModel) and back_populates fields that
    # were never defined on ContactModel. Nothing in the codebase reads
    # ContactRelation.from_contact / .to_contact; the plain FK columns
    # above are sufficient for current usage.