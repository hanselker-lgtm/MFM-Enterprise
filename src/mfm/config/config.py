"""
Configuration loader.
"""

from pathlib import Path
import tomllib


class Configuration:

    def __init__(self, filename: str):

        self.filename = Path(filename)

        with open(self.filename, "rb") as f:
            self.data = tomllib.load(f)

    def get(self, *keys, default=None):

        value = self.data

        for key in keys:

            if not isinstance(value, dict):

                return default

            value = value.get(key)

            if value is None:

                return default

        return value