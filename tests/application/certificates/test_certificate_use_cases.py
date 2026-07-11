from __future__ import annotations

from copy import deepcopy
from dataclasses import is_dataclass
from datetime import date
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.certificates.activate_certificate import ActivateCertificateRequest
from mfm.application.certificates.activate_certificate import ActivateCertificateUseCase
from mfm.application.certificates.create_certificate import BusinessRuleViolation
from mfm.application.certificates.create_certificate import ComplianceObservationInput
from mfm.application.certificates.create_certificate import CreateCertificateRequest
from mfm.application.certificates.create_certificate import CreateCertificateUseCase
from mfm.application.certificates.create_certificate import RepositoryException
from mfm.application.certificates.create_certificate import ValidationException
from mfm.application.certificates.evaluate_certificate_status import (
    EvaluateCertificateStatusRequest,
)
from mfm.application.certificates.evaluate_certificate_status import (
    EvaluateCertificateStatusUseCase,
)
from mfm.application.certificates.get_certificate_history import (
    GetCertificateHistoryRequest,
)
from mfm.application.certificates.get_certificate_history import (
    GetCertificateHistoryUseCase,
)
from mfm.application.certificates.get_expiring_certificates import (
    GetExpiringCertificatesRequest,
)
from mfm.application.certificates.get_expiring_certificates import (
    GetExpiringCertificatesUseCase,
)
from mfm.application.certificates.renew_certificate import RenewCertificateRequest
from mfm.application.certificates.renew_certificate import RenewCertificateUseCase
from mfm.application.certificates.revoke_certificate import RevokeCertificateRequest
from mfm.application.certificates.revoke_certificate import RevokeCertificateUseCase
from mfm.application.certificates.suspend_certificate import SuspendCertificateRequest
from mfm.application.certificates.suspend_certificate import SuspendCertificateUseCase
from mfm.application.uow.abstract_unit_of_work import AbstractUnitOfWork
from mfm.domain.certificates.certificate import Certificate
from mfm.domain.certificates.certificate_status import CertificateStatus
from mfm.domain.certificates.certificate_target import CertificateTarget
from mfm.domain.certificates.certificate_target_type import CertificateTargetType
from mfm.domain.certificates.certificate_type_reference import CertificateTypeReference
from mfm.domain.certificates.identifiers import CertificateTypeId
from mfm.domain.certificates.issuer_reference import IssuerReference
from mfm.domain.certificates.issuer_reference_type import IssuerReferenceType
from mfm.repositories.certificate_repository import CertificateRepository


class InMemoryCertificateRepository(CertificateRepository):
    def __init__(self) -> None:
        self._items: dict[UUID, Certificate] = {}
        self.add_calls = 0
        self.update_calls = 0
        self.get_expiring_calls = 0

    def snapshot(self) -> dict[UUID, Certificate]:
        return deepcopy(self._items)

    def restore(self, snapshot: dict[UUID, Certificate]) -> None:
        self._items = deepcopy(snapshot)

    def add(self, certificate: Certificate) -> None:
        self.add_calls += 1
        if certificate.id.value in self._items:
            raise ValueError("certificate already exists")
        self._items[certificate.id.value] = deepcopy(certificate)

    def get_by_id(self, certificate_id: UUID) -> Certificate | None:
        item = self._items.get(certificate_id)
        return deepcopy(item) if item is not None else None

    def update(self, certificate: Certificate) -> None:
        self.update_calls += 1
        if certificate.id.value not in self._items:
            raise ValueError("certificate does not exist")
        self._items[certificate.id.value] = deepcopy(certificate)

    def exists(self, certificate_id: UUID) -> bool:
        return certificate_id in self._items

    def list(self) -> list[Certificate]:
        return [deepcopy(item) for item in self._items.values()]

    def get_by_target(self, target: CertificateTarget) -> list[Certificate]:
        return [
            deepcopy(item)
            for item in self._items.values()
            if item.target == target
        ]

    def get_active_by_target(self, target: CertificateTarget) -> list[Certificate]:
        return [
            deepcopy(item)
            for item in self._items.values()
            if item.target == target and item.status is CertificateStatus.ACTIVE
        ]

    def get_expiring(self, *, as_of_date: date, within_days: int) -> list[Certificate]:
        self.get_expiring_calls += 1
        result: list[Certificate] = []
        threshold = as_of_date.toordinal() + within_days
        for item in self._items.values():
            if item.status is not CertificateStatus.ACTIVE:
                continue
            if item.expires_at is None:
                continue
            exp = item.expires_at.toordinal()
            if as_of_date.toordinal() <= exp <= threshold:
                result.append(deepcopy(item))
        result.sort(key=lambda cert: cert.expires_at or date.max)
        return result

    def get_expired(self, *, as_of_date: date) -> list[Certificate]:
        result: list[Certificate] = []
        for item in self._items.values():
            if item.status is CertificateStatus.EXPIRED:
                result.append(deepcopy(item))
                continue
            if (
                item.status is CertificateStatus.ACTIVE
                and item.expires_at is not None
                and item.expires_at < as_of_date
            ):
                result.append(deepcopy(item))
        result.sort(key=lambda cert: cert.expires_at or date.max)
        return result

    def get_renewal_history(self, certificate_id: UUID) -> list[Certificate]:
        start = self._items.get(certificate_id)
        if start is None:
            return []

        by_id = self._items
        root = start
        while root.renewed_from_certificate_id is not None:
            parent = by_id.get(root.renewed_from_certificate_id.value)
            if parent is None:
                break
            root = parent

        history: list[Certificate] = [deepcopy(root)]
        current = root
        while True:
            children = [
                item
                for item in by_id.values()
                if item.renewed_from_certificate_id is not None
                and item.renewed_from_certificate_id.value == current.id.value
            ]
            if not children:
                break
            child = sorted(children, key=lambda item: item.issued_date)[0]
            history.append(deepcopy(child))
            current = child

        return history


