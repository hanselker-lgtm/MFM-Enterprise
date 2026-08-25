"""Real, database-backed repository for membership billing profiles.

Replaces ``mfm.database.repositories.sqlite_membership_billing_repository.
SQLiteMembershipBillingRepository``, which was named as if it were a
SQLite adapter but was actually a plain in-process dict -- all fee
schedules, reminders, and billing history were lost on every restart.
"""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.membership_billing_mapper import MembershipBillingMapper
from mfm.database.models.membership_billing_model import MembershipFeeScheduleModel
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile
from mfm.repositories.membership_billing_repository import MembershipBillingRepository


class SqlAlchemyMembershipBillingRepository(MembershipBillingRepository):
    """SQLAlchemy-backed repository for membership billing profiles."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get(self, membership_type_id: UUID) -> MembershipBillingProfile | None:
        model = self._session.scalar(
            select(MembershipFeeScheduleModel).where(
                MembershipFeeScheduleModel.membership_type_id == membership_type_id
            )
        )
        if model is None:
            return None
        return MembershipBillingMapper.to_domain(model)

    def save(self, profile: MembershipBillingProfile) -> None:
        existing = self._session.scalar(
            select(MembershipFeeScheduleModel).where(
                MembershipFeeScheduleModel.membership_type_id == profile.membership_type_id
            )
        )
        model = MembershipBillingMapper.to_orm(profile, existing=existing)
        if existing is None:
            self._session.add(model)
        self._session.flush()

    def list(self) -> list[MembershipBillingProfile]:
        models = self._session.scalars(select(MembershipFeeScheduleModel)).all()
        return [MembershipBillingMapper.to_domain(model) for model in models]
