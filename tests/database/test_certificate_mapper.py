from __future__ import annotations

from datetime import date
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401

from mfm.database.mappers.certificate_mapper import CertificateMapper
from mfm.database.models.base_model import BaseModel
from mfm.database.models.certificate_model import CertificateModel
from mfm.domain.certificates.certificate import Certificate
from mfm.domain.certificates.certificate_status import CertificateStatus
from mfm.domain.certificates.certificate_target import CertificateTarget
from mfm.domain.certificates.certificate_target_type import CertificateTargetType
from mfm.domain.certificates.certificate_type_reference import CertificateTypeReference
from mfm.domain.certificates.compliance_observation import ComplianceObservation
from mfm.domain.certificates.identifiers import CertificateId
from mfm.domain.certificates.identifiers import CertificateTypeId
from mfm.domain.certificates.issuer_reference import IssuerReference
from mfm.domain.certificates.issuer_reference_type import IssuerReferenceType


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    return Session(engine)


def _close_session(session: Session) -> None:
    bind = session.get_bind()
    session.close()
    bind.dispose()


def _certificate_type() -> CertificateTypeReference:
    return CertificateTypeReference(
        certificate_type_id=CertificateTypeId(UUID("00000000-0000-0000-0000-00000000A101")),
        code="STATUTORY_CERT",
        display_name_snapshot="Statutory Certificate",
    )


def _target_vessel() -> CertificateTarget:
    return CertificateTarget(
        target_type=CertificateTargetType.VESSEL,
        target_id=UUID("00000000-0000-0000-0000-00000000B101"),
    )


def _target_organization() -> CertificateTarget:
    return CertificateTarget(
        target_type=CertificateTargetType.ORGANIZATION,
        target_id=UUID("00000000-0000-0000-0000-00000000B102"),
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


def _certificate(
    *,
    certificate_id: UUID,
    number: str,
    target: CertificateTarget,
    issuer: IssuerReference,
    issued_date: date,
    valid_from: date,
    expires_at: date | None,
    notes: str,
    document_reference: str,
    external_document_id: str,
) -> Certificate:
    return Certificate(
        id=CertificateId(certificate_id),
        certificate_type=_certificate_type(),
        certificate_number=number,
        target=target,
        issuer=issuer,
        issued_date=issued_date,
        valid_from=valid_from,
        expires_at=expires_at,
        status=CertificateStatus.DRAFT,
        renewal_required=True,
        notes=notes,
        document_reference=document_reference,
        external_document_id=external_document_id,
    )


def _persist_and_reload(session: Session, certificate: Certificate) -> Certificate:
    orm = CertificateMapper.to_orm_certificate(certificate)
    session.add(orm)
    session.commit()

    loaded = session.get(CertificateModel, certificate.id.value)
    assert loaded is not None
    return CertificateMapper.to_domain_certificate(loaded)


def test_certificate_roundtrip_persists_core_state(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-roundtrip-core")
    try:
        certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C101"),
            number="CERT-A",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 1, 1),
            valid_from=date(2027, 1, 1),
            expires_at=date(2028, 1, 1),
            notes="Context A",
            document_reference="DOC-A",
            external_document_id="EXT-A",
        )
        certificate.activate()

        restored = _persist_and_reload(session, certificate)

        assert restored.id == certificate.id
        assert restored.certificate_type == certificate.certificate_type
        assert restored.certificate_number == "CERT-A"
        assert restored.target == certificate.target
        assert restored.issuer == certificate.issuer
        assert restored.issued_date == certificate.issued_date
        assert restored.valid_from == certificate.valid_from
        assert restored.expires_at == certificate.expires_at
        assert restored.status is CertificateStatus.ACTIVE
        assert restored.notes == "Context A"
        assert restored.document_reference == "DOC-A"
        assert restored.external_document_id == "EXT-A"
    finally:
        _close_session(session)


def test_certificate_target_roundtrip_for_approved_types(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-targets")
    try:
        vessel = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C201"),
            number="CERT-V",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 2, 1),
            valid_from=date(2027, 2, 1),
            expires_at=date(2028, 2, 1),
            notes="Vessel",
            document_reference="DOC-V",
            external_document_id="EXT-V",
        )
        organization = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C202"),
            number="CERT-O",
            target=_target_organization(),
            issuer=_issuer_a(),
            issued_date=date(2027, 3, 1),
            valid_from=date(2027, 3, 1),
            expires_at=date(2028, 3, 1),
            notes="Organization",
            document_reference="DOC-O",
            external_document_id="EXT-O",
        )

        restored_vessel = _persist_and_reload(session, vessel)
        restored_org = _persist_and_reload(session, organization)

        assert restored_vessel.target.target_type is CertificateTargetType.VESSEL
        assert restored_org.target.target_type is CertificateTargetType.ORGANIZATION
        assert restored_vessel.target.target_id == vessel.target.target_id
        assert restored_org.target.target_id == organization.target.target_id
    finally:
        _close_session(session)


