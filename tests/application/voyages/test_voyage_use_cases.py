from __future__ import annotations

from copy import deepcopy
from dataclasses import is_dataclass
from datetime import UTC
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from uuid import UUID

import pytest

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.application.voyages.arrive_voyage import ArriveVoyageRequest
from mfm.application.voyages.arrive_voyage import ArriveVoyageUseCase
from mfm.application.voyages.cancel_voyage import CancelVoyageRequest
from mfm.application.voyages.cancel_voyage import CancelVoyageUseCase
from mfm.application.voyages.create_voyage import BusinessRuleViolation
from mfm.application.voyages.create_voyage import CreateVoyageRequest
from mfm.application.voyages.create_voyage import CreateVoyageUseCase
from mfm.application.voyages.create_voyage import RepositoryException
from mfm.application.voyages.create_voyage import ValidationException
from mfm.application.voyages.create_voyage import VoyageLocationInput
from mfm.application.voyages.depart_voyage import DepartVoyageRequest
from mfm.application.voyages.depart_voyage import DepartVoyageUseCase
from mfm.application.voyages.get_voyage import GetVoyageRequest
from mfm.application.voyages.get_voyage import GetVoyageUseCase
from mfm.application.voyages.list_vessel_voyages import ListVesselVoyagesRequest
from mfm.application.voyages.list_vessel_voyages import ListVesselVoyagesUseCase
from mfm.application.voyages.plan_voyage import PlanVoyageRequest
from mfm.application.voyages.plan_voyage import PlanVoyageUseCase
from mfm.domain.voyages.location_snapshot import LocationSnapshot
from mfm.domain.voyages.voyage import Voyage
from mfm.domain.voyages.voyage_purpose import VoyagePurpose
from mfm.domain.voyages.voyage_purpose_code import VoyagePurposeCode
from mfm.repositories.voyage_repository import VoyageRepository


class InMemoryVoyageRepository(VoyageRepository):
    def __init__(
        self,
        *,
        fail_on_add: bool = False,
        fail_on_update: bool = False,
    ) -> None:
        self._items: dict[UUID, Voyage] = {}
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

        self.add_calls = 0
        self.get_by_id_calls = 0
        self.update_calls = 0
        self.get_by_vessel_calls = 0

    def snapshot(self) -> dict[UUID, Voyage]:
        return deepcopy(self._items)

    def restore(self, snapshot: dict[UUID, Voyage]) -> None:
        self._items = deepcopy(snapshot)

    def add(self, voyage: Voyage) -> None:
        self.add_calls += 1
        if self._fail_on_add:
            raise RuntimeError("voyage add failed")
        self._items[voyage.id.value] = deepcopy(voyage)

    def get_by_id(self, voyage_id: UUID) -> Voyage | None:
        self.get_by_id_calls += 1
        value = self._items.get(voyage_id)
        return deepcopy(value) if value is not None else None

    def update(self, voyage: Voyage) -> None:
        self.update_calls += 1
        if self._fail_on_update:
            raise RuntimeError("voyage update failed")
        if voyage.id.value not in self._items:
            raise ValueError(f"Voyage {voyage.id.value} does not exist")
        self._items[voyage.id.value] = deepcopy(voyage)

    def exists(self, voyage_id: UUID) -> bool:
        return voyage_id in self._items

    def list(self) -> list[Voyage]:
        return [deepcopy(item) for item in self._items.values()]

    def get_by_vessel(self, vessel_id: UUID) -> list[Voyage]:
        self.get_by_vessel_calls += 1
        values = [
            deepcopy(item)
            for item in self._items.values()
            if item.vessel_id == vessel_id
        ]
        values.sort(key=lambda item: (item.planned_departure_at, item.id.value))
        return values


class FakeVoyageUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_voyage_add: bool = False,
        fail_voyage_update: bool = False,
        fail_commit: bool = False,
    ) -> None:
        super().__init__()
        self._fail_commit = fail_commit
        self._repository = InMemoryVoyageRepository(
            fail_on_add=fail_voyage_add,
            fail_on_update=fail_voyage_update,
        )
        self._snapshot: dict[UUID, Voyage] = {}
        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self.voyage_repository = self._repository
        self._snapshot = self._repository.snapshot()

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

    def _commit_impl(self) -> None:
        self.commits += 1
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self._repository.restore(self._snapshot)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


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
    voyage_id: UUID | None = None,
    vessel_id: UUID = UUID("00000000-0000-0000-0000-00000000D001"),
    planned_departure_at: datetime | None = None,
    planned_arrival_at: datetime | None = None,
    planned_departure_location: VoyageLocationInput | None = None,
    planned_arrival_location: VoyageLocationInput | None = None,
    purpose_code: str | None = "OPERATIONAL",
    purpose_detail: str | None = "Application test voyage",
) -> CreateVoyageRequest:
    return CreateVoyageRequest(
        voyage_id=voyage_id,
        vessel_id=vessel_id,
        planned_departure_location=planned_departure_location or _location("Port A", "PORT-A"),
        planned_arrival_location=planned_arrival_location or _location("Port B", "PORT-B"),
        planned_departure_at=planned_departure_at or _aware_utc(2028, 1, 1, 8, 0),
        planned_arrival_at=planned_arrival_at or _aware_utc(2028, 1, 1, 18, 0),
        voyage_reference="VOY-APP-001",
        purpose_code=purpose_code,
        purpose_detail=purpose_detail,
        notes="Voyage notes",
        document_reference="VOY-DOC-APP",
    )


def _seed_voyage(
    uow: FakeVoyageUnitOfWork,
    *,
    voyage_id: UUID,
    vessel_id: UUID,
    planned_departure_at: datetime,
) -> Voyage:
    voyage = Voyage(
        id=voyage_id,
        vessel_id=vessel_id,
        planned_departure_location=LocationSnapshot(
            name_snapshot="Port A",
            location_external_id="PORT-A",
            locality_snapshot="Port A locality",
            country_snapshot="Port A country",
        ),
        planned_arrival_location=LocationSnapshot(
            name_snapshot="Port B",
            location_external_id="PORT-B",
            locality_snapshot="Port B locality",
            country_snapshot="Port B country",
        ),
        planned_departure_at=planned_departure_at,
        planned_arrival_at=planned_departure_at + timedelta(hours=8),
        voyage_reference=f"REF-{voyage_id}",
        voyage_purpose=VoyagePurpose(purpose_code=VoyagePurposeCode.OPERATIONAL),
        notes="Seed voyage",
        document_reference="SEED-DOC",
    )
    uow._repository._items[voyage.id.value] = deepcopy(voyage)
    return voyage


def test_create_voyage_happy_path_commit_and_response_mapping() -> None:
    uow = FakeVoyageUnitOfWork()
    response = CreateVoyageUseCase(unit_of_work=uow).execute(_create_request())

    assert uow.commits == 1
    assert uow.rollbacks == 0
    assert response.voyage.status == "DRAFT"
    assert response.voyage.planned_departure_location.name_snapshot == "Port A"
    assert response.voyage.planned_arrival_location.name_snapshot == "Port B"
    assert response.voyage.actual_departure_location is None
    assert response.voyage.actual_arrival_location is None
    assert response.voyage.voyage_purpose is not None
    assert response.voyage.voyage_purpose.purpose_code == "OPERATIONAL"


def test_create_voyage_invalid_input_mapping_raises_validation() -> None:
    uow = FakeVoyageUnitOfWork()

    with pytest.raises(ValidationException):
        CreateVoyageUseCase(unit_of_work=uow).execute(
            _create_request(purpose_code="NOT-A-CODE")
        )

    assert uow.commits == 0


def test_create_voyage_invalid_domain_chronology_maps_business_rule_violation() -> None:
    uow = FakeVoyageUnitOfWork()

    with pytest.raises(BusinessRuleViolation):
        CreateVoyageUseCase(unit_of_work=uow).execute(
            _create_request(
                planned_departure_at=_aware_utc(2028, 1, 1, 18, 0),
                planned_arrival_at=_aware_utc(2028, 1, 1, 8, 0),
            )
        )

    assert uow.rollbacks >= 1


