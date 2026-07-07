"""
Common application paths.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

CONFIG_DIR = PROJECT_ROOT / "config"

LOG_DIR = PROJECT_ROOT / "logs"

RESOURCE_DIR = PROJECT_ROOT / "resources"

DATA_DIR = PROJECT_ROOT / "data"

DATABASE_DIR = DATA_DIR / "database"

DATABASE_FILE = DATABASE_DIR / "mfm.db"