"""Get expiring certificates feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol

from mfm.application.certificates.create_certificate import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.certificates.create_certificate import (
    ValidationException as ServiceValidationException,
)
from mfm.application.certificates.get_expiring_certificates import (
    GetExpiringCertificatesRequest as ServiceRequest,
)
from mfm.application.certificates.get_expiring_certificates import (
    GetExpiringCertificatesResponse as ServiceResponse,
)
from mfm.application.certificates.get_expiring_certificates import (
    GetExpiringCertificatesUseCase,
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
class GetExpiringCertificatesRequest:
    as_of_date: date
    within_days: int

    def validate(self) -> None:
        if not isinstance(self.as_of_date, date):
            raise ValidationException("as_of_date must be date")
        if not isinstance(self.within_days, int) or self.within_days < 0:
            raise ValidationException("within_days must be non-negative int")


@dataclass(frozen=True, slots=True)
class GetExpiringCertificatesResponse:
    certificates: tuple[CertificateResponse, ...]


class GetExpiringCertificatesService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class GetExpiringCertificatesFeature:
    """Feature facade for expiring certificate queries."""

    def __init__(self, *, service: GetExpiringCertificatesService) -> None:
        self._service = service

    def execute(
        self,
        request: GetExpiringCertificatesRequest,
    ) -> GetExpiringCertificatesResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    as_of_date=request.as_of_date,
                    within_days=request.within_days,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Get expiring certificates feature failed") from exc

        return GetExpiringCertificatesResponse(
            certificates=tuple(
                to_feature_certificate_response(item)
                for item in service_response.certificates
            )
        )
