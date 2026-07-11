from __future__ import annotations

from dataclasses import dataclass
from datetime import date
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
from mfm.application.features.fleet.create_vessel_feature import CreateVesselFeature
from mfm.application.features.fleet.create_vessel_feature import CreateVesselRequest
from mfm.application.features.technical_configuration.add_technical_component_feature import (
    AddTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.add_technical_component_feature import (
    AddTechnicalComponentRequest,
)
from mfm.application.features.technical_configuration.add_technical_component_feature import (
    SpecificationEntryInput,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    BusinessRuleViolation as TechnicalBusinessRuleViolation,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    CreateTechnicalConfigurationFeature,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    CreateTechnicalConfigurationRequest,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    TechnicalConfigurationResponse,
)
from mfm.application.features.technical_configuration.create_technical_configuration_feature import (
    to_feature_configuration_response,
)
from mfm.application.features.technical_configuration.install_technical_component_feature import (
    InstallTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.install_technical_component_feature import (
    InstallTechnicalComponentRequest,
)
from mfm.application.features.technical_configuration.remove_technical_component_feature import (
    RemoveTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.remove_technical_component_feature import (
    RemoveTechnicalComponentRequest,
)
from mfm.application.features.technical_configuration.replace_technical_component_feature import (
    ReplaceTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.replace_technical_component_feature import (
    ReplaceTechnicalComponentRequest,
)
from mfm.application.features.technical_configuration.update_technical_component_details_feature import (
    UpdateTechnicalComponentDetailsFeature,
)
from mfm.application.features.technical_configuration.update_technical_component_details_feature import (
    UpdateTechnicalComponentDetailsRequest,
)
from mfm.application.fleet.create_vessel import CreateVesselUseCase
from mfm.application.technical_configuration.add_technical_component import (
    AddTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    CreateTechnicalConfigurationUseCase,
)
from mfm.application.technical_configuration.create_technical_configuration import (
    to_configuration_response as to_application_configuration_response,
)
from mfm.application.technical_configuration.install_technical_component import (
    InstallTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.remove_technical_component import (
    RemoveTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.replace_technical_component import (
    ReplaceTechnicalComponentUseCase,
)
from mfm.application.technical_configuration.update_technical_component_details import (
    UpdateTechnicalComponentDetailsUseCase,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_status import VesselStatus
from mfm.infrastructure.persistence.sqlite.sqlite_asset_repository import SQLiteAssetRepository
from mfm.infrastructure.persistence.sqlite.sqlite_technical_configuration_repository import (
    SQLiteTechnicalConfigurationRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_vessel_repository import SQLiteVesselRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SqliteTechnicalConfigurationApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)

        self.asset_repository = SQLiteAssetRepository(self._persistence_uow)
        self.vessel_repository = SQLiteVesselRepository(self._persistence_uow)
        self.technical_configuration_repository = SQLiteTechnicalConfigurationRepository(
            self._persistence_uow
        )

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
    create_technical_configuration: CreateTechnicalConfigurationFeature
    add_technical_component: AddTechnicalComponentFeature
    install_technical_component: InstallTechnicalComponentFeature
    remove_technical_component: RemoveTechnicalComponentFeature
    replace_technical_component: ReplaceTechnicalComponentFeature
    update_technical_component_details: UpdateTechnicalComponentDetailsFeature


@pytest.fixture(autouse=True)
def clear_domain_registries() -> None:
    Asset._clear_registry_for_tests()
    Vessel._clear_registry_for_tests()


@pytest.fixture()
def sqlite_session(tmp_path: Path) -> Session:
    db_path = tmp_path / "technical-006.sqlite"
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
    app_uow = SqliteTechnicalConfigurationApplicationUnitOfWork(session)

    return FeatureStack(
        create_asset=CreateAssetFeature(
            service=CreateAssetUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        create_vessel=CreateVesselFeature(
            service=CreateVesselUseCase(unit_of_work=app_uow)
        ),
        create_technical_configuration=CreateTechnicalConfigurationFeature(
            service=CreateTechnicalConfigurationUseCase(unit_of_work=app_uow)
        ),
        add_technical_component=AddTechnicalComponentFeature(
            service=AddTechnicalComponentUseCase(unit_of_work=app_uow)
        ),
        install_technical_component=InstallTechnicalComponentFeature(
            service=InstallTechnicalComponentUseCase(unit_of_work=app_uow)
        ),
        remove_technical_component=RemoveTechnicalComponentFeature(
            service=RemoveTechnicalComponentUseCase(unit_of_work=app_uow)
        ),
        replace_technical_component=ReplaceTechnicalComponentFeature(
            service=ReplaceTechnicalComponentUseCase(unit_of_work=app_uow)
        ),
        update_technical_component_details=UpdateTechnicalComponentDetailsFeature(
            service=UpdateTechnicalComponentDetailsUseCase(unit_of_work=app_uow)
        ),
    )


def _create_vessel_prerequisite(stack: FeatureStack) -> UUID:
    create_asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-TC-{uuid4().hex[:6].upper()}",
            name="Technical Integration Asset",
            description="Asset prerequisite for technical configuration E2E",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Dock A",
        )
    )

    create_vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=create_asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Technical Integration Vessel",
            shipyard="Odense Yard",
            build_year=2019,
            construction_material=VesselMaterial.STEEL,
            length=28.0,
            beam=7.0,
            draft=2.4,
            status=VesselStatus.ACTIVE,
        )
    )

    return create_vessel_response.vessel_id


def _reload_technical_public(session: Session, configuration_id: UUID) -> TechnicalConfigurationResponse:
    repository = SQLiteTechnicalConfigurationRepository(UnitOfWork(session))
    configuration = repository.get_by_id(configuration_id)
    assert configuration is not None
    return to_feature_configuration_response(
        to_application_configuration_response(configuration)
    )


def _reload_asset(session: Session, asset_id: UUID) -> Asset:
    repository = SQLiteAssetRepository(UnitOfWork(session))
    loaded = repository.get_by_id(asset_id)
    assert loaded is not None
    return loaded


def _reload_vessel(session: Session, vessel_id: UUID) -> Vessel:
    repository = SQLiteVesselRepository(UnitOfWork(session))
    loaded = repository.get_by_id(vessel_id)
    assert loaded is not None
    return loaded


def test_technical_006_workflow_1_create_configuration_reload_verify_public_state(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    vessel_id = _create_vessel_prerequisite(stack)

    create_response = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    )

    assert isinstance(create_response.configuration.id, UUID)
    assert create_response.configuration.vessel_id == vessel_id
    assert create_response.configuration.components == ()

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_public = _reload_technical_public(reload_session, create_response.configuration.id)
        assert loaded_public.id == create_response.configuration.id
        assert loaded_public.vessel_id == vessel_id
        assert loaded_public.components == ()
    finally:
        reload_session.close()


def test_technical_006_workflow_2_add_install_component_reload_roundtrip(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    vessel_id = _create_vessel_prerequisite(stack)

    configuration_id = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    ).configuration.id

    add_response = stack.add_technical_component.execute(
        AddTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_type="PROPULSION_ENGINE",
            name="Main Engine",
            manufacturer="Generic Marine",
            model="ENG-1000",
            serial_number="ENG-001",
            specification_schema_key="ENGINE_V1",
            specification_entries=(
                SpecificationEntryInput(key="power_kw", value=2800, unit="kW"),
            ),
        )
    )

    component_id = next(
        item.id for item in add_response.configuration.components if item.name == "Main Engine"
    )

    stack.install_technical_component.execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 1, 10),
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_public = _reload_technical_public(reload_session, configuration_id)
        installed = next(item for item in loaded_public.components if item.id == component_id)

        assert installed.component_type == "PROPULSION_ENGINE"
        assert installed.name == "Main Engine"
        assert installed.manufacturer == "Generic Marine"
        assert installed.model == "ENG-1000"
        assert installed.status == "INSTALLED"
        assert installed.installed_date == date(2025, 1, 10)
        assert installed.removed_date is None
    finally:
        reload_session.close()


def test_technical_006_workflow_3_remove_component_preserves_history(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    vessel_id = _create_vessel_prerequisite(stack)
    configuration_id = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    ).configuration.id

    component_id = next(
        item.id
        for item in stack.add_technical_component.execute(
            AddTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_type="PUMP",
                name="Ballast Pump",
            )
        ).configuration.components
        if item.name == "Ballast Pump"
    )

    stack.install_technical_component.execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 2, 1),
        )
    )

    stack.remove_technical_component.execute(
        RemoveTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            removed_on=date(2025, 3, 1),
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_public = _reload_technical_public(reload_session, configuration_id)
        removed = next(item for item in loaded_public.components if item.id == component_id)

        assert removed.status == "REMOVED"
        assert removed.removed_date == date(2025, 3, 1)
        assert removed.installed_date == date(2025, 2, 1)
    finally:
        reload_session.close()


def test_technical_006_workflow_4_replace_component_roundtrip_keeps_historical_components(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    vessel_id = _create_vessel_prerequisite(stack)
    configuration_id = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    ).configuration.id

    add_response = stack.add_technical_component.execute(
        AddTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_type="GEARBOX",
            name="Component A",
            serial_number="GB-001",
        )
    )
    component_a_id = next(item.id for item in add_response.configuration.components if item.name == "Component A")

    stack.install_technical_component.execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_a_id,
            installed_on=date(2025, 1, 1),
        )
    )

    stack.replace_technical_component.execute(
        ReplaceTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_a_id,
            replaced_on=date(2025, 4, 1),
            reason="Wear",
            replacement_component_type="GEARBOX",
            replacement_name="Component B",
            replacement_serial_number="GB-002",
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_public = _reload_technical_public(reload_session, configuration_id)

        component_a = next(item for item in loaded_public.components if item.name == "Component A")
        component_b = next(item for item in loaded_public.components if item.name == "Component B")

        assert component_a.status == "REMOVED"
        assert component_a.removed_date == date(2025, 4, 1)
        assert component_a.replacement_successor_id == component_b.id

        assert component_b.status == "INSTALLED"
        assert component_b.installed_date == date(2025, 4, 1)

        assert len(loaded_public.replacement_history) == 1
        history = loaded_public.replacement_history[0]
        assert history.replaced_component_id == component_a.id
        assert history.replacement_component_id == component_b.id
    finally:
        reload_session.close()


def test_technical_006_workflow_5_update_component_details_keeps_identity_and_lifecycle(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    vessel_id = _create_vessel_prerequisite(stack)
    configuration_id = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    ).configuration.id

    component_id = next(
        item.id
        for item in stack.add_technical_component.execute(
            AddTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_type="GENERATOR",
                name="Aux Generator",
                serial_number="GEN-001",
            )
        ).configuration.components
        if item.name == "Aux Generator"
    )

    stack.install_technical_component.execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 1, 1),
        )
    )

    stack.update_technical_component_details.execute(
        UpdateTechnicalComponentDetailsRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            manufacturer="Updated Corp",
            model="GEN-900",
            specification_schema_key="GENERATOR_V1",
            specification_entries=(
                SpecificationEntryInput(key="rating_kw", value=400, unit="kW"),
            ),
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_public = _reload_technical_public(reload_session, configuration_id)
        component = next(item for item in loaded_public.components if item.id == component_id)

        assert component.manufacturer == "Updated Corp"
        assert component.model == "GEN-900"
        assert component.status == "INSTALLED"
        assert component.installed_date == date(2025, 1, 1)
    finally:
        reload_session.close()


def test_technical_006_workflow_6_propulsion_chain_roundtrip_public_state(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    vessel_id = _create_vessel_prerequisite(stack)
    configuration_id = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    ).configuration.id

    flow = [
        (
            "PROPULSION_ENGINE",
            "Propulsion Engine",
            "ENGINE_V1",
            (SpecificationEntryInput(key="power_kw", value=3000, unit="kW"),),
        ),
        (
            "GEARBOX",
            "Reversing Arrangement",
            "GEARBOX_V1",
            (SpecificationEntryInput(key="ratio", value=4.1),),
        ),
        (
            "SHAFT",
            "Main Shaft",
            "SHAFT_V1",
            (SpecificationEntryInput(key="diameter_mm", value=320, unit="mm"),),
        ),
        (
            "PROPELLER",
            "Controllable Pitch Propeller",
            "PROPELLER_V1",
            (SpecificationEntryInput(key="pitch_type", value="controllable"),),
        ),
    ]

    for component_type, name, schema, entries in flow:
        add_response = stack.add_technical_component.execute(
            AddTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_type=component_type,
                name=name,
                specification_schema_key=schema,
                specification_entries=entries,
            )
        )
        component_id = next(item.id for item in add_response.configuration.components if item.name == name)

        stack.install_technical_component.execute(
            InstallTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_id,
                installed_on=date(2025, 1, 1),
            )
        )

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_public = _reload_technical_public(reload_session, configuration_id)
        names = [item.name for item in loaded_public.components]
        statuses = {item.name: item.status for item in loaded_public.components}

        assert "Propulsion Engine" in names
        assert "Reversing Arrangement" in names
        assert "Main Shaft" in names
        assert "Controllable Pitch Propeller" in names

        assert statuses["Propulsion Engine"] == "INSTALLED"
        assert statuses["Reversing Arrangement"] == "INSTALLED"
        assert statuses["Main Shaft"] == "INSTALLED"
        assert statuses["Controllable Pitch Propeller"] == "INSTALLED"

        propeller = next(item for item in loaded_public.components if item.name == "Controllable Pitch Propeller")
        assert propeller.specification_schema_key == "PROPELLER_V1"
        assert any(entry.key == "pitch_type" and entry.value == "controllable" for entry in propeller.specification_entries)
    finally:
        reload_session.close()


