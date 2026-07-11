"""Mapper between maintenance domain and persistence models."""

from __future__ import annotations

from mfm.database.models.maintenance_plan_model import MaintenancePlanModel
from mfm.database.models.maintenance_record_model import MaintenanceRecordModel
from mfm.database.models.maintenance_requirement_model import MaintenanceRequirementModel
from mfm.database.models.work_order_model import WorkOrderModel
from mfm.domain.maintenance.identifiers import MaintenancePlanId
from mfm.domain.maintenance.identifiers import MaintenanceRecordId
from mfm.domain.maintenance.identifiers import MaintenanceRequirementId
from mfm.domain.maintenance.identifiers import WorkOrderId
from mfm.domain.maintenance.maintenance_interval import MaintenanceInterval
from mfm.domain.maintenance.maintenance_plan import MaintenancePlan
from mfm.domain.maintenance.maintenance_record import MaintenanceRecord
from mfm.domain.maintenance.maintenance_requirement import MaintenanceRequirement
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.domain.maintenance.performer_reference import PerformerReference
from mfm.domain.maintenance.work_order import WorkOrder


class MaintenanceMapper:
    """Map maintenance aggregates to/from SQLAlchemy models."""

    @staticmethod
    def to_orm_plan(plan: MaintenancePlan) -> MaintenancePlanModel:
        orm = MaintenancePlanModel(
            id=plan.id.value,
            target_type=plan.maintenance_target.target_type,
            target_id=plan.maintenance_target.target_id,
            status=plan.status,
        )

        for requirement in plan.list_requirements():
            last_completed_date = None
            last_completed_running_hours = None
            next_due_date = None
            next_due_running_hours = None

            if requirement.due_basis.value == "CALENDAR_DATE":
                last_completed_date = requirement.last_completed
                next_due_date = requirement.next_due
            else:
                last_completed_running_hours = requirement.last_completed
                next_due_running_hours = requirement.next_due

            orm.requirements.append(
                MaintenanceRequirementModel(
                    id=requirement.id.value,
                    maintenance_plan_id=plan.id.value,
                    title=requirement.title,
                    description=requirement.description,
                    target_type=requirement.maintenance_target.target_type,
                    target_id=requirement.maintenance_target.target_id,
                    maintenance_type=requirement.maintenance_type,
                    interval_type=requirement.interval.interval_type,
                    interval_value=requirement.interval.interval_value,
                    due_basis=requirement.due_basis,
                    last_completed_date=last_completed_date,
                    last_completed_running_hours=last_completed_running_hours,
                    next_due_date=next_due_date,
                    next_due_running_hours=next_due_running_hours,
                    status=requirement.status,
                    instructions=requirement.instructions,
                    notes=requirement.notes,
                )
            )

        return orm

    @staticmethod
    def to_domain_plan(orm: MaintenancePlanModel) -> MaintenancePlan:
        plan = MaintenancePlan(
            id=MaintenancePlanId(orm.id),
            maintenance_target=MaintenanceTarget(
                target_type=orm.target_type,
                target_id=orm.target_id,
            ),
            status=orm.status,
        )

        for requirement_orm in orm.requirements:
            requirement = MaintenanceRequirement(
                id=MaintenanceRequirementId(requirement_orm.id),
                title=requirement_orm.title,
                description=requirement_orm.description,
                maintenance_target=MaintenanceTarget(
                    target_type=requirement_orm.target_type,
                    target_id=requirement_orm.target_id,
                ),
                maintenance_type=requirement_orm.maintenance_type,
                interval=MaintenanceInterval(
                    interval_type=requirement_orm.interval_type,
                    interval_value=requirement_orm.interval_value,
                ),
                due_basis=requirement_orm.due_basis,
                last_completed=(
                    requirement_orm.last_completed_date
                    if requirement_orm.due_basis.value == "CALENDAR_DATE"
                    else requirement_orm.last_completed_running_hours
                ),
                next_due=(
                    requirement_orm.next_due_date
                    if requirement_orm.due_basis.value == "CALENDAR_DATE"
                    else requirement_orm.next_due_running_hours
                ),
                status=requirement_orm.status,
                instructions=requirement_orm.instructions,
                notes=requirement_orm.notes,
            )
            plan._requirements[requirement.id] = requirement

        plan.pull_events()
        return plan

    @staticmethod
    def to_orm_work_order(work_order: WorkOrder) -> WorkOrderModel:
        orm = WorkOrderModel(
            id=work_order.id.value,
            maintenance_requirement_id=(
                work_order.maintenance_requirement_id.value
                if work_order.maintenance_requirement_id is not None
                else None
            ),
            target_type=work_order.maintenance_target.target_type,
            target_id=work_order.maintenance_target.target_id,
            title=work_order.title,
            description=work_order.description,
            status=work_order.status,
            planned_date=work_order.planned_date,
            started_at=work_order.started_at,
            completed_at=work_order.completed_at,
            performer_type=(
                work_order.performed_by.performer_type
                if work_order.performed_by is not None
                else None
            ),
            performer_id_or_external_key=(
                work_order.performed_by.performer_id_or_external_key
                if work_order.performed_by is not None
                else None
            ),
            performer_display_name_snapshot=(
                work_order.performed_by.display_name_snapshot
                if work_order.performed_by is not None
                else None
            ),
            notes=work_order.notes,
        )

        if work_order.maintenance_record is not None:
            record = work_order.maintenance_record
            orm.records.append(
                MaintenanceRecordModel(
                    id=record.id.value,
                    work_order_id=work_order.id.value,
                    maintenance_requirement_id=(
                        record.maintenance_requirement_id.value
                        if record.maintenance_requirement_id is not None
                        else None
                    ),
                    target_type=record.maintenance_target.target_type,
                    target_id=record.maintenance_target.target_id,
                    completed_at=record.completed_at,
                    performer_type=(
                        record.performed_by.performer_type
                        if record.performed_by is not None
                        else None
                    ),
                    performer_id_or_external_key=(
                        record.performed_by.performer_id_or_external_key
                        if record.performed_by is not None
                        else None
                    ),
                    performer_display_name_snapshot=(
                        record.performed_by.display_name_snapshot
                        if record.performed_by is not None
                        else None
                    ),
                    notes=record.notes,
                    finding=record.finding,
                    replacement_may_be_required=record.replacement_may_be_required,
                )
            )

        return orm

    @staticmethod
    def to_domain_work_order(orm: WorkOrderModel) -> WorkOrder:
        performed_by = None
        if orm.performer_type is not None and orm.performer_id_or_external_key is not None:
            performed_by = PerformerReference(
                performer_type=orm.performer_type,
                performer_id_or_external_key=orm.performer_id_or_external_key,
                display_name_snapshot=orm.performer_display_name_snapshot,
            )

        work_order = WorkOrder(
            id=WorkOrderId(orm.id),
            maintenance_requirement_id=(
                MaintenanceRequirementId(orm.maintenance_requirement_id)
                if orm.maintenance_requirement_id is not None
                else None
            ),
            maintenance_target=MaintenanceTarget(
                target_type=orm.target_type,
                target_id=orm.target_id,
            ),
            title=orm.title,
            description=orm.description,
            status=orm.status,
            planned_date=orm.planned_date,
            started_at=orm.started_at,
            completed_at=orm.completed_at,
            performed_by=performed_by,
            notes=orm.notes,
        )

        if orm.records:
            record_orm = orm.records[0]
            record_performer = None
            if (
                record_orm.performer_type is not None
                and record_orm.performer_id_or_external_key is not None
            ):
                record_performer = PerformerReference(
                    performer_type=record_orm.performer_type,
                    performer_id_or_external_key=record_orm.performer_id_or_external_key,
                    display_name_snapshot=record_orm.performer_display_name_snapshot,
                )

            work_order._record = MaintenanceRecord(
                id=MaintenanceRecordId(record_orm.id),
                work_order_id=WorkOrderId(record_orm.work_order_id),
                maintenance_requirement_id=(
                    MaintenanceRequirementId(record_orm.maintenance_requirement_id)
                    if record_orm.maintenance_requirement_id is not None
                    else None
                ),
                maintenance_target=MaintenanceTarget(
                    target_type=record_orm.target_type,
                    target_id=record_orm.target_id,
                ),
                completed_at=record_orm.completed_at,
                performed_by=record_performer,
                notes=record_orm.notes,
                finding=record_orm.finding,
                replacement_may_be_required=record_orm.replacement_may_be_required,
            )

        work_order.pull_events()
        return work_order
