from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import date
from datetime import datetime
from datetime import timezone
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.maintenance.exceptions import DuplicateMaintenanceRequirementError
from mfm.domain.maintenance.exceptions import InvalidMaintenanceDueCalculationError
from mfm.domain.maintenance.exceptions import InvalidMaintenanceIntervalError
from mfm.domain.maintenance.exceptions import InvalidMaintenancePlanStateError
from mfm.domain.maintenance.exceptions import InvalidMaintenanceTargetError
from mfm.domain.maintenance.exceptions import InvalidWorkOrderChronologyError
from mfm.domain.maintenance.exceptions import InvalidWorkOrderLifecycleError
from mfm.domain.maintenance.identifiers import MaintenanceRequirementId
from mfm.domain.maintenance.maintenance_due_basis import MaintenanceDueBasis
from mfm.domain.maintenance.maintenance_interval import MaintenanceInterval
from mfm.domain.maintenance.maintenance_interval_type import MaintenanceIntervalType
from mfm.domain.maintenance.maintenance_plan import MaintenancePlan
from mfm.domain.maintenance.maintenance_plan_status import MaintenancePlanStatus
from mfm.domain.maintenance.maintenance_requirement import MaintenanceRequirement
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType
from mfm.domain.maintenance.maintenance_type import MaintenanceType
from mfm.domain.maintenance.performer_reference import PerformerReference
from mfm.domain.maintenance.performer_reference_type import PerformerReferenceType
from mfm.domain.maintenance.work_order import WorkOrder
from mfm.domain.maintenance.work_order_status import WorkOrderStatus


def _utc_dt(year: int, month: int, day: int, hour: int = 9) -> datetime:
    return datetime(year, month, day, hour, tzinfo=timezone.utc)


def _target_vessel() -> MaintenanceTarget:
    return MaintenanceTarget(
        target_type=MaintenanceTargetType.VESSEL,
        target_id=uuid4(),
    )


def _target_component() -> MaintenanceTarget:
    return MaintenanceTarget(
        target_type=MaintenanceTargetType.TECHNICAL_COMPONENT,
        target_id=uuid4(),
    )


def _calendar_requirement(*, target: MaintenanceTarget, title: str = "Inspect") -> MaintenanceRequirement:
    return MaintenanceRequirement(
        id=MaintenanceRequirementId.new(),
        title=title,
        description="Calendar maintenance requirement",
        maintenance_target=target,
        maintenance_type=MaintenanceType.PREVENTIVE,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
            interval_value=12,
        ),
        due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        instructions="Follow checklist",
        notes="Annual",
    )


def _running_hours_requirement(*, target: MaintenanceTarget, title: str = "Runtime") -> MaintenanceRequirement:
    return MaintenanceRequirement(
        id=MaintenanceRequirementId.new(),
        title=title,
        description="Running-hours maintenance requirement",
        maintenance_target=target,
        maintenance_type=MaintenanceType.CONDITION_BASED,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.RUNNING_HOURS,
            interval_value=100,
        ),
        due_basis=MaintenanceDueBasis.RUNNING_HOURS,
    )


def test_maintenance_target_vessel() -> None:
    target = _target_vessel()

    assert target.target_type is MaintenanceTargetType.VESSEL
    assert isinstance(target.target_id, UUID)


def test_maintenance_target_technical_component() -> None:
    target = _target_component()

    assert target.target_type is MaintenanceTargetType.TECHNICAL_COMPONENT
    assert isinstance(target.target_id, UUID)


def test_maintenance_target_invalid_target_type() -> None:
    with pytest.raises(InvalidMaintenanceTargetError):
        MaintenanceTarget(target_type="INVALID", target_id=uuid4())  # type: ignore[arg-type]


def test_maintenance_target_missing_target_id() -> None:
    with pytest.raises(InvalidMaintenanceTargetError):
        MaintenanceTarget(
            target_type=MaintenanceTargetType.VESSEL,
            target_id=None,  # type: ignore[arg-type]
        )


def test_maintenance_target_immutability() -> None:
    target = _target_vessel()

    with pytest.raises(FrozenInstanceError):
        target.target_id = uuid4()  # type: ignore[misc]


