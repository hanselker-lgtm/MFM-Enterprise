# MFM v1.0 PROJECTS & BUDGET

## MaritimForeningsManager — Projektstyring, projektøkonomi, budget og finansieringsopfølgning

**Version:** 1.0  
**Status:** Development Baseline  
**Parent:** MFM v1.0 Membership & Member Management  
**Purpose:** Define the practical project and budget module for an almennyttig association

---

# 1. Purpose

The Projects & Budget module provides MFM with a controlled way to plan, manage and financially monitor association projects.

The module SHALL support:

- projects;
- project numbers;
- project status;
- project responsibility;
- project budgets;
- project income;
- project expenditure;
- funding;
- grants;
- project-linked accounting;
- budget versus actual;
- project reports;
- project documents;
- project history;
- project closure.

The module SHALL use the Accounting Core as the authoritative financial source.

---

# 2. Core Principle

> **A project is an organisational and reporting object; the accounting ledger remains the authoritative source of financial transactions.**

Therefore:

```text
PROJECT
   ↓
BUDGET / FUNDING PLAN
   ↓
ACCOUNTING TRANSACTIONS
   ↓
PROJECT REPORT
```

The project module SHALL not create a competing accounting ledger.

---

# 3. Architectural Position

```text
MFM ARCHITECTURE
       ↓
DATABASE FOUNDATION
       ↓
ACCOUNTING CORE
       ↓
MEMBERSHIP
       ↓
PROJECTS & BUDGET
```

Projects consume the services of the Accounting Core and may interact with Membership and Grants.

---

# 4. Scope

The module SHALL cover:

1. Project creation
2. Project identification
3. Project status
4. Project responsibility
5. Project budget
6. Project income
7. Project expenditure
8. Project accounting
9. Budget variance
10. Funding overview
11. Grant relationship
12. Project documents
13. Project reporting
14. Project closure
15. Audit trail

---

# 5. Out of Scope

MFM v1.0 SHALL NOT attempt to become a full enterprise project-management platform.

It does not require:

- complex Gantt scheduling;
- resource optimisation;
- agile sprint management;
- enterprise portfolio management;
- autonomous project planning;
- complex workflow engines.

Simple project administration is sufficient.

---

# 6. Project Entity

Minimum fields:

```text
project_number
name
description
start_date
end_date
budget_amount
status
responsible_user
created_at
updated_at
```

---

# 7. Project Number

Every project SHALL have a unique project number.

Example:

```text
P-2027-001
P-2027-002
P-2027-003
```

The exact numbering scheme SHALL be configurable.

A project number SHALL not be reused after historical financial activity exists.

---

# 8. Project Status

Recommended:

```text
PLANNED
ACTIVE
PAUSED
COMPLETED
CANCELLED
```

---

# 9. Project Status Transitions

```text
PLANNED
   ↓
ACTIVE
   ↓
COMPLETED

ACTIVE
   ↓
PAUSED
   ↓
ACTIVE

PLANNED / ACTIVE
   ↓
CANCELLED
```

A completed project SHALL remain available for historical reporting.

---

# 10. Project Creation

Project creation SHALL require:

- project number;
- name;
- status.

Recommended:

- responsible person;
- start date;
- planned end date;
- description;
- initial budget.

---

# 11. Project Responsibility

A project SHOULD have one responsible user.

The responsible user is accountable for project information, not necessarily for financial approval.

Financial authority remains governed by application roles.

---

# 12. Project Budget

A project budget defines planned financial activity.

A project MAY have:

```text
TOTAL BUDGET
+
ACCOUNT BUDGET
+
OPTIONAL FUNDING BUDGET
```

---

# 13. Budget Model

The budget SHALL be separate from actual accounting.

```text
BUDGET
      +
ACTUAL
      ↓
VARIANCE
```

---

# 14. Budget Lines

Budget lines SHOULD be linked to:

- project;
- account;
- financial year;
- amount;
- optional period;
- notes.

