"""Create certificate feature facade following Public API Standard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol
from uuid import UUID

from mfm.application.certificates.create_certificate import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.certificates.create_certificate import (
    CertificateResponse as ServiceCertificateResponse,
)
from mfm.application.certificates.create_certificate import (
    CertificateTargetResponse as ServiceCertificateTargetResponse,
)
from mfm.application.certificates.create_certificate import (
    CertificateTypeResponse as ServiceCertificateTypeResponse,
)
from mfm.application.certificates.create_certificate import (
    ComplianceObservationInput as ServiceComplianceObservationInput,
)
from mfm.application.certificates.create_certificate import (
    ComplianceObservationResponse as ServiceComplianceObservationResponse,
)
from mfm.application.certificates.create_certificate import (
    CreateCertificateRequest as ServiceRequest,
)
from mfm.application.certificates.create_certificate import (
    CreateCertificateResponse as ServiceResponse,
)
from mfm.application.certificates.create_certificate import CreateCertificateUseCase
from mfm.application.certificates.create_certificate import (
    IssuerReferenceResponse as ServiceIssuerReferenceResponse,
)
from mfm.application.certificates.create_certificate import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.certificates.create_certificate import (
    ValidationException as ServiceValidationException,
)


class ApplicationException(Exception):
    """Base exception for certificate feature failures."""


class ValidationException(ApplicationException):
    """Raised when feature request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when domain/application business rules are violated."""


class RepositoryException(ApplicationException):
    """Raised when repository or persistence operations fail."""


@dataclass(frozen=True, slots=True)
class CertificateTypeResponse:
    certificate_type_id: UUID
    code: str
    display_name_snapshot: str | None


@dataclass(frozen=True, slots=True)
class CertificateTargetResponse:
    target_type: str
    target_id: UUID


@dataclass(frozen=True, slots=True)
class IssuerReferenceResponse:
    issuer_type: str
    issuer_id_or_external_key: str
    issuer_name_snapshot: str


@dataclass(frozen=True, slots=True)
class ComplianceObservationResponse:
    summary: str
    observed_on: date
    requires_maintenance_work: bool


@dataclass(frozen=True, slots=True)
class CertificateResponse:
    id: UUID
    certificate_type: CertificateTypeResponse
    certificate_number: str
    target: CertificateTargetResponse
    issuer: IssuerReferenceResponse
    issued_date: date
    valid_from: date
    expires_at: date | None
    status: str
    renewal_required: bool
    renewed_from_certificate_id: UUID | None
    document_reference: str | None
    external_document_id: str | None
    notes: str | None
    compliance_observations: tuple[ComplianceObservationResponse, ...]


@dataclass(frozen=True, slots=True)
class ComplianceObservationInput:
    summary: str
    observed_on: date
    requires_maintenance_work: bool = False

    def validate(self) -> None:
        if not isinstance(self.summary, str) or not self.summary.strip():
            raise ValidationException("summary must be a non-empty string")
        if not isinstance(self.observed_on, date):
            raise ValidationException("observed_on must be date")
        if not isinstance(self.requires_maintenance_work, bool):
            raise ValidationException("requires_maintenance_work must be bool")


@dataclass(frozen=True, slots=True)
class CreateCertificateRequest:
    certificate_type_id: UUID
    certificate_type_code: str
    target_type: str
    target_id: UUID
    certificate_number: str
    issuer_type: str
    issuer_id_or_external_key: str
    issuer_name_snapshot: str
    issued_date: date
    valid_from: date
    expires_at: date | None = None
    renewal_required: bool = False
    certificate_type_display_name_snapshot: str | None = None
    document_reference: str | None = None
    external_document_id: str | None = None
    notes: str | None = None
    compliance_observations: tuple[ComplianceObservationInput, ...] = ()

    def validate(self) -> None:
        if not isinstance(self.certificate_type_id, UUID):
            raise ValidationException("certificate_type_id must be UUID")
        if (
            not isinstance(self.certificate_type_code, str)
            or not self.certificate_type_code.strip()
        ):
            raise ValidationException("certificate_type_code must be a non-empty string")
        if not isinstance(self.target_type, str) or not self.target_type.strip():
            raise ValidationException("target_type must be a non-empty string")
        if not isinstance(self.target_id, UUID):
            raise ValidationException("target_id must be UUID")
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
        if not isinstance(self.renewal_required, bool):
            raise ValidationException("renewal_required must be bool")
        if (
            self.certificate_type_display_name_snapshot is not None
            and not isinstance(self.certificate_type_display_name_snapshot, str)
        ):
            raise ValidationException(
                "certificate_type_display_name_snapshot must be string or None"
            )
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
        if not isinstance(self.compliance_observations, tuple):
            raise ValidationException("compliance_observations must be tuple")
        for observation in self.compliance_observations:
            observation.validate()


@dataclass(frozen=True, slots=True)
class CreateCertificateResponse:
    certificate: CertificateResponse


class CreateCertificateService(Protocol):
    def execute(self, request: ServiceRequest) -> ServiceResponse: ...


def to_feature_certificate_type_response(
    response: ServiceCertificateTypeResponse,
) -> CertificateTypeResponse:
    return CertificateTypeResponse(
        certificate_type_id=response.certificate_type_id,
        code=response.code,
        display_name_snapshot=response.display_name_snapshot,
    )


def to_feature_target_response(
    response: ServiceCertificateTargetResponse,
) -> CertificateTargetResponse:
    return CertificateTargetResponse(
        target_type=response.target_type,
        target_id=response.target_id,
    )


def to_feature_issuer_response(
    response: ServiceIssuerReferenceResponse,
) -> IssuerReferenceResponse:
    return IssuerReferenceResponse(
        issuer_type=response.issuer_type,
        issuer_id_or_external_key=response.issuer_id_or_external_key,
        issuer_name_snapshot=response.issuer_name_snapshot,
    )


def to_feature_observation_response(
    response: ServiceComplianceObservationResponse,
) -> ComplianceObservationResponse:
    return ComplianceObservationResponse(
        summary=response.summary,
        observed_on=response.observed_on,
        requires_maintenance_work=response.requires_maintenance_work,
    )


def to_feature_certificate_response(
    response: ServiceCertificateResponse,
) -> CertificateResponse:
    return CertificateResponse(
        id=response.id,
        certificate_type=to_feature_certificate_type_response(response.certificate_type),
        certificate_number=response.certificate_number,
        target=to_feature_target_response(response.target),
        issuer=to_feature_issuer_response(response.issuer),
        issued_date=response.issued_date,
        valid_from=response.valid_from,
        expires_at=response.expires_at,
        status=response.status,
        renewal_required=response.renewal_required,
        renewed_from_certificate_id=response.renewed_from_certificate_id,
        document_reference=response.document_reference,
        external_document_id=response.external_document_id,
        notes=response.notes,
        compliance_observations=tuple(
            to_feature_observation_response(item)
            for item in response.compliance_observations
        ),
    )


class CreateCertificateFeature:
    """Feature facade for certificate creation."""

    def __init__(self, *, service: CreateCertificateService) -> None:
        self._service = service

    def execute(self, request: CreateCertificateRequest) -> CreateCertificateResponse:
        request.validate()

        try:
            service_response = self._service.execute(
                ServiceRequest(
                    certificate_type_id=request.certificate_type_id,
                    certificate_type_code=request.certificate_type_code,
                    certificate_type_display_name_snapshot=(
                        request.certificate_type_display_name_snapshot
                    ),
                    target_type=request.target_type,
                    target_id=request.target_id,
                    certificate_number=request.certificate_number,
                    issuer_type=request.issuer_type,
                    issuer_id_or_external_key=request.issuer_id_or_external_key,
                    issuer_name_snapshot=request.issuer_name_snapshot,
                    issued_date=request.issued_date,
                    valid_from=request.valid_from,
                    expires_at=request.expires_at,
                    renewal_required=request.renewal_required,
                    document_reference=request.document_reference,
                    external_document_id=request.external_document_id,
                    notes=request.notes,
                    compliance_observations=tuple(
                        ServiceComplianceObservationInput(
                            summary=item.summary,
                            observed_on=item.observed_on,
                            requires_maintenance_work=item.requires_maintenance_work,
                        )
                        for item in request.compliance_observations
                    ),
                )
            )
        except ServiceValidationException as exc:
            raise ValidationException(str(exc)) from exc
        except ServiceBusinessRuleViolation as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except ServiceRepositoryException as exc:
            raise RepositoryException(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create certificate feature failed") from exc

        return CreateCertificateResponse(
            certificate=to_feature_certificate_response(service_response.certificate)
        )
