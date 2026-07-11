"""Activate certificate feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from mfm.application.certificates.activate_certificate import (
    ActivateCertificateRequest as ServiceRequest,
)
from mfm.application.certificates.activate_certificate import (
    ActivateCertificateResponse as ServiceResponse,
)
from mfm.application.certificates.activate_certificate import ActivateCertificateUseCase
from mfm.application.certificates.create_certificate import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.certificates.create_certificate import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.certificates.create_certificate import (
    ValidationException as ServiceValidationException,
)
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
class ActivateCertificateRequest:
    certificate_id: UUID

    def validate(self) -> None:
        if not isinstance(self.certificate_id, UUID):
            raise ValidationException("certificate_id must be UUID")


@dataclass(frozen=True, slots=True)
class ActivateCertificateResponse:
    certificate: CertificateResponse


class ActivateCertificateService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class ActivateCertificateFeature:
    """Feature facade for certificate activation."""

    def __init__(self, *, service: ActivateCertificateService) -> None:
        self._service = service

    def execute(self, request: ActivateCertificateRequest) -> ActivateCertificateResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(certificate_id=request.certificate_id)
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Activate certificate feature failed") from exc

        return ActivateCertificateResponse(
            certificate=to_feature_certificate_response(service_response.certificate)
        )
