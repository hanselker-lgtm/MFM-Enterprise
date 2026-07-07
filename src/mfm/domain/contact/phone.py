from __future__ import annotations

from dataclasses import dataclass

from mfm.common.enums import PhoneType


@dataclass(slots=True, frozen=True)
class Phone:

    number: str

    type: PhoneType = PhoneType.MOBILE

    primary: bool = False