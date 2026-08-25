# MFM v1.0 ARCHITECTURE BASELINE

## MaritimForeningsManager — Foreningsadministration, økonomi, projekter og dokumentstyring

**Version:** 1.0  
**Status:** Architecture Baseline / Development Foundation  
**Derived from:** EA-IMETA-PC-RG series through RG-503  
**Target:** Almennyttig forening  
**Primary principle:** Simple, robust, auditable and maintainable

---

# 1. Executive Summary

MFM v1.0 Architecture Baseline is the practical translation of the extensive EA-IMETA-PC-RG architecture into a proportionate application architecture for a small or medium-sized non-profit association.

The purpose is not to reproduce enterprise complexity inside the application.

The purpose is to retain the useful architectural principles:

- clear authority;
- reliable accounting;
- traceability;
- controlled changes;
- separation of data and presentation;
- project accountability;
- document integrity;
- backup and recovery;
- appropriate security;
- transparent reporting.

MFM SHALL therefore optimise for:

```text
SIMPLICITY
+
RELIABILITY
+
TRACEABILITY
+
USABILITY
+
MAINTAINABILITY
```

rather than enterprise-scale autonomous optimisation.

---

# 2. Architecture Decision

The EA-IMETA-PC-RG series is now treated as the **architectural parent and governance reference**.

MFM v1.0 is the **implementation baseline**.

Future MFM development SHALL NOT automatically require creation of another large RG document.

New requirements SHALL first be assessed against this baseline.

Only changes that materially alter the architecture, governance model or application scope should require a new architecture revision.

---

# 3. Scope

MFM v1.0 covers:

1. Association administration
2. Member management
3. Membership fees
4. Chart of accounts
5. Bookkeeping
6. Vouchers
7. Bank transactions
8. Budget
9. Projects
10. Grants and funding applications
11. Assets
12. Documents
13. Reports
14. User administration
15. Audit trail
16. Backup and restore
17. Data export
18. Configuration

MFM v1.0 does NOT attempt to become:

- an ERP system;
- a banking platform;
- a payroll system;
- a tax authority system;
- a general-purpose CRM;
- a fully autonomous financial decision system.

---

# 4. Architectural Principles

## 4.1 Principle: Proportionality

Architecture SHALL be proportionate to the association's size, risk and actual needs.

## 4.2 Principle: Human Authority

Financial and governance decisions remain human decisions.

## 4.3 Principle: Accounting Integrity

Posted accounting transactions SHALL be traceable and protected from silent alteration.

## 4.4 Principle: Simplicity

The simplest architecture capable of meeting the requirement SHALL be preferred.

## 4.5 Principle: Auditability

Material financial actions SHALL be reconstructable.

## 4.6 Principle: Explicitness

Important business rules SHALL be explicit in code and documentation.

## 4.7 Principle: Separation

GUI, business logic, data access and persistence SHALL be separated.

## 4.8 Principle: Recoverability

The application SHALL support reliable backup and restoration.

## 4.9 Principle: Exportability

Association data SHALL not be trapped inside the application.

## 4.10 Principle: Maintainability

The system SHALL be understandable by a competent Python developer without requiring knowledge of the original EA series.

---

# 5. Target Architecture

```text
+------------------------------------------------------+
|                    MFM APPLICATION                   |
+------------------------------------------------------+
| GUI / Presentation                                   |
| Dashboard | Members | Accounting | Projects | Docs |
+------------------------------------------------------+
| Application Services                                 |
| Member Service | Accounting Service | Project      |
| Service | Document Service | Report Service         |
+------------------------------------------------------+
| Domain / Business Rules                              |
| Membership | Accounting | Projects | Grants | Assets|
+------------------------------------------------------+
| Data Access Layer                                    |
| Repository / Query / Transaction Management          |
+------------------------------------------------------+
| Persistence                                          |
| SQLite Database | File Storage | Backup             |
+------------------------------------------------------+
| Operating System                                     |
| Windows                                              |
+------------------------------------------------------+
```

---

# 6. Technology Baseline

