from __future__ import annotations

from dataclasses import dataclass

from mfm.common.enums import AddressType
from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class Address(ValueObject):
    """
    Immutable postal address.
    """

    line1: str

    postal_code: str

    city: str

    country: str

    address_type: AddressType = AddressType.HOME

    primary: bool = False

    line2: str = ""

    state: str = ""

    def __post_init__(self):

        object.__setattr__(
            self,
            "line1",
            self.line1.strip(),
        )

        object.__setattr__(
            self,
            "line2",
            self.line2.strip(),
        )

        object.__setattr__(
            self,
            "postal_code",
            self.postal_code.strip(),
        )

        object.__setattr__(
            self,
            "city",
            self.city.strip(),
        )

        object.__setattr__(
            self,
            "state",
            self.state.strip(),
        )

        object.__setattr__(
            self,
            "country",
            self.country.strip(),
        )

    @property
    def single_line(self) -> str:

        return (
            f"{self.line1}, "
            f"{self.postal_code} "
            f"{self.city}, "
            f"{self.country}"
        )

    def __str__(self):

        return self.single_line