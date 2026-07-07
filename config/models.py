from dataclasses import dataclass


@dataclass(slots=True)
class ApplicationConfig:
    name: str
    version: str
    language: str
    theme: str


@dataclass(slots=True)
class DatabaseConfig:
    provider: str
    path: str


@dataclass(slots=True)
class LoggingConfig:
    level: str
    directory: str
    filename: str


@dataclass(slots=True)
class GuiConfig:
    style: str


@dataclass(slots=True)
class Config:

    application: ApplicationConfig

    database: DatabaseConfig

    logging: LoggingConfig

    gui: GuiConfig