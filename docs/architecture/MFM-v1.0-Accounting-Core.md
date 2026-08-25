# MFM v1.0 ACCOUNTING CORE

## MaritimForeningsManager — Regnskabsmotor og finansiel kerne

**Version:** 1.0  
**Status:** Development Baseline  
**Parent:** MFM v1.0 Database Foundation  
**Purpose:** Define the complete accounting engine for a small non-profit association

---

# 1. Purpose

The Accounting Core is the financial heart of MFM.

It SHALL provide:

- double-entry bookkeeping;
- chart of accounts;
- accounting periods;
- vouchers;
- voucher lines;
- posting;
- reversal;
- corrections;
- account balances;
- ledger;
- income statement;
- balance sheet;
- budget comparison;
- project accounting;
- audit trail;
- controlled period closing.

The Accounting Core SHALL be simple enough for a small association while preserving proper financial integrity.

---

# 2. Core Principle

> **Every posted financial transaction must be balanced, traceable, attributable and reproducible.**

The accounting engine SHALL never trade accounting integrity for convenience.

---

# 3. Accounting Model

```text
ACCOUNT
   ↓
VOUCHER
   ↓
VOUCHER LINES
   ↓
POSTING
   ↓
GENERAL LEDGER
   ↓
REPORTING
```

Each voucher SHALL contain at least two lines unless a specific accounting mechanism explicitly supports another controlled form.

---

# 4. Double-Entry Rule

For every posted voucher:

```text
TOTAL DEBIT = TOTAL CREDIT
```

Example:

```text
Bank                     Debit     1,000
Membership Income       Credit     1,000
```

The accounting service SHALL reject an unbalanced voucher.

---

# 5. Accounting Objects

Core objects:

```text
Account
AccountingPeriod
Voucher
VoucherLine
LedgerEntry
Reversal
Budget
ProjectAllocation
AccountingReport
```

---

# 6. Chart of Accounts

The chart of accounts SHALL classify accounts as:

```text
ASSET
LIABILITY
EQUITY
INCOME
EXPENSE
```

Each account SHALL have:

- account number;
- name;
- type;
- active state;
- optional parent;
- reporting group;
- optional VAT code.

---

# 7. Account Numbering

The system SHALL permit configurable account numbering.

A recommended structure is:

```text
1000–1999  ASSETS
2000–2999  LIABILITIES
3000–3999  EQUITY
4000–4999  INCOME
5000–9999  EXPENSES
```

This is a recommendation, not a hard-coded requirement.

---

# 8. Account Hierarchy

Accounts MAY have parent accounts.

Example:

```text
5000 Administration
 ├── 5010 Office supplies
 ├── 5020 Telephone
 └── 5030 Software

6000 Projects
 ├── 6010 Restoration
 ├── 6020 Events
 └── 6030 Education
```

Parent accounts MAY be reporting categories rather than posting accounts.

---

# 9. Posting Account

Only active posting accounts SHALL accept voucher lines.

A non-posting group account SHALL reject direct posting.

---

# 10. Account Lifecycle

```text
CREATE
 ↓
ACTIVE
 ↓
INACTIVE
```

An account with historical transactions SHALL normally be deactivated rather than deleted.

---

# 11. Accounting Periods

Each financial year SHALL consist of one or more accounting periods.

Minimum:

```text
OPEN
CLOSED
LOCKED
```

---

# 12. Period Rules

### OPEN

Posting allowed.

### CLOSED

Ordinary posting prohibited.

### LOCKED

No ordinary modification or reopening without elevated authority.

---

# 13. Period Closing

Closing sequence:

```text
CHECK UNPOSTED
 ↓
CHECK UNBALANCED
 ↓
CHECK BANK
 ↓
CHECK REQUIRED RECONCILIATION
 ↓
GENERATE PERIOD REPORTS
 ↓
USER CONFIRMATION
 ↓
CLOSE PERIOD
```

---

# 14. Reopening Period

A closed period SHALL not be reopened through ordinary user actions.

Reopening SHALL require:

- appropriate role;
- reason;
- audit event;
- confirmation.

