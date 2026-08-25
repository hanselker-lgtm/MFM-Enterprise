class SearchService:
    def __init__(self, db):
        self.db = db

    def search(self, term, limit=50):
        term = term.strip()
        if not term:
            return []

        like = f"%{term}%"
        results = []

        queries = [
            ("Member", """
                SELECT id, member_no || ' — ' || first_name || ' ' || last_name AS title,
                       email AS detail
                FROM members
                WHERE member_no LIKE ? OR first_name LIKE ? OR last_name LIKE ? OR email LIKE ?
                LIMIT ?
            """, (like, like, like, like, limit)),
            ("Project", """
                SELECT id, name AS title, description AS detail
                FROM projects
                WHERE name LIKE ? OR description LIKE ?
                LIMIT ?
            """, (like, like, limit)),
            ("Task", """
                SELECT id, title, owner AS detail
                FROM tasks
                WHERE title LIKE ? OR owner LIKE ?
                LIMIT ?
            """, (like, like, limit)),
            ("Risk", """
                SELECT id, title, severity || ' — ' || status AS detail
                FROM risks
                WHERE title LIKE ? OR owner LIKE ? OR mitigation LIKE ?
                LIMIT ?
            """, (like, like, like, limit)),
            ("Decision", """
                SELECT id, title, status AS detail
                FROM decisions
                WHERE title LIKE ? OR decision_text LIKE ? OR owner LIKE ?
                LIMIT ?
            """, (like, like, like, limit)),
            ("Account", """
                SELECT id, number || ' — ' || name AS title, account_type AS detail
                FROM accounts
                WHERE number LIKE ? OR name LIKE ?
                LIMIT ?
            """, (like, like, limit)),
            ("Journal", """
                SELECT id, 'Journal #' || journal_no AS title, description AS detail
                FROM journals
                WHERE description LIKE ? OR CAST(journal_no AS TEXT) LIKE ?
                LIMIT ?
            """, (like, like, limit)),
            ("Invoice", """
                SELECT id, 'Invoice #' || invoice_no AS title, status AS detail
                FROM membership_invoices
                WHERE CAST(invoice_no AS TEXT) LIKE ? OR status LIKE ?
                LIMIT ?
            """, (like, like, limit)),
        ]

        for entity, sql, params in queries:
            for row in self.db.fetch_all(sql, params):
                results.append({
                    "entity": entity,
                    "id": row["id"],
                    "title": row["title"],
                    "detail": row["detail"] or "",
                })

        return results[:limit]
