# MFM v1.0 DATABASE FOUNDATION

## MaritimForeningsManager — Database- og persistensbaseline

**Version:** 1.0  
**Status:** Development Baseline  
**Parent:** MFM v1.0 Architecture Baseline  
**Database:** SQLite  
**Target:** Windows desktop application  
**Purpose:** Establish the complete, practical database foundation for MFM v1.0

---

# 1. Purpose

This document defines the database foundation for MFM v1.0.

The database SHALL provide a reliable foundation for:

- members;
- memberships;
- membership fees;
- users and roles;
- chart of accounts;
- accounting periods;
- vouchers;
- voucher lines;
- bank transactions;
- reconciliations;
- budgets;
- projects;
- grants;
- assets;
- documents;
- audit events;
- settings;
- backups.

The database SHALL remain deliberately simple.

MFM v1.0 is a desktop application for an almennyttig association. SQLite is therefore the selected persistence technology.

---

# 2. Architectural Principles

## 2.1 Single Authoritative Database

The SQLite database SHALL be the authoritative source for structured MFM data.

## 2.2 Files Are Separate

Documents SHALL remain files. The database stores metadata and references.

## 2.3 No Duplicate Financial Truth

Reports, dashboards and exports SHALL derive from the database.

## 2.4 Transaction Integrity

Financial changes SHALL use database transactions.

## 2.5 Foreign-Key Integrity

Foreign keys SHALL be enabled.

## 2.6 Auditability

Material changes SHALL be traceable.

## 2.7 Migration Safety

Schema changes SHALL be versioned.

## 2.8 Recoverability

The database SHALL be backupable and restorable.

---

# 3. Logical Database Architecture

```text
                    MFM DATABASE
                         |
       +-----------------+------------------+
       |                 |                  |
   IDENTITY          MEMBERSHIP         FINANCE
       |                 |                  |
 users / roles      members             accounts
                    memberships          periods
                    fees                 vouchers
                                         voucher_lines
                                         bank
                                         budgets
       |                 |                  |
       +-----------------+------------------+
                         |
                      PROJECTS
                         |
                 projects / grants
                         |
                      ASSETS
                         |
                     DOCUMENTS
                         |
                       AUDIT
                         |
                    SETTINGS
                         |
                     BACKUPS
```

---

# 4. Naming Conventions

Tables SHALL use lowercase snake_case.

Examples:

```text
members
membership_fees
voucher_lines
audit_events
```

Primary keys SHALL normally be:

```text
id INTEGER PRIMARY KEY
```

Foreign keys SHALL use:

```text
<entity>_id
```

Examples:

```text
member_id
project_id
account_id
voucher_id
```

---

# 5. Core Tables

The minimum schema consists of:

```text
users
roles
user_roles

members
memberships
membership_fees

accounts
accounting_periods
vouchers
voucher_lines

bank_transactions
bank_reconciliations

budgets
budget_lines

projects
project_transactions

grants
grant_payments

assets

documents

audit_events

settings
backup_records

schema_migrations
```

---

# 6. Users

Table:

```text
users
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| username | TEXT | UNIQUE, NOT NULL |
| password_hash | TEXT | NOT NULL |
| display_name | TEXT | NOT NULL |
| email | TEXT | Optional |
| is_active | INTEGER | NOT NULL |
| created_at | TEXT | NOT NULL |
| updated_at | TEXT | NOT NULL |

Passwords SHALL never be stored as plaintext.

---

# 7. Roles

Table:

```text
roles
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| name | TEXT | UNIQUE |
| description | TEXT | Optional |

Initial roles:

```text
ADMIN
TREASURER
ACCOUNTANT
BOARD_USER
READ_ONLY
```

---

# 8. User Roles

Table:

```text
user_roles
```

Fields:

| Field | Type | Rule |
|---|---|---|
| user_id | INTEGER | FK users |
| role_id | INTEGER | FK roles |

Primary key:

```text
(user_id, role_id)
```

---

# 9. Members

Table:

```text
members
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| member_number | TEXT | UNIQUE |
| first_name | TEXT | NOT NULL |
| last_name | TEXT | NOT NULL |
| address | TEXT | Optional |
| postal_code | TEXT | Optional |
| city | TEXT | Optional |
| phone | TEXT | Optional |
| email | TEXT | Optional |
| join_date | TEXT | Optional |
| leave_date | TEXT | Optional |
| status | TEXT | NOT NULL |
| notes | TEXT | Optional |
| created_at | TEXT | NOT NULL |
| updated_at | TEXT | NOT NULL |

Member status:

```text
ACTIVE
INACTIVE
PENDING
LEFT
```

---

# 10. Memberships

Table:

```text
memberships
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| member_id | INTEGER | FK |
| membership_type | TEXT | NOT NULL |
| start_date | TEXT | NOT NULL |
| end_date | TEXT | Optional |
| status | TEXT | NOT NULL |
| notes | TEXT | Optional |

A member MAY have historical memberships.

---

# 11. Membership Fees

Table:

```text
membership_fees
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| membership_id | INTEGER | FK |
| financial_year | INTEGER | NOT NULL |
| amount | NUMERIC | NOT NULL |
| due_date | TEXT | NOT NULL |
| status | TEXT | NOT NULL |
| voucher_id | INTEGER | Optional FK |
| created_at | TEXT | NOT NULL |

Fee status:

```text
OPEN
PARTIAL
PAID
CANCELLED
```

---

# 12. Accounts

Table:

```text
accounts
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| account_number | TEXT | UNIQUE |
| name | TEXT | NOT NULL |
| account_type | TEXT | NOT NULL |
| parent_id | INTEGER | Optional FK |
| is_active | INTEGER | NOT NULL |
| vat_code | TEXT | Optional |
| report_group | TEXT | Optional |
| created_at | TEXT | NOT NULL |
| updated_at | TEXT | NOT NULL |

Account types:

```text
ASSET
LIABILITY
EQUITY
INCOME
EXPENSE
```

---

# 13. Accounting Periods

Table:

```text
accounting_periods
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| year | INTEGER | NOT NULL |
| period_number | INTEGER | NOT NULL |
| start_date | TEXT | NOT NULL |
| end_date | TEXT | NOT NULL |
| status | TEXT | NOT NULL |

Status:

```text
OPEN
CLOSED
LOCKED
```

A closed period SHALL prevent ordinary posting.

---

# 14. Vouchers

Table:

```text
vouchers
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| voucher_number | TEXT | UNIQUE |
| voucher_date | TEXT | NOT NULL |
| description | TEXT | NOT NULL |
| period_id | INTEGER | FK |
| status | TEXT | NOT NULL |
| source | TEXT | Optional |
| reference | TEXT | Optional |
| created_by | INTEGER | FK users |
| posted_at | TEXT | Optional |
| created_at | TEXT | NOT NULL |

Voucher status:

```text
DRAFT
POSTED
REVERSED
```

---

# 15. Voucher Lines

Table:

```text
voucher_lines
```

Fields:

| Field | Type | Rule |
|---|---|---|
| id | INTEGER | PK |
| voucher_id | INTEGER | FK |
| line_number | INTEGER | NOT NULL |
| account_id | INTEGER | FK |
| project_id | INTEGER | Optional FK |
| description | TEXT | Optional |
| debit | NUMERIC | NOT NULL |
| credit | NUMERIC | NOT NULL |

Rules:

```text
debit >= 0
credit >= 0
```

A line SHALL normally contain either debit or credit.

A posted voucher SHALL satisfy:

```text
SUM(debit) = SUM(credit)
```

---

# 16. Accounting Integrity

The application service layer SHALL validate:

```text
TOTAL DEBIT
=
TOTAL CREDIT
```

before posting.

SQLite triggers MAY provide additional protection, but business validation SHALL remain in the accounting service.

---

# 17. Voucher Immutability

Once:

```text
status = POSTED
```

the voucher SHALL not be silently edited.

Correction SHALL use a reversal.