def test_create_voyage_repository_failure_rolls_back_and_maps_repository_exception() -> None:
    uow = FakeVoyageUnitOfWork(fail_voyage_add=True)

    with pytest.raises(RepositoryException):
        CreateVoyageUseCase(unit_of_work=uow).execute(_create_request())

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_plan_voyage_happy_path_not_found_and_invalid_lifecycle() -> None:
    uow = FakeVoyageUnitOfWork()
    voyage = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D101"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D201"),
        planned_departure_at=_aware_utc(2028, 2, 1, 8, 0),
    )

    planned = PlanVoyageUseCase(unit_of_work=uow).execute(
        PlanVoyageRequest(voyage_id=voyage.id.value)
    )
    assert planned.voyage.status == "PLANNED"
    assert uow.commits == 1

    with pytest.raises(BusinessRuleViolation):
        PlanVoyageUseCase(unit_of_work=uow).execute(
            PlanVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000D999"))
        )

    with pytest.raises(BusinessRuleViolation):
        PlanVoyageUseCase(unit_of_work=uow).execute(
            PlanVoyageRequest(voyage_id=voyage.id.value)
        )


def test_depart_voyage_happy_path_not_found_invalid_lifecycle_and_explicit_time() -> None:
    uow = FakeVoyageUnitOfWork()
    voyage = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D102"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D202"),
        planned_departure_at=_aware_utc(2028, 2, 2, 8, 0),
    )
    PlanVoyageUseCase(unit_of_work=uow).execute(PlanVoyageRequest(voyage_id=voyage.id.value))

    departed_at = _aware_utc(2028, 2, 2, 9, 15)
    response = DepartVoyageUseCase(unit_of_work=uow).execute(
        DepartVoyageRequest(
            voyage_id=voyage.id.value,
            departed_at=departed_at,
            actual_departure_location=_location("Port A", "PORT-A"),
        )
    )

    assert response.voyage.status == "UNDERWAY"
    assert response.voyage.departed_at == departed_at
    assert response.voyage.actual_departure_location is not None
    assert response.voyage.actual_departure_location.name_snapshot == "Port A"

    with pytest.raises(BusinessRuleViolation):
        DepartVoyageUseCase(unit_of_work=uow).execute(
            DepartVoyageRequest(
                voyage_id=UUID("00000000-0000-0000-0000-00000000D998"),
                departed_at=departed_at,
                actual_departure_location=_location("Port A", "PORT-A"),
            )
        )

    with pytest.raises(BusinessRuleViolation):
        DepartVoyageUseCase(unit_of_work=uow).execute(
            DepartVoyageRequest(
                voyage_id=voyage.id.value,
                departed_at=_aware_utc(2028, 2, 2, 10, 0),
                actual_departure_location=_location("Port A", "PORT-A"),
            )
        )


