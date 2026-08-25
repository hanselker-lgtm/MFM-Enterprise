class UserRepository:
    def __init__(self, db):
        self.db = db

    def seed_roles(self):
        for name, description in [
            ("Administrator", "Full system access"),
            ("Manager", "Management and reporting access"),
            ("User", "Standard operational access"),
        ]:
            self.db.execute(
                "INSERT OR IGNORE INTO roles(name,description) VALUES(?,?)",
                (name, description)
            )

    def roles(self):
        return self.db.fetch_all("SELECT * FROM roles ORDER BY id")

    def get_role(self, name):
        return self.db.fetch_one("SELECT * FROM roles WHERE name=?", (name,))

    def create_user(self, username, display_name, password_hash, role_id):
        return self.db.execute(
            """INSERT INTO users(username,display_name,password_hash,role_id)
               VALUES(?,?,?,?)""",
            (username, display_name, password_hash, role_id)
        )

    def get_user(self, username):
        return self.db.fetch_one(
            """SELECT u.*, r.name role_name
               FROM users u JOIN roles r ON r.id=u.role_id
               WHERE u.username=? AND u.active=1""",
            (username,)
        )

    def list_users(self):
        return self.db.fetch_all(
            """SELECT u.id,u.username,u.display_name,u.active,r.name role_name
               FROM users u JOIN roles r ON r.id=u.role_id ORDER BY u.username"""
        )

    def count_users(self):
        return self.db.fetch_one("SELECT COUNT(*) c FROM users")["c"]
