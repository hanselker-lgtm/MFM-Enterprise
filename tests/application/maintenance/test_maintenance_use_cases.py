from __future__ import annotations

from copy import deepcopy
from dataclasses import is_dataclass
from datetime import date
from datetime import datetime
from datetime import timezone
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.maintenance.add_maintenance_requirement import (
    AddMaintenanceRequirementRequest,
)
from mfm.application.maintenance.add_maintenance_requirement import (
    AddMaintenanceRequirementUseCase,
)
from mfm.application.maintenance.calculate_due_maintenance import (
    CalculateDueMaintenanceRequest,
)
from mfm.application.maintenance.calculate_due_maintenance import (
    CalculateDueMaintenanceUseCase,
)
from mfm.application.maintenance.cancel_work_order import CancelWorkOrderRequest
from mfm.application.maintenance.cancel_work_order import CancelWorkOrderUseCase
from mfm.application.maintenance.complete_work_order import CompleteWorkOrderRequest
from mfm.application.maintenance.complete_work_order import CompleteWorkOrderUseCase
from mfm.application.maintenance.create_maintenance_plan import (
    BusinessRuleViolation,
)
from mfm.application.maintenance.create_maintenance_plan import (
    CreateMaintenancePlanRequest,
)
from mfm.application.maintenance.create_maintenance_plan import (
    CreateMaintenancePlanUseCase,
)
from mfm.application.maintenance.create_maintenance_plan import RepositoryException
from mfm.application.maintenance.create_maintenance_plan import ValidationException
from mfm.application.maintenance.create_work_order import CreateWorkOrderRequest
from mfm.application.maintenance.create_work_order import CreateWorkOrderUseCase
from mfm.application.maintenance.get_maintenance_history import (
    GetMaintenanceHistoryRequest,
)
from mfm.application.maintenance.get_maintenance_history import (
    GetMaintenanceHistoryUseCase,
)
from mfm.application.maintenance.open_work_order import OpenWorkOrderRequest
from mfm.application.maintenance.open_work_order import OpenWorkOrderUseCase
from mfm.application.maintenance.start_work_order import StartWorkOrderRequest
from mfm.application.maintenance.start_work_order import StartWorkOrderUseCase
from mfm.application.maintenance.update_maintenance_requirement import (
    UpdateMaintenanceRequirementRequest,
)
from mfm.application.maintenance.update_maintenance_requirement import (
    UpdateMaintenanceRequirementUseCase,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.maintenance.maintenance_plan import MaintenancePlan
from mfm.domain.maintenance.maintenance_target import MaintenanceTarget
from mfm.domain.maintenance.maintenance_target_type import MaintenanceTargetType
from mfm.domain.maintenance.work_order import WorkOrder
from mfm.repositories.maintenance_plan_repository import MaintenancePlanRepository
from mfm.repositories.work_order_repository import WorkOrderRepository


class InMemoryMaintenancePlanRepository(MaintenancePlanRepository):
    def __init__(self) -> None:
        self._items: dict[UUID, MaintenancePlan] = {}
        self.add_calls = 0
        self.update_calls = 0

    def snapshot(self) -> dict[UUID, MaintenancePlan]:
        return deepcopy(self._items)

    def restore(self, snapshot: dict[UUID, MaintenancePlan]) -> None:
        self._items = deepcopy(snapshot)

    def add(self, plan: MaintenancePlan) -> None:
        self.add_calls += 1
        self._items[plan.id.value] = deepcopy(plan)

    def get_by_id(self, plan_id: UUID) -> MaintenancePlan | None:
        item = self._items.get(plan_id)
        return deepcopy(item) if item is not None else None

    def update(self, plan: MaintenancePlan) -> None:
        self.update_calls += 1
        if plan.id.value not in self._items:
            raise ValueError("plan does not exist")
        self._items[plan.id.value] = deepcopy(plan)

    def delete(self, plan_id: UUID) -> None:
        self._items.pop(plan_id, None)

    def exists(self, plan_id: UUID) -> bool:
        return plan_id in self._items

    def list(self) -> list[MaintenancePlan]:
        return [deepcopy(item) for item in self._items.values()]

    def get_by_target(self, target: MaintenanceTarget) -> list[MaintenancePlan]:
        return [
            deepcopy(item)
            for item in self._items.values()
            if item.maintenance_target == target
        ]


class InMemoryWorkOrderRepository(WorkOrderRepository):
    def __init__(self) -> None:
        self._items: dict[UUID, WorkOrder] = {}
        self.add_calls = 0
        self.update_calls = 0

    def snapshot(self) -> dict[UUID, WorkOrder]:
        return deepcopy(self._items)

    def restore(self, snapshot: dict[UUID, WorkOrder]) -> None:
        self._items = deepcopy(snapshot)

    def add(self, work_order: WorkOrder) -> None:
        self.add_calls += 1
        self._items[work_order.id.value] = deepcopy(work_order)

    def get_by_id(self, work_order_id: UUID) -> WorkOrder | None:
        item = self._items.get(work_order_id)
        return deepcopy(item) if item is not None else None

    def update(self, work_order: WorkOrder) -> None:
        self.update_calls += 1
        if work_order.id.value not in self._items:
            raise ValueError("work order does not exist")
        self._items[work_order.id.value] = deepcopy(work_order)

    def delete(self, work_order_id: UUID) -> None:
        self._items.pop(work_order_id, None)

    def exists(self, work_order_id: UUID) -> bool:
        return work_order_id in self._items

    def list(self) -> list[WorkOrder]:
        return [deepcopy(item) for item in self._items.values()]

    def get_by_maintenance_requirement_id(
        self,
        maintenance_requirement_id: UUID,
    ) -> list[WorkOrder]:
        return [
            deepcopy(item)
            for item in self._items.values()
            if item.maintenance_requirement_id is not None
            and item.maintenance_requirement_id.value == maintenance_requirement_id
        ]


class FakeMaintenanceUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        plan_repository: InMemoryMaintenancePlanRepository | None = None,
        work_order_repository: InMemoryWorkOrderRepository | None = None,
        fail_commit: bool = False,
    ) -> None:
        super().__init__()
        self._plan_repository = plan_repository or InMemoryMaintenancePlanRepository()
        self._work_order_repository = work_order_repository or InMemoryWorkOrderRepository()
        self._fail_commit = fail_commit
        self.commits = 0
        self.rollbacks = 0
        self._plan_snapshot: dict[UUID, MaintenancePlan] = {}
        self._work_order_snapshot: dict[UUID, WorkOrder] = {}

    def _start_scope(self) -> None:
        self.maintenance_plan_repository = self._plan_repository
        self.work_order_repository = self._work_order_repository

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

        self._plan_snapshot = self._plan_repository.snapshot()
        self._work_order_snapshot = self._work_order_repository.snapshot()

    def _commit_impl(self) -> None:
        self.commits += 1
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self._plan_repository.restore(self._plan_snapshot)
        self._work_order_repository.restore(self._work_order_snapshot)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


