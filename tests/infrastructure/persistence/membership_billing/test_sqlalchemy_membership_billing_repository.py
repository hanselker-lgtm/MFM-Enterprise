"""Tests for the real, database-backed membership billing repository.

Replaces the previous ``SQLiteMembershipBillingRepository``, which
despite its name stored data in a plain process-lifetime dict --
these tests specifically prove persistence survives across separate
sessions, which the old implementation would fail.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mfm.database.base import Base
import mfm.database.metadata  # noqa: F401  (registers ORM models on Base.metadata)
from mfm.domain.membership_billing.fee_schedule import FeeSchedule
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingProfile
from mfm.domain.membership_billing.membership_billing_profile import MembershipBillingRun
from mfm.domain.membership_billing.membership_fee import MembershipFee
from mfm.domain.membership_billing.reminder import Reminder
from mfm.infrastructure.persistence.membership_billing.sqlalchemy_membership_billing_repository import (
    SqlAlchemyMembershipBillingRepository,
)


def _session_factory():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine, expire_on_commit=False)


def _profile(membership_type_id) -> MembershipBillingProfile:
    return MembershipBillingProfile(
        membership_type_id=membership_type_id,
        fee_schedule=FeeSchedule(
            membership_fee=MembershipFee(
                membership_type_id=membership_type_id,
                membership_type_code="STD",
                membership_type_name="Standard",
                amount=Decimal("250.00"),
                currency="DKK",
            ),
            due_days=30,
        ),
    )


def test_save_and_get_round_trips_fee_schedule() -> None:
    session_factory = _session_factory()
    membership_type_id = uuid4()

    session = session_factory()
    SqlAlchemyMembershipBillingRepository(session).save(_profile(membership_type_id))
    session.commit()
    session.close()

    session2 = session_factory()
    fetched = SqlAlchemyMembershipBillingRepository(session2).get(membership_type_id)

    assert fetched is not None
    assert fetched.fee_schedule.membership_fee.amount == Decimal("250.00")
    assert fetched.fee_schedule.due_days == 30


def test_get_returns_none_for_unknown_membership_type() -> None:
    session = _session_factory()()
    result = SqlAlchemyMembershipBillingRepository(session).get(uuid4())
    assert result is None


def test_list_returns_all_saved_profiles() -> None:
    session_factory = _session_factory()
    session = session_factory()
    repo = SqlAlchemyMembershipBillingRepository(session)
    repo.save(_profile(uuid4()))
    repo.save(_profile(uuid4()))
    session.commit()

    assert len(repo.list()) == 2


def test_save_persists_reminders_and_runs_across_sessions() -> None:
    session_factory = _session_factory()
    membership_type_id = uuid4()
    profile = _profile(membership_type_id)
    profile.add_reminder(
        Reminder(member_id=uuid4(), message="Please pay", due_date=date.today())
    )
    profile.add_run(
        MembershipBillingRun(
            fiscal_year=2026,
            billing_date=date.today(),
            processed=5,
            invoices_created=5,
            journals_created=5,
            skipped=0,
        )
    )

    session = session_factory()
    SqlAlchemyMembershipBillingRepository(session).save(profile)
    session.commit()
    session.close()

    session2 = session_factory()
    fetched = SqlAlchemyMembershipBillingRepository(session2).get(membership_type_id)

    assert len(fetched.reminders) == 1
    assert len(fetched.runs) == 1
    assert fetched.runs[0].processed == 5


def test_save_twice_updates_existing_profile_instead_of_duplicating() -> None:
    session_factory = _session_factory()
    membership_type_id = uuid4()

    session = session_factory()
    repo = SqlAlchemyMembershipBillingRepository(session)
    repo.save(_profile(membership_type_id))
    session.commit()

    updated = _profile(membership_type_id)
    updated.fee_schedule.membership_fee.amount = Decimal("300.00")
    repo.save(updated)
    session.commit()

    assert len(repo.list()) == 1
    assert repo.get(membership_type_id).fee_schedule.membership_fee.amount == Decimal("300.00")
