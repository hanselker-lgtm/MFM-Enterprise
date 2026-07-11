from __future__ import annotations

from dataclasses import dataclass
from dataclasses import fields
from dataclasses import is_dataclass
from datetime import date
from datetime import datetime
from pathlib import Path
from typing import Any
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
from mfm.application.features.maintenance.add_maintenance_requirement_feature import (
    AddMaintenanceRequirementFeature,
)
from mfm.application.features.maintenance.add_maintenance_requirement_feature import (
    AddMaintenanceRequirementRequest,
)
from mfm.application.features.maintenance.calculate_due_maintenance_feature import (
    CalculateDueMaintenanceFeature,
)
from mfm.application.features.maintenance.calculate_due_maintenance_feature import (
    CalculateDueMaintenanceRequest,
)
from mfm.application.features.maintenance.complete_work_order_feature import (
    CompleteWorkOrderFeature,
)
from mfm.application.features.maintenance.complete_work_order_feature import (
    CompleteWorkOrderRequest,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    BusinessRuleViolation as MaintenanceBusinessRuleViolation,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    CreateMaintenancePlanFeature,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    CreateMaintenancePlanRequest,
)
from mfm.application.features.maintenance.create_work_order_feature import (
    CreateWorkOrderFeature,
)
from mfm.application.features.maintenance.create_work_order_feature import (
    CreateWorkOrderRequest,
)
from mfm.application.features.maintenance.get_maintenance_history_feature import (
    GetMaintenanceHistoryFeature,
)
from mfm.application.features.maintenance.get_maintenance_history_feature import (
    GetMaintenanceHistoryRequest,
)
from mfm.application.features.maintenance.open_work_order_feature import (
    OpenWorkOrderFeature,
)
from mfm.application.features.maintenance.open_work_order_feature import (
    OpenWorkOrderRequest,
)
from mfm.application.features.maintenance.start_work_order_feature import (
    StartWorkOrderFeature,
)
from mfm.application.features.maintenance.start_work_order_feature import (
    StartWorkOrderRequest,
)
from mfm.application.features.maintenance.update_maintenance_requirement_feature import (
    UpdateMaintenanceRequirementFeature,
)
from mfm.application.features.maintenance.update_maintenance_requirement_feature import (
    UpdateMaintenanceRequirementRequest,
)
from mfm.application.features.technical_configuration.add_technical_component_feature import (
    AddTechnicalComponentFeature,
)
from mfm.application.features.technical_configuration.add_technical_component_feature import (
    AddTechnicalComponentRequest,
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
from mfm.application.fleet.create_vessel import CreateVesselUseCase
from mfm.application.maintenance.add_maintenance_requirement import (
    AddMaintenanceRequirementUseCase,
)
from mfm.application.maintenance.calculate_due_maintenance import (
    CalculateDueMaintenanceUseCase,
)
from mfm.application.maintenance.complete_work_order import CompleteWorkOrderUseCase
from mfm.application.maintenance.create_maintenance_plan import CreateMaintenancePlanUseCase
from mfm.application.maintenance.create_work_order import CreateWorkOrderUseCase
from mfm.application.maintenance.get_maintenance_history import GetMaintenanceHistoryUseCase
from mfm.application.maintenance.open_work_order import OpenWorkOrderUseCase
from mfm.application.maintenance.start_work_order import StartWorkOrderUseCase
from mfm.application.maintenance.update_maintenance_requirement import (
    UpdateMaintenanceRequirementUseCase,
)
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
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.database.models.maintenance_plan_model import MaintenancePlanModel  # noqa: F401
from mfm.database.models.maintenance_record_model import MaintenanceRecordModel  # noqa: F401
from mfm.database.models.maintenance_requirement_model import (  # noqa: F401
    MaintenanceRequirementModel,
)
from mfm.database.models.technical_component_link_model import (  # noqa: F401
    TechnicalComponentLinkModel,
)
from mfm.database.models.technical_component_model import TechnicalComponentModel  # noqa: F401
from mfm.database.models.technical_component_replacement_model import (  # noqa: F401
    TechnicalComponentReplacementModel,
)
from mfm.database.models.technical_configuration_model import (  # noqa: F401
    TechnicalConfigurationModel,
)
from mfm.database.models.vessel_dimensions_model import VesselDimensionsModel  # noqa: F401
from mfm.database.models.vessel_model import VesselModel  # noqa: F401
from mfm.database.models.work_order_model import WorkOrderModel  # noqa: F401
from mfm.domain.asset.asset import Asset
from mfm.domain.asset.asset_category import AssetCategory
from mfm.domain.fleet.vessel import Vessel
from mfm.domain.fleet.vessel_material import VesselMaterial
from mfm.domain.fleet.vessel_status import VesselStatus
from mfm.infrastructure.persistence.sqlite.sqlite_asset_repository import SQLiteAssetRepository
from mfm.infrastructure.persistence.sqlite.sqlite_maintenance_plan_repository import (
    SQLiteMaintenancePlanRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_technical_configuration_repository import (
    SQLiteTechnicalConfigurationRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_vessel_repository import SQLiteVesselRepository
from mfm.infrastructure.persistence.sqlite.sqlite_work_order_repository import (
    SQLiteWorkOrderRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SqliteMaintenanceEndToEndUnitOfWork(AbstractUnitOfWork):
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
        self.maintenance_plan_repository = SQLiteMaintenancePlanRepository(
            self._persistence_uow
        )
        self.work_order_repository = SQLiteWorkOrderRepository(self._persistence_uow)

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
    create_plan: CreateMaintenancePlanFeature
    add_requirement: AddMaintenanceRequirementFeature
    update_requirement: UpdateMaintenanceRequirementFeature
    calculate_due: CalculateDueMaintenanceFeature
    create_work_order: CreateWorkOrderFeature
    open_work_order: OpenWorkOrderFeature
    start_work_order: StartWorkOrderFeature
    complete_work_order: CompleteWorkOrderFeature
    history: GetMaintenanceHistoryFeature


@pytest.fixture(autouse=True)
def clear_domain_registries() -> None:
    Asset._clear_registry_for_tests()
    Vessel._clear_registry_for_tests()


@pytest.fixture()
def sqlite_session(tmp_path: Path) -> Session:
    db_path = tmp_path / "maintenance-006.sqlite"
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
    app_uow = SqliteMaintenanceEndToEndUnitOfWork(session)

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
        create_plan=CreateMaintenancePlanFeature(
            service=CreateMaintenancePlanUseCase(unit_of_work=app_uow)
        ),
        add_requirement=AddMaintenanceRequirementFeature(
            service=AddMaintenanceRequirementUseCase(unit_of_work=app_uow)
        ),
        update_requirement=UpdateMaintenanceRequirementFeature(
            service=UpdateMaintenanceRequirementUseCase(unit_of_work=app_uow)
        ),
        calculate_due=CalculateDueMaintenanceFeature(
            service=CalculateDueMaintenanceUseCase(unit_of_work=app_uow)
        ),
        create_work_order=CreateWorkOrderFeature(
            service=CreateWorkOrderUseCase(unit_of_work=app_uow)
        ),
        open_work_order=OpenWorkOrderFeature(
            service=OpenWorkOrderUseCase(unit_of_work=app_uow)
        ),
        start_work_order=StartWorkOrderFeature(
            service=StartWorkOrderUseCase(unit_of_work=app_uow)
        ),
        complete_work_order=CompleteWorkOrderFeature(
            service=CompleteWorkOrderUseCase(unit_of_work=app_uow)
        ),
        history=GetMaintenanceHistoryFeature(
            service=GetMaintenanceHistoryUseCase(unit_of_work=app_uow)
        ),
    )


def _dt(year: int, month: int, day: int, hour: int, minute: int = 0) -> datetime:
    return datetime(year, month, day, hour, minute)


def _create_asset_and_vessel(stack: FeatureStack) -> tuple[UUID, UUID]:
    asset_response = stack.create_asset.execute(
        CreateAssetRequest(
            asset_number=f"ASSET-MAINT-{uuid4().hex[:6].upper()}",
            name="Maintenance Integration Asset",
            description="Asset prerequisite for maintenance workflows",
            category=AssetCategory.EQUIPMENT,
            owner_id=None,
            location="Harbor Integration",
        )
    )

    vessel_response = stack.create_vessel.execute(
        CreateVesselRequest(
            asset_id=asset_response.asset_id,
            registration=f"OY-{uuid4().hex[:6].upper()}",
            name="Maintenance Integration Vessel",
            shipyard="Odense Yard",
            build_year=2020,
            construction_material=VesselMaterial.STEEL,
            length=25.1,
            beam=6.1,
            draft=2.2,
            status=VesselStatus.ACTIVE,
        )
    )

    return asset_response.asset_id, vessel_response.vessel_id


def _create_installed_component(
    stack: FeatureStack,
    *,
    vessel_id: UUID,
    component_type: str,
    component_name: str,
) -> tuple[UUID, UUID, TechnicalConfigurationResponse]:
    config_id = stack.create_technical_configuration.execute(
        CreateTechnicalConfigurationRequest(vessel_id=vessel_id)
    ).configuration.id

    add_response = stack.add_technical_component.execute(
        AddTechnicalComponentRequest(
            configuration_id=config_id,
            component_type=component_type,
            name=component_name,
            manufacturer="Generic Marine",
            model="GEN-100",
            serial_number=f"SN-{uuid4().hex[:8].upper()}",
            specification_schema_key="GENERIC_V1",
        )
    )
    component_id = next(
        item.id
        for item in add_response.configuration.components
        if item.name == component_name
    )

    install_response = stack.install_technical_component.execute(
        InstallTechnicalComponentRequest(
            configuration_id=config_id,
            component_id=component_id,
            installed_on=date(2027, 1, 10),
        )
    )

    return config_id, component_id, install_response.configuration


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


def _reload_technical_public(
    session: Session,
    configuration_id: UUID,
) -> TechnicalConfigurationResponse:
    repository = SQLiteTechnicalConfigurationRepository(UnitOfWork(session))
    configuration = repository.get_by_id(configuration_id)
    assert configuration is not None
    return to_feature_configuration_response(
        to_application_configuration_response(configuration)
    )


def _reload_work_order_status(session: Session, work_order_id: UUID) -> tuple[str, Any]:
    repository = SQLiteWorkOrderRepository(UnitOfWork(session))
    loaded = repository.get_by_id(work_order_id)
    assert loaded is not None
    return loaded.status.value, loaded.maintenance_record


def _assert_no_domain_or_persistence_leakage(value: Any) -> None:
    if value is None:
        return

    value_module = value.__class__.__module__
    assert not value_module.startswith("mfm.domain")
    assert not value_module.startswith("mfm.database.models")

    if is_dataclass(value):
        for item in fields(value):
            _assert_no_domain_or_persistence_leakage(getattr(value, item.name))
        return

    if isinstance(value, tuple | list):
        for item in value:
            _assert_no_domain_or_persistence_leakage(item)
        return

    if isinstance(value, dict):
        for key, item in value.items():
            _assert_no_domain_or_persistence_leakage(key)
            _assert_no_domain_or_persistence_leakage(item)


def test_maint_006_workflow_1_vessel_maintenance_plan(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    _, vessel_id = _create_asset_and_vessel(stack)

    created = stack.create_plan.execute(
        CreateMaintenancePlanRequest(target_type="VESSEL", target_id=vessel_id)
    )
    updated = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=created.plan.id,
            title="Hull planking inspection",
            description="Inspect external hull planking",
            maintenance_type="INSPECTION",
            interval_type="CALENDAR_YEARS",
            interval_value=1,
            due_basis="CALENDAR_DATE",
            instructions="Use visual and sounding hammer inspection",
            notes="Document findings in survey log",
        )
    )

    assert updated.plan.id == created.plan.id
    assert updated.plan.target.target_type == "VESSEL"
    assert updated.plan.target.target_id == vessel_id
    requirement = updated.plan.requirements[0]
    assert requirement.maintenance_type == "INSPECTION"
    assert requirement.interval.interval_type == "CALENDAR_YEARS"
    assert requirement.interval.interval_value == 1
    assert requirement.instructions == "Use visual and sounding hammer inspection"
    assert requirement.notes == "Document findings in survey log"

    reload_session = Session(sqlite_session.get_bind())
    try:
        reload_stack = _build_stack(reload_session)
        history = reload_stack.history.execute(
            GetMaintenanceHistoryRequest(target_type="VESSEL", target_id=vessel_id)
        )

        assert len(history.plans) == 1
        plan = history.plans[0]
        assert plan.id == created.plan.id
        assert plan.target.target_type == "VESSEL"
        assert plan.target.target_id == vessel_id
        assert len(plan.requirements) == 1
        assert plan.requirements[0].id == requirement.id
        assert plan.requirements[0].instructions == requirement.instructions
        assert plan.requirements[0].notes == requirement.notes

        _assert_no_domain_or_persistence_leakage(plan)
        _assert_no_domain_or_persistence_leakage(history)
    finally:
        reload_session.close()


def test_maint_006_workflow_2_technical_component_maintenance(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    _, vessel_id = _create_asset_and_vessel(stack)
    configuration_id, component_id, technical_before = _create_installed_component(
        stack,
        vessel_id=vessel_id,
        component_type="PROPULSION_ENGINE",
        component_name="Main Engine A",
    )

    component_before = next(
        item for item in technical_before.components if item.id == component_id
    )

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(
            target_type="TECHNICAL_COMPONENT",
            target_id=component_id,
        )
    )
    stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Engine lubrication task",
            description="Lubricate engine parts",
            maintenance_type="PREVENTIVE",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
            instructions="Use OEM-approved lubrication procedure",
            notes="No component mutation expected",
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        technical_after = _reload_technical_public(reload_session, configuration_id)
        component_after = next(
            item for item in technical_after.components if item.id == component_id
        )

        assert technical_after.id == configuration_id
        assert technical_after.vessel_id == vessel_id
        assert component_after == component_before

        reload_stack = _build_stack(reload_session)
        history = reload_stack.history.execute(
            GetMaintenanceHistoryRequest(
                target_type="TECHNICAL_COMPONENT",
                target_id=component_id,
            )
        )
        assert len(history.plans) == 1
        assert history.plans[0].target.target_id == component_id
        assert len(history.records) == 0

        _assert_no_domain_or_persistence_leakage(history)
    finally:
        reload_session.close()


def test_maint_006_workflow_3_due_maintenance(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    target_id = uuid4()

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(
            target_type="TECHNICAL_COMPONENT",
            target_id=target_id,
        )
    )

    calendar_requirement = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Calendar-based inspection",
            description="Periodic inspection",
            maintenance_type="INSPECTION",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
        )
    ).plan.requirements[0]

    running_hours_requirement = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Running-hour oil check",
            description="Running-hour based oil check",
            maintenance_type="PREVENTIVE",
            interval_type="RUNNING_HOURS",
            interval_value=250,
            due_basis="RUNNING_HOURS",
        )
    ).plan.requirements[1]

    result_a = stack.calculate_due.execute(
        CalculateDueMaintenanceRequest(
            maintenance_plan_id=plan.plan.id,
            as_of_date=date(2027, 1, 1),
            running_hours_by_requirement_id={running_hours_requirement.id: 100},
        )
    )
    result_b = stack.calculate_due.execute(
        CalculateDueMaintenanceRequest(
            maintenance_plan_id=plan.plan.id,
            as_of_date=date(2027, 1, 1),
            running_hours_by_requirement_id={running_hours_requirement.id: 100},
        )
    )

    assert calendar_requirement.id != running_hours_requirement.id
    assert result_a.due_requirements == ()
    assert result_b.due_requirements == result_a.due_requirements
    _assert_no_domain_or_persistence_leakage(result_a)


