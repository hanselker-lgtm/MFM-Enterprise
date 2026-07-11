from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.domain.certificates.certificate import Certificate
from mfm.domain.certificates.certificate_evaluation_status import (
    CertificateEvaluationStatus,
)
from mfm.domain.certificates.certificate_status import CertificateStatus
from mfm.domain.certificates.certificate_target import CertificateTarget
from mfm.domain.certificates.certificate_target_type import CertificateTargetType
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
from mfm.domain.certificates.exceptions import InvalidCertificateTargetError
from mfm.domain.certificates.exceptions import InvalidCertificateTypeError
from mfm.domain.certificates.exceptions import InvalidIssuerReferenceError
from mfm.domain.certificates.identifiers import CertificateTypeId
from mfm.domain.certificates.issuer_reference import IssuerReference
from mfm.domain.certificates.issuer_reference_type import IssuerReferenceType


def _type_reference() -> CertificateTypeReference:
    return CertificateTypeReference(
        certificate_type_id=CertificateTypeId.new(),
        code="STATUTORY_CERT",
        display_name_snapshot="Statutory Certificate",
    )


def _target_vessel() -> CertificateTarget:
    return CertificateTarget(
        target_type=CertificateTargetType.VESSEL,
        target_id=uuid4(),
    )


def _target_organization() -> CertificateTarget:
    return CertificateTarget(
        target_type=CertificateTargetType.ORGANIZATION,
        target_id=uuid4(),
    )


def _issuer_a() -> IssuerReference:
    return IssuerReference(
        issuer_type=IssuerReferenceType.AUTHORITY,
        issuer_id_or_external_key="AUTH-001",
        issuer_name_snapshot="Maritime Authority A",
    )


def _issuer_b() -> IssuerReference:
    return IssuerReference(
        issuer_type=IssuerReferenceType.CLASSIFICATION_SOCIETY,
        issuer_id_or_external_key="CLASS-002",
        issuer_name_snapshot="Maritime Authority B",
    )


def _certificate(*, target: CertificateTarget | None = None, expires_at: date | None = date(2028, 1, 1)) -> Certificate:
    return Certificate(
        certificate_type=_type_reference(),
        certificate_number="CERT-A",
        target=target or _target_vessel(),
        issuer=_issuer_a(),
        issued_date=date(2027, 1, 1),
        valid_from=date(2027, 1, 1),
        expires_at=expires_at,
        renewal_required=True,
        document_reference="DOC-A",
        external_document_id="EXT-A",
        notes="Context A",
    )


def test_certificate_target_vessel() -> None:
    target = _target_vessel()

    assert target.target_type is CertificateTargetType.VESSEL
    assert isinstance(target.target_id, UUID)


def test_certificate_target_organization() -> None:
    target = _target_organization()

    assert target.target_type is CertificateTargetType.ORGANIZATION
    assert isinstance(target.target_id, UUID)


@pytest.mark.parametrize("unsupported", ["PERSON", "TECHNICAL_COMPONENT", "INVALID"])
def test_certificate_target_unsupported_type_rejected(unsupported: str) -> None:
    with pytest.raises(InvalidCertificateTargetError):
        CertificateTarget(target_type=unsupported, target_id=uuid4())  # type: ignore[arg-type]


def test_certificate_target_missing_target_id_rejected() -> None:
    with pytest.raises(InvalidCertificateTargetError):
        CertificateTarget(
            target_type=CertificateTargetType.VESSEL,
            target_id=None,  # type: ignore[arg-type]
        )


def test_certificate_target_immutability() -> None:
    target = _target_vessel()

    with pytest.raises(FrozenInstanceError):
        target.target_id = uuid4()  # type: ignore[misc]


def test_certificate_type_reference_valid_controlled_type() -> None:
    certificate_type = _type_reference()

    assert isinstance(certificate_type.certificate_type_id, CertificateTypeId)
    assert certificate_type.code == "STATUTORY_CERT"


def test_certificate_type_reference_invalid_type_rejected() -> None:
    with pytest.raises(InvalidCertificateTypeError):
        CertificateTypeReference(
            certificate_type_id=CertificateTypeId.new(),
            code="",
        )


def test_certificate_type_reference_immutability() -> None:
    certificate_type = _type_reference()

    with pytest.raises(FrozenInstanceError):
        certificate_type.code = "CHANGED"  # type: ignore[misc]


