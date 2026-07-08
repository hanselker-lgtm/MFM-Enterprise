from __future__ import annotations

import re
from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.common.enums import EmailType


_EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)


@dataclass(frozen=True, slots=True)
class Email(ValueObject):
    """
    Immutable Email Value Object.

    Equality is based on the normalized e-mail address.
    """

    address: str
    email_type: EmailType = EmailType.PRIVATE
    primary: bool = False
    verified: bool = False

    def __post_init__(self) -> None:

        normalized = self.address.strip().lower()

        if not _EMAIL_PATTERN.fullmatch(normalized):
            raise ValueError(f"Invalid e-mail address: {self.address}")

        object.__setattr__(self, "address", normalized)

    @property
    def domain(self) -> str:
        return self.address.split("@", 1)[1]

    @property
    def local_part(self) -> str:
        return self.address.split("@", 1)[0]

    def __str__(self) -> str:
        return self.address