"""In-process repository adapter for contact communication profiles."""

from __future__ import annotations

from copy import deepcopy
from uuid import UUID

from mfm.domain.contact_communication.contact_communication_profile import (
    ContactCommunicationProfile,
)
from mfm.repositories.contact_communication_repository import (
    ContactCommunicationRepository,
)


class SQLiteContactCommunicationRepository(ContactCommunicationRepository):
    """Repository adapter preserving profiles for current process lifetime."""

    _store: dict[UUID, ContactCommunicationProfile] = {}

    def get(self, contact_id: UUID) -> ContactCommunicationProfile | None:
        profile = self._store.get(contact_id)
        if profile is None:
            return None
        return deepcopy(profile)

    def save(self, profile: ContactCommunicationProfile) -> None:
        self._store[profile.contact_id] = deepcopy(profile)

    def list(self) -> list[ContactCommunicationProfile]:
        return [deepcopy(item) for item in self._store.values()]

    @classmethod
    def clear(cls) -> None:
        cls._store.clear()
