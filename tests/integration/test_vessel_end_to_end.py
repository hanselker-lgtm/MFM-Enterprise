from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.application.asset.create_asset import CreateAssetUseCase
from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.features.asset.create_asset_feature import CreateAssetFeature
from mfm.application.features.asset.create_asset_feature import CreateAssetRequest
from mfm.application.features.fleet.change_vessel_registration_feature import (
    BusinessRuleViolation as ChangeVesselRegistrationBusinessRuleViolation,
)
from mfm.application.features.fleet.change_vessel_registration_feature import (
    ChangeVesselRegistrationFeature,
)
from mfm.application.features.fleet.change_vessel_registration_feature import (
    ChangeVesselRegistrationRequest,
)
from mfm.application.features.fleet.change_vessel_status_feature import (
    BusinessRuleViolation as ChangeVesselStatusBusinessRuleViolation,
)
from mfm.application.features.fleet.change_vessel_status_feature import (
    ChangeVesselStatusFeature,
)
from mfm.application.features.fleet.change_vessel_status_feature import (
    ChangeVesselStatusRequest,
)
from mfm.application.features.fleet.create_vessel_feature import CreateVesselFeature
from mfm.application.features.fleet.create_vessel_feature import CreateVesselRequest
from mfm.application.features.fleet.rename_vessel_feature import RenameVesselFeature
from mfm.application.features.fleet.rename_vessel_feature import RenameVesselRequest
from mfm.application.features.fleet.update_vessel_dimensions_feature import (
    UpdateVesselDimensionsFeature,
)
from mfm.application.features.fleet.update_vessel_dimensions_feature import (
    UpdateVesselDimensionsRequest,
)
from mfm.application.fleet.change_vessel_registration import ChangeVesselRegistrationUseCase
from mfm.application.fleet.change_vessel_status import ChangeVesselStatusUseCase
from mfm.application.fleet.create_vessel import CreateVesselUseCase
from mfm.application.fleet.rename_vessel import RenameVesselUseCase
from mfm.application.fleet.update_vessel_dimensions import UpdateVesselDimensionsUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.base_model import BaseModel
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.asset.asset_status import AssetStatus
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_status import VesselStatus
from mfm.infrastructure.persistence.sqlite.sqlite_asset_repository import SQLiteAssetRepository
from mfm.infrastructure.persistence.sqlite.sqlite_vessel_repository import SQLiteVesselRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SqliteFleetApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.asset_repository = SQLiteAssetRepository(self._persistence_uow)
        self.vessel_repository = SQLiteVesselRepository(self._persistence_uow)

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


@dataclass(frozen=True, slots=True)
class FeatureStack:
    create_asset: CreateAssetFeature
    create_vessel: CreateVesselFeature
    rename_vessel: RenameVesselFeature
    change_vessel_registration: ChangeVesselRegistrationFeature
    update_vessel_dimensions: UpdateVesselDimensionsFeature
    change_vessel_status: ChangeVesselStatusFeature


@pytest.fixture(autouse=True)
def clear_domain_registries() -> None:
    Asset._clear_registry_for_tests()
    Vessel._clear_registry_for_tests()


@pytest.fixture()
def sqlite_session(tmp_path: Path) -> Session:
    db_path = tmp_path / "fleet-006.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)

    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


def _build_stack(session: Session) -> FeatureStack:
    dispatcher = DomainEventDispatcher()
    app_uow = SqliteFleetApplicationUnitOfWork(session)

    return FeatureStack(
        create_asset=CreateAssetFeature(
            service=CreateAssetUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        create_vessel=CreateVesselFeature(
            service=CreateVesselUseCase(unit_of_work=app_uow)
        ),
        rename_vessel=RenameVesselFeature(
            service=RenameVesselUseCase(unit_of_work=app_uow)
        ),
        change_vessel_registration=ChangeVesselRegistrationFeature(
            service=ChangeVesselRegistrationUseCase(unit_of_work=app_uow)
        ),
        update_vessel_dimensions=UpdateVesselDimensionsFeature(
            service=UpdateVesselDimensionsUseCase(unit_of_work=app_uow)
        ),
        change_vessel_status=ChangeVesselStatusFeature(
            service=ChangeVesselStatusUseCase(unit_of_work=app_uow)
        ),
    )


def _reload_asset(session: Session, asset_id: UUID) -> Asset:
    reload_uow = UnitOfWork(session)
    repository = SQLiteAssetRepository(reload_uow)
    reloaded = repository.get_by_id(asset_id)
    assert reloaded is not None
    return reloaded


def _reload_vessel(session: Session, vessel_id: UUID) -> Vessel:
    reload_uow = UnitOfWork(session)
    repository = SQLiteVesselRepository(reload_uow)
    reloaded = repository.get_by_id(vessel_id)
    assert reloaded is not None
    return reloaded


def test_fleet_006_workflow_1_create_vessel_persist_reload_verify_complete_state(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)

    create_asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-FLT-{uuid4().hex[:6].upper()}",
            name="E2E Vessel Asset",
            description="Asset prerequisite for vessel workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Harbor North",
        )
    )

    create_vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=create_asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="E2E Northern Star",
            shipyard="Odense Yard",
            build_year=2019,
            construction_material=VesselMaterial.STEEL,
            length=24.5,
            beam=6.3,
            draft=2.1,
            status=VesselStatus.ACTIVE,
        )
    )

    assert isinstance(create_vessel_response.vessel_id, UUID)
    assert create_vessel_response.asset_id == create_asset_response.asset_id
    assert create_vessel_response.registration.startswith("OY-")
    assert create_vessel_response.name == "E2E Northern Star"
    assert create_vessel_response.status == "ACTIVE"

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_vessel(reload_session, create_vessel_response.vessel_id)
        assert reloaded.id.value == create_vessel_response.vessel_id
        assert reloaded.asset_id == create_asset_response.asset_id
        assert reloaded.registration.value == create_vessel_response.registration
        assert reloaded.name == "E2E Northern Star"
        assert reloaded.shipyard == "Odense Yard"
        assert reloaded.build_year == 2019
        assert reloaded.length == pytest.approx(24.5)
        assert reloaded.beam == pytest.approx(6.3)
        assert reloaded.draft == pytest.approx(2.1)
        assert reloaded.construction_material is VesselMaterial.STEEL
        assert reloaded.status is VesselStatus.ACTIVE
    finally:
        reload_session.close()


