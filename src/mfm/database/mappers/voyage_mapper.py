"""Mapper between voyages domain and persistence models."""

from __future__ import annotations

from datetime import UTC
from datetime import datetime

from mfm.database.models.voyage_model import VoyageModel
from mfm.domain.voyages.identifiers import VoyageId
from mfm.domain.voyages.location_snapshot import LocationSnapshot
from mfm.domain.voyages.voyage import Voyage
from mfm.domain.voyages.voyage_purpose import VoyagePurpose


class VoyageMapper:
    """Map Voyage aggregate to/from SQLAlchemy model."""

    @staticmethod
    def to_orm_voyage(voyage: Voyage) -> VoyageModel:
        return VoyageModel(
            id=voyage.id.value,
            vessel_id=voyage.vessel_id,
            voyage_reference=voyage.voyage_reference,
            planned_departure_location_external_id=(
                voyage.planned_departure_location.location_external_id
            ),
            planned_departure_location_name_snapshot=(
                voyage.planned_departure_location.name_snapshot
            ),
            planned_departure_location_locality_snapshot=(
                voyage.planned_departure_location.locality_snapshot
            ),
            planned_departure_location_country_snapshot=(
                voyage.planned_departure_location.country_snapshot
            ),
            planned_arrival_location_external_id=(
                voyage.planned_arrival_location.location_external_id
            ),
            planned_arrival_location_name_snapshot=(
                voyage.planned_arrival_location.name_snapshot
            ),
            planned_arrival_location_locality_snapshot=(
                voyage.planned_arrival_location.locality_snapshot
            ),
            planned_arrival_location_country_snapshot=(
                voyage.planned_arrival_location.country_snapshot
            ),
            planned_departure_at=voyage.planned_departure_at,
            planned_arrival_at=voyage.planned_arrival_at,
            status=voyage.status,
            actual_departure_location_external_id=(
                voyage.actual_departure_location.location_external_id
                if voyage.actual_departure_location is not None
                else None
            ),
            actual_departure_location_name_snapshot=(
                voyage.actual_departure_location.name_snapshot
                if voyage.actual_departure_location is not None
                else None
            ),
            actual_departure_location_locality_snapshot=(
                voyage.actual_departure_location.locality_snapshot
                if voyage.actual_departure_location is not None
                else None
            ),
            actual_departure_location_country_snapshot=(
                voyage.actual_departure_location.country_snapshot
                if voyage.actual_departure_location is not None
                else None
            ),
            actual_arrival_location_external_id=(
                voyage.actual_arrival_location.location_external_id
                if voyage.actual_arrival_location is not None
                else None
            ),
            actual_arrival_location_name_snapshot=(
                voyage.actual_arrival_location.name_snapshot
                if voyage.actual_arrival_location is not None
                else None
            ),
            actual_arrival_location_locality_snapshot=(
                voyage.actual_arrival_location.locality_snapshot
                if voyage.actual_arrival_location is not None
                else None
            ),
            actual_arrival_location_country_snapshot=(
                voyage.actual_arrival_location.country_snapshot
                if voyage.actual_arrival_location is not None
                else None
            ),
            departed_at=voyage.departed_at,
            arrived_at=voyage.arrived_at,
            purpose_code=(
                voyage.voyage_purpose.purpose_code
                if voyage.voyage_purpose is not None
                else None
            ),
            purpose_detail=(
                voyage.voyage_purpose.purpose_detail
                if voyage.voyage_purpose is not None
                else None
            ),
            notes=voyage.notes,
            cancellation_reason=voyage.cancellation_reason,
            cancelled_at=voyage.cancelled_at,
            cancelled_by_reference=voyage.cancelled_by_reference,
            document_reference=voyage.document_reference,
        )

    @staticmethod
    def to_domain_voyage(orm: VoyageModel) -> Voyage:
        voyage = Voyage(
            id=VoyageId(orm.id),
            vessel_id=orm.vessel_id,
            planned_departure_location=LocationSnapshot(
                location_external_id=orm.planned_departure_location_external_id,
                name_snapshot=orm.planned_departure_location_name_snapshot,
                locality_snapshot=orm.planned_departure_location_locality_snapshot,
                country_snapshot=orm.planned_departure_location_country_snapshot,
            ),
            planned_arrival_location=LocationSnapshot(
                location_external_id=orm.planned_arrival_location_external_id,
                name_snapshot=orm.planned_arrival_location_name_snapshot,
                locality_snapshot=orm.planned_arrival_location_locality_snapshot,
                country_snapshot=orm.planned_arrival_location_country_snapshot,
            ),
            planned_departure_at=VoyageMapper._normalize_timestamp(
                orm.planned_departure_at,
            ),
            planned_arrival_at=VoyageMapper._normalize_timestamp(
                orm.planned_arrival_at,
            ),
            status=orm.status,
            voyage_reference=orm.voyage_reference,
            actual_departure_location=(
                None
                if orm.actual_departure_location_name_snapshot is None
                else LocationSnapshot(
                    location_external_id=orm.actual_departure_location_external_id,
                    name_snapshot=orm.actual_departure_location_name_snapshot,
                    locality_snapshot=orm.actual_departure_location_locality_snapshot,
                    country_snapshot=orm.actual_departure_location_country_snapshot,
                )
            ),
            actual_arrival_location=(
                None
                if orm.actual_arrival_location_name_snapshot is None
                else LocationSnapshot(
                    location_external_id=orm.actual_arrival_location_external_id,
                    name_snapshot=orm.actual_arrival_location_name_snapshot,
                    locality_snapshot=orm.actual_arrival_location_locality_snapshot,
                    country_snapshot=orm.actual_arrival_location_country_snapshot,
                )
            ),
            departed_at=(
                None
                if orm.departed_at is None
                else VoyageMapper._normalize_timestamp(orm.departed_at)
            ),
            arrived_at=(
                None
                if orm.arrived_at is None
                else VoyageMapper._normalize_timestamp(orm.arrived_at)
            ),
            voyage_purpose=(
                None
                if orm.purpose_code is None
                else VoyagePurpose(
                    purpose_code=orm.purpose_code,
                    purpose_detail=orm.purpose_detail,
                )
            ),
            notes=orm.notes,
            cancellation_reason=orm.cancellation_reason,
            cancelled_at=(
                None
                if orm.cancelled_at is None
                else VoyageMapper._normalize_timestamp(orm.cancelled_at)
            ),
            cancelled_by_reference=orm.cancelled_by_reference,
            document_reference=orm.document_reference,
        )

        voyage.pull_events()
        return voyage

    @staticmethod
    def _normalize_timestamp(value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)