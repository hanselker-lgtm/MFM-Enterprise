from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from datetime import date
from typing import Any
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.events.domain_event_dispatcher import DomainEventDispatcher
from mfm.application.events.event_handler import EventHandler
from mfm.application.organization.assign_role import AssignRoleRequest
from mfm.application.organization.assign_role import AssignRoleUseCase
from mfm.application.organization.assign_role import RoleAssignedEvent
from mfm.application.organization.create_board import BoardCreatedEvent
from mfm.application.organization.create_board import BoardMemberInput
from mfm.application.organization.create_board import CreateBoardRequest
from mfm.application.organization.create_board import CreateBoardUseCase
from mfm.application.organization.create_committee import CommitteeCreatedEvent
from mfm.application.organization.create_committee import CommitteeMemberInput
from mfm.application.organization.create_committee import CreateCommitteeRequest
from mfm.application.organization.create_committee import CreateCommitteeUseCase
from mfm.application.organization.create_organization import BusinessRuleViolation
from mfm.application.organization.create_organization import CreateOrganizationRequest
from mfm.application.organization.create_organization import CreateOrganizationUseCase
from mfm.application.organization.create_organization import OrganizationCreatedEvent
from mfm.application.organization.create_organization import RepositoryException
from mfm.application.organization.create_organization import ValidationException
from mfm.application.organization.register_volunteer import RegisterVolunteerRequest
from mfm.application.organization.register_volunteer import RegisterVolunteerUseCase
from mfm.application.organization.register_volunteer import VolunteerCertificateInput
from mfm.application.organization.register_volunteer import VolunteerRegisteredEvent
from mfm.application.organization.update_organization import OrganizationUpdatedEvent
from mfm.application.organization.update_organization import UpdateOrganizationRequest
from mfm.application.organization.update_organization import UpdateOrganizationUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.common.domain_event import DomainEvent
from mfm.domain.organization.board import Board
from mfm.domain.organization.committee import Committee
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType
from mfm.domain.organization.role import Role
from mfm.domain.organization.role_code import RoleCode
from mfm.domain.organization.role_type import RoleType
from mfm.domain.organization.volunteer import Volunteer


class EventCollector(EventHandler):
    def __init__(self) -> None:
        self.events: list[DomainEvent] = []

    def handle(self, event: DomainEvent) -> None:
        self.events.append(event)


class InMemoryOrganizationRepository:
    def __init__(
        self,
        store: dict[UUID, Organization],
        *,
        fail_on_add: bool = False,
        fail_on_update: bool = False,
    ) -> None:
        self._store = store
        self._fail_on_add = fail_on_add
        self._fail_on_update = fail_on_update

    def add(self, organization: Organization) -> None:
        if self._fail_on_add:
            raise RuntimeError("organization add failed")
        self._store[organization.id.value] = organization

    def get_by_id(self, organization_id: UUID) -> Organization | None:
        return self._store.get(organization_id)

    def update(self, organization: Organization) -> None:
        if self._fail_on_update:
            raise RuntimeError("organization update failed")
        self._store[organization.id.value] = organization

    def delete(self, organization_id: UUID) -> None:
        self._store.pop(organization_id, None)

    def exists(self, organization_id: UUID) -> bool:
        return organization_id in self._store

    def list(self) -> list[Organization]:
        return list(self._store.values())

    def search(self, text: str) -> list[Organization]:
        lowered = text.casefold()
        return [
            item
            for item in self._store.values()
            if lowered in item.organization_number.value.casefold()
            or lowered in item.name.casefold()
        ]


class InMemoryBoardRepository:
    def __init__(self, store: dict[UUID, Board], *, fail_on_add: bool = False) -> None:
        self._store = store
        self._fail_on_add = fail_on_add

    def add(self, board: Board) -> None:
        if self._fail_on_add:
            raise RuntimeError("board add failed")
        self._store[board.id] = board

    def get_by_id(self, board_id: UUID) -> Board | None:
        return self._store.get(board_id)

    def update(self, board: Board) -> None:
        self._store[board.id] = board

    def delete(self, board_id: UUID) -> None:
        self._store.pop(board_id, None)

    def exists(self, board_id: UUID) -> bool:
        return board_id in self._store

    def list(self) -> list[Board]:
        return list(self._store.values())

    def search(self, text: str) -> list[Board]:
        lowered = text.casefold()
        return [item for item in self._store.values() if lowered in item.name.casefold()]


