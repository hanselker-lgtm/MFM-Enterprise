from __future__ import annotations

import ast
from datetime import date
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import mfm.database.models  # noqa: F401
import pytest
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from mfm.application.certificates.activate_certificate import ActivateCertificateUseCase
from mfm.application.certificates.create_certificate import CreateCertificateUseCase
from mfm.application.certificates.evaluate_certificate_status import (
    EvaluateCertificateStatusUseCase,
)
from mfm.application.certificates.get_certificate_history import (
    GetCertificateHistoryUseCase,
)
from mfm.application.certificates.get_expiring_certificates import (
    GetExpiringCertificatesUseCase,
)
from mfm.application.certificates.renew_certificate import RenewCertificateUseCase
from mfm.application.certificates.revoke_certificate import RevokeCertificateUseCase
from mfm.application.certificates.suspend_certificate import SuspendCertificateUseCase
from mfm.application.features.certificates.activate_certificate_feature import (
    ActivateCertificateFeature,
)
from mfm.application.features.certificates.activate_certificate_feature import (
    ActivateCertificateRequest,
)
from mfm.application.features.certificates.create_certificate_feature import (
    ComplianceObservationInput,
)
from mfm.application.features.certificates.create_certificate_feature import (
    CreateCertificateFeature,
)
from mfm.application.features.certificates.create_certificate_feature import (
    CreateCertificateRequest,
)
from mfm.application.features.certificates.create_certificate_feature import (
    RepositoryException,
)
from mfm.application.features.certificates.evaluate_certificate_status_feature import (
    EvaluateCertificateStatusFeature,
)
from mfm.application.features.certificates.evaluate_certificate_status_feature import (
    EvaluateCertificateStatusRequest,
)
from mfm.application.features.certificates.get_certificate_history_feature import (
    GetCertificateHistoryFeature,
)
from mfm.application.features.certificates.get_certificate_history_feature import (
    GetCertificateHistoryRequest,
)
from mfm.application.features.certificates.get_expiring_certificates_feature import (
    GetExpiringCertificatesFeature,
)
from mfm.application.features.certificates.get_expiring_certificates_feature import (
    GetExpiringCertificatesRequest,
)
from mfm.application.features.certificates.renew_certificate_feature import (
    RenewCertificateFeature,
)
from mfm.application.features.certificates.renew_certificate_feature import (
    RenewCertificateRequest,
)
from mfm.application.features.certificates.revoke_certificate_feature import (
    RevokeCertificateFeature,
)
from mfm.application.features.certificates.revoke_certificate_feature import (
    RevokeCertificateRequest,
)
from mfm.application.features.certificates.suspend_certificate_feature import (
    SuspendCertificateFeature,
)
from mfm.application.features.certificates.suspend_certificate_feature import (
    SuspendCertificateRequest,
)
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.database.models.asset_location_model import AssetLocationModel  # noqa: F401
from mfm.database.models.asset_model import AssetModel  # noqa: F401
from mfm.database.models.base_model import BaseModel
from mfm.domain.certificates.certificate_status import CertificateStatus
from mfm.domain.certificates.certificate_target_type import CertificateTargetType
from mfm.infrastructure.persistence.sqlite.sqlite_certificate_repository import (
    SQLiteCertificateRepository,
)
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteCertificateApplicationUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session, *, fail_commit: bool = False) -> None:
        super().__init__()
        self._session = session
        self._persistence_uow: UnitOfWork | None = None
        self._fail_commit = fail_commit

    def _start_scope(self) -> None:
        self._persistence_uow = UnitOfWork(self._session)
        self.certificate_repository = SQLiteCertificateRepository(self._persistence_uow)

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

    def _commit_impl(self) -> None:
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")
        assert self._persistence_uow is not None
        self._persistence_uow.commit()

    def _rollback_impl(self) -> None:
        assert self._persistence_uow is not None
        self._persistence_uow.rollback()

    def _flush_impl(self) -> None:
        self._session.flush()

    def _close_impl(self) -> None:
        return None


@pytest.fixture()
def sqlite_session_factory(tmp_path: Path):
    db_path = tmp_path / "certificate_feature_e2e.sqlite"
    engine = create_engine(f"sqlite:///{db_path}")
    BaseModel.metadata.create_all(engine)

    factory = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)
    try:
        yield factory
    finally:
        engine.dispose()