def test_maintenance_interval_valid_calendar_interval() -> None:
    interval = MaintenanceInterval(
        interval_type=MaintenanceIntervalType.CALENDAR_DAYS,
        interval_value=30,
    )
    interval.validate_due_basis(MaintenanceDueBasis.CALENDAR_DATE)

    assert interval.interval_value == 30


def test_maintenance_interval_valid_running_hours_interval() -> None:
    interval = MaintenanceInterval(
        interval_type=MaintenanceIntervalType.RUNNING_HOURS,
        interval_value=250,
    )
    interval.validate_due_basis(MaintenanceDueBasis.RUNNING_HOURS)

    assert interval.interval_value == 250


def test_maintenance_interval_zero_rejected() -> None:
    with pytest.raises(InvalidMaintenanceIntervalError):
        MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_DAYS,
            interval_value=0,
        )


def test_maintenance_interval_negative_rejected() -> None:
    with pytest.raises(InvalidMaintenanceIntervalError):
        MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_DAYS,
            interval_value=-1,
        )


def test_maintenance_interval_invalid_type() -> None:
    with pytest.raises(InvalidMaintenanceIntervalError):
        MaintenanceInterval(interval_type="WRONG", interval_value=12)  # type: ignore[arg-type]


def test_maintenance_interval_invalid_due_basis_combination_rejected() -> None:
    interval = MaintenanceInterval(
        interval_type=MaintenanceIntervalType.RUNNING_HOURS,
        interval_value=10,
    )

    with pytest.raises(InvalidMaintenanceIntervalError):
        interval.validate_due_basis(MaintenanceDueBasis.CALENDAR_DATE)


def test_maintenance_plan_create_plan() -> None:
    target = _target_vessel()
    plan = MaintenancePlan(maintenance_target=target)

    assert plan.maintenance_target == target
    assert plan.status is MaintenancePlanStatus.DRAFT
    assert plan.list_requirements() == ()


def test_maintenance_plan_add_requirement() -> None:
    target = _target_vessel()
    plan = MaintenancePlan(maintenance_target=target)
    requirement = _calendar_requirement(target=target)

    plan.add_requirement(requirement)

    assert plan.get_requirement(requirement.id) is requirement


def test_maintenance_plan_duplicate_requirement_handling() -> None:
    target = _target_vessel()
    plan = MaintenancePlan(maintenance_target=target)
    first = _calendar_requirement(target=target, title="Hull")
    second = _calendar_requirement(target=target, title="Hull")

    plan.add_requirement(first)

    with pytest.raises(DuplicateMaintenanceRequirementError):
        plan.add_requirement(second)


def test_maintenance_plan_update_requirement() -> None:
    target = _target_vessel()
    plan = MaintenancePlan(maintenance_target=target)
    requirement = _calendar_requirement(target=target)
    plan.add_requirement(requirement)

    plan.update_requirement(
        requirement.id,
        instructions="Updated instructions",
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_YEARS,
            interval_value=2,
        ),
        notes="Updated notes",
    )

    updated = plan.get_requirement(requirement.id)
    assert updated is not None
    assert updated.instructions == "Updated instructions"
    assert updated.interval.interval_type is MaintenanceIntervalType.CALENDAR_YEARS
    assert updated.notes == "Updated notes"


def test_maintenance_plan_target_preserved() -> None:
    target = _target_vessel()
    other_target = _target_component()
    plan = MaintenancePlan(maintenance_target=target)

    with pytest.raises(InvalidMaintenancePlanStateError):
        plan.add_requirement(_calendar_requirement(target=other_target))


def test_maintenance_plan_maintenance_type_validation() -> None:
    with pytest.raises(Exception):
        MaintenanceRequirement(
            id=MaintenanceRequirementId.new(),
            title="Type",
            description="Type",
            maintenance_target=_target_vessel(),
            maintenance_type="INVALID",  # type: ignore[arg-type]
            interval=MaintenanceInterval(
                interval_type=MaintenanceIntervalType.CALENDAR_DAYS,
                interval_value=7,
            ),
            due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        )


