class TaskRepository:
    def __init__(self, db): self.db = db
    def list(self): return self.db.fetch_all("SELECT * FROM tasks ORDER BY id DESC")
    def create(self, title, owner="", due_date=None):
        return self.db.execute(
            "INSERT INTO tasks(title,owner,due_date) VALUES(?,?,?)",
            (title, owner, due_date))
    def count_open(self): return self.db.fetch_one(
        "SELECT COUNT(*) c FROM tasks WHERE status='Open'")["c"]
    def count_overdue(self, today):
        return self.db.fetch_one(
            "SELECT COUNT(*) c FROM tasks WHERE status='Open' AND due_date IS NOT NULL AND due_date < ?",
            (today,))["c"]
