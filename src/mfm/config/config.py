from pathlib import Path
import tomllib

from mfm.config.models import *


CONFIG_FILE = (
    Path(__file__)
    .resolve()
    .parents[3]
    / "config"
    / "default.toml"
)


def load_configuration() -> Config:

    with CONFIG_FILE.open("rb") as fp:
        data = tomllib.load(fp)

    return Config(
        application=ApplicationConfig(**data["application"]),
        database=DatabaseConfig(**data["database"]),
        logging=LoggingConfig(**data["logging"]),
        gui=GuiConfig(**data["gui"]),
    )