def test_maintenance_plan_interval_validation() -> None:
    with pytest.raises(InvalidMaintenanceIntervalError):
        MaintenanceRequirement(
            id=MaintenanceRequirementId.new(),
            title="Interval",
            description="Interval",
            maintenance_target=_target_vessel(),
            maintenance_type=MaintenanceType.PREVENTIVE,
            interval=MaintenanceInterval(
                interval_type=MaintenanceIntervalType.RUNNING_HOURS,
                interval_value=7,
            ),
            due_basis=MaintenanceDueBasis.CALENDAR_DATE,
        )


def test_maintenance_plan_due_calculation_explicit_current_date_behaviour() -> None:
    target = _target_component()
    plan = MaintenancePlan(maintenance_target=target)
    requirement = _calendar_requirement(target=target, title="Oil")
    plan.add_requirement(requirement)

    plan.record_requirement_completion(
        requirement.id,
        completed_on=date(2026, 1, 1),
    )

    due = plan.calculate_due(as_of_date=date(2027, 1, 1))
    not_due = plan.calculate_due(as_of_date=date(2026, 12, 31))

    assert due == (requirement,)
    assert not_due == ()


def test_maintenance_running_hours_due_calculation_with_supplied_state() -> None:
    target = _target_component()
    plan = MaintenancePlan(maintenance_target=target)
    requirement = _running_hours_requirement(target=target)
    plan.add_requirement(requirement)

    plan.record_requirement_completion(
        requirement.id,
        completed_running_hours=500,
    )

    due = plan.calculate_due(
        as_of_date=date(2027, 1, 1),
        running_hours_by_requirement_id={requirement.id.value: 600},
    )
    not_due = plan.calculate_due(
        as_of_date=date(2027, 1, 1),
        running_hours_by_requirement_id={requirement.id.value: 599},
    )

    assert requirement.next_due == 600
    assert due == (requirement,)
    assert not_due == ()


def test_maintenance_running_hours_requires_supplied_state() -> None:
    target = _target_component()
    plan = MaintenancePlan(maintenance_target=target)
    requirement = _running_hours_requirement(target=target)
    plan.add_requirement(requirement)

    plan.record_requirement_completion(
        requirement.id,
        completed_running_hours=100,
    )

    with pytest.raises(InvalidMaintenanceDueCalculationError):
        plan.calculate_due(as_of_date=date(2027, 1, 1))


def test_maintenance_calendar_overdue_behaviour() -> None:
    requirement = _calendar_requirement(target=_target_component(), title="Overdue")
    requirement.record_completion(completed_on=date(2026, 1, 1))

    assert requirement.next_due == date(2027, 1, 1)
    assert requirement.is_overdue(as_of_date=date(2027, 1, 1)) is False
    assert requirement.is_overdue(as_of_date=date(2027, 1, 2)) is True


def test_maintenance_running_hours_overdue_behaviour() -> None:
    requirement = _running_hours_requirement(target=_target_component(), title="Hours overdue")
    requirement.record_completion(completed_running_hours=500)

    assert requirement.next_due == 600
    assert requirement.is_overdue(current_running_hours=600) is False
    assert requirement.is_overdue(current_running_hours=601) is True


def test_work_order_create_work_order() -> None:
    order = WorkOrder(
        maintenance_target=_target_vessel(),
        title="Hull inspection",
        description="Inspect hull planking",
        planned_date=date(2027, 5, 1),
    )

    assert order.status is WorkOrderStatus.PLANNED
    assert order.started_at is None
    assert order.completed_at is None


def test_work_order_valid_lifecycle_transitions() -> None:
    order = WorkOrder(
        maintenance_target=_target_component(),
        title="Engine service",
        description="Change lubricating oil",
    )

    order.open()
    order.start(_utc_dt(2027, 5, 2, 9))
    record = order.complete(completed_at=_utc_dt(2027, 5, 2, 12))

    assert order.status is WorkOrderStatus.COMPLETED
    assert record.work_order_id == order.id


def test_work_order_invalid_lifecycle_transitions() -> None:
    order = WorkOrder(
        maintenance_target=_target_component(),
        title="Invalid transitions",
        description="Invalid transitions",
    )

    with pytest.raises(InvalidWorkOrderLifecycleError):
        order.start(_utc_dt(2027, 5, 1, 9))


