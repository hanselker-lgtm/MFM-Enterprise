class PermissionRepository:
    def __init__(self, db):
        self.db = db

    def seed_permissions(self):
        permissions = [
            ("dashboard.view", "View management dashboard"),
            ("projects.view", "View projects"),
            ("projects.edit", "Create and edit projects"),
            ("members.view", "View members"),
            ("members.edit", "Create and edit members"),
            ("accounting.view", "View accounting"),
            ("accounting.post", "Post accounting journals"),
            ("bank.view", "View bank transactions"),
            ("bank.reconcile", "Reconcile bank transactions"),
            ("reports.export", "Export reports"),
            ("system.backup", "Create and restore backups"),
            ("system.settings", "Change organization settings"),
            ("users.manage", "Manage users and roles"),
        ]
        for code, description in permissions:
            self.db.execute(
                "INSERT OR IGNORE INTO permissions(code,description) VALUES(?,?)",
                (code, description)
            )

    def permissions(self):
        return self.db.fetch_all("SELECT * FROM permissions ORDER BY code")

    def role_permissions(self, role_id):
        return self.db.fetch_all(
            """SELECT p.* FROM permissions p
               JOIN role_permissions rp ON rp.permission_id=p.id
               WHERE rp.role_id=? ORDER BY p.code""",
            (role_id,)
        )

    def grant(self, role_id, permission_id):
        self.db.execute(
            "INSERT OR IGNORE INTO role_permissions(role_id,permission_id) VALUES(?,?)",
            (role_id, permission_id)
        )

    def has_permission(self, role_id, code):
        row = self.db.fetch_one(
            """SELECT 1 ok
               FROM role_permissions rp
               JOIN permissions p ON p.id=rp.permission_id
               WHERE rp.role_id=? AND p.code=?""",
            (role_id, code)
        )
        return row is not None
