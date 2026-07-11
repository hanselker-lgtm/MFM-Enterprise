from __future__ import annotations

import ast
from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.features.voyages.arrive_voyage_feature import ArriveVoyageFeature
from mfm.application.features.voyages.arrive_voyage_feature import ArriveVoyageRequest
from mfm.application.features.voyages.cancel_voyage_feature import CancelVoyageFeature
from mfm.application.features.voyages.cancel_voyage_feature import CancelVoyageRequest
from mfm.application.features.voyages.create_voyage_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.voyages.create_voyage_feature import CreateVoyageFeature
from mfm.application.features.voyages.create_voyage_feature import CreateVoyageRequest
from mfm.application.features.voyages.create_voyage_feature import VoyageLocationInput
from mfm.application.features.voyages.depart_voyage_feature import DepartVoyageFeature
from mfm.application.features.voyages.depart_voyage_feature import DepartVoyageRequest
from mfm.application.features.voyages.get_voyage_feature import GetVoyageFeature
from mfm.application.features.voyages.get_voyage_feature import GetVoyageRequest
from mfm.application.features.voyages.list_vessel_voyages_feature import (
    ListVesselVoyagesFeature,
)
from mfm.application.features.voyages.list_vessel_voyages_feature import (
    ListVesselVoyagesRequest,
)
from mfm.application.features.voyages.plan_voyage_feature import PlanVoyageFeature
from mfm.application.features.voyages.plan_voyage_feature import PlanVoyageRequest
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.voyages.arrive_voyage import ArriveVoyageUseCase
from mfm.application.voyages.cancel_voyage import CancelVoyageUseCase
from mfm.application.voyages.create_voyage import CreateVoyageUseCase
from mfm.application.voyages.depart_voyage import DepartVoyageUseCase
from mfm.application.voyages.get_voyage import GetVoyageUseCase
from mfm.application.voyages.list_vessel_voyages import ListVesselVoyagesUseCase
from mfm.application.voyages.plan_voyage import PlanVoyageUseCase
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.database.models.voyage_model import VoyageModel  # noqa: F401
from mfm.infrastructure.persistence.sqlite.sqlite_voyage_repository import (
    SQLiteVoyageRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteVoyageApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.voyage_repository = SQLiteVoyageRepository(self._persistence_uow)

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

    def _commit_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.commit()

    def _rollback_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        return None


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "voyage_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)

    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)
    try:
        yield factory
    finally:
        engine.dispose()


def _aware_utc(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute, tzinfo=UTC)


def _location(name: str, external_id: str) -> VoyageLocationInput:
    return VoyageLocationInput(
        name_snapshot=name,
        location_external_id=external_id,
        locality_snapshot=f"{name} locality",
        country_snapshot=f"{name} country",
    )


def _create_request(
    *,
    voyage_id: UUID,
    vessel_id: UUID,
    planned_departure_at: datetime,
    planned_arrival_at: datetime,
    voyage_reference: str,
) -> CreateVoyageRequest:
    return CreateVoyageRequest(
        voyage_id=voyage_id,
        vessel_id=vessel_id,
        planned_departure_location=_location("PORT-A", "PORT-A"),
        planned_arrival_location=_location("PORT-B", "PORT-B"),
        planned_departure_at=planned_departure_at,
        planned_arrival_at=planned_arrival_at,
        voyage_reference=voyage_reference,
        purpose_code="DEMONSTRATION",
        purpose_detail="E2E proof",
        notes="Voyage E2E",
        document_reference="VOY-E2E-DOC",
    )


def _build_feature_stack(session: Session) -> dict[str, object]:
    uow = SQLiteVoyageApplicationUnitOfWork(session)

    return {
        "create": CreateVoyageFeature(service=CreateVoyageUseCase(unit_of_work=uow)),
        "plan": PlanVoyageFeature(service=PlanVoyageUseCase(unit_of_work=uow)),
        "depart": DepartVoyageFeature(service=DepartVoyageUseCase(unit_of_work=uow)),
        "arrive": ArriveVoyageFeature(service=ArriveVoyageUseCase(unit_of_work=uow)),
        "cancel": CancelVoyageFeature(service=CancelVoyageUseCase(unit_of_work=uow)),
        "get": GetVoyageFeature(service=GetVoyageUseCase(unit_of_work=uow)),
        "list": ListVesselVoyagesFeature(
            service=ListVesselVoyagesUseCase(unit_of_work=uow)
        ),
    }