def test_work_order_start_complete_cancel_paths() -> None:
    order = WorkOrder(
        maintenance_target=_target_component(),
        title="Lifecycle",
        description="Lifecycle",
    )

    order.open()
    order.start(_utc_dt(2027, 1, 10, 8))
    order.complete(completed_at=_utc_dt(2027, 1, 10, 10))

    with pytest.raises(InvalidWorkOrderLifecycleError):
        order.cancel(notes="Too late")


def test_work_order_cancel_if_in_scope() -> None:
    order = WorkOrder(
        maintenance_target=_target_vessel(),
        title="Cancel",
        description="Cancel",
    )

    order.cancel(notes="Weather")

    assert order.status is WorkOrderStatus.CANCELLED


def test_work_order_invalid_chronology() -> None:
    order = WorkOrder(
        maintenance_target=_target_component(),
        title="Chronology",
        description="Chronology",
    )
    order.open()
    order.start(_utc_dt(2027, 6, 1, 10))

    with pytest.raises(InvalidWorkOrderChronologyError):
        order.complete(completed_at=_utc_dt(2027, 6, 1, 9))


def test_work_order_completed_cannot_restart() -> None:
    order = WorkOrder(
        maintenance_target=_target_component(),
        title="Restart",
        description="Restart",
    )

    order.open()
    order.start(_utc_dt(2027, 1, 1, 8))
    order.complete(completed_at=_utc_dt(2027, 1, 1, 9))

    with pytest.raises(InvalidWorkOrderLifecycleError):
        order.start(_utc_dt(2027, 1, 1, 10))


def test_work_order_cancelled_cannot_complete() -> None:
    order = WorkOrder(
        maintenance_target=_target_component(),
        title="Cancelled",
        description="Cancelled",
    )

    order.cancel(notes="Abort")

    with pytest.raises(InvalidWorkOrderLifecycleError):
        order.complete(completed_at=_utc_dt(2027, 1, 1, 12))


def test_work_order_completed_at_requires_completion() -> None:
    with pytest.raises(InvalidWorkOrderLifecycleError):
        WorkOrder(
            maintenance_target=_target_component(),
            title="Bad completed",
            description="Bad completed",
            status=WorkOrderStatus.COMPLETED,
            completed_at=_utc_dt(2027, 1, 1, 10),
        )


def test_work_order_with_performer_reference() -> None:
    performer = PerformerReference(
        performer_type=PerformerReferenceType.VOLUNTEER,
        performer_id_or_external_key="vol-42",
        display_name_snapshot="Volunteer 42",
    )
    order = WorkOrder(
        maintenance_target=_target_component(),
        title="Performer",
        description="Performer",
    )

    order.open()
    order.start(_utc_dt(2027, 1, 1, 8))
    record = order.complete(
        completed_at=_utc_dt(2027, 1, 1, 9),
        performed_by=performer,
    )

    assert record.performed_by == performer


def test_maintenance_history_records_preserved_across_requirement_update() -> None:
    target = _target_component()
    requirement = _calendar_requirement(target=target, title="Propulsion oil")
    plan = MaintenancePlan(maintenance_target=target)
    plan.add_requirement(requirement)

    work_a = WorkOrder(
        maintenance_requirement_id=requirement.id,
        maintenance_target=target,
        title="WO-A",
        description="First completion",
    )
    work_a.open()
    work_a.start(_utc_dt(2027, 1, 1, 8))
    record_a = work_a.complete(
        completed_at=_utc_dt(2027, 1, 1, 9),
        notes="First service",
    )
    plan.record_requirement_completion(requirement.id, completed_on=date(2027, 1, 1))

    plan.update_requirement(
        requirement.id,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
            interval_value=6,
        ),
        instructions="Updated 6 month interval",
    )

    work_b = WorkOrder(
        maintenance_requirement_id=requirement.id,
        maintenance_target=target,
        title="WO-B",
        description="Second completion",
    )
    work_b.open()
    work_b.start(_utc_dt(2027, 7, 1, 8))
    record_b = work_b.complete(
        completed_at=_utc_dt(2027, 7, 1, 10),
        notes="Second service",
    )
    plan.record_requirement_completion(requirement.id, completed_on=date(2027, 7, 1))

    current_requirement = plan.get_requirement(requirement.id)
    assert current_requirement is not None
    assert current_requirement.interval.interval_value == 6
    assert current_requirement.instructions == "Updated 6 month interval"

    assert record_a.notes == "First service"
    assert record_b.notes == "Second service"
    assert record_a.id != record_b.id


