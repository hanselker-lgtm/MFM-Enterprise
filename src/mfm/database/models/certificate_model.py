"""SQLAlchemy ORM model for certificates."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel
from mfm.domain.certificates.certificate_status import CertificateStatus
from mfm.domain.certificates.certificate_target_type import CertificateTargetType
from mfm.domain.certificates.issuer_reference_type import IssuerReferenceType

if TYPE_CHECKING:
    from mfm.database.models.certificate_compliance_observation_model import (
        CertificateComplianceObservationModel,
    )


class CertificateModel(BaseModel):
    """Persistence model for certificate aggregate root."""

    __tablename__ = "certificate"

    certificate_type_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    certificate_type_code: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    certificate_type_display_name_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    certificate_number: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    target_type: Mapped[CertificateTargetType] = mapped_column(
        Enum(CertificateTargetType, native_enum=False, length=40),
        nullable=False,
    )

    target_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    issuer_type: Mapped[IssuerReferenceType] = mapped_column(
        Enum(IssuerReferenceType, native_enum=False, length=40),
        nullable=False,
    )

    issuer_id_or_external_key: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    issuer_name_snapshot: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    issued_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    valid_from: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    expires_at: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[CertificateStatus] = mapped_column(
        Enum(CertificateStatus, native_enum=False, length=20),
        nullable=False,
        default=CertificateStatus.DRAFT,
    )

    renewal_required: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    renewed_from_certificate_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("certificate.id"),
        nullable=True,
        index=True,
    )

    document_reference: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    external_document_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        String(4000),
        nullable=True,
    )

    compliance_observations: Mapped[list["CertificateComplianceObservationModel"]] = relationship(
        "CertificateComplianceObservationModel",
        back_populates="certificate",
        cascade="all, delete-orphan",
        single_parent=True,
    )
