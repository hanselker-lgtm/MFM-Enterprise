"""Application service for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.domain.contact_communication.communication_preference import (
    CommunicationPreference,
)
from mfm.domain.contact_communication.communication_preference import PreferenceFrequency
from mfm.domain.contact_communication.contact_communication_profile import (
    ContactCommunicationProfile,
)
from mfm.domain.contact_communication.contact_method import ContactMethod
from mfm.domain.contact_communication.contact_method import ContactMethodType
from mfm.domain.contact_communication.email_address import EmailAddress
from mfm.domain.contact_communication.notification import Notification
from mfm.domain.contact_communication.phone_number import PhoneNumber
from mfm.domain.contact_communication.postal_address import PostalAddress


class ApplicationException(Exception):
    """Base exception for contact communication service failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository access fails."""


@dataclass(frozen=True, slots=True)
class SetupContactCommunicationRequest:
    contact_id: UUID
    email_address: str
    phone_number: str
    postal_line1: str
    postal_code: str
    postal_city: str
    postal_country: str
    allow_marketing: bool = False

    def validate(self) -> None:
        if not isinstance(self.contact_id, UUID):
            raise ValidationException("contact_id must be UUID")
        if not isinstance(self.email_address, str) or not self.email_address.strip():
            raise ValidationException("email_address must be non-empty string")
        if not isinstance(self.phone_number, str) or not self.phone_number.strip():
            raise ValidationException("phone_number must be non-empty string")
        if not isinstance(self.postal_line1, str) or not self.postal_line1.strip():
            raise ValidationException("postal_line1 must be non-empty string")
        if not isinstance(self.postal_code, str) or not self.postal_code.strip():
            raise ValidationException("postal_code must be non-empty string")
        if not isinstance(self.postal_city, str) or not self.postal_city.strip():
            raise ValidationException("postal_city must be non-empty string")
        if not isinstance(self.postal_country, str) or not self.postal_country.strip():
            raise ValidationException("postal_country must be non-empty string")
        if not isinstance(self.allow_marketing, bool):
            raise ValidationException("allow_marketing must be bool")


@dataclass(frozen=True, slots=True)
class SetupContactCommunicationResponse:
    contact_id: UUID
    method_count: int
    notification_count: int
    preferred_method_type: str
    allow_marketing: bool
    generated_at: datetime


class ContactCommunicationRepositoryPort(Protocol):
    def get(self, contact_id: UUID) -> ContactCommunicationProfile | None: ...

    def save(self, profile: ContactCommunicationProfile) -> None: ...


class ContactCommunicationService:
    """Configure communication profile and notification baseline for a contact."""

    def __init__(self, *, repository: ContactCommunicationRepositoryPort) -> None:
        self._repository = repository

    def setup(self, request: SetupContactCommunicationRequest) -> SetupContactCommunicationResponse:
        request.validate()

        try:
            existing = self._repository.get(request.contact_id)
            if existing is not None:
                raise BusinessRuleViolation(
                    f"Communication profile for {request.contact_id} already exists"
                )

            profile = ContactCommunicationProfile(contact_id=request.contact_id)

            primary_email = ContactMethod(
                method_type=ContactMethodType.EMAIL,
                email=EmailAddress(request.email_address),
                is_primary=True,
            )
            phone = ContactMethod(
                method_type=ContactMethodType.PHONE,
                phone=PhoneNumber(request.phone_number),
            )
            postal = ContactMethod(
                method_type=ContactMethodType.POSTAL,
                postal=PostalAddress(
                    line1=request.postal_line1,
                    postal_code=request.postal_code,
                    city=request.postal_city,
                    country=request.postal_country,
                ),
            )

            profile.add_method(primary_email)
            profile.add_method(phone)
            profile.add_method(postal)

            preference = CommunicationPreference(
                preferred_method_id=primary_email.id,
                allow_marketing=request.allow_marketing,
                frequency=PreferenceFrequency.IMMEDIATE,
            )
            profile.set_preference(preference)

            welcome_notification = Notification(
                contact_id=request.contact_id,
                method_id=primary_email.id,
                subject="Communication profile enabled",
                message="Your contact communication profile has been configured.",
            )
            profile.schedule_notification(welcome_notification)

            self._repository.save(profile)

            return SetupContactCommunicationResponse(
                contact_id=profile.contact_id,
                method_count=len(profile.methods),
                notification_count=len(profile.notifications),
                preferred_method_type=primary_email.method_type.value,
                allow_marketing=(
                    profile.preference.allow_marketing
                    if profile.preference is not None
                    else False
                ),
                generated_at=datetime.now(UTC),
            )
        except (ValidationException, BusinessRuleViolation):
            raise
        except ValueError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Contact communication setup failed") from exc