def test_arrive_voyage_happy_path_not_found_invalid_chronology_and_port_b_vs_port_c() -> None:
    uow = FakeVoyageUnitOfWork()
    voyage = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D103"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D203"),
        planned_departure_at=_aware_utc(2028, 2, 3, 8, 0),
    )
    PlanVoyageUseCase(unit_of_work=uow).execute(PlanVoyageRequest(voyage_id=voyage.id.value))
    DepartVoyageUseCase(unit_of_work=uow).execute(
        DepartVoyageRequest(
            voyage_id=voyage.id.value,
            departed_at=_aware_utc(2028, 2, 3, 9, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )
    )

    arrived = ArriveVoyageUseCase(unit_of_work=uow).execute(
        ArriveVoyageRequest(
            voyage_id=voyage.id.value,
            arrived_at=_aware_utc(2028, 2, 3, 20, 30),
            actual_arrival_location=_location("Port C", "PORT-C"),
        )
    )

    assert arrived.voyage.status == "COMPLETED"
    assert arrived.voyage.planned_arrival_location.name_snapshot == "Port B"
    assert arrived.voyage.actual_arrival_location is not None
    assert arrived.voyage.actual_arrival_location.name_snapshot == "Port C"

    with pytest.raises(BusinessRuleViolation):
        ArriveVoyageUseCase(unit_of_work=uow).execute(
            ArriveVoyageRequest(
                voyage_id=UUID("00000000-0000-0000-0000-00000000D997"),
                arrived_at=_aware_utc(2028, 2, 3, 21, 0),
                actual_arrival_location=_location("Port C", "PORT-C"),
            )
        )

    voyage_2 = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D104"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D204"),
        planned_departure_at=_aware_utc(2028, 2, 4, 8, 0),
    )
    PlanVoyageUseCase(unit_of_work=uow).execute(PlanVoyageRequest(voyage_id=voyage_2.id.value))
    DepartVoyageUseCase(unit_of_work=uow).execute(
        DepartVoyageRequest(
            voyage_id=voyage_2.id.value,
            departed_at=_aware_utc(2028, 2, 4, 9, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )
    )

    with pytest.raises(BusinessRuleViolation):
        ArriveVoyageUseCase(unit_of_work=uow).execute(
            ArriveVoyageRequest(
                voyage_id=voyage_2.id.value,
                arrived_at=_aware_utc(2028, 2, 4, 8, 30),
                actual_arrival_location=_location("Port C", "PORT-C"),
            )
        )


def test_cancel_voyage_happy_path_not_found_invalid_lifecycle_and_no_actual_fabrication() -> None:
    uow = FakeVoyageUnitOfWork()
    voyage = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D105"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D205"),
        planned_departure_at=_aware_utc(2028, 2, 5, 8, 0),
    )
    PlanVoyageUseCase(unit_of_work=uow).execute(PlanVoyageRequest(voyage_id=voyage.id.value))

    cancelled = CancelVoyageUseCase(unit_of_work=uow).execute(
        CancelVoyageRequest(
            voyage_id=voyage.id.value,
            cancellation_reason="Weather closure",
            cancelled_at=_aware_utc(2028, 2, 5, 7, 30),
            cancelled_by_reference="planner",
        )
    )

    assert cancelled.voyage.status == "CANCELLED"
    assert cancelled.voyage.cancellation_reason == "Weather closure"
    assert cancelled.voyage.actual_departure_location is None
    assert cancelled.voyage.actual_arrival_location is None
    assert cancelled.voyage.departed_at is None
    assert cancelled.voyage.arrived_at is None

    with pytest.raises(BusinessRuleViolation):
        CancelVoyageUseCase(unit_of_work=uow).execute(
            CancelVoyageRequest(
                voyage_id=UUID("00000000-0000-0000-0000-00000000D996"),
                cancellation_reason="x",
                cancelled_at=_aware_utc(2028, 2, 5, 7, 0),
            )
        )

    voyage_underway = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D106"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D206"),
        planned_departure_at=_aware_utc(2028, 2, 6, 8, 0),
    )
    PlanVoyageUseCase(unit_of_work=uow).execute(
        PlanVoyageRequest(voyage_id=voyage_underway.id.value)
    )
    DepartVoyageUseCase(unit_of_work=uow).execute(
        DepartVoyageRequest(
            voyage_id=voyage_underway.id.value,
            departed_at=_aware_utc(2028, 2, 6, 9, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )
    )

    with pytest.raises(BusinessRuleViolation):
        CancelVoyageUseCase(unit_of_work=uow).execute(
            CancelVoyageRequest(
                voyage_id=voyage_underway.id.value,
                cancellation_reason="Too late",
                cancelled_at=_aware_utc(2028, 2, 6, 10, 0),
            )
        )


def test_get_voyage_state_mappings_and_missing() -> None:
    uow = FakeVoyageUnitOfWork()

    draft = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D201"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D301"),
        planned_departure_at=_aware_utc(2028, 3, 1, 8, 0),
    )

    planned = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D202"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D302"),
        planned_departure_at=_aware_utc(2028, 3, 2, 8, 0),
    )
    planned.plan()
    uow._repository._items[planned.id.value] = deepcopy(planned)

    underway = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D203"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D303"),
        planned_departure_at=_aware_utc(2028, 3, 3, 8, 0),
    )
    underway.plan()
    underway.depart(
        departed_at=_aware_utc(2028, 3, 3, 9, 0),
        actual_departure_location=LocationSnapshot(name_snapshot="Port A", location_external_id="PORT-A"),
    )
    uow._repository._items[underway.id.value] = deepcopy(underway)

    completed = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D204"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D304"),
        planned_departure_at=_aware_utc(2028, 3, 4, 8, 0),
    )
    completed.plan()
    completed.depart(
        departed_at=_aware_utc(2028, 3, 4, 9, 0),
        actual_departure_location=LocationSnapshot(name_snapshot="Port A", location_external_id="PORT-A"),
    )
    completed.arrive(
        arrived_at=_aware_utc(2028, 3, 4, 20, 0),
        actual_arrival_location=LocationSnapshot(name_snapshot="Port C", location_external_id="PORT-C"),
    )
    uow._repository._items[completed.id.value] = deepcopy(completed)

    cancelled = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D205"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D305"),
        planned_departure_at=_aware_utc(2028, 3, 5, 8, 0),
    )
    cancelled.plan()
    cancelled.cancel(
        cancellation_reason="Storm",
        cancelled_at=_aware_utc(2028, 3, 5, 7, 30),
    )
    uow._repository._items[cancelled.id.value] = deepcopy(cancelled)

    get_use_case = GetVoyageUseCase(unit_of_work=uow)

    assert get_use_case.execute(GetVoyageRequest(voyage_id=draft.id.value)).voyage.status == "DRAFT"
    assert get_use_case.execute(GetVoyageRequest(voyage_id=planned.id.value)).voyage.status == "PLANNED"
    assert get_use_case.execute(GetVoyageRequest(voyage_id=underway.id.value)).voyage.status == "UNDERWAY"
    assert get_use_case.execute(GetVoyageRequest(voyage_id=completed.id.value)).voyage.status == "COMPLETED"
    assert get_use_case.execute(GetVoyageRequest(voyage_id=cancelled.id.value)).voyage.status == "CANCELLED"

    with pytest.raises(BusinessRuleViolation):
        get_use_case.execute(
            GetVoyageRequest(voyage_id=UUID("00000000-0000-0000-0000-00000000D995"))
        )


