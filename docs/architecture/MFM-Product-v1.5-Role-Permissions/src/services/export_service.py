import csv
from pathlib import Path

class ExportService:
    def __init__(self, context):
        self.ctx = context

    def _write_csv(self, path, headers, rows):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
        return path

    def export_members(self, path):
        rows = self.ctx.members.members()
        headers = ["member_no","first_name","last_name","email","phone","status","joined_date"]
        return self._write_csv(path, headers, [[r[h] for h in headers] for r in rows])

    def export_projects(self, path):
        rows = self.ctx.projects.list()
        headers = ["id","name","status","budget","start_date","end_date"]
        return self._write_csv(path, headers, [[r[h] for h in headers] for r in rows])

    def export_journals(self, path):
        rows = self.ctx.accounting.journals()
        headers = ["journal_no","journal_date","description","status"]
        return self._write_csv(path, headers, [[r[h] for h in headers] for r in rows])

    def export_invoices(self, path):
        rows = self.ctx.members.invoices()
        headers = ["invoice_no","member_no","first_name","last_name","invoice_date","due_date","amount","status"]
        return self._write_csv(path, headers, [[r[h] for h in headers] for r in rows])

    def export_bank_transactions(self, path):
        rows = self.ctx.bank.transactions()
        headers = ["id","transaction_date","amount","description","external_reference","status"]
        return self._write_csv(path, headers, [[r[h] for h in headers] for r in rows])

    def export_trial_balance(self, path):
        rows = self.ctx.accounting.trial_balance()
        headers = ["number","name","debit","credit"]
        return self._write_csv(path, headers, [[r[h] for h in headers] for r in rows])
