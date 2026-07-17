"""In-process repository adapter for membership billing profiles."""

from __future__ import annotations

from copy import deepcopy
from uuid import UUID

from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile
from mfm.repositories.membership_billing_repository import MembershipBillingRepository


class SQLiteMembershipBillingRepository(MembershipBillingRepository):
    """Repository adapter preserving billing profiles for process lifetime."""

    _store: dict[UUID, MembershipBillingProfile] = {}

    def get(self, membership_type_id: UUID) -> MembershipBillingProfile | None:
        profile = self._store.get(membership_type_id)
        if profile is None:
            return None
        return deepcopy(profile)

    def save(self, profile: MembershipBillingProfile) -> None:
        self._store[profile.membership_type_id] = deepcopy(profile)

    def list(self) -> list[MembershipBillingProfile]:
        return [deepcopy(item) for item in self._store.values()]

    @classmethod
    def clear(cls) -> None:
        cls._store.clear()
