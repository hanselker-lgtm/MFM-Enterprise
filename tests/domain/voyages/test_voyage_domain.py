from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import UTC
from datetime import datetime
from datetime import timedelta
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.voyages.events import VoyageArrived
from mfm.domain.voyages.events import VoyageCancelled
from mfm.domain.voyages.events import VoyageCreated
from mfm.domain.voyages.events import VoyageDeparted
from mfm.domain.voyages.events import VoyagePlanned
from mfm.domain.voyages.exceptions import InvalidVoyageChronologyError
from mfm.domain.voyages.exceptions import InvalidVoyageLifecycleError
from mfm.domain.voyages.exceptions import InvalidVoyageLocationError
from mfm.domain.voyages.exceptions import InvalidVoyagePurposeError
from mfm.domain.voyages.exceptions import InvalidVoyageStateError
from mfm.domain.voyages.location_snapshot import LocationSnapshot
from mfm.domain.voyages.voyage import Voyage
from mfm.domain.voyages.voyage_purpose import VoyagePurpose
from mfm.domain.voyages.voyage_purpose_code import VoyagePurposeCode
from mfm.domain.voyages.voyage_status import VoyageStatus


def _dt(
    year: int,
    month: int,
    day: int,
    hour: int = 0,
    minute: int = 0,
    tz_offset_hours: int = 0,
) -> datetime:
    return datetime(
        year,
        month,
        day,
        hour,
        minute,
        tzinfo=UTC if tz_offset_hours == 0 else UTC,
    ) + timedelta(hours=tz_offset_hours)


def _aware_with_offset(
    year: int,
    month: int,
    day: int,
    hour: int = 0,
    minute: int = 0,
    offset_hours: int = 0,
) -> datetime:
    return datetime(
        year,
        month,
        day,
        hour,
        minute,
        tzinfo=UTC,
    ).astimezone(UTC) + timedelta(hours=offset_hours)


def _location(
    name: str,
    *,
    external_id: str | None = None,
    locality: str | None = None,
    country: str | None = None,
) -> LocationSnapshot:
    return LocationSnapshot(
        name_snapshot=name,
        location_external_id=external_id,
        locality_snapshot=locality,
        country_snapshot=country,
    )


def _purpose(code: VoyagePurposeCode = VoyagePurposeCode.DEMONSTRATION) -> VoyagePurpose:
    return VoyagePurpose(purpose_code=code, purpose_detail="Open day sailing")


def _voyage(
    *,
    vessel_id: UUID | None = None,
    planned_departure_location: LocationSnapshot | None = None,
    planned_arrival_location: LocationSnapshot | None = None,
    planned_departure_at: datetime | None = None,
    planned_arrival_at: datetime | None = None,
    voyage_reference: str | None = "VOY-ALPHA",
    voyage_purpose: VoyagePurpose | None = None,
    notes: str | None = "Historic demonstration run",
    document_reference: str | None = "DOC-VOY-1",
) -> Voyage:
    return Voyage(
        vessel_id=vessel_id or uuid4(),
        planned_departure_location=planned_departure_location or _location(
            "Location A",
            external_id="PORT-A",
            locality="Harbor A",
            country="Country A",
        ),
        planned_arrival_location=planned_arrival_location or _location(
            "Location B",
            external_id="PORT-B",
            locality="Harbor B",
            country="Country B",
        ),
        planned_departure_at=planned_departure_at or datetime(2027, 6, 1, 8, 0, tzinfo=UTC),
        planned_arrival_at=planned_arrival_at or datetime(2027, 6, 1, 18, 0, tzinfo=UTC),
        voyage_reference=voyage_reference,
        voyage_purpose=voyage_purpose or _purpose(),
        notes=notes,
        document_reference=document_reference,
    )


def test_vessel_reference_valid_uuid_identity_only() -> None:
    vessel_id = uuid4()
    voyage = _voyage(vessel_id=vessel_id)

    assert voyage.vessel_id == vessel_id
    assert isinstance(voyage.vessel_id, UUID)


