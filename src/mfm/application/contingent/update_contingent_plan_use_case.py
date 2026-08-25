"""Update ContingentPlan use case."""

from __future__ import annotations

from mfm.domain.contingent.contingent_plan import ContingentPlan
from mfm.domain.contingent.exceptions import ContingentPlanNotFoundError
from mfm.repositories.contingent_plan_repository import ContingentPlanRepository


class UpdateContingentPlanUseCase:
    """Update contingent plan and validate business rules."""

    def __init__(self, repository: ContingentPlanRepository) -> None:
        self._repository = repository

    def execute(self, plan: ContingentPlan) -> ContingentPlan:
        if not isinstance(plan, ContingentPlan):
            raise TypeError("plan must be a ContingentPlan")

        existing = self._repository.get(plan.id)
        if existing is None:
            raise ContingentPlanNotFoundError(
                f"Contingent plan {plan.id} was not found"
            )

        same_membership_type = self._repository.list_by_membership_type(plan.membership_type_id)
        plans_without_current = [item for item in same_membership_type if item.id != plan.id]
        plans_after_update = [*plans_without_current, plan]

        ContingentPlan.ensure_no_overlaps(plans_after_update, plan.membership_type_id)
        ContingentPlan.ensure_single_active(plans_after_update, plan.membership_type_id)

        self._repository.update(plan)
        return plan
