from datetime import date

class BankService:
    def __init__(self, repo):
        self.repo = repo

    def accounts(self):
        return self.repo.list_accounts()

    def create_account(self, name, account_number="", opening_balance=0):
        if not name.strip():
            raise ValueError("Bank account name is required.")
        return self.repo.create_account(
            name.strip(), account_number.strip(), float(opening_balance or 0)
        )

    def transactions(self, bank_account_id=None):
        return self.repo.list_transactions(bank_account_id)

    def import_transaction(self, bank_account_id, amount, description="",
                           transaction_date=None, external_reference=""):
        transaction_date = transaction_date or date.today().isoformat()
        amount = float(amount)
        if amount == 0:
            raise ValueError("Bank transaction amount cannot be zero.")
        return self.repo.create_transaction(
            bank_account_id, transaction_date, amount,
            description.strip(), external_reference.strip()
        )

    def unmatched(self):
        return self.repo.list_unmatched()

    def candidates(self, amount):
        return self.repo.list_candidate_journals(float(amount))

    def match(self, transaction_id, journal_id):
        transaction = self.repo.get_transaction(transaction_id)
        if not transaction:
            raise ValueError("Bank transaction not found.")
        if transaction["status"] == "Matched":
            raise ValueError("Bank transaction is already matched.")
        amount = abs(float(transaction["amount"]))
        self.repo.match(transaction_id, journal_id, amount)

    def summary(self):
        return self.repo.reconciliation_summary()
