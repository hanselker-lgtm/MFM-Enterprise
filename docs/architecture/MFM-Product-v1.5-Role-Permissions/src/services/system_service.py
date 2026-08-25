import shutil
from datetime import datetime
from pathlib import Path

class SystemService:
    def __init__(self, db):
        self.db = db

    def get_setting(self, key, default=""):
        row = self.db.fetch_one("SELECT value FROM app_settings WHERE key=?", (key,))
        return row["value"] if row else default

    def set_setting(self, key, value):
        self.db.execute(
            """INSERT INTO app_settings(key,value) VALUES(?,?)
               ON CONFLICT(key) DO UPDATE SET value=excluded.value""",
            (key, str(value))
        )

    def backup(self, destination):
        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Close any active SQLite connection before copying.
        with self.db.connect() as conn:
            conn.execute("PRAGMA wal_checkpoint(FULL)")
        shutil.copy2(self.db.path, destination)
        return destination

    def restore(self, source):
        source = Path(source)
        if not source.exists():
            raise FileNotFoundError("Backup file not found.")
        # Keep the existing database file as a safety copy.
        safety = self.db.path.with_name(
            self.db.path.stem + "_before_restore_" +
            datetime.now().strftime("%Y%m%d_%H%M%S") + self.db.path.suffix
        )
        if self.db.path.exists():
            shutil.copy2(self.db.path, safety)
        shutil.copy2(source, self.db.path)
        return safety
