"""Create ContingentPlan use case."""

from __future__ import annotations

from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.repositories.contingent_plan_repository import ContingentPlanRepository


class CreateContingentPlanUseCase:
    """Create a contingent plan when business rules are satisfied."""

    def __init__(self, repository: ContingentPlanRepository) -> None:
        self._repository = repository

    def execute(self, plan: ContingentPlan) -> ContingentPlan:
        if not isinstance(plan, ContingentPlan):
            raise TypeError("plan must be a ContingentPlan")

        existing_plans = self._repository.list_by_membership_type(plan.membership_type_id)
        plans_with_new = [*existing_plans, plan]

        ContingentPlan.ensure_no_overlaps(plans_with_new, plan.membership_type_id)
        ContingentPlan.ensure_single_active(plans_with_new, plan.membership_type_id)

        self._repository.add(plan)
        return plan