Example:

```text
Restoration project

Materials       100,000
Labour           75,000
Equipment        25,000
Travel            5,000
-----------------------
Total           205,000
```

---

# 15. Budget by Account

A project budget MAY be connected to the chart of accounts.

Example:

```text
Account 6010 Materials     100,000
Account 6020 Services       75,000
Account 6030 Travel          5,000
```

Actual transactions coded to the project can then be compared with budget.

---

# 16. Budget by Period

Where useful, budget lines MAY contain:

```text
year
quarter
month
```

MFM v1.0 may initially use annual budgets.

---

# 17. Budget Approval

A budget SHOULD have a lifecycle:

```text
DRAFT
 ↓
REVIEW
 ↓
APPROVED
 ↓
ACTIVE
 ↓
CLOSED
```

The simplest v1.0 implementation MAY use:

```text
DRAFT
APPROVED
CLOSED
```

---

# 18. Budget Changes

Changes to an approved budget SHALL be controlled.

A change SHOULD record:

- old amount;
- new amount;
- reason;
- user;
- timestamp.

---

# 19. Budget Versioning

If budget history is important, the system SHOULD preserve revisions.

Example:

```text
Budget v1 = 200,000
Budget v2 = 225,000
Budget v3 = 240,000
```

The active version is used for current reporting.

---

# 20. Project Income

Project income may include:

- grants;
- donations;
- sponsorship;
- membership contributions;
- project-specific sales;
- other funding.

Income SHALL ultimately be recorded through the Accounting Core.

---

# 21. Project Expenditure

Project expenditure may include:

- materials;
- services;
- transport;
- equipment;
- travel;
- events;
- restoration;
- other approved project costs.

Actual expenditure SHALL be derived from posted accounting transactions.

---

# 22. Project Accounting Link

The preferred relationship is:

```text
Voucher
   ↓
VoucherLine
   ↓
Project ID
```

This means project reporting can query the accounting ledger.

---

# 23. No Duplicate Ledger

The project module SHALL NOT maintain a second financial ledger.

Avoid:

```text
Accounting Ledger
+
Project Ledger
```

Instead:

```text
Accounting Ledger
       ↓
Project-filtered reporting
```

---

# 24. Project Result

For a period:

```text
PROJECT INCOME
-
PROJECT EXPENDITURE
=
PROJECT RESULT
```

The result SHALL be calculated from posted transactions.

---

# 25. Project Budget Variance

For expense categories:

```text
VARIANCE = BUDGET - ACTUAL
```

The report SHALL clearly indicate whether the result is favourable or unfavourable.

---

# 26. Budget Utilisation

The system SHOULD calculate:

```text
ACTUAL / BUDGET × 100
```

Example:

```text
Budget   100,000
Actual    60,000
Usage        60%
```

If budget is zero, the application SHALL avoid division by zero and display an appropriate status.

---

# 27. Project Income versus Budget

Where income is budgeted:

```text
BUDGETED INCOME
vs
ACTUAL INCOME
```

This is useful for grant-funded projects.

---

# 28. Project Funding

Funding sources SHOULD be visible separately:

```text
Association funds
Grant
Donation
Sponsor
Other
```

The funding source does not replace accounting classification.

---

# 29. Grants

Grants MAY be linked to projects.

Relationship:

```text
PROJECT
   ↓
GRANT APPLICATION
   ↓
APPROVED FUNDING
   ↓
PAYMENT
   ↓
ACCOUNTING
```

---

# 30. Grant Independence

The grant module remains responsible for:

- application;
- funder;
- deadline;
- requested amount;
- approved amount;
- reporting deadline.

The Accounting Core remains responsible for actual financial transactions.

---

# 31. Funding Gap

The project module SHOULD calculate:

```text
PROJECT BUDGET
-
CONFIRMED FUNDING
=
FUNDING GAP
```

Example:

```text
Budget             500,000
Confirmed funding  350,000
Funding gap        150,000
```

