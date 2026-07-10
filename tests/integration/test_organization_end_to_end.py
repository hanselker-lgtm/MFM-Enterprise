from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.events.event_handler import EventHandler
from mfm.application.features.organization.assign_role_feature import AssignRoleFeature
from mfm.application.features.organization.assign_role_feature import AssignRoleRequest
from mfm.application.features.organization.create_board_feature import BoardMemberInput
from mfm.application.features.organization.create_board_feature import CreateBoardFeature
from mfm.application.features.organization.create_board_feature import CreateBoardRequest
from mfm.application.features.organization.create_committee_feature import CommitteeMemberInput
from mfm.application.features.organization.create_committee_feature import CreateCommitteeFeature
from mfm.application.features.organization.create_committee_feature import CreateCommitteeRequest
from mfm.application.features.organization.create_organization_feature import CreateOrganizationFeature
from mfm.application.features.organization.create_organization_feature import CreateOrganizationRequest
from mfm.application.features.organization.register_volunteer_feature import RegisterVolunteerFeature
from mfm.application.features.organization.register_volunteer_feature import RegisterVolunteerRequest
from mfm.application.features.organization.register_volunteer_feature import VolunteerCertificateInput
from mfm.application.features.organization.update_organization_feature import UpdateOrganizationFeature
from mfm.application.features.organization.update_organization_feature import UpdateOrganizationRequest
from mfm.application.organization.assign_role import AssignRoleUseCase
from mfm.application.organization.assign_role import RoleAssignedEvent
from mfm.application.organization.create_board import BoardCreatedEvent
from mfm.application.organization.create_board import CreateBoardUseCase
from mfm.application.organization.create_committee import CommitteeCreatedEvent
from mfm.application.organization.create_committee import CreateCommitteeUseCase
from mfm.application.organization.create_organization import CreateOrganizationUseCase
from mfm.application.organization.create_organization import OrganizationCreatedEvent
from mfm.application.organization.register_volunteer import RegisterVolunteerUseCase
from mfm.application.organization.register_volunteer import VolunteerRegisteredEvent
from mfm.application.organization.update_organization import OrganizationUpdatedEvent
from mfm.application.organization.update_organization import UpdateOrganizationUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.common.enums import ContactStatus
from mfm.database.models.base_model import BaseModel
from mfm.database.models.contact_model import ContactModel
from mfm.database.models.member_model import MemberModel
from mfm.domain.member.member_status import MemberStatus
from mfm.domain.organization.exceptions import InvalidOrganizationStatusTransitionError
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType
from mfm.domain.organization.role import Role
from mfm.domain.organization.role_code import RoleCode
from mfm.domain.organization.role_type import RoleType
from mfm.infrastructure.persistence.sqlite.sqlite_board_repository import SQLiteBoardRepository
from mfm.infrastructure.persistence.sqlite.sqlite_committee_repository import SQLiteCommitteeRepository
from mfm.infrastructure.persistence.sqlite.sqlite_organization_repository import SQLiteOrganizationRepository
from mfm.infrastructure.persistence.sqlite.sqlite_role_repository import SQLiteRoleRepository
from mfm.infrastructure.persistence.sqlite.sqlite_volunteer_repository import SQLiteVolunteerRepository
from mfm.repositories.unit_of_work import UnitOfWork


class EventCollector(EventHandler):
    def __init__(self) -> None:
        self.events: list[DomainEvent] = []

    def handle(self, event: DomainEvent) -> None:
        self.events.append(event)


class SqliteApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)

        self.organization_repository = SQLiteOrganizationRepository(self._persistence_uow)
        self.board_repository = SQLiteBoardRepository(self._persistence_uow)
        self.committee_repository = SQLiteCommitteeRepository(self._persistence_uow)
        self.volunteer_repository = SQLiteVolunteerRepository(self._persistence_uow)
        self.role_repository = SQLiteRoleRepository(self._persistence_uow)

        # Unused by organization use cases but required by abstract contract footprint.
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
        # Session lifecycle is managed by the surrounding pytest fixture.
        return None


