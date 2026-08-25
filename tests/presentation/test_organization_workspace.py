from __future__ import annotations

from uuid import UUID
from uuid import uuid4

from mfm.presentation.organizations.organization_controller import OrganizationController
from mfm.presentation.organizations.organization_viewmodels import (
    CreateOrganizationCommandViewModel,
    UpdateOrganizationCommandViewModel,
)
from mfm.presentation.organizations.organization_workspace import OrganizationWorkspace


class _FakeOrgDTO:
    def __init__(self, organization_id, number, name, org_type="ASSOCIATION", status="ACTIVE"):
        self.organization_id = organization_id
        self.organization_number = number
        self.name = name
        self.organization_type = org_type
        self.status = status


class _FakeCreateOrganizationFeature:
    def __init__(self, store):
        self._store = store

    def execute(self, request):
        org_id = uuid4()
        self._store[org_id] = _FakeOrgDTO(org_id, request.organization_number, request.name)

        class _Response:
            organization_id = org_id
            organization_number = request.organization_number
            name = request.name

        return _Response()


class _FakeUpdateOrganizationFeature:
    def __init__(self, store):
        self._store = store

    def execute(self, request):
        dto = self._store[request.organization_id]
        if request.name is not None:
            dto.name = request.name
        if request.status is not None:
            dto.status = request.status

        class _Response:
            pass

        return _Response()


class _FakeListOrganizationsFeature:
    def __init__(self, store):
        self._store = store

    def execute(self, request):
        class _Response:
            organizations = tuple(self._store.values())

        return _Response()


def test_organization_workspace_builds_and_shows_created_org(qapp) -> None:
    store: dict[UUID, _FakeOrgDTO] = {}
    controller = OrganizationController(
        create_organization_feature=_FakeCreateOrganizationFeature(store),
        update_organization_feature=_FakeUpdateOrganizationFeature(store),
        list_organizations_feature=_FakeListOrganizationsFeature(store),
    )

    org_id = controller.create_organization(
        CreateOrganizationCommandViewModel(
            organization_number="ORG-1", name="Test Org", organization_type="ASSOCIATION"
        )
    )

    workspace = OrganizationWorkspace(controller=controller)
    assert workspace._list.count() == 1

    controller.update_organization(
        UpdateOrganizationCommandViewModel(organization_id=org_id, name="Renamed", status="INACTIVE")
    )
    lst = controller.load_organization_list()
    assert lst.items[0].name == "Renamed"
    assert lst.items[0].status == "INACTIVE"
