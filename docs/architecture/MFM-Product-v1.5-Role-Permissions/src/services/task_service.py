class TaskService:
    def __init__(self, repo): self.repo = repo
    def create(self, title, owner="", due_date=None):
        title = title.strip()
        if not title: raise ValueError("Task title is required.")
        return self.repo.create(title, owner.strip(), due_date)
    def list(self): return self.repo.list()
    def count_open(self): return self.repo.count_open()
    def count_overdue(self, today): return self.repo.count_overdue(today)