---

# 32. Funding Status

Recommended:

```text
NOT FUNDED
PARTIALLY FUNDED
FULLY FUNDED
OVERFUNDED
```

The system SHALL show the underlying amounts.

---

# 33. Project Documents

Documents MAY be linked to projects.

Examples:

- project description;
- quotations;
- invoices;
- grant applications;
- grant decisions;
- contracts;
- drawings;
- photographs;
- reports.

The Document module remains responsible for file storage.

---

# 34. Project Document Categories

Recommended:

```text
PROJECT_PLAN
BUDGET
QUOTE
CONTRACT
GRANT_APPLICATION
GRANT_DECISION
INVOICE
REPORT
OTHER
```

---

# 35. Project Dashboard

A project dashboard SHOULD show:

```text
PROJECT STATUS
BUDGET
ACTUAL
VARIANCE
FUNDING
FUNDING GAP
INCOME
EXPENDITURE
DOCUMENTS
DEADLINES
```

---

# 36. Project List

Recommended columns:

```text
Project No.
Name
Status
Responsible
Budget
Actual
Variance
Funding
```

Filters:

```text
status
responsible
year
```

---

# 37. Project Detail

Recommended sections:

```text
OVERVIEW
BUDGET
ACTUAL
FUNDING
GRANTS
DOCUMENTS
TRANSACTIONS
REPORTS
HISTORY
```

---

# 38. Project Transaction View

A project transaction list SHOULD show:

```text
Date
Voucher
Account
Description
Debit
Credit
Net
```

Users SHALL be able to open the source voucher.

---

# 39. Source Traceability

Every project financial figure SHOULD be traceable:

```text
REPORT
 ↓
PROJECT
 ↓
VOUCHER LINE
 ↓
VOUCHER
 ↓
ACCOUNT
```

This is essential for auditability.

---

# 40. Budget Service

`BudgetService` SHALL manage:

```text
create_budget()
update_budget()
approve_budget()
close_budget()
add_budget_line()
update_budget_line()
compare_budget_actual()
```

---

# 41. Project Service

`ProjectService` SHALL manage:

```text
create_project()
update_project()
change_status()
set_responsible()
get_project()
search_projects()
close_project()
cancel_project()
get_project_financials()
```

---

# 42. Project Repository

`ProjectRepository` SHALL manage persistence for:

- projects;
- project metadata;
- project queries;
- project relationships.

It SHALL not calculate accounting balances independently.

---

# 43. Budget Repository

`BudgetRepository` SHALL manage:

- budgets;
- budget lines;
- budget versions where implemented.

---

# 44. Project Financial Service

A dedicated `ProjectFinancialService` MAY coordinate:

```text
AccountingService
+
ProjectService
+
BudgetService
```

to produce project financial views.

---

# 45. Accounting Integration

The project module SHALL use:

```text
AccountingService
```

for:

- project income;
- project expenses;
- project adjustments;
- financial reports.

It SHALL not write directly to accounting tables.

---

# 46. Project Budget Integration

Budget data is planning data.

Accounting data is actual data.

The report layer combines them.

```text
BudgetRepository
        +
AccountingService
        ↓
Project Financial Report
```

---

# 47. Project Cost Allocation

A voucher line MAY contain:

```text
account_id
project_id
amount
```

This is sufficient for most small association project accounting.

Complex cost allocation is not required for v1.0.

---

# 48. Shared Costs

A shared cost MAY need allocation between projects.

MFM v1.0 MAY support manual split lines.

Example:

```text
Expense 1,000

Project A   600
Project B   400
```

The total accounting amount SHALL remain balanced.

---

# 49. Shared Cost Rule

Allocated project amounts SHALL never exceed the underlying transaction amount unless a controlled allocation method explicitly supports another representation.

---

# 50. Project Income Allocation

Income MAY be allocated to a project using the same project identifier on the relevant voucher line.

---

# 51. Project Budget Controls