def test_e2e_workflow_1_complete_voyage_and_historical_truth_with_new_session(
    sqlite_session_factory,
) -> None:
    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)
        create = stack["create"]
        plan = stack["plan"]
        depart = stack["depart"]
        arrive = stack["arrive"]
        get = stack["get"]
        assert isinstance(create, CreateVoyageFeature)
        assert isinstance(plan, PlanVoyageFeature)
        assert isinstance(depart, DepartVoyageFeature)
        assert isinstance(arrive, ArriveVoyageFeature)
        assert isinstance(get, GetVoyageFeature)

        voyage_id = UUID("00000000-0000-0000-0000-00000000F001")
        vessel_id = UUID("00000000-0000-0000-0000-00000000A001")
        p1 = _aware_utc(2030, 1, 1, 8, 0)
        p2 = _aware_utc(2030, 1, 1, 18, 0)
        a1 = _aware_utc(2030, 1, 1, 9, 0)
        a2 = _aware_utc(2030, 1, 1, 20, 0)

        created = create.execute(
            _create_request(
                voyage_id=voyage_id,
                vessel_id=vessel_id,
                planned_departure_at=p1,
                planned_arrival_at=p2,
                voyage_reference="VOY-E2E-001",
            )
        )
        assert created.voyage.status == "DRAFT"

        planned = plan.execute(PlanVoyageRequest(voyage_id=voyage_id))
        assert planned.voyage.status == "PLANNED"

        departed = depart.execute(
            DepartVoyageRequest(
                voyage_id=voyage_id,
                departed_at=a1,
                actual_departure_location=_location("PORT-A", "PORT-A"),
            )
        )
        assert departed.voyage.status == "UNDERWAY"

        arrived = arrive.execute(
            ArriveVoyageRequest(
                voyage_id=voyage_id,
                arrived_at=a2,
                actual_arrival_location=_location("PORT-C", "PORT-C"),
            )
        )
        assert arrived.voyage.status == "COMPLETED"

        loaded = get.execute(GetVoyageRequest(voyage_id=voyage_id))
        assert loaded.voyage.planned_departure_location.name_snapshot == "PORT-A"
        assert loaded.voyage.planned_arrival_location.name_snapshot == "PORT-B"
        assert loaded.voyage.planned_departure_at == p1
        assert loaded.voyage.planned_arrival_at == p2
        assert loaded.voyage.actual_departure_location is not None
        assert loaded.voyage.actual_departure_location.name_snapshot == "PORT-A"
        assert loaded.voyage.actual_arrival_location is not None
        assert loaded.voyage.actual_arrival_location.name_snapshot == "PORT-C"
        assert loaded.voyage.departed_at == a1
        assert loaded.voyage.arrived_at == a2
    finally:
        write_session.close()

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)
        get = stack["get"]
        assert isinstance(get, GetVoyageFeature)

        loaded = get.execute(
            GetVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000F001"))
        )

        assert loaded.voyage.status == "COMPLETED"
        assert loaded.voyage.planned_departure_location.name_snapshot == "PORT-A"
        assert loaded.voyage.planned_arrival_location.name_snapshot == "PORT-B"
        assert loaded.voyage.actual_departure_location is not None
        assert loaded.voyage.actual_departure_location.name_snapshot == "PORT-A"
        assert loaded.voyage.actual_arrival_location is not None
        assert loaded.voyage.actual_arrival_location.name_snapshot == "PORT-C"
    finally:
        read_session.close()