def _build_feature_stack(
    session: Session,
    *,
    fail_commit: bool = False,
) -> dict[str, object]:
    uow = SQLiteCertificateApplicationUnitOfWork(session, fail_commit=fail_commit)

    return {
        "create": CreateCertificateFeature(service=CreateCertificateUseCase(unit_of_work=uow)),
        "activate": ActivateCertificateFeature(
            service=ActivateCertificateUseCase(unit_of_work=uow)
        ),
        "evaluate": EvaluateCertificateStatusFeature(
            service=EvaluateCertificateStatusUseCase(unit_of_work=uow)
        ),
        "suspend": SuspendCertificateFeature(service=SuspendCertificateUseCase(unit_of_work=uow)),
        "revoke": RevokeCertificateFeature(service=RevokeCertificateUseCase(unit_of_work=uow)),
        "renew": RenewCertificateFeature(service=RenewCertificateUseCase(unit_of_work=uow)),
        "history": GetCertificateHistoryFeature(
            service=GetCertificateHistoryUseCase(unit_of_work=uow)
        ),
        "expiring": GetExpiringCertificatesFeature(
            service=GetExpiringCertificatesUseCase(unit_of_work=uow)
        ),
    }


def _create_request(
    *,
    target_type: str = "VESSEL",
    target_id: UUID | None = None,
    certificate_number: str = "CERT-A",
    issuer_type: str = "AUTHORITY",
    issuer_id_or_external_key: str = "ISSUER-A",
    issuer_name_snapshot: str = "Maritime Authority A",
    issued_date: date = date(2027, 1, 1),
    valid_from: date = date(2027, 1, 1),
    expires_at: date | None = date(2028, 1, 1),
    notes: str | None = "Context A notes",
    document_reference: str | None = "DOC-A",
) -> CreateCertificateRequest:
    return CreateCertificateRequest(
        certificate_type_id=UUID("00000000-0000-0000-0000-00000000F101"),
        certificate_type_code="STATUTORY_CERT",
        certificate_type_display_name_snapshot="Statutory Certificate",
        target_type=target_type,
        target_id=target_id or uuid4(),
        certificate_number=certificate_number,
        issuer_type=issuer_type,
        issuer_id_or_external_key=issuer_id_or_external_key,
        issuer_name_snapshot=issuer_name_snapshot,
        issued_date=issued_date,
        valid_from=valid_from,
        expires_at=expires_at,
        renewal_required=True,
        document_reference=document_reference,
        external_document_id="EXT-A",
        notes=notes,
        compliance_observations=(
            ComplianceObservationInput(
                summary="Inspection indicates maintenance work required",
                observed_on=date(2027, 12, 1),
                requires_maintenance_work=True,
            ),
        ),
    )


