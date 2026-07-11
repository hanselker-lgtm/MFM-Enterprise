from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import date
from datetime import datetime
from datetime import timezone
from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

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
from mfm.application.features.maintenance.cancel_work_order_feature import (
    CancelWorkOrderFeature,
)
from mfm.application.features.maintenance.cancel_work_order_feature import (
    CancelWorkOrderRequest,
)
from mfm.application.features.maintenance.complete_work_order_feature import (
    CompleteWorkOrderFeature,
)
from mfm.application.features.maintenance.complete_work_order_feature import (
    CompleteWorkOrderRequest,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    BusinessRuleViolation as FeatureBusinessRuleViolation,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    CreateMaintenancePlanFeature,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    CreateMaintenancePlanRequest,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    RepositoryException as FeatureRepositoryException,
)
from mfm.application.features.maintenance.create_maintenance_plan_feature import (
    ValidationException as FeatureValidationException,
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
from mfm.application.maintenance.add_maintenance_requirement import (
    AddMaintenanceRequirementUseCase,
)
from mfm.application.maintenance.calculate_due_maintenance import (
    CalculateDueMaintenanceUseCase,
)
from mfm.application.maintenance.cancel_work_order import CancelWorkOrderUseCase
from mfm.application.maintenance.complete_work_order import CompleteWorkOrderUseCase
from mfm.application.maintenance.create_maintenance_plan import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.maintenance.create_maintenance_plan import (
    CreateMaintenancePlanUseCase,
)
from mfm.application.maintenance.create_maintenance_plan import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.maintenance.create_maintenance_plan import (
    ValidationException as ServiceValidationException,
)
from mfm.application.maintenance.create_work_order import CreateWorkOrderUseCase
from mfm.application.maintenance.get_maintenance_history import GetMaintenanceHistoryUseCase
from mfm.application.maintenance.open_work_order import OpenWorkOrderUseCase
from mfm.application.maintenance.start_work_order import StartWorkOrderUseCase
from mfm.application.maintenance.update_maintenance_requirement import (
    UpdateMaintenanceRequirementUseCase,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.infrastructure.persistence.sqlite.sqlite_maintenance_plan_repository import (
    SQLiteMaintenancePlanRepository,
)
from mfm.infrastructure.persistence.sqlite.sqlite_work_order_repository import (
    SQLiteWorkOrderRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        if self._error is not None:
            raise self._error
        return self._response


class SqliteMaintenanceApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
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


@pytest.fixture()
def sqlite_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)

    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


def _utc(year: int, month: int, day: int, hour: int) -> datetime:
    return datetime(year, month, day, hour)


def _build_feature_stack(uow: SqliteMaintenanceApplicationUnitOfWork) -> dict[str, object]:
    return {
        "create_plan": CreateMaintenancePlanFeature(
            service=CreateMaintenancePlanUseCase(unit_of_work=uow)
        ),
        "add_requirement": AddMaintenanceRequirementFeature(
            service=AddMaintenanceRequirementUseCase(unit_of_work=uow)
        ),
        "update_requirement": UpdateMaintenanceRequirementFeature(
            service=UpdateMaintenanceRequirementUseCase(unit_of_work=uow)
        ),
        "calculate_due": CalculateDueMaintenanceFeature(
            service=CalculateDueMaintenanceUseCase(unit_of_work=uow)
        ),
        "create_work_order": CreateWorkOrderFeature(
            service=CreateWorkOrderUseCase(unit_of_work=uow)
        ),
        "open_work_order": OpenWorkOrderFeature(
            service=OpenWorkOrderUseCase(unit_of_work=uow)
        ),
        "start_work_order": StartWorkOrderFeature(
            service=StartWorkOrderUseCase(unit_of_work=uow)
        ),
        "complete_work_order": CompleteWorkOrderFeature(
            service=CompleteWorkOrderUseCase(unit_of_work=uow)
        ),
        "cancel_work_order": CancelWorkOrderFeature(
            service=CancelWorkOrderUseCase(unit_of_work=uow)
        ),
        "history": GetMaintenanceHistoryFeature(
            service=GetMaintenanceHistoryUseCase(unit_of_work=uow)
        ),
    }


def test_create_plan_feature_for_vessel_and_component_and_immutable_request(
    sqlite_session: Session,
) -> None:
    uow = SqliteMaintenanceApplicationUnitOfWork(sqlite_session)
    feature = CreateMaintenancePlanFeature(service=CreateMaintenancePlanUseCase(unit_of_work=uow))

    vessel_request = CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4())
    component_request = CreateMaintenancePlanRequest(
        target_type="TECHNICAL_COMPONENT",
        target_id=uuid4(),
    )

    vessel_response = feature.execute(vessel_request)
    component_response = feature.execute(component_request)

    assert vessel_response.plan.target.target_type == "VESSEL"
    assert component_response.plan.target.target_type == "TECHNICAL_COMPONENT"

    with pytest.raises(FrozenInstanceError):
        vessel_request.target_type = "X"  # type: ignore[misc]


def test_create_plan_feature_validation_and_exception_mapping() -> None:
    feature = CreateMaintenancePlanFeature(service=StubService(response=None))

    with pytest.raises(FeatureValidationException):
        feature.execute(CreateMaintenancePlanRequest(target_type="", target_id=uuid4()))

    duplicate = CreateMaintenancePlanFeature(
        service=StubService(error=ServiceBusinessRuleViolation("already exists"))
    )
    with pytest.raises(FeatureBusinessRuleViolation):
        duplicate.execute(
            CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4())
        )

    repo_error = CreateMaintenancePlanFeature(
        service=StubService(error=ServiceRepositoryException("failed"))
    )
    with pytest.raises(FeatureRepositoryException):
        repo_error.execute(
            CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4())
        )