def _utc(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour, tzinfo=timezone.utc)


def _create_plan_with_requirement(
    uow: FakeMaintenanceUnitOfWork,
    *,
    target_type: str = "TECHNICAL_COMPONENT",
    title: str = "12 month oil maintenance",
    instructions: str | None = "Instruction A",
) -> tuple[UUID, UUID]:
    create_response = CreateMaintenancePlanUseCase(unit_of_work=uow).execute(
        CreateMaintenancePlanRequest(target_type=target_type, target_id=uuid4())
    )

    updated = AddMaintenanceRequirementUseCase(unit_of_work=uow).execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=create_response.plan.id,
            title=title,
            description="Generic maintenance requirement",
            maintenance_type="PREVENTIVE",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
            instructions=instructions,
            notes="Generic note",
        )
    )

    requirement_id = updated.plan.requirements[0].id
    return create_response.plan.id, requirement_id


def test_create_maintenance_plan_for_vessel_and_component_targets() -> None:
    uow = FakeMaintenanceUnitOfWork()
    use_case = CreateMaintenancePlanUseCase(unit_of_work=uow)

    vessel_response = use_case.execute(
        CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4())
    )
    component_response = use_case.execute(
        CreateMaintenancePlanRequest(target_type="TECHNICAL_COMPONENT", target_id=uuid4())
    )

    assert vessel_response.plan.target.target_type == "VESSEL"
    assert component_response.plan.target.target_type == "TECHNICAL_COMPONENT"
    assert uow.commits == 2


def test_create_maintenance_plan_invalid_target_raises_validation() -> None:
    uow = FakeMaintenanceUnitOfWork()

    with pytest.raises(ValidationException):
        CreateMaintenancePlanUseCase(unit_of_work=uow).execute(
            CreateMaintenancePlanRequest(target_type="NOT_VALID", target_id=uuid4())
        )


def test_create_maintenance_plan_duplicate_target_rolls_back() -> None:
    uow = FakeMaintenanceUnitOfWork()
    use_case = CreateMaintenancePlanUseCase(unit_of_work=uow)
    target_id = uuid4()

    use_case.execute(CreateMaintenancePlanRequest(target_type="VESSEL", target_id=target_id))

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(CreateMaintenancePlanRequest(target_type="VESSEL", target_id=target_id))

    assert uow.rollbacks >= 1