The system MAY warn when:

```text
ACTUAL > BUDGET
```

It SHALL not automatically block accounting unless the association explicitly configures such a control.

---

# 52. Budget Warning Levels

Recommended:

```text
NORMAL       < 80%
WARNING      80–100%
OVER BUDGET  > 100%
```

Thresholds SHALL be configurable.

---

# 53. Funding Warning

The system SHOULD warn when:

```text
Funding gap > 0
```

for a project expected to be fully funded.

---

# 54. Project Status Controls

A completed project SHALL normally reject new project transactions unless an authorised user reopens it.

A cancelled project SHALL normally reject new transactions.

Exceptions SHALL be audited.

---

# 55. Project Reopening

Reopening a completed or cancelled project SHALL require:

- appropriate permission;
- reason;
- audit event.

---

# 56. Project Closure

Before closure:

```text
CHECK UNPOSTED
CHECK OPEN GRANTS
CHECK OUTSTANDING FUNDING
CHECK BUDGET
CHECK DOCUMENTS
CHECK FINAL REPORT
```

The user then confirms closure.

---

# 57. Project Completion

Completion does not delete data.

The project remains available for:

- reporting;
- audit;
- historical analysis;
- document access.

---

# 58. Project Cancellation

Cancellation SHALL record:

- date;
- user;
- reason.

Existing accounting history remains untouched.

---

# 59. Project Reports

Minimum:

1. Project overview
2. Project budget
3. Project actual
4. Budget versus actual
5. Project income
6. Project expenditure
7. Funding overview
8. Funding gap
9. Project transaction list
10. Project final report

---

# 60. Project Final Report

Recommended structure:

```text
Project
Period
Budget
Actual Income
Actual Expense
Result
Confirmed Funding
Funding Gap
Key Documents
Status
```

---

# 61. Annual Project Overview

The association SHOULD be able to see:

```text
ACTIVE PROJECTS
TOTAL PROJECT BUDGET
TOTAL PROJECT ACTUAL
TOTAL FUNDING
TOTAL FUNDING GAP
```

---

# 62. Portfolio Overview

A simple project portfolio screen MAY show:

| Project | Budget | Actual | Variance | Funding | Status |
|---|---:|---:|---:|---:|---|

This is sufficient for MFM v1.0.

No enterprise portfolio engine is required.

---

# 63. Project Search

Search SHOULD support:

- project number;
- project name;
- responsible person;
- status.

---

# 64. Project Permissions

Recommended:

```text
VIEW_PROJECT
CREATE_PROJECT
EDIT_PROJECT
MANAGE_BUDGET
APPROVE_BUDGET
VIEW_PROJECT_FINANCE
CLOSE_PROJECT
EXPORT_PROJECT
```

---

# 65. Financial Approval

Project responsibility does not automatically grant financial posting authority.

```text
PROJECT RESPONSIBILITY
        ≠
ACCOUNTING AUTHORITY
```

This separation SHALL remain explicit.

---

# 66. Project Budget Approval

Budget approval SHOULD require an appropriate role.

For a small association this may be:

```text
TREASURER
```

or:

```text
ADMIN
```

according to association policy.

---

# 67. Project Changes

Material project changes SHOULD create audit events:

```text
PROJECT_CREATED
PROJECT_UPDATED
PROJECT_STATUS_CHANGED
BUDGET_CREATED
BUDGET_APPROVED
BUDGET_CHANGED
PROJECT_CLOSED
PROJECT_REOPENED
```

---

# 68. Negative Testing

```text
Duplicate project number → BLOCK
Missing project name → BLOCK
Invalid project status → BLOCK
Invalid budget amount → BLOCK
Budget line without project → BLOCK
Unauthorised budget approval → BLOCK
Post to cancelled project → BLOCK / WARN
Post to completed project → BLOCK / WARN
Project actual without valid voucher → BLOCK
Project transaction without valid account → BLOCK
Budget version changed without audit → BLOCK
Delete project with financial history → BLOCK
Delete project financial history → BLOCK
Funding gap incorrectly calculated → TEST FAILURE
Actual not matching ledger → TEST FAILURE
Database failure during project update → ROLLBACK
```