class FakeCertificateUnitOfWork(AbstractUnitOfWork):
    def __init__(self, *, fail_commit: bool = False) -> None:
        super().__init__()
        self._repository = InMemoryCertificateRepository()
        self._fail_commit = fail_commit
        self.commits = 0
        self.rollbacks = 0
        self._snapshot: dict[UUID, Certificate] = {}

    def _start_scope(self) -> None:
        self.certificate_repository = self._repository
        self._snapshot = self._repository.snapshot()

        self.contact_repository = None
        self.member_repository = None
        self.membership_repository = None
        self.invoice_repository = None
        self.payment_repository = None
        self.journal_repository = None

    def _commit_impl(self) -> None:
        self.commits += 1
        if self._fail_commit:
            raise RuntimeError("simulated commit failure")

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self._repository.restore(self._snapshot)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


def _create_request(
    *,
    target_type: str = "VESSEL",
    target_id: UUID | None = None,
    certificate_number: str = "CERT-A",
    issuer_type: str = "AUTHORITY",
    issuer_id_or_external_key: str = "AUTH-001",
    issuer_name_snapshot: str = "Maritime Authority A",
    issued_date: date = date(2027, 1, 1),
    valid_from: date = date(2027, 1, 1),
    expires_at: date | None = date(2028, 1, 1),
    notes: str | None = "Context A",
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
        document_reference="DOC-A",
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


def test_create_certificate_vessel_target_and_public_safe_mapping() -> None:
    uow = FakeCertificateUnitOfWork()

    response = CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())

    assert response.certificate.target.target_type == "VESSEL"
    assert is_dataclass(response.certificate)
    assert response.certificate.issuer.issuer_name_snapshot == "Maritime Authority A"
    assert response.certificate.document_reference == "DOC-A"
    assert response.certificate.compliance_observations[0].requires_maintenance_work is True
    assert uow.commits == 1
    assert uow.rollbacks == 0


def test_create_certificate_organization_target_supported() -> None:
    uow = FakeCertificateUnitOfWork()

    response = CreateCertificateUseCase(unit_of_work=uow).execute(
        _create_request(target_type="ORGANIZATION")
    )

    assert response.certificate.target.target_type == "ORGANIZATION"


def test_create_certificate_invalid_request_rolls_back() -> None:
    uow = FakeCertificateUnitOfWork()

    with pytest.raises(ValidationException):
        CreateCertificateUseCase(unit_of_work=uow).execute(
            _create_request(target_type="INVALID")
        )

    assert uow.commits == 0


def test_create_certificate_commit_failure_raises_repository_exception() -> None:
    uow = FakeCertificateUnitOfWork(fail_commit=True)

    with pytest.raises(RepositoryException):
        CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())

    assert uow.commits == 1
    assert uow.rollbacks >= 1


