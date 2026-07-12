from __future__ import annotations

from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pathlib import Path
import weakref
from uuid import UUID

import mfm.database.models  # noqa: F401
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.voyages.location_snapshot import LocationSnapshot
from mfm.domain.voyages.voyage import Voyage
from mfm.domain.voyages.voyage_purpose import VoyagePurpose
from mfm.domain.voyages.voyage_purpose_code import VoyagePurposeCode
from mfm.domain.voyages.voyage_status import VoyageStatus
from mfm.infrastructure.persistence.sqlite.sqlite_voyage_repository import (
    SQLiteVoyageRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


def _new_session(db_path: Path) -> Session:
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return session


def _aware_utc(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _location(name: str, external_id: str) -> LocationSnapshot:
    return LocationSnapshot(
        name_snapshot=name,
        location_external_id=external_id,
        locality_snapshot=f"{name} locality",
        country_snapshot=f"{name} country",
    )


def _purpose(code: VoyagePurposeCode = VoyagePurposeCode.OPERATIONAL) -> VoyagePurpose:
    return VoyagePurpose(
        purpose_code=code,
        purpose_detail="Repository integration test",
    )


def _voyage(
    *,
    voyage_id: UUID,
    vessel_id: UUID,
    planned_departure_location: LocationSnapshot | None = None,
    planned_arrival_location: LocationSnapshot | None = None,
    planned_departure_at: datetime | None = None,
    planned_arrival_at: datetime | None = None,
    voyage_reference: str = "VOY-REPO",
) -> Voyage:
    return Voyage(
        id=voyage_id,
        vessel_id=vessel_id,
        planned_departure_location=planned_departure_location
        or _location("Port A", "PORT-A"),
        planned_arrival_location=planned_arrival_location or _location("Port B", "PORT-B"),
        planned_departure_at=planned_departure_at or _aware_utc(2028, 1, 1, 8, 0),
        planned_arrival_at=planned_arrival_at or _aware_utc(2028, 1, 1, 18, 0),
        voyage_reference=voyage_reference,
        voyage_purpose=_purpose(),
        notes="Voyage notes",
        document_reference="VOY-DOC-1",
    )


def test_voyage_repository_add_get_by_id_and_missing(tmp_path: Path) -> None:
    db_path = tmp_path / "voyage-repo-add-get.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteVoyageRepository(UnitOfWork(session))
        voyage = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B001"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000C001"),
            voyage_reference="VOY-REPO-001",
        )

        repository.add(voyage)
        session.commit()

        loaded = repository.get_by_id(voyage.id.value)
        assert loaded is not None
        assert loaded.id == voyage.id
        assert loaded.voyage_reference == "VOY-REPO-001"

        missing = repository.get_by_id(UUID("00000000-0000-0000-0000-00000000B999"))
        assert missing is None
    finally:
        session.close()


def test_voyage_repository_update_and_historical_truth_roundtrip_with_new_session(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "voyage-repo-update.sqlite"
    first_session = _new_session(db_path)
    try:
        repository = SQLiteVoyageRepository(UnitOfWork(first_session))
        voyage = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B002"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000C002"),
            planned_departure_location=_location("Port A", "PORT-A"),
            planned_arrival_location=_location("Port B", "PORT-B"),
            planned_departure_at=_aware_utc(2028, 2, 1, 7, 0),
            planned_arrival_at=_aware_utc(2028, 2, 1, 17, 0),
            voyage_reference="VOY-REPO-002",
        )
        repository.add(voyage)
        first_session.commit()

        voyage.plan()
        voyage.depart(
            departed_at=_aware_utc(2028, 2, 1, 8, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )
        voyage.arrive(
            arrived_at=_aware_utc(2028, 2, 1, 19, 30),
            actual_arrival_location=_location("Port C", "PORT-C"),
        )
        repository.update(voyage)
        first_session.commit()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        repository = SQLiteVoyageRepository(UnitOfWork(second_session))
        restored = repository.get_by_id(UUID("00000000-0000-0000-0000-00000000B002"))

        assert restored is not None
        assert restored.status is VoyageStatus.COMPLETED
        assert restored.planned_departure_location.name_snapshot == "Port A"
        assert restored.planned_arrival_location.name_snapshot == "Port B"
        assert restored.actual_departure_location is not None
        assert restored.actual_departure_location.name_snapshot == "Port A"
        assert restored.actual_arrival_location is not None
        assert restored.actual_arrival_location.name_snapshot == "Port C"
        assert restored.planned_arrival_location.name_snapshot != restored.actual_arrival_location.name_snapshot
    finally:
        second_session.close()


def test_voyage_repository_exists_list_get_by_vessel_and_isolation(tmp_path: Path) -> None:
    db_path = tmp_path / "voyage-repo-list.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteVoyageRepository(UnitOfWork(session))
        vessel_a = UUID("00000000-0000-0000-0000-00000000C101")
        vessel_b = UUID("00000000-0000-0000-0000-00000000C102")

        first = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B101"),
            vessel_id=vessel_a,
            planned_departure_at=_aware_utc(2028, 3, 1, 8, 0),
            planned_arrival_at=_aware_utc(2028, 3, 1, 18, 0),
            voyage_reference="VOY-LIST-1",
        )
        second = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B102"),
            vessel_id=vessel_a,
            planned_departure_at=_aware_utc(2028, 3, 2, 8, 0),
            planned_arrival_at=_aware_utc(2028, 3, 2, 18, 0),
            voyage_reference="VOY-LIST-2",
        )
        third = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B103"),
            vessel_id=vessel_b,
            planned_departure_at=_aware_utc(2028, 3, 3, 8, 0),
            planned_arrival_at=_aware_utc(2028, 3, 3, 18, 0),
            voyage_reference="VOY-LIST-3",
        )

        for voyage in (first, second, third):
            repository.add(voyage)
        session.commit()

        assert repository.exists(first.id.value) is True
        assert repository.exists(UUID("00000000-0000-0000-0000-00000000B199")) is False

        listed = repository.list()
        assert [item.id for item in listed] == [first.id, second.id, third.id]

        by_vessel = repository.get_by_vessel(vessel_a)
        assert [item.id for item in by_vessel] == [first.id, second.id]
        assert all(item.vessel_id == vessel_a for item in by_vessel)
    finally:
        session.close()