def test_e2e_workflow_1_create_vessel_certificate(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        assert isinstance(create, CreateCertificateFeature)

        target_id = uuid4()
        response = create.execute(_create_request(target_id=target_id))

        # Public response proof.
        assert isinstance(response.certificate.id, UUID)
        assert response.certificate.target.target_type == "VESSEL"
        assert response.certificate.target.target_id == target_id
        assert isinstance(response.certificate.status, str)
        assert response.certificate.issuer.issuer_name_snapshot == "Maritime Authority A"

        session.close()
        read_session = sqlite_session_factory()
        try:
            read_repository = SQLiteCertificateRepository(UnitOfWork(read_session))
            loaded = read_repository.get_by_id(response.certificate.id)
            assert loaded is not None
            assert loaded.certificate_number == "CERT-A"
            assert loaded.target.target_type is CertificateTargetType.VESSEL
            assert loaded.target.target_id == target_id
            assert loaded.issuer.issuer_id_or_external_key == "ISSUER-A"
            assert loaded.issuer.issuer_name_snapshot == "Maritime Authority A"
            assert loaded.issued_date == date(2027, 1, 1)
            assert loaded.valid_from == date(2027, 1, 1)
            assert loaded.expires_at == date(2028, 1, 1)
            assert loaded.status is CertificateStatus.DRAFT
            assert loaded.notes == "Context A notes"
            assert loaded.document_reference == "DOC-A"
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_2_activate_certificate(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        activate = stack["activate"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)

        created = create.execute(_create_request(certificate_number="CERT-ACT"))
        activated = activate.execute(
            ActivateCertificateRequest(certificate_id=created.certificate.id)
        )
        assert activated.certificate.status == "ACTIVE"

        session.close()
        read_session = sqlite_session_factory()
        try:
            read_repository = SQLiteCertificateRepository(UnitOfWork(read_session))
            loaded = read_repository.get_by_id(created.certificate.id)
            assert loaded is not None
            assert loaded.status is CertificateStatus.ACTIVE
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_3_valid_evaluation_no_state_mutation(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        activate = stack["activate"]
        evaluate = stack["evaluate"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)
        assert isinstance(evaluate, EvaluateCertificateStatusFeature)

        created = create.execute(_create_request(certificate_number="CERT-VALID"))
        activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))

        result = evaluate.execute(
            EvaluateCertificateStatusRequest(
                certificate_id=created.certificate.id,
                as_of_date=date(2027, 3, 1),
                expiring_threshold_days=30,
            )
        )

        assert result.evaluated_status == "VALID"
        assert result.certificate.status == "ACTIVE"

        session.close()
        read_session = sqlite_session_factory()
        try:
            read_repository = SQLiteCertificateRepository(UnitOfWork(read_session))
            loaded = read_repository.get_by_id(created.certificate.id)
            assert loaded is not None
            assert loaded.status is CertificateStatus.ACTIVE
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_4_expiring_evaluation_boundary(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        activate = stack["activate"]
        evaluate = stack["evaluate"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)
        assert isinstance(evaluate, EvaluateCertificateStatusFeature)

        created = create.execute(
            _create_request(
                certificate_number="CERT-EXPIRING",
                expires_at=date(2028, 1, 1),
            )
        )
        activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))

        result = evaluate.execute(
            EvaluateCertificateStatusRequest(
                certificate_id=created.certificate.id,
                as_of_date=date(2027, 12, 2),
                expiring_threshold_days=30,
            )
        )

        assert result.evaluated_status == "EXPIRING"
        assert result.certificate.status == "ACTIVE"

        session.close()
        read_session = sqlite_session_factory()
        try:
            read_repository = SQLiteCertificateRepository(UnitOfWork(read_session))
            loaded = read_repository.get_by_id(created.certificate.id)
            assert loaded is not None
            assert loaded.status is CertificateStatus.ACTIVE
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_5_expired_evaluation_with_explicit_date(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        activate = stack["activate"]
        evaluate = stack["evaluate"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)
        assert isinstance(evaluate, EvaluateCertificateStatusFeature)

        created = create.execute(
            _create_request(
                certificate_number="CERT-EXPIRED",
                expires_at=date(2028, 1, 1),
            )
        )
        activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))

        result = evaluate.execute(
            EvaluateCertificateStatusRequest(
                certificate_id=created.certificate.id,
                as_of_date=date(2028, 1, 2),
                expiring_threshold_days=30,
            )
        )

        assert result.evaluated_status == "EXPIRED"
        assert result.certificate.status == "EXPIRED"

        session.close()
        read_session = sqlite_session_factory()
        try:
            read_repository = SQLiteCertificateRepository(UnitOfWork(read_session))
            loaded = read_repository.get_by_id(created.certificate.id)
            assert loaded is not None
            assert loaded.status is CertificateStatus.EXPIRED
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_6_renewal_historical_truth_and_roundtrip(sqlite_session_factory) -> None:
    write_session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(write_session)
        create = stack["create"]
        activate = stack["activate"]
        renew = stack["renew"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)
        assert isinstance(renew, RenewCertificateFeature)

        cert_a = create.execute(
            _create_request(
                certificate_number="CERT-A",
                issuer_id_or_external_key="ISSUER-A",
                issuer_name_snapshot="Maritime Authority A",
                issued_date=date(2027, 1, 1),
                valid_from=date(2027, 1, 1),
                expires_at=date(2028, 1, 1),
                notes="Context A notes",
                document_reference="DOC-A",
            )
        )
        activate.execute(ActivateCertificateRequest(certificate_id=cert_a.certificate.id))

        cert_b = renew.execute(
            RenewCertificateRequest(
                source_certificate_id=cert_a.certificate.id,
                certificate_number="CERT-B",
                issuer_type="AUTHORITY",
                issuer_id_or_external_key="ISSUER-B",
                issuer_name_snapshot="Maritime Authority B",
                issued_date=date(2028, 1, 2),
                valid_from=date(2028, 1, 2),
                expires_at=date(2029, 1, 1),
                document_reference="DOC-B",
                external_document_id="EXT-B",
                notes="Context B notes",
                renewal_required=False,
            )
        )

        # Prove A->B->C chain in scope.
        activate.execute(ActivateCertificateRequest(certificate_id=cert_b.renewed_certificate.id))
        renew.execute(
            RenewCertificateRequest(
                source_certificate_id=cert_b.renewed_certificate.id,
                certificate_number="CERT-C",
                issuer_type="AUTHORITY",
                issuer_id_or_external_key="ISSUER-C",
                issuer_name_snapshot="Maritime Authority C",
                issued_date=date(2029, 1, 2),
                valid_from=date(2029, 1, 2),
                expires_at=date(2030, 1, 1),
                document_reference="DOC-C",
                external_document_id="EXT-C",
                notes="Context C notes",
                renewal_required=True,
            )
        )

        # New persistence session boundary for history proof.
        write_session.close()
        read_session = sqlite_session_factory()
        try:
            read_stack = _build_feature_stack(read_session)
            history = read_stack["history"]
            assert isinstance(history, GetCertificateHistoryFeature)

            chain = history.execute(
                GetCertificateHistoryRequest(certificate_id=cert_a.certificate.id)
            )

            assert [item.certificate_number for item in chain.certificates] == [
                "CERT-A",
                "CERT-B",
                "CERT-C",
            ]

            a = chain.certificates[0]
            b = chain.certificates[1]
            c = chain.certificates[2]

            assert a.issuer.issuer_name_snapshot == "Maritime Authority A"
            assert a.issued_date == date(2027, 1, 1)
            assert a.valid_from == date(2027, 1, 1)
            assert a.expires_at == date(2028, 1, 1)
            assert a.notes == "Context A notes"
            assert a.document_reference == "DOC-A"

            assert b.issuer.issuer_name_snapshot == "Maritime Authority B"
            assert b.issued_date == date(2028, 1, 2)
            assert b.valid_from == date(2028, 1, 2)
            assert b.expires_at == date(2029, 1, 1)
            assert b.notes == "Context B notes"
            assert b.document_reference == "DOC-B"
            assert b.renewed_from_certificate_id == a.id

            assert c.issuer.issuer_name_snapshot == "Maritime Authority C"
            assert c.notes == "Context C notes"
            assert c.renewed_from_certificate_id == b.id

            # Repository-level roundtrip proof of separate historical records.
            repository = SQLiteCertificateRepository(UnitOfWork(read_session))
            all_certificates = {item.id.value: item for item in repository.list()}
            assert a.id in all_certificates
            assert b.id in all_certificates
            assert c.id in all_certificates
            assert all_certificates[a.id].certificate_number == "CERT-A"
            assert all_certificates[b.id].certificate_number == "CERT-B"
            assert all_certificates[c.id].certificate_number == "CERT-C"
            assert all_certificates[b.id].renewed_from_certificate_id is not None
            assert all_certificates[b.id].renewed_from_certificate_id.value == a.id
            assert all_certificates[b.id].issuer.issuer_name_snapshot == "Maritime Authority B"
        finally:
            read_session.close()
    finally:
        if write_session.is_active:
            write_session.close()