def test_maint_006_workflow_4_complete_work_order(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    _, vessel_id = _create_asset_and_vessel(stack)

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(target_type="VESSEL", target_id=vessel_id)
    )
    requirement_id = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Deck maintenance",
            description="Maintain vessel deck",
            maintenance_type="PREVENTIVE",
            interval_type="CALENDAR_MONTHS",
            interval_value=6,
            due_basis="CALENDAR_DATE",
            instructions="Prepare deck and apply treatment",
        )
    ).plan.requirements[0].id

    created_work_order = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-DECK-001",
            description="Perform deck treatment",
        )
    )
    opened = stack.open_work_order.execute(
        OpenWorkOrderRequest(work_order_id=created_work_order.work_order.id)
    )
    started = stack.start_work_order.execute(
        StartWorkOrderRequest(
            work_order_id=created_work_order.work_order.id,
            started_at=_dt(2027, 3, 1, 8),
        )
    )
    completed = stack.complete_work_order.execute(
        CompleteWorkOrderRequest(
            work_order_id=created_work_order.work_order.id,
            completed_at=_dt(2027, 3, 1, 11),
            performer_type="MEMBER",
            performer_id_or_external_key="member-42",
            performer_display_name_snapshot="Maintenance Member",
            notes="Deck treatment completed",
            finding="No structural damage",
        )
    )

    assert opened.work_order.status == "OPEN"
    assert started.work_order.status == "IN_PROGRESS"
    assert completed.work_order.status == "COMPLETED"
    assert completed.work_order.started_at == _dt(2027, 3, 1, 8)
    assert completed.work_order.completed_at == _dt(2027, 3, 1, 11)
    assert completed.work_order.maintenance_record is not None
    assert completed.work_order.maintenance_record.notes == "Deck treatment completed"

    reload_session = Session(sqlite_session.get_bind())
    try:
        persisted_status, persisted_record = _reload_work_order_status(
            reload_session,
            created_work_order.work_order.id,
        )
        assert persisted_status == "COMPLETED"
        assert persisted_record is not None

        history = _build_stack(reload_session).history.execute(
            GetMaintenanceHistoryRequest(target_type="VESSEL", target_id=vessel_id)
        )
        assert len(history.records) == 1
        assert history.records[0].work_order_id == created_work_order.work_order.id
        assert history.records[0].completed_at == _dt(2027, 3, 1, 11)

        _assert_no_domain_or_persistence_leakage(completed)
        _assert_no_domain_or_persistence_leakage(history)
    finally:
        reload_session.close()