def test_certificate_type_roundtrip_controlled_reference(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-type")
    try:
        certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C301"),
            number="CERT-T",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 4, 1),
            valid_from=date(2027, 4, 1),
            expires_at=date(2028, 4, 1),
            notes="Type",
            document_reference="DOC-T",
            external_document_id="EXT-T",
        )

        restored = _persist_and_reload(session, certificate)

        assert restored.certificate_type.certificate_type_id == certificate.certificate_type.certificate_type_id
        assert restored.certificate_type.code == "STATUTORY_CERT"
        assert restored.certificate_type.display_name_snapshot == "Statutory Certificate"
    finally:
        _close_session(session)


def test_issuer_snapshot_roundtrip_preserves_a_and_b(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-issuer")
    try:
        certificate_a = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C401"),
            number="CERT-A",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 1, 1),
            valid_from=date(2027, 1, 1),
            expires_at=date(2028, 1, 1),
            notes="Context A",
            document_reference="DOC-A",
            external_document_id="EXT-A",
        )
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
        )
        certificate_b.activate()

        session.add(CertificateMapper.to_orm_certificate(certificate_a))
        session.add(CertificateMapper.to_orm_certificate(certificate_b))
        session.commit()

        loaded_a = session.get(CertificateModel, certificate_a.id.value)
        loaded_b = session.get(CertificateModel, certificate_b.id.value)
        assert loaded_a is not None
        assert loaded_b is not None

        restored_a = CertificateMapper.to_domain_certificate(loaded_a)
        restored_b = CertificateMapper.to_domain_certificate(loaded_b)

        assert restored_a.issuer.issuer_name_snapshot == "Maritime Authority A"
        assert restored_b.issuer.issuer_name_snapshot == "Maritime Authority B"
        assert restored_b.renewed_from_certificate_id == restored_a.id
    finally:
        _close_session(session)


def test_validity_and_status_roundtrip_fixed_and_non_expiring(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-validity")
    try:
        fixed = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C501"),
            number="CERT-F",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 5, 1),
            valid_from=date(2027, 5, 1),
            expires_at=date(2028, 5, 1),
            notes="Fixed",
            document_reference="DOC-F",
            external_document_id="EXT-F",
        )
        fixed.activate()

        non_expiring = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C502"),
            number="CERT-N",
            target=_target_organization(),
            issuer=_issuer_a(),
            issued_date=date(2027, 6, 1),
            valid_from=date(2027, 6, 1),
            expires_at=None,
            notes="Non-expiring",
            document_reference="DOC-N",
            external_document_id="EXT-N",
        )
        non_expiring.activate()

        restored_fixed = _persist_and_reload(session, fixed)
        restored_non_expiring = _persist_and_reload(session, non_expiring)

        assert restored_fixed.issued_date == date(2027, 5, 1)
        assert restored_fixed.valid_from == date(2027, 5, 1)
        assert restored_fixed.expires_at == date(2028, 5, 1)
        assert restored_fixed.status is CertificateStatus.ACTIVE

        assert restored_non_expiring.issued_date == date(2027, 6, 1)
        assert restored_non_expiring.valid_from == date(2027, 6, 1)
        assert restored_non_expiring.expires_at is None
        assert restored_non_expiring.status is CertificateStatus.ACTIVE
    finally:
        _close_session(session)


def test_lifecycle_status_roundtrip_for_persisted_states(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-lifecycle")
    try:
        draft = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C601"),
            number="CERT-D",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 7, 1),
            valid_from=date(2027, 7, 1),
            expires_at=date(2028, 7, 1),
            notes="Draft",
            document_reference="DOC-D",
            external_document_id="EXT-D",
        )

        active = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C602"),
            number="CERT-ACT",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 7, 2),
            valid_from=date(2027, 7, 2),
            expires_at=date(2028, 7, 2),
            notes="Active",
            document_reference="DOC-ACT",
            external_document_id="EXT-ACT",
        )
        active.activate()

        suspended = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C603"),
            number="CERT-SUS",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 7, 3),
            valid_from=date(2027, 7, 3),
            expires_at=date(2028, 7, 3),
            notes="Suspended",
            document_reference="DOC-SUS",
            external_document_id="EXT-SUS",
        )
        suspended.activate()
        suspended.suspend(notes="Temporary hold")

        revoked = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C604"),
            number="CERT-REV",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 7, 4),
            valid_from=date(2027, 7, 4),
            expires_at=date(2028, 7, 4),
            notes="Revoked",
            document_reference="DOC-REV",
            external_document_id="EXT-REV",
        )
        revoked.activate()
        revoked.revoke(notes="Non-compliant")

        restored_draft = _persist_and_reload(session, draft)
        restored_active = _persist_and_reload(session, active)
        restored_suspended = _persist_and_reload(session, suspended)
        restored_revoked = _persist_and_reload(session, revoked)

        assert restored_draft.status is CertificateStatus.DRAFT
        assert restored_active.status is CertificateStatus.ACTIVE
        assert restored_suspended.status is CertificateStatus.SUSPENDED
        assert restored_revoked.status is CertificateStatus.REVOKED
    finally:
        _close_session(session)