---

# 15. Voucher

A voucher is the basic accounting transaction.

Minimum fields:

```text
voucher_number
voucher_date
description
period
status
created_by
created_at
```

---

# 16. Voucher Status

```text
DRAFT
POSTED
REVERSED
```

---

# 17. Draft Voucher

A draft voucher:

- may be edited;
- may be deleted by authorised users;
- is not part of the official ledger;
- SHALL not affect financial reports.

---

# 18. Posted Voucher

A posted voucher:

- becomes part of the official ledger;
- cannot be silently edited;
- cannot be deleted;
- SHALL be included in reports.

---

# 19. Reversed Voucher

A reversed voucher remains part of history.

The reversal SHALL create a new balancing transaction.

---

# 20. Voucher Lines

Each line SHALL contain:

```text
account
description
debit
credit
optional project
```

Rules:

```text
debit >= 0
credit >= 0
```

A line SHALL not contain both a positive debit and positive credit.

---

# 21. Voucher Validation

Before posting:

```text
VOUCHER EXISTS
 ↓
DATE VALID
 ↓
PERIOD OPEN
 ↓
USER AUTHORISED
 ↓
LINES EXIST
 ↓
ACCOUNTS ACTIVE
 ↓
DEBITS >= 0
 ↓
CREDITS >= 0
 ↓
TOTAL DEBIT = TOTAL CREDIT
 ↓
PROJECT REFERENCES VALID
 ↓
POST
```

---

# 22. Posting Transaction

Posting SHALL be atomic.

```text
BEGIN TRANSACTION
      ↓
VALIDATE
      ↓
POST VOUCHER
      ↓
WRITE LEDGER EFFECT
      ↓
WRITE AUDIT EVENT
      ↓
COMMIT
```

Failure SHALL cause rollback.

---

# 23. Ledger

The general ledger is derived from posted voucher lines.

```text
Voucher
   ↓
VoucherLine
   ↓
Ledger Query
```

A separate duplicate financial ledger SHOULD NOT be maintained unless technically necessary.

---

# 24. Account Balance

Account balance SHALL be calculated from posted entries.

Conceptually:

```text
BALANCE = DEBITS - CREDITS
```

The display logic SHALL interpret the result according to account type.

---

# 25. Trial Balance

The system SHALL provide a trial balance.

Minimum:

| Account | Debit | Credit |
|---|---:|---:|

Total debit and credit SHALL balance.

---

# 26. General Ledger Report

The general ledger SHALL support:

- account;
- date range;
- voucher number;
- description;
- debit;
- credit;
- balance.

---

# 27. Journal Report

A journal report SHALL list posted vouchers chronologically.

Minimum:

```text
date
voucher number
description
account
debit
credit
```

---

# 28. Income Statement

The income statement SHALL summarise:

```text
INCOME
-
EXPENSES
=
RESULT
```

It SHALL be filterable by:

- financial year;
- period;
- project where applicable.

---

# 29. Balance Sheet

The balance sheet SHALL summarise:

```text
ASSETS
=
LIABILITIES + EQUITY
```

The exact presentation may be configured.

---

# 30. Equity / Opening Balance

The application SHALL support opening balances through controlled accounting entries.

Opening balances SHALL not be inserted by directly manipulating report data.

---

# 31. Membership Income

Membership fees SHALL ultimately enter accounting through controlled transactions.

Example:

```text
Debit  Receivable
Credit Membership Income
```

When paid:

```text
Debit  Bank
Credit Receivable
```

The exact accounts SHALL be configurable.

---

# 32. Expense Transaction

Example:

```text
Debit  Expense
Credit Bank / Payable
```

The application SHALL not force one specific account combination.

---

# 33. Project Accounting

Project transactions MAY be linked to voucher lines.

Example:

```text
Voucher
  ↓
VoucherLine
  ↓
Account = Project Expense
Project = Álvur Restoration
```

This allows project reporting without a separate accounting ledger.

---

# 34. Project Result

Project result:

```text
PROJECT INCOME
-
PROJECT EXPENSE
=
PROJECT RESULT
```