class InMemoryCommitteeRepository:
    def __init__(
        self,
        store: dict[UUID, Committee],
        *,
        fail_on_add: bool = False,
    ) -> None:
        self._store = store
        self._fail_on_add = fail_on_add

    def add(self, committee: Committee) -> None:
        if self._fail_on_add:
            raise RuntimeError("committee add failed")
        self._store[committee.id.value] = committee

    def get_by_id(self, committee_id: UUID) -> Committee | None:
        return self._store.get(committee_id)

    def update(self, committee: Committee) -> None:
        self._store[committee.id.value] = committee

    def delete(self, committee_id: UUID) -> None:
        self._store.pop(committee_id, None)

    def exists(self, committee_id: UUID) -> bool:
        return committee_id in self._store

    def list(self) -> list[Committee]:
        return list(self._store.values())

    def search(self, text: str) -> list[Committee]:
        lowered = text.casefold()
        return [
            item
            for item in self._store.values()
            if lowered in item.name.casefold() or lowered in item.purpose.casefold()
        ]


class InMemoryVolunteerRepository:
    def __init__(
        self,
        store: dict[UUID, Volunteer],
        *,
        fail_on_add: bool = False,
    ) -> None:
        self._store = store
        self._fail_on_add = fail_on_add

    def add(self, volunteer: Volunteer) -> None:
        if self._fail_on_add:
            raise RuntimeError("volunteer add failed")
        self._store[volunteer.id.value] = volunteer

    def get_by_id(self, volunteer_id: UUID) -> Volunteer | None:
        return self._store.get(volunteer_id)

    def update(self, volunteer: Volunteer) -> None:
        self._store[volunteer.id.value] = volunteer

    def delete(self, volunteer_id: UUID) -> None:
        self._store.pop(volunteer_id, None)

    def exists(self, volunteer_id: UUID) -> bool:
        return volunteer_id in self._store

    def list(self) -> list[Volunteer]:
        return list(self._store.values())

    def search(self, text: str) -> list[Volunteer]:
        lowered = text.casefold()
        return [
            item
            for item in self._store.values()
            if lowered in ",".join(str(skill) for skill in item.skills).casefold()
        ]


class InMemoryRoleRepository:
    def __init__(
        self,
        store: dict[UUID, Role],
        *,
        fail_on_update: bool = False,
    ) -> None:
        self._store = store
        self._fail_on_update = fail_on_update

    def add(self, role: Role) -> None:
        self._store[role.id.value] = role

    def get_by_id(self, role_id: UUID) -> Role | None:
        return self._store.get(role_id)

    def update(self, role: Role) -> None:
        if self._fail_on_update:
            raise RuntimeError("role update failed")
        self._store[role.id.value] = role

    def delete(self, role_id: UUID) -> None:
        self._store.pop(role_id, None)

    def exists(self, role_id: UUID) -> bool:
        return role_id in self._store

    def list(self) -> list[Role]:
        return list(self._store.values())

    def search(self, text: str) -> list[Role]:
        lowered = text.casefold()
        return [item for item in self._store.values() if lowered in item.name.casefold()]


@dataclass(slots=True)
class _NoopRepo:
    def add(self, entity: Any) -> None:
        _ = entity


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        *,
        fail_organization_add: bool = False,
        fail_organization_update: bool = False,
        fail_board_add: bool = False,
        fail_committee_add: bool = False,
        fail_volunteer_add: bool = False,
        fail_role_update: bool = False,
    ) -> None:
        super().__init__()
        self.fail_organization_add = fail_organization_add
        self.fail_organization_update = fail_organization_update
        self.fail_board_add = fail_board_add
        self.fail_committee_add = fail_committee_add
        self.fail_volunteer_add = fail_volunteer_add
        self.fail_role_update = fail_role_update

        self.organizations: dict[UUID, Organization] = {}
        self.boards: dict[UUID, Board] = {}
        self.committees: dict[UUID, Committee] = {}
        self.volunteers: dict[UUID, Volunteer] = {}
        self.roles: dict[UUID, Role] = {}

        self.commits = 0
        self.rollbacks = 0

    def _start_scope(self) -> None:
        self._snapshot = (
            deepcopy(self.organizations),
            deepcopy(self.boards),
            deepcopy(self.committees),
            deepcopy(self.volunteers),
            deepcopy(self.roles),
        )

        self.organization_repository = InMemoryOrganizationRepository(
            self.organizations,
            fail_on_add=self.fail_organization_add,
            fail_on_update=self.fail_organization_update,
        )
        self.board_repository = InMemoryBoardRepository(
            self.boards,
            fail_on_add=self.fail_board_add,
        )
        self.committee_repository = InMemoryCommitteeRepository(
            self.committees,
            fail_on_add=self.fail_committee_add,
        )
        self.volunteer_repository = InMemoryVolunteerRepository(
            self.volunteers,
            fail_on_add=self.fail_volunteer_add,
        )
        self.role_repository = InMemoryRoleRepository(
            self.roles,
            fail_on_update=self.fail_role_update,
        )

        self.contact_repository = _NoopRepo()
        self.member_repository = _NoopRepo()
        self.membership_repository = _NoopRepo()
        self.invoice_repository = _NoopRepo()
        self.payment_repository = _NoopRepo()
        self.journal_repository = _NoopRepo()

    def _commit_impl(self) -> None:
        self.commits += 1

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        organizations, boards, committees, volunteers, roles = self._snapshot
        self.organizations = organizations
        self.boards = boards
        self.committees = committees
        self.volunteers = volunteers
        self.roles = roles

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


@pytest.fixture(autouse=True)
def clear_registries() -> None:
    Organization._clear_registry_for_tests()
    Role._clear_registry_for_tests()


def _event_collector(dispatcher: DomainEventDispatcher, event_type: type[DomainEvent]) -> EventCollector:
    collector = EventCollector()
    dispatcher.register(event_type, collector)
    return collector


def test_create_organization_happy_path_commit_and_event() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, OrganizationCreatedEvent)
    use_case = CreateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)

    response = use_case.execute(
        CreateOrganizationRequest(
            organization_number="ORG-APP-001",
            name="MFM Test Org",
            organization_type=OrganizationType.ASSOCIATION,
        )
    )

    assert uow.commits == 1
    assert response.organization_id in uow.organizations
    assert len(collector.events) == 1


def test_create_organization_validation_error() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    use_case = CreateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(ValidationException):
        use_case.execute(
            CreateOrganizationRequest(
                organization_number="",
                name="X",
                organization_type=OrganizationType.ASSOCIATION,
            )
        )


def test_create_organization_duplicate_entity() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    use_case = CreateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)

    existing = Organization(
        organization_number=OrganizationNumber("ORG-APP-002"),
        name="Existing",
        organization_type=OrganizationType.ASSOCIATION,
    )
    uow.organizations[existing.id.value] = existing

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            CreateOrganizationRequest(
                organization_number="ORG-APP-002",
                name="Duplicate",
                organization_type=OrganizationType.ASSOCIATION,
            )
        )


def test_create_organization_rollback_on_repository_error() -> None:
    uow = FakeUnitOfWork(fail_organization_add=True)
    dispatcher = DomainEventDispatcher()
    use_case = CreateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(RepositoryException):
        use_case.execute(
            CreateOrganizationRequest(
                organization_number="ORG-APP-003",
                name="Failing",
                organization_type=OrganizationType.ASSOCIATION,
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_update_organization_happy_path_commit_and_event() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, OrganizationUpdatedEvent)
    organization = Organization(
        organization_number=OrganizationNumber("ORG-APP-004"),
        name="Before",
        organization_type=OrganizationType.ASSOCIATION,
    )
    uow.organizations[organization.id.value] = organization

    use_case = UpdateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)
    response = use_case.execute(
        UpdateOrganizationRequest(
            organization_id=organization.id.value,
            name="After",
            status=OrganizationStatus.INACTIVE,
        )
    )

    assert uow.commits == 1
    assert response.name == "After"
    assert response.status is OrganizationStatus.INACTIVE
    assert len(collector.events) == 1


def test_update_organization_validation_duplicate_and_rollback() -> None:
    uow = FakeUnitOfWork(fail_organization_update=True)
    dispatcher = DomainEventDispatcher()

    first = Organization(
        organization_number=OrganizationNumber("ORG-APP-004A"),
        name="First",
        organization_type=OrganizationType.ASSOCIATION,
    )
    second = Organization(
        organization_number=OrganizationNumber("ORG-APP-004B"),
        name="Second",
        organization_type=OrganizationType.ASSOCIATION,
    )
    uow.organizations[first.id.value] = first
    uow.organizations[second.id.value] = second

    use_case = UpdateOrganizationUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(ValidationException):
        use_case.execute(
            UpdateOrganizationRequest(
                organization_id=first.id.value,
                name="   ",
            )
        )

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            UpdateOrganizationRequest(
                organization_id=first.id.value,
                organization_number="ORG-APP-004B",
            )
        )

    with pytest.raises(RepositoryException):
        use_case.execute(
            UpdateOrganizationRequest(
                organization_id=first.id.value,
                name="Will Rollback",
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 2


def test_create_board_happy_path_duplicate_validation_and_event() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, BoardCreatedEvent)
    organization = Organization(
        organization_number=OrganizationNumber("ORG-APP-005"),
        name="Board Org",
        organization_type=OrganizationType.ASSOCIATION,
    )
    uow.organizations[organization.id.value] = organization

    use_case = CreateBoardUseCase(unit_of_work=uow, dispatcher=dispatcher)

    request = CreateBoardRequest(
        organization_id=organization.id.value,
        name="Main Board",
        term_start=date(2026, 1, 1),
        term_end=date(2026, 12, 31),
        members=(
            BoardMemberInput(
                member_id=uuid4(),
                role="CHAIR",
                appointed_on=date(2026, 1, 1),
                is_chair=True,
            ),
        ),
    )
    response = use_case.execute(request)

    assert uow.commits == 1
    assert response.board_id in uow.boards
    assert len(collector.events) == 1

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(request)


def test_create_board_rollback_on_error() -> None:
    uow = FakeUnitOfWork(fail_board_add=True)
    dispatcher = DomainEventDispatcher()
    organization = Organization(
        organization_number=OrganizationNumber("ORG-APP-006"),
        name="Board Org",
        organization_type=OrganizationType.ASSOCIATION,
    )
    uow.organizations[organization.id.value] = organization

    use_case = CreateBoardUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(RepositoryException):
        use_case.execute(
            CreateBoardRequest(
                organization_id=organization.id.value,
                name="Main Board",
                term_start=date(2026, 1, 1),
                term_end=date(2026, 12, 31),
                members=(
                    BoardMemberInput(
                        member_id=uuid4(),
                        role="CHAIR",
                        appointed_on=date(2026, 1, 1),
                        is_chair=True,
                    ),
                ),
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_create_board_validation_error() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    organization = Organization(
        organization_number=OrganizationNumber("ORG-APP-006A"),
        name="Board Org",
        organization_type=OrganizationType.ASSOCIATION,
    )
    uow.organizations[organization.id.value] = organization

    use_case = CreateBoardUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(ValidationException):
        use_case.execute(
            CreateBoardRequest(
                organization_id=organization.id.value,
                name="Main Board",
                term_start=date(2026, 1, 1),
                term_end=date(2026, 12, 31),
                members=(),
            )
        )


def test_create_committee_happy_path_duplicate_validation_and_event() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, CommitteeCreatedEvent)
    organization = Organization(
        organization_number=OrganizationNumber("ORG-APP-007"),
        name="Committee Org",
        organization_type=OrganizationType.ASSOCIATION,
    )
    uow.organizations[organization.id.value] = organization

    use_case = CreateCommitteeUseCase(unit_of_work=uow, dispatcher=dispatcher)
    request = CreateCommitteeRequest(
        organization_id=organization.id.value,
        name="Safety Committee",
        purpose="Safety",
        members=(
            CommitteeMemberInput(
                reference_id=uuid4(),
                function_title="Lead",
                joined_at=date(2026, 1, 1),
            ),
        ),
    )

    response = use_case.execute(request)

    assert uow.commits == 1
    assert response.committee_id in uow.committees
    assert len(collector.events) == 1

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(request)


def test_create_committee_rollback_on_error() -> None:
    uow = FakeUnitOfWork(fail_committee_add=True)
    dispatcher = DomainEventDispatcher()
    organization = Organization(
        organization_number=OrganizationNumber("ORG-APP-007A"),
        name="Committee Org",
        organization_type=OrganizationType.ASSOCIATION,
    )
    uow.organizations[organization.id.value] = organization

    use_case = CreateCommitteeUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(RepositoryException):
        use_case.execute(
            CreateCommitteeRequest(
                organization_id=organization.id.value,
                name="Safety Committee",
                purpose="Safety",
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_register_volunteer_happy_path_duplicate_validation_and_event() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, VolunteerRegisteredEvent)

    use_case = RegisterVolunteerUseCase(unit_of_work=uow, dispatcher=dispatcher)

    request = RegisterVolunteerRequest(
        contact_id=uuid4(),
        member_id=uuid4(),
        is_available=True,
        max_hours_per_week=6,
        preferred_days=("MONDAY",),
        skills=("FIRST AID",),
        certificates=(VolunteerCertificateInput(name="CPR", expires_at=date(2027, 1, 1)),),
        joined_at=date(2026, 1, 1),
    )

    response = use_case.execute(request)

    assert uow.commits == 1
    assert response.volunteer_id in uow.volunteers
    assert len(collector.events) == 1

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(request)

    with pytest.raises(ValidationException):
        use_case.execute(
            RegisterVolunteerRequest(
                contact_id=uuid4(),
                member_id=None,
                is_available=True,
                max_hours_per_week=-1,
                preferred_days=("MONDAY",),
                skills=("FIRST AID",),
                certificates=(),
                joined_at=date(2026, 1, 1),
            )
        )


def test_register_volunteer_rollback_on_error() -> None:
    uow = FakeUnitOfWork(fail_volunteer_add=True)
    dispatcher = DomainEventDispatcher()
    use_case = RegisterVolunteerUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(RepositoryException):
        use_case.execute(
            RegisterVolunteerRequest(
                contact_id=uuid4(),
                member_id=None,
                is_available=True,
                max_hours_per_week=4,
                preferred_days=(),
                skills=("FIRST AID",),
                certificates=(),
                joined_at=date(2026, 1, 1),
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 1


def test_assign_role_happy_path_validation_duplicate_and_event() -> None:
    uow = FakeUnitOfWork()
    dispatcher = DomainEventDispatcher()
    collector = _event_collector(dispatcher, RoleAssignedEvent)

    role = Role(
        role_code=RoleCode("OPS-APP-001"),
        name="Operations",
        category=RoleType.OPERATIONAL,
    )
    uow.roles[role.id.value] = role

    use_case = AssignRoleUseCase(unit_of_work=uow, dispatcher=dispatcher)

    assignee_id = uuid4()
    request = AssignRoleRequest(
        role_id=role.id.value,
        assignee_id=assignee_id,
        organization_id=uuid4(),
        valid_from=date(2026, 1, 1),
    )

    response = use_case.execute(request)

    assert uow.commits == 1
    assert response.role_id == role.id.value
    assert len(uow.roles[role.id.value].assignments) == 1
    assert len(collector.events) == 1

    with pytest.raises(ValidationException):
        use_case.execute(
            AssignRoleRequest(
                role_id=role.id.value,
                assignee_id=uuid4(),
                organization_id=uuid4(),
                valid_from=date(2026, 2, 1),
                valid_to=date(2026, 1, 1),
            )
        )

    with pytest.raises(BusinessRuleViolation):
        use_case.execute(
            AssignRoleRequest(
                role_id=role.id.value,
                assignee_id=assignee_id,
                organization_id=request.organization_id,
                valid_from=date(2026, 1, 15),
            )
        )


def test_assign_role_rollback_on_repository_failure() -> None:
    uow = FakeUnitOfWork(fail_role_update=True)
    dispatcher = DomainEventDispatcher()

    role = Role(
        role_code=RoleCode("OPS-APP-002"),
        name="Operations 2",
        category=RoleType.OPERATIONAL,
    )
    uow.roles[role.id.value] = role

    use_case = AssignRoleUseCase(unit_of_work=uow, dispatcher=dispatcher)

    with pytest.raises(RepositoryException):
        use_case.execute(
            AssignRoleRequest(
                role_id=role.id.value,
                assignee_id=uuid4(),
                organization_id=uuid4(),
                valid_from=date(2026, 1, 1),
            )
        )

    assert uow.commits == 0
    assert uow.rollbacks == 1
