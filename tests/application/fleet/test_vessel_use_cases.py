from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.fleet.change_vessel_registration import (
    ChangeVesselRegistrationRequest,
    ChangeVesselRegistrationUseCase,
)
from mfm.application.fleet.change_vessel_status import (
    ChangeVesselStatusRequest,
    ChangeVesselStatusUseCase,
)
from mfm.application.fleet.create_vessel import (
    BusinessRuleViolation,
    CreateVesselRequest,
    CreateVesselUseCase,
    RepositoryException,
)
from mfm.application.fleet.rename_vessel import RenameVesselRequest
from mfm.application.fleet.rename_vessel import RenameVesselUseCase
from mfm.application.fleet.update_vessel import UpdateVesselRequest
from mfm.application.fleet.update_vessel import UpdateVesselUseCase
from mfm.application.fleet.update_vessel_dimensions import (
    UpdateVesselDimensionsRequest,
    UpdateVesselDimensionsUseCase,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_registration import VesselRegistration
from mfm.domain.fleet.vessel_status import VesselStatus


class InMemoryVesselRepository:
    def __init__(
        self,
        store: dict[UUID, Vessel],
        *,
        fail_on_add: bool = False,
        fail_on_update: bool = False,
    ) -> None:
        self._store = store
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

        self.add_calls = 0
        self.get_by_id_calls = 0
        self.get_by_registration_calls = 0
        self.update_calls = 0

    def add(self, vessel: Vessel) -> None:
        self.add_calls += 1
        if self._fail_on_add:
            raise RuntimeError("vessel add failed")
        self._store[vessel.id.value] = vessel

    def get_by_id(self, vessel_id: UUID) -> Vessel | None:
        self.get_by_id_calls += 1
        return self._store.get(vessel_id)

    def get_by_registration(self, registration: str) -> Vessel | None:
        self.get_by_registration_calls += 1
        normalized = VesselRegistration(registration).value
        return next(
            (
                item
                for item in self._store.values()
                if item.registration.value == normalized
            ),
            None,
        )

    def update(self, vessel: Vessel) -> None:
        self.update_calls += 1
        if self._fail_on_update:
            raise RuntimeError("vessel update failed")
        self._store[vessel.id.value] = vessel

    def delete(self, vessel_id: UUID) -> None:
        self._store.pop(vessel_id, None)

    def exists(self, vessel_id: UUID) -> bool:
        return vessel_id in self._store

    def list(self) -> list[Vessel]:
        return list(self._store.values())

    def search(self, text: str) -> list[Vessel]:
        lowered = text.casefold()
        return [
            item
            for item in self._store.values()
            if lowered in item.registration.value.casefold()
            or lowered in item.name.casefold()
            or lowered in item.shipyard.casefold()
        ]


@dataclass(slots=True)
class _NoopRepo:
    def add(self, entity):
        _ = entity


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_vessel_add: bool = False,
        fail_vessel_update: bool = False,
    ) -> None:
        super().__init__()
        self.fail_vessel_add = fail_vessel_add
        self.fail_vessel_update = fail_vessel_update

        self.vessels: dict[UUID, Vessel] = {}

        self.commits = 0
        self.rollbacks = 0
        self.last_vessel_repository: InMemoryVesselRepository | None = None

    def _start_scope(self) -> None:
        self._snapshot = deepcopy(self.vessels)

        self.vessel_repository = InMemoryVesselRepository(
            self.vessels,
            fail_on_add=self.fail_vessel_add,
            fail_on_update=self.fail_vessel_update,
        )
        self.last_vessel_repository = self.vessel_repository

        self.contact_repository = _NoopRepo()
        self.member_repository = _NoopRepo()
        self.membership_repository = _NoopRepo()
        self.invoice_repository = _NoopRepo()
        self.payment_repository = _NoopRepo()
        self.journal_repository = _NoopRepo()

    def _commit_impl(self) -> None:
        self.commits += 1

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self.vessels = self._snapshot

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Vessel._clear_registry_for_tests()


def _seed_vessel(uow: FakeUnitOfWork, registration: str = "OY-APP-001") -> Vessel:
    vessel = Vessel(
        asset_id=uuid4(),
        registration=VesselRegistration(registration),
        name="Seed Vessel",
        shipyard="Odense",
        build_year=2012,
        construction_material=VesselMaterial.STEEL,
        length=21.5,
        beam=5.2,
        draft=1.7,
        status=VesselStatus.ACTIVE,
    )
    uow.vessels[vessel.id.value] = vessel
    return vessel


def test_create_vessel() -> None:
    uow = FakeUnitOfWork()
    use_case = CreateVesselUseCase(unit_of_work=uow)
    asset_id = uuid4()

    response = use_case.execute(
        CreateVesselRequest(
            asset_id=asset_id,
            registration="OY-APP-100",
            name="Application Vessel",
            shipyard="Frederikshavn",
            build_year=2020,
            construction_material=VesselMaterial.ALUMINUM,
            length=14.2,
            beam=4.1,
            draft=1.3,
            status=VesselStatus.ACTIVE,
        )
    )

    assert uow.commits == 1
    assert response.asset_id == asset_id
    assert response.registration == "OY-APP-100"
    assert response.status == "ACTIVE"
    assert response.vessel_id in uow.vessels


def test_duplicate_registration() -> None:
    uow = FakeUnitOfWork()
    _ = _seed_vessel(uow, "OY-APP-DUP")
    use_case = CreateVesselUseCase(unit_of_work=uow)

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            CreateVesselRequest(
                asset_id=uuid4(),
                registration="oy-app-dup",
                name="Duplicate",
                shipyard="Yard",
                build_year=2011,
                construction_material=VesselMaterial.OTHER,
                length=10.0,
                beam=3.0,
                draft=1.0,
                status=VesselStatus.ACTIVE,
            )
        )