def test_renewal_relation_and_historical_truth_roundtrip(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-renewal")
    try:
        certificate_a = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C701"),
            number="CERT-A",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 1, 1),
            valid_from=date(2027, 1, 1),
            expires_at=date(2028, 1, 1),
            notes="Context A",
            document_reference="DOC-A",
            external_document_id="EXT-A",
        )
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
        )
        certificate_b.activate()

        session.add(CertificateMapper.to_orm_certificate(certificate_a))
        session.add(CertificateMapper.to_orm_certificate(certificate_b))
        session.commit()

        loaded_a = session.get(CertificateModel, certificate_a.id.value)
        loaded_b = session.get(CertificateModel, certificate_b.id.value)
        assert loaded_a is not None
        assert loaded_b is not None

        restored_a = CertificateMapper.to_domain_certificate(loaded_a)
        restored_b = CertificateMapper.to_domain_certificate(loaded_b)

        assert restored_a.id == CertificateId(UUID("00000000-0000-0000-0000-00000000C701"))
        assert restored_a.certificate_number == "CERT-A"
        assert restored_a.issuer.issuer_name_snapshot == "Maritime Authority A"
        assert restored_a.issued_date == date(2027, 1, 1)
        assert restored_a.valid_from == date(2027, 1, 1)
        assert restored_a.expires_at == date(2028, 1, 1)
        assert restored_a.notes == "Context A"
        assert restored_a.document_reference == "DOC-A"

        assert restored_b.certificate_number == "CERT-B"
        assert restored_b.issuer.issuer_name_snapshot == "Maritime Authority B"
        assert restored_b.issued_date == date(2028, 1, 2)
        assert restored_b.valid_from == date(2028, 1, 2)
        assert restored_b.expires_at == date(2029, 1, 1)
        assert restored_b.notes == "Context B"
        assert restored_b.document_reference == "DOC-B"
        assert restored_b.renewed_from_certificate_id == restored_a.id
    finally:
        _close_session(session)


def test_compliance_observation_roundtrip_and_maintenance_boundary(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-compliance")
    try:
        certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C801"),
            number="CERT-C",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 8, 1),
            valid_from=date(2027, 8, 1),
            expires_at=date(2028, 8, 1),
            notes="Compliance",
            document_reference="DOC-C",
            external_document_id="EXT-C",
        )
        certificate.activate()
        certificate.record_compliance_observation(
            ComplianceObservation(
                summary="Inspection indicates maintenance work required",
                observed_on=date(2027, 12, 1),
                requires_maintenance_work=True,
            )
        )

        restored = _persist_and_reload(session, certificate)

        assert len(restored.compliance_observations) == 1
        observation = restored.compliance_observations[0]
        assert observation.summary == "Inspection indicates maintenance work required"
        assert observation.requires_maintenance_work is True
        assert not hasattr(restored, "create_work_order")
    finally:
        _close_session(session)


def test_event_restoration_does_not_emit_false_history_events(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-events")
    try:
        certificate_a = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000C901"),
            number="CERT-A",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 9, 1),
            valid_from=date(2027, 9, 1),
            expires_at=date(2028, 9, 1),
            notes="Event A",
            document_reference="DOC-EA",
            external_document_id="EXT-EA",
        )
        certificate_a.activate()
        certificate_b = certificate_a.renew(
            certificate_number="CERT-B",
            issuer=_issuer_b(),
            issued_date=date(2028, 9, 2),
            valid_from=date(2028, 9, 2),
            expires_at=date(2029, 9, 1),
            notes="Event B",
            document_reference="DOC-EB",
            external_document_id="EXT-EB",
        )

        session.add(CertificateMapper.to_orm_certificate(certificate_a))
        session.add(CertificateMapper.to_orm_certificate(certificate_b))
        session.commit()

        loaded_a = session.get(CertificateModel, certificate_a.id.value)
        loaded_b = session.get(CertificateModel, certificate_b.id.value)
        assert loaded_a is not None
        assert loaded_b is not None

        restored_a = CertificateMapper.to_domain_certificate(loaded_a)
        restored_b = CertificateMapper.to_domain_certificate(loaded_b)

        assert restored_a.pull_events() == []
        assert restored_b.pull_events() == []
    finally:
        _close_session(session)