| Component | Baseline |
|---|---|
| Language | Python 3.x |
| Application | Desktop Windows application |
| Database | SQLite |
| GUI | Tkinter/ttk or existing MFM GUI framework |
| Data access | Python database abstraction |
| Reports | Python-generated reports |
| Spreadsheet export | XLSX |
| Document export | PDF/print-ready reports where required |
| Configuration | Local configuration |
| Backup | Database + document backup |
| Packaging | Windows executable/package |
| Source control | Git |

The architecture SHALL avoid unnecessary external infrastructure for v1.0.

---

# 7. Application Modules

## 7.1 Dashboard

Purpose:

- financial overview;
- account balances;
- project status;
- unpaid membership fees;
- recent vouchers;
- warnings;
- backup status.

## 7.2 Members

Functions:

- create member;
- edit member;
- deactivate member;
- membership type;
- contact details;
- membership status;
- fee status;
- notes;
- member history.

## 7.3 Membership Fees

Functions:

- fee definition;
- annual fee;
- member-specific fee;
- invoice/charge registration;
- payment registration;
- outstanding balance;
- fee report.

## 7.4 Chart of Accounts

Functions:

- account number;
- account name;
- account type;
- active/inactive;
- VAT configuration where required;
- reporting category.

## 7.5 Accounting

Functions:

- create voucher;
- voucher lines;
- debit;
- credit;
- date;
- description;
- account;
- project;
- document reference;
- posting;
- correction through controlled reversal.

## 7.6 Bank

Functions:

- bank transaction import;
- manual bank entry;
- matching;
- reconciliation;
- balance comparison.

## 7.7 Budget

Functions:

- annual budget;
- account budget;
- project budget;
- actual versus budget;
- variance;
- forecast.

## 7.8 Projects

Functions:

- project creation;
- project number;
- project name;
- responsible person;
- start/end;
- budget;
- income;
- expenditure;
- funding;
- project documents;
- project status.

## 7.9 Grants and Funding

Functions:

- funder;
- application;
- deadline;
- requested amount;
- approved amount;
- project relationship;
- application status;
- reporting deadline;
- documentation.

## 7.10 Assets

Functions:

- asset register;
- acquisition;
- value;
- location;
- responsible person;
- maintenance note;
- disposal;
- document relation.

## 7.11 Documents

Functions:

- voucher attachment;
- project document;
- grant document;
- member document where appropriate;
- document metadata;
- file reference;
- document category.

## 7.12 Reports

Minimum reports:

- income statement;
- balance;
- account ledger;
- voucher list;
- budget versus actual;
- project financial report;
- membership report;
- outstanding fees;
- grant overview;
- asset register;
- audit report.

---

# 8. Data Architecture

Core entities:

```text
Association
User
Role
Member
Membership
MembershipFee
Account
Voucher
VoucherLine
BankTransaction
BankReconciliation
Budget
BudgetLine
Project
ProjectTransaction
Grant
GrantPayment
Asset
Document
AuditEvent
Setting
Backup
```

Relationships SHALL be explicit.

---

# 9. Accounting Model

The accounting engine SHALL use double-entry principles.

A voucher consists of:

```text
Voucher
  |
  +-- VoucherLine
        |
        +-- Account
        +-- Debit
        +-- Credit
        +-- Project
        +-- Description
```

For each posted voucher:

```text
SUM(DEBIT) = SUM(CREDIT)
```

A voucher that does not balance SHALL NOT be posted.

---

# 10. Accounting Lifecycle

```text
DRAFT
 ↓
VALIDATE
 ↓
POST
 ↓
AUDIT
 ↓
REPORT
```

A posted voucher SHALL NOT be silently edited.

Corrections SHALL use:

```text
REVERSAL
+
CORRECTED TRANSACTION
```

This preserves the audit trail.

---

# 11. Project Accounting

Project accounting SHALL allow association transactions to be attributed to projects without requiring a separate accounting system.

```text
ACCOUNT
   +
PROJECT
   +
VOUCHER
   ↓
PROJECT FINANCIAL POSITION
```

