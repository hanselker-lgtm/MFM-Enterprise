from __future__ import annotations

from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.organization.exceptions import DuplicateVolunteerCertificateError
from mfm.domain.organization.exceptions import DuplicateVolunteerSkillError
from mfm.domain.organization.exceptions import InvalidVolunteerReferenceError
from mfm.domain.organization.exceptions import InvalidVolunteerStatusTransitionError
from mfm.domain.organization.exceptions import VolunteerCertificateNotFoundError
from mfm.domain.organization.exceptions import VolunteerSerializationError
from mfm.domain.organization.exceptions import VolunteerSkillNotFoundError
from mfm.domain.organization.volunteer import Volunteer
from mfm.domain.organization.volunteer_availability import VolunteerAvailability
from mfm.domain.organization.volunteer_id import VolunteerId
from mfm.domain.organization.volunteer_skill import VolunteerSkill
from mfm.domain.organization.volunteer_status import VolunteerStatus


def _availability() -> VolunteerAvailability:
    return VolunteerAvailability(
        is_available=True,
        max_hours_per_week=8,
        preferred_days=("mon", "wed"),
    )


def test_create_volunteer() -> None:
    contact_id = uuid4()
    volunteer = Volunteer(
        contact_id=contact_id,
        availability=_availability(),
    )

    assert isinstance(volunteer.id, VolunteerId)
    assert isinstance(volunteer.id.value, UUID)
    assert volunteer.contact_id == contact_id
    assert volunteer.member_id is None
    assert volunteer.status is VolunteerStatus.ACTIVE
    assert volunteer.left_at is None


def test_contact_is_required() -> None:
    with pytest.raises(InvalidVolunteerReferenceError):
        Volunteer(  # type: ignore[arg-type]
            contact_id="not-a-uuid",
            availability=_availability(),
        )


def test_member_is_optional() -> None:
    member_id = uuid4()
    volunteer = Volunteer(
        contact_id=uuid4(),
        member_id=member_id,
        availability=_availability(),
    )

    assert volunteer.member_id == member_id


def test_skills_cannot_duplicate() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        availability=_availability(),
    )

    volunteer.add_skill(VolunteerSkill("First Aid"))

    with pytest.raises(DuplicateVolunteerSkillError):
        volunteer.add_skill(VolunteerSkill(" first aid "))


def test_add_remove_skill() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        availability=_availability(),
    )
    skill = VolunteerSkill("Navigation")

    volunteer.add_skill(skill)
    assert skill in volunteer.skills

    volunteer.remove_skill(skill)
    assert skill not in volunteer.skills

    with pytest.raises(VolunteerSkillNotFoundError):
        volunteer.remove_skill(skill)


def test_certificates_can_have_expiry() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        availability=_availability(),
    )

    volunteer.add_certificate("Radio License", expires_at=date(2027, 5, 1))

    assert len(volunteer.certificates) == 1
    assert volunteer.certificates[0].expires_at == date(2027, 5, 1)


def test_duplicate_certificate_rejected() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        availability=_availability(),
    )

    volunteer.add_certificate("Safety Course")
    with pytest.raises(DuplicateVolunteerCertificateError):
        volunteer.add_certificate(" safety course ")


def test_remove_certificate() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        availability=_availability(),
    )

    volunteer.add_certificate("VHF")
    volunteer.remove_certificate("vhf")

    assert volunteer.certificates == []

    with pytest.raises(VolunteerCertificateNotFoundError):
        volunteer.remove_certificate("vhf")


def test_deactivate_activate_retire_with_history() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        availability=_availability(),
        joined_at=date(2026, 1, 1),
    )

    volunteer.deactivate(on_date=date(2026, 3, 1))
    assert volunteer.status is VolunteerStatus.INACTIVE
    assert volunteer.left_at == date(2026, 3, 1)

    volunteer.activate()
    assert volunteer.status is VolunteerStatus.ACTIVE
    assert volunteer.left_at is None

    volunteer.retire(on_date=date(2026, 6, 1))
    assert volunteer.status is VolunteerStatus.RETIRED
    assert volunteer.left_at == date(2026, 6, 1)


def test_retired_cannot_be_activated_or_deactivated() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        availability=_availability(),
        status=VolunteerStatus.RETIRED,
        joined_at=date(2026, 1, 1),
        left_at=date(2026, 2, 1),
    )

    with pytest.raises(InvalidVolunteerStatusTransitionError):
        volunteer.activate()

    with pytest.raises(InvalidVolunteerStatusTransitionError):
        volunteer.deactivate(on_date=date(2026, 3, 1))


def test_equality() -> None:
    volunteer_id = VolunteerId.new()
    contact_id = uuid4()
    member_id = uuid4()

    left = Volunteer(
        id=volunteer_id,
        contact_id=contact_id,
        member_id=member_id,
        availability=_availability(),
        status=VolunteerStatus.INACTIVE,
        skills=[VolunteerSkill("Engine")],
        joined_at=date(2026, 1, 1),
        left_at=date(2026, 2, 1),
    )
    right = Volunteer(
        id=volunteer_id,
        contact_id=contact_id,
        member_id=member_id,
        availability=_availability(),
        status=VolunteerStatus.INACTIVE,
        skills=[VolunteerSkill("engine")],
        joined_at=date(2026, 1, 1),
        left_at=date(2026, 2, 1),
    )

    assert left == right


def test_serialization_round_trip() -> None:
    volunteer = Volunteer(
        contact_id=uuid4(),
        member_id=uuid4(),
        availability=_availability(),
        skills=[VolunteerSkill("Rescue")],
        joined_at=date(2026, 1, 1),
    )
    volunteer.add_certificate("First Aid", expires_at=date(2028, 1, 1))

    payload = volunteer.to_dict()
    restored = Volunteer.from_dict(payload)

    assert restored == volunteer


def test_serialization_invalid_payload() -> None:
    with pytest.raises(VolunteerSerializationError):
        Volunteer.from_dict({"contact_id": str(uuid4())})
