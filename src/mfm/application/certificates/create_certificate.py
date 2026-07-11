"""Create Certificate use case and shared certificate application DTOs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from uuid import UUID

from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.certificates.certificate import Certificate
from mfm.domain.certificates.certificate_evaluation_status import (
    CertificateEvaluationStatus,
)
from mfm.domain.certificates.certificate_target import CertificateTarget
from mfm.domain.certificates.certificate_target_type import CertificateTargetType
from mfm.domain.certificates.certificate_type_reference import CertificateTypeReference
from mfm.domain.certificates.compliance_observation import ComplianceObservation
from mfm.domain.certificates.exceptions import CertificateError
from mfm.domain.certificates.identifiers import CertificateTypeId
from mfm.domain.certificates.issuer_reference import IssuerReference
from mfm.domain.certificates.issuer_reference_type import IssuerReferenceType
from mfm.repositories.certificate_repository import CertificateRepository


class ApplicationException(Exception):
    """Base exception for certificate application use cases."""


class ValidationException(ApplicationException):
    """Raised when request validation fails."""


class BusinessRuleViolation(ApplicationException):
    """Raised when a business rule blocks execution."""


class RepositoryException(ApplicationException):
    """Raised for repository/persistence failures."""


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


def parse_target_type(value: str) -> CertificateTargetType:
    try:
        return CertificateTargetType(value.strip().upper())
    except Exception as exc:
        raise ValidationException("target_type is invalid") from exc


def parse_issuer_type(value: str) -> IssuerReferenceType:
    try:
        return IssuerReferenceType(value.strip().upper())
    except Exception as exc:
        raise ValidationException("issuer_type is invalid") from exc


def to_certificate_type_reference(
    *,
    certificate_type_id: UUID,
    code: str,
    display_name_snapshot: str | None,
) -> CertificateTypeReference:
    return CertificateTypeReference(
        certificate_type_id=CertificateTypeId(certificate_type_id),
        code=code,
        display_name_snapshot=display_name_snapshot,
    )


def to_issuer_reference(
    *,
    issuer_type: str,
    issuer_id_or_external_key: str,
    issuer_name_snapshot: str,
) -> IssuerReference:
    return IssuerReference(
        issuer_type=parse_issuer_type(issuer_type),
        issuer_id_or_external_key=issuer_id_or_external_key,
        issuer_name_snapshot=issuer_name_snapshot,
    )


def to_compliance_observation(
    input_value: ComplianceObservationInput,
) -> ComplianceObservation:
    return ComplianceObservation(
        summary=input_value.summary,
        observed_on=input_value.observed_on,
        requires_maintenance_work=input_value.requires_maintenance_work,
    )


def to_certificate_response(certificate: Certificate) -> CertificateResponse:
    return CertificateResponse(
        id=certificate.id.value,
        certificate_type=CertificateTypeResponse(
            certificate_type_id=certificate.certificate_type.certificate_type_id.value,
            code=certificate.certificate_type.code,
            display_name_snapshot=certificate.certificate_type.display_name_snapshot,
        ),
        certificate_number=certificate.certificate_number,
        target=CertificateTargetResponse(
            target_type=certificate.target.target_type.value,
            target_id=certificate.target.target_id,
        ),
        issuer=IssuerReferenceResponse(
            issuer_type=certificate.issuer.issuer_type.value,
            issuer_id_or_external_key=certificate.issuer.issuer_id_or_external_key,
            issuer_name_snapshot=certificate.issuer.issuer_name_snapshot,
        ),
        issued_date=certificate.issued_date,
        valid_from=certificate.valid_from,
        expires_at=certificate.expires_at,
        status=certificate.status.value,
        renewal_required=certificate.renewal_required,
        renewed_from_certificate_id=(
            certificate.renewed_from_certificate_id.value
            if certificate.renewed_from_certificate_id is not None
            else None
        ),
        document_reference=certificate.document_reference,
        external_document_id=certificate.external_document_id,
        notes=certificate.notes,
        compliance_observations=tuple(
            ComplianceObservationResponse(
                summary=observation.summary,
                observed_on=observation.observed_on,
                requires_maintenance_work=observation.requires_maintenance_work,
            )
            for observation in certificate.compliance_observations
        ),
    )


@dataclass(frozen=True, slots=True)
class EvaluateCertificateStatusResponse:
    certificate: CertificateResponse
    evaluated_status: str


def to_evaluated_status_response(
    *,
    certificate: Certificate,
    evaluated_status: CertificateEvaluationStatus,
) -> EvaluateCertificateStatusResponse:
    return EvaluateCertificateStatusResponse(
        certificate=to_certificate_response(certificate),
        evaluated_status=evaluated_status.value,
    )


class CreateCertificateUseCase:
    """Create certificate aggregate in one transactional boundary."""

    def __init__(self, *, unit_of_work: AbstractUnitOfWork) -> None:
        self._unit_of_work = unit_of_work

    def execute(self, request: CreateCertificateRequest) -> CreateCertificateResponse:
        request.validate()

        certificate = Certificate(
            certificate_type=to_certificate_type_reference(
                certificate_type_id=request.certificate_type_id,
                code=request.certificate_type_code,
                display_name_snapshot=request.certificate_type_display_name_snapshot,
            ),
            certificate_number=request.certificate_number,
            target=CertificateTarget(
                target_type=parse_target_type(request.target_type),
                target_id=request.target_id,
            ),
            issuer=to_issuer_reference(
                issuer_type=request.issuer_type,
                issuer_id_or_external_key=request.issuer_id_or_external_key,
                issuer_name_snapshot=request.issuer_name_snapshot,
            ),
            issued_date=request.issued_date,
            valid_from=request.valid_from,
            expires_at=request.expires_at,
            renewal_required=request.renewal_required,
            document_reference=request.document_reference,
            external_document_id=request.external_document_id,
            notes=request.notes,
            compliance_observations=tuple(
                to_compliance_observation(item)
                for item in request.compliance_observations
            ),
        )

        try:
            with self._unit_of_work as uow:
                repository: CertificateRepository = uow.certificate_repository
                repository.add(certificate)
                uow.commit()
        except (ValidationException, BusinessRuleViolation):
            raise
        except CertificateError as exc:
            raise BusinessRuleViolation(str(exc)) from exc
        except Exception as exc:
            raise RepositoryException("Create certificate failed") from exc

        return CreateCertificateResponse(certificate=to_certificate_response(certificate))
