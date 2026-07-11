from __future__ import annotations

from datetime import date
from pathlib import Path
from uuid import UUID

import mfm.database.models  # noqa: F401
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
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
from mfm.infrastructure.persistence.sqlite.sqlite_certificate_repository import (
    SQLiteCertificateRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


def _sqlite_session(tmp_path: Path, name: str) -> Session:
    db_path = tmp_path / f"{name}.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)
    return Session(engine)


def _certificate_type() -> CertificateTypeReference:
    return CertificateTypeReference(
        certificate_type_id=CertificateTypeId(UUID("00000000-0000-0000-0000-00000000D101")),
        code="STATUTORY_CERT",
        display_name_snapshot="Statutory Certificate",
    )


def _target_vessel() -> CertificateTarget:
    return CertificateTarget(
        target_type=CertificateTargetType.VESSEL,
        target_id=UUID("00000000-0000-0000-0000-00000000D201"),
    )


def _target_organization() -> CertificateTarget:
    return CertificateTarget(
        target_type=CertificateTargetType.ORGANIZATION,
        target_id=UUID("00000000-0000-0000-0000-00000000D202"),
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


def _issuer_c() -> IssuerReference:
    return IssuerReference(
        issuer_type=IssuerReferenceType.INSPECTION_BODY,
        issuer_id_or_external_key="INSP-003",
        issuer_name_snapshot="Inspection Body C",
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
        renewal_required=True,
        notes=notes,
        document_reference=document_reference,
        external_document_id=external_document_id,
    )


def test_certificate_repository_add_get_exists_list_and_not_found(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-repo-basic")
    try:
        repository = SQLiteCertificateRepository(UnitOfWork(session))
        certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E101"),
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

        repository.add(certificate)
        session.commit()

        loaded = repository.get_by_id(certificate.id.value)
        assert loaded is not None
        assert loaded.id == certificate.id
        assert loaded.certificate_number == "CERT-A"

        assert repository.get_by_id(UUID("00000000-0000-0000-0000-00000000EEEE")) is None
        assert repository.exists(certificate.id.value) is True
        assert repository.exists(UUID("00000000-0000-0000-0000-00000000EEEE")) is False

        listed = repository.list()
        assert len(listed) == 1
        assert listed[0].id == certificate.id
    finally:
        session.close()


def test_certificate_repository_get_by_target_for_all_approved_types(tmp_path: Path) -> None:
    session = _sqlite_session(tmp_path, "cert-repo-target")
    try:
        repository = SQLiteCertificateRepository(UnitOfWork(session))

        vessel_certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E201"),
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
        organization_certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E202"),
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

        repository.add(vessel_certificate)
        repository.add(organization_certificate)
        session.commit()

        vessel_result = repository.get_by_target(_target_vessel())
        organization_result = repository.get_by_target(_target_organization())

        assert len(vessel_result) == 1
        assert vessel_result[0].target.target_type is CertificateTargetType.VESSEL

        assert len(organization_result) == 1
        assert (
            organization_result[0].target.target_type
            is CertificateTargetType.ORGANIZATION
        )
    finally:
        session.close()


def test_certificate_repository_update_lifecycle_roundtrip_without_transition_logic(
    tmp_path: Path,
) -> None:
    session = _sqlite_session(tmp_path, "cert-repo-update")
    try:
        repository = SQLiteCertificateRepository(UnitOfWork(session))
        certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E301"),
            number="CERT-U",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 4, 1),
            valid_from=date(2027, 4, 1),
            expires_at=date(2028, 4, 1),
            notes="Update",
            document_reference="DOC-U",
            external_document_id="EXT-U",
        )

        repository.add(certificate)
        session.commit()

        certificate.activate()
        repository.update(certificate)
        session.commit()
        loaded_active = repository.get_by_id(certificate.id.value)
        assert loaded_active is not None
        assert loaded_active.status is CertificateStatus.ACTIVE

        certificate.suspend(notes="Temporary hold")
        repository.update(certificate)
        session.commit()
        loaded_suspended = repository.get_by_id(certificate.id.value)
        assert loaded_suspended is not None
        assert loaded_suspended.status is CertificateStatus.SUSPENDED

        certificate.revoke(notes="Permanent revoke")
        repository.update(certificate)
        session.commit()
        loaded_revoked = repository.get_by_id(certificate.id.value)
        assert loaded_revoked is not None
        assert loaded_revoked.status is CertificateStatus.REVOKED
    finally:
        session.close()


def test_certificate_repository_validity_queries_with_explicit_reference_dates(
    tmp_path: Path,
) -> None:
    session = _sqlite_session(tmp_path, "cert-repo-validity")
    try:
        repository = SQLiteCertificateRepository(UnitOfWork(session))

        active_valid = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E401"),
            number="CERT-VALID",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 1, 1),
            valid_from=date(2027, 1, 1),
            expires_at=date(2028, 12, 31),
            notes="Valid",
            document_reference="DOC-VALID",
            external_document_id="EXT-VALID",
        )
        active_valid.activate()

        active_expiring = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E402"),
            number="CERT-EXPIRING",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 2, 1),
            valid_from=date(2027, 2, 1),
            expires_at=date(2028, 1, 20),
            notes="Expiring",
            document_reference="DOC-EXPIRING",
            external_document_id="EXT-EXPIRING",
        )
        active_expiring.activate()

        active_expired = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E403"),
            number="CERT-EXPIRED",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 3, 1),
            valid_from=date(2027, 3, 1),
            expires_at=date(2028, 1, 10),
            notes="Expired",
            document_reference="DOC-EXPIRED",
            external_document_id="EXT-EXPIRED",
        )
        active_expired.activate()

        active_non_expiring = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E404"),
            number="CERT-NONEXP",
            target=_target_organization(),
            issuer=_issuer_a(),
            issued_date=date(2027, 4, 1),
            valid_from=date(2027, 4, 1),
            expires_at=None,
            notes="Non-expiring",
            document_reference="DOC-NONEXP",
            external_document_id="EXT-NONEXP",
        )
        active_non_expiring.activate()

        persisted_expired = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E405"),
            number="CERT-PERSISTED-EXP",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 5, 1),
            valid_from=date(2027, 5, 1),
            expires_at=date(2028, 1, 1),
            notes="Persisted expired",
            document_reference="DOC-PEXP",
            external_document_id="EXT-PEXP",
        )
        persisted_expired.activate()
        persisted_expired.evaluate_status(as_of_date=date(2028, 2, 1))

        for certificate in (
            active_valid,
            active_expiring,
            active_expired,
            active_non_expiring,
            persisted_expired,
        ):
            repository.add(certificate)
        session.commit()

        active_by_target = repository.get_active_by_target(_target_vessel())
        active_ids = {certificate.id.value for certificate in active_by_target}
        assert UUID("00000000-0000-0000-0000-00000000E401") in active_ids
        assert UUID("00000000-0000-0000-0000-00000000E402") in active_ids
        assert UUID("00000000-0000-0000-0000-00000000E403") in active_ids
        assert UUID("00000000-0000-0000-0000-00000000E405") not in active_ids

        expiring = repository.get_expiring(
            as_of_date=date(2028, 1, 1),
            within_days=30,
        )
        expiring_ids = {certificate.id.value for certificate in expiring}
        assert UUID("00000000-0000-0000-0000-00000000E402") in expiring_ids
        assert UUID("00000000-0000-0000-0000-00000000E404") not in expiring_ids

        expired = repository.get_expired(as_of_date=date(2028, 1, 15))
        expired_ids = {certificate.id.value for certificate in expired}
        assert UUID("00000000-0000-0000-0000-00000000E403") in expired_ids

        expired_after_persisted = repository.get_expired(as_of_date=date(2028, 2, 2))
        expired_after_ids = {certificate.id.value for certificate in expired_after_persisted}
        assert UUID("00000000-0000-0000-0000-00000000E405") in expired_after_ids

        # Repository query must not mutate lifecycle state.
        loaded_expiring = repository.get_by_id(UUID("00000000-0000-0000-0000-00000000E402"))
        assert loaded_expiring is not None
        assert loaded_expiring.status is CertificateStatus.ACTIVE
    finally:
        session.close()