Example:

```text
ORIGINAL VOUCHER
      ↓
REVERSAL VOUCHER
      ↓
CORRECTED VOUCHER
```

---

# 18. Bank Transactions

Table:

```text
bank_transactions
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| transaction_date | TEXT |
| value_date | TEXT |
| description | TEXT |
| amount | NUMERIC |
| balance | NUMERIC |
| external_reference | TEXT |
| imported_at | TEXT |
| matched_voucher_id | INTEGER FK |
| reconciliation_status | TEXT |

Status:

```text
UNMATCHED
MATCHED
RECONCILED
IGNORED
```

---

# 19. Bank Reconciliation

Table:

```text
bank_reconciliations
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| reconciliation_date | TEXT |
| statement_balance | NUMERIC |
| book_balance | NUMERIC |
| difference | NUMERIC |
| status | TEXT |
| completed_by | INTEGER FK |
| completed_at | TEXT |

---

# 20. Budgets

Table:

```text
budgets
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| name | TEXT |
| financial_year | INTEGER |
| status | TEXT |
| created_by | INTEGER FK |
| created_at | TEXT |

---

# 21. Budget Lines

Table:

```text
budget_lines
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| budget_id | INTEGER FK |
| account_id | INTEGER FK |
| project_id | INTEGER FK |
| amount | NUMERIC |
| notes | TEXT |

Project_id MAY be NULL for general association budget lines.

---

# 22. Projects

Table:

```text
projects
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| project_number | TEXT UNIQUE |
| name | TEXT NOT NULL |
| description | TEXT |
| start_date | TEXT |
| end_date | TEXT |
| budget_amount | NUMERIC |
| status | TEXT |
| responsible_user_id | INTEGER FK |
| created_at | TEXT |
| updated_at | TEXT |

Status:

```text
PLANNED
ACTIVE
PAUSED
COMPLETED
CANCELLED
```

---

# 23. Project Transactions

Table:

```text
project_transactions
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| project_id | INTEGER FK |
| voucher_line_id | INTEGER FK |
| amount | NUMERIC |
| transaction_type | TEXT |

Project accounting SHOULD normally derive from voucher lines rather than creating a second financial ledger.

This table is therefore optional and SHALL only be used if a specific project workflow requires it.

---

# 24. Grants

Table:

```text
grants
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| project_id | INTEGER FK |
| funder | TEXT |
| application_date | TEXT |
| deadline | TEXT |
| requested_amount | NUMERIC |
| approved_amount | NUMERIC |
| status | TEXT |
| reporting_deadline | TEXT |
| notes | TEXT |

Status:

```text
PLANNED
PREPARING
SUBMITTED
APPROVED
REJECTED
COMPLETED
```

---

# 25. Grant Payments

Table:

```text
grant_payments
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| grant_id | INTEGER FK |
| payment_date | TEXT |
| amount | NUMERIC |
| voucher_id | INTEGER FK |
| reference | TEXT |

---

# 26. Assets

Table:

```text
assets
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| asset_number | TEXT UNIQUE |
| name | TEXT |
| acquisition_date | TEXT |
| acquisition_value | NUMERIC |
| current_value | NUMERIC |
| location | TEXT |
| responsible_user_id | INTEGER FK |
| status | TEXT |
| notes | TEXT |

Status:

```text
ACTIVE
MAINTENANCE
DISPOSED
LOST
```

---

# 27. Documents

Table:

```text
documents
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| file_name | TEXT |
| storage_path | TEXT |
| document_type | TEXT |
| entity_type | TEXT |
| entity_id | INTEGER |
| checksum | TEXT |
| file_size | INTEGER |
| created_by | INTEGER FK |
| created_at | TEXT |

Documents SHALL not be stored as arbitrary binary blobs inside ordinary application tables unless a specific requirement justifies it.

---

# 28. Audit Events

Table:

```text
audit_events
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| user_id | INTEGER FK |
| event_type | TEXT |
| entity_type | TEXT |
| entity_id | INTEGER |
| old_value | TEXT |
| new_value | TEXT |
| description | TEXT |
| created_at | TEXT |

Audit events SHALL be append-oriented.

---

# 29. Settings

Table:

```text
settings
```

Fields:

| Field | Type |
|---|---|
| key | TEXT PK |
| value | TEXT |
| value_type | TEXT |
| description | TEXT |
| updated_at | TEXT |

Examples:

```text
association.name
association.address
financial.default_year
backup.directory
documents.directory
```

---

# 30. Backup Records

Table:

```text
backup_records
```

Fields:

| Field | Type |
|---|---|
| id | INTEGER PK |
| backup_date | TEXT |
| file_path | TEXT |
| file_size | INTEGER |
| checksum | TEXT |
| backup_type | TEXT |
| status | TEXT |
| verified_at | TEXT |

---

# 31. Schema Migrations

Table:

```text
schema_migrations
```

Fields:

| Field | Type |
|---|---|
| version | INTEGER PK |
| description | TEXT |
| applied_at | TEXT |

The application SHALL never rely on an undocumented database structure.

---

# 32. Foreign-Key Rules

Recommended defaults:

```text
ON DELETE RESTRICT
```

for financial records.

Where historical relationships must remain:

```text
ON DELETE RESTRICT
```

is preferred over cascading deletion.

Cascading delete SHALL NOT be used for posted financial history.

---

# 33. Indexes

Minimum indexes:

```text
members.member_number
members.email
members.status

accounts.account_number
accounts.account_type

vouchers.voucher_number
vouchers.voucher_date
vouchers.period_id
vouchers.status

voucher_lines.voucher_id
voucher_lines.account_id
voucher_lines.project_id

bank_transactions.transaction_date
bank_transactions.external_reference

projects.project_number
projects.status

documents.entity_type
documents.entity_id

audit_events.entity_type
audit_events.entity_id
audit_events.created_at
```

---

# 34. Database Connection

A single database access module SHALL control connection creation.

Recommended responsibilities:

```text
get_connection()
initialize_database()
enable_foreign_keys()
begin_transaction()
commit()
rollback()
close()
```

The GUI SHALL not create arbitrary database connections.

---

# 35. SQLite Configuration

At connection startup:

```sql
PRAGMA foreign_keys = ON;
```

Where appropriate:

```sql
PRAGMA journal_mode = WAL;
```

WAL SHALL only be used if it provides a clear benefit for the deployment environment.

---

# 36. Transaction Management

Application services SHALL use:

```text
BEGIN
  operation
  audit
COMMIT
```

On failure:

```text
ROLLBACK
```

A service SHALL not partially commit a financial operation.

---

# 37. Database Initialisation

Startup sequence:

```text
OPEN DATABASE
 ↓
ENABLE FOREIGN KEYS
 ↓
CHECK SCHEMA VERSION
 ↓
RUN MIGRATIONS
 ↓
VERIFY REQUIRED TABLES
 ↓
VERIFY DEFAULT DATA
 ↓
