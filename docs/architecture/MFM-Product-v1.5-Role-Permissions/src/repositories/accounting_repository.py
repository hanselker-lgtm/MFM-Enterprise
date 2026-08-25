class AccountingRepository:
    def __init__(self, db):
        self.db = db

    def list_accounts(self):
        return self.db.fetch_all(
            "SELECT * FROM accounts WHERE active=1 ORDER BY number"
        )

    def create_account(self, number, name, account_type):
        return self.db.execute(
            "INSERT INTO accounts(number,name,account_type) VALUES(?,?,?)",
            (number, name, account_type),
        )

    def get_account(self, account_id):
        return self.db.fetch_one("SELECT * FROM accounts WHERE id=?", (account_id,))

    def create_fiscal_year(self, year):
        return self.db.execute(
            "INSERT INTO fiscal_years(year) VALUES(?)", (year,)
        )

    def get_fiscal_year(self, year):
        return self.db.fetch_one("SELECT * FROM fiscal_years WHERE year=?", (year,))

    def list_fiscal_years(self):
        return self.db.fetch_all("SELECT * FROM fiscal_years ORDER BY year DESC")

    def create_period(self, fiscal_year_id, period_no, start_date, end_date):
        return self.db.execute(
            """INSERT INTO fiscal_periods
               (fiscal_year_id,period_no,start_date,end_date)
               VALUES(?,?,?,?)""",
            (fiscal_year_id, period_no, start_date, end_date),
        )

    def list_periods(self, fiscal_year_id):
        return self.db.fetch_all(
            "SELECT * FROM fiscal_periods WHERE fiscal_year_id=? ORDER BY period_no",
            (fiscal_year_id,),
        )

    def set_period_status(self, period_id, status):
        self.db.execute("UPDATE fiscal_periods SET status=? WHERE id=?", (status, period_id))

    def create_journal(self, journal_no, journal_date, description):
        return self.db.execute(
            "INSERT INTO journals(journal_no,journal_date,description) VALUES(?,?,?)",
            (journal_no, journal_date, description),
        )

    def add_line(self, journal_id, account_id, description, debit, credit, project_id=None):
        return self.db.execute(
            """INSERT INTO journal_lines
               (journal_id,account_id,description,debit,credit,project_id)
               VALUES(?,?,?,?,?,?)""",
            (journal_id, account_id, description, debit, credit, project_id),
        )

    def get_journal_lines(self, journal_id):
        return self.db.fetch_all(
            """SELECT jl.*, a.number, a.name
               FROM journal_lines jl
               JOIN accounts a ON a.id=jl.account_id
               WHERE jl.journal_id=? ORDER BY jl.id""",
            (journal_id,),
        )

    def next_journal_number(self, journal_type="FIN"):
        row = self.db.fetch_one(
            "SELECT next_number FROM journal_sequences WHERE journal_type=?",
            (journal_type,),
        )
        if row is None:
            self.db.execute(
                "INSERT INTO journal_sequences(journal_type,next_number) VALUES(?,?)",
                (journal_type, 2),
            )
            return 1
        number = row["next_number"]
        self.db.execute(
            "UPDATE journal_sequences SET next_number=? WHERE journal_type=?",
            (number + 1, journal_type),
        )
        return number

    def set_journal_status(self, journal_id, status):
        self.db.execute("UPDATE journals SET status=? WHERE id=?", (status, journal_id))

    def list_journals(self):
        return self.db.fetch_all(
            "SELECT * FROM journals ORDER BY journal_date DESC, journal_no DESC"
        )

    def trial_balance(self):
        return self.db.fetch_all(
            """SELECT a.number, a.name,
                      COALESCE(SUM(jl.debit),0) debit,
                      COALESCE(SUM(jl.credit),0) credit
               FROM accounts a
               LEFT JOIN journal_lines jl ON jl.account_id=a.id
               LEFT JOIN journals j ON j.id=jl.journal_id AND j.status='Posted'
               WHERE a.active=1
               GROUP BY a.id
               ORDER BY a.number"""
        )


def _unused(self):
    pass

def account_movements(self, account_id, start_date=None, end_date=None):
    sql = """
        SELECT j.journal_no, j.journal_date, j.description AS journal_description,
               jl.description, jl.debit, jl.credit,
               p.name AS project_name
        FROM journal_lines jl
        JOIN journals j ON j.id = jl.journal_id
        LEFT JOIN projects p ON p.id = jl.project_id
        WHERE jl.account_id=? AND j.status='Posted'
    """
    params = [account_id]
    if start_date:
        sql += " AND j.journal_date>=?"
        params.append(start_date)
    if end_date:
        sql += " AND j.journal_date<=?"
        params.append(end_date)
    sql += " ORDER BY j.journal_date, j.journal_no, jl.id"
    return self.db.fetch_all(sql, tuple(params))

def project_financials(self, project_id):
    return self.db.fetch_one(
        """SELECT
             COALESCE(SUM(jl.debit),0) debit,
             COALESCE(SUM(jl.credit),0) credit
           FROM journal_lines jl
           JOIN journals j ON j.id=jl.journal_id
           WHERE jl.project_id=? AND j.status='Posted'""",
        (project_id,)
    )


def project_actuals(self, project_id):
    return self.db.fetch_one(
        """SELECT
             COALESCE(SUM(jl.debit),0) debit,
             COALESCE(SUM(jl.credit),0) credit
           FROM journal_lines jl
           JOIN journals j ON j.id=jl.journal_id
           WHERE jl.project_id=? AND j.status='Posted'""",
        (project_id,)
    )
