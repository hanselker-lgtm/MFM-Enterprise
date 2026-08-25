class DecisionRepository:
    def __init__(self, db): self.db = db
    def list(self): return self.db.fetch_all("SELECT * FROM decisions ORDER BY id DESC")
    def create(self, title, owner="", decision_text=""):
        return self.db.execute(
            "INSERT INTO decisions(title,owner,decision_text) VALUES(?,?,?)",
            (title, owner, decision_text))
    def count_pending(self): return self.db.fetch_one(
        "SELECT COUNT(*) c FROM decisions WHERE status='Pending'")["c"]