A project may therefore show:

- income;
- expenditure;
- net result;
- budget;
- variance;
- funding.

---

# 12. Membership Architecture

Membership is separated from accounting.

```text
MEMBER
 ↓
MEMBERSHIP
 ↓
FEE
 ↓
CHARGE
 ↓
PAYMENT
 ↓
ACCOUNTING
```

This prevents the member database from becoming the accounting ledger.

---

# 13. Document Architecture

Documents SHALL be stored outside the accounting tables as files, with metadata stored in the database.

Minimum metadata:

- document ID;
- file name;
- category;
- date;
- related entity;
- checksum where practical;
- storage path;
- created timestamp.

---

# 14. Security Architecture

MFM v1.0 SHALL implement proportionate security.

Minimum:

- user authentication;
- role-based permissions;
- password protection;
- audit logging;
- controlled administrative functions;
- backup protection.

Roles SHOULD include:

```text
ADMIN
TREASURER
ACCOUNTANT
BOARD_USER
READ_ONLY
```

A small association MAY use fewer roles if appropriate.

---

# 15. Authority Model

```text
BOARD / ASSOCIATION GOVERNANCE
          ↓
       ADMIN
          ↓
 FUNCTIONAL USERS
          ↓
      APPLICATION
```

The application SHALL not decide association policy.

It SHALL enforce configured rules and record human decisions.

---

# 16. AI and Automation

AI is optional in MFM v1.0.

Useful future functions include:

- transaction categorisation suggestions;
- anomaly detection;
- report explanations;
- document classification;
- grant deadline reminders;
- budget variance analysis.

AI SHALL remain advisory.

```text
AI
 ↓
SUGGESTION
 ↓
HUMAN REVIEW
 ↓
AUTHORISATION
 ↓
EXECUTION
```

AI SHALL NOT:

- post uncontrolled accounting transactions;
- change the chart of accounts autonomously;
- change financial policies;
- delete audit records;
- change user authority;
- alter posted accounting history.

---

# 17. Audit Architecture

Audit events SHALL capture, where relevant:

- user;
- timestamp;
- action;
- entity;
- entity ID;
- previous value;
- new value;
- result.

Examples:

```text
USER CREATED
MEMBER UPDATED
VOUCHER POSTED
VOUCHER REVERSED
PAYMENT REGISTERED
PROJECT CREATED
DOCUMENT ATTACHED
SETTING CHANGED
BACKUP CREATED
```

---

# 18. Backup Architecture

Backup SHALL include:

1. SQLite database;
2. document repository;
3. configuration;
4. optional export package.

Recommended:

```text
LOCAL BACKUP
+
SECOND COPY
+
PERIODIC EXTERNAL/OFFLINE COPY
```

Restore SHALL be tested periodically.

---

# 19. Error Handling

Errors SHALL be classified as:

```text
USER ERROR
VALIDATION ERROR
BUSINESS RULE ERROR
DATABASE ERROR
FILE ERROR
SYSTEM ERROR
```

The user interface SHALL show understandable messages.

Technical details SHALL be logged for diagnostics.

---

# 20. Transaction Safety

Financial operations SHALL use database transactions.

Example:

```text
BEGIN
 ↓
VALIDATE
 ↓
WRITE
 ↓
AUDIT
 ↓
COMMIT
```

If a critical operation fails:

```text
ROLLBACK
```

No partial accounting transaction SHALL remain.

---

# 21. Data Validation

Examples:

- account must exist;
- debit/credit must be numeric;
- voucher must balance;
- date must be valid;
- member status must be valid;
- project must exist when project coding is mandatory;
- required document references must exist;
- duplicate identifiers SHALL be rejected.

---

# 22. Reporting Architecture

Reports SHALL be generated from authoritative database data.

Reports SHALL not maintain their own competing financial data.

```text
DATABASE
 ↓
QUERY
 ↓
REPORT MODEL
 ↓
PDF / XLSX / SCREEN
```

---

# 23. Import / Export

MFM SHALL support:

