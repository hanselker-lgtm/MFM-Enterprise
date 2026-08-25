from __future__ import annotations

import pytest

from mfm.application.uow.sqlalchemy_unit_of_work import SQLAlchemyUnitOfWork


class FakeSession:
    def __init__(self) -> None:
        self.commits = 0
        self.rollbacks = 0
        self.flushes = 0
        self.closes = 0

    def commit(self) -> None:
        self.commits += 1

    def rollback(self) -> None:
        self.rollbacks += 1

    def flush(self) -> None:
        self.flushes += 1

    def close(self) -> None:
        self.closes += 1


def test_commit():
    session = FakeSession()
    uow = SQLAlchemyUnitOfWork(lambda: session)

    with uow:
        uow.commit()

    assert session.commits == 1


def test_commit_only_once():
    session = FakeSession()
    uow = SQLAlchemyUnitOfWork(lambda: session)

    with uow:
        uow.commit()
        with pytest.raises(RuntimeError):
            uow.commit()

    assert session.commits == 1


def test_rollback():
    session = FakeSession()
    uow = SQLAlchemyUnitOfWork(lambda: session)

    with uow:
        uow.rollback()

    assert session.rollbacks == 1


def test_nested_usage():
    session = FakeSession()
    uow = SQLAlchemyUnitOfWork(lambda: session)

    with uow as outer:
        with uow as inner:
            assert outer is inner
            assert session.closes == 0
            uow.flush()
        assert session.closes == 0

    assert session.closes == 1
    assert session.flushes == 1


def test_exception_rollback():
    session = FakeSession()
    uow = SQLAlchemyUnitOfWork(lambda: session)

    with pytest.raises(ValueError):
        with uow:
            raise ValueError("boom")

    assert session.rollbacks == 1
    assert session.closes == 1


def test_repository_access_and_shared_session():
    session = FakeSession()
    uow = SQLAlchemyUnitOfWork(lambda: session)

    with uow:
        assert uow.contact_repository is not None
        assert uow.member_repository is not None
        assert uow.membership_repository is not None
        assert uow.invoice_repository is not None
        assert uow.payment_repository is not None
        assert uow.journal_repository is not None

        assert uow.contact_repository._session is session
        assert uow.member_repository._session is session
        assert uow.membership_repository._session is session
        assert uow.invoice_repository._session is session
        assert uow.payment_repository._session is session
        assert uow.journal_repository._session is session


def test_session_lifecycle():
    session = FakeSession()
    uow = SQLAlchemyUnitOfWork(lambda: session)

    with uow:
        assert uow.session is session

    assert session.closes == 1
