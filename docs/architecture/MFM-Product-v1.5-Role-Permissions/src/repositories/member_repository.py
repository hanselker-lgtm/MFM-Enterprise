class MemberRepository:
    def __init__(self, db):
        self.db = db

    def list_members(self):
        return self.db.fetch_all("SELECT * FROM members ORDER BY last_name, first_name")

    def create_member(self, member_no, first_name, last_name, email="", phone="",
                      address="", postal_code="", city="", joined_date=None):
        return self.db.execute(
            """INSERT INTO members
               (member_no,first_name,last_name,email,phone,address,postal_code,city,joined_date)
               VALUES(?,?,?,?,?,?,?,?,?)""",
            (member_no, first_name, last_name, email, phone, address, postal_code, city, joined_date)
        )

    def list_membership_types(self):
        return self.db.fetch_all(
            "SELECT * FROM membership_types WHERE active=1 ORDER BY name"
        )

    def create_membership_type(self, name, annual_fee):
        return self.db.execute(
            "INSERT INTO membership_types(name,annual_fee) VALUES(?,?)",
            (name, annual_fee)
        )

    def create_membership(self, member_id, membership_type_id, start_date, end_date=None):
        return self.db.execute(
            """INSERT INTO memberships(member_id,membership_type_id,start_date,end_date)
               VALUES(?,?,?,?)""",
            (member_id, membership_type_id, start_date, end_date)
        )

    def list_memberships(self):
        return self.db.fetch_all(
            """SELECT m.id, m.member_no, m.first_name, m.last_name,
                      mt.name membership_type, mt.annual_fee,
                      ms.start_date, ms.end_date, ms.status
               FROM memberships ms
               JOIN members m ON m.id=ms.member_id
               JOIN membership_types mt ON mt.id=ms.membership_type_id
               ORDER BY m.last_name, m.first_name"""
        )

    def next_invoice_number(self):
        row = self.db.fetch_one(
            "SELECT COALESCE(MAX(invoice_no),0)+1 n FROM membership_invoices"
        )
        return row["n"]

    def create_invoice(self, member_id, membership_id, invoice_no,
                       invoice_date, due_date, amount):
        return self.db.execute(
            """INSERT INTO membership_invoices
               (member_id,membership_id,invoice_no,invoice_date,due_date,amount)
               VALUES(?,?,?,?,?,?)""",
            (member_id, membership_id, invoice_no, invoice_date, due_date, amount)
        )

    def list_invoices(self):
        return self.db.fetch_all(
            """SELECT i.*, m.member_no, m.first_name, m.last_name
               FROM membership_invoices i
               JOIN members m ON m.id=i.member_id
               ORDER BY i.invoice_date DESC, i.invoice_no DESC"""
        )


def get_invoice(self, invoice_id):
    return self.db.fetch_one(
        "SELECT * FROM membership_invoices WHERE id=?", (invoice_id,)
    )

def register_payment(self, invoice_id, payment_date, amount, journal_id=None):
    return self.db.execute(
        """INSERT INTO membership_payments
           (invoice_id,payment_date,amount,journal_id)
           VALUES(?,?,?,?)""",
        (invoice_id, payment_date, amount, journal_id)
    )

def invoice_paid_amount(self, invoice_id):
    row = self.db.fetch_one(
        "SELECT COALESCE(SUM(amount),0) amount FROM membership_payments WHERE invoice_id=?",
        (invoice_id,)
    )
    return float(row["amount"] or 0)

def update_invoice_status(self, invoice_id, status):
    self.db.execute(
        "UPDATE membership_invoices SET status=? WHERE id=?",
        (status, invoice_id)
    )

def list_payments(self):
    return self.db.fetch_all(
        """SELECT p.*, i.invoice_no, m.member_no, m.first_name, m.last_name
           FROM membership_payments p
           JOIN membership_invoices i ON i.id=p.invoice_id
           JOIN members m ON m.id=i.member_id
           ORDER BY p.payment_date DESC, p.id DESC"""
    )
