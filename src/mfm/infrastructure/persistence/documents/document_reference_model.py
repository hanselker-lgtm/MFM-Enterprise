"""SQLAlchemy ORM model for document versions and cross-capability references."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.infrastructure.persistence.documents.document_model import DocumentModel


class DocumentReferenceModel(BaseModel):
    """Persistence model for document version metadata and external references."""

    __tablename__ = "document_reference"
    __table_args__ = (
        UniqueConstraint(
            "document_id",
            "reference_order",
            name="uq_document_reference_order",
        ),
        UniqueConstraint(
            "document_id",
            "version_number",
            name="uq_document_reference_version_number",
        ),
    )

    document_id: Mapped[UUID] = mapped_column(
        ForeignKey("document.id"),
        nullable=False,
        index=True,
    )

    reference_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    version_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    storage_key: Mapped[str] = mapped_column(
        String(1024),
        nullable=False,
    )

    file_name: Mapped[str | None] = mapped_column(
        String(512),
        nullable=True,
    )

    mime_type: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    checksum: Mapped[str | None] = mapped_column(
        String(512),
        nullable=True,
    )

    size_bytes: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    version_created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    target_capability: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
        index=True,
    )

    target_aggregate_type: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    target_aggregate_id: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        index=True,
    )

    exists: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    authorized: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    is_soft_deleted: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    is_archived: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    checked_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(2000),
        nullable=True,
    )

    document: Mapped["DocumentModel"] = relationship(
        "DocumentModel",
        back_populates="references",
    )
