"""Issuer reference value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.certificates.exceptions import InvalidIssuerReferenceError
from mfm.domain.certificates.issuer_reference_type import IssuerReferenceType


@dataclass(frozen=True, slots=True)
class IssuerReference(ValueObject):
    """Identity and historical name snapshot for certificate issuer."""

    issuer_type: IssuerReferenceType
    issuer_id_or_external_key: str
    issuer_name_snapshot: str

    def __post_init__(self) -> None:
        if not isinstance(self.issuer_type, IssuerReferenceType):
            try:
                normalized_type = IssuerReferenceType(str(self.issuer_type).upper())
            except Exception as exc:
                raise InvalidIssuerReferenceError("issuer_type is invalid") from exc
            object.__setattr__(self, "issuer_type", normalized_type)

        if not isinstance(self.issuer_id_or_external_key, str):
            raise InvalidIssuerReferenceError(
                "issuer_id_or_external_key must be string"
            )
        normalized_key = self.issuer_id_or_external_key.strip()
        if not normalized_key:
            raise InvalidIssuerReferenceError(
                "issuer_id_or_external_key must be non-empty"
            )
        object.__setattr__(self, "issuer_id_or_external_key", normalized_key)

        if not isinstance(self.issuer_name_snapshot, str):
            raise InvalidIssuerReferenceError("issuer_name_snapshot must be string")
        normalized_name = self.issuer_name_snapshot.strip()
        if not normalized_name:
            raise InvalidIssuerReferenceError("issuer_name_snapshot must be non-empty")
        object.__setattr__(self, "issuer_name_snapshot", normalized_name)