def test_issuer_reference_valid() -> None:
    issuer = _issuer_a()

    assert issuer.issuer_type is IssuerReferenceType.AUTHORITY
    assert issuer.issuer_name_snapshot == "Maritime Authority A"


def test_issuer_reference_required_identity_and_name_snapshot() -> None:
    with pytest.raises(InvalidIssuerReferenceError):
        IssuerReference(
            issuer_type=IssuerReferenceType.AUTHORITY,
            issuer_id_or_external_key=" ",
            issuer_name_snapshot="Maritime Authority A",
        )

    with pytest.raises(InvalidIssuerReferenceError):
        IssuerReference(
            issuer_type=IssuerReferenceType.AUTHORITY,
            issuer_id_or_external_key="AUTH-01",
            issuer_name_snapshot=" ",
        )


def test_issuer_reference_immutability() -> None:
    issuer = _issuer_a()

    with pytest.raises(FrozenInstanceError):
        issuer.issuer_name_snapshot = "Changed"  # type: ignore[misc]


def test_issuer_historical_name_snapshot_preserved() -> None:
    certificate_a = _certificate()
    certificate_a.activate()

    certificate_b = certificate_a.renew(
        certificate_number="CERT-B",
        issuer=_issuer_b(),
        issued_date=date(2028, 1, 2),
        valid_from=date(2028, 1, 2),
        expires_at=date(2029, 1, 1),
        notes="Context B",
    )

    assert certificate_a.issuer.issuer_name_snapshot == "Maritime Authority A"
    assert certificate_b.issuer.issuer_name_snapshot == "Maritime Authority B"


def test_validity_fixed_expiry() -> None:
    certificate = _certificate(expires_at=date(2028, 1, 1))
    certificate.activate()

    assert (
        certificate.evaluate_status(as_of_date=date(2027, 6, 1), expiring_threshold_days=30)
        is CertificateEvaluationStatus.VALID
    )


def test_validity_non_expiring_certificate() -> None:
    certificate = _certificate(expires_at=None)
    certificate.activate()

    assert (
        certificate.evaluate_status(as_of_date=date(2035, 1, 1), expiring_threshold_days=30)
        is CertificateEvaluationStatus.VALID
    )


def test_validity_invalid_chronology_rejected() -> None:
    with pytest.raises(InvalidCertificateChronologyError):
        Certificate(
            certificate_type=_type_reference(),
            certificate_number="CERT-A",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 2, 1),
            valid_from=date(2027, 1, 1),
            expires_at=date(2027, 12, 31),
        )


def test_validity_explicit_current_date_expiring_and_boundary_dates() -> None:
    certificate = _certificate(expires_at=date(2028, 1, 1))
    certificate.activate()

    assert (
        certificate.evaluate_status(as_of_date=date(2027, 12, 2), expiring_threshold_days=30)
        is CertificateEvaluationStatus.EXPIRING
    )
    assert (
        certificate.evaluate_status(as_of_date=date(2028, 1, 1), expiring_threshold_days=30)
        is CertificateEvaluationStatus.EXPIRING
    )


def test_validity_expired_state_and_event() -> None:
    certificate = _certificate(expires_at=date(2028, 1, 1))
    certificate.activate()
    certificate.pull_events()

    result = certificate.evaluate_status(
        as_of_date=date(2028, 1, 2),
        expiring_threshold_days=30,
    )

    assert result is CertificateEvaluationStatus.EXPIRED
    assert certificate.status is CertificateStatus.EXPIRED
    assert any(isinstance(event, CertificateExpired) for event in certificate.pull_events())


def test_lifecycle_create_certificate_and_created_event() -> None:
    certificate = _certificate()

    assert certificate.status is CertificateStatus.DRAFT
    assert any(isinstance(event, CertificateCreated) for event in certificate.pull_events())


def test_lifecycle_activate_and_invalid_duplicate_activation() -> None:
    certificate = _certificate()
    certificate.pull_events()

    certificate.activate()
    events = certificate.pull_events()

    assert certificate.status is CertificateStatus.ACTIVE
    assert any(isinstance(event, CertificateActivated) for event in events)

    with pytest.raises(InvalidCertificateLifecycleError):
        certificate.activate()


def test_lifecycle_suspend_and_invalid_suspension() -> None:
    certificate = _certificate()

    with pytest.raises(InvalidCertificateLifecycleError):
        certificate.suspend()

    certificate.activate()
    certificate.pull_events()
    certificate.suspend(notes="Pending evidence")

    assert certificate.status is CertificateStatus.SUSPENDED
    assert certificate.notes == "Pending evidence"
    assert any(isinstance(event, CertificateSuspended) for event in certificate.pull_events())