def test_activate_certificate_valid_and_invalid_paths() -> None:
    uow = FakeCertificateUnitOfWork()
    created = CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())

    activated = ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created.certificate.id)
    )
    assert activated.certificate.status == "ACTIVE"

    with pytest.raises(BusinessRuleViolation):
        ActivateCertificateUseCase(unit_of_work=uow).execute(
            ActivateCertificateRequest(certificate_id=created.certificate.id)
        )

    with pytest.raises(BusinessRuleViolation):
        ActivateCertificateUseCase(unit_of_work=uow).execute(
            ActivateCertificateRequest(certificate_id=uuid4())
        )


def test_evaluate_status_expiring_and_non_expiring_without_hidden_clock() -> None:
    uow = FakeCertificateUnitOfWork()
    created = CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created.certificate.id)
    )

    expiring = EvaluateCertificateStatusUseCase(unit_of_work=uow).execute(
        EvaluateCertificateStatusRequest(
            certificate_id=created.certificate.id,
            as_of_date=date(2027, 12, 15),
            expiring_threshold_days=30,
        )
    )
    assert expiring.evaluated_status == "EXPIRING"
    assert expiring.certificate.status == "ACTIVE"

    non_expiring_created = CreateCertificateUseCase(unit_of_work=uow).execute(
        _create_request(
            certificate_number="CERT-NONEXP",
            expires_at=None,
            notes="Non-expiring",
        )
    )
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=non_expiring_created.certificate.id)
    )

    non_expiring = EvaluateCertificateStatusUseCase(unit_of_work=uow).execute(
        EvaluateCertificateStatusRequest(
            certificate_id=non_expiring_created.certificate.id,
            as_of_date=date(2035, 1, 1),
            expiring_threshold_days=30,
        )
    )
    assert non_expiring.evaluated_status == "VALID"


def test_evaluate_status_expired_persists_domain_state_when_mutated() -> None:
    uow = FakeCertificateUnitOfWork()
    created = CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created.certificate.id)
    )

    expired = EvaluateCertificateStatusUseCase(unit_of_work=uow).execute(
        EvaluateCertificateStatusRequest(
            certificate_id=created.certificate.id,
            as_of_date=date(2028, 1, 2),
            expiring_threshold_days=30,
        )
    )

    assert expired.evaluated_status == "EXPIRED"
    assert expired.certificate.status == "EXPIRED"


def test_suspend_and_revoke_certificate_paths_with_commit_and_rollback() -> None:
    uow = FakeCertificateUnitOfWork()
    created = CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())

    with pytest.raises(BusinessRuleViolation):
        SuspendCertificateUseCase(unit_of_work=uow).execute(
            SuspendCertificateRequest(certificate_id=created.certificate.id)
        )

    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created.certificate.id)
    )

    suspended = SuspendCertificateUseCase(unit_of_work=uow).execute(
        SuspendCertificateRequest(
            certificate_id=created.certificate.id,
            notes="Pending review",
        )
    )
    assert suspended.certificate.status == "SUSPENDED"

    revoked = RevokeCertificateUseCase(unit_of_work=uow).execute(
        RevokeCertificateRequest(
            certificate_id=created.certificate.id,
            notes="Revoked after review",
        )
    )
    assert revoked.certificate.status == "REVOKED"

    with pytest.raises(BusinessRuleViolation):
        RevokeCertificateUseCase(unit_of_work=uow).execute(
            RevokeCertificateRequest(certificate_id=created.certificate.id)
        )


def test_renew_certificate_preserves_historical_truth_and_relation() -> None:
    uow = FakeCertificateUnitOfWork()
    created_a = CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created_a.certificate.id)
    )

    renewed = RenewCertificateUseCase(unit_of_work=uow).execute(
        RenewCertificateRequest(
            source_certificate_id=created_a.certificate.id,
            certificate_number="CERT-B",
            issuer_type="CLASSIFICATION_SOCIETY",
            issuer_id_or_external_key="CLASS-002",
            issuer_name_snapshot="Maritime Authority B",
            issued_date=date(2028, 1, 2),
            valid_from=date(2028, 1, 2),
            expires_at=date(2029, 1, 1),
            document_reference="DOC-B",
            external_document_id="EXT-B",
            notes="Context B",
            renewal_required=False,
        )
    )

    history = GetCertificateHistoryUseCase(unit_of_work=uow).execute(
        GetCertificateHistoryRequest(certificate_id=created_a.certificate.id)
    )

    assert len(history.certificates) == 2
    cert_a = history.certificates[0]
    cert_b = history.certificates[1]

    assert cert_a.certificate_number == "CERT-A"
    assert cert_a.issuer.issuer_name_snapshot == "Maritime Authority A"
    assert cert_a.notes == "Context A"

    assert cert_b.id == renewed.renewed_certificate.id
    assert cert_b.certificate_number == "CERT-B"
    assert cert_b.issuer.issuer_name_snapshot == "Maritime Authority B"
    assert cert_b.notes == "Context B"
    assert cert_b.renewed_from_certificate_id == cert_a.id