def test_list_vessel_voyages_filters_and_returns_content_only_for_requested_vessel() -> None:
    uow = FakeVoyageUnitOfWork()
    vessel_a = UUID("00000000-0000-0000-0000-00000000D401")
    vessel_b = UUID("00000000-0000-0000-0000-00000000D402")

    a1 = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D501"),
        vessel_id=vessel_a,
        planned_departure_at=_aware_utc(2028, 4, 1, 8, 0),
    )
    a2 = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D502"),
        vessel_id=vessel_a,
        planned_departure_at=_aware_utc(2028, 4, 2, 8, 0),
    )
    _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D503"),
        vessel_id=vessel_b,
        planned_departure_at=_aware_utc(2028, 4, 3, 8, 0),
    )

    response = ListVesselVoyagesUseCase(unit_of_work=uow).execute(
        ListVesselVoyagesRequest(vessel_id=vessel_a)
    )

    assert [item.voyage_id for item in response.voyages] == [a1.id.value, a2.id.value]
    assert [item.voyage_reference for item in response.voyages] == [
        f"REF-{a1.id.value}",
        f"REF-{a2.id.value}",
    ]
    assert all(item.vessel_id == vessel_a for item in response.voyages)
    assert uow._repository.get_by_vessel_calls >= 1


def test_historical_voyage_truth_is_preserved_through_application_services() -> None:
    uow = FakeVoyageUnitOfWork()

    created = CreateVoyageUseCase(unit_of_work=uow).execute(
        CreateVoyageRequest(
            voyage_id=UUID("00000000-0000-0000-0000-00000000D601"),
            vessel_id=UUID("00000000-0000-0000-0000-00000000D701"),
            planned_departure_location=_location("Port A", "PORT-A"),
            planned_arrival_location=_location("Port B", "PORT-B"),
            planned_departure_at=_aware_utc(2028, 6, 1, 8, 0),
            planned_arrival_at=_aware_utc(2028, 6, 1, 18, 0),
            voyage_reference="VOY-HISTORY",
            purpose_code="DEMONSTRATION",
            purpose_detail="Historic run",
        )
    )

    PlanVoyageUseCase(unit_of_work=uow).execute(
        PlanVoyageRequest(voyage_id=created.voyage.voyage_id)
    )
    DepartVoyageUseCase(unit_of_work=uow).execute(
        DepartVoyageRequest(
            voyage_id=created.voyage.voyage_id,
            departed_at=_aware_utc(2028, 6, 1, 9, 0),
            actual_departure_location=_location("Port A", "PORT-A"),
        )
    )
    ArriveVoyageUseCase(unit_of_work=uow).execute(
        ArriveVoyageRequest(
            voyage_id=created.voyage.voyage_id,
            arrived_at=_aware_utc(2028, 6, 1, 20, 0),
            actual_arrival_location=_location("Port C", "PORT-C"),
        )
    )

    loaded = GetVoyageUseCase(unit_of_work=uow).execute(
        GetVoyageRequest(voyage_id=created.voyage.voyage_id)
    )

    assert loaded.voyage.planned_departure_location.name_snapshot == "Port A"
    assert loaded.voyage.planned_arrival_location.name_snapshot == "Port B"
    assert loaded.voyage.planned_departure_at == _aware_utc(2028, 6, 1, 8, 0)
    assert loaded.voyage.planned_arrival_at == _aware_utc(2028, 6, 1, 18, 0)

    assert loaded.voyage.actual_departure_location is not None
    assert loaded.voyage.actual_departure_location.name_snapshot == "Port A"
    assert loaded.voyage.actual_arrival_location is not None
    assert loaded.voyage.actual_arrival_location.name_snapshot == "Port C"
    assert loaded.voyage.departed_at == _aware_utc(2028, 6, 1, 9, 0)
    assert loaded.voyage.arrived_at == _aware_utc(2028, 6, 1, 20, 0)


