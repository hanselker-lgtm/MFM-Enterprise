class ProjectRepository:
    def __init__(self, db): self.db = db
    def list(self): return self.db.fetch_all("SELECT * FROM projects ORDER BY id DESC")
    def create(self, name, description, status, budget):
        return self.db.execute(
            "INSERT INTO projects(name,description,status,budget) VALUES(?,?,?,?)",
            (name, description, status, budget))
    def count(self): return self.db.fetch_one("SELECT COUNT(*) c FROM projects")["c"]


def set_budget(self, project_id, amount):
    existing = self.db.fetch_one(
        "SELECT id FROM project_budgets WHERE project_id=?", (project_id,)
    )
    if existing:
        self.db.execute(
            "UPDATE project_budgets SET budget_amount=? WHERE project_id=?",
            (amount, project_id)
        )
        return existing["id"]
    return self.db.execute(
        "INSERT INTO project_budgets(project_id,budget_amount) VALUES(?,?)",
        (project_id, amount)
    )

def project_budget(self, project_id):
    return self.db.fetch_one(
        "SELECT * FROM project_budgets WHERE project_id=?", (project_id,)
    )