@dataclass(frozen=True, slots=True)
class WorkflowGraph:
    organization_id: UUID
    board_id: UUID
    committee_id: UUID
    volunteer_id: UUID
    role_id: UUID
    contact_id: UUID
    member_id: UUID


@dataclass(frozen=True, slots=True)
class FeatureStack:
    create_organization: CreateOrganizationFeature
    create_board: CreateBoardFeature
    create_committee: CreateCommitteeFeature
    register_volunteer: RegisterVolunteerFeature
    assign_role: AssignRoleFeature
    update_organization: UpdateOrganizationFeature


@pytest.fixture(autouse=True)
def clear_domain_registries() -> None:
    Organization._clear_registry_for_tests()
    Role._clear_registry_for_tests()


@pytest.fixture()
def sqlite_session(tmp_path: Path) -> Session:
    db_path = tmp_path / "org-010.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)

    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


def _seed_contact_and_member(session: Session) -> tuple[UUID, UUID]:
    contact = ContactModel(
        contact_number=f"C-{uuid4().hex[:6].upper()}",
        status=ContactStatus.ACTIVE,
    )
    session.add(contact)
    session.flush()

    member = MemberModel(
        contact_id=contact.id,
        member_number=f"M-{uuid4().hex[:6].upper()}",
        status=MemberStatus.ACTIVE,
        join_date=date(2026, 1, 1),
    )
    session.add(member)
    session.flush()

    return contact.id, member.id