def test_lifecycle_revoke_and_invalid_revocation() -> None:
    certificate = _certificate()

    with pytest.raises(InvalidCertificateLifecycleError):
        certificate.revoke()

    certificate.activate()
    certificate.pull_events()
    certificate.revoke(notes="Regulatory non-compliance")

    assert certificate.status is CertificateStatus.REVOKED
    assert any(isinstance(event, CertificateRevoked) for event in certificate.pull_events())


def test_lifecycle_terminal_state_behaviour() -> None:
    certificate = _certificate()
    certificate.activate()
    certificate.revoke()

    with pytest.raises(InvalidCertificateLifecycleError):
        certificate.activate()

    with pytest.raises(InvalidCertificateLifecycleError):
        certificate.renew(
            certificate_number="CERT-B",
            issuer=_issuer_b(),
            issued_date=date(2028, 1, 1),
            valid_from=date(2028, 1, 1),
            expires_at=date(2029, 1, 1),
        )


def test_certificate_renewal_preserves_historical_truth() -> None:
    certificate_a = _certificate(expires_at=date(2028, 1, 1))
    certificate_a.activate()

    certificate_b = certificate_a.renew(
        certificate_number="CERT-B",
        issuer=_issuer_b(),
        issued_date=date(2028, 1, 2),
        valid_from=date(2028, 1, 2),
        expires_at=date(2029, 1, 1),
        document_reference="DOC-B",
        external_document_id="EXT-B",
        notes="Context B",
        renewal_required=False,
    )

    assert certificate_a.id != certificate_b.id
    assert certificate_a.certificate_number == "CERT-A"
    assert certificate_a.issuer.issuer_name_snapshot == "Maritime Authority A"
    assert certificate_a.issued_date == date(2027, 1, 1)
    assert certificate_a.valid_from == date(2027, 1, 1)
    assert certificate_a.expires_at == date(2028, 1, 1)
    assert certificate_a.notes == "Context A"
    assert certificate_a.document_reference == "DOC-A"

    assert certificate_b.certificate_number == "CERT-B"
    assert certificate_b.issuer.issuer_name_snapshot == "Maritime Authority B"
    assert certificate_b.issued_date == date(2028, 1, 2)
    assert certificate_b.valid_from == date(2028, 1, 2)
    assert certificate_b.expires_at == date(2029, 1, 1)
    assert certificate_b.notes == "Context B"
    assert certificate_b.document_reference == "DOC-B"
    assert certificate_b.renewed_from_certificate_id == certificate_a.id

    renewal_events = certificate_a.pull_events()
    assert any(isinstance(event, CertificateRenewed) for event in renewal_events)


def test_historical_truth_context_a_and_context_b_are_independent() -> None:
    certificate_a = _certificate(expires_at=date(2028, 1, 1))
    certificate_a.activate()

    certificate_b = certificate_a.renew(
        certificate_number="CERT-B",
        issuer=_issuer_b(),
        issued_date=date(2028, 1, 3),
        valid_from=date(2028, 1, 3),
        expires_at=date(2029, 1, 3),
        notes="Context B",
    )

    assert certificate_a.certificate_number == "CERT-A"
    assert certificate_a.notes == "Context A"
    assert certificate_a.issuer.issuer_name_snapshot == "Maritime Authority A"

    assert certificate_b.certificate_number == "CERT-B"
    assert certificate_b.notes == "Context B"
    assert certificate_b.issuer.issuer_name_snapshot == "Maritime Authority B"


def test_inspection_boundary_records_compliance_result_without_maintenance_operations() -> None:
    certificate = _certificate()
    certificate.activate()

    certificate.record_compliance_observation(
        ComplianceObservation(
            summary="Renewal inspection indicates maintenance work required",
            observed_on=date(2027, 12, 1),
            requires_maintenance_work=True,
        )
    )

    assert len(certificate.compliance_observations) == 1
    assert certificate.compliance_observations[0].requires_maintenance_work is True

    assert not hasattr(certificate, "create_maintenance_plan")
    assert not hasattr(certificate, "add_maintenance_task")
    assert not hasattr(certificate, "create_work_order")
    assert not hasattr(certificate, "start_work_order")
    assert not hasattr(certificate, "complete_work_order")
    assert not hasattr(certificate, "write_maintenance_record")