def test_e2e_workflow_2_underway_voyage_new_session_proof(sqlite_session_factory) -> None:
    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)
        create = stack["create"]
        plan = stack["plan"]
        depart = stack["depart"]
        assert isinstance(create, CreateVoyageFeature)
        assert isinstance(plan, PlanVoyageFeature)
        assert isinstance(depart, DepartVoyageFeature)

        voyage_id = UUID("00000000-0000-0000-0000-00000000F002")
        create.execute(
            _create_request(
                voyage_id=voyage_id,
                vessel_id=UUID("00000000-0000-0000-0000-00000000A002"),
                planned_departure_at=_aware_utc(2030, 2, 1, 8, 0),
                planned_arrival_at=_aware_utc(2030, 2, 1, 18, 0),
                voyage_reference="VOY-E2E-002",
            )
        )
        plan.execute(PlanVoyageRequest(voyage_id=voyage_id))
        depart.execute(
            DepartVoyageRequest(
                voyage_id=voyage_id,
                departed_at=_aware_utc(2030, 2, 1, 9, 0),
                actual_departure_location=_location("PORT-A", "PORT-A"),
            )
        )
    finally:
        write_session.close()

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)
        get = stack["get"]
        assert isinstance(get, GetVoyageFeature)

        loaded = get.execute(
            GetVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000F002"))
        )

        assert loaded.voyage.status == "UNDERWAY"
        assert loaded.voyage.planned_departure_location.name_snapshot == "PORT-A"
        assert loaded.voyage.planned_arrival_location.name_snapshot == "PORT-B"
        assert loaded.voyage.actual_departure_location is not None
        assert loaded.voyage.actual_departure_location.name_snapshot == "PORT-A"
        assert loaded.voyage.actual_arrival_location is None
        assert loaded.voyage.arrived_at is None
    finally:
        read_session.close()


def test_e2e_workflow_3_cancelled_voyage_new_session_proof(sqlite_session_factory) -> None:
    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)
        create = stack["create"]
        plan = stack["plan"]
        cancel = stack["cancel"]
        assert isinstance(create, CreateVoyageFeature)
        assert isinstance(plan, PlanVoyageFeature)
        assert isinstance(cancel, CancelVoyageFeature)

        voyage_id = UUID("00000000-0000-0000-0000-00000000F003")
        create.execute(
            _create_request(
                voyage_id=voyage_id,
                vessel_id=UUID("00000000-0000-0000-0000-00000000A003"),
                planned_departure_at=_aware_utc(2030, 3, 1, 8, 0),
                planned_arrival_at=_aware_utc(2030, 3, 1, 18, 0),
                voyage_reference="VOY-E2E-003",
            )
        )
        plan.execute(PlanVoyageRequest(voyage_id=voyage_id))
        cancel.execute(
            CancelVoyageRequest(
                voyage_id=voyage_id,
                cancellation_reason="Weather closure",
                cancelled_at=_aware_utc(2030, 3, 1, 7, 30),
                cancelled_by_reference="scheduler",
            )
        )
    finally:
        write_session.close()

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)
        get = stack["get"]
        assert isinstance(get, GetVoyageFeature)

        loaded = get.execute(
            GetVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000F003"))
        )

        assert loaded.voyage.status == "CANCELLED"
        assert loaded.voyage.planned_departure_location.name_snapshot == "PORT-A"
        assert loaded.voyage.planned_arrival_location.name_snapshot == "PORT-B"
        assert loaded.voyage.cancellation_reason == "Weather closure"
        assert loaded.voyage.actual_departure_location is None
        assert loaded.voyage.actual_arrival_location is None
        assert loaded.voyage.departed_at is None
        assert loaded.voyage.arrived_at is None
    finally:
        read_session.close()