def test_vessel_reference_missing_identity_rejected() -> None:
    with pytest.raises(InvalidVoyageStateError):
        Voyage(
            vessel_id=None,  # type: ignore[arg-type]
            planned_departure_location=_location("Location A"),
            planned_arrival_location=_location("Location B"),
            planned_departure_at=datetime(2027, 6, 1, 8, 0, tzinfo=UTC),
            planned_arrival_at=datetime(2027, 6, 1, 18, 0, tzinfo=UTC),
        )


def test_location_snapshot_valid_and_immutable() -> None:
    location = _location(
        "Port Name A",
        external_id="PORT-A",
        locality="Town A",
        country="Country A",
    )

    assert location.name_snapshot == "Port Name A"
    assert location.location_external_id == "PORT-A"

    with pytest.raises(FrozenInstanceError):
        location.name_snapshot = "Changed"  # type: ignore[misc]


def test_location_snapshot_requires_name() -> None:
    with pytest.raises(InvalidVoyageLocationError):
        LocationSnapshot(name_snapshot=" ")


def test_location_snapshot_preserves_historical_snapshot_independently() -> None:
    planned = _location("Port Name A", external_id="PORT-1")
    actual = _location("Port Name A - Historical", external_id="PORT-1")

    assert planned.name_snapshot == "Port Name A"
    assert actual.name_snapshot == "Port Name A - Historical"


@pytest.mark.parametrize(
    "code",
    [
        VoyagePurposeCode.OPERATIONAL,
        VoyagePurposeCode.TRAINING,
        VoyagePurposeCode.PRESERVATION,
        VoyagePurposeCode.DEMONSTRATION,
        VoyagePurposeCode.TRANSFER,
        VoyagePurposeCode.INSPECTION,
        VoyagePurposeCode.OTHER,
    ],
)
def test_voyage_purpose_valid_codes(code: VoyagePurposeCode) -> None:
    purpose = VoyagePurpose(purpose_code=code, purpose_detail="detail")

    assert purpose.purpose_code is code


def test_voyage_purpose_invalid_code_rejected() -> None:
    with pytest.raises(InvalidVoyagePurposeError):
        VoyagePurpose(purpose_code="INVALID")  # type: ignore[arg-type]


def test_voyage_purpose_immutable() -> None:
    purpose = _purpose()

    with pytest.raises(FrozenInstanceError):
        purpose.purpose_detail = "Changed"  # type: ignore[misc]


def test_voyage_creation_valid_initial_state_and_created_event() -> None:
    voyage = _voyage()
    events = voyage.pull_events()

    assert voyage.status is VoyageStatus.DRAFT
    assert voyage.voyage_reference == "VOY-ALPHA"
    assert any(isinstance(event, VoyageCreated) for event in events)


def test_voyage_creation_invalid_planned_chronology_rejected() -> None:
    with pytest.raises(InvalidVoyageChronologyError):
        _voyage(
            planned_departure_at=datetime(2027, 6, 2, 8, 0, tzinfo=UTC),
            planned_arrival_at=datetime(2027, 6, 1, 18, 0, tzinfo=UTC),
        )


def test_voyage_creation_requires_timezone_aware_planned_timestamps() -> None:
    with pytest.raises(InvalidVoyageChronologyError):
        _voyage(
            planned_departure_at=datetime(2027, 6, 1, 8, 0),
            planned_arrival_at=datetime(2027, 6, 1, 18, 0, tzinfo=UTC),
        )


def test_voyage_creation_normalizes_aware_timestamps_for_storage() -> None:
    departure = datetime(2027, 6, 1, 10, 0, tzinfo=UTC)
    arrival = datetime(2027, 6, 1, 20, 0, tzinfo=UTC)

    voyage = _voyage(planned_departure_at=departure, planned_arrival_at=arrival)

    assert voyage.planned_departure_at.tzinfo is UTC
    assert voyage.planned_arrival_at.tzinfo is UTC


def test_plan_valid_transition_and_event() -> None:
    voyage = _voyage()
    voyage.pull_events()

    voyage.plan()
    events = voyage.pull_events()

    assert voyage.status is VoyageStatus.PLANNED
    assert any(isinstance(event, VoyagePlanned) for event in events)


def test_plan_invalid_transition_rejected() -> None:
    voyage = _voyage()
    voyage.plan()

    with pytest.raises(InvalidVoyageLifecycleError):
        voyage.plan()


