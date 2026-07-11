from __future__ import annotations

from datetime import date
from datetime import datetime
from datetime import timezone
from uuid import UUID

import mfm.database.models  # noqa: F401
from mfm.database.mappers.maintenance_mapper import MaintenanceMapper
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.maintenance_plan_model import MaintenancePlanModel
from mfm.database.models.work_order_model import WorkOrderModel
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


def _utc(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, tzinfo=timezone.utc)


def _build_plan(target_type: MaintenanceTargetType) -> MaintenancePlan:
    target_id = (
        UUID("00000000-0000-0000-0000-000000000011")
        if target_type is MaintenanceTargetType.VESSEL
        else UUID("00000000-0000-0000-0000-000000000012")
    )
    target = MaintenanceTarget(target_type=target_type, target_id=target_id)
    plan = MaintenancePlan(maintenance_target=target)

    calendar_requirement = MaintenanceRequirement(
        id=UUID("00000000-0000-0000-0000-000000000101"),
        title="Change lubricating oil",
        description="Preventive lubrication service",
        maintenance_target=target,
        maintenance_type=MaintenanceType.PREVENTIVE,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
            interval_value=12,
        ),
        due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        instructions="Inspect and lubricate",
        notes="Engine room task",
    )
    calendar_requirement.record_completion(completed_on=date(2027, 1, 1))

    running_requirement = MaintenanceRequirement(
        id=UUID("00000000-0000-0000-0000-000000000102"),
        title="Condition follow-up",
        description="Runtime based condition check",
        maintenance_target=target,
        maintenance_type=MaintenanceType.CONDITION_BASED,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.RUNNING_HOURS,
            interval_value=250,
        ),
        due_basis=MaintenanceDueBasis.RUNNING_HOURS,
        instructions="Log running-hours",
    )
    running_requirement.record_completion(completed_running_hours=4000)

    plan.add_requirement(calendar_requirement)
    plan.add_requirement(running_requirement)
    return plan


def _build_completed_work_order() -> WorkOrder:
    target = MaintenanceTarget(
        target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
        target_id=UUID("00000000-0000-0000-0000-000000000201"),
    )
    performer = PerformerReference(
        performer_type=PerformerReferenceType.MEMBER,
        performer_id_or_external_key="member-7",
        display_name_snapshot="Member Seven",
    )

    work_order = WorkOrder(
        maintenance_target=target,
        maintenance_requirement_id=UUID("00000000-0000-0000-0000-000000000101"),
        title="Oil Change WO",
        description="Execute oil change",
        planned_date=date(2028, 1, 2),
    )
    work_order.open()
    work_order.start(_utc(2028, 1, 2, 9))
    work_order.complete(
        completed_at=_utc(2028, 1, 2, 11),
        performed_by=performer,
        notes="Completed without deviation",
        finding="Replacement may be required in next drydock",
        replacement_may_be_required=True,
    )
    return work_order


def test_maintenance_target_roundtrip_for_vessel_and_component() -> None:
    vessel_plan = _build_plan(MaintenanceTargetType.VESSEL)
    component_plan = _build_plan(MaintenanceTargetType.TECHNICAL_COMPONENT)

    vessel_restored = MaintenanceMapper.to_domain_plan(
        MaintenanceMapper.to_orm_plan(vessel_plan)
    )
    component_restored = MaintenanceMapper.to_domain_plan(
        MaintenanceMapper.to_orm_plan(component_plan)
    )

    assert vessel_restored.maintenance_target.target_type is MaintenanceTargetType.VESSEL
    assert component_restored.maintenance_target.target_type is MaintenanceTargetType.TECHNICAL_COMPONENT
    assert isinstance(vessel_restored.maintenance_target.target_id, UUID)
    assert isinstance(component_restored.maintenance_target.target_id, UUID)


def test_maintenance_plan_mapper_roundtrip_preserves_requirement_state() -> None:
    plan = _build_plan(MaintenanceTargetType.TECHNICAL_COMPONENT)

    orm = MaintenanceMapper.to_orm_plan(plan)
    assert isinstance(orm, MaintenancePlanModel)
    assert len(orm.requirements) == 2

    restored = MaintenanceMapper.to_domain_plan(orm)
    requirements = {requirement.id.value: requirement for requirement in restored.list_requirements()}

    assert restored.id == plan.id
    assert restored.maintenance_target == plan.maintenance_target

    calendar = requirements[UUID("00000000-0000-0000-0000-000000000101")]
    assert calendar.maintenance_type is MaintenanceType.PREVENTIVE
    assert calendar.interval.interval_type is MaintenanceIntervalType.CALENDAR_MONTHS
    assert calendar.interval.interval_value == 12
    assert calendar.last_completed == date(2027, 1, 1)
    assert calendar.next_due == date(2028, 1, 1)
    assert calendar.instructions == "Inspect and lubricate"
    assert calendar.notes == "Engine room task"

    runtime = requirements[UUID("00000000-0000-0000-0000-000000000102")]
    assert runtime.interval.interval_type is MaintenanceIntervalType.RUNNING_HOURS
    assert runtime.last_completed == 4000
    assert runtime.next_due == 4250


