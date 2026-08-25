from datetime import date

class AccountingService:
    def __init__(self, repo):
        self.repo = repo

    def seed_standard_accounts(self):
        existing = self.repo.list_accounts()
        if existing:
            return
        defaults = [
            ("1000", "Bank", "Asset"),
            ("1100", "Cash", "Asset"),
            ("1200", "Receivables", "Asset"),
            ("2000", "Payables", "Liability"),
            ("3000", "Membership Income", "Income"),
            ("4000", "Grants and Donations", "Income"),
            ("5000", "Operating Expenses", "Expense"),
            ("5100", "Project Expenses", "Expense"),
        ]
        for item in defaults:
            self.repo.create_account(*item)

    def accounts(self):
        return self.repo.list_accounts()

    def create_account(self, number, name, account_type):
        number = number.strip()
        name = name.strip()
        if not number or not name:
            raise ValueError("Account number and name are required.")
        return self.repo.create_account(number, name, account_type)

    def create_fiscal_year(self, year):
        year = int(year)
        if self.repo.get_fiscal_year(year):
            raise ValueError("Fiscal year already exists.")
        year_id = self.repo.create_fiscal_year(year)
        for month in range(1, 13):
            start = f"{year:04d}-{month:02d}-01"
            if month == 12:
                end = f"{year:04d}-12-31"
            else:
                from calendar import monthrange
                end = f"{year:04d}-{month:02d}-{monthrange(year, month)[1]:02d}"
            self.repo.create_period(year_id, month, start, end)
        return year_id

    def fiscal_years(self):
        return self.repo.list_fiscal_years()

    def periods(self, year):
        fy = self.repo.get_fiscal_year(int(year))
        if not fy:
            return []
        return self.repo.list_periods(fy["id"])

    def close_period(self, period_id):
        row = self.repo.db.fetch_one("SELECT status FROM fiscal_periods WHERE id=?", (period_id,))
        if not row:
            raise ValueError("Period not found.")
        if row["status"] == "Closed":
            return
        self.repo.set_period_status(period_id, "Closed")

    def reopen_period(self, period_id):
        self.repo.set_period_status(period_id, "Open")

    def post_journal(self, journal_no, description, lines, journal_date=None):
        journal_date = journal_date or date.today().isoformat()
        if journal_no is None:
            journal_no = self.repo.next_journal_number("FIN")
        if not lines or len(lines) < 2:
            raise ValueError("A journal needs at least two lines.")

        debit = round(sum(float(x["debit"]) for x in lines), 2)
        credit = round(sum(float(x["credit"]) for x in lines), 2)
        if debit <= 0 or credit <= 0 or debit != credit:
            raise ValueError("Journal must balance: total debit must equal total credit.")

        journal_id = self.repo.create_journal(journal_no, journal_date, description.strip())
        for line in lines:
            d = float(line["debit"])
            c = float(line["credit"])
            if d < 0 or c < 0 or (d > 0 and c > 0):
                raise ValueError("Each line must contain either debit or credit.")
            self.repo.add_line(
                journal_id,
                int(line["account_id"]),
                line.get("description", ""),
                d, c,
                line.get("project_id"),
            )
        self.repo.set_journal_status(journal_id, "Posted")
        return journal_id

    def journals(self):
        return self.repo.list_journals()

    def trial_balance(self):
        return self.repo.trial_balance()


def _account_totals(self):
    rows = self.repo.trial_balance()
    result = []
    for r in rows:
        debit = float(r["debit"] or 0)
        credit = float(r["credit"] or 0)
        result.append({
            "number": r["number"],
            "name": r["name"],
            "debit": debit,
            "credit": credit,
            "balance": debit - credit,
        })
    return result

def income_statement(self):
    rows = self._account_totals()
    income = [r for r in rows if r["number"].startswith("3") or r["number"].startswith("4")]
    expenses = [r for r in rows if r["number"].startswith("5")]
    total_income = sum(-r["balance"] for r in income)
    total_expenses = sum(r["balance"] for r in expenses)
    return {
        "income": income,
        "expenses": expenses,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "result": total_income - total_expenses,
    }

def balance_sheet(self):
    rows = self._account_totals()
    assets = [r for r in rows if r["number"].startswith("1")]
    liabilities = [r for r in rows if r["number"].startswith("2")]
    equity = [r for r in rows if r["number"].startswith("8") or r["number"].startswith("9")]
    total_assets = sum(r["balance"] for r in assets)
    total_liabilities = sum(-r["balance"] for r in liabilities)
    total_equity = sum(-r["balance"] for r in equity)
    return {
        "assets": assets,
        "liabilities": liabilities,
        "equity": equity,
        "total_assets": total_assets,
        "total_liabilities": total_liabilities,
        "total_equity": total_equity,
    }

def account_movements(self, account_id, start_date=None, end_date=None):
    return self.repo.account_movements(account_id, start_date, end_date)

def project_financials(self, project_id):
    return self.repo.project_financials(project_id)


def project_budget_vs_actual(self, project_id):
    budget = self.repo.db.fetch_one(
        "SELECT budget_amount FROM project_budgets WHERE project_id=?",
        (project_id,)
    )
    actual = self.repo.project_actuals(project_id)
    budget_amount = float(budget["budget_amount"]) if budget else 0.0
    # Project expenses are represented by debit minus credit in this first baseline.
    actual_amount = float(actual["debit"] or 0) - float(actual["credit"] or 0)
    return {
        "budget": budget_amount,
        "actual": actual_amount,
        "variance": budget_amount - actual_amount,
        "utilization": (actual_amount / budget_amount * 100) if budget_amount else 0.0,
    }
