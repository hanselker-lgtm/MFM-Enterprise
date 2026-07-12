import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mfm.database.models.base_model import BaseModel
from mfm.database.repositories.sqlite_membership_type_repository import (
    SQLiteMembershipTypeRepository,
)
from mfm.domain.membership.membership_type import MembershipType


def _create_session():
    engine = create_engine("sqlite:///:memory:")
    BaseModel.metadata.create_all(engine)
    return engine, Session(engine)


def test_membership_type_repository_persists_and_reads_membership_type():
    engine, session = _create_session()
    try:
        repository = SQLiteMembershipTypeRepository(session)

        membership_type = MembershipType(
            code="STANDARD",
            name="Standard",
            description="Default type",
        )

        repository.add(membership_type)
        session.commit()

        stored = repository.get(membership_type.id)
        assert stored is not None
        assert stored.code == "STANDARD"

        by_code = repository.get_by_code("standard")
        assert by_code is not None
        assert by_code.id == membership_type.id
    finally:
        session.close()
        engine.dispose()


def test_membership_type_repository_supports_list_exists_delete():
    engine, session = _create_session()
    try:
        repository = SQLiteMembershipTypeRepository(session)

        membership_type = MembershipType(code="YOUTH", name="Youth")
        repository.add(membership_type)
        session.commit()

        assert repository.exists(membership_type.id) is True
        assert len(repository.list()) == 1

        repository.delete(membership_type.id)
        session.commit()

        assert repository.exists(membership_type.id) is False
        assert repository.get(membership_type.id) is None
    finally:
        session.close()
        engine.dispose()


def test_membership_type_repository_rejects_duplicate_code():
    engine, session = _create_session()
    try:
        repository = SQLiteMembershipTypeRepository(session)

        first = MembershipType(code="VIP", name="VIP")
        second = MembershipType(code="VIP", name="Another VIP")

        repository.add(first)
        session.commit()

        with pytest.raises(ValueError):
            repository.add(second)
    finally:
        session.close()
        engine.dispose()


def test_membership_type_repository_updates_fields_and_validates_unique_code():
    engine, session = _create_session()
    try:
        repository = SQLiteMembershipTypeRepository(session)

        premium = MembershipType(code="PREMIUM", name="Premium")
        basic = MembershipType(code="BASIC", name="Basic")
        repository.add(premium)
        repository.add(basic)
        session.commit()

        premium.rename(name="Premium Plus", description="Priority support")
        premium.deactivate()
        repository.update(premium)
        session.commit()

        stored = repository.get(premium.id)
        assert stored is not None
        assert stored.name == "Premium Plus"
        assert stored.description == "Priority support"
        assert stored.is_active is False

        premium.code = "BASIC"
        with pytest.raises(ValueError):
            repository.update(premium)
    finally:
        session.close()
        engine.dispose()
