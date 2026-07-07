from mfm.config.manager import ConfigManager


def test_configuration_loads():

    config = ConfigManager.load()

    assert config.application.name == "MFM Enterprise"

    assert config.database.provider == "sqlite"