def test_maint_006_workflow_5_permanent_historical_snapshot(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    _, vessel_id = _create_asset_and_vessel(stack)

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(target_type="VESSEL", target_id=vessel_id)
    )
    requirement_id = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Oil maintenance",
            description="Maintain oil system",
            maintenance_type="PREVENTIVE",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
            instructions="instruction A",
            notes="context A",
        )
    ).plan.requirements[0].id

    work_a = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-A",
            description="Maintenance run A",
        )
    )
    stack.open_work_order.execute(OpenWorkOrderRequest(work_order_id=work_a.work_order.id))
    stack.start_work_order.execute(
        StartWorkOrderRequest(work_order_id=work_a.work_order.id, started_at=_dt(2027, 5, 1, 8))
    )
    stack.complete_work_order.execute(
        CompleteWorkOrderRequest(
            work_order_id=work_a.work_order.id,
            completed_at=_dt(2027, 5, 1, 12),
            notes="instruction A",
            finding="finding A",
        )
    )

    reload_session_a = Session(sqlite_session.get_bind())
    try:
        history_a = _build_stack(reload_session_a).history.execute(
            GetMaintenanceHistoryRequest(target_type="VESSEL", target_id=vessel_id)
        )
        assert len(history_a.records) == 1
        assert history_a.records[0].work_order_id == work_a.work_order.id
        assert history_a.records[0].notes == "instruction A"
        assert history_a.records[0].finding == "finding A"
    finally:
        reload_session_a.close()

    stack.update_requirement.execute(
        UpdateMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            instructions="instruction B",
            interval_type="CALENDAR_MONTHS",
            interval_value=6,
            notes="context B",
        )
    )

    reload_session_b = Session(sqlite_session.get_bind())
    try:
        history_after_update = _build_stack(reload_session_b).history.execute(
            GetMaintenanceHistoryRequest(target_type="VESSEL", target_id=vessel_id)
        )
        assert history_after_update.plans[0].requirements[0].instructions == "instruction B"
        assert (
            history_after_update.plans[0].requirements[0].interval.interval_value == 6
        )
    finally:
        reload_session_b.close()

    work_b = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-B",
            description="Maintenance run B",
        )
    )
    stack.open_work_order.execute(OpenWorkOrderRequest(work_order_id=work_b.work_order.id))
    stack.start_work_order.execute(
        StartWorkOrderRequest(work_order_id=work_b.work_order.id, started_at=_dt(2028, 5, 1, 8))
    )
    stack.complete_work_order.execute(
        CompleteWorkOrderRequest(
            work_order_id=work_b.work_order.id,
            completed_at=_dt(2028, 5, 1, 11),
            notes="instruction B",
            finding="finding B",
        )
    )

    reload_session_final = Session(sqlite_session.get_bind())
    try:
        history = _build_stack(reload_session_final).history.execute(
            GetMaintenanceHistoryRequest(target_type="VESSEL", target_id=vessel_id)
        )
        assert len(history.records) == 2

        record_a = history.records[0]
        record_b = history.records[1]

        assert record_a.work_order_id == work_a.work_order.id
        assert record_a.notes == "instruction A"
        assert record_a.finding == "finding A"
        assert record_a.completed_at == _dt(2027, 5, 1, 12)

        assert record_b.work_order_id == work_b.work_order.id
        assert record_b.notes == "instruction B"
        assert record_b.finding == "finding B"
        assert record_b.completed_at == _dt(2028, 5, 1, 11)

        current_requirement = history.plans[0].requirements[0]
        assert current_requirement.instructions == "instruction B"
        assert current_requirement.interval.interval_value == 6

        assert record_a.notes != current_requirement.instructions
        assert record_b.notes == current_requirement.instructions

        _assert_no_domain_or_persistence_leakage(history)
    finally:
        reload_session_final.close()