def test_certificate_repository_renewal_history_and_historical_truth_and_chain(
    tmp_path: Path,
) -> None:
    session = _sqlite_session(tmp_path, "cert-repo-renewal")
    try:
        repository = SQLiteCertificateRepository(UnitOfWork(session))

        certificate_a = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E501"),
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
            notes="Context B",
            document_reference="DOC-B",
            external_document_id="EXT-B",
        )
        certificate_b.activate()

        certificate_c = certificate_b.renew(
            certificate_number="CERT-C",
            issuer=_issuer_c(),
            issued_date=date(2029, 1, 3),
            valid_from=date(2029, 1, 3),
            expires_at=date(2030, 1, 1),
            notes="Context C",
            document_reference="DOC-C",
            external_document_id="EXT-C",
        )
        certificate_c.activate()

        repository.add(certificate_a)
        repository.add(certificate_b)
        repository.add(certificate_c)
        session.commit()

        loaded_a = repository.get_by_id(certificate_a.id.value)
        loaded_b = repository.get_by_id(certificate_b.id.value)
        loaded_c = repository.get_by_id(certificate_c.id.value)
        assert loaded_a is not None and loaded_b is not None and loaded_c is not None

        assert loaded_a.certificate_number == "CERT-A"
        assert loaded_a.issuer.issuer_name_snapshot == "Maritime Authority A"
        assert loaded_a.notes == "Context A"

        assert loaded_b.certificate_number == "CERT-B"
        assert loaded_b.issuer.issuer_name_snapshot == "Maritime Authority B"
        assert loaded_b.notes == "Context B"
        assert loaded_b.renewed_from_certificate_id == loaded_a.id

        assert loaded_c.certificate_number == "CERT-C"
        assert loaded_c.issuer.issuer_name_snapshot == "Inspection Body C"
        assert loaded_c.notes == "Context C"
        assert loaded_c.renewed_from_certificate_id == loaded_b.id

        history = repository.get_renewal_history(certificate_a.id.value)
        assert [certificate.certificate_number for certificate in history] == [
            "CERT-A",
            "CERT-B",
            "CERT-C",
        ]

        loaded_b.notes = "Context B updated"
        repository.update(loaded_b)
        session.commit()

        reloaded_a = repository.get_by_id(certificate_a.id.value)
        reloaded_b = repository.get_by_id(certificate_b.id.value)
        assert reloaded_a is not None and reloaded_b is not None
        assert reloaded_a.notes == "Context A"
        assert reloaded_b.notes == "Context B updated"
    finally:
        session.close()


