class OrganizationService:
    def __init__(self, db):
        self.db = db

    def get(self):
        return self.db.fetch_one("SELECT * FROM organization WHERE id=1")

    def save(self, name, registration_no="", address="", postal_code="",
             city="", country="Denmark", email="", phone="", currency="DKK",
             fiscal_year_start=1):
        name = name.strip()
        if not name:
            raise ValueError("Organization name is required.")
        self.db.execute(
            """INSERT INTO organization
               (id,name,registration_no,address,postal_code,city,country,email,phone,currency,fiscal_year_start)
               VALUES(1,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(id) DO UPDATE SET
                 name=excluded.name,
                 registration_no=excluded.registration_no,
                 address=excluded.address,
                 postal_code=excluded.postal_code,
                 city=excluded.city,
                 country=excluded.country,
                 email=excluded.email,
                 phone=excluded.phone,
                 currency=excluded.currency,
                 fiscal_year_start=excluded.fiscal_year_start""",
            (name, registration_no.strip(), address.strip(), postal_code.strip(),
             city.strip(), country.strip(), email.strip(), phone.strip(),
             currency.strip().upper(), int(fiscal_year_start))
        )
        return self.get()
