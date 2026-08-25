"""Mapper between MembershipBillingProfile domain objects and ORM models."""

from __future__ import annotations

from mfm.database.models.membership_billing_model import MembershipBillingReminderModel
from mfm.database.models.membership_billing_model import MembershipBillingRunModel
from mfm.database.models.membership_billing_model import MembershipFeeScheduleModel
from mfm.domain.membership_billing.fee_schedule import FeeSchedule
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingRun
from mfm.domain.membership_billing.membership_fee import MembershipFee
from mfm.domain.membership_billing.reminder import Reminder
from mfm.domain.membership_billing.reminder import ReminderStatus


class MembershipBillingMapper:
    """Translates between the MembershipBillingProfile aggregate and its ORM rows."""

    @staticmethod
    def to_orm(profile: MembershipBillingProfile, *, existing: MembershipFeeScheduleModel | None = None) -> MembershipFeeScheduleModel:
        fee = profile.fee_schedule.membership_fee
        model = existing or MembershipFeeScheduleModel(id=profile.fee_schedule.id)

        model.membership_type_id = profile.membership_type_id
        model.membership_type_code = fee.membership_type_code
        model.membership_type_name = fee.membership_type_name
        model.amount = fee.amount
        model.currency = fee.currency
        model.due_days = profile.fee_schedule.due_days
        model.billing_period = profile.fee_schedule.billing_period
        model.active = profile.fee_schedule.active

        existing_reminder_ids = {r.id for r in model.reminders}
        new_reminder_ids = {r.id for r in profile.reminders}
        model.reminders = [
            reminder for reminder in model.reminders if reminder.id in new_reminder_ids
        ]
        for reminder in profile.reminders:
            if reminder.id not in existing_reminder_ids:
                model.reminders.append(
                    MembershipBillingReminderModel(
                        id=reminder.id,
                        member_id=reminder.member_id,
                        invoice_id=reminder.invoice_id,
                        message=reminder.message,
                        due_date=reminder.due_date,
                        status=reminder.status.value,
                        sent_at=reminder.sent_at,
                    )
                )
            else:
                for orm_reminder in model.reminders:
                    if orm_reminder.id == reminder.id:
                        orm_reminder.status = reminder.status.value
                        orm_reminder.sent_at = reminder.sent_at

        existing_run_ids = {id(run) for run in model.runs}
        _ = existing_run_ids  # runs are append-only; no in-place updates needed
        recorded_runs = len(model.runs)
        for run in profile.runs[recorded_runs:]:
            model.runs.append(
                MembershipBillingRunModel(
                    fiscal_year=run.fiscal_year,
                    billing_date=run.billing_date,
                    processed=run.processed,
                    invoices_created=run.invoices_created,
                    journals_created=run.journals_created,
                    skipped=run.skipped,
                    errors="; ".join(run.errors) if run.errors else None,
                )
            )

        return model

    @staticmethod
    def to_domain(model: MembershipFeeScheduleModel) -> MembershipBillingProfile:
        fee = MembershipFee(
            membership_type_id=model.membership_type_id,
            membership_type_code=model.membership_type_code,
            membership_type_name=model.membership_type_name,
            amount=model.amount,
            currency=model.currency,
        )
        schedule = FeeSchedule(
            membership_fee=fee,
            due_days=model.due_days,
            billing_period=model.billing_period,
            active=model.active,
            id=model.id,
        )
        reminders = [
            Reminder(
                id=r.id,
                member_id=r.member_id,
                invoice_id=r.invoice_id,
                message=r.message,
                due_date=r.due_date,
                status=ReminderStatus(r.status),
                sent_at=r.sent_at,
            )
            for r in model.reminders
        ]
        runs = [
            MembershipBillingRun(
                fiscal_year=r.fiscal_year,
                billing_date=r.billing_date,
                processed=r.processed,
                invoices_created=r.invoices_created,
                journals_created=r.journals_created,
                skipped=r.skipped,
                errors=tuple(r.errors.split("; ")) if r.errors else (),
            )
            for r in model.runs
        ]

        return MembershipBillingProfile(
            membership_type_id=model.membership_type_id,
            fee_schedule=schedule,
            reminders=reminders,
            runs=runs,
        )