def test_fleet_006_workflow_2_rename_vessel_persist_reload_verify_new_name(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)

    asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-FLT-{uuid4().hex[:6].upper()}",
            name="Rename Asset",
            description="Asset for rename workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Harbor South",
        )
    )

    vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Old Name",
            shipyard="Svendborg",
            build_year=2015,
            construction_material=VesselMaterial.WOOD,
            length=11.0,
            beam=3.2,
            draft=1.0,
            status=VesselStatus.ACTIVE,
        )
    )

    rename_response = stack.rename_vessel.execute(
        RenameVesselRequest(vessel_id=vessel_response.vessel_id, name="New Name")
    )

    assert rename_response.vessel_id == vessel_response.vessel_id
    assert rename_response.name == "New Name"

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_vessel(reload_session, vessel_response.vessel_id)
        assert reloaded.name == "New Name"
    finally:
        reload_session.close()


def test_fleet_006_workflow_3_change_registration_persist_reload_and_lookup(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)

    asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-FLT-{uuid4().hex[:6].upper()}",
            name="Registration Asset",
            description="Asset for registration workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Harbor East",
        )
    )

    vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Registration Test",
            shipyard="Roskilde",
            build_year=2018,
            construction_material=VesselMaterial.COMPOSITE,
            length=13.0,
            beam=3.7,
            draft=1.2,
            status=VesselStatus.ACTIVE,
        )
    )

    new_registration = f"OY-{uuid4().hex[:6].upper()}"
    update_response = stack.change_vessel_registration.execute(
        ChangeVesselRegistrationRequest(
            vessel_id=vessel_response.vessel_id,
            registration=new_registration,
        )
    )

    assert update_response.vessel_id == vessel_response.vessel_id
    assert update_response.registration == new_registration

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_vessel(reload_session, vessel_response.vessel_id)
        assert reloaded.registration.value == new_registration

        lookup_repository = SQLiteVesselRepository(UnitOfWork(reload_session))
        looked_up = lookup_repository.get_by_registration(new_registration)
        assert looked_up is not None
        assert looked_up.id.value == vessel_response.vessel_id
    finally:
        reload_session.close()


def test_fleet_006_workflow_4_update_dimensions_persist_reload_roundtrip(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)

    asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-FLT-{uuid4().hex[:6].upper()}",
            name="Dimensions Asset",
            description="Asset for dimensions workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Harbor West",
        )
    )

    vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Dimensions Test",
            shipyard="Frederikshavn",
            build_year=2021,
            construction_material=VesselMaterial.ALUMINUM,
            length=9.5,
            beam=2.8,
            draft=0.9,
            status=VesselStatus.ACTIVE,
        )
    )

    update_response = stack.update_vessel_dimensions.execute(
        UpdateVesselDimensionsRequest(
            vessel_id=vessel_response.vessel_id,
            length=10.2,
            beam=3.1,
            draft=1.0,
        )
    )

    assert update_response.vessel_id == vessel_response.vessel_id
    assert update_response.length == pytest.approx(10.2)
    assert update_response.beam == pytest.approx(3.1)
    assert update_response.draft == pytest.approx(1.0)

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_vessel(reload_session, vessel_response.vessel_id)
        assert reloaded.length == pytest.approx(10.2)
        assert reloaded.beam == pytest.approx(3.1)
        assert reloaded.draft == pytest.approx(1.0)
    finally:
        reload_session.close()