---

# 35. Budget

Budget SHALL be separate from posted actual accounting.

```text
BUDGET
      +
ACTUAL
      ↓
VARIANCE
```

---

# 36. Budget Variance

For expenses:

```text
VARIANCE = BUDGET - ACTUAL
```

The UI SHALL clearly indicate whether a variance is favourable or unfavourable based on account type.

---

# 37. Budget by Account

Budget MAY be assigned to:

```text
financial year
account
project
period
```

---

# 38. Budget by Project

A project budget MAY contain:

- personnel;
- materials;
- travel;
- equipment;
- services;
- other expenses.

The detailed categories remain configurable.

---

# 39. Bank Integration

MFM v1.0 SHOULD support manual bank entry initially.

Future bank import MAY use:

```text
CSV
```

or another supported bank format.

Bank import SHALL never automatically post transactions without validation unless explicitly configured and safe.

---

# 40. Bank Reconciliation

Reconciliation compares:

```text
BANK STATEMENT
vs
MFM BOOK BALANCE
```

Difference:

```text
STATEMENT BALANCE - BOOK BALANCE
```

Target:

```text
0
```

---

# 41. Reconciliation Status

```text
OPEN
IN_PROGRESS
RECONCILED
```

A completed reconciliation SHALL be auditable.

---

# 42. VAT

VAT functionality SHALL be configurable.

The application SHALL not assume every association is VAT registered.

VAT-related fields MAY include:

```text
vat_code
net_amount
vat_amount
gross_amount
```

The accounting implementation SHALL allow VAT to be disabled.

---

# 43. Currency

MFM v1.0 SHALL support one base currency.

Default SHOULD be:

```text
DKK
```

Multi-currency SHALL be considered future scope unless specifically required.

---

# 44. Rounding

Financial calculations SHALL use a defined rounding policy.

Rounding SHALL be consistent throughout:

- posting;
- reporting;
- budget calculations;
- exports.

---

# 45. Corrections

Corrections to posted accounting SHALL use controlled reversal and replacement.

Never:

```text
DELETE POSTED VOUCHER
```

Instead:

```text
ORIGINAL
 ↓
REVERSAL
 ↓
CORRECTED
```

---

# 46. Reversal

A reversal SHALL create lines with inverted debit/credit values.

Example:

Original:

```text
Debit  Expense  500
Credit Bank     500
```

Reversal:

```text
Debit  Bank     500
Credit Expense  500
```

---

# 47. Correction Reason

Every reversal SHOULD contain:

- reason;
- original voucher;
- user;
- timestamp.

---

# 48. Duplicate Prevention

The service SHALL detect likely duplicates based on configurable criteria such as:

- date;
- amount;
- account;
- reference;
- description.

Duplicate detection SHOULD warn rather than automatically reject unless the duplicate is certain.

---

# 49. Accounting Permissions

Recommended:

### ADMIN

Full configuration and administration.

### TREASURER

Financial operations and reports.

### ACCOUNTANT

Accounting operations.

### BOARD_USER

Reports and permitted approvals.

### READ_ONLY

Read-only access.

---

# 50. Financial Authority

The application SHALL distinguish:

```text
CAN ENTER
CAN POST
CAN REVERSE
CAN CLOSE PERIOD
CAN REOPEN PERIOD
CAN CONFIGURE ACCOUNTS
CAN EXPORT
```

These permissions SHOULD be configurable by role.

---

# 51. Separation of Duties

For a small association, strict segregation MAY be impractical.

Nevertheless, the application SHOULD support separation between:

```text
ENTRY
POSTING
REVIEW
```

Where staffing permits.

---

# 52. Audit Events

Financial audit events SHOULD include:

```text
VOUCHER_CREATED
VOUCHER_EDITED
VOUCHER_POSTED
VOUCHER_REVERSED
PERIOD_CLOSED
PERIOD_REOPENED
ACCOUNT_CREATED
ACCOUNT_DEACTIVATED
BUDGET_CHANGED
BANK_RECONCILED
```

---

# 53. Accounting Reports

