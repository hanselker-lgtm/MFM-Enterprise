"""SQLAlchemy ORM model for document aggregate root metadata."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.document.document_status import DocumentStatus

if TYPE_CHECKING:
    from mfm.infrastructure.persistence.documents.document_reference_model import DocumentReferenceModel


class DocumentModel(BaseModel):
    """Persistence model for Document aggregate root."""

    __tablename__ = "document"

    document_number: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True,
        index=True,
    )

    document_title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    document_type: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(4000),
        nullable=True,
    )

    status: Mapped[DocumentStatus] = mapped_column(
        Enum(DocumentStatus, native_enum=False, length=20),
        nullable=False,
        default=DocumentStatus.DRAFT,
    )

    document_created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    document_updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    archived_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    disposed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    references: Mapped[list["DocumentReferenceModel"]] = relationship(
        "DocumentReferenceModel",
        back_populates="document",
        cascade="all, delete-orphan",
        single_parent=True,
        order_by="DocumentReferenceModel.reference_order",
    )
