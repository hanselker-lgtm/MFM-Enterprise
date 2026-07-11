"""Certificate aggregate root."""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import date

from mfm.common.aggregate_root import AggregateRoot
from mfm.domain.certificates.certificate_evaluation_status import (
    CertificateEvaluationStatus,
)
from mfm.domain.certificates.certificate_status import CertificateStatus
from mfm.domain.certificates.certificate_target import CertificateTarget
from mfm.domain.certificates.certificate_type_reference import CertificateTypeReference
from mfm.domain.certificates.compliance_observation import ComplianceObservation
from mfm.domain.certificates.events import CertificateActivated
from mfm.domain.certificates.events import CertificateCreated
from mfm.domain.certificates.events import CertificateExpired
from mfm.domain.certificates.events import CertificateRenewed
from mfm.domain.certificates.events import CertificateRevoked
from mfm.domain.certificates.events import CertificateSuspended
from mfm.domain.certificates.exceptions import InvalidCertificateChronologyError
from mfm.domain.certificates.exceptions import InvalidCertificateLifecycleError
from mfm.domain.certificates.exceptions import InvalidCertificateStateError
from mfm.domain.certificates.identifiers import CertificateId
from mfm.domain.certificates.issuer_reference import IssuerReference


@dataclass(slots=True)
class Certificate(AggregateRoot):
    """Aggregate root for certificates and compliance lifecycle."""

    certificate_type: CertificateTypeReference
    certificate_number: str
    target: CertificateTarget
    issuer: IssuerReference
    issued_date: date
    valid_from: date
    id: CertificateId = field(default_factory=CertificateId.new)
    expires_at: date | None = None
    status: CertificateStatus = CertificateStatus.DRAFT
    renewal_required: bool = False
    renewed_from_certificate_id: CertificateId | None = None
    document_reference: str | None = None
    external_document_id: str | None = None
    notes: str | None = None
    compliance_observations: tuple[ComplianceObservation, ...] = field(
        default_factory=tuple
    )

    def __post_init__(self) -> None:
        AggregateRoot.__init__(self)

        if not isinstance(self.id, CertificateId):
            self.id = CertificateId(self.id)

        if not isinstance(self.certificate_type, CertificateTypeReference):
            raise TypeError("certificate_type must be CertificateTypeReference")

        self.certificate_number = self._normalize_non_empty(
            self.certificate_number,
            "certificate_number",
        )

        if not isinstance(self.target, CertificateTarget):
            raise TypeError("target must be CertificateTarget")

        if not isinstance(self.issuer, IssuerReference):
            raise TypeError("issuer must be IssuerReference")

        if not isinstance(self.issued_date, date):
            raise InvalidCertificateChronologyError("issued_date must be date")
        if not isinstance(self.valid_from, date):
            raise InvalidCertificateChronologyError("valid_from must be date")
        if self.expires_at is not None and not isinstance(self.expires_at, date):
            raise InvalidCertificateChronologyError("expires_at must be date or None")

        self._validate_chronology(
            issued_date=self.issued_date,
            valid_from=self.valid_from,
            expires_at=self.expires_at,
        )

        if not isinstance(self.status, CertificateStatus):
            self.status = CertificateStatus(str(self.status).upper())

        if not isinstance(self.renewal_required, bool):
            raise InvalidCertificateStateError("renewal_required must be bool")

        if self.renewed_from_certificate_id is not None and not isinstance(
            self.renewed_from_certificate_id,
            CertificateId,
        ):
            self.renewed_from_certificate_id = CertificateId(
                self.renewed_from_certificate_id
            )

        if self.renewed_from_certificate_id is not None:
            if self.renewed_from_certificate_id.value == self.id.value:
                raise InvalidCertificateStateError(
                    "renewed_from_certificate_id cannot reference self"
                )

        self.document_reference = self._normalize_optional_text(self.document_reference)
        self.external_document_id = self._normalize_optional_text(self.external_document_id)
        self.notes = self._normalize_optional_text(self.notes)

        if not isinstance(self.compliance_observations, tuple):
            raise InvalidCertificateStateError(
                "compliance_observations must be tuple"
            )
        for observation in self.compliance_observations:
            if not isinstance(observation, ComplianceObservation):
                raise InvalidCertificateStateError(
                    "compliance_observations must contain ComplianceObservation"
                )

        self._validate_status_invariants()

        self.add_event(CertificateCreated(certificate_id=self.id.value))

    @staticmethod
    def _normalize_non_empty(value: str, field_name: str) -> str:
        if not isinstance(value, str):
            raise InvalidCertificateStateError(f"{field_name} must be string")
        normalized = value.strip()
        if not normalized:
            raise InvalidCertificateStateError(f"{field_name} must be non-empty")
        return normalized

    @staticmethod
    def _normalize_optional_text(value: str | None) -> str | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise InvalidCertificateStateError("optional text field must be string")
        normalized = value.strip()
        return normalized or None

    @staticmethod
    def _validate_chronology(
        *,
        issued_date: date,
        valid_from: date,
        expires_at: date | None,
    ) -> None:
        if issued_date > valid_from:
            raise InvalidCertificateChronologyError(
                "issued_date cannot be after valid_from"
            )
        if expires_at is not None and valid_from > expires_at:
            raise InvalidCertificateChronologyError(
                "valid_from cannot be after expires_at"
            )
        if expires_at is not None and issued_date > expires_at:
            raise InvalidCertificateChronologyError(
                "issued_date cannot be after expires_at"
            )

    def _validate_status_invariants(self) -> None:
        if self.status is CertificateStatus.DRAFT:
            return

        if self.status is CertificateStatus.ACTIVE:
            return

        if self.status is CertificateStatus.SUSPENDED:
            return

        if self.status is CertificateStatus.REVOKED:
            return

        if self.status is CertificateStatus.EXPIRED:
            if self.expires_at is None:
                raise InvalidCertificateStateError(
                    "expired certificate requires expires_at"
                )
            return

    def activate(self) -> None:
        if self.status is not CertificateStatus.DRAFT:
            raise InvalidCertificateLifecycleError("only draft certificate can activate")
        self.status = CertificateStatus.ACTIVE
        self.add_event(CertificateActivated(certificate_id=self.id.value))

    def suspend(self, *, notes: str | None = None) -> None:
        if self.status is not CertificateStatus.ACTIVE:
            raise InvalidCertificateLifecycleError("only active certificate can suspend")
        if notes is not None:
            self.notes = self._normalize_optional_text(notes)
        self.status = CertificateStatus.SUSPENDED
        self.add_event(CertificateSuspended(certificate_id=self.id.value))

    def revoke(self, *, notes: str | None = None) -> None:
        if self.status not in {
            CertificateStatus.ACTIVE,
            CertificateStatus.SUSPENDED,
        }:
            raise InvalidCertificateLifecycleError(
                "only active or suspended certificate can revoke"
            )
        if notes is not None:
            self.notes = self._normalize_optional_text(notes)
        self.status = CertificateStatus.REVOKED
        self.add_event(CertificateRevoked(certificate_id=self.id.value))

    def evaluate_status(
        self,
        *,
        as_of_date: date,
        expiring_threshold_days: int = 30,
    ) -> CertificateEvaluationStatus:
        if not isinstance(as_of_date, date):
            raise InvalidCertificateChronologyError("as_of_date must be date")
        if not isinstance(expiring_threshold_days, int) or expiring_threshold_days < 0:
            raise InvalidCertificateStateError(
                "expiring_threshold_days must be non-negative int"
            )

        if self.status is CertificateStatus.DRAFT:
            return CertificateEvaluationStatus.DRAFT
        if self.status is CertificateStatus.SUSPENDED:
            return CertificateEvaluationStatus.SUSPENDED
        if self.status is CertificateStatus.REVOKED:
            return CertificateEvaluationStatus.REVOKED
        if self.status is CertificateStatus.EXPIRED:
            return CertificateEvaluationStatus.EXPIRED

        if self.status is not CertificateStatus.ACTIVE:
            raise InvalidCertificateStateError("unsupported certificate status")

        if self.expires_at is None:
            return CertificateEvaluationStatus.VALID

        if as_of_date > self.expires_at:
            self.status = CertificateStatus.EXPIRED
            self.add_event(
                CertificateExpired(certificate_id=self.id.value, as_of_date=as_of_date)
            )
            return CertificateEvaluationStatus.EXPIRED

        days_remaining = (self.expires_at - as_of_date).days
        if days_remaining <= expiring_threshold_days:
            return CertificateEvaluationStatus.EXPIRING
        return CertificateEvaluationStatus.VALID

    def record_compliance_observation(
        self,
        observation: ComplianceObservation,
    ) -> None:
        if not isinstance(observation, ComplianceObservation):
            raise InvalidCertificateStateError(
                "observation must be ComplianceObservation"
            )
        self.compliance_observations = (*self.compliance_observations, observation)

    def renew(
        self,
        *,
        certificate_number: str,
        issuer: IssuerReference,
        issued_date: date,
        valid_from: date,
        expires_at: date | None,
        document_reference: str | None = None,
        external_document_id: str | None = None,
        notes: str | None = None,
        renewal_required: bool | None = None,
    ) -> "Certificate":
        if self.status in {CertificateStatus.DRAFT, CertificateStatus.REVOKED}:
            raise InvalidCertificateLifecycleError(
                "draft or revoked certificate cannot be renewed"
            )

        renewed_certificate = Certificate(
            id=CertificateId.new(),
            certificate_type=self.certificate_type,
            certificate_number=certificate_number,
            target=self.target,
            issuer=issuer,
            issued_date=issued_date,
            valid_from=valid_from,
            expires_at=expires_at,
            status=CertificateStatus.DRAFT,
            renewal_required=(
                self.renewal_required
                if renewal_required is None
                else renewal_required
            ),
            renewed_from_certificate_id=self.id,
            document_reference=document_reference,
            external_document_id=external_document_id,
            notes=notes,
            compliance_observations=(),
        )

        self.add_event(
            CertificateRenewed(
                certificate_id=self.id.value,
                renewed_certificate_id=renewed_certificate.id.value,
            )
        )
        return renewed_certificate