def test_e2e_workflow_4_multi_vessel_isolation(sqlite_session_factory) -> None:
    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)
        create = stack["create"]
        list_feature = stack["list"]
        assert isinstance(create, CreateVoyageFeature)
        assert isinstance(list_feature, ListVesselVoyagesFeature)

        vessel_a = UUID("00000000-0000-0000-0000-00000000A010")
        vessel_b = UUID("00000000-0000-0000-0000-00000000A011")

        a1 = UUID("00000000-0000-0000-0000-00000000F101")
        a2 = UUID("00000000-0000-0000-0000-00000000F102")
        b1 = UUID("00000000-0000-0000-0000-00000000F103")

        create.execute(
            _create_request(
                voyage_id=a1,
                vessel_id=vessel_a,
                planned_departure_at=_aware_utc(2030, 4, 1, 8, 0),
                planned_arrival_at=_aware_utc(2030, 4, 1, 18, 0),
                voyage_reference="VOY-A1",
            )
        )
        create.execute(
            _create_request(
                voyage_id=a2,
                vessel_id=vessel_a,
                planned_departure_at=_aware_utc(2030, 4, 2, 8, 0),
                planned_arrival_at=_aware_utc(2030, 4, 2, 18, 0),
                voyage_reference="VOY-A2",
            )
        )
        create.execute(
            _create_request(
                voyage_id=b1,
                vessel_id=vessel_b,
                planned_departure_at=_aware_utc(2030, 4, 3, 8, 0),
                planned_arrival_at=_aware_utc(2030, 4, 3, 18, 0),
                voyage_reference="VOY-B1",
            )
        )

        listed_a = list_feature.execute(ListVesselVoyagesRequest(vessel_id=vessel_a))
        ids_a = [item.voyage_id for item in listed_a.voyages]
        assert ids_a == [a1, a2]
        refs_a = [item.voyage_reference for item in listed_a.voyages]
        assert refs_a == ["VOY-A1", "VOY-A2"]
    finally:
        write_session.close()

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)
        list_feature = stack["list"]
        assert isinstance(list_feature, ListVesselVoyagesFeature)

        vessel_a = UUID("00000000-0000-0000-0000-00000000A010")
        vessel_b = UUID("00000000-0000-0000-0000-00000000A011")

        listed_a = list_feature.execute(ListVesselVoyagesRequest(vessel_id=vessel_a))
        listed_b = list_feature.execute(ListVesselVoyagesRequest(vessel_id=vessel_b))

        assert [item.voyage_id for item in listed_a.voyages] == [
            UUID("00000000-0000-0000-0000-00000000F101"),
            UUID("00000000-0000-0000-0000-00000000F102"),
        ]
        assert [item.voyage_id for item in listed_b.voyages] == [
            UUID("00000000-0000-0000-0000-00000000F103")
        ]
    finally:
        read_session.close()