def test_technical_006_workflow_7_historical_propulsion_replacement_keeps_other_chain_components(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    vessel_id = _create_vessel_prerequisite(stack)
    configuration_id = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    ).configuration.id

    def add_and_install(component_type: str, name: str) -> UUID:
        add_response = stack.add_technical_component.execute(
            AddTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_type=component_type,
                name=name,
            )
        )
        component_id = next(item.id for item in add_response.configuration.components if item.name == name)
        stack.install_technical_component.execute(
            InstallTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_id,
                installed_on=date(2025, 1, 1),
            )
        )
        return component_id

    engine_a_id = add_and_install("PROPULSION_ENGINE", "Engine A")
    _ = add_and_install("GEARBOX", "Gearbox")
    _ = add_and_install("SHAFT", "Shaft")
    _ = add_and_install("PROPELLER", "Propeller")

    stack.replace_technical_component.execute(
        ReplaceTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=engine_a_id,
            replaced_on=date(2025, 6, 1),
            reason="Upgrade",
            replacement_component_type="PROPULSION_ENGINE",
            replacement_name="Engine B",
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_public = _reload_technical_public(reload_session, configuration_id)

        engine_a = next(item for item in loaded_public.components if item.name == "Engine A")
        engine_b = next(item for item in loaded_public.components if item.name == "Engine B")
        gearbox = next(item for item in loaded_public.components if item.name == "Gearbox")
        shaft = next(item for item in loaded_public.components if item.name == "Shaft")
        propeller = next(item for item in loaded_public.components if item.name == "Propeller")

        assert engine_a.status == "REMOVED"
        assert engine_b.status == "INSTALLED"

        assert gearbox.status == "INSTALLED"
        assert shaft.status == "INSTALLED"
        assert propeller.status == "INSTALLED"

        assert len(loaded_public.replacement_history) == 1
    finally:
        reload_session.close()


def test_technical_006_workflow_8_asset_fleet_technical_boundary_integrity(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)

    asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-TC-{uuid4().hex[:6].upper()}",
            name="Boundary Asset",
            description="Boundary workflow",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Boundary Dock",
        )
    )

    vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Boundary Vessel",
            shipyard="Aalborg",
            build_year=2018,
            construction_material=VesselMaterial.OTHER,
            length=18.0,
            beam=5.1,
            draft=1.8,
            status=VesselStatus.ACTIVE,
        )
    )

    create_technical_response = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_response.vessel_id)
    )

    add_response = stack.add_technical_component.execute(
        AddTechnicalComponentRequest(
            configuration_id=create_technical_response.configuration.id,
            component_type="PUMP",
            name="Boundary Pump",
        )
    )
    pump_id = next(item.id for item in add_response.configuration.components if item.name == "Boundary Pump")

    stack.install_technical_component.execute(
        InstallTechnicalComponentRequest(
            configuration_id=create_technical_response.configuration.id,
            component_id=pump_id,
            installed_on=date(2025, 1, 1),
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_asset = _reload_asset(reload_session, asset_response.asset_id)
        loaded_vessel = _reload_vessel(reload_session, vessel_response.vessel_id)
        loaded_technical = _reload_technical_public(
            reload_session,
            create_technical_response.configuration.id,
        )

        assert loaded_asset.id.value == asset_response.asset_id
        assert loaded_vessel.id.value == vessel_response.vessel_id
        assert loaded_technical.vessel_id == vessel_response.vessel_id

        assert isinstance(loaded_asset, Asset)
        assert isinstance(loaded_vessel, Vessel)

        assert loaded_vessel.asset_id == loaded_asset.id.value
        assert all(item.component_type != "VESSEL" for item in loaded_technical.components)
    finally:
        reload_session.close()


def test_technical_006_failure_workflow_invalid_lifecycle_rolls_back_and_keeps_db_state(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    vessel_id = _create_vessel_prerequisite(stack)
    configuration_id = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    ).configuration.id

    component_id = next(
        item.id
        for item in stack.add_technical_component.execute(
            AddTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_type="PUMP",
                name="Lifecycle Pump",
            )
        ).configuration.components
        if item.name == "Lifecycle Pump"
    )

    stack.install_technical_component.execute(
        InstallTechnicalComponentRequest(
            configuration_id=configuration_id,
            component_id=component_id,
            installed_on=date(2025, 1, 1),
        )
    )

    with pytest.raises(TechnicalBusinessRuleViolation):
        stack.install_technical_component.execute(
            InstallTechnicalComponentRequest(
                configuration_id=configuration_id,
                component_id=component_id,
                installed_on=date(2025, 1, 2),
            )
        )

    reload_session = Session(sqlite_session.get_bind())
    try:
        loaded_public = _reload_technical_public(reload_session, configuration_id)
        pump = next(item for item in loaded_public.components if item.id == component_id)

        assert pump.status == "INSTALLED"
        assert pump.installed_date == date(2025, 1, 1)
        assert pump.removed_date is None
        assert loaded_public.replacement_history == ()
    finally:
        reload_session.close()