def test_depart_valid_transition_preserves_planned_context_and_emits_event() -> None:
    voyage = _voyage()
    voyage.plan()
    voyage.pull_events()
    actual_departure = _location("Location A", external_id="PORT-A")
    departed_at = datetime(2027, 6, 1, 9, 0, tzinfo=UTC)

    voyage.depart(
        departed_at=departed_at,
        actual_departure_location=actual_departure,
    )
    events = voyage.pull_events()

    assert voyage.status is VoyageStatus.UNDERWAY
    assert voyage.actual_departure_location == actual_departure
    assert voyage.planned_departure_location.name_snapshot == "Location A"
    assert voyage.departed_at == departed_at
    assert any(isinstance(event, VoyageDeparted) for event in events)


def test_depart_invalid_state_rejected() -> None:
    voyage = _voyage()

    with pytest.raises(InvalidVoyageLifecycleError):
        voyage.depart(
            departed_at=datetime(2027, 6, 1, 9, 0, tzinfo=UTC),
            actual_departure_location=_location("Location A"),
        )


def test_depart_requires_timezone_aware_timestamp() -> None:
    voyage = _voyage()
    voyage.plan()

    with pytest.raises(InvalidVoyageChronologyError):
        voyage.depart(
            departed_at=datetime(2027, 6, 1, 9, 0),
            actual_departure_location=_location("Location A"),
        )


def test_arrive_valid_transition_preserves_planned_and_actual_context_and_emits_event() -> None:
    voyage = _voyage()
    voyage.plan()
    voyage.depart(
        departed_at=datetime(2027, 6, 1, 9, 0, tzinfo=UTC),
        actual_departure_location=_location("Location A", external_id="PORT-A"),
    )
    voyage.pull_events()
    actual_arrival = _location("Location C", external_id="PORT-C")
    arrived_at = datetime(2027, 6, 1, 19, 30, tzinfo=UTC)

    voyage.arrive(arrived_at=arrived_at, actual_arrival_location=actual_arrival)
    events = voyage.pull_events()

    assert voyage.status is VoyageStatus.COMPLETED
    assert voyage.planned_arrival_location.name_snapshot == "Location B"
    assert voyage.actual_arrival_location == actual_arrival
    assert voyage.arrived_at == arrived_at
    assert any(isinstance(event, VoyageArrived) for event in events)


def test_arrive_invalid_state_rejected() -> None:
    voyage = _voyage()
    voyage.plan()

    with pytest.raises(InvalidVoyageLifecycleError):
        voyage.arrive(
            arrived_at=datetime(2027, 6, 1, 19, 0, tzinfo=UTC),
            actual_arrival_location=_location("Location B"),
        )


def test_arrive_before_departure_rejected() -> None:
    voyage = _voyage()
    voyage.plan()
    voyage.depart(
        departed_at=datetime(2027, 6, 1, 9, 0, tzinfo=UTC),
        actual_departure_location=_location("Location A"),
    )

    with pytest.raises(InvalidVoyageChronologyError):
        voyage.arrive(
            arrived_at=datetime(2027, 6, 1, 8, 59, tzinfo=UTC),
            actual_arrival_location=_location("Location C"),
        )


def test_historical_voyage_truth_preserves_plan_and_actual_independently() -> None:
    planned_departure = _location("Location A", external_id="PORT-A")
    planned_arrival = _location("Location B", external_id="PORT-B")
    voyage = _voyage(
        planned_departure_location=planned_departure,
        planned_arrival_location=planned_arrival,
        planned_departure_at=datetime(2027, 7, 1, 8, 0, tzinfo=UTC),
        planned_arrival_at=datetime(2027, 7, 1, 18, 0, tzinfo=UTC),
    )
    voyage.plan()

    actual_departure = _location("Location A", external_id="PORT-A")
    actual_arrival = _location("Location C", external_id="PORT-C")
    actual_departure_at = datetime(2027, 7, 1, 9, 0, tzinfo=UTC)
    actual_arrival_at = datetime(2027, 7, 1, 20, 30, tzinfo=UTC)

    voyage.depart(
        departed_at=actual_departure_at,
        actual_departure_location=actual_departure,
    )
    voyage.arrive(
        arrived_at=actual_arrival_at,
        actual_arrival_location=actual_arrival,
    )

    assert voyage.planned_departure_location.name_snapshot == "Location A"
    assert voyage.planned_arrival_location.name_snapshot == "Location B"
    assert voyage.planned_departure_at == datetime(2027, 7, 1, 8, 0, tzinfo=UTC)
    assert voyage.planned_arrival_at == datetime(2027, 7, 1, 18, 0, tzinfo=UTC)
    assert voyage.actual_departure_location.name_snapshot == "Location A"
    assert voyage.actual_arrival_location.name_snapshot == "Location C"
    assert voyage.departed_at == actual_departure_at
    assert voyage.arrived_at == actual_arrival_at


