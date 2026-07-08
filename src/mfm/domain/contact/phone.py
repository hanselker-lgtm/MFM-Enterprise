from __future__ import annotations

import re
from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.common.enums import PhoneType

from mfm.domain.contact.exceptions import InvalidPhoneError


_PHONE_PATTERN = re.compile(r"^\+?[0-9 ]{6,20}$")


@dataclass(frozen=True, slots=True)
class Phone(ValueObject):
    """
    Immutable phone number.
    """

    number: str

    phone_type: PhoneType = PhoneType.MOBILE

    primary: bool = False

    verified: bool = False

    def __post_init__(self):

        normalized = self.number.replace(" ", "")

        if not _PHONE_PATTERN.fullmatch(normalized):

            raise InvalidPhoneError(
                f"Invalid phone number: {self.number}"
            )

        object.__setattr__(
            self,
            "number",
            normalized,
        )

        @property
        def display_name(self) -> str:
            return self.full_name

    def __str__(self):

        return self.number