"""Mapper between certificates domain and persistence models."""

from __future__ import annotations

from mfm.database.models.certificate_compliance_observation_model import (
    CertificateComplianceObservationModel,
)
from mfm.database.models.certificate_model import CertificateModel
from mfm.domain.certificates.certificate import Certificate
from mfm.domain.certificates.certificate_target import CertificateTarget
from mfm.domain.certificates.certificate_type_reference import CertificateTypeReference
from mfm.domain.certificates.compliance_observation import ComplianceObservation
from mfm.domain.certificates.identifiers import CertificateId
from mfm.domain.certificates.identifiers import CertificateTypeId
from mfm.domain.certificates.issuer_reference import IssuerReference


class CertificateMapper:
    """Map certificate aggregate to/from SQLAlchemy models."""

    @staticmethod
    def to_orm_certificate(certificate: Certificate) -> CertificateModel:
        orm = CertificateModel(
            id=certificate.id.value,
            certificate_type_id=certificate.certificate_type.certificate_type_id.value,
            certificate_type_code=certificate.certificate_type.code,
            certificate_type_display_name_snapshot=(
                certificate.certificate_type.display_name_snapshot
            ),
            certificate_number=certificate.certificate_number,
            target_type=certificate.target.target_type,
            target_id=certificate.target.target_id,
            issuer_type=certificate.issuer.issuer_type,
            issuer_id_or_external_key=certificate.issuer.issuer_id_or_external_key,
            issuer_name_snapshot=certificate.issuer.issuer_name_snapshot,
            issued_date=certificate.issued_date,
            valid_from=certificate.valid_from,
            expires_at=certificate.expires_at,
            status=certificate.status,
            renewal_required=certificate.renewal_required,
            renewed_from_certificate_id=(
                certificate.renewed_from_certificate_id.value
                if certificate.renewed_from_certificate_id is not None
                else None
            ),
            document_reference=certificate.document_reference,
            external_document_id=certificate.external_document_id,
            notes=certificate.notes,
        )

        for index, observation in enumerate(certificate.compliance_observations):
            orm.compliance_observations.append(
                CertificateComplianceObservationModel(
                    certificate_id=certificate.id.value,
                    observation_order=index,
                    summary=observation.summary,
                    observed_on=observation.observed_on,
                    requires_maintenance_work=observation.requires_maintenance_work,
                )
            )

        return orm

    @staticmethod
    def to_domain_certificate(orm: CertificateModel) -> Certificate:
        certificate = Certificate(
            id=CertificateId(orm.id),
            certificate_type=CertificateTypeReference(
                certificate_type_id=CertificateTypeId(orm.certificate_type_id),
                code=orm.certificate_type_code,
                display_name_snapshot=orm.certificate_type_display_name_snapshot,
            ),
            certificate_number=orm.certificate_number,
            target=CertificateTarget(
                target_type=orm.target_type,
                target_id=orm.target_id,
            ),
            issuer=IssuerReference(
                issuer_type=orm.issuer_type,
                issuer_id_or_external_key=orm.issuer_id_or_external_key,
                issuer_name_snapshot=orm.issuer_name_snapshot,
            ),
            issued_date=orm.issued_date,
            valid_from=orm.valid_from,
            expires_at=orm.expires_at,
            status=orm.status,
            renewal_required=orm.renewal_required,
            renewed_from_certificate_id=(
                CertificateId(orm.renewed_from_certificate_id)
                if orm.renewed_from_certificate_id is not None
                else None
            ),
            document_reference=orm.document_reference,
            external_document_id=orm.external_document_id,
            notes=orm.notes,
            compliance_observations=tuple(
                ComplianceObservation(
                    summary=observation.summary,
                    observed_on=observation.observed_on,
                    requires_maintenance_work=observation.requires_maintenance_work,
                )
                for observation in sorted(
                    orm.compliance_observations,
                    key=lambda item: item.observation_order,
                )
            ),
        )

        # Restored aggregates must not emit creation events on load.
        certificate.pull_events()
        return certificate
