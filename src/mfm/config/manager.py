from __future__ import annotations

from pathlib import Path
from typing import Any

import tomllib

from mfm.config.exceptions import ConfigurationError
from mfm.config.models import (
    ApplicationConfig,
    Config,
    DatabaseConfig,
    GuiConfig,
    LoggingConfig,
)


class ConfigManager:
    """
    Loads the application configuration.

    Configuration is loaded in two steps:

    1. config/default.toml (required)
    2. config/user.toml (optional)

    Values from user.toml override the defaults.
    """

    CONFIG_DIR = (
        Path(__file__).resolve().parents[3]
        / "config"
    )

    DEFAULT_FILE = CONFIG_DIR / "default.toml"

    USER_FILE = CONFIG_DIR / "user.toml"

    @classmethod
    def _load_toml(cls, path: Path) -> dict[str, Any]:
        """
        Load a TOML file.

        Returns an empty dict if the file does not exist.
        """

        if not path.exists():
            return {}

        try:
            with path.open("rb") as fp:
                data = tomllib.load(fp)

        except Exception as exc:
            raise ConfigurationError(
                f"Unable to read configuration file '{path.name}': {exc}"
            ) from exc

        if not isinstance(data, dict):
            return {}

        return data

    @staticmethod
    def _merge(
        default: dict[str, Any],
        user: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Merge user configuration into default configuration.
        """

        result: dict[str, Any] = default.copy()

        for key, value in user.items():

            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                merged = result[key].copy()
                merged.update(value)
                result[key] = merged

            else:
                result[key] = value

        return result

    @classmethod
    def load(cls) -> Config:
        """
        Load the effective application configuration.
        """

        default_data = cls._load_toml(
            cls.DEFAULT_FILE
        )

        if not default_data:
            raise ConfigurationError(
                "default.toml is missing or empty."
            )

        user_data = cls._load_toml(
            cls.USER_FILE
        )

        data = cls._merge(
            default_data,
            user_data,
        )

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