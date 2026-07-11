"""Renew certificate feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
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
from mfm.application.certificates.renew_certificate import (
    RenewCertificateRequest as ServiceRequest,
)
from mfm.application.certificates.renew_certificate import (
    RenewCertificateResponse as ServiceResponse,
)
from mfm.application.certificates.renew_certificate import RenewCertificateUseCase
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
class RenewCertificateRequest:
    source_certificate_id: UUID
    certificate_number: str
    issuer_type: str
    issuer_id_or_external_key: str
    issuer_name_snapshot: str
    issued_date: date
    valid_from: date
    expires_at: date | None = None
    document_reference: str | None = None
    external_document_id: str | None = None
    notes: str | None = None
    renewal_required: bool | None = None

    def validate(self) -> None:
        if not isinstance(self.source_certificate_id, UUID):
            raise ValidationException("source_certificate_id must be UUID")
        if (
            not isinstance(self.certificate_number, str)
            or not self.certificate_number.strip()
        ):
            raise ValidationException("certificate_number must be a non-empty string")
        if not isinstance(self.issuer_type, str) or not self.issuer_type.strip():
            raise ValidationException("issuer_type must be a non-empty string")
        if (
            not isinstance(self.issuer_id_or_external_key, str)
            or not self.issuer_id_or_external_key.strip()
        ):
            raise ValidationException(
                "issuer_id_or_external_key must be a non-empty string"
            )
        if (
            not isinstance(self.issuer_name_snapshot, str)
            or not self.issuer_name_snapshot.strip()
        ):
            raise ValidationException("issuer_name_snapshot must be a non-empty string")
        if not isinstance(self.issued_date, date):
            raise ValidationException("issued_date must be date")
        if not isinstance(self.valid_from, date):
            raise ValidationException("valid_from must be date")
        if self.expires_at is not None and not isinstance(self.expires_at, date):
            raise ValidationException("expires_at must be date or None")
        if self.issued_date > self.valid_from:
            raise ValidationException("issued_date cannot be after valid_from")
        if self.expires_at is not None and self.valid_from > self.expires_at:
            raise ValidationException("valid_from cannot be after expires_at")
        if self.expires_at is not None and self.issued_date > self.expires_at:
            raise ValidationException("issued_date cannot be after expires_at")
        if self.document_reference is not None and not isinstance(
            self.document_reference,
            str,
        ):
            raise ValidationException("document_reference must be string or None")
        if self.external_document_id is not None and not isinstance(
            self.external_document_id,
            str,
        ):
            raise ValidationException("external_document_id must be string or None")
        if self.notes is not None and not isinstance(self.notes, str):
            raise ValidationException("notes must be string or None")
        if self.renewal_required is not None and not isinstance(
            self.renewal_required,
            bool,
        ):
            raise ValidationException("renewal_required must be bool or None")


@dataclass(frozen=True, slots=True)
class RenewCertificateResponse:
    source_certificate_id: UUID
    renewed_certificate: CertificateResponse


class RenewCertificateService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


class RenewCertificateFeature:
    """Feature facade for certificate renewal."""

    def __init__(self, *, service: RenewCertificateService) -> None:
        self._service = service

    def execute(self, request: RenewCertificateRequest) -> RenewCertificateResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    source_certificate_id=request.source_certificate_id,
                    certificate_number=request.certificate_number,
                    issuer_type=request.issuer_type,
                    issuer_id_or_external_key=request.issuer_id_or_external_key,
                    issuer_name_snapshot=request.issuer_name_snapshot,
                    issued_date=request.issued_date,
                    valid_from=request.valid_from,
                    expires_at=request.expires_at,
                    document_reference=request.document_reference,
                    external_document_id=request.external_document_id,
                    notes=request.notes,
                    renewal_required=request.renewal_required,
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Renew certificate feature failed") from exc

        return RenewCertificateResponse(
            source_certificate_id=service_response.source_certificate_id,
            renewed_certificate=to_feature_certificate_response(
                service_response.renewed_certificate
            ),
        )
