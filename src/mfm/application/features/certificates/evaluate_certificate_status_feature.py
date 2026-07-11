"""Evaluate certificate status feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.certificates.create_certificate import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.certificates.create_certificate import (
    EvaluateCertificateStatusResponse as ServiceResponse,
)
from mfm.application.certificates.create_certificate import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.certificates.create_certificate import (
    ValidationException as ServiceValidationException,
)
from mfm.application.certificates.evaluate_certificate_status import (
    EvaluateCertificateStatusRequest as ServiceRequest,
)
from mfm.application.certificates.evaluate_certificate_status import (
    EvaluateCertificateStatusUseCase,
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
class EvaluateCertificateStatusRequest:
    certificate_id: UUID
    as_of_date: date
    expiring_threshold_days: int = 30

    def validate(self) -> None:
        if not isinstance(self.certificate_id, UUID):
            raise ValidationException("certificate_id must be UUID")
        if not isinstance(self.as_of_date, date):
            raise ValidationException("as_of_date must be date")
        if (
            not isinstance(self.expiring_threshold_days, int)
            or self.expiring_threshold_days < 0
        ):
            raise ValidationException("expiring_threshold_days must be non-negative int")


@dataclass(frozen=True, slots=True)
class EvaluateCertificateStatusResponse:
    certificate: CertificateResponse
    evaluated_status: str


class EvaluateCertificateStatusService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class EvaluateCertificateStatusFeature:
    """Feature facade for certificate status evaluation with explicit date."""

    def __init__(self, *, service: EvaluateCertificateStatusService) -> None:
        self._service = service

    def execute(
        self,
        request: EvaluateCertificateStatusRequest,
    ) -> EvaluateCertificateStatusResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    certificate_id=request.certificate_id,
                    as_of_date=request.as_of_date,
                    expiring_threshold_days=request.expiring_threshold_days,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Evaluate certificate status feature failed") from exc

        return EvaluateCertificateStatusResponse(
            certificate=to_feature_certificate_response(service_response.certificate),
            evaluated_status=service_response.evaluated_status,
        )