Minimum:

1. Trial balance
2. General ledger
3. Journal
4. Income statement
5. Balance sheet
6. Budget versus actual
7. Project financial report
8. Account statement
9. Voucher list

---

# 54. Report Date Rules

Reports SHALL use explicit date boundaries.

Example:

```text
FROM 2026-01-01
TO   2026-12-31
```

Inclusive/exclusive behaviour SHALL be consistent.

---

# 55. Report Integrity

Reports SHALL read only posted accounting transactions unless explicitly labelled otherwise.

Draft vouchers SHALL not appear in official financial reports.

---

# 56. Accounting Dashboard

The dashboard MAY display:

```text
BANK BALANCE
INCOME YTD
EXPENSE YTD
RESULT YTD
OPEN FEES
PROJECT SPEND
BUDGET VARIANCE
```

Dashboard figures SHALL link to underlying reports.

---

# 57. Accounting Service

`AccountingService` SHALL own the main financial workflows.

Recommended methods:

```text
create_voucher()
update_draft_voucher()
validate_voucher()
post_voucher()
reverse_voucher()
get_account_balance()
get_trial_balance()
get_ledger()
get_income_statement()
get_balance_sheet()
close_period()
reopen_period()
```

---

# 58. Account Service

`AccountService` SHALL handle:

```text
create_account()
update_account()
deactivate_account()
get_account()
list_accounts()
validate_account()
```

It SHALL prevent deletion of historically used accounts.

---

# 59. Budget Service

`BudgetService` SHALL handle:

```text
create_budget()
add_budget_line()
update_budget_line()
get_budget()
compare_budget_actual()
```

---

# 60. Bank Service

`BankService` SHALL handle:

```text
import_transactions()
create_transaction()
match_transaction()
reconcile()
```

---

# 61. Accounting Repository

`AccountingRepository` SHALL handle persistence for:

- vouchers;
- voucher lines;
- accounts;
- periods;
- accounting queries.

It SHALL not contain GUI logic.

---

# 62. Transaction Boundary

A complete voucher posting SHALL occur inside one database transaction.

The service SHALL not:

```text
save voucher
COMMIT
then save lines
```

It SHALL save the complete transaction atomically.

---

# 63. Validation Layer

Validation SHALL be separated into:

```text
FIELD VALIDATION
BUSINESS VALIDATION
ACCOUNTING VALIDATION
AUTHORITY VALIDATION
```

---

# 64. Field Validation

Examples:

```text
amount numeric
date valid
description present
account selected
```

---

# 65. Business Validation

Examples:

```text
period open
project active
account active
user permitted
```

---

# 66. Accounting Validation

Examples:

```text
debit >= 0
credit >= 0
debit + credit > 0
total debit = total credit
```

---

# 67. Authority Validation

Before posting:

```text
USER ACTIVE
+
ROLE PERMISSION
+
PERIOD PERMISSION
=
POST ALLOWED
```

---

# 68. Accounting Error Codes

Recommended:

```text
ACC001_INVALID_DATE
ACC002_PERIOD_CLOSED
ACC003_NO_LINES
ACC004_UNBALANCED
ACC005_INVALID_ACCOUNT
ACC006_INACTIVE_ACCOUNT
ACC007_INVALID_PROJECT
ACC008_UNAUTHORISED
ACC009_ALREADY_POSTED
ACC010_NOT_REVERSIBLE
```

Errors SHALL be understandable to users.

---

# 69. GUI Accounting Workflow

```text
Accounting
   ↓
New Voucher
   ↓
Enter Date
   ↓
Enter Description
   ↓
Enter Lines
   ↓
Validate
   ↓
Display Balance
   ↓
Post
   ↓
Confirmation
```

---

# 70. Voucher Entry Screen

Recommended fields:

```text
Voucher No.
Date
Description
Reference
Project
```

Lines:

```text
Account
Description
Debit
Credit
Project
```

Footer:

```text
TOTAL DEBIT
TOTAL CREDIT
DIFFERENCE
```

Post button SHALL remain disabled until validation succeeds.

---

