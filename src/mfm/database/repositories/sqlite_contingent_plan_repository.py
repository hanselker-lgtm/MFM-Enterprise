"""SQLite repository for ContingentPlan aggregates."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from mfm.database.mappers.contingent_plan_mapper import ContingentPlanMapper
from mfm.database.models.contingent_plan_model import ContingentPlanModel
from mfm.database.models.membership_type_model import MembershipTypeModel
from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.membership.membership_type import MembershipType
from mfm.repositories.contingent_plan_repository import ContingentPlanRepository


class SQLiteContingentPlanRepository(ContingentPlanRepository):
    """SQLAlchemy-backed repository for ContingentPlan aggregates."""

    def __init__(self, session: Session):
        self._session = session

    def add(self, plan: ContingentPlan) -> None:
        orm = ContingentPlanMapper.to_orm(plan)
        self._session.add(orm)
        self._session.flush()

    def update(self, plan: ContingentPlan) -> None:
        orm = self._session.get(ContingentPlanModel, plan.id)
        if orm is None:
            raise ValueError(f"Contingent plan {plan.id} does not exist")

        orm.membership_type_id = plan.membership_type_id
        orm.amount = plan.price.amount
        orm.currency = plan.price.currency
        orm.billing_period = plan.invoice_rule.billing_period
        orm.due_days = plan.invoice_rule.due_days
        orm.prorate_on_start = plan.invoice_rule.prorate_on_start
        orm.valid_from = plan.valid_from
        orm.valid_to = plan.valid_to
        self._session.flush()

    def get(self, plan_id: UUID) -> ContingentPlan | None:
        statement = select(ContingentPlanModel).where(ContingentPlanModel.id == plan_id)
        orm = self._session.scalar(statement)
        if orm is None:
            return None

        membership_type = self._resolve_membership_type(orm.membership_type_id)
        return ContingentPlanMapper.to_domain(orm, membership_type)

    def list(self) -> list[ContingentPlan]:
        statement = select(ContingentPlanModel)
        orm_rows = self._session.scalars(statement).all()
        return [
            ContingentPlanMapper.to_domain(
                orm,
                self._resolve_membership_type(orm.membership_type_id),
            )
            for orm in orm_rows
        ]

    def list_by_membership_type(self, membership_type_id: UUID) -> list[ContingentPlan]:
        statement = select(ContingentPlanModel).where(
            ContingentPlanModel.membership_type_id == membership_type_id
        )
        orm_rows = self._session.scalars(statement).all()
        membership_type = self._resolve_membership_type(membership_type_id)
        return [ContingentPlanMapper.to_domain(orm, membership_type) for orm in orm_rows]

    def get_active_for_membership_type(self, membership_type_id, at_date) -> ContingentPlan | None:
        """Return the plan valid for this membership type on ``at_date``, if any.

        Used by :class:`mfm.application.features.annual_contingent_generation.
        AnnualContingentGenerationFeature` to look up pricing when generating
        invoices. Not part of the original :class:`ContingentPlanRepository`
        ABC, but required by that feature's narrower ``ContingentRepository``
        protocol -- both are satisfied by the same object.
        """

        statement = select(ContingentPlanModel).where(
            ContingentPlanModel.membership_type_id == membership_type_id,
            ContingentPlanModel.valid_from <= at_date,
        )
        candidates = self._session.scalars(statement).all()
        active = [
            orm for orm in candidates if orm.valid_to is None or orm.valid_to >= at_date
        ]
        if not active:
            return None

        # Prefer the most recently started plan if more than one overlaps.
        chosen = max(active, key=lambda orm: orm.valid_from)
        membership_type = self._resolve_membership_type(membership_type_id)
        return ContingentPlanMapper.to_domain(chosen, membership_type)

    def exists(self, plan_id: UUID) -> bool:
        return self._session.get(ContingentPlanModel, plan_id) is not None

    def delete(self, plan_id: UUID) -> None:
        orm = self._session.get(ContingentPlanModel, plan_id)
        if orm is None:
            return

        self._session.delete(orm)
        self._session.flush()

    def _resolve_membership_type(self, membership_type_id: UUID) -> MembershipType:
        orm = self._session.get(MembershipTypeModel, membership_type_id)
        if orm is None:
            raise ValueError(
                f"Membership type {membership_type_id} does not exist for contingent plan"
            )

        return MembershipType(
            id=orm.id,
            code=orm.code,
            name=orm.name,
            description=orm.description,
            is_active=orm.is_active,
        )
