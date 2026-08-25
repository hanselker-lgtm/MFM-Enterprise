from datetime import date, timedelta

class MemberService:
    def __init__(self, repo, accounting=None):
        self.repo = repo
        self.accounting = accounting

    def create_member(self, member_no, first_name, last_name, **kwargs):
        if not member_no.strip():
            raise ValueError("Member number is required.")
        if not first_name.strip() or not last_name.strip():
            raise ValueError("First name and last name are required.")
        return self.repo.create_member(
            member_no.strip(), first_name.strip(), last_name.strip(),
            kwargs.get("email","").strip(), kwargs.get("phone","").strip(),
            kwargs.get("address","").strip(), kwargs.get("postal_code","").strip(),
            kwargs.get("city","").strip(), kwargs.get("joined_date")
        )

    def members(self):
        return self.repo.list_members()

    def create_membership_type(self, name, annual_fee):
        name = name.strip()
        annual_fee = float(annual_fee)
        if not name:
            raise ValueError("Membership type name is required.")
        if annual_fee < 0:
            raise ValueError("Membership fee cannot be negative.")
        return self.repo.create_membership_type(name, annual_fee)

    def membership_types(self):
        return self.repo.list_membership_types()

    def add_membership(self, member_id, membership_type_id, start_date=None):
        start_date = start_date or date.today().isoformat()
        return self.repo.create_membership(member_id, membership_type_id, start_date)

    def memberships(self):
        return self.repo.list_memberships()

    def invoice_membership(self, membership_id, member_id, amount, invoice_date=None, due_date=None):
        invoice_date = invoice_date or date.today().isoformat()
        due_date = due_date or (date.today() + timedelta(days=14)).isoformat()
        invoice_no = self.repo.next_invoice_number()
        invoice_id = self.repo.create_invoice(
            member_id, membership_id, invoice_no, invoice_date, due_date, float(amount)
        )
        return invoice_id

    def invoices(self):
        return self.repo.list_invoices()


def register_payment(self, invoice_id, amount, payment_date=None):
    payment_date = payment_date or date.today().isoformat()
    invoice = self.repo.get_invoice(invoice_id)
    if not invoice:
        raise ValueError("Invoice not found.")
    amount = float(amount)
    if amount <= 0:
        raise ValueError("Payment must be greater than zero.")

    paid_before = self.repo.invoice_paid_amount(invoice_id)
    remaining = round(float(invoice["amount"]) - paid_before, 2)
    if amount > remaining:
        raise ValueError("Payment exceeds outstanding invoice amount.")

    journal_id = None
    if self.accounting:
        accounts = self.accounting.accounts()
        bank = next((a for a in accounts if a["number"] == "1000"), None)
        receivable = next((a for a in accounts if a["number"] == "1200"), None)
        if bank and receivable:
            journal_id = self.accounting.post_journal(
                None,
                f"Payment invoice {invoice['invoice_no']}",
                [
                    {"account_id": bank["id"], "debit": amount, "credit": 0},
                    {"account_id": receivable["id"], "debit": 0, "credit": amount},
                ],
                payment_date
            )

    payment_id = self.repo.register_payment(
        invoice_id, payment_date, amount, journal_id
    )
    paid_after = round(paid_before + amount, 2)
    self.repo.update_invoice_status(
        invoice_id, "Paid" if paid_after >= float(invoice["amount"]) else "Partially Paid"
    )
    return payment_id

def payments(self):
    return self.repo.list_payments()