def test_add_and_update_maintenance_requirement_and_repository_interactions() -> None:
    uow = FakeMaintenanceUnitOfWork()
    plan_id, requirement_id = _create_plan_with_requirement(uow)

    updated = UpdateMaintenanceRequirementUseCase(unit_of_work=uow).execute(
        UpdateMaintenanceRequirementRequest(
            maintenance_plan_id=plan_id,
            maintenance_requirement_id=requirement_id,
            instructions="Instruction B",
            interval_type="CALENDAR_MONTHS",
            interval_value=6,
        )
    )

    assert updated.plan.requirements[0].instructions == "Instruction B"
    assert updated.plan.requirements[0].interval.interval_value == 6
    assert uow.maintenance_plan_repository.add_calls >= 1
    assert uow.maintenance_plan_repository.update_calls >= 2


def test_add_duplicate_requirement_raises_business_rule_violation() -> None:
    uow = FakeMaintenanceUnitOfWork()
    plan_id, _ = _create_plan_with_requirement(uow, title="duplicate-title")

    with pytest.raises(BusinessRuleViolation):
        AddMaintenanceRequirementUseCase(unit_of_work=uow).execute(
            AddMaintenanceRequirementRequest(
                maintenance_plan_id=plan_id,
                title="duplicate-title",
                description="Generic maintenance requirement",
                maintenance_type="PREVENTIVE",
                interval_type="CALENDAR_MONTHS",
                interval_value=12,
                due_basis="CALENDAR_DATE",
                instructions="Instruction A",
            )
        )


def test_plan_not_found_rolls_back() -> None:
    uow = FakeMaintenanceUnitOfWork()

    with pytest.raises(BusinessRuleViolation):
        UpdateMaintenanceRequirementUseCase(unit_of_work=uow).execute(
            UpdateMaintenanceRequirementRequest(
                maintenance_plan_id=uuid4(),
                maintenance_requirement_id=uuid4(),
                instructions="Instruction B",
            )
        )

    assert uow.rollbacks >= 1


def test_due_calculation_uses_explicit_request_values() -> None:
    uow = FakeMaintenanceUnitOfWork()
    plan_id, requirement_id = _create_plan_with_requirement(uow)

    due_response = CalculateDueMaintenanceUseCase(unit_of_work=uow).execute(
        CalculateDueMaintenanceRequest(
            maintenance_plan_id=plan_id,
            as_of_date=date(2030, 1, 2),
            running_hours_by_requirement_id={requirement_id: 0},
        )
    )

    assert len(due_response.due_requirements) == 0

    plan = uow.maintenance_plan_repository.get_by_id(plan_id)
    assert plan is not None
    plan.record_requirement_completion(requirement_id, completed_on=date(2029, 1, 1))
    uow.maintenance_plan_repository.update(plan)

    due_response_after_completion = CalculateDueMaintenanceUseCase(unit_of_work=uow).execute(
        CalculateDueMaintenanceRequest(
            maintenance_plan_id=plan_id,
            as_of_date=date(2030, 1, 2),
            running_hours_by_requirement_id={requirement_id: 0},
        )
    )

    assert len(due_response_after_completion.due_requirements) == 1
    assert due_response_after_completion.due_requirements[0].id == requirement_id


def test_work_order_lifecycle_and_completion_history_with_performer_mapping() -> None:
    uow = FakeMaintenanceUnitOfWork()
    plan_id, requirement_id = _create_plan_with_requirement(uow)

    created = CreateWorkOrderUseCase(unit_of_work=uow).execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan_id,
            maintenance_requirement_id=requirement_id,
            title="WO-1",
            description="Execute requirement",
            planned_date=date(2030, 1, 1),
        )
    )

    opened = OpenWorkOrderUseCase(unit_of_work=uow).execute(
        OpenWorkOrderRequest(work_order_id=created.work_order.id)
    )
    started = StartWorkOrderUseCase(unit_of_work=uow).execute(
        StartWorkOrderRequest(
            work_order_id=opened.work_order.id,
            started_at=_utc(2030, 1, 1, 9),
        )
    )
    completed = CompleteWorkOrderUseCase(unit_of_work=uow).execute(
        CompleteWorkOrderRequest(
            work_order_id=started.work_order.id,
            completed_at=_utc(2030, 1, 1, 12),
            performer_type="MEMBER",
            performer_id_or_external_key="member-100",
            performer_display_name_snapshot="Member 100",
            notes="Instruction A",
            finding="possible replacement required",
            replacement_may_be_required=True,
        )
    )

    assert completed.work_order.status == "COMPLETED"
    assert completed.work_order.maintenance_record is not None
    assert completed.work_order.maintenance_record.performer is not None
    assert completed.work_order.maintenance_record.performer.performer_type == "MEMBER"
    assert completed.work_order.maintenance_record.finding == "possible replacement required"
    assert completed.work_order.maintenance_record.replacement_may_be_required is True


