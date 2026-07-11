"""Certificate target value object."""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from mfm.common.value_object import ValueObject
from mfm.domain.certificates.certificate_target_type import CertificateTargetType
from mfm.domain.certificates.exceptions import InvalidCertificateTargetError


@dataclass(frozen=True, slots=True)
class CertificateTarget(ValueObject):
    """Identity reference to certificate holder/target."""

    target_type: CertificateTargetType
    target_id: UUID

    def __post_init__(self) -> None:
        if not isinstance(self.target_type, CertificateTargetType):
            try:
                normalized_type = CertificateTargetType(str(self.target_type).upper())
            except Exception as exc:
                raise InvalidCertificateTargetError("target_type is invalid") from exc
            object.__setattr__(self, "target_type", normalized_type)

        if isinstance(self.target_id, str):
            try:
                normalized_id = UUID(self.target_id)
            except Exception as exc:
                raise InvalidCertificateTargetError("target_id must be UUID") from exc
            object.__setattr__(self, "target_id", normalized_id)
            return

        if not isinstance(self.target_id, UUID):
            raise InvalidCertificateTargetError("target_id must be UUID")
