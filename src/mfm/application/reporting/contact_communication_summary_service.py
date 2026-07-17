"""Reporting service for contact communication capability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC
from datetime import datetime
from typing import Protocol
from uuid import UUID

from mfm.application.reporting.models.contact_communication_summary_dto import (
    ContactCommunicationSummaryResponse,
)
from mfm.domain.contact_communication.contact_communication_profile import (
    ContactCommunicationProfile,
)
from mfm.domain.contact_communication.notification import NotificationStatus


class ApplicationException(Exception):
    """Base exception for reporting failures."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class RepositoryException(ApplicationException):
    """Raised when repository dependencies fail."""


@dataclass(frozen=True, slots=True)
class ContactCommunicationSummaryRequest:
    contact_id: UUID

    def validate(self) -> None:
        if not isinstance(self.contact_id, UUID):
            raise ValidationException("contact_id must be UUID")


class ContactCommunicationRepositoryPort(Protocol):
    def get(self, contact_id: UUID) -> ContactCommunicationProfile | None: ...


class ContactCommunicationSummaryService:
    """Build summary metrics for one contact communication profile."""

    def __init__(self, *, repository: ContactCommunicationRepositoryPort) -> None:
        self._repository = repository

    def execute(self, request: ContactCommunicationSummaryRequest) -> ContactCommunicationSummaryResponse:
        request.validate()

        try:
            profile = self._repository.get(request.contact_id)
        except ValidationException:
            raise
        except Exception as exc:
            raise RepositoryException("Contact communication summary retrieval failed") from exc

        if profile is None:
            raise ValidationException(
                f"Contact communication profile not found for {request.contact_id}"
            )

        pending = sum(
            1 for item in profile.notifications if item.status is NotificationStatus.PENDING
        )
        sent = sum(
            1 for item in profile.notifications if item.status is NotificationStatus.SENT
        )
        failed = sum(
            1 for item in profile.notifications if item.status is NotificationStatus.FAILED
        )

        return ContactCommunicationSummaryResponse(
            contact_id=profile.contact_id,
            method_count=len(profile.methods),
            notification_count=len(profile.notifications),
            has_preference=profile.preference is not None,
            pending_notifications=pending,
            sent_notifications=sent,
            failed_notifications=failed,
            generated_at=datetime.now(UTC),
        )
