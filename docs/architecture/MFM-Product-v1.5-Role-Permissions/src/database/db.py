from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "mfm.db"

class Database:
    def __init__(self, path=DB_PATH):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self):
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def execute(self, sql, params=()):
        with self.connect() as conn:
            cur = conn.execute(sql, params)
            conn.commit()
            return cur.lastrowid

    def fetch_all(self, sql, params=()):
        with self.connect() as conn:
            return conn.execute(sql, params).fetchall()

    def fetch_one(self, sql, params=()):
        with self.connect() as conn:
            return conn.execute(sql, params).fetchone()

    def transaction(self, statements):
        with self.connect() as conn:
            try:
                for sql, params in statements:
                    conn.execute(sql, params)
                conn.commit()
            except Exception:
                conn.rollback()
                raise
