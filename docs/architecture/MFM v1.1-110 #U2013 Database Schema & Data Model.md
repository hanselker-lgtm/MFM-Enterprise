# MFM v1.1-110 – Database Schema & Data Model

Version: 1.1

Document ID: MFM-v1.1-110

Status: Technical Implementation

---

# 1. Purpose

This document defines the physical database architecture for MaritimForeningsManager (MFM) v1.1.

The database model implements the functional architecture established in MFM v1.0 and the software architecture defined in MFM v1.1-100.

The objectives are:

- Data integrity
- Performance
- Maintainability
- Auditability
- Simplicity

SQLite remains the default database platform.

---

# 2. Design Principles

The database shall follow these principles:

- One authoritative table for each business entity
- No duplicated business data
- Strong referential integrity
- Surrogate primary keys (INTEGER AUTOINCREMENT)
- Business UUID for external references
- Foreign key enforcement enabled
- Soft deletion where appropriate
- Audit fields on every business table

---

# 3. Overall Database Architecture

```
+-----------------------------------------------------------+
|                       SQLite Database                     |
+-----------------------------------------------------------+

Membership
Projects
Grants
Accounting
Documents
Reporting
Security
Administration
Audit

+-----------------------------------------------------------+
```

Each module owns its own tables.

Modules communicate through foreign keys—not duplicated data.

---

# 4. Naming Standards

Tables

```
members
projects
grants
documents
accounts
journal_entries
```

Primary Keys

```
member_id
project_id
grant_id
document_id
```

Foreign Keys

```
member_id
project_id
grant_id
```

Indexes

```
idx_members_name
idx_projects_status
idx_documents_reference
```

---

# 5. Common Base Columns

Every business table contains:

```
id INTEGER PRIMARY KEY AUTOINCREMENT

uuid TEXT UNIQUE NOT NULL

created_at DATETIME

created_by INTEGER

updated_at DATETIME

updated_by INTEGER

is_active BOOLEAN

is_deleted BOOLEAN
```

These fields provide:

- Traceability
- Soft delete
- Synchronisation support
- Future API compatibility

---

# 6. Membership Module

## Table: members

```
member_id

member_number

first_name

last_name

address

postal_code

city

country

email

phone

birth_date

membership_type

membership_status

join_date

leave_date

notes
```

Indexes

```
email

member_number

last_name
```

---

## Table: membership_categories

Stores:

- Active
- Passive
- Honorary
- Family

---

## Table: membership_payments

Stores:

```
payment_date

amount

accounting_reference

member_id
```

Accounting transactions are referenced—not duplicated.

---

# 7. Accounting Module

## Table: chart_of_accounts

```
account_id

account_number

account_name

account_type

vat_code

active
```

---

## Table: journal_entries

```
journal_id

voucher_number

voucher_date

description

posted_by

posted_date
```

---

## Table: journal_lines

```
line_id

journal_id

account_id

debit

credit

project_id

member_id

grant_id
```

Double-entry bookkeeping is enforced.

---

# 8. Project Module

## Table: projects

```
project_id

project_number

project_name

description

status

start_date

end_date

manager_id

budget_amount
```

Projects never store accounting balances.

---

## Table: project_milestones

Stores:

- Title
- Description
- Due Date
- Completed
- Responsible User

---

# 9. Grant Module

## Table: grants

```
grant_id

grant_name

organisation

application_date

requested_amount

approved_amount

status

project_id
```

Requested amount and approved amount remain separate.

---

## Table: grant_reports

Stores reporting obligations.

---

# 10. Document Module

## Table: documents

```
document_id

document_uuid

title

filename

storage_path

mime_type

file_size

checksum

version

status
```

---

## Table: document_links

```
document_id

entity_type

entity_id
```

One document.

Many business references.

---

# 11. Security Module

## Table: users

```
user_id

username

password_hash

email

role_id

active
```

---

## Table: roles

Stores:

- Administrator
- Chairman
- Treasurer
- Secretary
- Project Manager
- Member Administrator
- Auditor

---

## Table: permissions

Stores every application permission.

---

## Table: role_permissions

Many-to-many relationship.

---

# 12. Audit Module

## Table: audit_log

```
audit_id

timestamp

user_id

module

entity

action

old_value

new_value

ip_address
```

Audit records are immutable.

---

# 13. Administration Module

Stores:

- System Parameters
- Number Series
- Email Configuration
- Backup Configuration
- Report Configuration

---

# 14. Reporting Module

Reporting owns no business data.

Optional cache tables:

```
dashboard_cache

report_cache
```

Cache can always be regenerated.

---

# 15. Relationships

```
Member

↓

Projects

↓

Grants

↓

Accounting

↓

Documents

↓

Reporting
```

Every relationship is implemented through foreign keys.

---

# 16. Constraints

Examples:

```
Debit >= 0

Credit >= 0

Approved Amount >= 0

Project End >= Project Start

Email UNIQUE

Member Number UNIQUE
```

Database constraints complement business validation.

---

# 17. Index Strategy

Indexes:

```
Members

Projects

Documents

Voucher Number

Account Number

Grant Status

Project Status
```

Indexes are created only where beneficial.

---

# 18. Views

Useful database views:

```
vw_member_overview

vw_project_budget

vw_grant_status

vw_account_balance

vw_dashboard
```

Views are read-only.

---

# 19. Transactions

Every Service controls transactions.

Pattern:

```
BEGIN

↓

Validation

↓

Repository

↓

COMMIT

↓

Audit
```

Rollback occurs automatically on failure.

---

# 20. Migration Strategy

Database migrations shall:

- Never destroy data
- Be version controlled
- Support rollback
- Be repeatable
- Be idempotent where possible

Migration history is stored.

---

# 21. Backup Compatibility

Database schema supports:

- Full backup
- Incremental backup
- Schema validation
- Restore verification

---

# 22. Performance Targets

Target database sizes:

Members

10,000+

Projects

5,000+

Documents

100,000+

Accounting Lines

500,000+

Expected performance:

Typical searches below 100 ms.

---

# 23. Future Database Support

Repository abstraction allows migration to:

- PostgreSQL
- SQL Server
- MariaDB

No business logic changes required.

---

# 24. Database Governance

Only Repository classes may execute SQL.

GUI never accesses the database directly.

Business rules remain inside Services.

This separation is mandatory.

---

# 25. Summary

The MFM v1.1 database schema establishes a robust, normalized and maintainable relational data model for the application.

The schema preserves the architectural principles established throughout the MFM project by ensuring:

- Single source of truth
- Strong referential integrity
- Separation of concerns
- High auditability
- Excellent maintainability

The Repository layer isolates the database implementation from the business logic, allowing future database technologies to be adopted without affecting the application architecture.

---

# Next Document

**MFM v1.1-120 – Service Layer Architecture & Business Services**

---

# END OF DOCUMENT