---

# 69. Acceptance Test — Project Creation

Create:

```text
P-2027-001
Restoration Project
ACTIVE
```

Expected:

```text
project created
unique project number
audit event
```

---

# 70. Acceptance Test — Budget

Create:

```text
Budget = 200,000
```

Expected:

```text
budget stored
status DRAFT
```

Approve budget.

Expected:

```text
status APPROVED
audit event
```

---

# 71. Acceptance Test — Project Expense

Post:

```text
Expense 20,000
Project P-2027-001
```

Expected:

```text
Project actual expense = 20,000
Budget remains 200,000
Variance = 180,000
```

---

# 72. Acceptance Test — Project Income

Post:

```text
Income 50,000
Project P-2027-001
```

Expected:

```text
Project income = 50,000
```

---

# 73. Acceptance Test — Funding Gap

Budget:

```text
200,000
```

Confirmed funding:

```text
150,000
```

Expected:

```text
Funding gap = 50,000
```

---

# 74. Acceptance Test — Over Budget

Budget:

```text
100,000
```

Actual:

```text
110,000
```

Expected:

```text
Actual > Budget
Warning = OVER BUDGET
```

Accounting SHALL remain intact.

---

# 75. Acceptance Test — Project Closure

Project with no unresolved blocking items is completed.

Expected:

```text
status = COMPLETED
audit event
historical financial data preserved
```

---

# 76. Acceptance Test — Traceability

Select project actual amount.

Expected navigation:

```text
Project Report
 ↓
Project Transaction
 ↓
Voucher Line
 ↓
Voucher
 ↓
Account
```

---

# 77. Budget Variance Logic

For expense:

```text
Variance = Budget - Actual
```

For income:

```text
Variance = Actual - Budget
```

The report SHALL present favourable/unfavourable meaning clearly rather than relying only on the sign.

---

# 78. Forecast

A future enhancement MAY calculate:

```text
ACTUAL TO DATE
+
EXPECTED REMAINING
=
FORECAST
```

Forecast values SHALL be clearly distinguished from posted actuals.

---

# 79. Project Risk

MFM v1.0 MAY display simple project warnings:

```text
OVER BUDGET
FUNDING GAP
DEADLINE NEAR
GRANT REPORT DUE
PROJECT INACTIVE
```

No complex risk engine is required.

---

# 80. Project Deadlines

Projects MAY have:

- start date;
- planned end date;
- reporting deadlines;
- funding deadlines.

The system SHOULD expose upcoming deadlines.

---

# 81. Grant Deadline Integration

A project overview SHOULD show related grant deadlines.

Example:

```text
Grant report due: 2027-10-15
```

---

# 82. Project Documents

A project document list SHOULD show:

```text
File
Type
Date
Related entity
```

Documents SHALL open through the document service.

---

# 83. Project Import

Projects MAY be imported from CSV/XLSX.

Import flow:

```text
IMPORT
 ↓
VALIDATE
 ↓
PREVIEW
 ↓
CONFIRM
 ↓
CREATE
 ↓
AUDIT
```

---

# 84. Project Export

Project export SHOULD include:

```text
project number
name
status
budget
actual
variance
funding
funding gap
```

---

# 85. Excel Project Report

The XLSX report MAY contain:

```text
Project Summary
Budget
Actual
Variance
Funding
Transactions
```

---

# 86. Project Dashboard Integration

Main dashboard MAY show:

```text
Active Projects: 5
Total Project Budget: DKK xxx
Project Actual: DKK xxx
Funding Gap: DKK xxx
Projects Over Budget: 1
```

Values SHALL derive from services.

---

# 87. Database Relationships

```text
projects
   |
   +---- budget_lines
   |
   +---- grants
   |
   +---- documents
   |
   +---- voucher_lines
```

