from __future__ import annotations

from datetime import date
from datetime import datetime
from datetime import timezone
from pathlib import Path
import weakref
from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import mfm.database.models  # noqa: F401
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.maintenance.maintenance_due_basis import MaintenanceDueBasis
from mfm.domain.maintenance.maintenance_interval import MaintenanceInterval
from mfm.domain.maintenance.maintenance_interval_type import MaintenanceIntervalType
from mfm.domain.maintenance.maintenance_plan import MaintenancePlan
from mfm.domain.maintenance.maintenance_requirement import MaintenanceRequirement
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType
from mfm.domain.maintenance.maintenance_type import MaintenanceType
from mfm.domain.maintenance.performer_reference import PerformerReference
from mfm.domain.maintenance.performer_reference_type import PerformerReferenceType
from mfm.domain.maintenance.work_order import WorkOrder
from mfm.domain.maintenance.work_order_status import WorkOrderStatus
from mfm.infrastructure.persistence.sqlite.sqlite_maintenance_plan_repository import (
    SQLiteMaintenancePlanRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_work_order_repository import (
    SQLiteWorkOrderRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


def _utc(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, tzinfo=timezone.utc)


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    session = Session(engine)
    weakref.finalize(session, engine.dispose)
    return session


def _build_plan(target: MaintenanceTarget) -> MaintenancePlan:
    plan = MaintenancePlan(maintenance_target=target)

    yearly_requirement = MaintenanceRequirement(
        id=uuid4(),
        title="Main oil service",
        description="Service lubrication system",
        maintenance_target=target,
        maintenance_type=MaintenanceType.PREVENTIVE,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
            interval_value=12,
        ),
        due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        instructions="Inspect and lubricate",
        notes="Primary interval",
    )
    yearly_requirement.record_completion(completed_on=date(2028, 1, 1))

    runtime_requirement = MaintenanceRequirement(
        id=uuid4(),
        title="Runtime condition check",
        description="Check based on running hours",
        maintenance_target=target,
        maintenance_type=MaintenanceType.CONDITION_BASED,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.RUNNING_HOURS,
            interval_value=300,
        ),
        due_basis=MaintenanceDueBasis.RUNNING_HOURS,
        instructions="Read hour meter",
    )
    runtime_requirement.record_completion(completed_running_hours=5000)

    plan.add_requirement(yearly_requirement)
    plan.add_requirement(runtime_requirement)
    return plan


def _build_completed_work_order(
    *,
    target: MaintenanceTarget,
    requirement_id: UUID,
    title: str,
    finding: str | None,
    replacement: bool,
) -> WorkOrder:
    performer = PerformerReference(
        performer_type=PerformerReferenceType.MEMBER,
        performer_id_or_external_key="member-42",
        display_name_snapshot="Member Forty Two",
    )

    work_order = WorkOrder(
        maintenance_target=target,
        maintenance_requirement_id=requirement_id,
        title=title,
        description=f"Execute {title}",
        planned_date=date(2028, 2, 1),
    )
    work_order.open()
    work_order.start(_utc(2028, 2, 1, 9))
    work_order.complete(
        completed_at=_utc(2028, 2, 1, 11),
        performed_by=performer,
        notes=f"Completed {title}",
        finding=finding,
        replacement_may_be_required=replacement,
    )
    return work_order


def test_maintenance_plan_repository_crud_and_roundtrip(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "maint-plan-crud")
    try:
        plan_target = MaintenanceTarget(
            target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
            target_id=uuid4(),
        )

        plan_repository = SQLiteMaintenancePlanRepository(UnitOfWork(session))
        plan = _build_plan(plan_target)

        plan_repository.add(plan)
        session.commit()

        assert plan_repository.exists(plan.id.value) is True

        loaded = plan_repository.get_by_id(plan.id.value)
        assert loaded is not None
        assert loaded.id == plan.id
        assert loaded.maintenance_target == plan_target

        requirements = loaded.list_requirements()
        assert len(requirements) == 2

        calendar_requirement = next(
            req
            for req in requirements
            if req.interval.interval_type is MaintenanceIntervalType.CALENDAR_MONTHS
        )
        runtime_requirement = next(
            req
            for req in requirements
            if req.interval.interval_type is MaintenanceIntervalType.RUNNING_HOURS
        )

        assert calendar_requirement.maintenance_type is MaintenanceType.PREVENTIVE
        assert calendar_requirement.next_due == date(2029, 1, 1)
        assert calendar_requirement.instructions == "Inspect and lubricate"
        assert calendar_requirement.notes == "Primary interval"

        assert runtime_requirement.last_completed == 5000
        assert runtime_requirement.next_due == 5300

        all_plans = plan_repository.list()
        assert [item.id for item in all_plans] == [plan.id]

        plan.update_requirement(
            calendar_requirement.id,
            instructions="Inspect, lubricate and report",
            interval=MaintenanceInterval(
                interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
                interval_value=9,
            ),
        )
        plan_repository.update(plan)
        session.commit()

        updated = plan_repository.get_by_id(plan.id.value)
        assert updated is not None
        updated_requirement = updated.get_requirement(calendar_requirement.id)
        assert updated_requirement is not None
        assert updated_requirement.instructions == "Inspect, lubricate and report"
        assert updated_requirement.interval.interval_value == 9

        plan_repository.delete(plan.id.value)
        session.commit()

        assert plan_repository.get_by_id(plan.id.value) is None
        assert plan_repository.exists(plan.id.value) is False
        assert plan_repository.get_by_id(uuid4()) is None
    finally:
        session.close()