def test_fleet_006_workflow_5_vessel_lifecycle_and_permanent_retirement_rule(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)

    asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-FLT-{uuid4().hex[:6].upper()}",
            name="Lifecycle Asset",
            description="Asset for lifecycle workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Dock 5",
        )
    )

    vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Lifecycle Test",
            shipyard="Skagen",
            build_year=2012,
            construction_material=VesselMaterial.STEEL,
            length=14.0,
            beam=4.0,
            draft=1.4,
            status=VesselStatus.ACTIVE,
        )
    )

    laid_up = stack.change_vessel_status.execute(
        ChangeVesselStatusRequest(
            vessel_id=vessel_response.vessel_id,
            status=VesselStatus.LAID_UP,
        )
    )
    restoration = stack.change_vessel_status.execute(
        ChangeVesselStatusRequest(
            vessel_id=vessel_response.vessel_id,
            status=VesselStatus.RESTORATION,
        )
    )
    active_again = stack.change_vessel_status.execute(
        ChangeVesselStatusRequest(
            vessel_id=vessel_response.vessel_id,
            status=VesselStatus.ACTIVE,
        )
    )
    retired = stack.change_vessel_status.execute(
        ChangeVesselStatusRequest(
            vessel_id=vessel_response.vessel_id,
            status=VesselStatus.RETIRED,
        )
    )

    assert laid_up.status == "LAID_UP"
    assert restoration.status == "RESTORATION"
    assert active_again.status == "ACTIVE"
    assert retired.status == "RETIRED"

    with pytest.raises(ChangeVesselStatusBusinessRuleViolation):
        stack.change_vessel_status.execute(
            ChangeVesselStatusRequest(
                vessel_id=vessel_response.vessel_id,
                status=VesselStatus.ACTIVE,
            )
        )

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded = _reload_vessel(reload_session, vessel_response.vessel_id)
        assert reloaded.status is VesselStatus.RETIRED
    finally:
        reload_session.close()


def test_fleet_006_workflow_6_asset_fleet_boundary_integrity(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)

    create_asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-FLT-{uuid4().hex[:6].upper()}",
            name="Boundary Asset",
            description="Asset for fleet boundary workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Boundary Harbor",
        )
    )

    create_vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=create_asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Boundary Vessel",
            shipyard="Aalborg",
            build_year=2016,
            construction_material=VesselMaterial.OTHER,
            length=16.3,
            beam=4.6,
            draft=1.5,
            status=VesselStatus.ACTIVE,
        )
    )

    assert isinstance(create_vessel_response.vessel_id, UUID)
    assert isinstance(create_vessel_response.asset_id, UUID)
    assert isinstance(create_vessel_response.status, str)

    reload_session = Session(sqlite_session.get_bind())
    try:
        reloaded_asset = _reload_asset(reload_session, create_asset_response.asset_id)
        reloaded_vessel = _reload_vessel(reload_session, create_vessel_response.vessel_id)

        assert isinstance(reloaded_asset, Asset)
        assert isinstance(reloaded_vessel, Vessel)
        assert reloaded_vessel.asset_id == reloaded_asset.id.value

        assert reloaded_asset.asset_number.value == create_asset_response.asset_number
        assert reloaded_asset.name == "Boundary Asset"
        assert reloaded_asset.status is AssetStatus.ACTIVE
        assert reloaded_asset.location.value == "Boundary Harbor"

        assert reloaded_vessel.name == "Boundary Vessel"
        assert not hasattr(reloaded_vessel, "location")
        assert reloaded_vessel.status is VesselStatus.ACTIVE

        vessel_repo = SQLiteVesselRepository(UnitOfWork(reload_session))
        looked_up = vessel_repo.get_by_registration(create_vessel_response.registration)
        assert looked_up is not None
        assert looked_up.asset_id == create_asset_response.asset_id
    finally:
        reload_session.close()


def test_fleet_006_workflow_3_duplicate_registration_rejected(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)

    first_asset = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-FLT-{uuid4().hex[:6].upper()}",
            name="First Asset",
            description="First asset for duplicate registration test",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Dock A",
        )
    )
    second_asset = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-FLT-{uuid4().hex[:6].upper()}",
            name="Second Asset",
            description="Second asset for duplicate registration test",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Dock B",
        )
    )

    registration = f"OY-{uuid4().hex[:6].upper()}"
    first_vessel = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=first_asset.asset_id,
            registration=registration,
            name="First Vessel",
            shipyard="Nakskov",
            build_year=2014,
            construction_material=VesselMaterial.STEEL,
            length=12.0,
            beam=3.5,
            draft=1.1,
            status=VesselStatus.ACTIVE,
        )
    )

    second_vessel = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=second_asset.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Second Vessel",
            shipyard="Nakskov",
            build_year=2014,
            construction_material=VesselMaterial.STEEL,
            length=12.0,
            beam=3.5,
            draft=1.1,
            status=VesselStatus.ACTIVE,
        )
    )

    with pytest.raises(ChangeVesselRegistrationBusinessRuleViolation):
        stack.change_vessel_registration.execute(
            ChangeVesselRegistrationRequest(
                vessel_id=second_vessel.vessel_id,
                registration=registration,
            )
        )

    reload_session = Session(sqlite_session.get_bind())
    try:
        first_reloaded = _reload_vessel(reload_session, first_vessel.vessel_id)
        second_reloaded = _reload_vessel(reload_session, second_vessel.vessel_id)

        assert first_reloaded.registration.value == registration
        assert second_reloaded.registration.value != registration
    finally:
        reload_session.close()
