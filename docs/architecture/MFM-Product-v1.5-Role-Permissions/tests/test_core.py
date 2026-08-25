import tempfile
from pathlib import Path
from src.database.db import Database
from src.database.schema import initialize_schema
from src.application.context import ApplicationContext

def test_core_crud():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        ctx.projects.create("Test Project")
        ctx.tasks.create("Test Task")
        ctx.risks.create("Test Risk", "High")
        ctx.decisions.create("Test Decision")
        assert ctx.projects.count() == 1
        assert ctx.tasks.count_open() == 1
        assert ctx.risks.count_high() == 1
        assert ctx.decisions.count_pending() == 1


def test_accounting_balanced_posting():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        accounts = ctx.accounting.accounts()
        bank = next(a for a in accounts if a["number"] == "1000")
        income = next(a for a in accounts if a["number"] == "3000")
        jid = ctx.accounting.post_journal(
            1,
            "Membership payment",
            [
                {"account_id": bank["id"], "debit": 500, "credit": 0},
                {"account_id": income["id"], "debit": 0, "credit": 500},
            ],
        )
        assert jid == 1
        assert db.fetch_one("SELECT status FROM journals WHERE id=?", (jid,))["status"] == "Posted"

def test_accounting_rejects_unbalanced_journal():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        accounts = ctx.accounting.accounts()
        a = accounts[0]
        b = accounts[1]
        try:
            ctx.accounting.post_journal(
                1, "Invalid", [
                    {"account_id": a["id"], "debit": 100, "credit": 0},
                    {"account_id": b["id"], "debit": 0, "credit": 90},
                ])
            assert False, "Expected ValueError"
        except ValueError:
            pass


def test_fiscal_year_creates_12_open_periods():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        ctx.accounting.create_fiscal_year(2026)
        periods = ctx.accounting.periods(2026)
        assert len(periods) == 12
        assert all(p["status"] == "Open" for p in periods)
        assert periods[0]["start_date"] == "2026-01-01"
        assert periods[-1]["end_date"] == "2026-12-31"

def test_journal_number_is_automatic():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        accounts = ctx.accounting.accounts()
        bank = next(a for a in accounts if a["number"] == "1000")
        income = next(a for a in accounts if a["number"] == "3000")
        ctx.accounting.post_journal(None, "First", [
            {"account_id": bank["id"], "debit": 10, "credit": 0},
            {"account_id": income["id"], "debit": 0, "credit": 10},
        ])
        ctx.accounting.post_journal(None, "Second", [
            {"account_id": bank["id"], "debit": 20, "credit": 0},
            {"account_id": income["id"], "debit": 0, "credit": 20},
        ])
        rows = db.fetch_all("SELECT journal_no FROM journals ORDER BY id")
        assert [r["journal_no"] for r in rows] == [1, 2]


def test_financial_reports():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        accounts = ctx.accounting.accounts()
        bank = next(a for a in accounts if a["number"] == "1000")
        income = next(a for a in accounts if a["number"] == "3000")
        expense = next(a for a in accounts if a["number"] == "5000")
        ctx.accounting.post_journal(None, "Income", [
            {"account_id": bank["id"], "debit": 1000, "credit": 0},
            {"account_id": income["id"], "debit": 0, "credit": 1000},
        ])
        ctx.accounting.post_journal(None, "Expense", [
            {"account_id": expense["id"], "debit": 300, "credit": 0},
            {"account_id": bank["id"], "debit": 0, "credit": 300},
        ])
        income_report = ctx.accounting.income_statement()
        assert income_report["total_income"] == 1000
        assert income_report["total_expenses"] == 300
        assert income_report["result"] == 700


def test_project_budget_vs_actual():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        project_id = ctx.projects.create("Restoration")
        ctx.projects.set_budget(project_id, 1000)
        accounts = ctx.accounting.accounts()
        expense = next(a for a in accounts if a["number"] == "5000")
        bank = next(a for a in accounts if a["number"] == "1000")
        ctx.accounting.post_journal(None, "Project expense", [
            {"account_id": expense["id"], "debit": 250, "credit": 0, "project_id": project_id},
            {"account_id": bank["id"], "debit": 0, "credit": 250, "project_id": project_id},
        ])
        r = ctx.accounting.project_budget_vs_actual(project_id)
        assert r["budget"] == 1000
        assert r["actual"] == 250
        assert r["variance"] == 750
        assert r["utilization"] == 25


def test_membership_core():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        member_id = ctx.members.create_member("M001", "Hans", "Hansen")
        type_id = ctx.members.create_membership_type("Ordinary", 500)
        membership_id = ctx.members.add_membership(member_id, type_id)
        invoice_id = ctx.members.invoice_membership(membership_id, member_id, 500)
        assert member_id == 1
        assert membership_id == 1
        assert invoice_id == 1
        assert ctx.members.members()[0]["member_no"] == "M001"
        assert ctx.members.invoices()[0]["amount"] == 500