The accounting relationship is:

```text
projects.id
   ↓
voucher_lines.project_id
```

---

# 88. Repository Boundaries

Project repository handles project data.

Budget repository handles budget data.

Accounting repository handles accounting data.

No repository SHALL duplicate another repository's authoritative information.

---

# 89. Service Boundaries

```text
ProjectService
BudgetService
ProjectFinancialService
GrantService
AccountingService
DocumentService
```

They cooperate through explicit service contracts.

---

# 90. Project Financial Query

A project financial query SHALL conceptually calculate:

```text
INCOME
= SUM(project-linked income)

EXPENSE
= SUM(project-linked expense)

RESULT
= INCOME - EXPENSE

BUDGET
= SUM(project budget lines)

VARIANCE
= BUDGET - EXPENSE
```

Account type determines whether a transaction is income or expense.

---

# 91. Data Integrity

Project financial totals SHALL never be stored as manually editable values.

They SHALL be calculated from:

- budget data;
- posted accounting data;
- funding data.

Caching MAY be used later, but authoritative recalculation SHALL remain possible.

---

# 92. Auditability

A project report SHALL be reproducible from the database.

The same data and report parameters should produce the same financial result.

---

# 93. Performance

For expected association scale:

```text
SQLite
+
indexed project_id
+
indexed voucher_date
```

is sufficient.

No data warehouse is required.

---

# 94. Security

Users SHALL only access project financial information permitted by their roles.

Project documents may have additional restrictions.

---

# 95. Backup

Project data, budgets, grants and linked document metadata SHALL be included in the standard MFM backup.

Project documents SHALL be included in document backup.

---

# 96. Error Handling

Examples:

```text
"The project number already exists."
"The project is closed and cannot receive new transactions."
"The budget cannot be approved by this user."
"The selected account is not valid."
"The project budget has not been approved."
```

Technical errors SHALL be logged separately.

---

# 97. Development Sequence

```text
1. Project model
2. Budget model
3. Project repository
4. Budget repository
5. Project service
6. Budget service
7. Financial query service
8. Accounting integration
9. Grant integration
10. Project GUI
11. Budget GUI
12. Reports
13. Export
14. Tests
```

---

# 98. Suggested Files

```text
src/
├── models/
│   ├── project.py
│   └── budget.py
│
├── repositories/
│   ├── project_repository.py
│   └── budget_repository.py
│
├── services/
│   ├── project_service.py
│   ├── budget_service.py
│   └── project_financial_service.py
│
└── gui/
    ├── projects.py
    ├── project_detail.py
    └── budget.py
```

Existing MFM files MAY be reused and refactored.

---

# 99. Definition of Done

Projects & Budget v1.0 is complete when:

- projects can be created;
- project numbers are unique;
- project status works;
- responsibility works;
- budgets can be created;
- budgets can be approved;
- budget lines work;
- project-linked accounting works;
- actual values come from posted accounting;
- budget versus actual works;
- funding is visible;
- funding gaps are calculated;
- grants can be linked;
- project documents can be linked;
- project reports work;
- export works;
- project closure works;
- audit works;
- negative tests pass.

---

# 100. Relationship to Previous Modules

```text
Architecture Baseline
       ↓
Database Foundation
       ↓
Accounting Core
       ↓
Membership
       ↓
Projects & Budget
```

Projects use the Accounting Core for actual financial information.

Membership may generate project-related activity but remains independent.

Grants extend project funding information.

---

# 101. Final Governing Principle

> **Projects SHALL make the association's activities understandable financially without creating a second accounting system.**

MFM v1.0 therefore keeps the architecture deliberately simple:

```text
PLAN
 ↓
BUDGET
 ↓
EXECUTE
 ↓
ACCOUNT
 ↓
COMPARE
 ↓
REPORT
 ↓
CLOSE
```

# END OF MFM v1.0 PROJECTS & BUDGET