START APPLICATION
```

If migration fails, the application SHALL not continue as if the database were valid.

---

# 38. Initial Seed Data

Initial seed data SHOULD include:

### Roles

```text
ADMIN
TREASURER
ACCOUNTANT
BOARD_USER
READ_ONLY
```

### Account types

```text
ASSET
LIABILITY
EQUITY
INCOME
EXPENSE
```

No association-specific account numbers SHALL be hard-coded unless explicitly configured.

---

# 39. Financial Year

Financial year SHALL be configurable.

Default:

```text
01-01 → 31-12
```

The architecture SHOULD permit other periods later without redesigning the core accounting model.

---

# 40. Decimal Handling

Financial values SHALL be handled carefully.

Python business logic SHOULD use:

```text
Decimal
```

rather than binary floating-point for financial calculations.

SQLite storage SHALL use a consistent representation.

The implementation SHALL define one canonical monetary representation and use it consistently.

---

# 41. Date Handling

Dates SHALL use ISO representation:

```text
YYYY-MM-DD
```

Timestamps SHOULD use:

```text
YYYY-MM-DD HH:MM:SS
```

The application SHALL centralise date handling.

---

# 42. Null Handling

NULL SHALL mean:

```text
unknown
not applicable
not provided
```

Empty strings SHALL not be used as a substitute for NULL where the distinction matters.

---

# 43. Unique Constraints

Unique constraints SHALL protect:

- username;
- member number;
- account number;
- voucher number;
- project number;
- asset number;
- settings key.

External references SHOULD be unique where the source system guarantees uniqueness.

---

# 44. Data Validation at Database Level

Database constraints SHOULD protect:

- required fields;
- uniqueness;
- foreign keys;
- basic numeric validity.

Business rules SHALL remain in application services.

---

# 45. Database Validation at Application Level

The service layer SHALL validate:

- balanced vouchers;
- closed periods;
- membership rules;
- project status;
- grant status;
- role permissions;
- accounting rules;
- document relationships.

---

# 46. Audit Strategy

Audit events SHALL be generated by services rather than GUI widgets.

Example:

```text
AccountingService.post_voucher()
       ↓
Database transaction
       ↓
Voucher written
       ↓
Audit event written
       ↓
COMMIT
```

---

# 47. Deletion Policy

## Members

Members SHOULD normally be deactivated rather than deleted.

## Accounts

Accounts used historically SHALL be deactivated rather than deleted.

## Vouchers

Posted vouchers SHALL not be deleted.

## Projects

Projects with financial history SHALL not be deleted.

## Documents

Documents SHALL require controlled deletion.

## Audit Events

Audit events SHALL not be deleted through ordinary application functions.

---

# 48. Soft Deactivation

Where historical relationships matter, use:

```text
is_active
```

or a status field.

This preserves historical reporting.

---

# 49. Referential Integrity Example

A posted voucher line references:

```text
voucher
account
project
```

Those entities SHALL remain available for historical interpretation.

Therefore:

```text
DELETE account
```

SHALL be blocked if historical voucher lines reference it.

The account may instead become inactive.

---

# 50. Database Backup

Backup SHALL produce a consistent database snapshot.

Preferred process:

```text
CHECK DATABASE
 ↓
CREATE CONSISTENT BACKUP
 ↓
CALCULATE CHECKSUM
 ↓
STORE BACKUP RECORD
 ↓
VERIFY BACKUP
```

---

# 51. Restore

Restore process:

```text
SELECT BACKUP
 ↓
VERIFY CHECKSUM
 ↓
RESTORE TO SAFE LOCATION
 ↓
OPEN DATABASE
 ↓
RUN INTEGRITY CHECK
 ↓
VERIFY SCHEMA
 ↓
VERIFY FINANCIAL DATA
 ↓
ACTIVATE
```

---

# 52. SQLite Integrity Check

Recovery SHALL use:

```sql
PRAGMA integrity_check;
```

A failed integrity check SHALL prevent normal activation of the restored database until investigated.

---

# 53. Data Export

Minimum database exports:

```text
members.csv
accounts.csv
vouchers.csv
voucher_lines.csv
projects.csv
grants.csv
assets.csv
audit_events.csv
```

Full application backup SHALL additionally contain documents.

---

# 54. Database Security

The SQLite file SHALL be protected by operating-system permissions.

The application data directory SHOULD not be exposed unnecessarily.

Sensitive exports SHALL be treated as confidential.

---

# 55. Document Storage

Recommended:

```text
MFM/
├── data/
│   └── mfm.db
├── documents/
│   ├── members/
│   ├── projects/
│   ├── grants/
│   └── vouchers/
├── backups/
└── exports/
```

The exact path SHALL be configurable.

---

# 56. Document Integrity

For important documents, SHA-256 checksum SHOULD be stored.

On retrieval:

```text
FILE
 ↓
CHECKSUM
 ↓
COMPARE
 ↓