- CSV import/export where useful;
- XLSX export;
- accounting export;
- member export;
- project export;
- backup export.

Export SHALL be considered a core architectural safeguard.

---

# 24. Configuration

Configuration SHALL include:

- association name;
- address;
- contact details;
- financial year;
- default accounts;
- membership types;
- fee rules;
- report settings;
- backup settings.

Configuration SHALL be separated from source code.

---

# 25. Database Architecture

Suggested logical schema:

```text
users
roles
user_roles

members
memberships
membership_fees

accounts
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
backups
```

Foreign keys SHOULD be enabled.

Indexes SHALL be created for frequently queried identifiers and relationships.

---

# 26. Repository Architecture

Application services SHALL access data through repositories rather than embedding SQL throughout the GUI.

Example:

```text
MemberService
    ↓
MemberRepository
    ↓
Database
```

and:

```text
AccountingService
    ↓
VoucherRepository
    ↓
Database
```

This is essential for maintainability.

---

# 27. Service Architecture

Recommended services:

```text
member_service
membership_service
account_service
voucher_service
accounting_service
bank_service
budget_service
project_service
grant_service
asset_service
document_service
report_service
audit_service
backup_service
settings_service
```

Services SHALL contain business rules.

GUI code SHALL primarily coordinate user interaction.

---

# 28. GUI Architecture

The GUI SHOULD use:

```text
MainWindow
 ├── Dashboard
 ├── Members
 ├── Accounting
 │    ├── Kontoplan
 │    ├── Bilag
 │    ├── Finans
 │    └── Bank
 ├── Budget
 ├── Projects
 ├── Grants
 ├── Assets
 ├── Documents
 ├── Reports
 └── Settings
```

---

# 29. Project Structure

Recommended:

```text
MFM/
│
├── run.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── src/
│   ├── main.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── schema.py
│   │   └── migrations.py
│   │
│   ├── models/
│   │   ├── member.py
│   │   ├── accounting.py
│   │   ├── project.py
│   │   ├── grant.py
│   │   └── document.py
│   │
│   ├── repositories/
│   │   ├── member_repository.py
│   │   ├── accounting_repository.py
│   │   └── project_repository.py
│   │
│   ├── services/
│   │   ├── member_service.py
│   │   ├── accounting_service.py
│   │   ├── project_service.py
│   │   ├── report_service.py
│   │   ├── audit_service.py
│   │   └── backup_service.py
│   │
│   ├── gui/
│   │   ├── main_window.py
│   │   ├── dashboard.py
│   │   ├── members.py
│   │   ├── accounting.py
│   │   ├── projects.py
│   │   ├── reports.py
│   │   └── settings.py
│   │
│   └── utils/
│
├── data/
├── documents/
├── backups/
├── exports/
└── tests/
```

---

# 30. Development Rules

1. GUI SHALL NOT contain accounting rules.
2. SQL SHALL NOT be scattered through GUI modules.
3. Business rules SHALL reside in services/domain logic.
4. Database changes SHALL use migrations.
5. Posted accounting data SHALL be protected.
6. Every material mutation SHOULD create an audit event.
7. New functionality SHALL include tests.
8. Existing functionality SHALL not be broken without an explicit migration.
9. Configuration SHALL not be hard-coded.
10. Backup SHALL remain independent from ordinary application operation.

---

# 31. Testing Strategy

Testing levels:

```text
UNIT TESTS
   ↓
SERVICE TESTS
   ↓
DATABASE TESTS
   ↓
GUI TESTS
   ↓
INTEGRATION TESTS
   ↓
USER ACCEPTANCE TEST
```

Minimum critical tests:

- balanced voucher;
- unbalanced voucher rejection;
- voucher reversal;
- member creation;
- membership fee;
- payment;
- project transaction;
- budget variance;
- backup;
- restore;
- permissions;
- audit trail.

---

# 32. Financial Acceptance Tests

MFM SHALL demonstrate:

```text
Debit = Credit
```

for every posted voucher.

The system SHALL prevent:

- unbalanced posting;
- deletion of posted vouchers;
- unauthorised account modification;
- unauthorised period manipulation;
- silent financial history changes.