def test_get_certificate_history_chain_and_not_found() -> None:
    uow = FakeCertificateUnitOfWork()
    created_a = CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created_a.certificate.id)
    )

    renewed_b = RenewCertificateUseCase(unit_of_work=uow).execute(
        RenewCertificateRequest(
            source_certificate_id=created_a.certificate.id,
            certificate_number="CERT-B",
            issuer_type="CLASSIFICATION_SOCIETY",
            issuer_id_or_external_key="CLASS-002",
            issuer_name_snapshot="Maritime Authority B",
            issued_date=date(2028, 1, 2),
            valid_from=date(2028, 1, 2),
            expires_at=date(2029, 1, 1),
        )
    )
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=renewed_b.renewed_certificate.id)
    )

    RenewCertificateUseCase(unit_of_work=uow).execute(
        RenewCertificateRequest(
            source_certificate_id=renewed_b.renewed_certificate.id,
            certificate_number="CERT-C",
            issuer_type="INSPECTION_BODY",
            issuer_id_or_external_key="INSP-003",
            issuer_name_snapshot="Inspection Body C",
            issued_date=date(2029, 1, 2),
            valid_from=date(2029, 1, 2),
            expires_at=date(2030, 1, 1),
        )
    )

    chain = GetCertificateHistoryUseCase(unit_of_work=uow).execute(
        GetCertificateHistoryRequest(certificate_id=created_a.certificate.id)
    )
    assert [item.certificate_number for item in chain.certificates] == [
        "CERT-A",
        "CERT-B",
        "CERT-C",
    ]

    with pytest.raises(BusinessRuleViolation):
        GetCertificateHistoryUseCase(unit_of_work=uow).execute(
            GetCertificateHistoryRequest(certificate_id=uuid4())
        )


def test_get_expiring_certificates_and_boundary_dates() -> None:
    uow = FakeCertificateUnitOfWork()

    created_expiring = CreateCertificateUseCase(unit_of_work=uow).execute(
        _create_request(
            certificate_number="CERT-EXP",
            expires_at=date(2028, 1, 20),
            notes="Expiring",
        )
    )
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created_expiring.certificate.id)
    )

    created_non_expiring = CreateCertificateUseCase(unit_of_work=uow).execute(
        _create_request(
            certificate_number="CERT-NONEXP",
            expires_at=None,
            notes="Non-expiring",
        )
    )
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created_non_expiring.certificate.id)
    )

    created_expired = CreateCertificateUseCase(unit_of_work=uow).execute(
        _create_request(
            certificate_number="CERT-OLD",
            expires_at=date(2028, 1, 5),
            notes="Old",
        )
    )
    ActivateCertificateUseCase(unit_of_work=uow).execute(
        ActivateCertificateRequest(certificate_id=created_expired.certificate.id)
    )

    response = GetExpiringCertificatesUseCase(unit_of_work=uow).execute(
        GetExpiringCertificatesRequest(
            as_of_date=date(2028, 1, 1),
            within_days=30,
        )
    )

    numbers = {item.certificate_number for item in response.certificates}
    assert "CERT-EXP" in numbers
    assert "CERT-NONEXP" not in numbers
    assert "CERT-OLD" in numbers


def test_public_response_safety_no_domain_object_leakage() -> None:
    uow = FakeCertificateUnitOfWork()
    response = CreateCertificateUseCase(unit_of_work=uow).execute(_create_request())

    certificate = response.certificate
    assert isinstance(certificate.id, UUID)
    assert isinstance(certificate.certificate_type.code, str)
    assert isinstance(certificate.target.target_type, str)
    assert isinstance(certificate.target.target_id, UUID)
    assert isinstance(certificate.issuer.issuer_id_or_external_key, str)
    assert isinstance(certificate.issuer.issuer_name_snapshot, str)
    assert isinstance(certificate.status, str)
    assert certificate.renewed_from_certificate_id is None
