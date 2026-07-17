"""Fee schedule domain entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from uuid import UUID
from uuid import uuid4

from mfm.domain.membership_billing.membership_fee import MembershipFee


@dataclass(slots=True)
class FeeSchedule:
    """Billing schedule and fee settings for one membership type."""

    membership_fee: MembershipFee
    due_days: int
    billing_period: str = "YEARLY"
    active: bool = True
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")
        if not isinstance(self.membership_fee, MembershipFee):
            raise ValueError("membership_fee must be MembershipFee")
        if not isinstance(self.due_days, int) or self.due_days < 0:
            raise ValueError("due_days must be an integer >= 0")
        if not isinstance(self.billing_period, str) or not self.billing_period.strip():
            raise ValueError("billing_period must be non-empty string")
        if not isinstance(self.active, bool):
            raise ValueError("active must be bool")

        self.billing_period = self.billing_period.strip().upper()
