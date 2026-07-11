"""Identity value objects for certificates domain."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from uuid import uuid4

from mfm.common.value_object import ValueObject


@dataclass(frozen=True, slots=True)
class CertificateId(ValueObject):
    """Identity for certificate aggregate."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("CertificateId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "CertificateId":
        return cls(uuid4())


@dataclass(frozen=True, slots=True)
class CertificateTypeId(ValueObject):
    """Identity for controlled certificate type reference."""

    value: UUID

    def __post_init__(self) -> None:
        if isinstance(self.value, str):
            object.__setattr__(self, "value", UUID(self.value))
            return
        if not isinstance(self.value, UUID):
            raise TypeError("CertificateTypeId value must be UUID or UUID string")

    @classmethod
    def new(cls) -> "CertificateTypeId":
        return cls(uuid4())
