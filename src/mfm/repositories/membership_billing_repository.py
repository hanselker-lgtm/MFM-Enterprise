"""Repository contract for membership billing capability."""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile


class MembershipBillingRepository(ABC):
    """Persistence contract for membership billing profiles."""

    @abstractmethod
    def get(self, membership_type_id: UUID) -> MembershipBillingProfile | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, profile: MembershipBillingProfile) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[MembershipBillingProfile]:
        raise NotImplementedError
