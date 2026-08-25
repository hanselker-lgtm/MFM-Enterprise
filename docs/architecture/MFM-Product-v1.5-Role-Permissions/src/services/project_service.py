class ProjectService:
    def __init__(self, repo): self.repo = repo
    def create(self, name, description="", status="Planned", budget=0):
        name = name.strip()
        if not name: raise ValueError("Project name is required.")
        return self.repo.create(name, description.strip(), status, float(budget or 0))
    def list(self): return self.repo.list()
    def count(self): return self.repo.count()


def set_budget(self, project_id, amount):
    amount = float(amount)
    if amount < 0:
        raise ValueError("Budget cannot be negative.")
    return self.repo.set_budget(project_id, amount)

def budget(self, project_id):
    return self.repo.project_budget(project_id)