VALID / MODIFIED
```

---

# 57. Database Test Data

Development test data SHALL be clearly separated from production data.

Recommended:

```text
tests/
fixtures/
```

Test database:

```text
mfm_test.db
```

Production database:

```text
mfm.db
```

---

# 58. Database Unit Tests

Minimum:

1. database initialisation;
2. migration;
3. foreign keys;
4. member insert;
5. account insert;
6. voucher insert;
7. voucher balance;
8. project relationship;
9. audit event;
10. backup record.

---

# 59. Accounting Database Tests

Test:

```text
balanced voucher → accepted
unbalanced voucher → rejected
missing account → rejected
closed period → rejected
posted voucher mutation → rejected
reversal → accepted
duplicate voucher number → rejected
```

---

# 60. Membership Database Tests

Test:

```text
member creation
membership creation
fee creation
fee status
historical membership
member deactivation
```

---

# 61. Project Database Tests

Test:

```text
project creation
project budget
project-linked voucher
project report query
project completion
historical project preservation
```

---

# 62. Grant Database Tests

Test:

```text
grant creation
project relationship
requested amount
approved amount
payment
reporting deadline
status transition
```

---

# 63. Audit Database Tests

Every material service operation SHOULD verify:

```text
action occurred
audit event exists
user identified
entity identified
timestamp exists
```

---

# 64. Migration Strategy

Migration files SHOULD be numbered:

```text
001_initial_schema
002_add_membership
003_add_projects
004_add_grants
005_add_audit
```

Each migration SHALL be:

- deterministic;
- documented;
- testable;
- applied once.

---

# 65. Migration Safety

Before migration:

```text
BACKUP
```

Then:

```text
MIGRATE
 ↓
VERIFY
 ↓
TEST
```

If migration fails, restore from backup or use a controlled rollback strategy.

---

# 66. Schema Version

Application startup SHALL compare:

```text
APPLICATION EXPECTED SCHEMA
vs
DATABASE SCHEMA
```

An incompatible schema SHALL produce a clear error.

---

# 67. Repository Boundaries

Repositories SHALL be responsible for persistence operations.

Examples:

```text
MemberRepository
AccountRepository
VoucherRepository
ProjectRepository
GrantRepository
DocumentRepository
AuditRepository
```

Repositories SHALL not contain GUI logic.

---

# 68. Service Boundaries

Services SHALL coordinate:

```text
validation
business rules
repositories
transactions
audit
```

Example:

```text
AccountingService
 ├── validate voucher
 ├── verify period
 ├── verify permissions
 ├── save voucher
 ├── save lines
 ├── audit
 └── commit
```

---

# 69. Reporting Queries

Reports SHALL use read-oriented queries.

Reports SHALL not modify financial data.

---

# 70. Database Performance

For expected association scale:

```text
SQLite
+
proper indexes
+
reasonable queries
```

is sufficient.

Premature optimisation SHALL be avoided.

---

# 71. Concurrency

MFM v1.0 is desktop-first.

If multiple-user concurrent database access becomes necessary later, the architecture SHALL be reviewed before moving to a network database.

SQLite SHALL not be forced into a multi-user architecture beyond its practical limits.

---

# 72. Database Logging

Database errors SHALL be logged with:

- timestamp;
- operation;
- exception type;
- relevant entity;
- user where available.

Passwords and sensitive credentials SHALL never be logged.

---

# 73. Failure Handling

Database unavailable:

```text
SHOW USER MESSAGE
LOG ERROR
DO NOT CONTINUE FINANCIAL WRITE
```

Transaction failure:

```text
ROLLBACK
LOG
SHOW ERROR
```

Corrupt database:

```text
STOP
BACKUP CURRENT FILE
RUN INTEGRITY CHECK
RECOVER
```

---

# 74. Database Health

MFM SHOULD expose:

- database path;
- schema version;
- database size;
- last backup;
- last successful integrity check;
- document directory;
- available storage.

---

# 75. Database Maintenance

Periodic maintenance MAY include:

- integrity check;
- backup;
- index review;
- obsolete temporary-file cleanup;
- document consistency check.

Maintenance SHALL not modify financial history.

---

# 76. Database Acceptance Criteria

The database foundation is accepted when:

- all required tables exist;
- foreign keys are enabled;
- migrations work;
- users and roles work;
- members work;
- memberships work;
- accounts work;
- periods work;
- vouchers work;
- voucher lines work;
- double-entry integrity works;
- projects work;
- grants work;
- documents work;
- audit works;
- backup works;
- restore works;
- export works;
- integrity checks work;
- production and test databases are separated.

---

# 77. Minimum Initial Schema

The initial implementation SHALL contain at least:

```text
users
roles
user_roles
members
memberships
membership_fees
accounts
accounting_periods
vouchers
voucher_lines
projects
grants
grant_payments
documents
audit_events
settings
backup_records
schema_migrations
```

Bank, budget and asset tables SHOULD be included in the initial schema if their service modules are implemented concurrently.

---

# 78. Recommended Initial SQL Structure

The database initialisation module SHOULD create tables in dependency order:

```text
1. schema_migrations
2. users
3. roles
4. user_roles
5. members
6. memberships
7. accounts
8. accounting_periods
9. projects
10. vouchers
11. voucher_lines
12. membership_fees
13. bank_transactions
14. bank_reconciliations
15. budgets
16. budget_lines
17. grants
18. grant_payments
19. assets
20. documents
21. audit_events
22. settings
23. backup_records
```

---

# 79. Database Foundation Development Sequence

```text
CREATE db.py
        ↓
