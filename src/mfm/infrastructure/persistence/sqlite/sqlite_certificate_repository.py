"""SQLite repository for Certificate aggregates."""

from __future__ import annotations

from collections import defaultdict
from datetime import date
from datetime import timedelta
from typing import cast
from uuid import UUID

from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from mfm.database.mappers.certificate_mapper import CertificateMapper
from mfm.database.models.certificate_model import CertificateModel
from mfm.domain.certificates.certificate import Certificate
from mfm.domain.certificates.certificate_status import CertificateStatus
from mfm.domain.certificates.certificate_target import CertificateTarget
from mfm.repositories.certificate_repository import CertificateRepository
from mfm.repositories.unit_of_work import UnitOfWork


class SQLiteCertificateRepository(CertificateRepository):
    """SQLAlchemy-backed repository for Certificate aggregates."""

    def __init__(self, unit_of_work: UnitOfWork):
        self._uow = unit_of_work
        self._session = cast(Session, unit_of_work.session)

    def add(self, certificate: Certificate) -> None:
        self._session.add(CertificateMapper.to_orm_certificate(certificate))
        self._session.flush()

    def get_by_id(self, certificate_id: UUID) -> Certificate | None:
        orm = self._session.scalar(
            select(CertificateModel)
            .options(selectinload(CertificateModel.compliance_observations))
            .where(CertificateModel.id == certificate_id)
        )
        if orm is None:
            return None
        return CertificateMapper.to_domain_certificate(orm)

    def update(self, certificate: Certificate) -> None:
        existing = self._session.scalar(
            select(CertificateModel)
            .options(selectinload(CertificateModel.compliance_observations))
            .where(CertificateModel.id == certificate.id.value)
        )
        if existing is None:
            raise ValueError(f"Certificate {certificate.id.value} does not exist")

        self._session.merge(CertificateMapper.to_orm_certificate(certificate))
        self._session.flush()

    def exists(self, certificate_id: UUID) -> bool:
        return self._session.get(CertificateModel, certificate_id) is not None

    def list(self) -> list[Certificate]:
        orm_entities = self._session.scalars(
            select(CertificateModel)
            .options(selectinload(CertificateModel.compliance_observations))
            .order_by(CertificateModel.issued_date, CertificateModel.created_at)
        ).unique().all()
        return [CertificateMapper.to_domain_certificate(orm) for orm in orm_entities]

    def get_by_target(self, target: CertificateTarget) -> list[Certificate]:
        orm_entities = self._session.scalars(
            select(CertificateModel)
            .options(selectinload(CertificateModel.compliance_observations))
            .where(
                CertificateModel.target_type == target.target_type,
                CertificateModel.target_id == target.target_id,
            )
            .order_by(CertificateModel.issued_date, CertificateModel.created_at)
        ).unique().all()
        return [CertificateMapper.to_domain_certificate(orm) for orm in orm_entities]

    def get_active_by_target(self, target: CertificateTarget) -> list[Certificate]:
        orm_entities = self._session.scalars(
            select(CertificateModel)
            .options(selectinload(CertificateModel.compliance_observations))
            .where(
                CertificateModel.target_type == target.target_type,
                CertificateModel.target_id == target.target_id,
                CertificateModel.status == CertificateStatus.ACTIVE,
            )
            .order_by(CertificateModel.issued_date, CertificateModel.created_at)
        ).unique().all()
        return [CertificateMapper.to_domain_certificate(orm) for orm in orm_entities]

    def get_expiring(
        self,
        *,
        as_of_date: date,
        within_days: int,
    ) -> list[Certificate]:
        if not isinstance(as_of_date, date):
            raise TypeError("as_of_date must be date")
        if not isinstance(within_days, int) or within_days < 0:
            raise ValueError("within_days must be non-negative int")

        threshold_date = as_of_date + timedelta(days=within_days)

        orm_entities = self._session.scalars(
            select(CertificateModel)
            .options(selectinload(CertificateModel.compliance_observations))
            .where(
                CertificateModel.status == CertificateStatus.ACTIVE,
                CertificateModel.expires_at.is_not(None),
                CertificateModel.expires_at >= as_of_date,
                CertificateModel.expires_at <= threshold_date,
            )
            .order_by(CertificateModel.expires_at, CertificateModel.issued_date)
        ).unique().all()
        return [CertificateMapper.to_domain_certificate(orm) for orm in orm_entities]

    def get_expired(self, *, as_of_date: date) -> list[Certificate]:
        if not isinstance(as_of_date, date):
            raise TypeError("as_of_date must be date")

        orm_entities = self._session.scalars(
            select(CertificateModel)
            .options(selectinload(CertificateModel.compliance_observations))
            .where(
                or_(
                    CertificateModel.status == CertificateStatus.EXPIRED,
                    and_(
                        CertificateModel.status == CertificateStatus.ACTIVE,
                        CertificateModel.expires_at.is_not(None),
                        CertificateModel.expires_at < as_of_date,
                    ),
                )
            )
            .order_by(CertificateModel.expires_at, CertificateModel.issued_date)
        ).unique().all()
        return [CertificateMapper.to_domain_certificate(orm) for orm in orm_entities]

    def get_renewal_history(self, certificate_id: UUID) -> list[Certificate]:
        orm_entities = self._session.scalars(
            select(CertificateModel).options(
                selectinload(CertificateModel.compliance_observations)
            )
        ).unique().all()
        by_id = {orm.id: orm for orm in orm_entities}

        start = by_id.get(certificate_id)
        if start is None:
            return []

        root = start
        while root.renewed_from_certificate_id is not None:
            parent = by_id.get(root.renewed_from_certificate_id)
            if parent is None:
                break
            root = parent

        children_by_parent: dict[UUID, list[CertificateModel]] = defaultdict(list)
        for orm in orm_entities:
            if orm.renewed_from_certificate_id is not None:
                children_by_parent[orm.renewed_from_certificate_id].append(orm)

        for children in children_by_parent.values():
            children.sort(key=lambda item: (item.issued_date, item.created_at))

        ordered_ids: list[UUID] = []
        queue: list[CertificateModel] = [root]
        while queue:
            current = queue.pop(0)
            ordered_ids.append(current.id)
            queue.extend(children_by_parent.get(current.id, []))

        ordered = [by_id[item_id] for item_id in ordered_ids]
        return [CertificateMapper.to_domain_certificate(orm) for orm in ordered]