def test_update_vessel() -> None:
    uow = FakeUnitOfWork()
    vessel = _seed_vessel(uow, "OY-APP-UPD")
    use_case = UpdateVesselUseCase(unit_of_work=uow)

    response = use_case.execute(
        UpdateVesselRequest(
            vessel_id=vessel.id.value,
            shipyard="Esbjerg",
            build_year=2018,
            construction_material=VesselMaterial.COMPOSITE,
        )
    )

    assert uow.commits == 1
    assert response.shipyard == "Esbjerg"
    assert response.build_year == 2018
    assert response.construction_material == "COMPOSITE"


def test_rename_vessel() -> None:
    uow = FakeUnitOfWork()
    vessel = _seed_vessel(uow, "OY-APP-RNM")
    use_case = RenameVesselUseCase(unit_of_work=uow)

    response = use_case.execute(
        RenameVesselRequest(vessel_id=vessel.id.value, name="Renamed Vessel")
    )

    assert uow.commits == 1
    assert response.name == "Renamed Vessel"
    assert uow.vessels[vessel.id.value].name == "Renamed Vessel"


def test_change_registration() -> None:
    uow = FakeUnitOfWork()
    vessel = _seed_vessel(uow, "OY-APP-REG")
    use_case = ChangeVesselRegistrationUseCase(unit_of_work=uow)

    response = use_case.execute(
        ChangeVesselRegistrationRequest(
            vessel_id=vessel.id.value,
            registration="OY-APP-REG-NEW",
        )
    )

    assert uow.commits == 1
    assert response.registration == "OY-APP-REG-NEW"


def test_update_dimensions() -> None:
    uow = FakeUnitOfWork()
    vessel = _seed_vessel(uow, "OY-APP-DIM")
    use_case = UpdateVesselDimensionsUseCase(unit_of_work=uow)

    response = use_case.execute(
        UpdateVesselDimensionsRequest(
            vessel_id=vessel.id.value,
            length=30.1,
            beam=6.3,
            draft=2.4,
        )
    )

    assert uow.commits == 1
    assert response.length == 30.1
    assert response.beam == 6.3
    assert response.draft == 2.4


def test_change_status() -> None:
    uow = FakeUnitOfWork()
    vessel = _seed_vessel(uow, "OY-APP-STS")
    use_case = ChangeVesselStatusUseCase(unit_of_work=uow)

    response = use_case.execute(
        ChangeVesselStatusRequest(
            vessel_id=vessel.id.value,
            status=VesselStatus.LAID_UP,
        )
    )

    assert uow.commits == 1
    assert response.status == "LAID_UP"


def test_invalid_state_transition() -> None:
    uow = FakeUnitOfWork()
    vessel = _seed_vessel(uow, "OY-APP-TRANS")
    vessel.change_status(VesselStatus.RETIRED)

    use_case = ChangeVesselStatusUseCase(unit_of_work=uow)

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            ChangeVesselStatusRequest(
                vessel_id=vessel.id.value,
                status=VesselStatus.ACTIVE,
            )
        )


def test_repository_interaction() -> None:
    uow = FakeUnitOfWork()
    vessel = _seed_vessel(uow, "OY-APP-INT")
    use_case = RenameVesselUseCase(unit_of_work=uow)

    _ = use_case.execute(
        RenameVesselRequest(vessel_id=vessel.id.value, name="Interaction")
    )

    assert uow.last_vessel_repository is not None
    assert uow.last_vessel_repository.get_by_id_calls >= 1
    assert uow.last_vessel_repository.update_calls == 1


def test_unit_of_work_commit() -> None:
    uow = FakeUnitOfWork()
    use_case = CreateVesselUseCase(unit_of_work=uow)

    _ = use_case.execute(
        CreateVesselRequest(
            asset_id=uuid4(),
            registration="OY-APP-COMMIT",
            name="Commit Vessel",
            shipyard="Yard",
            build_year=2019,
            construction_material=VesselMaterial.STEEL,
            length=12.0,
            beam=4.0,
            draft=1.4,
            status=VesselStatus.ACTIVE,
        )
    )

    assert uow.commits == 1


def test_rollback_on_error() -> None:
    uow = FakeUnitOfWork(fail_vessel_add=True)
    use_case = CreateVesselUseCase(unit_of_work=uow)

    with pytest.raises(RepositoryException):
        use_case.execute(
            CreateVesselRequest(
                asset_id=uuid4(),
                registration="OY-APP-ROLL",
                name="Rollback Vessel",
                shipyard="Yard",
                build_year=2014,
                construction_material=VesselMaterial.OTHER,
                length=10.0,
                beam=3.2,
                draft=1.0,
                status=VesselStatus.ACTIVE,
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_response_dto_mapping() -> None:
    uow = FakeUnitOfWork()
    use_case = CreateVesselUseCase(unit_of_work=uow)

    response = use_case.execute(
        CreateVesselRequest(
            asset_id=uuid4(),
            registration="OY-APP-DTO",
            name="DTO Vessel",
            shipyard="Aarhus",
            build_year=2021,
            construction_material=VesselMaterial.FIBERGLASS,
            length=13.5,
            beam=4.3,
            draft=1.2,
            status=VesselStatus.RESTORATION,
        )
    )

    assert isinstance(response.vessel_id, UUID)
    assert isinstance(response.asset_id, UUID)
    assert response.registration == "OY-APP-DTO"
    assert response.name == "DTO Vessel"
    assert response.status == "RESTORATION"
