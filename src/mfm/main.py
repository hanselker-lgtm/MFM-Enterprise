"""
Application entry point.
"""

from pathlib import Path

from mfm.config.config import Configuration
from mfm.common.logging import configure_logging
from mfm.database.session import create_session


def main():

    config = Configuration(
        Path("config") / "development.toml"
    )

    configure_logging(
        config.get("logging", "file"),
        config.get("logging", "level"),
    )

    database_path = config.get("database", "path")

    database_url = f"sqlite:///{database_path}"

    engine, session_factory = create_session(database_url)

    print("MFM Enterprise started successfully.")

    print(engine)


if __name__ == "__main__":

    main()