def test_maint_006_workflow_6_propulsion_engine_maintenance(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    _, vessel_id = _create_asset_and_vessel(stack)
    configuration_id, component_id, technical_before = _create_installed_component(
        stack,
        vessel_id=vessel_id,
        component_type="PROPULSION_ENGINE",
        component_name="Propulsion Engine",
    )

    component_before = next(
        item for item in technical_before.components if item.id == component_id
    )

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(
            target_type="TECHNICAL_COMPONENT",
            target_id=component_id,
        )
    )
    requirement_id = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Change lubricating oil",
            description="Lubricating oil replacement",
            maintenance_type="PREVENTIVE",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
            instructions="Use approved marine lubricant",
        )
    ).plan.requirements[0].id

    due = stack.calculate_due.execute(
        CalculateDueMaintenanceRequest(
            maintenance_plan_id=plan.plan.id,
            as_of_date=date(2027, 7, 1),
        )
    )
    assert due.due_requirements == ()

    work = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-PROP-001",
            description="Propulsion oil replacement",
        )
    )
    stack.open_work_order.execute(OpenWorkOrderRequest(work_order_id=work.work_order.id))
    stack.start_work_order.execute(
        StartWorkOrderRequest(work_order_id=work.work_order.id, started_at=_dt(2027, 7, 2, 9))
    )
    stack.complete_work_order.execute(
        CompleteWorkOrderRequest(
            work_order_id=work.work_order.id,
            completed_at=_dt(2027, 7, 2, 13),
            notes="Oil successfully changed",
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        history = _build_stack(reload_session).history.execute(
            GetMaintenanceHistoryRequest(
                target_type="TECHNICAL_COMPONENT",
                target_id=component_id,
            )
        )
        technical_after = _reload_technical_public(reload_session, configuration_id)
        component_after = next(
            item for item in technical_after.components if item.id == component_id
        )

        assert len(history.records) == 1
        assert history.records[0].target_id == component_id
        assert component_after == component_before

        _assert_no_domain_or_persistence_leakage(history)
    finally:
        reload_session.close()


def test_maint_006_workflow_7_pitch_propeller_inspection_finding(
    sqlite_session: Session,
) -> None:
    stack = _build_stack(sqlite_session)
    _, vessel_id = _create_asset_and_vessel(stack)
    configuration_id, component_id, _ = _create_installed_component(
        stack,
        vessel_id=vessel_id,
        component_type="PROPELLER",
        component_name="CPP Unit",
    )

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(
            target_type="TECHNICAL_COMPONENT",
            target_id=component_id,
        )
    )
    requirement_id = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Pitch propeller inspection",
            description="Inspect CPP blade and pitch mechanism",
            maintenance_type="INSPECTION",
            interval_type="CALENDAR_YEARS",
            interval_value=1,
            due_basis="CALENDAR_DATE",
            instructions="Inspect blade edges and hub movement",
        )
    ).plan.requirements[0].id

    work = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-CPP-001",
            description="CPP inspection",
        )
    )
    stack.open_work_order.execute(OpenWorkOrderRequest(work_order_id=work.work_order.id))
    stack.start_work_order.execute(
        StartWorkOrderRequest(work_order_id=work.work_order.id, started_at=_dt(2027, 8, 10, 8))
    )
    completed = stack.complete_work_order.execute(
        CompleteWorkOrderRequest(
            work_order_id=work.work_order.id,
            completed_at=_dt(2027, 8, 10, 11),
            finding="possible replacement required",
            replacement_may_be_required=True,
            notes="CPP finding captured",
        )
    )

    assert completed.work_order.maintenance_record is not None
    assert (
        completed.work_order.maintenance_record.finding
        == "possible replacement required"
    )
    assert completed.work_order.maintenance_record.replacement_may_be_required is True

    reload_session = Session(sqlite_session.get_bind())
    try:
        history = _build_stack(reload_session).history.execute(
            GetMaintenanceHistoryRequest(
                target_type="TECHNICAL_COMPONENT",
                target_id=component_id,
            )
        )
        technical_after = _reload_technical_public(reload_session, configuration_id)
        component_after = next(
            item for item in technical_after.components if item.id == component_id
        )

        assert len(history.records) == 1
        assert history.records[0].finding == "possible replacement required"
        assert history.records[0].replacement_may_be_required is True

        assert component_after.replacement_successor_id is None
        assert technical_after.replacement_history == ()
    finally:
        reload_session.close()