def test_membership_payment_posts_to_accounting():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        member_id = ctx.members.create_member("M002", "Test", "Member")
        type_id = ctx.members.create_membership_type("Ordinary", 500)
        membership_id = ctx.members.add_membership(member_id, type_id)
        invoice_id = ctx.members.invoice_membership(membership_id, member_id, 500)
        payment_id = ctx.members.register_payment(invoice_id, 500)
        assert payment_id == 1
        invoice = db.fetch_one("SELECT status FROM membership_invoices WHERE id=?", (invoice_id,))
        assert invoice["status"] == "Paid"
        journals = db.fetch_all("SELECT * FROM journals WHERE status='Posted'")
        assert len(journals) == 1
        lines = db.fetch_all("SELECT * FROM journal_lines WHERE journal_id=?", (journals[0]["id"],))
        assert sum(x["debit"] for x in lines) == 500
        assert sum(x["credit"] for x in lines) == 500


def test_bank_reconciliation():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        bank_id = ctx.bank.create_account("Main Bank", "123")
        bank = next(a for a in ctx.accounting.accounts() if a["number"] == "1000")
        income = next(a for a in ctx.accounting.accounts() if a["number"] == "3000")
        journal_id = ctx.accounting.post_journal(None, "Bank deposit", [
            {"account_id": bank["id"], "debit": 500, "credit": 0},
            {"account_id": income["id"], "debit": 0, "credit": 500},
        ])
        tx_id = ctx.bank.import_transaction(bank_id, 500, "Bank deposit")
        assert len(ctx.bank.unmatched()) == 1
        candidates = ctx.bank.candidates(500)
        assert any(x["id"] == journal_id for x in candidates)
        ctx.bank.match(tx_id, journal_id)
        assert ctx.bank.summary()["matched"] == 1
        assert ctx.bank.summary()["unmatched"] == 0


def test_management_snapshot_and_attention():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        ctx.tasks.create("Overdue task", due_date="2000-01-01")
        ctx.risks.create("High risk", "High")
        ctx.decisions.create("Pending decision")
        snapshot = ctx.management.snapshot()
        assert snapshot["open_tasks"] == 1
        assert snapshot["overdue_tasks"] == 1
        assert snapshot["high_risks"] == 1
        assert snapshot["pending_decisions"] == 1
        priorities = [x[0] for x in ctx.management.attention_items()]
        assert "HIGH" in priorities


def test_user_authentication():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        user = ctx.users.authenticate("admin", "admin")
        assert user is not None
        assert user["role_name"] == "Administrator"
        assert ctx.users.authenticate("admin", "wrong") is None


def test_backup_restore():
    with tempfile.TemporaryDirectory() as d:
        base = Path(d)
        db = Database(base / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        ctx.system.set_setting("company_name", "Test Association")
        backup = base / "backup.db"
        ctx.system.backup(backup)
        assert backup.exists()
        ctx.system.set_setting("company_name", "Changed")
        safety = ctx.system.restore(backup)
        assert safety.exists()
        restored = Database(db.path)
        assert restored.fetch_one(
            "SELECT value FROM app_settings WHERE key='company_name'"
        )["value"] == "Test Association"


def test_global_search():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        ctx.members.create_member("M100", "Hans", "Search")
        ctx.projects.create("Álvur Restoration", "Historic vessel project")
        ctx.tasks.create("Prepare restoration application")
        results = ctx.search.search("Hans")
        assert any(x["entity"] == "Member" for x in results)
        results = ctx.search.search("Álvur")
        assert any(x["entity"] == "Project" for x in results)
        results = ctx.search.search("restoration")
        assert any(x["entity"] == "Project" for x in results)
        assert any(x["entity"] == "Task" for x in results)


def test_exports():
    with tempfile.TemporaryDirectory() as d:
        base = Path(d)
        db = Database(base / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        ctx.members.create_member("M300", "Export", "Test")
        ctx.projects.create("Export Project")
        member_file = base / "members.csv"
        project_file = base / "projects.csv"
        ctx.export.export_members(member_file)
        ctx.export.export_projects(project_file)
        assert "Export,Test" in member_file.read_text(encoding="utf-8-sig")
        assert "Export Project" in project_file.read_text(encoding="utf-8-sig")


def test_organization_settings():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        ctx.organization.save(
            "Álvur Preservation Association",
            "12345678",
            "Harbour Road 1",
            "5000",
            "Odense",
            "Denmark",
            "info@example.org",
            "+45 12345678",
            "DKK",
            1
        )
        org = ctx.organization.get()
        assert org["name"] == "Álvur Preservation Association"
        assert org["currency"] == "DKK"
        assert org["fiscal_year_start"] == 1


def test_role_permissions():
    with tempfile.TemporaryDirectory() as d:
        db = Database(Path(d) / "test.db")
        initialize_schema(db)
        ctx = ApplicationContext(db)
        admin = ctx.users.authenticate("admin", "admin")
        assert ctx.permissions.can(admin, "users.manage")
        manager_role = ctx.users.repo.get_role("Manager")
        manager_id = ctx.users.repo.create_user(
            "manager", "Manager User", ctx.users._hash("pw"), manager_role["id"]
        )
        manager = ctx.users.authenticate("manager", "pw")
        assert manager is not None
        assert ctx.permissions.can(manager, "projects.edit")
        assert not ctx.permissions.can(manager, "users.manage")
        user_role = ctx.users.repo.get_role("User")
        ctx.users.repo.create_user(
            "basic", "Basic User", ctx.users._hash("pw"), user_role["id"]
        )
        basic = ctx.users.authenticate("basic", "pw")
        assert ctx.permissions.can(basic, "projects.view")
        assert not ctx.permissions.can(basic, "projects.edit")
