from __future__ import annotations

from datetime import UTC
from datetime import datetime
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.mappers.voyage_mapper import VoyageMapper
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.database.models.voyage_model import VoyageModel
from mfm.domain.voyages.events import VoyageArrived
from mfm.domain.voyages.events import VoyageCancelled
from mfm.domain.voyages.events import VoyageCreated
from mfm.domain.voyages.events import VoyageDeparted
from mfm.domain.voyages.events import VoyagePlanned
from mfm.domain.voyages.exceptions import InvalidVoyageChronologyError
from mfm.domain.voyages.exceptions import InvalidVoyageLifecycleError
from mfm.domain.voyages.exceptions import InvalidVoyagePurposeError
from mfm.domain.voyages.location_snapshot import LocationSnapshot
from mfm.domain.voyages.voyage import Voyage
from mfm.domain.voyages.voyage_purpose import VoyagePurpose
from mfm.domain.voyages.voyage_purpose_code import VoyagePurposeCode
from mfm.domain.voyages.voyage_status import VoyageStatus


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    return Session(engine)
def _aware(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


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
    return VoyagePurpose(purpose_code=code, purpose_detail="Harbor presentation")


def _voyage(
    *,
    voyage_id: UUID | None = None,
    vessel_id: UUID = UUID("00000000-0000-0000-0000-00000000A101"),
    planned_departure_location: LocationSnapshot | None = None,
    planned_arrival_location: LocationSnapshot | None = None,
    planned_departure_at: datetime | None = None,
    planned_arrival_at: datetime | None = None,
    voyage_reference: str | None = "VOY-100",
    voyage_purpose: VoyagePurpose | None = None,
    notes: str | None = "Historic trial passage",
    document_reference: str | None = "VOY-DOC-1",
) -> Voyage:
    return Voyage(
        id=UUID("00000000-0000-0000-0000-00000000A001") if voyage_id is None else voyage_id,
        vessel_id=vessel_id,
        planned_departure_location=planned_departure_location
        or _location(
            "Port A",
            external_id="PORT-A",
            locality="Harbor A",
            country="Country A",
        ),
        planned_arrival_location=planned_arrival_location
        or _location(
            "Port B",
            external_id="PORT-B",
            locality="Harbor B",
            country="Country B",
        ),
        planned_departure_at=planned_departure_at or _aware(2027, 6, 1, 8, 15),
        planned_arrival_at=planned_arrival_at or _aware(2027, 6, 1, 18, 45),
        voyage_reference=voyage_reference,
        voyage_purpose=voyage_purpose or _purpose(),
        notes=notes,
        document_reference=document_reference,
    )


def _persist_and_reload(session: Session, voyage: Voyage) -> Voyage:
    orm = VoyageMapper.to_orm_voyage(voyage)
    session.add(orm)
    session.commit()
    session.expunge_all()

    loaded = session.get(VoyageModel, voyage.id.value)
    assert loaded is not None
    return VoyageMapper.to_domain_voyage(loaded)


def test_voyage_mapper_creation_roundtrip_persists_initial_state(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-roundtrip-create")
    try:
        voyage = _voyage()

        restored = _persist_and_reload(session, voyage)

        assert restored.id == voyage.id
        assert restored.vessel_id == voyage.vessel_id
        assert restored.status is VoyageStatus.DRAFT
        assert restored.voyage_reference == "VOY-100"
        assert restored.voyage_purpose == voyage.voyage_purpose
        assert restored.notes == "Historic trial passage"
        assert restored.document_reference == "VOY-DOC-1"
    finally:
        session.close()


def test_vessel_reference_roundtrip_preserves_identity_only(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-vessel-ref")
    try:
        voyage = _voyage(vessel_id=UUID("00000000-0000-0000-0000-00000000A202"))

        restored = _persist_and_reload(session, voyage)

        assert restored.vessel_id == UUID("00000000-0000-0000-0000-00000000A202")
        assert not hasattr(restored, "vessel")
    finally:
        session.close()


def test_location_roundtrip_preserves_all_snapshot_fields_independently(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-location-roundtrip")
    try:
        voyage = _voyage(
            planned_departure_location=_location(
                "Port Alpha",
                external_id="ALPHA",
                locality="Alpha Town",
                country="Alpha Country",
            ),
            planned_arrival_location=_location(
                "Port Beta",
                external_id="BETA",
                locality="Beta Town",
                country="Beta Country",
            ),
        )
        voyage.plan()
        voyage.depart(
            departed_at=_aware(2027, 6, 1, 9, 0),
            actual_departure_location=_location(
                "Port Alpha Actual",
                external_id="ALPHA-ACT",
                locality="Alpha Actual Town",
                country="Alpha Actual Country",
            ),
        )
        voyage.arrive(
            arrived_at=_aware(2027, 6, 1, 20, 0),
            actual_arrival_location=_location(
                "Port Gamma",
                external_id="GAMMA",
                locality="Gamma Town",
                country="Gamma Country",
            ),
        )

        restored = _persist_and_reload(session, voyage)

        assert restored.planned_departure_location.name_snapshot == "Port Alpha"
        assert restored.planned_departure_location.location_external_id == "ALPHA"
        assert restored.planned_departure_location.locality_snapshot == "Alpha Town"
        assert restored.planned_departure_location.country_snapshot == "Alpha Country"

        assert restored.planned_arrival_location.name_snapshot == "Port Beta"
        assert restored.planned_arrival_location.location_external_id == "BETA"
        assert restored.actual_departure_location is not None
        assert restored.actual_departure_location.name_snapshot == "Port Alpha Actual"
        assert restored.actual_departure_location.location_external_id == "ALPHA-ACT"
        assert restored.actual_arrival_location is not None
        assert restored.actual_arrival_location.name_snapshot == "Port Gamma"
        assert restored.actual_arrival_location.location_external_id == "GAMMA"
    finally:
        session.close()


def test_planned_context_roundtrip_preserves_plan_independently(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-plan-roundtrip")
    try:
        voyage = _voyage(
            planned_departure_location=_location("Location A", external_id="PORT-A"),
            planned_arrival_location=_location("Location B", external_id="PORT-B"),
            planned_departure_at=_aware(2027, 7, 1, 8, 0),
            planned_arrival_at=_aware(2027, 7, 1, 18, 0),
        )
        voyage.plan()

        restored = _persist_and_reload(session, voyage)

        assert restored.planned_departure_location.name_snapshot == "Location A"
        assert restored.planned_arrival_location.name_snapshot == "Location B"
        assert restored.planned_departure_at == _aware(2027, 7, 1, 8, 0)
        assert restored.planned_arrival_at == _aware(2027, 7, 1, 18, 0)
        assert restored.status is VoyageStatus.PLANNED
    finally:
        session.close()


def test_underway_voyage_roundtrip_preserves_planned_and_actual_departure(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-underway-roundtrip")
    try:
        voyage = _voyage()
        voyage.plan()
        voyage.depart(
            departed_at=_aware(2027, 8, 1, 9, 30),
            actual_departure_location=_location("Location A", external_id="PORT-A"),
        )

        restored = _persist_and_reload(session, voyage)

        assert restored.status is VoyageStatus.UNDERWAY
        assert restored.planned_arrival_location.name_snapshot == "Port B"
        assert restored.actual_departure_location is not None
        assert restored.actual_departure_location.name_snapshot == "Location A"
        assert restored.departed_at == _aware(2027, 8, 1, 9, 30)
        assert restored.actual_arrival_location is None
        assert restored.arrived_at is None
    finally:
        session.close()


def test_completed_voyage_roundtrip_preserves_historical_truth(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-completed-roundtrip")
    try:
        voyage = _voyage(
            planned_departure_location=_location("Location A", external_id="PORT-A"),
            planned_arrival_location=_location("Location B", external_id="PORT-B"),
            planned_departure_at=_aware(2027, 9, 1, 8, 0),
            planned_arrival_at=_aware(2027, 9, 1, 18, 0),
        )
        voyage.plan()
        voyage.depart(
            departed_at=_aware(2027, 9, 1, 9, 0),
            actual_departure_location=_location("Location A", external_id="PORT-A"),
        )
        voyage.arrive(
            arrived_at=_aware(2027, 9, 1, 20, 30),
            actual_arrival_location=_location("Location C", external_id="PORT-C"),
        )

        restored = _persist_and_reload(session, voyage)

        assert restored.status is VoyageStatus.COMPLETED
        assert restored.planned_departure_location.name_snapshot == "Location A"
        assert restored.planned_arrival_location.name_snapshot == "Location B"
        assert restored.planned_departure_at == _aware(2027, 9, 1, 8, 0)
        assert restored.planned_arrival_at == _aware(2027, 9, 1, 18, 0)
        assert restored.actual_departure_location is not None
        assert restored.actual_departure_location.name_snapshot == "Location A"
        assert restored.actual_arrival_location is not None
        assert restored.actual_arrival_location.name_snapshot == "Location C"
        assert restored.departed_at == _aware(2027, 9, 1, 9, 0)
        assert restored.arrived_at == _aware(2027, 9, 1, 20, 30)
    finally:
        session.close()


def test_cancelled_voyage_roundtrip_preserves_cancellation_and_plan(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-cancelled-roundtrip")
    try:
        voyage = _voyage()
        voyage.plan()
        voyage.cancel(
            cancellation_reason="Weather window closed",
            cancelled_at=_aware(2027, 10, 1, 7, 45),
            cancelled_by_reference="scheduler-1",
        )

        restored = _persist_and_reload(session, voyage)

        assert restored.status is VoyageStatus.CANCELLED
        assert restored.planned_departure_location.name_snapshot == "Port A"
        assert restored.cancellation_reason == "Weather window closed"
        assert restored.cancelled_at == _aware(2027, 10, 1, 7, 45)
        assert restored.cancelled_by_reference == "scheduler-1"
        assert restored.actual_departure_location is None
        assert restored.actual_arrival_location is None
        assert restored.departed_at is None
        assert restored.arrived_at is None
    finally:
        session.close()


def test_lifecycle_state_roundtrip_for_supported_states(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-status-roundtrip")
    try:
        draft = _voyage(voyage_id=UUID("00000000-0000-0000-0000-00000000A301"))

        planned = _voyage(voyage_id=UUID("00000000-0000-0000-0000-00000000A302"))
        planned.plan()

        underway = _voyage(voyage_id=UUID("00000000-0000-0000-0000-00000000A303"))
        underway.plan()
        underway.depart(
            departed_at=_aware(2027, 11, 1, 9, 0),
            actual_departure_location=_location("Port A"),
        )

        completed = _voyage(voyage_id=UUID("00000000-0000-0000-0000-00000000A304"))
        completed.plan()
        completed.depart(
            departed_at=_aware(2027, 11, 2, 9, 0),
            actual_departure_location=_location("Port A"),
        )
        completed.arrive(
            arrived_at=_aware(2027, 11, 2, 19, 0),
            actual_arrival_location=_location("Port C"),
        )

        cancelled = _voyage(voyage_id=UUID("00000000-0000-0000-0000-00000000A305"))
        cancelled.plan()
        cancelled.cancel(
            cancellation_reason="Port closure",
            cancelled_at=_aware(2027, 11, 3, 7, 0),
        )

        for voyage, expected_status in (
            (draft, VoyageStatus.DRAFT),
            (planned, VoyageStatus.PLANNED),
            (underway, VoyageStatus.UNDERWAY),
            (completed, VoyageStatus.COMPLETED),
            (cancelled, VoyageStatus.CANCELLED),
        ):
            restored = _persist_and_reload(session, voyage)
            assert restored.status is expected_status
    finally:
        session.close()


def test_voyage_purpose_roundtrip_preserved(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-purpose-roundtrip")
    try:
        voyage = _voyage(
            voyage_purpose=VoyagePurpose(
                purpose_code=VoyagePurposeCode.TRAINING,
                purpose_detail="Apprentice instruction",
            )
        )

        restored = _persist_and_reload(session, voyage)

        assert restored.voyage_purpose is not None
        assert restored.voyage_purpose.purpose_code is VoyagePurposeCode.TRAINING
        assert restored.voyage_purpose.purpose_detail == "Apprentice instruction"
    finally:
        session.close()


def test_timezone_roundtrip_preserves_utc_semantics(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-timezone-roundtrip")
    try:
        departure = datetime(2027, 12, 1, 10, 0, tzinfo=UTC)
        arrival = datetime(2027, 12, 1, 16, 0, tzinfo=UTC)
        voyage = _voyage(
            planned_departure_at=departure,
            planned_arrival_at=arrival,
        )
        voyage.plan()
        voyage.depart(
            departed_at=datetime(2027, 12, 1, 10, 30, tzinfo=UTC),
            actual_departure_location=_location("Port A"),
        )
        voyage.arrive(
            arrived_at=datetime(2027, 12, 1, 16, 15, tzinfo=UTC),
            actual_arrival_location=_location("Port B"),
        )

        restored = _persist_and_reload(session, voyage)

        assert restored.planned_departure_at == departure
        assert restored.planned_arrival_at == arrival
        assert restored.departed_at == datetime(2027, 12, 1, 10, 30, tzinfo=UTC)
        assert restored.arrived_at == datetime(2027, 12, 1, 16, 15, tzinfo=UTC)
        assert restored.planned_departure_at.tzinfo is UTC
        assert restored.departed_at is not None and restored.departed_at.tzinfo is UTC
    finally:
        session.close()


def test_historical_voyage_truth_roundtrip_keeps_planned_b_and_actual_c(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-historical-truth")
    try:
        voyage = _voyage(
            planned_departure_location=_location("PORT-A", external_id="A"),
            planned_arrival_location=_location("PORT-B", external_id="B"),
            planned_departure_at=_aware(2028, 1, 10, 8, 0),
            planned_arrival_at=_aware(2028, 1, 10, 18, 0),
        )
        voyage.plan()
        voyage.depart(
            departed_at=_aware(2028, 1, 10, 9, 0),
            actual_departure_location=_location("PORT-A", external_id="A"),
        )
        voyage.arrive(
            arrived_at=_aware(2028, 1, 10, 20, 0),
            actual_arrival_location=_location("PORT-C", external_id="C"),
        )

        restored = _persist_and_reload(session, voyage)

        assert restored.planned_arrival_location.name_snapshot == "PORT-B"
        assert restored.actual_arrival_location is not None
        assert restored.actual_arrival_location.name_snapshot == "PORT-C"
        assert restored.planned_departure_at == _aware(2028, 1, 10, 8, 0)
        assert restored.planned_arrival_at == _aware(2028, 1, 10, 18, 0)
        assert restored.departed_at == _aware(2028, 1, 10, 9, 0)
        assert restored.arrived_at == _aware(2028, 1, 10, 20, 0)
    finally:
        session.close()


def test_restoration_emits_no_false_domain_events_for_persisted_states(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "voyage-restoration-events")
    try:
        completed = _voyage(voyage_id=UUID("00000000-0000-0000-0000-00000000A401"))
        completed.plan()
        completed.depart(
            departed_at=_aware(2028, 2, 1, 9, 0),
            actual_departure_location=_location("Port A"),
        )
        completed.arrive(
            arrived_at=_aware(2028, 2, 1, 19, 0),
            actual_arrival_location=_location("Port C"),
        )

        cancelled = _voyage(voyage_id=UUID("00000000-0000-0000-0000-00000000A402"))
        cancelled.plan()
        cancelled.cancel(
            cancellation_reason="No berth available",
            cancelled_at=_aware(2028, 2, 2, 7, 0),
        )

        restored_completed = _persist_and_reload(session, completed)
        restored_cancelled = _persist_and_reload(session, cancelled)

        assert restored_completed.pull_events() == []
        assert restored_cancelled.pull_events() == []
    finally:
        session.close()


def test_invalid_persistence_state_unsupported_status_fails_clearly() -> None:
    orm = VoyageModel(
        id=UUID("00000000-0000-0000-0000-00000000A501"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000A502"),
        planned_departure_location_name_snapshot="Port A",
        planned_arrival_location_name_snapshot="Port B",
        planned_departure_at=_aware(2028, 3, 1, 8, 0),
        planned_arrival_at=_aware(2028, 3, 1, 18, 0),
        status="INVALID",  # type: ignore[arg-type]
    )

    with pytest.raises((ValueError, InvalidVoyageLifecycleError, InvalidVoyageChronologyError)):
        VoyageMapper.to_domain_voyage(orm)


def test_invalid_persistence_state_invalid_purpose_fails_clearly() -> None:
    orm = VoyageModel(
        id=UUID("00000000-0000-0000-0000-00000000A601"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000A602"),
        planned_departure_location_name_snapshot="Port A",
        planned_arrival_location_name_snapshot="Port B",
        planned_departure_at=_aware(2028, 4, 1, 8, 0),
        planned_arrival_at=_aware(2028, 4, 1, 18, 0),
        status=VoyageStatus.DRAFT,
        purpose_code="INVALID",  # type: ignore[arg-type]
    )

    with pytest.raises((ValueError, InvalidVoyagePurposeError)):
        VoyageMapper.to_domain_voyage(orm)


def test_invalid_persistence_state_incomplete_actual_arrival_fails_clearly() -> None:
    orm = VoyageModel(
        id=UUID("00000000-0000-0000-0000-00000000A701"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000A702"),
        planned_departure_location_name_snapshot="Port A",
        planned_arrival_location_name_snapshot="Port B",
        planned_departure_at=_aware(2028, 5, 1, 8, 0),
        planned_arrival_at=_aware(2028, 5, 1, 18, 0),
        status=VoyageStatus.COMPLETED,
        actual_departure_location_name_snapshot="Port A",
        departed_at=_aware(2028, 5, 1, 9, 0),
        arrived_at=_aware(2028, 5, 1, 19, 0),
    )

    with pytest.raises(InvalidVoyageLifecycleError):
        VoyageMapper.to_domain_voyage(orm)


def test_invalid_persistence_state_invalid_chronology_fails_clearly() -> None:
    orm = VoyageModel(
        id=UUID("00000000-0000-0000-0000-00000000A801"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000A802"),
        planned_departure_location_name_snapshot="Port A",
        planned_arrival_location_name_snapshot="Port B",
        planned_departure_at=_aware(2028, 6, 1, 20, 0),
        planned_arrival_at=_aware(2028, 6, 1, 18, 0),
        status=VoyageStatus.DRAFT,
    )

    with pytest.raises(InvalidVoyageChronologyError):
        VoyageMapper.to_domain_voyage(orm)