def test_command_failures_roll_back_and_do_not_commit() -> None:
    uow = FakeVoyageUnitOfWork()
    voyage = _seed_voyage(
        uow,
        voyage_id=UUID("00000000-0000-0000-0000-00000000D602"),
        vessel_id=UUID("00000000-0000-0000-0000-00000000D702"),
        planned_departure_at=_aware_utc(2028, 7, 1, 8, 0),
    )
    PlanVoyageUseCase(unit_of_work=uow).execute(PlanVoyageRequest(voyage_id=voyage.id.value))

    before = GetVoyageUseCase(unit_of_work=uow).execute(
        GetVoyageRequest(voyage_id=voyage.id.value)
    )

    with pytest.raises(BusinessRuleViolation):
        ArriveVoyageUseCase(unit_of_work=uow).execute(
            ArriveVoyageRequest(
                voyage_id=voyage.id.value,
                arrived_at=_aware_utc(2028, 7, 1, 7, 0),
                actual_arrival_location=_location("Port C", "PORT-C"),
            )
        )

    after = GetVoyageUseCase(unit_of_work=uow).execute(
        GetVoyageRequest(voyage_id=voyage.id.value)
    )

    assert before.voyage.status == "PLANNED"
    assert after.voyage.status == "PLANNED"
    assert after.voyage.planned_arrival_location.name_snapshot == "Port B"
    assert after.voyage.actual_arrival_location is None


def test_timezone_policy_preserves_utc_normalization_and_has_no_hidden_clock() -> None:
    uow = FakeVoyageUnitOfWork()
    plus_two = timezone(timedelta(hours=2))

    created = CreateVoyageUseCase(unit_of_work=uow).execute(
        _create_request(
            voyage_id=UUID("00000000-0000-0000-0000-00000000D603"),
            planned_departure_at=datetime(2028, 8, 1, 10, 0, tzinfo=plus_two),
            planned_arrival_at=datetime(2028, 8, 1, 14, 0, tzinfo=plus_two),
        )
    )

    assert created.voyage.planned_departure_at == datetime(2028, 8, 1, 8, 0, tzinfo=UTC)
    assert created.voyage.planned_arrival_at == datetime(2028, 8, 1, 12, 0, tzinfo=UTC)


def test_response_is_application_safe_and_does_not_leak_domain_types() -> None:
    uow = FakeVoyageUnitOfWork()
    created = CreateVoyageUseCase(unit_of_work=uow).execute(_create_request())

    assert is_dataclass(created.voyage)
    assert not isinstance(created.voyage, Voyage)
    assert not isinstance(created.voyage.planned_departure_location, LocationSnapshot)
    assert created.voyage.voyage_purpose is not None
    assert not isinstance(created.voyage.voyage_purpose, VoyagePurpose)
    assert isinstance(created.voyage.status, str)
    assert isinstance(created.voyage.vessel_id, UUID)


def test_create_voyage_commit_failure_maps_repository_exception_and_rolls_back() -> None:
    uow = FakeVoyageUnitOfWork(fail_commit=True)

    with pytest.raises(RepositoryException):
        CreateVoyageUseCase(unit_of_work=uow).execute(_create_request())

    assert uow.commits == 1
    assert uow.rollbacks >= 1