def test_technical_boundary_records_finding_without_replacement_operation() -> None:
    target = _target_component()
    order = WorkOrder(
        maintenance_target=target,
        title="CPP inspection",
        description="Inspect pitch mechanism",
    )

    order.open()
    order.start(_utc_dt(2027, 9, 1, 10))
    record = order.complete(
        completed_at=_utc_dt(2027, 9, 1, 11),
        finding="Pitch mechanism wear indicates replacement may be required",
        replacement_may_be_required=True,
    )

    assert record.finding is not None
    assert record.replacement_may_be_required is True
    assert hasattr(order, "complete")
    assert not hasattr(order, "replace_component")


def test_alvur_design_validation_scenario_1_generic_data() -> None:
    target = _target_component()
    requirement = MaintenanceRequirement(
        id=MaintenanceRequirementId.new(),
        title="Change lubricating oil",
        description="Preventive oil change",
        maintenance_target=target,
        maintenance_type=MaintenanceType.PREVENTIVE,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_MONTHS,
            interval_value=12,
        ),
        due_basis=MaintenanceDueBasis.CALENDAR_DATE,
    )
    plan = MaintenancePlan(maintenance_target=target)
    plan.add_requirement(requirement)

    plan.record_requirement_completion(requirement.id, completed_on=date(2027, 1, 1))
    due = plan.calculate_due(as_of_date=date(2028, 1, 1))

    order = WorkOrder(
        maintenance_requirement_id=requirement.id,
        maintenance_target=target,
        title="Oil change WO",
        description="Perform oil change",
    )
    order.open()
    order.start(_utc_dt(2028, 1, 2, 8))
    record = order.complete(completed_at=_utc_dt(2028, 1, 2, 11))

    assert due == (requirement,)
    assert record.work_order_id == order.id


def test_alvur_design_validation_scenario_2_generic_data() -> None:
    target = _target_component()
    requirement = MaintenanceRequirement(
        id=MaintenanceRequirementId.new(),
        title="Inspect pitch mechanism",
        description="Inspection work",
        maintenance_target=target,
        maintenance_type=MaintenanceType.INSPECTION,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_YEARS,
            interval_value=1,
        ),
        due_basis=MaintenanceDueBasis.CALENDAR_DATE,
    )
    plan = MaintenancePlan(maintenance_target=target)
    plan.add_requirement(requirement)

    order = WorkOrder(
        maintenance_requirement_id=requirement.id,
        maintenance_target=target,
        title="Inspection WO",
        description="Inspect propeller mechanism",
    )
    order.open()
    order.start(_utc_dt(2027, 3, 1, 8))
    record = order.complete(
        completed_at=_utc_dt(2027, 3, 1, 9),
        finding="Replacement may be required",
        replacement_may_be_required=True,
    )

    assert record.replacement_may_be_required is True
    assert not hasattr(plan, "replace_component")


def test_alvur_design_validation_scenario_3_generic_data() -> None:
    target = _target_vessel()
    requirement = MaintenanceRequirement(
        id=MaintenanceRequirementId.new(),
        title="Inspect hull planking",
        description="Vessel-level inspection",
        maintenance_target=target,
        maintenance_type=MaintenanceType.INSPECTION,
        interval=MaintenanceInterval(
            interval_type=MaintenanceIntervalType.CALENDAR_YEARS,
            interval_value=1,
        ),
        due_basis=MaintenanceDueBasis.CALENDAR_DATE,
    )
    plan = MaintenancePlan(maintenance_target=target)
    plan.add_requirement(requirement)

    order = WorkOrder(
        maintenance_requirement_id=requirement.id,
        maintenance_target=target,
        title="Hull inspection WO",
        description="Inspect hull",
    )
    order.open()
    order.start(_utc_dt(2027, 4, 1, 9))
    record = order.complete(completed_at=_utc_dt(2027, 4, 1, 12))

    assert record.maintenance_target.target_type is MaintenanceTargetType.VESSEL
