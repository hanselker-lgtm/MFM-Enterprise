from __future__ import annotations

from datetime import UTC
from datetime import datetime
from uuid import UUID

import pytest

from mfm.domain.organization.exceptions import DuplicateOrganizationNumberError
from mfm.domain.organization.exceptions import InvalidOrganizationNameError
from mfm.domain.organization.exceptions import InvalidOrganizationStatusTransitionError
from mfm.domain.organization.exceptions import OrganizationSerializationError
from mfm.domain.organization.organization import Organization
from mfm.domain.organization.organization_id import OrganizationId
from mfm.domain.organization.organization_id import OrganizationNumber
from mfm.domain.organization.organization_status import OrganizationStatus
from mfm.domain.organization.organization_type import OrganizationType


@pytest.fixture(autouse=True)
def clear_registry() -> None:
    Organization._clear_registry_for_tests()


def test_create_organization() -> None:
    organization = Organization(
        organization_number=OrganizationNumber("org-1000"),
        name="  Maritime Association  ",
        organization_type=OrganizationType.ASSOCIATION,
    )

    assert isinstance(organization.id, OrganizationId)
    assert isinstance(organization.id.value, UUID)
    assert organization.organization_number == OrganizationNumber("ORG-1000")
    assert organization.name == "Maritime Association"
    assert organization.organization_type is OrganizationType.ASSOCIATION
    assert organization.status is OrganizationStatus.ACTIVE
    assert organization.created_at.tzinfo == UTC
    assert organization.updated_at.tzinfo == UTC


def test_rename() -> None:
    organization = Organization(
        organization_number=OrganizationNumber("ORG-1001"),
        name="Old Name",
        organization_type=OrganizationType.COMPANY,
    )

    before = organization.updated_at
    organization.rename("  New Name  ")

    assert organization.name == "New Name"
    assert organization.updated_at >= before


def test_activate_from_inactive() -> None:
    organization = Organization(
        organization_number=OrganizationNumber("ORG-1002"),
        name="Inactive Org",
        organization_type=OrganizationType.COMMITTEE,
        status=OrganizationStatus.INACTIVE,
    )

    organization.activate()

    assert organization.status is OrganizationStatus.ACTIVE


def test_deactivate_from_active() -> None:
    organization = Organization(
        organization_number=OrganizationNumber("ORG-1003"),
        name="Active Org",
        organization_type=OrganizationType.FOUNDATION,
    )

    organization.deactivate()

    assert organization.status is OrganizationStatus.INACTIVE


def test_archive() -> None:
    organization = Organization(
        organization_number=OrganizationNumber("ORG-1004"),
        name="Archive Org",
        organization_type=OrganizationType.OTHER,
    )

    organization.archive()

    assert organization.status is OrganizationStatus.ARCHIVED


def test_invalid_name() -> None:
    with pytest.raises(InvalidOrganizationNameError):
        Organization(
            organization_number=OrganizationNumber("ORG-1005"),
            name="   ",
            organization_type=OrganizationType.ASSOCIATION,
        )


def test_invalid_transitions_archived_cannot_activate() -> None:
    organization = Organization(
        organization_number=OrganizationNumber("ORG-1006"),
        name="Archived Org",
        organization_type=OrganizationType.ASSOCIATION,
        status=OrganizationStatus.ARCHIVED,
    )

    with pytest.raises(InvalidOrganizationStatusTransitionError):
        organization.activate()


def test_invalid_transitions_archived_cannot_deactivate() -> None:
    organization = Organization(
        organization_number=OrganizationNumber("ORG-1007"),
        name="Archived Org 2",
        organization_type=OrganizationType.COMPANY,
        status=OrganizationStatus.ARCHIVED,
    )

    with pytest.raises(InvalidOrganizationStatusTransitionError):
        organization.deactivate()


def test_organization_number_is_unique() -> None:
    _ = Organization(
        organization_number=OrganizationNumber("ORG-1008"),
        name="A",
        organization_type=OrganizationType.ASSOCIATION,
    )

    with pytest.raises(DuplicateOrganizationNumberError):
        Organization(
            organization_number=OrganizationNumber("org-1008"),
            name="B",
            organization_type=OrganizationType.COMPANY,
        )


def test_equality() -> None:
    org_id = OrganizationId.new()
    created_at = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
    updated_at = datetime(2026, 1, 2, 0, 0, tzinfo=UTC)

    left = Organization(
        id=org_id,
        organization_number=OrganizationNumber("ORG-1009"),
        name="Equal Org",
        organization_type=OrganizationType.FOUNDATION,
        status=OrganizationStatus.INACTIVE,
        created_at=created_at,
        updated_at=updated_at,
    )
    right = Organization(
        id=org_id,
        organization_number=OrganizationNumber("ORG-1009"),
        name="Equal Org",
        organization_type=OrganizationType.FOUNDATION,
        status=OrganizationStatus.INACTIVE,
        created_at=created_at,
        updated_at=updated_at,
    )

    assert left == right


def test_serialization_round_trip() -> None:
    organization = Organization(
        organization_number=OrganizationNumber("ORG-1010"),
        name="Serializable Org",
        organization_type=OrganizationType.COMMITTEE,
        status=OrganizationStatus.INACTIVE,
    )

    payload = organization.to_dict()
    restored = Organization.from_dict(payload)

    assert restored == organization
    assert restored.organization_number == OrganizationNumber("ORG-1010")


def test_serialization_rejects_invalid_data() -> None:
    with pytest.raises(OrganizationSerializationError):
        Organization.from_dict({"name": "missing fields"})