---

# 33. Project Acceptance Tests

A project SHALL demonstrate:

- budget;
- income;
- expenditure;
- balance;
- linked vouchers;
- funding;
- report generation.

---

# 34. Backup Acceptance Tests

A successful backup SHALL be:

1. created;
2. verified;
3. restorable.

A backup that cannot be restored SHALL not be considered successful.

---

# 35. Security Acceptance Tests

Test:

- valid login;
- invalid login;
- permission denial;
- administrator access;
- read-only restrictions;
- audit creation;
- password handling.

---

# 36. Recovery

Recovery scenarios:

```text
DATABASE CORRUPTION
FILE LOSS
USER ERROR
APPLICATION FAILURE
COMPUTER FAILURE
BACKUP RESTORE
```

The target is restoration of:

```text
DATABASE
+
DOCUMENTS
+
CONFIGURATION
```

---

# 37. Versioning

MFM SHALL use semantic versioning:

```text
MAJOR.MINOR.PATCH
```

Examples:

```text
1.0.0
1.0.1
1.1.0
2.0.0
```

Architecture baseline:

```text
MFM v1.0
```

---

# 38. Change Governance

A change is:

```text
SMALL
```

if it affects implementation without changing architecture.

A change is:

```text
ARCHITECTURAL
```

if it changes:

- core data model;
- authority model;
- accounting model;
- persistence architecture;
- major module boundaries;
- security architecture.

Architectural changes require a baseline revision.

---

# 39. Out-of-Scope Complexity

The following SHALL NOT be introduced merely because the EA architecture supports them:

- autonomous financial optimisation;
- multi-market economic clearing;
- enterprise-wide control networks;
- complex AI agents;
- autonomous governance;
- distributed enterprise control;
- unnecessary microservices;
- cloud infrastructure without need;
- blockchain;
- event streaming infrastructure unless justified.

The application is for a non-profit association.

---

# 40. Practical User Experience

The application SHALL be usable by a person who is not a software engineer.

The primary user flow should be:

```text
OPEN MFM
 ↓
SEE STATUS
 ↓
CHOOSE TASK
 ↓
ENTER DATA
 ↓
VALIDATE
 ↓
SAVE / POST
 ↓
REVIEW
```

Important actions SHALL be visible.

Dangerous actions SHALL require confirmation.

---

# 41. Dashboard Baseline

Dashboard SHOULD show:

- bank balance;
- cash balance;
- current-year income;
- current-year expenses;
- result;
- unpaid membership fees;
- active projects;
- project budget status;
- upcoming grant deadlines;
- latest backup;
- warnings.

---

# 42. Association Administration

The system SHALL support:

- association identity;
- financial year;
- board/user roles;
- contact information;
- configurable membership types;
- standard reports.

---

# 43. Data Ownership

The association owns its data.

MFM SHALL provide mechanisms to:

- export;
- backup;
- restore;
- inspect;
- migrate.

The application SHALL not make data extraction unnecessarily difficult.

---

# 44. Privacy

Only necessary personal information SHALL be stored.

Member data SHALL be protected through:

- access control;
- appropriate storage;
- controlled export;
- audit logging.

Data retention SHALL be configurable according to association requirements and applicable rules.

---

# 45. Performance

For the expected scale of a small association:

- SQLite is sufficient;
- local desktop execution is sufficient;
- complex distributed infrastructure is unnecessary.

The system SHOULD remain responsive for ordinary association datasets.

---

# 46. Maintainability

Priority:

```text
READABLE CODE
>
CLEVER CODE
```

The project SHALL favour explicit, understandable Python.

Functions SHOULD be small enough to test.

Modules SHOULD have clear responsibilities.

---

# 47. Documentation

The project SHALL contain:

- README;
- installation guide;
- user guide;
- database documentation;
- accounting rules;
- backup guide;
- developer guide;
- release notes.

---

# 48. Deployment

Target:

```text
WINDOWS DESKTOP
```

Deployment SHOULD provide:

- installer or executable;
- application data directory;
- document directory;
- backup directory;
- configuration;
- version information.

---

# 49. Release Process

```text
DEVELOP
 ↓
UNIT TEST
 ↓
INTEGRATION TEST
 ↓
USER TEST
 ↓
BACKUP TEST
 ↓
PACKAGE
 ↓
RELEASE
```

No release SHALL be considered complete without a tested backup/restore path.

---

# 50. MFM v1.0 Minimum Viable Product

The MVP SHALL include:

1. Login
2. Dashboard
3. Members
4. Membership fees
5. Chart of accounts
6. Vouchers
7. Double-entry accounting
8. Projects
9. Budget
10. Reports
11. Documents
12. Audit log
13. Backup
14. Restore
15. Excel export

---

# 51. MFM v1.0 Extended Functions

After MVP:

- bank import;
- reconciliation;
- grant management;
- asset register;
- advanced reports;
- document search;
- automated reminders.

---

# 52. Future Functions

Possible future:

- AI assistance;
- OCR;
- automatic voucher suggestions;
- bank matching;
- grant deadline alerts;
- mobile access;
- multi-user networking.

These SHALL remain optional.

---

# 53. Final Architecture

```text
                MFM v1.0
                   │
       ┌───────────┴───────────┐
       │                       │
    PEOPLE                  FINANCE
       │                       │
 MEMBERSHIP               ACCOUNTING
       │                       │
       └──────────┬────────────┘
                  │
               PROJECTS
                  │
             GRANTS / ASSETS
                  │
              DOCUMENTS
                  │
               REPORTS
                  │
              AUDIT / BACKUP
                  │
              SQLITE + FILES
```

---

# 54. Relationship to EA-IMETA-PC-RG

The relationship is:

```text
EA-IMETA-PC-RG
       ↓
ARCHITECTURAL PRINCIPLES
       ↓
MFM v1.0 BASELINE
       ↓
APPLICATION DESIGN
       ↓
IMPLEMENTATION
```

The EA series provides principles.

MFM provides practical implementation.

MFM SHALL NOT implement every EA capability.

---

# 55. Architecture Freeze

The following are frozen for MFM v1.0 unless a documented architectural reason exists:

- desktop-first architecture;
- Python;
- SQLite;
- layered application;
- service-oriented internal structure;
- double-entry accounting;
- project accounting;
- audit trail;
- backup/restore;
- export;
- human authority;
- proportionate security.

---

# 56. Development Roadmap

```text
PHASE 1
DATABASE FOUNDATION
        ↓
PHASE 2
ACCOUNTING CORE
        ↓
PHASE 3
MEMBERSHIP
        ↓
PHASE 4
PROJECTS / BUDGET
        ↓
PHASE 5
DOCUMENTS / GRANTS
        ↓
PHASE 6
REPORTS
        ↓
PHASE 7
AUDIT / BACKUP / RESTORE
        ↓
PHASE 8
GUI INTEGRATION
        ↓
PHASE 9
TESTING
        ↓
PHASE 10
WINDOWS RELEASE
```

---

# 57. Definition of Done

MFM v1.0 is complete when:

- application starts reliably;
- database initialises correctly;
- users can log in;
- members can be managed;
- fees can be managed;
- accounts can be managed;
- vouchers can be entered and posted;
- accounting balances;
- projects can be managed;
- budgets can be compared with actuals;
- reports can be generated;
- documents can be linked;
- audit trail works;
- backup works;
- restore works;
- export works;
- permissions work;
- critical tests pass;
- Windows deployment works.

---

# 58. Final Governing Principle

> **MFM shall be as simple as possible, but no simpler than required to protect the association's members, finances, projects, documents and governance.**

The extensive EA-IMETA-PC-RG architecture remains the conceptual parent.

MFM v1.0 deliberately translates that architecture into a practical application suitable for an almennyttig association.

The objective is no longer to build an abstract enterprise control system.

The objective is to build a **reliable, understandable and useful association management system**.

# END OF MFM v1.0 ARCHITECTURE BASELINE