def test_maintenance_plan_repository_get_by_target_for_vessel_and_component(
    tmp_path: Path,
) -> None:
    session = _sqlite_session(tmp_path, "maint-plan-target")
    try:
        vessel_target = MaintenanceTarget(
            target_type=MaintenanceTargetType.VESSEL,
            target_id=uuid4(),
        )
        component_target = MaintenanceTarget(
            target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
            target_id=uuid4(),
        )

        plan_repository = SQLiteMaintenancePlanRepository(UnitOfWork(session))

        vessel_plan = _build_plan(vessel_target)
        component_plan = _build_plan(component_target)

        plan_repository.add(vessel_plan)
        plan_repository.add(component_plan)
        session.commit()

        vessel_results = plan_repository.get_by_target(vessel_target)
        component_results = plan_repository.get_by_target(component_target)

        assert len(vessel_results) == 1
        assert vessel_results[0].maintenance_target.target_type is MaintenanceTargetType.VESSEL

        assert len(component_results) == 1
        assert (
            component_results[0].maintenance_target.target_type
            is MaintenanceTargetType.TECHNICAL_COMPONENT
        )
    finally:
        session.close()


def test_work_order_repository_crud_get_by_requirement_and_lifecycle_roundtrip(
    tmp_path: Path,
) -> None:
    session = _sqlite_session(tmp_path, "work-order-crud")
    try:
        target = MaintenanceTarget(
            target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
            target_id=uuid4(),
        )
        requirement_id = uuid4()

        work_order_repository = SQLiteWorkOrderRepository(UnitOfWork(session))

        planned = WorkOrder(
            maintenance_target=target,
            maintenance_requirement_id=requirement_id,
            title="Planned WO",
            description="Planned state",
        )
        open_order = WorkOrder(
            maintenance_target=target,
            maintenance_requirement_id=requirement_id,
            title="Open WO",
            description="Open state",
        )
        open_order.open()

        in_progress = WorkOrder(
            maintenance_target=target,
            maintenance_requirement_id=requirement_id,
            title="In Progress WO",
            description="In progress state",
        )
        in_progress.open()
        in_progress.start(_utc(2028, 1, 1, 8))

        completed = _build_completed_work_order(
            target=target,
            requirement_id=requirement_id,
            title="Completed WO",
            finding="Observe next overhaul window",
            replacement=False,
        )

        cancelled = WorkOrder(
            maintenance_target=target,
            maintenance_requirement_id=requirement_id,
            title="Cancelled WO",
            description="Cancelled state",
        )
        cancelled.cancel(notes="Cancelled by planner")

        for order in (planned, open_order, in_progress, completed, cancelled):
            work_order_repository.add(order)
        session.commit()

        assert work_order_repository.exists(completed.id.value) is True
        assert work_order_repository.exists(uuid4()) is False

        by_id = work_order_repository.get_by_id(completed.id.value)
        assert by_id is not None
        assert by_id.status is WorkOrderStatus.COMPLETED
        assert by_id.maintenance_record is not None
        assert by_id.maintenance_record.finding == "Observe next overhaul window"

        requirement_orders = work_order_repository.get_by_maintenance_requirement_id(
            requirement_id
        )
        assert len(requirement_orders) == 5

        statuses = {order.status for order in work_order_repository.list()}
        assert statuses == {
            WorkOrderStatus.PLANNED,
            WorkOrderStatus.OPEN,
            WorkOrderStatus.IN_PROGRESS,
            WorkOrderStatus.COMPLETED,
            WorkOrderStatus.CANCELLED,
        }

        loaded_cancelled = work_order_repository.get_by_id(cancelled.id.value)
        assert loaded_cancelled is not None
        assert loaded_cancelled.status is WorkOrderStatus.CANCELLED

        loaded_planned = work_order_repository.get_by_id(planned.id.value)
        assert loaded_planned is not None
        loaded_planned.open()
        work_order_repository.update(loaded_planned)
        session.commit()
        assert work_order_repository.get_by_id(planned.id.value) is not None
        assert work_order_repository.get_by_id(planned.id.value).status is WorkOrderStatus.OPEN

        work_order_repository.delete(in_progress.id.value)
        session.commit()
        assert work_order_repository.get_by_id(in_progress.id.value) is None
        assert work_order_repository.get_by_id(uuid4()) is None

        with pytest.raises(ValueError):
            work_order_repository.delete(completed.id.value)

        session.rollback()
        preserved_completed = work_order_repository.get_by_id(completed.id.value)
        assert preserved_completed is not None
        assert preserved_completed.maintenance_record is not None
        assert preserved_completed.maintenance_record.finding == "Observe next overhaul window"
    finally:
        session.close()