def test_e2e_workflow_7_suspend_certificate(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        activate = stack["activate"]
        suspend = stack["suspend"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)
        assert isinstance(suspend, SuspendCertificateFeature)

        created = create.execute(_create_request(certificate_number="CERT-SUSPEND"))
        activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))

        suspended = suspend.execute(
            SuspendCertificateRequest(
                certificate_id=created.certificate.id,
                notes="Suspended for review",
            )
        )
        assert suspended.certificate.status == "SUSPENDED"

        with pytest.raises(Exception):
            suspend.execute(SuspendCertificateRequest(certificate_id=created.certificate.id))

        session.close()
        read_session = sqlite_session_factory()
        try:
            repository = SQLiteCertificateRepository(UnitOfWork(read_session))
            loaded = repository.get_by_id(created.certificate.id)
            assert loaded is not None
            assert loaded.status is CertificateStatus.SUSPENDED
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_8_revoke_certificate(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        activate = stack["activate"]
        revoke = stack["revoke"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)
        assert isinstance(revoke, RevokeCertificateFeature)

        created = create.execute(_create_request(certificate_number="CERT-REVOKE"))
        activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))

        revoked = revoke.execute(
            RevokeCertificateRequest(
                certificate_id=created.certificate.id,
                notes="Revoked by authority",
            )
        )
        assert revoked.certificate.status == "REVOKED"

        with pytest.raises(Exception):
            activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))

        session.close()
        read_session = sqlite_session_factory()
        try:
            repository = SQLiteCertificateRepository(UnitOfWork(read_session))
            loaded = repository.get_by_id(created.certificate.id)
            assert loaded is not None
            assert loaded.status is CertificateStatus.REVOKED
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_9_organization_target_identity_only(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        assert isinstance(create, CreateCertificateFeature)

        target_id = uuid4()
        created = create.execute(
            _create_request(
                target_type="ORGANIZATION",
                target_id=target_id,
                certificate_number="CERT-ORG",
            )
        )

        session.close()
        read_session = sqlite_session_factory()
        try:
            history = _build_feature_stack(read_session)["history"]
            assert isinstance(history, GetCertificateHistoryFeature)
            result = history.execute(
                GetCertificateHistoryRequest(certificate_id=created.certificate.id)
            )
            assert len(result.certificates) == 1
            assert result.certificates[0].target.target_type == "ORGANIZATION"
            assert result.certificates[0].target.target_id == target_id
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_10_compliance_finding_without_maintenance_side_effect(
    sqlite_session_factory,
) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        history = stack["history"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(history, GetCertificateHistoryFeature)

        created = create.execute(_create_request(certificate_number="CERT-COMP"))
        found = history.execute(
            GetCertificateHistoryRequest(certificate_id=created.certificate.id)
        )
        assert len(found.certificates) == 1
        assert (
            found.certificates[0].compliance_observations[0].requires_maintenance_work
            is True
        )

        # No maintenance workflow side effects.
        maintenance_tables = [
            "maintenance_plan",
            "maintenance_requirement",
            "work_order",
            "maintenance_record",
        ]
        for table in maintenance_tables:
            count = session.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar_one()
            assert count == 0
    finally:
        if session.is_active:
            session.close()


def test_e2e_workflow_11_failure_and_rollback(sqlite_session_factory) -> None:
    setup_session = sqlite_session_factory()
    try:
        setup_stack = _build_feature_stack(setup_session)
        create = setup_stack["create"]
        activate = setup_stack["activate"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)

        cert_a = create.execute(
            _create_request(
                certificate_number="CERT-ROLL-A",
                notes="Original A",
                expires_at=date(2028, 1, 1),
            )
        )
        activate.execute(ActivateCertificateRequest(certificate_id=cert_a.certificate.id))
        setup_session.close()

        # Domain-invalid renewal fails before persistence.
        invalid_session = sqlite_session_factory()
        try:
            invalid_stack = _build_feature_stack(invalid_session)
            renew = invalid_stack["renew"]
            assert isinstance(renew, RenewCertificateFeature)

            with pytest.raises(Exception):
                renew.execute(
                    RenewCertificateRequest(
                        source_certificate_id=cert_a.certificate.id,
                        certificate_number="CERT-ROLL-INVALID",
                        issuer_type="AUTHORITY",
                        issuer_id_or_external_key="ISSUER-X",
                        issuer_name_snapshot="Issuer X",
                        issued_date=date(2027, 1, 1),
                        valid_from=date(2026, 1, 1),
                        expires_at=date(2028, 1, 1),
                    )
                )
        finally:
            invalid_session.close()

        # Transaction-stage failure with rollback.
        failing_session = sqlite_session_factory()
        try:
            failing_stack = _build_feature_stack(failing_session, fail_commit=True)
            renew = failing_stack["renew"]
            assert isinstance(renew, RenewCertificateFeature)

            with pytest.raises(RepositoryException):
                renew.execute(
                    RenewCertificateRequest(
                        source_certificate_id=cert_a.certificate.id,
                        certificate_number="CERT-ROLL-B",
                        issuer_type="AUTHORITY",
                        issuer_id_or_external_key="ISSUER-B",
                        issuer_name_snapshot="Issuer B",
                        issued_date=date(2028, 1, 2),
                        valid_from=date(2028, 1, 2),
                        expires_at=date(2029, 1, 1),
                        notes="Should rollback",
                    )
                )
        finally:
            failing_session.close()

        verify_session = sqlite_session_factory()
        try:
            repository = SQLiteCertificateRepository(UnitOfWork(verify_session))
            all_items = repository.list()
            numbers = {item.certificate_number for item in all_items}
            assert "CERT-ROLL-A" in numbers
            assert "CERT-ROLL-B" not in numbers

            original = next(item for item in all_items if item.certificate_number == "CERT-ROLL-A")
            assert original.notes == "Original A"
            assert original.renewed_from_certificate_id is None
        finally:
            verify_session.close()
    finally:
        if setup_session.is_active:
            setup_session.close()


def test_e2e_workflow_12_capability_boundary_and_expiring_query(sqlite_session_factory) -> None:
    session = sqlite_session_factory()
    try:
        stack = _build_feature_stack(session)
        create = stack["create"]
        activate = stack["activate"]
        expiring = stack["expiring"]
        assert isinstance(create, CreateCertificateFeature)
        assert isinstance(activate, ActivateCertificateFeature)
        assert isinstance(expiring, GetExpiringCertificatesFeature)

        vessel = create.execute(
            _create_request(certificate_number="CERT-BOUND-V", target_type="VESSEL")
        )
        organization = create.execute(
            _create_request(
                certificate_number="CERT-BOUND-O",
                target_type="ORGANIZATION",
            )
        )

        exp_cert = create.execute(
            _create_request(
                certificate_number="CERT-EXP-Q",
                expires_at=date(2028, 1, 20),
            )
        )
        outside = create.execute(
            _create_request(
                certificate_number="CERT-OUTSIDE",
                expires_at=date(2028, 6, 1),
            )
        )
        non_exp = create.execute(
            _create_request(
                certificate_number="CERT-NONEXP",
                expires_at=None,
            )
        )
        revoked = create.execute(
            _create_request(
                certificate_number="CERT-REVOKED",
                expires_at=date(2028, 1, 15),
            )
        )

        activate.execute(ActivateCertificateRequest(certificate_id=vessel.certificate.id))
        activate.execute(
            ActivateCertificateRequest(certificate_id=organization.certificate.id)
        )
        activate.execute(ActivateCertificateRequest(certificate_id=exp_cert.certificate.id))
        activate.execute(ActivateCertificateRequest(certificate_id=outside.certificate.id))
        activate.execute(ActivateCertificateRequest(certificate_id=non_exp.certificate.id))
        activate.execute(ActivateCertificateRequest(certificate_id=revoked.certificate.id))
        stack["revoke"].execute(
            RevokeCertificateRequest(certificate_id=revoked.certificate.id)
        )

        session.close()
        read_session = sqlite_session_factory()
        try:
            read_stack = _build_feature_stack(read_session)
            expiring_feature = read_stack["expiring"]
            assert isinstance(expiring_feature, GetExpiringCertificatesFeature)

            response = expiring_feature.execute(
                GetExpiringCertificatesRequest(
                    as_of_date=date(2028, 1, 1),
                    within_days=30,
                )
            )
            numbers = {item.certificate_number for item in response.certificates}

            assert "CERT-EXP-Q" in numbers
            assert "CERT-OUTSIDE" not in numbers
            assert "CERT-NONEXP" not in numbers
            assert "CERT-REVOKED" not in numbers
            assert "CERT-BOUND-V" in numbers
            assert "CERT-BOUND-O" in numbers

            # Public API safety proof for nested responses.
            for item in response.certificates:
                assert isinstance(item.id, UUID)
                assert isinstance(item.status, str)
                assert isinstance(item.target.target_type, str)
                assert isinstance(item.issuer.issuer_name_snapshot, str)
        finally:
            read_session.close()
    finally:
        if session.is_active:
            session.close()


def test_certificate_feature_and_application_have_no_hidden_clock() -> None:
    root = Path(__file__).resolve().parents[4] / "src" / "mfm" / "application"
    paths = list((root / "features" / "certificates").rglob("*.py"))
    paths.extend((root / "certificates").rglob("*.py"))

    for path in paths:
        content = path.read_text(encoding="utf-8")
        assert "date.today(" not in content
        assert "datetime.now(" not in content


def test_certificate_feature_layer_no_persistence_or_locked_capability_imports() -> None:
    root = Path(__file__).resolve().parents[4] / "src" / "mfm" / "application" / "features" / "certificates"
    forbidden_prefixes = (
        "sqlalchemy",
        "mfm.database",
        "mfm.application.features.maintenance",
        "mfm.application.maintenance",
        "mfm.application.features.fleet",
        "mfm.application.fleet",
        "mfm.application.features.organization",
        "mfm.application.organization",
        "mfm.infrastructure.persistence",
    )

    for path in root.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
        imported_modules: set[str] = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_modules.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported_modules.add(node.module)

        for prefix in forbidden_prefixes:
            assert prefix not in source
            assert not any(
                item == prefix or item.startswith(f"{prefix}.")
                for item in imported_modules
            )
