from datetime import date

class ManagementService:
    def __init__(self, context):
        self.ctx = context

    def snapshot(self):
        today = date.today().isoformat()
        income = self.ctx.accounting.income_statement()
        bank = self.ctx.bank.summary()
        return {
            "projects": self.ctx.projects.count(),
            "open_tasks": self.ctx.tasks.count_open(),
            "overdue_tasks": self.ctx.tasks.count_overdue(today),
            "open_risks": self.ctx.risks.count_open(),
            "high_risks": self.ctx.risks.count_high(),
            "pending_decisions": self.ctx.decisions.count_pending(),
            "members": len(self.ctx.members.members()),
            "open_invoices": sum(1 for x in self.ctx.members.invoices() if x["status"] != "Paid"),
            "unmatched_bank": bank["unmatched"] or 0,
            "income": income["total_income"],
            "expenses": income["total_expenses"],
            "result": income["result"],
        }

    def attention_items(self):
        s = self.snapshot()
        items = []
        if s["overdue_tasks"]:
            items.append(("HIGH", f"{s['overdue_tasks']} task(s) are overdue."))
        if s["high_risks"]:
            items.append(("HIGH", f"{s['high_risks']} high-risk item(s) are open."))
        if s["pending_decisions"]:
            items.append(("MEDIUM", f"{s['pending_decisions']} decision(s) are pending."))
        if s["unmatched_bank"]:
            items.append(("MEDIUM", f"{s['unmatched_bank']} bank transaction(s) are unmatched."))
        if s["open_invoices"]:
            items.append(("MEDIUM", f"{s['open_invoices']} membership invoice(s) are not fully paid."))
        if not items:
            items.append(("INFO", "No immediate attention items detected."))
        return items
