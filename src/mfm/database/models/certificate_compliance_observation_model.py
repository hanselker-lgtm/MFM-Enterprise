"""SQLAlchemy ORM model for certificate compliance observations."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from mfm.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from mfm.database.models.certificate_model import CertificateModel


class CertificateComplianceObservationModel(BaseModel):
    """Persistence model for certificate-owned compliance observation."""

    __tablename__ = "certificate_compliance_observation"

    certificate_id: Mapped[UUID] = mapped_column(
        ForeignKey("certificate.id"),
        nullable=False,
        index=True,
    )

    observation_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    summary: Mapped[str] = mapped_column(
        String(2000),
        nullable=False,
    )

    observed_on: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    requires_maintenance_work: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    certificate: Mapped["CertificateModel"] = relationship(
        "CertificateModel",
        back_populates="compliance_observations",
    )