def test_add_and_update_requirement_feature_and_duplicate_mapping(
    sqlite_session: Session,
) -> None:
    stack = _build_feature_stack(SqliteMaintenanceApplicationUnitOfWork(sqlite_session))
    create_plan = stack["create_plan"]
    add_requirement = stack["add_requirement"]
    update_requirement = stack["update_requirement"]

    created = create_plan.execute(
        CreateMaintenancePlanRequest(target_type="TECHNICAL_COMPONENT", target_id=uuid4())
    )

    added = add_requirement.execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=created.plan.id,
            title="12 month oil maintenance",
            description="Generic oil requirement",
            maintenance_type="PREVENTIVE",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
            instructions="Instruction A",
            notes="Note A",
        )
    )

    requirement_id = added.plan.requirements[0].id

    with pytest.raises(FeatureBusinessRuleViolation):
        add_requirement.execute(
            AddMaintenanceRequirementRequest(
                maintenance_plan_id=created.plan.id,
                title="12 month oil maintenance",
                description="Generic oil requirement",
                maintenance_type="PREVENTIVE",
                interval_type="CALENDAR_MONTHS",
                interval_value=12,
                due_basis="CALENDAR_DATE",
            )
        )

    updated = update_requirement.execute(
        UpdateMaintenanceRequirementRequest(
            maintenance_plan_id=created.plan.id,
            maintenance_requirement_id=requirement_id,
            instructions="Instruction B",
            interval_type="CALENDAR_MONTHS",
            interval_value=6,
        )
    )

    assert updated.plan.requirements[0].instructions == "Instruction B"
    assert updated.plan.requirements[0].interval.interval_value == 6


