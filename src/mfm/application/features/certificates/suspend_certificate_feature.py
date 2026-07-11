"""Suspend certificate feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.certificates.create_certificate import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.certificates.create_certificate import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.certificates.create_certificate import (
    ValidationException as ServiceValidationException,
)
from mfm.application.certificates.suspend_certificate import (
    SuspendCertificateRequest as ServiceRequest,
)
from mfm.application.certificates.suspend_certificate import (
    SuspendCertificateResponse as ServiceResponse,
)
from mfm.application.certificates.suspend_certificate import SuspendCertificateUseCase
from mfm.application.features.certificates.create_certificate_feature import (
    BusinessRuleViolation,
)
from mfm.application.features.certificates.create_certificate_feature import (
    CertificateResponse,
)
from mfm.application.features.certificates.create_certificate_feature import (
    RepositoryException,
)
from mfm.application.features.certificates.create_certificate_feature import (
    ValidationException,
)
from mfm.application.features.certificates.create_certificate_feature import (
    to_feature_certificate_response,
)


@dataclass(frozen=True, slots=True)
class SuspendCertificateRequest:
    certificate_id: UUID
    notes: str | None = None

    def validate(self) -> None:
        if not isinstance(self.certificate_id, UUID):
            raise ValidationException("certificate_id must be UUID")
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")


@dataclass(frozen=True, slots=True)
class SuspendCertificateResponse:
    certificate: CertificateResponse


class SuspendCertificateService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class SuspendCertificateFeature:
    """Feature facade for certificate suspension."""

    def __init__(self, *, service: SuspendCertificateService) -> None:
        self._service = service

    def execute(self, request: SuspendCertificateRequest) -> SuspendCertificateResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    certificate_id=request.certificate_id,
                    notes=request.notes,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Suspend certificate feature failed") from exc

        return SuspendCertificateResponse(
            certificate=to_feature_certificate_response(service_response.certificate)
        )
