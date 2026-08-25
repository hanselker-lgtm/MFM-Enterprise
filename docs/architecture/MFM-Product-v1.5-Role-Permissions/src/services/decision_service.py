class DecisionService:
    def __init__(self, repo): self.repo = repo
    def create(self, title, owner="", decision_text=""):
        title = title.strip()
        if not title: raise ValueError("Decision title is required.")
        return self.repo.create(title, owner.strip(), decision_text.strip())
    def list(self): return self.repo.list()
    def count_pending(self): return self.repo.count_pending()
