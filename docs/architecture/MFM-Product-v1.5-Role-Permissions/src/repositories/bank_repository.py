class BankRepository:
    def __init__(self, db):
        self.db = db

    def list_accounts(self):
        return self.db.fetch_all(
            "SELECT * FROM bank_accounts WHERE active=1 ORDER BY name"
        )

    def create_account(self, name, account_number="", opening_balance=0):
        return self.db.execute(
            """INSERT INTO bank_accounts(name,account_number,opening_balance)
               VALUES(?,?,?)""",
            (name, account_number, opening_balance)
        )

    def list_transactions(self, bank_account_id=None):
        if bank_account_id:
            return self.db.fetch_all(
                """SELECT * FROM bank_transactions
                   WHERE bank_account_id=?
                   ORDER BY transaction_date DESC, id DESC""",
                (bank_account_id,)
            )
        return self.db.fetch_all(
            "SELECT * FROM bank_transactions ORDER BY transaction_date DESC, id DESC"
        )

    def create_transaction(self, bank_account_id, transaction_date, amount,
                           description="", external_reference=""):
        return self.db.execute(
            """INSERT INTO bank_transactions
               (bank_account_id,transaction_date,amount,description,external_reference)
               VALUES(?,?,?,?,?)""",
            (bank_account_id, transaction_date, amount, description, external_reference)
        )

    def get_transaction(self, transaction_id):
        return self.db.fetch_one(
            "SELECT * FROM bank_transactions WHERE id=?", (transaction_id,)
        )

    def list_unmatched(self):
        return self.db.fetch_all(
            """SELECT bt.*, ba.name bank_name
               FROM bank_transactions bt
               JOIN bank_accounts ba ON ba.id=bt.bank_account_id
               WHERE bt.status='Unmatched'
               ORDER BY bt.transaction_date, bt.id"""
        )

    def list_candidate_journals(self, amount):
        return self.db.fetch_all(
            """SELECT j.id, j.journal_no, j.journal_date, j.description,
                      SUM(jl.debit) debit, SUM(jl.credit) credit
               FROM journals j
               JOIN journal_lines jl ON jl.journal_id=j.id
               WHERE j.status='Posted'
               GROUP BY j.id
               HAVING ABS(SUM(jl.debit)-?) < 0.005
                   OR ABS(SUM(jl.credit)-?) < 0.005
               ORDER BY j.journal_date DESC, j.journal_no DESC""",
            (abs(amount), abs(amount))
        )

    def match(self, transaction_id, journal_id, amount):
        self.db.execute(
            """INSERT INTO bank_matches(bank_transaction_id,journal_id,matched_amount)
               VALUES(?,?,?)""",
            (transaction_id, journal_id, amount)
        )
        self.db.execute(
            "UPDATE bank_transactions SET status='Matched', journal_id=? WHERE id=?",
            (journal_id, transaction_id)
        )

    def reconciliation_summary(self):
        return self.db.fetch_one(
            """SELECT
                 COUNT(*) total,
                 SUM(CASE WHEN status='Matched' THEN 1 ELSE 0 END) matched,
                 SUM(CASE WHEN status='Unmatched' THEN 1 ELSE 0 END) unmatched
               FROM bank_transactions"""
        )
