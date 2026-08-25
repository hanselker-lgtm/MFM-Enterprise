class PermissionService:
    DEFAULTS = {
        "Administrator": ["*"],
        "Manager": [
            "dashboard.view", "projects.view", "projects.edit",
            "members.view", "members.edit", "accounting.view",
            "bank.view", "bank.reconcile", "reports.export"
        ],
        "User": [
            "dashboard.view", "projects.view", "members.view",
            "accounting.view", "bank.view"
        ],
    }

    def __init__(self, repo, user_repo):
        self.repo = repo
        self.user_repo = user_repo

    def ensure_defaults(self):
        self.repo.seed_permissions()
        permissions = self.repo.permissions()
        roles = self.user_repo.roles()
        for role in roles:
            desired = self.DEFAULTS.get(role["name"], [])
            if "*" in desired:
                desired = [p["code"] for p in permissions]
            for p in permissions:
                if p["code"] in desired:
                    self.repo.grant(role["id"], p["id"])

    def can(self, user, code):
        if not user:
            return False
        if user["role_name"] == "Administrator":
            return True
        return self.repo.has_permission(user["role_id"], code)

    def permissions_for(self, user):
        if not user:
            return []
        if user["role_name"] == "Administrator":
            return self.repo.permissions()
        return self.repo.role_permissions(user["role_id"])