def test_certificate_repository_compliance_observation_boundary_and_event_restoration(
    tmp_path: Path,
) -> None:
    session = _sqlite_session(tmp_path, "cert-repo-compliance")
    try:
        repository = SQLiteCertificateRepository(UnitOfWork(session))
        certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E601"),
            number="CERT-COMP",
            target=_target_organization(),
            issuer=_issuer_a(),
            issued_date=date(2027, 6, 1),
            valid_from=date(2027, 6, 1),
            expires_at=date(2028, 6, 1),
            notes="Compliance context",
            document_reference="DOC-COMP",
            external_document_id="EXT-COMP",
        )
        certificate.activate()
        certificate.record_compliance_observation(
            ComplianceObservation(
                summary="Inspection indicates maintenance work required",
                observed_on=date(2027, 12, 1),
                requires_maintenance_work=True,
            )
        )

        repository.add(certificate)
        session.commit()

        loaded = repository.get_by_id(certificate.id.value)
        assert loaded is not None
        assert len(loaded.compliance_observations) == 1
        assert loaded.compliance_observations[0].requires_maintenance_work is True

        # Restored aggregate should not emit false historical events from reload.
        assert loaded.pull_events() == []
    finally:
        session.close()


def test_certificate_repository_uses_uow_transaction_without_implicit_commit(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "cert-repo-uow.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)

    session_one = Session(engine)
    session_two = Session(engine)
    try:
        repository = SQLiteCertificateRepository(UnitOfWork(session_one))
        certificate = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E701"),
            number="CERT-UOW",
            target=_target_vessel(),
            issuer=_issuer_a(),
            issued_date=date(2027, 7, 1),
            valid_from=date(2027, 7, 1),
            expires_at=date(2028, 7, 1),
            notes="UoW",
            document_reference="DOC-UOW",
            external_document_id="EXT-UOW",
        )

        repository.add(certificate)

        verification_repository_before_commit = SQLiteCertificateRepository(
            UnitOfWork(session_two)
        )
        assert (
            verification_repository_before_commit.get_by_id(certificate.id.value)
            is None
        )

        session_one.commit()
        verification_after_commit = verification_repository_before_commit.get_by_id(
            certificate.id.value
        )
        assert verification_after_commit is not None

        certificate_two = _certificate(
            certificate_id=UUID("00000000-0000-0000-0000-00000000E702"),
            number="CERT-ROLLBACK",
            target=_target_vessel(),
            issuer=_issuer_b(),
            issued_date=date(2027, 8, 1),
            valid_from=date(2027, 8, 1),
            expires_at=date(2028, 8, 1),
            notes="Rollback",
            document_reference="DOC-ROLL",
            external_document_id="EXT-ROLL",
        )
        repository.add(certificate_two)
        session_one.rollback()

        assert (
            verification_repository_before_commit.get_by_id(certificate_two.id.value)
            is None
        )
    finally:
        session_one.close()
        session_two.close()
