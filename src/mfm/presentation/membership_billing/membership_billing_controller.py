"""Controller for the Membership Billing workspace."""

from __future__ import annotations

from typing import Protocol

from mfm.application.features.membership_billing.list_fee_schedules_feature import (
    ListFeeSchedulesRequest,
)
from mfm.application.features.membership_billing.manage_membership_billing_feature import (
    ManageMembershipBillingRequest,
)
from mfm.application.features.membership_type import ListMembershipTypesRequest
from mfm.presentation.membership_billing.membership_billing_viewmodels import (
    FeeScheduleListItemViewModel,
    FeeScheduleListViewModel,
    RunBillingCommandViewModel,
    RunBillingResultViewModel,
    SetupFeeScheduleCommandViewModel,
)


class ManageMembershipBillingPort(Protocol):
    def execute(self, request: ManageMembershipBillingRequest): ...


class ListFeeSchedulesPort(Protocol):
    def execute(self, request: ListFeeSchedulesRequest): ...


class ListMembershipTypesPort(Protocol):
    def execute(self, request: ListMembershipTypesRequest): ...


class MembershipBillingController:
    """UI controller that orchestrates membership billing features."""

    def __init__(
        self,
        *,
        manage_membership_billing_feature: ManageMembershipBillingPort,
        list_fee_schedules_feature: ListFeeSchedulesPort,
        list_membership_types_feature: ListMembershipTypesPort,
    ) -> None:
        self._manage_billing = manage_membership_billing_feature
        self._list_fee_schedules = list_fee_schedules_feature
        self._list_membership_types = list_membership_types_feature

    def load_membership_type_options(self):
        response = self._list_membership_types.execute(
            ListMembershipTypesRequest(active_only=True)
        )
        return response.membership_types

    def load_fee_schedule_list(self) -> FeeScheduleListViewModel:
        response = self._list_fee_schedules.execute(ListFeeSchedulesRequest())
        items = tuple(
            FeeScheduleListItemViewModel(
                membership_type_id=fs.membership_type_id,
                membership_type_code=fs.membership_type_code,
                membership_type_name=fs.membership_type_name,
                fee_amount=fs.fee_amount,
                currency=fs.currency,
                due_days=fs.due_days,
                reminder_count=fs.reminder_count,
            )
            for fs in response.fee_schedules
        )
        return FeeScheduleListViewModel(items=items)

    def setup_fee_schedule(self, command: SetupFeeScheduleCommandViewModel) -> FeeScheduleListItemViewModel:
        response = self._manage_billing.execute(
            ManageMembershipBillingRequest(
                operation="setup-fee",
                membership_type_id=command.membership_type_id,
                membership_type_code=command.membership_type_code,
                membership_type_name=command.membership_type_name,
                amount=command.amount,
                currency=command.currency,
                due_days=command.due_days,
            )
        )
        result = response.result
        return FeeScheduleListItemViewModel(
            membership_type_id=result.membership_type_id,
            membership_type_code=command.membership_type_code,
            membership_type_name=command.membership_type_name,
            fee_amount=result.fee_amount,
            currency=result.currency,
            due_days=result.due_days,
            reminder_count=result.reminder_count,
        )

    def run_billing(self, command: RunBillingCommandViewModel) -> RunBillingResultViewModel:
        response = self._manage_billing.execute(
            ManageMembershipBillingRequest(
                operation="run-billing",
                membership_type_id=command.membership_type_id,
                fiscal_year=command.fiscal_year,
                billing_date=command.billing_date,
                dry_run=command.dry_run,
            )
        )
        result = response.result
        return RunBillingResultViewModel(
            processed=result.run_processed,
            invoices_created=result.run_invoices_created,
            reminder_count=result.reminder_count,
        )