# 71. Kontoplan Screen

The chart-of-accounts screen SHOULD show:

```text
No.
Name
Type
Group
Active
```

Actions:

```text
New
Edit
Deactivate
Search
Filter
```

---

# 72. Ledger Screen

The ledger SHOULD allow:

```text
account
from date
to date
project
```

and show:

```text
date
voucher
description
debit
credit
balance
```

---

# 73. Period Closing Screen

The screen SHOULD show:

```text
UNPOSTED VOUCHERS
BANK RECONCILIATION
TRIAL BALANCE
OPEN ITEMS
```

before allowing closure.

---

# 74. Accounting Acceptance Test 1 — Balanced Voucher

Input:

```text
Debit  1,000
Credit 1,000
```

Expected:

```text
POST SUCCESS
```

---

# 75. Accounting Acceptance Test 2 — Unbalanced Voucher

Input:

```text
Debit  1,000
Credit   900
```

Expected:

```text
POST REJECTED
ACC004_UNBALANCED
```

---

# 76. Accounting Acceptance Test 3 — Closed Period

Attempt to post into closed period.

Expected:

```text
POST REJECTED
ACC002_PERIOD_CLOSED
```

---

# 77. Accounting Acceptance Test 4 — Inactive Account

Attempt to post to inactive account.

Expected:

```text
POST REJECTED
ACC006_INACTIVE_ACCOUNT
```

---

# 78. Accounting Acceptance Test 5 — Reversal

Given a posted voucher:

```text
Debit Expense 500
Credit Bank  500
```

Execute reversal.

Expected:

```text
Original remains POSTED/REVERSED
New reversal voucher POSTED
Ledger net effect = 0
Audit event exists
```

---

# 79. Accounting Acceptance Test 6 — Period Close

Given no unresolved blocking conditions:

```text
Close period
```

Expected:

```text
status = CLOSED
audit event created
```

---

# 80. Accounting Acceptance Test 7 — Report Integrity

Given posted transactions:

```text
income
expense
asset
liability
```

Expected:

```text
Trial balance balanced
Income statement correct
Balance sheet balanced
```

---

# 81. Accounting Acceptance Test 8 — Audit

Post a voucher.

Expected audit event:

```text
event_type = VOUCHER_POSTED
user_id != NULL
entity_id = voucher.id
timestamp != NULL
```

---

# 82. Negative Testing

```text
Post unbalanced voucher → BLOCK
Post to inactive account → BLOCK
Post to closed period → BLOCK
Delete posted voucher → BLOCK
Edit posted voucher → BLOCK
Reverse non-posted voucher → BLOCK
Reverse already reversed voucher → BLOCK
Post without permission → BLOCK
Use invalid project → BLOCK
Use invalid account → BLOCK
Duplicate voucher number → BLOCK
Negative debit → BLOCK
Negative credit → BLOCK
Both debit and credit on line → BLOCK
No accounting lines → BLOCK
Database failure during posting → ROLLBACK
Audit failure during posting → ROLLBACK
```

---

# 83. Accounting Reconciliation

The accounting core SHALL support reconciliation between:

```text
BANK
+
CASH
+
LEDGER
```

The system SHALL expose differences rather than silently adjusting balances.

---

# 84. Cash Accounting

Cash transactions MAY be entered similarly to bank transactions.

Example:

```text
Debit Expense
Credit Cash
```

Cash balance SHALL be reportable.

---

# 85. Opening Balance

Opening balance SHALL be introduced through an opening-balance voucher.

It SHALL be:

- dated;
- authorised;
- documented;
- auditable.

---

# 86. Year-End

Year-end functionality SHALL support:

- final reports;
- period closing;
- opening balances for next year.

Automatic income/expense closing MAY be implemented later according to the association's accounting method.

---

# 87. Financial Export

Accounting exports SHOULD include:

```text
voucher number
date
description
account number
account name
debit
credit
project
```

---

# 88. Excel Export

The report service SHALL provide XLSX exports where appropriate.

Export SHALL be read-only and SHALL not alter accounting.

---

# 89. PDF Reports