def test_maintenance_interval_types_roundtrip_preserved() -> None:
    target = MaintenanceTarget(
        target_type=MaintenanceTargetType.VESSEL,
        target_id=UUID("00000000-0000-0000-0000-000000000301"),
    )
    plan = MaintenancePlan(maintenance_target=target)

    interval_types = (
        MaintenanceIntervalType.CALENDAR_DAYS,
        MaintenanceIntervalType.CALENDAR_MONTHS,
        MaintenanceIntervalType.CALENDAR_YEARS,
        MaintenanceIntervalType.RUNNING_HOURS,
    )

    for index, interval_type in enumerate(interval_types, start=1):
        due_basis = (
            MaintenanceDueBasis.RUNNING_HOURS
            if interval_type is MaintenanceIntervalType.RUNNING_HOURS
            else MaintenanceDueBasis.CALENDAR_DATE
        )
        requirement = MaintenanceRequirement(
            id=UUID(int=index),
            title=f"Req {index}",
            description="Type coverage",
            maintenance_target=target,
            maintenance_type=MaintenanceType.INSPECTION,
            interval=MaintenanceInterval(interval_type=interval_type, interval_value=10),
            due_basis=due_basis,
        )
        plan.add_requirement(requirement)

    restored = MaintenanceMapper.to_domain_plan(MaintenanceMapper.to_orm_plan(plan))
    restored_types = {r.interval.interval_type for r in restored.list_requirements()}
    assert restored_types == set(interval_types)


def test_work_order_mapper_roundtrip_for_all_lifecycle_states() -> None:
    target = MaintenanceTarget(
        target_type=MaintenanceTargetType.VESSEL,
        target_id=UUID("00000000-0000-0000-0000-000000000401"),
    )

    planned = WorkOrder(
        maintenance_target=target,
        title="Planned",
        description="Planned",
        planned_date=date(2028, 1, 1),
    )

    open_order = WorkOrder(
        maintenance_target=target,
        title="Open",
        description="Open",
    )
    open_order.open()

    in_progress = WorkOrder(
        maintenance_target=target,
        title="Progress",
        description="Progress",
    )
    in_progress.open()
    in_progress.start(_utc(2028, 1, 1, 9))

    completed = _build_completed_work_order()

    cancelled = WorkOrder(
        maintenance_target=target,
        title="Cancelled",
        description="Cancelled",
    )
    cancelled.cancel(notes="Deferred")

    for order in (planned, open_order, in_progress, completed, cancelled):
        orm = MaintenanceMapper.to_orm_work_order(order)
        assert isinstance(orm, WorkOrderModel)
        restored = MaintenanceMapper.to_domain_work_order(orm)

        assert restored.status is order.status
        assert restored.planned_date == order.planned_date
        assert restored.started_at == order.started_at
        assert restored.completed_at == order.completed_at

    completed_restored = MaintenanceMapper.to_domain_work_order(
        MaintenanceMapper.to_orm_work_order(completed)
    )
    assert completed_restored.maintenance_record is not None
    assert completed_restored.maintenance_record.finding == "Replacement may be required in next drydock"
    assert completed_restored.maintenance_record.replacement_may_be_required is True


def test_historical_snapshot_integrity_not_derived_from_current_plan() -> None:
    target = MaintenanceTarget(
        target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
        target_id=UUID("00000000-0000-0000-0000-000000000501"),
    )

    plan = MaintenancePlan(maintenance_target=target)
    requirement = MaintenanceRequirement(
        id=UUID("00000000-0000-0000-0000-000000000111"),
        title="Pitch inspection",
        description="Inspect CPP",
        maintenance_target=target,
        maintenance_type=MaintenanceType.INSPECTION,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_YEARS,
            interval_value=1,
        ),
        due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        instructions="Inspect and lubricate",
    )
    plan.add_requirement(requirement)

    work_a = WorkOrder(
        maintenance_target=target,
        maintenance_requirement_id=requirement.id,
        title="WO-A",
        description="Initial inspection",
    )
    work_a.open()
    work_a.start(_utc(2027, 3, 1, 9))
    work_a.complete(
        completed_at=_utc(2027, 3, 1, 10),
        notes="Instruction snapshot: Inspect and lubricate",
    )

    plan.update_requirement(
        requirement.id,
        instructions="Disassemble, inspect and lubricate",
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
            interval_value=6,
        ),
    )

    restored_work_a = MaintenanceMapper.to_domain_work_order(
        MaintenanceMapper.to_orm_work_order(work_a)
    )
    restored_plan = MaintenanceMapper.to_domain_plan(MaintenanceMapper.to_orm_plan(plan))

    assert restored_work_a.maintenance_record is not None
    assert restored_work_a.maintenance_record.notes == "Instruction snapshot: Inspect and lubricate"
    restored_requirement = next(iter(restored_plan.list_requirements()))
    assert restored_requirement.instructions == "Disassemble, inspect and lubricate"
