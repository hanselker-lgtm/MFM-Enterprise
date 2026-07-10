"""Volunteer aggregate."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import UTC
from datetime import date
from datetime import datetime
from typing import Any
from typing import Mapping
from uuid import UUID

from mfm.domain.organization.exceptions import DuplicateVolunteerCertificateError
from mfm.domain.organization.exceptions import DuplicateVolunteerSkillError
from mfm.domain.organization.exceptions import InvalidVolunteerReferenceError
from mfm.domain.organization.exceptions import InvalidVolunteerStatusTransitionError
from mfm.domain.organization.exceptions import VolunteerCertificateNotFoundError
from mfm.domain.organization.exceptions import VolunteerSerializationError
from mfm.domain.organization.exceptions import VolunteerSkillNotFoundError
from mfm.domain.organization.volunteer_availability import VolunteerAvailability
from mfm.domain.organization.volunteer_id import VolunteerId
from mfm.domain.organization.volunteer_skill import VolunteerSkill
from mfm.domain.organization.volunteer_status import VolunteerStatus


@dataclass(frozen=True, slots=True)
class VolunteerCertificate:
    """Certificate record for volunteer qualifications."""

    name: str
    expires_at: date | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("certificate name must be a non-empty string")
        object.__setattr__(self, "name", self.name.strip())

        if self.expires_at is not None and not isinstance(self.expires_at, date):
            raise ValueError("expires_at must be a date or None")


@dataclass(slots=True)
class Volunteer:
    """Aggregate root for volunteer profile, skills and lifecycle."""

    contact_id: UUID
    availability: VolunteerAvailability
    id: VolunteerId = field(default_factory=VolunteerId.new)
    member_id: UUID | None = None
    status: VolunteerStatus = VolunteerStatus.ACTIVE
    skills: list[VolunteerSkill] = field(default_factory=list)
    certificates: list[VolunteerCertificate] = field(default_factory=list)
    joined_at: date = field(default_factory=lambda: datetime.now(UTC).date())
    left_at: date | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.id, VolunteerId):
            self.id = VolunteerId(self.id)

        if not isinstance(self.contact_id, UUID):
            raise InvalidVolunteerReferenceError("contact_id must be UUID")

        if self.member_id is not None and not isinstance(self.member_id, UUID):
            raise InvalidVolunteerReferenceError("member_id must be UUID or None")

        if not isinstance(self.availability, VolunteerAvailability):
            raise TypeError("availability must be VolunteerAvailability")

        if not isinstance(self.status, VolunteerStatus):
            self.status = VolunteerStatus(str(self.status).upper())

        if not isinstance(self.joined_at, date):
            raise TypeError("joined_at must be date")

        if self.left_at is not None:
            if not isinstance(self.left_at, date):
                raise TypeError("left_at must be date or None")
            if self.left_at < self.joined_at:
                raise InvalidVolunteerStatusTransitionError(
                    "left_at cannot be before joined_at"
                )

        self.skills = list(self.skills)
        self.certificates = list(self.certificates)
        self._assert_unique_skills()
        self._assert_unique_certificates()

    def _assert_unique_skills(self) -> None:
        seen: set[str] = set()
        for skill in self.skills:
            key = str(skill)
            if key in seen:
                raise DuplicateVolunteerSkillError(f"Duplicate skill {key}")
            seen.add(key)

    def _assert_unique_certificates(self) -> None:
        seen: set[str] = set()
        for certificate in self.certificates:
            key = certificate.name.upper()
            if key in seen:
                raise DuplicateVolunteerCertificateError(
                    f"Duplicate certificate {certificate.name}"
                )
            seen.add(key)

    def add_skill(self, skill: VolunteerSkill) -> None:
        if not isinstance(skill, VolunteerSkill):
            raise TypeError("skill must be VolunteerSkill")
        if any(existing == skill for existing in self.skills):
            raise DuplicateVolunteerSkillError(f"Duplicate skill {skill}")
        self.skills.append(skill)

    def remove_skill(self, skill: VolunteerSkill) -> None:
        if not isinstance(skill, VolunteerSkill):
            raise TypeError("skill must be VolunteerSkill")
        try:
            self.skills.remove(skill)
        except ValueError as exc:
            raise VolunteerSkillNotFoundError(f"Skill {skill} not found") from exc

    def add_certificate(self, name: str, expires_at: date | None = None) -> None:
        certificate = VolunteerCertificate(name=name, expires_at=expires_at)
        if any(c.name.upper() == certificate.name.upper() for c in self.certificates):
            raise DuplicateVolunteerCertificateError(
                f"Duplicate certificate {certificate.name}"
            )
        self.certificates.append(certificate)

    def remove_certificate(self, name: str) -> None:
        normalized = name.strip().upper() if isinstance(name, str) else ""
        if not normalized:
            raise VolunteerCertificateNotFoundError("Certificate name must be provided")

        for index, certificate in enumerate(self.certificates):
            if certificate.name.upper() == normalized:
                self.certificates.pop(index)
                return

        raise VolunteerCertificateNotFoundError(f"Certificate {name} not found")

    def activate(self) -> None:
        if self.status is VolunteerStatus.RETIRED:
            raise InvalidVolunteerStatusTransitionError(
                "Retired volunteer cannot be activated"
            )
        if self.status is VolunteerStatus.ACTIVE:
            return
        self.status = VolunteerStatus.ACTIVE
        self.left_at = None

    def deactivate(self, on_date: date | None = None) -> None:
        if self.status is VolunteerStatus.RETIRED:
            raise InvalidVolunteerStatusTransitionError(
                "Retired volunteer cannot be deactivated"
            )
        if self.status is VolunteerStatus.INACTIVE:
            return

        effective = on_date or datetime.now(UTC).date()
        if effective < self.joined_at:
            raise InvalidVolunteerStatusTransitionError(
                "deactivate date cannot be before joined_at"
            )

        self.status = VolunteerStatus.INACTIVE
        self.left_at = effective

    def retire(self, on_date: date | None = None) -> None:
        if self.status is VolunteerStatus.RETIRED:
            return

        effective = on_date or datetime.now(UTC).date()
        if effective < self.joined_at:
            raise InvalidVolunteerStatusTransitionError(
                "retire date cannot be before joined_at"
            )

        self.status = VolunteerStatus.RETIRED
        self.left_at = effective

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "contact_id": str(self.contact_id),
            "member_id": str(self.member_id) if self.member_id is not None else None,
            "status": self.status.value,
            "skills": [str(skill) for skill in self.skills],
            "certificates": [
                {
                    "name": certificate.name,
                    "expires_at": (
                        certificate.expires_at.isoformat()
                        if certificate.expires_at is not None
                        else None
                    ),
                }
                for certificate in self.certificates
            ],
            "availability": {
                "is_available": self.availability.is_available,
                "max_hours_per_week": self.availability.max_hours_per_week,
                "preferred_days": list(self.availability.preferred_days),
            },
            "joined_at": self.joined_at.isoformat(),
            "left_at": self.left_at.isoformat() if self.left_at is not None else None,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "Volunteer":
        if not isinstance(data, Mapping):
            raise VolunteerSerializationError("data must be a mapping")

        required = {
            "id",
            "contact_id",
            "member_id",
            "status",
            "skills",
            "certificates",
            "availability",
            "joined_at",
            "left_at",
        }
        if not required.issubset(data.keys()):
            missing = sorted(required - set(data.keys()))
            raise VolunteerSerializationError(
                f"data is missing required keys: {', '.join(missing)}"
            )

        try:
            availability_payload = data["availability"]
            if not isinstance(availability_payload, Mapping):
                raise VolunteerSerializationError("availability must be a mapping")

            skills_payload = data["skills"]
            certificates_payload = data["certificates"]
            if not isinstance(skills_payload, list) or not isinstance(
                certificates_payload,
                list,
            ):
                raise VolunteerSerializationError(
                    "skills and certificates must be lists"
                )

            return cls(
                id=VolunteerId(data["id"]),
                contact_id=UUID(str(data["contact_id"])),
                member_id=(
                    UUID(str(data["member_id"]))
                    if data["member_id"] is not None
                    else None
                ),
                status=VolunteerStatus(str(data["status"]).upper()),
                skills=[VolunteerSkill(str(item)) for item in skills_payload],
                certificates=[
                    VolunteerCertificate(
                        name=str(item["name"]),
                        expires_at=(
                            date.fromisoformat(str(item["expires_at"]))
                            if item.get("expires_at") is not None
                            else None
                        ),
                    )
                    for item in certificates_payload
                ],
                availability=VolunteerAvailability(
                    is_available=bool(availability_payload["is_available"]),
                    max_hours_per_week=int(availability_payload["max_hours_per_week"]),
                    preferred_days=tuple(availability_payload.get("preferred_days", [])),
                ),
                joined_at=date.fromisoformat(str(data["joined_at"])),
                left_at=(
                    date.fromisoformat(str(data["left_at"]))
                    if data["left_at"] is not None
                    else None
                ),
            )
        except VolunteerSerializationError:
            raise
        except Exception as exc:
            raise VolunteerSerializationError("Invalid serialized volunteer") from exc
