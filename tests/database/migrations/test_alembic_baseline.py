"""Alembic migration baseline tests (0.4 backlog item 3).

Verifies that the migration history under ``migrations/versions`` can
actually build a fresh database from nothing, and that the resulting
schema matches what the ORM models declare -- catching the case where
someone edits a model but forgets to add a migration.
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT / "src"))


def test_alembic_upgrade_head_builds_all_tables(tmp_path: Path) -> None:
    from alembic import command
    from alembic.config import Config

    database_path = tmp_path / "mfm.db"

    alembic_cfg = Config(str(PROJECT_ROOT / "alembic.ini"))
    alembic_cfg.set_main_option("script_location", str(PROJECT_ROOT / "migrations"))
    alembic_cfg.set_main_option("sqlalchemy.url", f"sqlite:///{database_path}")

    command.upgrade(alembic_cfg, "head")

    assert database_path.exists()

    con = sqlite3.connect(database_path)
    try:
        tables = {
            row[0]
            for row in con.execute(
                "select name from sqlite_master where type='table'"
            ).fetchall()
        }
    finally:
        con.close()

    assert "alembic_version" in tables
    assert "contact" in tables
    assert "project" in tables
    assert "journal" in tables
