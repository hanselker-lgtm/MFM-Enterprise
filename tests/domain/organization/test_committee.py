from __future__ import annotations

from datetime import UTC
from datetime import date
from datetime import datetime
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.organization.committee import Committee
from mfm.domain.organization.committee_id import CommitteeId
from mfm.domain.organization.committee_member import CommitteeMember
from mfm.domain.organization.committee_status import CommitteeStatus
from mfm.domain.organization.exceptions import CommitteeMemberNotFoundError
from mfm.domain.organization.exceptions import CommitteeSerializationError
from mfm.domain.organization.exceptions import DuplicateCommitteeMemberError
from mfm.domain.organization.exceptions import InvalidCommitteeNameError
from mfm.domain.organization.organization_id import OrganizationId


def _member(
    *,
    reference_id: UUID | None = None,
    function_title: str = "Member",
    joined_at: date = date(2026, 1, 1),
    left_at: date | None = None,
) -> CommitteeMember:
    return CommitteeMember(
        reference_id=reference_id or uuid4(),
        function_title=function_title,
        joined_at=joined_at,
        left_at=left_at,
    )


def test_create_committee() -> None:
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="  Audit Committee  ",
        purpose="  Review controls and governance  ",
        members=[_member(function_title="Chair")],
    )

    assert isinstance(committee.id, CommitteeId)
    assert committee.name == "Audit Committee"
    assert committee.purpose == "Review controls and governance"
    assert committee.status is CommitteeStatus.ACTIVE
    assert committee.created_at.tzinfo == UTC
    assert committee.updated_at.tzinfo == UTC


def test_invalid_name() -> None:
    with pytest.raises(InvalidCommitteeNameError):
        Committee(
            organization_id=OrganizationId.new(),
            name="   ",
            purpose="Purpose",
            members=[_member()],
        )


def test_members_must_not_be_duplicated() -> None:
    ref = uuid4()
    with pytest.raises(DuplicateCommitteeMemberError):
        Committee(
            organization_id=OrganizationId.new(),
            name="Ops",
            purpose="Purpose",
            members=[_member(reference_id=ref), _member(reference_id=ref)],
        )


def test_rename_updates_timestamp() -> None:
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="Safety",
        purpose="Purpose",
        members=[_member()],
    )

    before = committee.updated_at
    committee.rename("Safety and Quality")

    assert committee.name == "Safety and Quality"
    assert committee.updated_at >= before


def test_change_purpose_updates_timestamp() -> None:
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="Training",
        purpose="Initial",
        members=[_member()],
    )

    before = committee.updated_at
    committee.change_purpose("Develop competence and standards")

    assert committee.purpose == "Develop competence and standards"
    assert committee.updated_at >= before


def test_add_member() -> None:
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="Harbor",
        purpose="Ops",
        members=[_member()],
    )

    new_member = _member(function_title="Secretary")
    committee.add_member(new_member)

    assert new_member in committee.members


def test_remove_member_preserves_history() -> None:
    tracked = _member()
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="Events",
        purpose="Event planning",
        members=[tracked],
    )

    committee.remove_member(tracked.reference_id, on_date=date(2026, 6, 1))

    assert len(committee.members) == 1
    assert tracked.left_at == date(2026, 6, 1)


def test_remove_member_not_found() -> None:
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="Comms",
        purpose="Communication",
        members=[_member()],
    )

    with pytest.raises(CommitteeMemberNotFoundError):
        committee.remove_member(uuid4(), on_date=date(2026, 6, 1))


def test_activate_and_deactivate() -> None:
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="Finance",
        purpose="Budgeting",
        status=CommitteeStatus.INACTIVE,
        members=[_member()],
    )

    committee.activate()
    assert committee.status is CommitteeStatus.ACTIVE

    committee.deactivate()
    assert committee.status is CommitteeStatus.INACTIVE


def test_equality() -> None:
    committee_id = CommitteeId.new()
    organization_id = OrganizationId.new()
    member = _member(reference_id=uuid4())
    created = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
    updated = datetime(2026, 1, 2, 0, 0, tzinfo=UTC)

    left = Committee(
        id=committee_id,
        organization_id=organization_id,
        name="Equality Committee",
        purpose="Purpose",
        status=CommitteeStatus.ACTIVE,
        members=[member],
        created_at=created,
        updated_at=updated,
    )
    right = Committee(
        id=committee_id,
        organization_id=organization_id,
        name="Equality Committee",
        purpose="Purpose",
        status=CommitteeStatus.ACTIVE,
        members=[
            CommitteeMember(
                reference_id=member.reference_id,
                function_title=member.function_title,
                joined_at=member.joined_at,
                left_at=member.left_at,
            )
        ],
        created_at=created,
        updated_at=updated,
    )

    assert left == right


def test_serialization_round_trip() -> None:
    committee = Committee(
        organization_id=OrganizationId.new(),
        name="Serialized",
        purpose="Serialized purpose",
        status=CommitteeStatus.INACTIVE,
        members=[_member(function_title="Convener")],
    )

    payload = committee.to_dict()
    restored = Committee.from_dict(payload)

    assert restored == committee


def test_serialization_invalid_payload() -> None:
    with pytest.raises(CommitteeSerializationError):
        Committee.from_dict({"name": "missing fields"})