def test_due_feature_explicit_input_and_mapping(sqlite_session: Session) -> None:
    stack = _build_feature_stack(SqliteMaintenanceApplicationUnitOfWork(sqlite_session))

    created = stack["create_plan"].execute(
        CreateMaintenancePlanRequest(target_type="TECHNICAL_COMPONENT", target_id=uuid4())
    )
    added = stack["add_requirement"].execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=created.plan.id,
            title="Propulsion-engine-like maintenance",
            description="Generic requirement",
            maintenance_type="PREVENTIVE",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
        )
    )

    requirement_id = added.plan.requirements[0].id

    due_initial = stack["calculate_due"].execute(
        CalculateDueMaintenanceRequest(
            maintenance_plan_id=created.plan.id,
            as_of_date=date(2031, 1, 1),
            running_hours_by_requirement_id={requirement_id: 0},
        )
    )
    assert due_initial.due_requirements == ()


def test_work_order_lifecycle_features_and_not_found_mapping(
    sqlite_session: Session,
) -> None:
    stack = _build_feature_stack(SqliteMaintenanceApplicationUnitOfWork(sqlite_session))

    created = stack["create_plan"].execute(
        CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4())
    )
    added = stack["add_requirement"].execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=created.plan.id,
            title="Hull planking inspection",
            description="Generic hull requirement",
            maintenance_type="INSPECTION",
            interval_type="CALENDAR_YEARS",
            interval_value=1,
            due_basis="CALENDAR_DATE",
            instructions="Instruction A",
        )
    )

    requirement_id = added.plan.requirements[0].id

    work = stack["create_work_order"].execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=created.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-A",
            description="First work order",
        )
    )

    stack["open_work_order"].execute(OpenWorkOrderRequest(work_order_id=work.work_order.id))
    stack["start_work_order"].execute(
        StartWorkOrderRequest(work_order_id=work.work_order.id, started_at=_utc(2031, 1, 2, 9))
    )
    completed = stack["complete_work_order"].execute(
        CompleteWorkOrderRequest(
            work_order_id=work.work_order.id,
            completed_at=_utc(2031, 1, 2, 11),
            performer_type="MEMBER",
            performer_id_or_external_key="member-7",
            performer_display_name_snapshot="Member Seven",
            notes="Instruction A",
            finding="possible replacement required",
            replacement_may_be_required=True,
        )
    )

    assert completed.work_order.status == "COMPLETED"
    assert completed.work_order.maintenance_record is not None
    assert completed.work_order.maintenance_record.finding == "possible replacement required"
    assert completed.work_order.maintenance_record.replacement_may_be_required is True

    with pytest.raises(FeatureBusinessRuleViolation):
        stack["open_work_order"].execute(OpenWorkOrderRequest(work_order_id=uuid4()))


def test_cancel_feature_and_invalid_lifecycle_mapping(sqlite_session: Session) -> None:
    stack = _build_feature_stack(SqliteMaintenanceApplicationUnitOfWork(sqlite_session))

    created = stack["create_plan"].execute(
        CreateMaintenancePlanRequest(target_type="TECHNICAL_COMPONENT", target_id=uuid4())
    )
    added = stack["add_requirement"].execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=created.plan.id,
            title="Pitch-propeller-like inspection",
            description="Generic pitch requirement",
            maintenance_type="INSPECTION",
            interval_type="CALENDAR_MONTHS",
            interval_value=6,
            due_basis="CALENDAR_DATE",
        )
    )

    work = stack["create_work_order"].execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=created.plan.id,
            maintenance_requirement_id=added.plan.requirements[0].id,
            title="WO-cancel",
            description="Cancelled work order",
        )
    )

    cancelled = stack["cancel_work_order"].execute(
        CancelWorkOrderRequest(work_order_id=work.work_order.id, notes="Cancelled")
    )
    assert cancelled.work_order.status == "CANCELLED"

    with pytest.raises(FeatureBusinessRuleViolation):
        stack["start_work_order"].execute(
            StartWorkOrderRequest(
                work_order_id=work.work_order.id,
                started_at=_utc(2031, 3, 1, 9),
            )
        )


