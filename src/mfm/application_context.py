"""
Application Context.

Contains shared application services.
"""

from __future__ import annotations

from dataclasses import dataclass

from mfm.config.models import Config


@dataclass(slots=True)
class ApplicationContext:

    config: Config

    logger: object | None = None

    database: object | None = None

    services: object | None = None