"""Get certificate history feature facade following Public API Standard."""

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
from mfm.application.certificates.get_certificate_history import (
    GetCertificateHistoryRequest as ServiceRequest,
)
from mfm.application.certificates.get_certificate_history import (
    GetCertificateHistoryResponse as ServiceResponse,
)
from mfm.application.certificates.get_certificate_history import (
    GetCertificateHistoryUseCase,
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
class GetCertificateHistoryRequest:
    certificate_id: UUID

    def validate(self) -> None:
        if not isinstance(self.certificate_id, UUID):
            raise ValidationException("certificate_id must be UUID")


@dataclass(frozen=True, slots=True)
class GetCertificateHistoryResponse:
    certificates: tuple[CertificateResponse, ...]


class GetCertificateHistoryService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetCertificateHistoryFeature:
    """Feature facade for certificate history queries."""

    def __init__(self, *, service: GetCertificateHistoryService) -> None:
        self._service = service

    def execute(self, request: GetCertificateHistoryRequest) -> GetCertificateHistoryResponse:
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
            raise RepositoryException("Get certificate history feature failed") from exc

        return GetCertificateHistoryResponse(
            certificates=tuple(
                to_feature_certificate_response(item)
                for item in service_response.certificates
            )
        )
