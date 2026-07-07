from mfm.database.engine import EngineFactory
from mfm.database.health import check_database


def test_database_health():

    engine = EngineFactory.create(
        "sqlite:///:memory:"
    )

    assert check_database(engine)