PDF reporting MAY include:

- annual accounts;
- trial balance;
- project report;
- budget report.

The report generator SHALL read from the accounting service.

---

# 90. Accounting API Boundary

Internal service contract:

```text
GUI
 ↓
AccountingService
 ↓
AccountingRepository
 ↓
Database
```

The GUI SHALL not directly execute accounting SQL.

---

# 91. Accounting Logging

Operational logging SHALL record errors and diagnostics.

Financial audit SHALL use the dedicated audit table.

The two SHALL remain separate.

---

# 92. Performance

The accounting core is expected to support normal association volumes without specialised infrastructure.

Indexes SHALL support:

- voucher date;
- account;
- project;
- period;
- voucher number.

---

# 93. Accounting Security

Users SHALL only see or perform actions permitted by their roles.

Sensitive financial operations SHALL be audited.

---

# 94. Backup Before Critical Operations

The application SHOULD create or verify a recent backup before:

- period closing;
- schema migration;
- major accounting import.

---

# 95. Import Controls

Imported accounting data SHALL initially enter a review state.

Recommended:

```text
IMPORTED
 ↓
VALIDATED
 ↓
REVIEWED
 ↓
POSTED
```

No uncontrolled import SHALL directly modify posted history.

---

# 96. Bank Import

Future CSV import:

```text
CSV
 ↓
PARSE
 ↓
VALIDATE
 ↓
DUPLICATE CHECK
 ↓
IMPORT
 ↓
MATCH
 ↓
USER REVIEW
 ↓
POST
```

---

# 97. Automated Matching

Automated bank matching MAY use:

- amount;
- date;
- reference;
- description.

Matching SHALL produce a suggestion unless confidence is sufficiently high and the user has explicitly enabled automatic matching.

---

# 98. Accounting Notifications

The system MAY notify users of:

- unposted vouchers;
- unreconciled bank items;
- budget overruns;
- period closing readiness;
- missing project coding.

---

# 99. Accounting Health

The accounting dashboard SHOULD expose:

```text
UNPOSTED VOUCHERS
UNRECONCILED BANK ITEMS
OPEN PERIODS
LAST BACKUP
TRIAL BALANCE STATUS
```

---

# 100. Definition of Done

Accounting Core v1.0 is complete when:

- chart of accounts works;
- accounting periods work;
- vouchers work;
- voucher lines work;
- posting works;
- double-entry validation works;
- reversal works;
- ledger works;
- trial balance works;
- income statement works;
- balance sheet works;
- project coding works;
- budget comparison works;
- permissions work;
- audit works;
- negative tests pass;
- backup/restore protects accounting data.

---

# 101. Implementation Sequence

```text
1. Account model
2. Accounting period model
3. Voucher model
4. Voucher line model
5. Database repository
6. Accounting service
7. Validation
8. Posting
9. Reversal
10. Ledger queries
11. Trial balance
12. Income statement
13. Balance sheet
14. Budget comparison
15. Project accounting
16. Audit integration
17. GUI
18. Tests
```

---

# 102. Existing MFM Integration

The existing project has previously contained:

```text
src/database/db.py
src/database/schema.py
src/gui/kontoplan.py
src/gui/main_window.py
src/services/
```

The implementation SHALL preserve working components where possible.

The expected target is:

```text
src/gui/kontoplan.py
        ↓
AccountService
        ↓
AccountRepository
        ↓
Database
```

and:

```text
Voucher GUI
        ↓
AccountingService
        ↓
AccountingRepository
        ↓
Database
```

---

# 103. Critical Development Rule

No GUI module SHALL implement:

```text
SUM(debit)
SUM(credit)
period validation
posting rules
reversal rules
```

Those rules belong to the accounting service.

---

# 104. Final Accounting Principle

> **The accounting core must be boring, deterministic and trustworthy.**

It SHALL not attempt to be clever.

It SHALL:

```text
BALANCE
VALIDATE
POST
RECORD
REPORT
REVERSE
AUDIT
```

correctly and consistently.

# END OF MFM v1.0 ACCOUNTING CORE