def test_maint_006_workflow_8_vessel_hull_inspection(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    _, vessel_id = _create_asset_and_vessel(stack)

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(target_type="VESSEL", target_id=vessel_id)
    )
    requirement_id = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Hull planking inspection",
            description="Inspect vessel hull planking",
            maintenance_type="INSPECTION",
            interval_type="CALENDAR_YEARS",
            interval_value=1,
            due_basis="CALENDAR_DATE",
        )
    ).plan.requirements[0].id

    work = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-HULL-001",
            description="Hull inspection workflow",
        )
    )
    stack.open_work_order.execute(OpenWorkOrderRequest(work_order_id=work.work_order.id))
    stack.start_work_order.execute(
        StartWorkOrderRequest(work_order_id=work.work_order.id, started_at=_dt(2027, 9, 15, 9))
    )
    stack.complete_work_order.execute(
        CompleteWorkOrderRequest(
            work_order_id=work.work_order.id,
            completed_at=_dt(2027, 9, 15, 12),
            notes="Hull inspection completed",
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        history = _build_stack(reload_session).history.execute(
            GetMaintenanceHistoryRequest(target_type="VESSEL", target_id=vessel_id)
        )
        assert len(history.records) == 1
        assert history.records[0].work_order_id == work.work_order.id
        assert history.records[0].target_type == "VESSEL"
        assert history.records[0].target_id == vessel_id
    finally:
        reload_session.close()


def test_maint_006_workflow_9_failure_and_rollback(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    _, vessel_id = _create_asset_and_vessel(stack)

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(target_type="VESSEL", target_id=vessel_id)
    )
    requirement_id = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Rollback validation task",
            description="Task for rollback validation",
            maintenance_type="INSPECTION",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
        )
    ).plan.requirements[0].id

    baseline = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-BASELINE",
            description="Baseline completed work",
        )
    )
    stack.open_work_order.execute(OpenWorkOrderRequest(work_order_id=baseline.work_order.id))
    stack.start_work_order.execute(
        StartWorkOrderRequest(work_order_id=baseline.work_order.id, started_at=_dt(2027, 10, 1, 8))
    )
    stack.complete_work_order.execute(
        CompleteWorkOrderRequest(
            work_order_id=baseline.work_order.id,
            completed_at=_dt(2027, 10, 1, 10),
            notes="baseline completion",
        )
    )

    invalid = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-INVALID",
            description="Invalid completion attempt",
        )
    )

    with pytest.raises(MaintenanceBusinessRuleViolation):
        stack.complete_work_order.execute(
            CompleteWorkOrderRequest(
                work_order_id=invalid.work_order.id,
                completed_at=_dt(2027, 10, 2, 10),
                notes="should fail",
            )
        )

    reload_session = Session(sqlite_session.get_bind())
    try:
        status, record = _reload_work_order_status(reload_session, invalid.work_order.id)
        assert status == "PLANNED"
        assert record is None

        history = _build_stack(reload_session).history.execute(
            GetMaintenanceHistoryRequest(target_type="VESSEL", target_id=vessel_id)
        )
        assert len(history.records) == 1
        assert history.records[0].work_order_id == baseline.work_order.id
    finally:
        reload_session.close()