def test_historical_maintenance_roundtrip_snapshot_integrity(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "maint-history")
    try:
        target = MaintenanceTarget(
            target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
            target_id=uuid4(),
        )

        plan_repository = SQLiteMaintenancePlanRepository(UnitOfWork(session))
        work_order_repository = SQLiteWorkOrderRepository(UnitOfWork(session))

        plan = MaintenancePlan(maintenance_target=target)
        requirement_a = MaintenanceRequirement(
            id=uuid4(),
            title="12 month oil maintenance",
            description="Scheduled propulsion-engine-like service",
            maintenance_target=target,
            maintenance_type=MaintenanceType.PREVENTIVE,
            interval=MaintenanceInterval(
                interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
                interval_value=12,
            ),
            due_basis=MaintenanceDueBasis.CALENDAR_DATE,
            instructions="Inspect and lubricate",
            notes="Oil task",
        )
        plan.add_requirement(requirement_a)

        plan_repository.add(plan)
        session.commit()

        work_order_a = _build_completed_work_order(
            target=target,
            requirement_id=requirement_a.id.value,
            title="WO-A",
            finding="Pitch wear observed",
            replacement=True,
        )
        work_order_repository.add(work_order_a)
        session.commit()

        restored_a = work_order_repository.get_by_id(work_order_a.id.value)
        assert restored_a is not None
        assert restored_a.maintenance_record is not None
        record_a = restored_a.maintenance_record
        assert record_a.finding == "Pitch wear observed"
        assert record_a.replacement_may_be_required is True

        plan.update_requirement(
            requirement_a.id,
            interval=MaintenanceInterval(
                interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
                interval_value=6,
            ),
            instructions="Inspect, lubricate and tighten",
        )
        plan_repository.update(plan)
        session.commit()

        work_order_b = _build_completed_work_order(
            target=target,
            requirement_id=requirement_a.id.value,
            title="WO-B",
            finding="Follow-up stable",
            replacement=False,
        )
        work_order_repository.add(work_order_b)
        session.commit()

        reloaded_a = work_order_repository.get_by_id(work_order_a.id.value)
        reloaded_b = work_order_repository.get_by_id(work_order_b.id.value)
        reloaded_plan = plan_repository.get_by_id(plan.id.value)

        assert reloaded_a is not None and reloaded_a.maintenance_record is not None
        assert reloaded_b is not None and reloaded_b.maintenance_record is not None
        assert reloaded_plan is not None

        assert reloaded_a.maintenance_record.finding == "Pitch wear observed"
        assert reloaded_a.maintenance_record.replacement_may_be_required is True
        assert reloaded_a.maintenance_record.notes == "Completed WO-A"

        assert reloaded_b.maintenance_record.finding == "Follow-up stable"
        assert reloaded_b.maintenance_record.replacement_may_be_required is False

        restored_requirement = reloaded_plan.get_requirement(requirement_a.id)
        assert restored_requirement is not None
        assert restored_requirement.interval.interval_value == 6
        assert restored_requirement.instructions == "Inspect, lubricate and tighten"

        all_for_requirement = work_order_repository.get_by_maintenance_requirement_id(
            requirement_a.id.value
        )
        record_ids = {
            work_order.maintenance_record.id.value
            for work_order in all_for_requirement
            if work_order.maintenance_record is not None
        }
        assert len(record_ids) == 2
    finally:
        session.close()


