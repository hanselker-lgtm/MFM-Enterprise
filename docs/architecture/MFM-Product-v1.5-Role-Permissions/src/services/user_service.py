import base64
import hashlib
import hmac
import os

class UserService:
    ITERATIONS = 210_000

    def __init__(self, repo):
        self.repo = repo

    def _hash(self, password, salt=None):
        if not password:
            raise ValueError("Password is required.")
        salt = salt or os.urandom(16)
        digest = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, self.ITERATIONS
        )
        return f"pbkdf2_sha256${self.ITERATIONS}${base64.b64encode(salt).decode()}${base64.b64encode(digest).decode()}"

    def _verify(self, password, stored):
        try:
            scheme, iterations, salt_b64, digest_b64 = stored.split("$")
            salt = base64.b64decode(salt_b64)
            expected = base64.b64decode(digest_b64)
            actual = hashlib.pbkdf2_hmac(
                "sha256", password.encode("utf-8"), salt, int(iterations)
            )
            return hmac.compare_digest(actual, expected)
        except Exception:
            return False

    def ensure_defaults(self):
        self.repo.seed_roles()
        if self.repo.count_users() == 0:
            role = self.repo.get_role("Administrator")
            self.repo.create_user("admin", "Administrator", self._hash("admin"), role["id"])

    def authenticate(self, username, password):
        user = self.repo.get_user(username.strip())
        if not user or not self._verify(password, user["password_hash"]):
            return None
        return user

    def users(self):
        return self.repo.list_users()

    def roles(self):
        return self.repo.roles()
