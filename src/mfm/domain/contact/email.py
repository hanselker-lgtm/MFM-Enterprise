from __future__ import annotations

from dataclasses import dataclass

from mfm.common.enums import EmailType


@dataclass(slots=True, frozen=True)
class Email:
    """
    Email Value Object.
    """

    address: str
    type: EmailType = EmailType.PRIVATE
    primary: bool = False
    verified: bool = False

    def __post_init__(self) -> None:

        if "@" not in self.address:
            raise ValueError(
                f"Invalid email address: {self.address}"
            )

        object.__setattr__(
            self,
            "address",
            self.address.lower().strip(),
        )