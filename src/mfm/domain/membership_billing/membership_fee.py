"""Membership fee domain entity."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from decimal import Decimal
from uuid import UUID
from uuid import uuid4


@dataclass(slots=True)
class MembershipFee:
    """Fee amount assigned to one membership type."""

    membership_type_id: UUID
    membership_type_code: str
    membership_type_name: str
    amount: Decimal
    currency: str
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if not isinstance(self.id, UUID):
            raise ValueError("id must be UUID")
        if not isinstance(self.membership_type_id, UUID):
            raise ValueError("membership_type_id must be UUID")
        if not isinstance(self.membership_type_code, str) or not self.membership_type_code.strip():
            raise ValueError("membership_type_code must be non-empty string")
        if not isinstance(self.membership_type_name, str) or not self.membership_type_name.strip():
            raise ValueError("membership_type_name must be non-empty string")

        try:
            normalized_amount = (
                self.amount
                if isinstance(self.amount, Decimal)
                else Decimal(str(self.amount))
            )
        except Exception as exc:
            raise ValueError("amount must be a valid decimal") from exc

        if normalized_amount <= Decimal("0"):
            raise ValueError("amount must be greater than zero")

        if not isinstance(self.currency, str) or len(self.currency.strip()) != 3:
            raise ValueError("currency must be a 3-letter code")

        self.membership_type_code = self.membership_type_code.strip().upper()
        self.membership_type_name = self.membership_type_name.strip()
        self.amount = normalized_amount
        self.currency = self.currency.strip().upper()