def test_work_order_cancel_and_invalid_lifecycle() -> None:
    uow = FakeMaintenanceUnitOfWork()
    plan_id, requirement_id = _create_plan_with_requirement(uow, target_type="VESSEL")

    created = CreateWorkOrderUseCase(unit_of_work=uow).execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan_id,
            maintenance_requirement_id=requirement_id,
            title="WO-cancel",
            description="Cancel flow",
        )
    )

    cancelled = CancelWorkOrderUseCase(unit_of_work=uow).execute(
        CancelWorkOrderRequest(work_order_id=created.work_order.id, notes="Cancelled")
    )
    assert cancelled.work_order.status == "CANCELLED"

    with pytest.raises(BusinessRuleViolation):
        StartWorkOrderUseCase(unit_of_work=uow).execute(
            StartWorkOrderRequest(
                work_order_id=cancelled.work_order.id,
                started_at=_utc(2030, 1, 2, 9),
            )
        )


def test_work_order_not_found_and_rollback() -> None:
    uow = FakeMaintenanceUnitOfWork()

    with pytest.raises(BusinessRuleViolation):
        OpenWorkOrderUseCase(unit_of_work=uow).execute(
            OpenWorkOrderRequest(work_order_id=uuid4())
        )

    assert uow.rollbacks >= 1


def test_repository_error_causes_repository_exception_and_rollback() -> None:
    uow = FakeMaintenanceUnitOfWork(fail_commit=True)

    with pytest.raises(RepositoryException):
        CreateMaintenancePlanUseCase(unit_of_work=uow).execute(
            CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4())
        )

    assert uow.commits == 1
    assert uow.rollbacks >= 1


def test_historical_flow_snapshot_integrity_and_history_response() -> None:
    uow = FakeMaintenanceUnitOfWork()
    plan_id, requirement_id = _create_plan_with_requirement(
        uow,
        target_type="TECHNICAL_COMPONENT",
        title="Pitch-propeller-like inspection",
        instructions="Instruction A",
    )

    wo_a = CreateWorkOrderUseCase(unit_of_work=uow).execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan_id,
            maintenance_requirement_id=requirement_id,
            title="WO-A",
            description="First completion",
        )
    )
    OpenWorkOrderUseCase(unit_of_work=uow).execute(OpenWorkOrderRequest(work_order_id=wo_a.work_order.id))
    StartWorkOrderUseCase(unit_of_work=uow).execute(
        StartWorkOrderRequest(work_order_id=wo_a.work_order.id, started_at=_utc(2030, 2, 1, 8))
    )
    CompleteWorkOrderUseCase(unit_of_work=uow).execute(
        CompleteWorkOrderRequest(
            work_order_id=wo_a.work_order.id,
            completed_at=_utc(2030, 2, 1, 10),
            notes="Instruction A",
            finding="Record A finding",
            replacement_may_be_required=False,
        )
    )

    UpdateMaintenanceRequirementUseCase(unit_of_work=uow).execute(
        UpdateMaintenanceRequirementRequest(
            maintenance_plan_id=plan_id,
            maintenance_requirement_id=requirement_id,
            instructions="Instruction B",
            interval_type="CALENDAR_MONTHS",
            interval_value=6,
        )
    )

    wo_b = CreateWorkOrderUseCase(unit_of_work=uow).execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan_id,
            maintenance_requirement_id=requirement_id,
            title="WO-B",
            description="Second completion",
        )
    )
    OpenWorkOrderUseCase(unit_of_work=uow).execute(OpenWorkOrderRequest(work_order_id=wo_b.work_order.id))
    StartWorkOrderUseCase(unit_of_work=uow).execute(
        StartWorkOrderRequest(work_order_id=wo_b.work_order.id, started_at=_utc(2030, 8, 1, 8))
    )
    CompleteWorkOrderUseCase(unit_of_work=uow).execute(
        CompleteWorkOrderRequest(
            work_order_id=wo_b.work_order.id,
            completed_at=_utc(2030, 8, 1, 10),
            notes="Instruction B",
            finding="Record B finding",
            replacement_may_be_required=True,
        )
    )

    plan = uow.maintenance_plan_repository.get_by_id(plan_id)
    assert plan is not None
    assert plan.get_requirement(requirement_id) is not None
    assert plan.get_requirement(requirement_id).instructions == "Instruction B"

    history = GetMaintenanceHistoryUseCase(unit_of_work=uow).execute(
        GetMaintenanceHistoryRequest(
            target_type="TECHNICAL_COMPONENT",
            target_id=plan.maintenance_target.target_id,
        )
    )

    assert len(history.records) == 2
    assert history.records[0].notes == "Instruction A"
    assert history.records[1].notes == "Instruction B"
    assert history.records[0].finding == "Record A finding"
    assert history.records[1].finding == "Record B finding"


