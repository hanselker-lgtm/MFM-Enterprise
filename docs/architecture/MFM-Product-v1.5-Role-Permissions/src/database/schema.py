SCHEMA_VERSION = 1

def initialize_schema(db):
    statements = [
        """
        CREATE TABLE IF NOT EXISTS schema_migrations (
            version INTEGER PRIMARY KEY,
            applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS organization (
            id INTEGER PRIMARY KEY CHECK (id=1),
            name TEXT NOT NULL DEFAULT '',
            registration_no TEXT DEFAULT '',
            address TEXT DEFAULT '',
            postal_code TEXT DEFAULT '',
            city TEXT DEFAULT '',
            country TEXT DEFAULT '',
            email TEXT DEFAULT '',
            phone TEXT DEFAULT '',
            currency TEXT NOT NULL DEFAULT 'DKK',
            fiscal_year_start INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS app_settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL DEFAULT ''
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT DEFAULT ''
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS permissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            description TEXT DEFAULT ''
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS role_permissions (
            role_id INTEGER NOT NULL,
            permission_id INTEGER NOT NULL,
            PRIMARY KEY(role_id, permission_id),
            FOREIGN KEY(role_id) REFERENCES roles(id) ON DELETE CASCADE,
            FOREIGN KEY(permission_id) REFERENCES permissions(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            display_name TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            active INTEGER NOT NULL DEFAULT 1,
            role_id INTEGER NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(role_id) REFERENCES roles(id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_no TEXT NOT NULL UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT DEFAULT '',
            phone TEXT DEFAULT '',
            address TEXT DEFAULT '',
            postal_code TEXT DEFAULT '',
            city TEXT DEFAULT '',
            status TEXT NOT NULL DEFAULT 'Active',
            joined_date TEXT,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS membership_types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            annual_fee REAL NOT NULL DEFAULT 0,
            active INTEGER NOT NULL DEFAULT 1
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS memberships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            membership_type_id INTEGER NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT,
            status TEXT NOT NULL DEFAULT 'Active',
            FOREIGN KEY(member_id) REFERENCES members(id) ON DELETE CASCADE,
            FOREIGN KEY(membership_type_id) REFERENCES membership_types(id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS membership_invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            membership_id INTEGER NOT NULL,
            invoice_no INTEGER NOT NULL UNIQUE,
            invoice_date TEXT NOT NULL,
            due_date TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            journal_id INTEGER,
            FOREIGN KEY(member_id) REFERENCES members(id),
            FOREIGN KEY(membership_id) REFERENCES memberships(id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS membership_payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER NOT NULL,
            payment_date TEXT NOT NULL,
            amount REAL NOT NULL,
            journal_id INTEGER,
            status TEXT NOT NULL DEFAULT 'Registered',
            FOREIGN KEY(invoice_id) REFERENCES membership_invoices(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT DEFAULT '',
            status TEXT NOT NULL DEFAULT 'Planned',
            start_date TEXT,
            end_date TEXT,
            budget REAL NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            title TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            due_date TEXT,
            owner TEXT DEFAULT '',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE SET NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS risks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            title TEXT NOT NULL,
            severity TEXT NOT NULL DEFAULT 'Medium',
            status TEXT NOT NULL DEFAULT 'Open',
            owner TEXT DEFAULT '',
            mitigation TEXT DEFAULT '',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE SET NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            title TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending',
            decision_text TEXT DEFAULT '',
            owner TEXT DEFAULT '',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE SET NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS project_budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            budget_amount REAL NOT NULL DEFAULT 0,
            approved_at TEXT,
            status TEXT NOT NULL DEFAULT 'Draft',
            UNIQUE(project_id),
            FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS project_budget_lines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            budget_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL DEFAULT 0,
            FOREIGN KEY(budget_id) REFERENCES project_budgets(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS bank_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            account_number TEXT DEFAULT '',
            opening_balance REAL NOT NULL DEFAULT 0,
            active INTEGER NOT NULL DEFAULT 1
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS bank_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bank_account_id INTEGER NOT NULL,
            transaction_date TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT DEFAULT '',
            external_reference TEXT DEFAULT '',
            status TEXT NOT NULL DEFAULT 'Unmatched',
            journal_id INTEGER,
            FOREIGN KEY(bank_account_id) REFERENCES bank_accounts(id),
            FOREIGN KEY(journal_id) REFERENCES journals(id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS bank_matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bank_transaction_id INTEGER NOT NULL UNIQUE,
            journal_id INTEGER NOT NULL,
            matched_amount REAL NOT NULL,
            matched_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(bank_transaction_id) REFERENCES bank_transactions(id) ON DELETE CASCADE,
            FOREIGN KEY(journal_id) REFERENCES journals(id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            account_type TEXT NOT NULL,
            active INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS fiscal_years (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER NOT NULL UNIQUE,
            status TEXT NOT NULL DEFAULT 'Open',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS journals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            journal_no INTEGER NOT NULL UNIQUE,
            journal_date TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Draft',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS fiscal_periods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fiscal_year_id INTEGER NOT NULL,
            period_no INTEGER NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open',
            UNIQUE(fiscal_year_id, period_no),
            FOREIGN KEY(fiscal_year_id) REFERENCES fiscal_years(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS journal_sequences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            journal_type TEXT NOT NULL UNIQUE,
            next_number INTEGER NOT NULL DEFAULT 1
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS journal_lines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            journal_id INTEGER NOT NULL,
            account_id INTEGER NOT NULL,
            description TEXT DEFAULT '',
            debit REAL NOT NULL DEFAULT 0,
            credit REAL NOT NULL DEFAULT 0,
            project_id INTEGER,
            FOREIGN KEY(journal_id) REFERENCES journals(id) ON DELETE CASCADE,
            FOREIGN KEY(account_id) REFERENCES accounts(id),
            FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE SET NULL
        )
        """,
    ]
    db.transaction([(s, ()) for s in statements])
    existing = db.fetch_one("SELECT version FROM schema_migrations WHERE version=?", (SCHEMA_VERSION,))
    if existing is None:
        db.execute("INSERT INTO schema_migrations(version) VALUES (?)", (SCHEMA_VERSION,))
