from __future__ import annotations

import ast
from copy import deepcopy
from dataclasses import is_dataclass
from datetime import date
from pathlib import Path
from uuid import UUID
from uuid import uuid4

import pytest

from mfm.application.certificates.activate_certificate import ActivateCertificateUseCase
from mfm.application.certificates.create_certificate import (
    BusinessRuleViolation as ServiceBusinessRuleViolation,
)
from mfm.application.certificates.create_certificate import (
    CreateCertificateResponse as ServiceCreateCertificateResponse,
)
from mfm.application.certificates.create_certificate import (
    CreateCertificateUseCase,
)
from mfm.application.certificates.create_certificate import (
    RepositoryException as ServiceRepositoryException,
)
from mfm.application.certificates.create_certificate import (
    ValidationException as ServiceValidationException,
)
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
    BusinessRuleViolation,
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
from mfm.application.features.certificates.create_certificate_feature import (
    ValidationException,
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
from mfm.domain.certificates.certificate import Certificate
from mfm.domain.certificates.certificate_status import CertificateStatus
from mfm.domain.certificates.certificate_target import CertificateTarget
from mfm.repositories.certificate_repository import CertificateRepository


class StubService:
    def __init__(self, *, response=None, error: Exception | None = None) -> None:
        self._response = response
        self._error = error
        self.last_request = None

    def execute(self, request):
        self.last_request = request
        if self._error is not None:
            raise self._error
        return self._response


class InMemoryCertificateRepository(CertificateRepository):
    def __init__(self) -> None:
        self._items: dict[UUID, Certificate] = {}

    def snapshot(self) -> dict[UUID, Certificate]:
        return deepcopy(self._items)

    def restore(self, snapshot: dict[UUID, Certificate]) -> None:
        self._items = deepcopy(snapshot)

    def add(self, certificate: Certificate) -> None:
        self._items[certificate.id.value] = deepcopy(certificate)

    def get_by_id(self, certificate_id: UUID) -> Certificate | None:
        item = self._items.get(certificate_id)
        return deepcopy(item) if item is not None else None

    def update(self, certificate: Certificate) -> None:
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
    def __init__(self) -> None:
        super().__init__()
        self._repository = InMemoryCertificateRepository()
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

    def _rollback_impl(self) -> None:
        self.rollbacks += 1
        self._repository.restore(self._snapshot)

    def _flush_impl(self) -> None:
        return None

    def _close_impl(self) -> None:
        return None


@pytest.fixture()
def feature_stack() -> dict[str, object]:
    uow = FakeCertificateUnitOfWork()
    return {
        "create": CreateCertificateFeature(
            service=CreateCertificateUseCase(unit_of_work=uow)
        ),
        "activate": ActivateCertificateFeature(
            service=ActivateCertificateUseCase(unit_of_work=uow)
        ),
        "evaluate": EvaluateCertificateStatusFeature(
            service=EvaluateCertificateStatusUseCase(unit_of_work=uow)
        ),
        "suspend": SuspendCertificateFeature(
            service=SuspendCertificateUseCase(unit_of_work=uow)
        ),
        "revoke": RevokeCertificateFeature(
            service=RevokeCertificateUseCase(unit_of_work=uow)
        ),
        "renew": RenewCertificateFeature(
            service=RenewCertificateUseCase(unit_of_work=uow)
        ),
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
        target_id=uuid4(),
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


def _cert_files() -> list[Path]:
    root = Path(__file__).resolve().parents[4] / "src" / "mfm" / "application" / "features" / "certificates"
    return sorted(path for path in root.rglob("*.py") if path.is_file())


def _all_imports(path: Path) -> set[str]:
    module_name = "mfm.application.features.certificates"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imported: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0:
                imported.add(node.module or "")
            else:
                imported.add(module_name)

    return imported


def test_create_feature_vessel_target_and_public_safe_response(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    assert isinstance(create, CreateCertificateFeature)

    response = create.execute(_create_request())

    assert response.certificate.target.target_type == "VESSEL"
    assert response.certificate.issuer.issuer_name_snapshot == "Maritime Authority A"
    assert response.certificate.compliance_observations[0].requires_maintenance_work is True
    assert isinstance(response.certificate.id, UUID)
    assert isinstance(response.certificate.status, str)
    assert is_dataclass(response)


def test_create_feature_organization_target_supported(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    assert isinstance(create, CreateCertificateFeature)

    response = create.execute(_create_request(target_type="ORGANIZATION"))

    assert response.certificate.target.target_type == "ORGANIZATION"


def test_create_feature_invalid_target_type_maps_validation(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    assert isinstance(create, CreateCertificateFeature)

    with pytest.raises(ValidationException):
        create.execute(_create_request(target_type="INVALID"))


def test_create_feature_invalid_certificate_type_and_issuer_mapping(
    feature_stack: dict[str, object],
) -> None:
    create = feature_stack["create"]
    assert isinstance(create, CreateCertificateFeature)

    with pytest.raises(ValidationException):
        create.execute(
            CreateCertificateRequest(
                certificate_type_id=UUID("00000000-0000-0000-0000-00000000F101"),
                certificate_type_code="",
                target_type="VESSEL",
                target_id=uuid4(),
                certificate_number="CERT-X",
                issuer_type="AUTHORITY",
                issuer_id_or_external_key="AUTH-001",
                issuer_name_snapshot="Authority",
                issued_date=date(2027, 1, 1),
                valid_from=date(2027, 1, 1),
            )
        )

    with pytest.raises(ValidationException):
        create.execute(
            CreateCertificateRequest(
                certificate_type_id=UUID("00000000-0000-0000-0000-00000000F101"),
                certificate_type_code="STATUTORY_CERT",
                target_type="VESSEL",
                target_id=uuid4(),
                certificate_number="CERT-X",
                issuer_type="INVALID",
                issuer_id_or_external_key="AUTH-001",
                issuer_name_snapshot="Authority",
                issued_date=date(2027, 1, 1),
                valid_from=date(2027, 1, 1),
            )
        )


def test_create_feature_invalid_validity_chronology_maps_business_rule(
    feature_stack: dict[str, object],
) -> None:
    create = feature_stack["create"]
    assert isinstance(create, CreateCertificateFeature)

    with pytest.raises(ValidationException):
        create.execute(
            _create_request(
                issued_date=date(2028, 1, 2),
                valid_from=date(2028, 1, 1),
                expires_at=date(2029, 1, 1),
            )
        )


def test_create_feature_application_delegation_and_response_mapping() -> None:
    service_response = ServiceCreateCertificateResponse(
        certificate=CreateCertificateUseCase(unit_of_work=FakeCertificateUnitOfWork()).execute(
            _create_request()
        ).certificate
    )
    stub = StubService(response=service_response)
    feature = CreateCertificateFeature(service=stub)

    response = feature.execute(_create_request(certificate_number="CERT-DELEGATE"))

    assert response.certificate.certificate_number == "CERT-A"
    assert stub.last_request.certificate_number == "CERT-DELEGATE"


def test_create_feature_exception_mapping_standard() -> None:
    feature = CreateCertificateFeature(
        service=StubService(error=ServiceValidationException("invalid"))
    )
    with pytest.raises(ValidationException):
        feature.execute(_create_request())

    feature = CreateCertificateFeature(
        service=StubService(error=ServiceBusinessRuleViolation("invalid state"))
    )
    with pytest.raises(BusinessRuleViolation):
        feature.execute(_create_request())

    feature = CreateCertificateFeature(
        service=StubService(error=ServiceRepositoryException("repo"))
    )
    with pytest.raises(RepositoryException):
        feature.execute(_create_request())

    feature = CreateCertificateFeature(service=StubService(error=RuntimeError("boom")))
    with pytest.raises(RepositoryException):
        feature.execute(_create_request())


def test_activate_feature_paths(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    activate = feature_stack["activate"]
    assert isinstance(create, CreateCertificateFeature)
    assert isinstance(activate, ActivateCertificateFeature)

    created = create.execute(_create_request(certificate_number="CERT-ACT"))
    activated = activate.execute(
        ActivateCertificateRequest(certificate_id=created.certificate.id)
    )
    assert activated.certificate.status == "ACTIVE"

    with pytest.raises(BusinessRuleViolation):
        activate.execute(ActivateCertificateRequest(certificate_id=uuid4()))

    with pytest.raises(BusinessRuleViolation):
        activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))


def test_evaluate_feature_explicit_reference_date_and_statuses(
    feature_stack: dict[str, object],
) -> None:
    create = feature_stack["create"]
    activate = feature_stack["activate"]
    evaluate = feature_stack["evaluate"]
    assert isinstance(create, CreateCertificateFeature)
    assert isinstance(activate, ActivateCertificateFeature)
    assert isinstance(evaluate, EvaluateCertificateStatusFeature)

    with pytest.raises(ValidationException):
        evaluate.execute(  # type: ignore[arg-type]
            EvaluateCertificateStatusRequest(
                certificate_id=uuid4(),
                as_of_date="2028-01-01",
            )
        )

    created = create.execute(_create_request(certificate_number="CERT-EVAL"))
    activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))

    valid = evaluate.execute(
        EvaluateCertificateStatusRequest(
            certificate_id=created.certificate.id,
            as_of_date=date(2027, 2, 1),
            expiring_threshold_days=30,
        )
    )
    assert valid.evaluated_status == "VALID"

    expiring = evaluate.execute(
        EvaluateCertificateStatusRequest(
            certificate_id=created.certificate.id,
            as_of_date=date(2027, 12, 15),
            expiring_threshold_days=30,
        )
    )
    assert expiring.evaluated_status == "EXPIRING"
    assert expiring.certificate.status == "ACTIVE"

    boundary = evaluate.execute(
        EvaluateCertificateStatusRequest(
            certificate_id=created.certificate.id,
            as_of_date=date(2027, 12, 2),
            expiring_threshold_days=30,
        )
    )
    assert boundary.evaluated_status == "EXPIRING"

    expired = evaluate.execute(
        EvaluateCertificateStatusRequest(
            certificate_id=created.certificate.id,
            as_of_date=date(2028, 1, 2),
            expiring_threshold_days=30,
        )
    )
    assert expired.evaluated_status == "EXPIRED"

    non_expiring = create.execute(
        _create_request(
            certificate_number="CERT-NONEXP",
            expires_at=None,
            notes="Non-expiring",
        )
    )
    activate.execute(ActivateCertificateRequest(certificate_id=non_expiring.certificate.id))
    non_expiring_result = evaluate.execute(
        EvaluateCertificateStatusRequest(
            certificate_id=non_expiring.certificate.id,
            as_of_date=date(2035, 1, 1),
            expiring_threshold_days=30,
        )
    )
    assert non_expiring_result.evaluated_status == "VALID"


def test_suspend_feature_paths(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    activate = feature_stack["activate"]
    suspend = feature_stack["suspend"]
    assert isinstance(create, CreateCertificateFeature)
    assert isinstance(activate, ActivateCertificateFeature)
    assert isinstance(suspend, SuspendCertificateFeature)

    created = create.execute(_create_request(certificate_number="CERT-SUSP"))

    with pytest.raises(BusinessRuleViolation):
        suspend.execute(SuspendCertificateRequest(certificate_id=created.certificate.id))

    activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))
    suspended = suspend.execute(
        SuspendCertificateRequest(
            certificate_id=created.certificate.id,
            notes="Pending review",
        )
    )
    assert suspended.certificate.status == "SUSPENDED"

    with pytest.raises(BusinessRuleViolation):
        suspend.execute(SuspendCertificateRequest(certificate_id=uuid4()))


def test_revoke_feature_paths(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    activate = feature_stack["activate"]
    revoke = feature_stack["revoke"]
    assert isinstance(create, CreateCertificateFeature)
    assert isinstance(activate, ActivateCertificateFeature)
    assert isinstance(revoke, RevokeCertificateFeature)

    created = create.execute(_create_request(certificate_number="CERT-REV"))
    activate.execute(ActivateCertificateRequest(certificate_id=created.certificate.id))

    revoked = revoke.execute(
        RevokeCertificateRequest(
            certificate_id=created.certificate.id,
            notes="Revoked after review",
        )
    )
    assert revoked.certificate.status == "REVOKED"

    with pytest.raises(BusinessRuleViolation):
        revoke.execute(RevokeCertificateRequest(certificate_id=uuid4()))

    with pytest.raises(BusinessRuleViolation):
        revoke.execute(RevokeCertificateRequest(certificate_id=created.certificate.id))


def test_renew_and_history_preserve_historical_truth(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    activate = feature_stack["activate"]
    renew = feature_stack["renew"]
    history = feature_stack["history"]
    assert isinstance(create, CreateCertificateFeature)
    assert isinstance(activate, ActivateCertificateFeature)
    assert isinstance(renew, RenewCertificateFeature)
    assert isinstance(history, GetCertificateHistoryFeature)

    cert_a = create.execute(
        _create_request(
            certificate_number="CERT-A",
            issuer_name_snapshot="Maritime Authority A",
            notes="Context A",
        )
    )
    activate.execute(ActivateCertificateRequest(certificate_id=cert_a.certificate.id))

    renewed = renew.execute(
        RenewCertificateRequest(
            source_certificate_id=cert_a.certificate.id,
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

    chain = history.execute(
        GetCertificateHistoryRequest(certificate_id=cert_a.certificate.id)
    )

    assert len(chain.certificates) == 2
    first = chain.certificates[0]
    second = chain.certificates[1]

    assert first.certificate_number == "CERT-A"
    assert first.issuer.issuer_name_snapshot == "Maritime Authority A"
    assert first.notes == "Context A"

    assert second.certificate_number == "CERT-B"
    assert second.issuer.issuer_name_snapshot == "Maritime Authority B"
    assert second.notes == "Context B"
    assert second.renewed_from_certificate_id == first.id
    assert renewed.renewed_certificate.id == second.id


def test_history_chain_order_and_not_reconstructed(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    activate = feature_stack["activate"]
    renew = feature_stack["renew"]
    history = feature_stack["history"]
    assert isinstance(create, CreateCertificateFeature)
    assert isinstance(activate, ActivateCertificateFeature)
    assert isinstance(renew, RenewCertificateFeature)
    assert isinstance(history, GetCertificateHistoryFeature)

    cert_a = create.execute(_create_request(certificate_number="CERT-HA"))
    activate.execute(ActivateCertificateRequest(certificate_id=cert_a.certificate.id))

    cert_b = renew.execute(
        RenewCertificateRequest(
            source_certificate_id=cert_a.certificate.id,
            certificate_number="CERT-HB",
            issuer_type="CLASSIFICATION_SOCIETY",
            issuer_id_or_external_key="CLASS-HB",
            issuer_name_snapshot="Issuer B",
            issued_date=date(2028, 1, 2),
            valid_from=date(2028, 1, 2),
            expires_at=date(2029, 1, 1),
        )
    )
    activate.execute(ActivateCertificateRequest(certificate_id=cert_b.renewed_certificate.id))

    renew.execute(
        RenewCertificateRequest(
            source_certificate_id=cert_b.renewed_certificate.id,
            certificate_number="CERT-HC",
            issuer_type="INSPECTION_BODY",
            issuer_id_or_external_key="INSP-HC",
            issuer_name_snapshot="Issuer C",
            issued_date=date(2029, 1, 2),
            valid_from=date(2029, 1, 2),
            expires_at=date(2030, 1, 1),
        )
    )

    chain = history.execute(GetCertificateHistoryRequest(certificate_id=cert_a.certificate.id))
    assert [item.certificate_number for item in chain.certificates] == [
        "CERT-HA",
        "CERT-HB",
        "CERT-HC",
    ]


def test_get_expiring_feature_semantics_and_boundaries(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    activate = feature_stack["activate"]
    expiring = feature_stack["expiring"]
    assert isinstance(create, CreateCertificateFeature)
    assert isinstance(activate, ActivateCertificateFeature)
    assert isinstance(expiring, GetExpiringCertificatesFeature)

    exp_cert = create.execute(
        _create_request(certificate_number="CERT-EXP", expires_at=date(2028, 1, 20))
    )
    activate.execute(ActivateCertificateRequest(certificate_id=exp_cert.certificate.id))

    non_exp = create.execute(
        _create_request(certificate_number="CERT-NONEXP", expires_at=None)
    )
    activate.execute(ActivateCertificateRequest(certificate_id=non_exp.certificate.id))

    old = create.execute(
        _create_request(certificate_number="CERT-OLD", expires_at=date(2028, 1, 5))
    )
    activate.execute(ActivateCertificateRequest(certificate_id=old.certificate.id))

    response = expiring.execute(
        GetExpiringCertificatesRequest(as_of_date=date(2028, 1, 1), within_days=30)
    )
    numbers = {item.certificate_number for item in response.certificates}

    assert "CERT-EXP" in numbers
    assert "CERT-NONEXP" not in numbers
    assert "CERT-OLD" in numbers


def test_no_hidden_clock_in_certificate_feature_layer() -> None:
    for path in _cert_files():
        content = path.read_text(encoding="utf-8")
        assert "date.today(" not in content
        assert "datetime.now(" not in content


def test_inspection_maintenance_boundary_and_finding_visibility(
    feature_stack: dict[str, object],
) -> None:
    create = feature_stack["create"]
    assert isinstance(create, CreateCertificateFeature)

    response = create.execute(_create_request(certificate_number="CERT-MAINT"))
    assert response.certificate.compliance_observations[0].requires_maintenance_work is True

    forbidden_prefixes = (
        "mfm.application.features.maintenance",
        "mfm.application.maintenance",
        "mfm.domain.maintenance",
    )
    for path in _cert_files():
        imports = _all_imports(path)
        assert not any(
            item.startswith(prefix) or item == prefix
            for item in imports
            for prefix in forbidden_prefixes
        )


def test_fleet_organization_and_persistence_boundaries_in_imports() -> None:
    forbidden_prefixes = (
        "mfm.application.features.fleet",
        "mfm.application.fleet",
        "mfm.domain.fleet",
        "mfm.application.features.organization",
        "mfm.application.organization",
        "mfm.domain.organization",
        "mfm.database",
        "sqlalchemy",
    )
    for path in _cert_files():
        imports = _all_imports(path)
        assert not any(
            item.startswith(prefix) or item == prefix
            for item in imports
            for prefix in forbidden_prefixes
        )


def test_feature_public_response_has_no_domain_leakage(feature_stack: dict[str, object]) -> None:
    create = feature_stack["create"]
    assert isinstance(create, CreateCertificateFeature)

    response = create.execute(_create_request(certificate_number="CERT-SAFE"))

    certificate = response.certificate
    assert isinstance(certificate.id, UUID)
    assert isinstance(certificate.certificate_type.code, str)
    assert isinstance(certificate.target.target_type, str)
    assert isinstance(certificate.target.target_id, UUID)
    assert isinstance(certificate.issuer.issuer_id_or_external_key, str)
    assert isinstance(certificate.issuer.issuer_name_snapshot, str)
    assert isinstance(certificate.status, str)
    assert certificate.renewed_from_certificate_id is None