def test_e2e_workflow_5_invalid_lifecycle_rollback(sqlite_session_factory) -> None:
    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)
        create = stack["create"]
        depart = stack["depart"]
        assert isinstance(create, CreateVoyageFeature)
        assert isinstance(depart, DepartVoyageFeature)

        voyage_id = UUID("00000000-0000-0000-0000-00000000F005")
        create.execute(
            _create_request(
                voyage_id=voyage_id,
                vessel_id=UUID("00000000-0000-0000-0000-00000000A005"),
                planned_departure_at=_aware_utc(2030, 5, 1, 8, 0),
                planned_arrival_at=_aware_utc(2030, 5, 1, 18, 0),
                voyage_reference="VOY-E2E-005",
            )
        )

        with pytest.raises(BusinessRuleViolation):
            depart.execute(
                DepartVoyageRequest(
                    voyage_id=voyage_id,
                    departed_at=_aware_utc(2030, 5, 1, 9, 0),
                    actual_departure_location=_location("PORT-A", "PORT-A"),
                )
            )
    finally:
        write_session.close()

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)
        get = stack["get"]
        assert isinstance(get, GetVoyageFeature)

        loaded = get.execute(GetVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000F005")))
        assert loaded.voyage.status == "DRAFT"
        assert loaded.voyage.actual_departure_location is None
        assert loaded.voyage.actual_arrival_location is None
    finally:
        read_session.close()


def test_e2e_workflow_6_arrival_chronology_failure_rollback(sqlite_session_factory) -> None:
    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)
        create = stack["create"]
        plan = stack["plan"]
        depart = stack["depart"]
        arrive = stack["arrive"]
        assert isinstance(create, CreateVoyageFeature)
        assert isinstance(plan, PlanVoyageFeature)
        assert isinstance(depart, DepartVoyageFeature)
        assert isinstance(arrive, ArriveVoyageFeature)

        voyage_id = UUID("00000000-0000-0000-0000-00000000F006")
        create.execute(
            _create_request(
                voyage_id=voyage_id,
                vessel_id=UUID("00000000-0000-0000-0000-00000000A006"),
                planned_departure_at=_aware_utc(2030, 6, 1, 8, 0),
                planned_arrival_at=_aware_utc(2030, 6, 1, 18, 0),
                voyage_reference="VOY-E2E-006",
            )
        )
        plan.execute(PlanVoyageRequest(voyage_id=voyage_id))
        depart.execute(
            DepartVoyageRequest(
                voyage_id=voyage_id,
                departed_at=_aware_utc(2030, 6, 1, 9, 0),
                actual_departure_location=_location("PORT-A", "PORT-A"),
            )
        )

        with pytest.raises(BusinessRuleViolation):
            arrive.execute(
                ArriveVoyageRequest(
                    voyage_id=voyage_id,
                    arrived_at=_aware_utc(2030, 6, 1, 8, 30),
                    actual_arrival_location=_location("PORT-C", "PORT-C"),
                )
            )
    finally:
        write_session.close()

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)
        get = stack["get"]
        assert isinstance(get, GetVoyageFeature)

        loaded = get.execute(GetVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000F006")))

        assert loaded.voyage.status == "UNDERWAY"
        assert loaded.voyage.actual_departure_location is not None
        assert loaded.voyage.actual_departure_location.name_snapshot == "PORT-A"
        assert loaded.voyage.actual_arrival_location is None
        assert loaded.voyage.arrived_at is None
        assert loaded.voyage.planned_arrival_location.name_snapshot == "PORT-B"
    finally:
        read_session.close()


def test_e2e_workflow_7_explicit_time_timezone_roundtrip(sqlite_session_factory) -> None:
    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)
        create = stack["create"]
        plan = stack["plan"]
        depart = stack["depart"]
        arrive = stack["arrive"]
        assert isinstance(create, CreateVoyageFeature)
        assert isinstance(plan, PlanVoyageFeature)
        assert isinstance(depart, DepartVoyageFeature)
        assert isinstance(arrive, ArriveVoyageFeature)

        plus_two = timezone(timedelta(hours=2))
        minus_three = timezone(timedelta(hours=-3))

        voyage_id = UUID("00000000-0000-0000-0000-00000000F007")

        p1 = datetime(2030, 7, 1, 10, 0, tzinfo=plus_two)
        p2 = datetime(2030, 7, 1, 22, 0, tzinfo=plus_two)
        a1 = datetime(2030, 7, 1, 7, 30, tzinfo=UTC)
        a2 = datetime(2030, 7, 1, 17, 0, tzinfo=minus_three)

        create.execute(
            _create_request(
                voyage_id=voyage_id,
                vessel_id=UUID("00000000-0000-0000-0000-00000000A007"),
                planned_departure_at=p1,
                planned_arrival_at=p2,
                voyage_reference="VOY-E2E-007",
            )
        )
        plan.execute(PlanVoyageRequest(voyage_id=voyage_id))
        depart.execute(
            DepartVoyageRequest(
                voyage_id=voyage_id,
                departed_at=a1,
                actual_departure_location=_location("PORT-A", "PORT-A"),
            )
        )
        arrive.execute(
            ArriveVoyageRequest(
                voyage_id=voyage_id,
                arrived_at=a2,
                actual_arrival_location=_location("PORT-C", "PORT-C"),
            )
        )
    finally:
        write_session.close()

    read_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(read_session)
        get = stack["get"]
        assert isinstance(get, GetVoyageFeature)

        loaded = get.execute(
            GetVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000F007"))
        )

        assert loaded.voyage.planned_departure_at == datetime(2030, 7, 1, 8, 0, tzinfo=UTC)
        assert loaded.voyage.planned_arrival_at == datetime(2030, 7, 1, 20, 0, tzinfo=UTC)
        assert loaded.voyage.departed_at == datetime(2030, 7, 1, 7, 30, tzinfo=UTC)
        assert loaded.voyage.arrived_at == datetime(2030, 7, 1, 20, 0, tzinfo=UTC)
    finally:
        read_session.close()


def test_hidden_clock_search_in_voyage_production_layers() -> None:
    project_root = Path(__file__).resolve().parents[4]
    roots = (
        project_root / "src" / "mfm" / "domain" / "voyages",
        project_root / "src" / "mfm" / "application" / "voyages",
        project_root / "src" / "mfm" / "application" / "features" / "voyages",
    )
    patterns = ("date.today(", "datetime.now(", "datetime.today(", "time.time(")

    matches: list[str] = []
    for root in roots:
        for file_path in root.rglob("*.py"):
            source = file_path.read_text(encoding="utf-8")
            _ = ast.parse(source, filename=str(file_path))
            for pattern in patterns:
                if pattern in source:
                    matches.append(f"{file_path.relative_to(project_root)} contains {pattern}")

    assert not matches, "\n".join(matches)