CREATE schema.py
        ↓
CREATE migrations.py
        ↓
CREATE initial schema
        ↓
ENABLE foreign keys
        ↓
SEED roles
        ↓
SEED basic configuration
        ↓
TEST CONNECTION
        ↓
TEST CRUD
        ↓
TEST ACCOUNTING INTEGRITY
        ↓
TEST BACKUP / RESTORE
```

---

# 80. Relationship to Existing MFM Code

The existing MFM project has previously contained modules such as:

```text
src/database/db.py
src/database/schema.py
src/gui/main_window.py
src/gui/dashboard.py
src/gui/kontoplan.py
src/services/
```

The new baseline SHALL be used to bring those modules into a consistent structure.

Existing code SHALL be reviewed before being discarded.

The objective is:

```text
REUSE WHERE SOUND
+
REFACTOR WHERE NECESSARY
+
REPLACE BROKEN PARTS
```

not an unnecessary complete rewrite.

---

# 81. Known Historical Development Problems

Previous MFM development encountered issues including:

- import path inconsistencies;
- `start_app` import problems;
- undefined database cursor;
- missing GUI modules;
- inconsistent `src` imports;
- undefined service references;
- database/service/GUI boundaries becoming unclear.

The database foundation directly addresses these problems by enforcing clear module responsibilities.

---

# 82. Required Database Module Contract

`src/database/db.py` SHALL provide a stable interface for:

```text
get_connection()
initialize_database()
execute()
fetch_one()
fetch_all()
transaction()
backup_database()
integrity_check()
```

The exact implementation MAY differ, but callers SHALL not need to know low-level SQLite setup details.

---

# 83. Required Schema Module Contract

`src/database/schema.py` SHALL define:

- table creation;
- indexes;
- constraints;
- seed data where appropriate.

Schema definition SHALL not be mixed with GUI code.

---

# 84. Required Migration Module Contract

`src/database/migrations.py` SHALL:

- identify current schema version;
- determine pending migrations;
- apply migrations;
- record successful migrations;
- stop safely on failure.

---

# 85. Final Database Principle

> **The database is the foundation of MFM. It must be boring, predictable and trustworthy.**

MFM does not need a sophisticated database architecture.

It needs a database that:

```text
DOES NOT LOSE DATA
DOES NOT BREAK ACCOUNTING
DOES NOT HIDE HISTORY
DOES NOT CREATE DUPLICATE TRUTH
CAN BE BACKED UP
CAN BE RESTORED
CAN BE UNDERSTOOD
```

# END OF MFM v1.0 DATABASE FOUNDATION