def test_cancel_from_draft_valid_and_no_actual_context_fabricated() -> None:
    voyage = _voyage()
    voyage.pull_events()

    voyage.cancel(
        cancellation_reason="Weather window closed",
        cancelled_at=datetime(2027, 6, 1, 7, 30, tzinfo=UTC),
    )
    events = voyage.pull_events()

    assert voyage.status is VoyageStatus.CANCELLED
    assert voyage.actual_departure_location is None
    assert voyage.actual_arrival_location is None
    assert any(isinstance(event, VoyageCancelled) for event in events)


def test_cancel_from_planned_valid_and_preserves_planned_context() -> None:
    voyage = _voyage()
    voyage.plan()

    voyage.cancel(
        cancellation_reason="Crew unavailable",
        cancelled_at=datetime(2027, 6, 1, 7, 45, tzinfo=UTC),
        cancelled_by_reference="scheduler-1",
    )

    assert voyage.status is VoyageStatus.CANCELLED
    assert voyage.planned_arrival_location.name_snapshot == "Location B"
    assert voyage.departed_at is None
    assert voyage.arrived_at is None


@pytest.mark.parametrize("status_action", ["completed", "cancelled"])
def test_terminal_state_rejects_mutating_operations(status_action: str) -> None:
    voyage = _voyage()
    voyage.plan()
    if status_action == "completed":
        voyage.depart(
            departed_at=datetime(2027, 6, 1, 9, 0, tzinfo=UTC),
            actual_departure_location=_location("Location A"),
        )
        voyage.arrive(
            arrived_at=datetime(2027, 6, 1, 19, 0, tzinfo=UTC),
            actual_arrival_location=_location("Location B"),
        )
    else:
        voyage.cancel(
            cancellation_reason="No go",
            cancelled_at=datetime(2027, 6, 1, 7, 15, tzinfo=UTC),
        )

    with pytest.raises(InvalidVoyageLifecycleError):
        voyage.plan()
    with pytest.raises(InvalidVoyageLifecycleError):
        voyage.depart(
            departed_at=datetime(2027, 6, 1, 9, 30, tzinfo=UTC),
            actual_departure_location=_location("Location A"),
        )
    with pytest.raises(InvalidVoyageLifecycleError):
        voyage.cancel(
            cancellation_reason="Too late",
            cancelled_at=datetime(2027, 6, 1, 9, 35, tzinfo=UTC),
        )


def test_invalid_operations_emit_no_success_event() -> None:
    voyage = _voyage()
    voyage.pull_events()

    with pytest.raises(InvalidVoyageLifecycleError):
        voyage.depart(
            departed_at=datetime(2027, 6, 1, 9, 0, tzinfo=UTC),
            actual_departure_location=_location("Location A"),
        )

    assert voyage.pull_events() == []


def test_completed_voyage_preserves_identity_reference_only() -> None:
    vessel_id = uuid4()
    voyage = _voyage(vessel_id=vessel_id)
    voyage.plan()
    voyage.depart(
        departed_at=datetime(2027, 6, 1, 9, 0, tzinfo=UTC),
        actual_departure_location=_location("Location A"),
    )
    voyage.arrive(
        arrived_at=datetime(2027, 6, 1, 19, 0, tzinfo=UTC),
        actual_arrival_location=_location("Location B"),
    )

    assert voyage.vessel_id == vessel_id
    assert not hasattr(voyage, "vessel")