def test_voyage_repository_roundtrip_for_underway_completed_and_cancelled_states(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "voyage-repo-states.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteVoyageRepository(UnitOfWork(session))
        vessel_id = UUID("00000000-0000-0000-0000-00000000C201")

        underway = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B201"),
            vessel_id=vessel_id,
            voyage_reference="VOY-UNDERWAY",
        )
        underway.plan()
        underway.depart(
            departed_at=_aware_utc(2028, 4, 1, 9, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )

        completed = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B202"),
            vessel_id=vessel_id,
            voyage_reference="VOY-COMPLETED",
        )
        completed.plan()
        completed.depart(
            departed_at=_aware_utc(2028, 4, 2, 9, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )
        completed.arrive(
            arrived_at=_aware_utc(2028, 4, 2, 20, 0),
            actual_arrival_location=_location("Port C", "PORT-C"),
        )

        cancelled = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B203"),
            vessel_id=vessel_id,
            voyage_reference="VOY-CANCELLED",
        )
        cancelled.plan()
        cancelled.cancel(
            cancellation_reason="Weather closure",
            cancelled_at=_aware_utc(2028, 4, 3, 6, 30),
            cancelled_by_reference="voyage-planner",
        )

        for voyage in (underway, completed, cancelled):
            repository.add(voyage)
        session.commit()

        loaded_underway = repository.get_by_id(underway.id.value)
        loaded_completed = repository.get_by_id(completed.id.value)
        loaded_cancelled = repository.get_by_id(cancelled.id.value)

        assert loaded_underway is not None
        assert loaded_underway.status is VoyageStatus.UNDERWAY

        assert loaded_completed is not None
        assert loaded_completed.status is VoyageStatus.COMPLETED

        assert loaded_cancelled is not None
        assert loaded_cancelled.status is VoyageStatus.CANCELLED
        assert loaded_cancelled.cancellation_reason == "Weather closure"
    finally:
        session.close()


def test_voyage_repository_load_does_not_emit_false_restoration_events(tmp_path: Path) -> None:
    db_path = tmp_path / "voyage-repo-events.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteVoyageRepository(UnitOfWork(session))
        voyage = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B301"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000C301"),
        )
        repository.add(voyage)
        session.commit()

        loaded = repository.get_by_id(voyage.id.value)
        assert loaded is not None
        assert loaded.pull_events() == []
    finally:
        session.close()


def test_voyage_repository_defers_transaction_commit_to_unit_of_work(tmp_path: Path) -> None:
    db_path = tmp_path / "voyage-repo-rollback.sqlite"
    first_session = _new_session(db_path)
    try:
        uow = UnitOfWork(first_session)
        repository = SQLiteVoyageRepository(uow)
        voyage = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B401"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000C401"),
        )

        repository.add(voyage)
        # Repository must not commit; rollback removes the flushed insert.
        uow.rollback()
    finally:
        first_session.close()

    second_session = _new_session(db_path)
    try:
        repository = SQLiteVoyageRepository(UnitOfWork(second_session))
        assert repository.get_by_id(UUID("00000000-0000-0000-0000-00000000B401")) is None
    finally:
        second_session.close()


def test_voyage_repository_roundtrip_preserves_timezone_semantics(tmp_path: Path) -> None:
    db_path = tmp_path / "voyage-repo-timezone.sqlite"
    session = _new_session(db_path)
    try:
        repository = SQLiteVoyageRepository(UnitOfWork(session))
        plus_two = timezone(timedelta(hours=2))

        voyage = _voyage(
            voyage_id=UUID("00000000-0000-0000-0000-00000000B501"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000C501"),
            planned_departure_at=datetime(2028, 5, 1, 10, 0, tzinfo=plus_two),
            planned_arrival_at=datetime(2028, 5, 1, 14, 0, tzinfo=plus_two),
        )
        repository.add(voyage)
        session.commit()

        loaded = repository.get_by_id(voyage.id.value)
        assert loaded is not None
        assert loaded.planned_departure_at == datetime(2028, 5, 1, 8, 0, tzinfo=UTC)
        assert loaded.planned_arrival_at == datetime(2028, 5, 1, 12, 0, tzinfo=UTC)
    finally:
        session.close()
