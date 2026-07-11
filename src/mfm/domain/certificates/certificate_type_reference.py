"""Certificate type reference value object."""

from __future__ import annotations

from dataclasses import dataclass

from mfm.common.value_object import ValueObject
from mfm.domain.certificates.exceptions import InvalidCertificateTypeError
from mfm.domain.certificates.identifiers import CertificateTypeId


@dataclass(frozen=True, slots=True)
class CertificateTypeReference(ValueObject):
    """Controlled certificate type reference."""

    certificate_type_id: CertificateTypeId
    code: str
    display_name_snapshot: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.certificate_type_id, CertificateTypeId):
            try:
                normalized_id = CertificateTypeId(self.certificate_type_id)
            except Exception as exc:
                raise InvalidCertificateTypeError(
                    "certificate_type_id is invalid"
                ) from exc
            object.__setattr__(self, "certificate_type_id", normalized_id)

        if not isinstance(self.code, str):
            raise InvalidCertificateTypeError("code must be string")
        normalized_code = self.code.strip().upper()
        if not normalized_code:
            raise InvalidCertificateTypeError("code must be non-empty")
        object.__setattr__(self, "code", normalized_code)

        if self.display_name_snapshot is not None:
            if not isinstance(self.display_name_snapshot, str):
                raise InvalidCertificateTypeError(
                    "display_name_snapshot must be string or None"
                )
            normalized_name = self.display_name_snapshot.strip()
            object.__setattr__(
                self,
                "display_name_snapshot",
                normalized_name or None,
            )