def test_history_feature_preserves_historical_context(sqlite_session: Session) -> None:
    stack = _build_feature_stack(SqliteMaintenanceApplicationUnitOfWork(sqlite_session))

    created = stack["create_plan"].execute(
        CreateMaintenancePlanRequest(target_type="TECHNICAL_COMPONENT", target_id=uuid4())
    )
    added = stack["add_requirement"].execute(
        AddMaintenanceRequirementRequest(
            maintenance_plan_id=created.plan.id,
            title="Inspection requirement",
            description="Generic requirement",
            maintenance_type="INSPECTION",
            interval_type="CALENDAR_MONTHS",
            interval_value=12,
            due_basis="CALENDAR_DATE",
            instructions="Instruction A",
        )
    )

    requirement_id = added.plan.requirements[0].id

    wo_a = stack["create_work_order"].execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=created.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-A",
            description="Record A",
        )
    )
    stack["open_work_order"].execute(OpenWorkOrderRequest(work_order_id=wo_a.work_order.id))
    stack["start_work_order"].execute(
        StartWorkOrderRequest(work_order_id=wo_a.work_order.id, started_at=_utc(2031, 4, 1, 9))
    )
    stack["complete_work_order"].execute(
        CompleteWorkOrderRequest(
            work_order_id=wo_a.work_order.id,
            completed_at=_utc(2031, 4, 1, 11),
            notes="Instruction A",
            finding="Record A finding",
        )
    )

    stack["update_requirement"].execute(
        UpdateMaintenanceRequirementRequest(
            maintenance_plan_id=created.plan.id,
            maintenance_requirement_id=requirement_id,
            instructions="Instruction B",
            interval_type="CALENDAR_MONTHS",
            interval_value=6,
        )
    )

    wo_b = stack["create_work_order"].execute(
        CreateWorkOrderRequest(
            maintenance_plan_id=created.plan.id,
            maintenance_requirement_id=requirement_id,
            title="WO-B",
            description="Record B",
        )
    )
    stack["open_work_order"].execute(OpenWorkOrderRequest(work_order_id=wo_b.work_order.id))
    stack["start_work_order"].execute(
        StartWorkOrderRequest(work_order_id=wo_b.work_order.id, started_at=_utc(2031, 10, 1, 9))
    )
    stack["complete_work_order"].execute(
        CompleteWorkOrderRequest(
            work_order_id=wo_b.work_order.id,
            completed_at=_utc(2031, 10, 1, 11),
            notes="Instruction B",
            finding="Record B finding",
        )
    )

    history = stack["history"].execute(
        GetMaintenanceHistoryRequest(
            target_type="TECHNICAL_COMPONENT",
            target_id=created.plan.target.target_id,
        )
    )

    assert len(history.records) == 2
    assert history.records[0].notes == "Instruction A"
    assert history.records[1].notes == "Instruction B"
    assert history.records[0].finding == "Record A finding"
    assert history.records[1].finding == "Record B finding"
    assert history.plans[0].requirements[0].instructions == "Instruction B"


def test_feature_request_and_response_are_public_safe_and_no_domain_leakage(
    sqlite_session: Session,
) -> None:
    stack = _build_feature_stack(SqliteMaintenanceApplicationUnitOfWork(sqlite_session))

    created = stack["create_plan"].execute(
        CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4())
    )

    assert isinstance(created.plan.id, UUID)
    assert isinstance(created.plan.target.target_type, str)
    assert isinstance(created.plan.target.target_id, UUID)

    with pytest.raises(FrozenInstanceError):
        created.plan.status = "X"  # type: ignore[misc]


def test_unexpected_service_exception_maps_to_repository_exception() -> None:
    feature = CreateMaintenancePlanFeature(service=StubService(error=RuntimeError("boom")))

    with pytest.raises(FeatureRepositoryException):
        feature.execute(CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4()))


def test_service_validation_exception_maps_to_feature_validation_exception() -> None:
    feature = CreateMaintenancePlanFeature(
        service=StubService(error=ServiceValidationException("invalid"))
    )

    with pytest.raises(FeatureValidationException):
        feature.execute(CreateMaintenancePlanRequest(target_type="VESSEL", target_id=uuid4()))
