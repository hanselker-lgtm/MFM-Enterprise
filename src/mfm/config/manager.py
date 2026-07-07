from pathlib import Path
import shutil
import tomllib

from mfm.config.exceptions import ConfigurationError
from mfm.config.models import *


class ConfigManager:

    CONFIG_DIR = (
        Path(__file__).resolve().parents[3]
        / "config"
    )

    DEFAULT_FILE = CONFIG_DIR / "default.toml"

    USER_FILE = CONFIG_DIR / "user.toml"

    @classmethod
    def load(cls) -> Config:

        if not cls.USER_FILE.exists():

            shutil.copy(
                cls.DEFAULT_FILE,
                cls.USER_FILE,
            )

        try:

            with cls.USER_FILE.open("rb") as fp:

                data = tomllib.load(fp)

        except Exception as exc:

            raise ConfigurationError(str(exc))

        return Config(
            application=ApplicationConfig(
                **data["application"]
            ),
            database=DatabaseConfig(
                **data["database"]
            ),
            logging=LoggingConfig(
                **data["logging"]
            ),
            gui=GuiConfig(
                **data["gui"]
            ),
        )