def test_maint_006_workflow_10_capability_boundaries(sqlite_session: Session) -> None:
    stack = _build_stack(sqlite_session)
    asset_id, vessel_id = _create_asset_and_vessel(stack)
    configuration_id, component_id, technical_before = _create_installed_component(
        stack,
        vessel_id=vessel_id,
        component_type="PUMP",
        component_name="Sea Water Pump",
    )

    asset_before = _reload_asset(sqlite_session, asset_id)
    vessel_before = _reload_vessel(sqlite_session, vessel_id)
    component_before = next(
        item for item in technical_before.components if item.id == component_id
    )

    plan = stack.create_plan.execute(
        CreateMaintenancePlanRequest(
            target_type="TECHNICAL_COMPONENT",
            target_id=component_id,
        )
    )
    requirement_id = stack.add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=plan.plan.id,
            title="Pump maintenance",
            description="Maintain sea water pump",
            maintenance_type="PREVENTIVE",
            interval_type="CALENDAR_MONTHS",
            interval_value=6,
            due_basis="CALENDAR_DATE",
            instructions="Inspect impeller and seals",
        )
    ).plan.requirements[0].id
    work = stack.create_work_order.execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-PUMP-001",
            description="Pump maintenance execution",
        )
    )
    stack.open_work_order.execute(OpenWorkOrderRequest(work_order_id=work.work_order.id))
    stack.start_work_order.execute(
        StartWorkOrderRequest(work_order_id=work.work_order.id, started_at=_dt(2027, 11, 1, 9))
    )
    stack.complete_work_order.execute(
        CompleteWorkOrderRequest(
            work_order_id=work.work_order.id,
            completed_at=_dt(2027, 11, 1, 12),
            notes="Pump maintenance completed",
        )
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        asset_after = _reload_asset(reload_session, asset_id)
        vessel_after = _reload_vessel(reload_session, vessel_id)
        technical_after = _reload_technical_public(reload_session, configuration_id)
        component_after = next(
            item for item in technical_after.components if item.id == component_id
        )

        history = _build_stack(reload_session).history.execute(
            GetMaintenanceHistoryRequest(
                target_type="TECHNICAL_COMPONENT",
                target_id=component_id,
            )
        )

        assert asset_after.id == asset_before.id
        assert asset_after.asset_number == asset_before.asset_number
        assert asset_after.name == asset_before.name

        assert vessel_after.id == vessel_before.id
        assert vessel_after.asset_id == vessel_before.asset_id
        assert vessel_after.registration == vessel_before.registration
        assert vessel_after.name == vessel_before.name

        assert component_after == component_before
        assert technical_after.replacement_history == ()

        assert len(history.plans) == 1
        assert history.plans[0].target.target_id == component_id
        assert len(history.records) == 1
        assert history.records[0].target_id == component_id

        _assert_no_domain_or_persistence_leakage(history)
    finally:
        reload_session.close()