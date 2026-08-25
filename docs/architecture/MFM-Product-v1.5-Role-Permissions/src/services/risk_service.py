class RiskService:
    def __init__(self, repo): self.repo = repo
    def create(self, title, severity="Medium", owner="", mitigation=""):
        title = title.strip()
        if not title: raise ValueError("Risk title is required.")
        if severity not in {"Low","Medium","High","Critical"}:
            raise ValueError("Invalid risk severity.")
        return self.repo.create(title, severity, owner.strip(), mitigation.strip())
    def list(self): return self.repo.list()
    def count_open(self): return self.repo.count_open()
    def count_high(self): return self.repo.count_high()