def test_maritime_validation_scenarios_cover_component_and_vessel_targets() -> None:
    uow = FakeMaintenanceUnitOfWork()

    plan_component_id, req_component_id = _create_plan_with_requirement(
        uow,
        target_type="TECHNICAL_COMPONENT",
        title="Propulsion-engine-like oil maintenance",
        instructions="Oil instruction",
    )
    plan_vessel_id, req_vessel_id = _create_plan_with_requirement(
        uow,
        target_type="VESSEL",
        title="Hull planking inspection",
        instructions="Hull instruction",
    )

    comp_work = CreateWorkOrderUseCase(unit_of_work=uow).execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan_component_id,
            maintenance_requirement_id=req_component_id,
            title="Component WO",
            description="Component task",
        )
    )
    OpenWorkOrderUseCase(unit_of_work=uow).execute(OpenWorkOrderRequest(work_order_id=comp_work.work_order.id))
    StartWorkOrderUseCase(unit_of_work=uow).execute(
        StartWorkOrderRequest(work_order_id=comp_work.work_order.id, started_at=_utc(2031, 1, 1, 8))
    )
    CompleteWorkOrderUseCase(unit_of_work=uow).execute(
        CompleteWorkOrderRequest(
            work_order_id=comp_work.work_order.id,
            completed_at=_utc(2031, 1, 1, 10),
            finding="possible replacement required",
            replacement_may_be_required=True,
        )
    )

    vessel_work = CreateWorkOrderUseCase(unit_of_work=uow).execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan_vessel_id,
            maintenance_requirement_id=req_vessel_id,
            title="Vessel WO",
            description="Hull task",
        )
    )
    OpenWorkOrderUseCase(unit_of_work=uow).execute(OpenWorkOrderRequest(work_order_id=vessel_work.work_order.id))
    StartWorkOrderUseCase(unit_of_work=uow).execute(
        StartWorkOrderRequest(work_order_id=vessel_work.work_order.id, started_at=_utc(2031, 1, 2, 8))
    )
    CompleteWorkOrderUseCase(unit_of_work=uow).execute(
        CompleteWorkOrderRequest(
            work_order_id=vessel_work.work_order.id,
            completed_at=_utc(2031, 1, 2, 10),
            finding="Hull inspection completed",
            replacement_may_be_required=False,
        )
    )

    component_plan = uow.maintenance_plan_repository.get_by_id(plan_component_id)
    vessel_plan = uow.maintenance_plan_repository.get_by_id(plan_vessel_id)
    assert component_plan is not None and vessel_plan is not None

    component_history = GetMaintenanceHistoryUseCase(unit_of_work=uow).execute(
        GetMaintenanceHistoryRequest(
            target_type="TECHNICAL_COMPONENT",
            target_id=component_plan.maintenance_target.target_id,
        )
    )
    vessel_history = GetMaintenanceHistoryUseCase(unit_of_work=uow).execute(
        GetMaintenanceHistoryRequest(
            target_type="VESSEL",
            target_id=vessel_plan.maintenance_target.target_id,
        )
    )

    assert len(component_history.records) == 1
    assert component_history.records[0].replacement_may_be_required is True
    assert len(vessel_history.records) == 1
    assert vessel_history.records[0].target_type == "VESSEL"


def test_public_response_dtos_are_immutable_and_domain_safe() -> None:
    uow = FakeMaintenanceUnitOfWork()
    plan_id, requirement_id = _create_plan_with_requirement(uow)

    work = CreateWorkOrderUseCase(unit_of_work=uow).execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=plan_id,
            maintenance_requirement_id=requirement_id,
            title="DTO safety WO",
            description="DTO safety",
        )
    )

    assert is_dataclass(type(work.work_order))
    assert isinstance(work.work_order.id, UUID)
    assert isinstance(work.work_order.target_type, str)
    assert not isinstance(work.work_order, WorkOrder)

    plan = uow.maintenance_plan_repository.get_by_id(plan_id)
    assert plan is not None
    assert isinstance(plan.maintenance_target.target_type, MaintenanceTargetType)