def test_generic_maritime_scenarios_and_performer_roundtrip(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "maint-scenarios")
    try:
        plan_repository = SQLiteMaintenancePlanRepository(UnitOfWork(session))
        work_order_repository = SQLiteWorkOrderRepository(UnitOfWork(session))

        propulsion_target = MaintenanceTarget(
            target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
            target_id=uuid4(),
        )
        pitch_target = MaintenanceTarget(
            target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
            target_id=uuid4(),
        )
        vessel_target = MaintenanceTarget(
            target_type=MaintenanceTargetType.VESSEL,
            target_id=uuid4(),
        )

        propulsion_plan = MaintenancePlan(maintenance_target=propulsion_target)
        propulsion_requirement = MaintenanceRequirement(
            id=uuid4(),
            title="12 month oil maintenance task",
            description="Propulsion engine annual oil maintenance",
            maintenance_target=propulsion_target,
            maintenance_type=MaintenanceType.PREVENTIVE,
            interval=MaintenanceInterval(
                interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
                interval_value=12,
            ),
            due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        )
        propulsion_plan.add_requirement(propulsion_requirement)

        pitch_plan = MaintenancePlan(maintenance_target=pitch_target)
        pitch_requirement = MaintenanceRequirement(
            id=uuid4(),
            title="Pitch inspection",
            description="Pitch propeller inspection work",
            maintenance_target=pitch_target,
            maintenance_type=MaintenanceType.INSPECTION,
            interval=MaintenanceInterval(
                interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
                interval_value=6,
            ),
            due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        )
        pitch_plan.add_requirement(pitch_requirement)

        hull_plan = MaintenancePlan(maintenance_target=vessel_target)
        hull_requirement = MaintenanceRequirement(
            id=uuid4(),
            title="Hull planking inspection",
            description="Vessel hull condition inspection",
            maintenance_target=vessel_target,
            maintenance_type=MaintenanceType.INSPECTION,
            interval=MaintenanceInterval(
                interval_type=MaintenanceIntervalType.CALENDAR_YEARS,
                interval_value=1,
            ),
            due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        )
        hull_plan.add_requirement(hull_requirement)

        for plan in (propulsion_plan, pitch_plan, hull_plan):
            plan_repository.add(plan)
        session.commit()

        propulsion_work = _build_completed_work_order(
            target=propulsion_target,
            requirement_id=propulsion_requirement.id.value,
            title="Propulsion WO",
            finding=None,
            replacement=False,
        )
        pitch_work = _build_completed_work_order(
            target=pitch_target,
            requirement_id=pitch_requirement.id.value,
            title="Pitch WO",
            finding="Possible replacement required",
            replacement=True,
        )
        hull_work = _build_completed_work_order(
            target=vessel_target,
            requirement_id=hull_requirement.id.value,
            title="Hull WO",
            finding="No structural defects",
            replacement=False,
        )

        for work in (propulsion_work, pitch_work, hull_work):
            work_order_repository.add(work)
        session.commit()

        loaded_pitch_work = work_order_repository.get_by_id(pitch_work.id.value)
        assert loaded_pitch_work is not None
        assert loaded_pitch_work.maintenance_record is not None
        assert loaded_pitch_work.maintenance_record.finding == "Possible replacement required"

        loaded_hull_work = work_order_repository.get_by_id(hull_work.id.value)
        assert loaded_hull_work is not None
        assert loaded_hull_work.maintenance_record is not None
        assert loaded_hull_work.maintenance_target.target_type is MaintenanceTargetType.VESSEL

        loaded_propulsion_work = work_order_repository.get_by_id(propulsion_work.id.value)
        assert loaded_propulsion_work is not None
        assert loaded_propulsion_work.performed_by is not None
        assert loaded_propulsion_work.performed_by.performer_type is PerformerReferenceType.MEMBER
        assert loaded_propulsion_work.performed_by.performer_id_or_external_key == "member-42"

        import mfm.infrastructure.persistence.sqlite.sqlite_maintenance_plan_repository as plan_module
        import mfm.infrastructure.persistence.sqlite.sqlite_work_order_repository as work_module

        assert "TechnicalComponentModel" not in plan_module.__dict__
        assert "TechnicalConfigurationModel" not in plan_module.__dict__
        assert "TechnicalComponentModel" not in work_module.__dict__
        assert "TechnicalConfigurationModel" not in work_module.__dict__
    finally:
        session.close()
