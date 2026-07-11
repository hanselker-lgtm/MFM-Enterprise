"""Voyage aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import datetime
from uuid import UUID

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.voyages.events import VoyageArrived
from mfm.domain.voyages.events import VoyageCancelled
from mfm.domain.voyages.events import VoyageCreated
from mfm.domain.voyages.events import VoyageDeparted
from mfm.domain.voyages.events import VoyagePlanned
from mfm.domain.voyages.exceptions import InvalidVoyageChronologyError
from mfm.domain.voyages.exceptions import InvalidVoyageLifecycleError
from mfm.domain.voyages.exceptions import InvalidVoyageStateError
from mfm.domain.voyages.identifiers import VoyageId
from mfm.domain.voyages.location_snapshot import LocationSnapshot
from mfm.domain.voyages.voyage_purpose import VoyagePurpose
from mfm.domain.voyages.voyage_status import VoyageStatus


@dataclass(slots=True)
class Voyage(AggregateRoot):
    """Aggregate root for voyage planning and execution history."""

    vessel_id: UUID
    planned_departure_location: LocationSnapshot
    planned_arrival_location: LocationSnapshot
    planned_departure_at: datetime
    planned_arrival_at: datetime
    id: VoyageId = field(default_factory=VoyageId.new)
    status: VoyageStatus = VoyageStatus.DRAFT
    voyage_reference: str | None = None
    actual_departure_location: LocationSnapshot | None = None
    actual_arrival_location: LocationSnapshot | None = None
    departed_at: datetime | None = None
    arrived_at: datetime | None = None
    voyage_purpose: VoyagePurpose | None = None
    notes: str | None = None
    cancellation_reason: str | None = None
    cancelled_at: datetime | None = None
    cancelled_by_reference: str | None = None
    document_reference: str | None = None

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, VoyageId):
            self.id = VoyageId(self.id)

        self.vessel_id = self._normalize_uuid(self.vessel_id, "vessel_id")

        if not isinstance(self.planned_departure_location, LocationSnapshot):
            raise InvalidVoyageStateError(
                "planned_departure_location must be LocationSnapshot"
            )
        if not isinstance(self.planned_arrival_location, LocationSnapshot):
            raise InvalidVoyageStateError(
                "planned_arrival_location must be LocationSnapshot"
            )

        self.planned_departure_at = self._normalize_aware_datetime(
            self.planned_departure_at,
            "planned_departure_at",
        )
        self.planned_arrival_at = self._normalize_aware_datetime(
            self.planned_arrival_at,
            "planned_arrival_at",
        )

        if self.planned_departure_at > self.planned_arrival_at:
            raise InvalidVoyageChronologyError(
                "planned_departure_at cannot be after planned_arrival_at"
            )

        if not isinstance(self.status, VoyageStatus):
            self.status = VoyageStatus(str(self.status).upper())

        self.voyage_reference = self._normalize_optional_text(
            self.voyage_reference,
            "voyage_reference",
        )
        self.notes = self._normalize_optional_text(self.notes, "notes")
        self.cancellation_reason = self._normalize_optional_text(
            self.cancellation_reason,
            "cancellation_reason",
        )
        self.cancelled_by_reference = self._normalize_optional_text(
            self.cancelled_by_reference,
            "cancelled_by_reference",
        )
        self.document_reference = self._normalize_optional_text(
            self.document_reference,
            "document_reference",
        )

        if self.actual_departure_location is not None and not isinstance(
            self.actual_departure_location,
            LocationSnapshot,
        ):
            raise InvalidVoyageStateError(
                "actual_departure_location must be LocationSnapshot or None"
            )

        if self.actual_arrival_location is not None and not isinstance(
            self.actual_arrival_location,
            LocationSnapshot,
        ):
            raise InvalidVoyageStateError(
                "actual_arrival_location must be LocationSnapshot or None"
            )

        if self.departed_at is not None:
            self.departed_at = self._normalize_aware_datetime(
                self.departed_at,
                "departed_at",
            )
        if self.arrived_at is not None:
            self.arrived_at = self._normalize_aware_datetime(
                self.arrived_at,
                "arrived_at",
            )
        if self.cancelled_at is not None:
            self.cancelled_at = self._normalize_aware_datetime(
                self.cancelled_at,
                "cancelled_at",
            )

        if self.voyage_purpose is not None and not isinstance(
            self.voyage_purpose,
            VoyagePurpose,
        ):
            raise InvalidVoyageStateError("voyage_purpose must be VoyagePurpose or None")

        self._validate_status_invariants()

        self.add_event(VoyageCreated(voyage_id=self.id.value))

    @staticmethod
    def _normalize_uuid(value: UUID | str, field_name: str) -> UUID:
        if isinstance(value, str):
            try:
                return UUID(value)
            except Exception as exc:
                raise InvalidVoyageStateError(f"{field_name} must be UUID") from exc
        if not isinstance(value, UUID):
            raise InvalidVoyageStateError(f"{field_name} must be UUID")
        return value

    @staticmethod
    def _normalize_optional_text(value: str | None, field_name: str) -> str | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise InvalidVoyageStateError(f"{field_name} must be string or None")
        normalized = value.strip()
        return normalized or None

    @staticmethod
    def _normalize_aware_datetime(value: datetime, field_name: str) -> datetime:
        if not isinstance(value, datetime):
            raise InvalidVoyageChronologyError(f"{field_name} must be datetime")
        if value.tzinfo is None or value.utcoffset() is None:
            raise InvalidVoyageChronologyError(
                f"{field_name} must be timezone-aware datetime"
            )
        return value.astimezone(UTC)

    def _validate_status_invariants(self) -> None:
        if self.departed_at is not None and self.arrived_at is not None:
            if self.departed_at > self.arrived_at:
                raise InvalidVoyageChronologyError(
                    "departed_at cannot be after arrived_at"
                )

        if self.status is VoyageStatus.DRAFT:
            if any(
                value is not None
                for value in (
                    self.actual_departure_location,
                    self.actual_arrival_location,
                    self.departed_at,
                    self.arrived_at,
                    self.cancelled_at,
                    self.cancellation_reason,
                    self.cancelled_by_reference,
                )
            ):
                raise InvalidVoyageLifecycleError(
                    "draft voyage cannot have actual or cancellation state"
                )
            return

        if self.status is VoyageStatus.PLANNED:
            if any(
                value is not None
                for value in (
                    self.actual_departure_location,
                    self.actual_arrival_location,
                    self.departed_at,
                    self.arrived_at,
                    self.cancelled_at,
                    self.cancellation_reason,
                    self.cancelled_by_reference,
                )
            ):
                raise InvalidVoyageLifecycleError(
                    "planned voyage cannot have actual or cancellation state"
                )
            return

        if self.status is VoyageStatus.UNDERWAY:
            if self.departed_at is None or self.actual_departure_location is None:
                raise InvalidVoyageLifecycleError(
                    "underway voyage requires departure state"
                )
            if any(
                value is not None
                for value in (
                    self.arrived_at,
                    self.actual_arrival_location,
                    self.cancelled_at,
                    self.cancellation_reason,
                    self.cancelled_by_reference,
                )
            ):
                raise InvalidVoyageLifecycleError(
                    "underway voyage cannot have arrival or cancellation state"
                )
            return

        if self.status is VoyageStatus.COMPLETED:
            if (
                self.departed_at is None
                or self.actual_departure_location is None
                or self.arrived_at is None
                or self.actual_arrival_location is None
            ):
                raise InvalidVoyageLifecycleError(
                    "completed voyage requires full actual departure and arrival state"
                )
            if any(
                value is not None
                for value in (
                    self.cancelled_at,
                    self.cancellation_reason,
                    self.cancelled_by_reference,
                )
            ):
                raise InvalidVoyageLifecycleError(
                    "completed voyage cannot have cancellation state"
                )
            return

        if self.status is VoyageStatus.CANCELLED:
            if self.cancellation_reason is None or self.cancelled_at is None:
                raise InvalidVoyageLifecycleError(
                    "cancelled voyage requires cancellation_reason and cancelled_at"
                )
            if any(
                value is not None
                for value in (
                    self.actual_departure_location,
                    self.actual_arrival_location,
                    self.departed_at,
                    self.arrived_at,
                )
            ):
                raise InvalidVoyageLifecycleError(
                    "cancelled voyage cannot have actual departure or arrival state"
                )
            return

        raise InvalidVoyageStateError("unsupported voyage status")

    def plan(self) -> None:
        if self.status is not VoyageStatus.DRAFT:
            raise InvalidVoyageLifecycleError("only draft voyage can be planned")
        self.status = VoyageStatus.PLANNED
        self.add_event(VoyagePlanned(voyage_id=self.id.value))

    def depart(
        self,
        *,
        departed_at: datetime,
        actual_departure_location: LocationSnapshot,
    ) -> None:
        if self.status is not VoyageStatus.PLANNED:
            raise InvalidVoyageLifecycleError("only planned voyage can depart")
        if not isinstance(actual_departure_location, LocationSnapshot):
            raise InvalidVoyageStateError(
                "actual_departure_location must be LocationSnapshot"
            )

        normalized_departed_at = self._normalize_aware_datetime(
            departed_at,
            "departed_at",
        )

        self.departed_at = normalized_departed_at
        self.actual_departure_location = actual_departure_location
        self.status = VoyageStatus.UNDERWAY
        self.add_event(
            VoyageDeparted(
                voyage_id=self.id.value,
                departed_at=self.departed_at,
            )
        )

    def arrive(
        self,
        *,
        arrived_at: datetime,
        actual_arrival_location: LocationSnapshot,
    ) -> None:
        if self.status is not VoyageStatus.UNDERWAY:
            raise InvalidVoyageLifecycleError("only underway voyage can arrive")
        if self.departed_at is None:
            raise InvalidVoyageLifecycleError(
                "voyage must have departed before arrival"
            )
        if not isinstance(actual_arrival_location, LocationSnapshot):
            raise InvalidVoyageStateError(
                "actual_arrival_location must be LocationSnapshot"
            )

        normalized_arrived_at = self._normalize_aware_datetime(
            arrived_at,
            "arrived_at",
        )
        if normalized_arrived_at < self.departed_at:
            raise InvalidVoyageChronologyError(
                "arrived_at cannot be before departed_at"
            )

        self.arrived_at = normalized_arrived_at
        self.actual_arrival_location = actual_arrival_location
        self.status = VoyageStatus.COMPLETED
        self.add_event(
            VoyageArrived(
                voyage_id=self.id.value,
                arrived_at=self.arrived_at,
            )
        )

    def cancel(
        self,
        *,
        cancellation_reason: str,
        cancelled_at: datetime,
        cancelled_by_reference: str | None = None,
    ) -> None:
        if self.status not in {VoyageStatus.DRAFT, VoyageStatus.PLANNED}:
            raise InvalidVoyageLifecycleError(
                "only draft or planned voyage can be cancelled"
            )

        normalized_reason = self._normalize_optional_text(
            cancellation_reason,
            "cancellation_reason",
        )
        if normalized_reason is None:
            raise InvalidVoyageStateError("cancellation_reason must be non-empty")

        self.cancellation_reason = normalized_reason
        self.cancelled_at = self._normalize_aware_datetime(
            cancelled_at,
            "cancelled_at",
        )
        self.cancelled_by_reference = self._normalize_optional_text(
            cancelled_by_reference,
            "cancelled_by_reference",
        )
        self.status = VoyageStatus.CANCELLED
        self.add_event(
            VoyageCancelled(
                voyage_id=self.id.value,
                cancelled_at=self.cancelled_at,
            )
        )