def _build_stack(session: Session, dispatcher: DomainEventDispatcher) -> FeatureStack:
    app_uow = SqliteApplicationUnitOfWork(session)

    return FeatureStack(
        create_organization=CreateOrganizationFeature(
            service=CreateOrganizationUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        create_board=CreateBoardFeature(
            service=CreateBoardUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        create_committee=CreateCommitteeFeature(
            service=CreateCommitteeUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        register_volunteer=RegisterVolunteerFeature(
            service=RegisterVolunteerUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        assign_role=AssignRoleFeature(
            service=AssignRoleUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
        update_organization=UpdateOrganizationFeature(
            service=UpdateOrganizationUseCase(unit_of_work=app_uow, dispatcher=dispatcher)
        ),
    )


def _register_event_collectors(dispatcher: DomainEventDispatcher) -> EventCollector:
    collector = EventCollector()
    dispatcher.register(OrganizationCreatedEvent, collector)
    dispatcher.register(BoardCreatedEvent, collector)
    dispatcher.register(CommitteeCreatedEvent, collector)
    dispatcher.register(VolunteerRegisteredEvent, collector)
    dispatcher.register(RoleAssignedEvent, collector)
    dispatcher.register(OrganizationUpdatedEvent, collector)
    return collector


def _persist_role_for_assignment(
    *,
    session: Session,
    organization_id: UUID,
) -> UUID:
    persistence_uow = UnitOfWork(session)
    role_repository = SQLiteRoleRepository(persistence_uow)

    role = Role(
        role_code=RoleCode(f"OPS-{uuid4().hex[:5].upper()}"),
        name="Operations Coordinator",
        description="Coordinates operational tasks",
        category=RoleType.OPERATIONAL,
    )
    role.assign(
        assignee_id=uuid4(),
        organization_id=organization_id,
        valid_from=date(2025, 1, 1),
        valid_to=date(2025, 12, 31),
    )

    role_repository.add(role)
    persistence_uow.commit()
    return role.id.value


def _run_workflow_1(
    *,
    stack: FeatureStack,
    session: Session,
    contact_id: UUID,
    member_id: UUID,
) -> WorkflowGraph:
    create_org_response = stack.create_organization.execute(
        CreateOrganizationRequest(
            organization_number=f"ORG-E2E-{uuid4().hex[:6].upper()}",
            name="Maritime Federation Integration",
            organization_type=OrganizationType.ASSOCIATION,
        )
    )

    create_board_response = stack.create_board.execute(
        CreateBoardRequest(
            organization_id=create_org_response.organization_id,
            name="National Board",
            term_start=date(2026, 1, 1),
            term_end=date(2026, 12, 31),
            members=(
                BoardMemberInput(
                    member_id=member_id,
                    role="CHAIRMAN",
                    appointed_on=date(2026, 1, 1),
                    is_chair=True,
                ),
            ),
        )
    )

    create_committee_response = stack.create_committee.execute(
        CreateCommitteeRequest(
            organization_id=create_org_response.organization_id,
            name="Safety Committee",
            purpose="Safety and compliance",
            members=(
                CommitteeMemberInput(
                    reference_id=member_id,
                    function_title="Chairman",
                    joined_at=date(2026, 1, 2),
                ),
            ),
        )
    )

    register_volunteer_response = stack.register_volunteer.execute(
        RegisterVolunteerRequest(
            contact_id=contact_id,
            member_id=member_id,
            is_available=True,
            max_hours_per_week=6,
            preferred_days=("MONDAY", "THURSDAY"),
            skills=("FIRST AID", "SAFETY"),
            certificates=(
                VolunteerCertificateInput(name="CPR", expires_at=date(2027, 1, 1)),
            ),
            joined_at=date(2026, 1, 1),
        )
    )

    role_id = _persist_role_for_assignment(
        session=session,
        organization_id=create_org_response.organization_id,
    )

    assign_role_response = stack.assign_role.execute(
        AssignRoleRequest(
            role_id=role_id,
            assignee_id=register_volunteer_response.contact_id,
            organization_id=create_org_response.organization_id,
            valid_from=date(2026, 1, 10),
        )
    )

    return WorkflowGraph(
        organization_id=create_org_response.organization_id,
        board_id=create_board_response.board_id,
        committee_id=create_committee_response.committee_id,
        volunteer_id=register_volunteer_response.volunteer_id,
        role_id=assign_role_response.role_id,
        contact_id=register_volunteer_response.contact_id,
        member_id=member_id,
    )


def _reload_graph(session: Session, graph: WorkflowGraph):
    reload_uow = UnitOfWork(session)
    org_repo = SQLiteOrganizationRepository(reload_uow)
    board_repo = SQLiteBoardRepository(reload_uow)
    committee_repo = SQLiteCommitteeRepository(reload_uow)
    volunteer_repo = SQLiteVolunteerRepository(reload_uow)
    role_repo = SQLiteRoleRepository(reload_uow)

    organization = org_repo.get_by_id(graph.organization_id)
    board = board_repo.get_by_id(graph.board_id)
    committee = committee_repo.get_by_id(graph.committee_id)
    volunteer = volunteer_repo.get_by_id(graph.volunteer_id)
    role = role_repo.get_by_id(graph.role_id)

    return organization, board, committee, volunteer, role


def test_org_010_workflow_1_complete_graph_with_persist_reload(
    sqlite_session: Session,
) -> None:
    contact_id, member_id = _seed_contact_and_member(sqlite_session)

    dispatcher = DomainEventDispatcher()
    collector = _register_event_collectors(dispatcher)
    stack = _build_stack(sqlite_session, dispatcher)

    graph = _run_workflow_1(
        stack=stack,
        session=sqlite_session,
        contact_id=contact_id,
        member_id=member_id,
    )

    reload_session = Session(sqlite_session.get_bind())
    try:
        organization, board, committee, volunteer, role = _reload_graph(reload_session, graph)

        assert organization is not None
        assert organization.id == OrganizationId(graph.organization_id)
        assert organization.status is OrganizationStatus.ACTIVE

        assert board is not None
        assert board.organization_id == organization.id
        assert any(member.is_chair for member in board.members)

        assert committee is not None
        assert committee.organization_id == organization.id
        assert len(committee.members) == 1

        assert volunteer is not None
        assert volunteer.contact_id == graph.contact_id
        assert volunteer.member_id == graph.member_id
        assert volunteer.availability.preferred_days == ("MONDAY", "THURSDAY")

        assert role is not None
        assert any(
            assignment.assignee_id == graph.contact_id
            and assignment.organization_id == graph.organization_id
            for assignment in role.assignments
        )
    finally:
        reload_session.close()

    assert len(collector.events) == 5
    assert any(isinstance(event, OrganizationCreatedEvent) for event in collector.events)
    assert any(isinstance(event, BoardCreatedEvent) for event in collector.events)
    assert any(isinstance(event, CommitteeCreatedEvent) for event in collector.events)
    assert any(isinstance(event, VolunteerRegisteredEvent) for event in collector.events)
    assert any(isinstance(event, RoleAssignedEvent) for event in collector.events)


def test_org_010_workflow_2_deactivate_organization_keeps_children_consistent(
    sqlite_session: Session,
) -> None:
    contact_id, member_id = _seed_contact_and_member(sqlite_session)

    dispatcher = DomainEventDispatcher()
    stack = _build_stack(sqlite_session, dispatcher)

    graph = _run_workflow_1(
        stack=stack,
        session=sqlite_session,
        contact_id=contact_id,
        member_id=member_id,
    )

    response = stack.update_organization.execute(
        UpdateOrganizationRequest(
            organization_id=graph.organization_id,
            status=OrganizationStatus.INACTIVE,
        )
    )

    assert response.status == "INACTIVE"

    reload_session = Session(sqlite_session.get_bind())
    try:
        organization, board, committee, volunteer, role = _reload_graph(reload_session, graph)

        assert organization is not None
        assert organization.status is OrganizationStatus.INACTIVE

        assert board is not None
        assert board.organization_id == organization.id
        assert len(board.members) == 1

        assert committee is not None
        assert committee.organization_id == organization.id
        assert len(committee.members) == 1

        assert volunteer is not None
        assert volunteer.contact_id == graph.contact_id

        assert role is not None
        assert len(role.assignments) == 2
    finally:
        reload_session.close()


def test_org_010_workflow_3_archive_organization_and_verify_invariants(
    sqlite_session: Session,
) -> None:
    contact_id, member_id = _seed_contact_and_member(sqlite_session)

    dispatcher = DomainEventDispatcher()
    stack = _build_stack(sqlite_session, dispatcher)

    graph = _run_workflow_1(
        stack=stack,
        session=sqlite_session,
        contact_id=contact_id,
        member_id=member_id,
    )

    response = stack.update_organization.execute(
        UpdateOrganizationRequest(
            organization_id=graph.organization_id,
            status=OrganizationStatus.ARCHIVED,
        )
    )

    assert response.status == "ARCHIVED"

    reload_uow = UnitOfWork(sqlite_session)
    organization = SQLiteOrganizationRepository(reload_uow).get_by_id(graph.organization_id)

    assert organization is not None
    assert organization.status is OrganizationStatus.ARCHIVED

    with pytest.raises(InvalidOrganizationStatusTransitionError):
        organization.activate()

    with pytest.raises(InvalidOrganizationStatusTransitionError):
        organization.deactivate()


def test_org_010_workflow_4_repository_roundtrip_reload_and_equality(
    sqlite_session: Session,
) -> None:
    contact_id, member_id = _seed_contact_and_member(sqlite_session)

    dispatcher = DomainEventDispatcher()
    stack = _build_stack(sqlite_session, dispatcher)

    graph = _run_workflow_1(
        stack=stack,
        session=sqlite_session,
        contact_id=contact_id,
        member_id=member_id,
    )

    first_reload_session = Session(sqlite_session.get_bind())
    second_reload_session = Session(sqlite_session.get_bind())
    try:
        first_graph = _reload_graph(first_reload_session, graph)
        second_graph = _reload_graph(second_reload_session, graph)

        for left, right in zip(first_graph, second_graph, strict=True):
            assert left is not None
            assert right is not None
            assert left == right
    finally:
        first_reload_session.close()
        second_reload_session.close()
