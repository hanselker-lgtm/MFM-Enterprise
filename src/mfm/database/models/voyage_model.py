"""SQLAlchemy ORM model for voyages."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from mfm.database.models.base_model import BaseModel
from mfm.domain.voyages.voyage_purpose_code import VoyagePurposeCode
from mfm.domain.voyages.voyage_status import VoyageStatus


class VoyageModel(BaseModel):
    """Persistence model for the Voyage aggregate."""

    __tablename__ = "voyage"

    vessel_id: Mapped[UUID] = mapped_column(
        nullable=False,
        index=True,
    )

    voyage_reference: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    planned_departure_location_external_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    planned_departure_location_name_snapshot: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    planned_departure_location_locality_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    planned_departure_location_country_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    planned_arrival_location_external_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    planned_arrival_location_name_snapshot: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    planned_arrival_location_locality_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    planned_arrival_location_country_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    planned_departure_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    planned_arrival_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    status: Mapped[VoyageStatus] = mapped_column(
        Enum(VoyageStatus, native_enum=False, length=20),
        nullable=False,
        default=VoyageStatus.DRAFT,
    )

    actual_departure_location_external_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    actual_departure_location_name_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    actual_departure_location_locality_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    actual_departure_location_country_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    actual_arrival_location_external_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    actual_arrival_location_name_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    actual_arrival_location_locality_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    actual_arrival_location_country_snapshot: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    departed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    arrived_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    purpose_code: Mapped[VoyagePurposeCode | None] = mapped_column(
        Enum(VoyagePurposeCode, native_enum=False, length=40),
        nullable=True,
    )
    purpose_detail: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        String(4000),
        nullable=True,
    )

    cancellation_reason: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )
    cancelled_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    cancelled_by_reference: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    document_reference: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )