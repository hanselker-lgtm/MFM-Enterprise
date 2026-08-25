from __future__ import annotations

from uuid import UUID

from mfm.application.features.organizations import (
    GetOrganizationFeature,
    GetOrganizationRequest,
    ListOrganizationsFeature,
    ListOrganizationsRequest,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationNumber


class InMemoryOrganizationRepository:
    def __init__(self, store: dict[UUID, Organization]) -> None:
        self._store = store

    def add(self, organization: Organization) -> None:
        self._store[organization.id.value] = organization

    def get_by_id(self, organization_id: UUID) -> Organization | None:
        return self._store.get(organization_id)

    def list(self) -> list[Organization]:
        return list(self._store.values())


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        super().__init__()
        self._organizations: dict[UUID, Organization] = {}

    def _start_scope(self) -> None:
        self.organization_repository = InMemoryOrganizationRepository(self._organizations)

    def _commit_impl(self) -> None:
        pass

    def _rollback_impl(self) -> None:
        pass

    def _flush_impl(self) -> None:
        pass

    def _close_impl(self) -> None:
        pass


def test_list_organizations_returns_empty_when_none_exist() -> None:
    uow = FakeUnitOfWork()
    response = ListOrganizationsFeature(unit_of_work=uow).execute(ListOrganizationsRequest())
    assert response.organizations == ()


def test_list_and_get_organization_return_created_organization() -> None:
    uow = FakeUnitOfWork()
    organization = Organization(organization_number=OrganizationNumber("ORG-0100"), name="Test Assoc")
    with uow:
        uow.organization_repository.add(organization)

    list_response = ListOrganizationsFeature(unit_of_work=uow).execute(ListOrganizationsRequest())
    assert len(list_response.organizations) == 1
    assert list_response.organizations[0].name == "Test Assoc"

    get_response = GetOrganizationFeature(unit_of_work=uow).execute(
        GetOrganizationRequest(organization_id=organization.id.value)
    )
    assert get_response.organization.organization_number == "ORG-0100"
