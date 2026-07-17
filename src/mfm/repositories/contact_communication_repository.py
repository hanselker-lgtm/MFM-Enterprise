"""Repository contract for contact communication profiles."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.contact_communication.contact_communication_profile import (
    ContactCommunicationProfile,
)


class ContactCommunicationRepository(ABC):
    """Persistence contract for contact communication capability."""

    @abstractmethod
    def get(self, contact_id: UUID) -> ContactCommunicationProfile | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, profile: ContactCommunicationProfile) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[ContactCommunicationProfile]:
        raise NotImplementedError
