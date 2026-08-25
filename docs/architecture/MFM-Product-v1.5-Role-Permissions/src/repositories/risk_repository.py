class RiskRepository:
    def __init__(self, db): self.db = db
    def list(self): return self.db.fetch_all("SELECT * FROM risks ORDER BY id DESC")
    def create(self, title, severity="Medium", owner="", mitigation=""):
        return self.db.execute(
            "INSERT INTO risks(title,severity,owner,mitigation) VALUES(?,?,?,?)",
            (title, severity, owner, mitigation))
    def count_open(self): return self.db.fetch_one(
        "SELECT COUNT(*) c FROM risks WHERE status='Open'")["c"]
    def count_high(self): return self.db.fetch_one(
        "SELECT COUNT(*) c FROM risks WHERE status='Open' AND severity='High'")["c"]
