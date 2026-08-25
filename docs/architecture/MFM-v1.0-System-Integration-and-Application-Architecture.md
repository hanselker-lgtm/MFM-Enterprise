# MFM v1.0 SYSTEM INTEGRATION & APPLICATION ARCHITECTURE

## MaritimForeningsManager — Samlet applikationsarkitektur, modulintegration og runtime-struktur

**Version:** 1.0  
**Status:** Development Baseline  
**Parent:** MFM v1.0 Security, Users & Audit  
**Purpose:** Define the complete application-level architecture that integrates the MFM v1.0 modules into one maintainable association management application

---

# 1. Purpose

This document defines how the MFM v1.0 modules operate together as one application.

The objective is not to add another business module.

The objective is to establish the actual technical structure connecting:

```text
GUI
SERVICES
REPOSITORIES
DATABASE
DOCUMENT STORAGE
REPORTING
SECURITY
AUDIT
BACKUP
```

The architecture SHALL remain appropriate for a small almennyttig association.

---

# 2. Core Principle

> **MFM shall be one coherent application with clear module boundaries, one authoritative database, one accounting truth, one security model and controlled integration between modules.**

The preferred architecture is:

```text
USER
 ↓
GUI
 ↓
SERVICE LAYER
 ↓
REPOSITORY / DOMAIN ACCESS
 ↓
DATABASE
```

Cross-cutting services:

```text
SECURITY
AUDIT
DOCUMENT STORAGE
REPORTING
BACKUP
CONFIGURATION
```

---

# 3. Complete MFM Architecture

```text
                         USER
                           |
                           v
                    +-------------+
                    |     GUI     |
                    +------+------+ 
                           |
                           v
                 +-------------------+
                 | APPLICATION LAYER |
                 +---------+---------+
                           |
        +------------------+------------------+
        |         |          |        |       |
     Members  Accounting Projects  Grants Documents
        |         |          |        |       |
        +---------+----------+--------+-------+
                           |
                     SERVICE LAYER
                           |
                    +------+------+
                    | REPOSITORIES|
                    +------+------+
                           |
                    +------+------+
                    |   DATABASE  |
                    +-------------+

Cross-cutting:
Security / Audit / Reporting / Storage / Backup / Configuration
```

---

# 4. Architectural Layers

MFM SHALL use these conceptual layers:

```text
1. Presentation
2. Application Services
3. Domain / Business Rules
4. Persistence
5. Infrastructure
```

---

# 5. Presentation Layer

The presentation layer contains:

- windows;
- forms;
- lists;
- dashboards;
- dialogs;
- reports;
- navigation.

The presentation layer SHALL not contain core business rules.

---

# 6. Application Service Layer

Services coordinate business operations.

Examples:

```text
MemberService
AccountingService
ProjectService
BudgetService
GrantService
DocumentService
ReportService
DashboardService
AuthService
UserService
AuditService
```

---

# 7. Domain / Business Rules

Business rules SHALL define:

- valid statuses;
- valid transitions;
- accounting rules;
- fee rules;
- project rules;
- grant rules;
- security rules.

Rules SHALL not depend on GUI widgets.

---

# 8. Persistence Layer

Repositories provide controlled database access.

Examples:

```text
MemberRepository
AccountingRepository
ProjectRepository
BudgetRepository
GrantRepository
DocumentRepository
UserRepository
AuditRepository
```

---

# 9. Infrastructure Layer

Infrastructure includes:

```text
SQLite
File Storage
PDF generation
XLSX generation
Backup
Logging
Operating System Integration
```

---

# 10. Dependency Direction

The preferred dependency direction is:

```text
GUI
 ↓
Services
 ↓
Repositories
 ↓
Database
```

Infrastructure services may be called through service abstractions.

Repositories SHALL not depend on GUI modules.

---

# 11. GUI Boundary

GUI modules SHALL:

- display data;
- collect input;
- invoke services;
- show results;
- show validation errors.

GUI modules SHALL NOT:

- post SQL directly;
- implement accounting rules;
- calculate authoritative financial balances;
- bypass permission checks.

---

# 12. Service Boundary

Services SHALL:

- validate business rules;
- enforce permissions;
- coordinate transactions;
- call repositories;
- create audit events;
- return application-level results.

---

# 13. Repository Boundary

Repositories SHALL:

- query data;
- persist data;
- map database records;
- execute parameterised SQL.

Repositories SHALL not decide whether a business operation is permitted.

---

# 14. Database Boundary

The database SHALL provide:

- persistence;
- relational integrity;
- constraints;
- indexes;
- transactions.

The database is not the application business-rule engine.

---

# 15. MFM Module Map

```text
MFM v1.0
|
+-- Core
|   +-- Configuration
|   +-- Database
|   +-- Logging
|
+-- Security
|   +-- Authentication
|   +-- Authorisation
|   +-- Users
|   +-- Roles
|   +-- Audit
|
+-- Finance
|   +-- Accounting
|   +-- Bank
|   +-- Budget
|
+-- Association
|   +-- Members
|   +-- Membership
|
+-- Projects
|   +-- Projects
|   +-- Project Budget
|   +-- Funding
|
+-- Grants
|
+-- Documents
|
+-- Reporting
|
+-- Dashboard
|
+-- Backup
```

---

# 16. Startup Architecture

Application startup SHALL follow a controlled sequence.

```text
START
 ↓
LOAD CONFIGURATION
 ↓
INITIALISE LOGGING
 ↓
OPEN DATABASE
 ↓
VERIFY SCHEMA
 ↓
INITIALISE SECURITY
 ↓
INITIALISE SERVICES
 ↓
START GUI
```

---

# 17. Startup Failure

If a critical dependency fails:

```text
DATABASE UNAVAILABLE
```

the application SHALL not continue as though normal operation were possible.

The user SHALL receive a clear message.

---

# 18. Configuration

Configuration SHOULD contain:

```text
database path
document root
backup root
export root
application settings
security settings
```

Configuration SHALL not contain plaintext passwords or secrets.

---

# 19. Environment Separation

The application SHOULD distinguish:

```text
DEVELOPMENT
TEST
PRODUCTION
```

The default production database SHALL not be used for automated destructive tests.

---

# 20. Database Initialization

On first startup:

```text
DATABASE EXISTS?
   |
   +-- NO → CREATE DATABASE
   |
   +-- YES → VERIFY SCHEMA
```

Schema creation SHALL be idempotent.

---

# 21. Database Migration

Future schema changes SHALL use explicit migrations.

Example:

```text
001_initial
002_membership
003_projects
004_grants
```

MFM v1.0 SHOULD maintain a schema version.

---

# 22. Database Connection

Database connections SHALL be managed centrally.

Services SHOULD not create uncontrolled connections throughout the application.

---

# 23. Transaction Management

Business operations involving multiple changes SHALL use transactions.

Example:

```text
BEGIN
 ↓
VALIDATE
 ↓
WRITE DATA
 ↓
WRITE AUDIT
 ↓
COMMIT
```

Failure:

```text
ROLLBACK
```

---

# 24. Atomicity

The application SHALL avoid partial operations.

Example:

A payment registration must not:

```text
update fee
```

without also completing its required accounting and audit operation.

---

# 25. Accounting as Financial Authority

All actual financial transactions SHALL pass through:

```text
AccountingService
```

This includes transactions initiated by:

- membership;
- projects;
- grants;
- bank reconciliation.

---

# 26. Membership Integration

Membership fee flow:

```text
MembershipService
 ↓
Create Fee
 ↓
AccountingService
 ↓
Accounting Entry
 ↓
AuditService
```

---

# 27. Payment Integration

Payment flow:

```text
Payment Input
 ↓
MembershipService
 ↓
Validate
 ↓
AccountingService
 ↓
Update Fee
 ↓
Audit
 ↓
Commit
```

---

# 28. Project Integration

Project financial flow:

```text
Project
 ↓
Voucher Line.project_id
 ↓
AccountingService
 ↓
Accounting Ledger
```

Project reports query accounting data through controlled services.

---

# 29. Budget Integration

Budget flow:

```text
BudgetService
 ↓
Budget Repository
 ↓
Budget Data

AccountingService
 ↓
Actual Data

ReportService
 ↓
Budget vs Actual
```

---

# 30. Grant Integration

Grant approval is not the same as receipt.

```text
GrantService
 ↓
APPROVED
```

Actual receipt:

```text
GrantService
 ↓
AccountingService
 ↓
Bank / Income Transaction
```

---

# 31. Document Integration

Documents may be linked to:

```text
Member
Project
Grant
Voucher
General
```

The document service owns storage operations.

---

# 32. Reporting Integration

Reporting consumes:

```text
AccountingService
MembershipService
ProjectService
GrantService
DocumentService
```

It SHALL not bypass these services to obtain inconsistent business interpretations.

---

# 33. Dashboard Integration

Dashboard consumes reporting and summary services.

```text
DashboardService
 ↓
Summary Queries
 ↓
GUI Widgets
```

---

# 34. Security Integration

Every protected service operation SHALL use:

```text
AuthService
PermissionService
```

or equivalent central security functionality.

---

# 35. Audit Integration

Material service operations SHALL use:

```text
AuditService
```

Audit events SHALL be generated consistently across modules.

---

# 36. Error Handling Architecture

Errors SHALL be divided into:

```text
Validation Error
Permission Error
Business Rule Error
Database Error
Infrastructure Error
Unexpected Error
```

---

# 37. Validation Error

Example:

```text
Member name missing.
```

The GUI can display the message directly.

---

# 38. Permission Error

Example:

```text
You do not have permission to post this voucher.
```

The business operation SHALL not execute.

---

# 39. Business Rule Error

Example:

```text
A membership fee already exists for this year.
```

The transaction SHALL not execute.

---

# 40. Database Error

Example:

```text
Database unavailable.
```

The application SHALL rollback where appropriate and log technical detail.

---

# 41. Infrastructure Error

Example:

```text
Unable to store document.
```

No incomplete document reference SHALL remain.

---

# 42. Unexpected Error

Unexpected exceptions SHALL:

- be logged;
- show a safe user message;
- avoid exposing stack traces to ordinary users.

---

# 43. Exception Boundary

GUI event handlers SHOULD have a final exception boundary.

Conceptually:

```text
try:
    service_operation()
except ApplicationError:
    show_user_message()
except Exception:
    log_exception()
    show_safe_error()
```

---

# 44. Logging

Application logging SHOULD use levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Production default SHOULD avoid excessive debug output.

---

# 45. Logging Security

Logs SHALL not contain:

- passwords;
- authentication secrets;
- unnecessary personal data.

---

# 46. Audit versus Log

The distinction is:

```text
AUDIT
= business accountability

LOG
= technical diagnostics
```

They SHALL not be treated as the same mechanism.

---

# 47. Application Navigation

Recommended main menu:

```text
Dashboard
Members
Accounting
Projects
Grants
Documents
Reports
Administration
```

---

# 48. Dashboard Entry

The application SHOULD open on the dashboard after login.

Users without dashboard access MAY be directed to their authorised module.

---

# 49. Main Window

Recommended structure:

```text
+------------------------------------------------+
| MFM | Current User | Financial Year            |
+------------------+-----------------------------+
| Navigation       | Main Content                |
|                  |                             |
| Dashboard        |                             |
| Members          |                             |
| Accounting       |                             |
| Projects         |                             |
| Grants           |                             |
| Documents        |                             |
| Reports          |                             |
| Administration   |                             |
+------------------+-----------------------------+
```

---

# 50. User Context

The main window SHOULD display:

```text
Current user
Current financial year
Application version
```

---

# 51. Global Navigation

Navigation SHALL respect permissions.

Unavailable modules SHOULD be hidden or disabled.

---

# 52. Financial Year Context

Accounting screens SHALL clearly display the selected financial year.

Changing financial year SHALL not silently change existing transactions.

---

# 53. Module Independence

Modules SHALL be independently testable.

Example:

```text
MemberService
```

can be tested without launching the GUI.

---

# 54. Service Testability

Services SHOULD accept dependencies through controlled construction.

This improves unit testing.

---

# 55. Repository Testability

Repositories SHOULD be testable against a dedicated test database.

---

# 56. Test Database

Automated tests SHALL never use the production association database.

Recommended:

```text
tests/data/test.db
```

created fresh or reset for test execution.

---

# 57. Test Data

Test data SHALL be synthetic.

No real member personal data should be embedded in automated tests.

---

# 58. Test Categories

MFM SHALL support:

```text
Unit Tests
Service Tests
Repository Tests
Integration Tests
GUI Tests
Security Tests
Accounting Tests
Regression Tests
```

---

# 59. Unit Tests

Unit tests SHALL verify isolated business rules.

Examples:

```text
fee calculation
status transition
budget variance
funding gap
permission check
```

---

# 60. Service Tests

Service tests SHALL verify:

```text
validation
transactions
permissions
audit
integration
```

---

# 61. Repository Tests

Repository tests SHALL verify:

```text
create
read
update
query
constraints
transactions
```

---

# 62. Integration Tests

Integration tests SHALL verify module interaction.

Examples:

```text
Membership → Accounting
Project → Accounting
Grant → Project
Document → Project
Reporting → Accounting
Security → All protected services
```

---

# 63. Regression Tests

Every corrected defect SHOULD become a regression test.

This prevents previous errors from returning.

---

# 64. Accounting Integration Test

Scenario:

```text
Create membership fee
 ↓
Register payment
 ↓
Accounting transaction
 ↓
Report
```

Expected:

```text
Fee paid
Ledger correct
Audit present
Report correct
```

---

# 65. Project Integration Test

Scenario:

```text
Create project
 ↓
Create budget
 ↓
Post expense
 ↓
Project report
```

Expected:

```text
Actual correct
Variance correct
Ledger correct
```

---

# 66. Grant Integration Test

Scenario:

```text
Create grant
 ↓
Approve grant
 ↓
Receive payment
 ↓
Accounting
 ↓
Project funding report
```

Expected:

```text
Approved amount correct
Received amount correct
Accounting correct
Funding gap correct
```

---

# 67. Document Integration Test

Scenario:

```text
Create project
 ↓
Add document
 ↓
Open document
 ↓
Integrity check
```

Expected:

```text
document linked
file accessible
checksum valid
```

---

# 68. Security Integration Test

Scenario:

```text
Read-only user
 ↓
Attempt financial posting
```

Expected:

```text
DENIED
NO DATA CHANGE
AUDIT / SECURITY EVENT
```

---

# 69. Reporting Integration Test

Scenario:

```text
Post transactions
 ↓
Generate report
```

Expected:

```text
report reflects posted transactions
draft data excluded from official report
```

---

# 70. Database Integrity

Database integrity SHALL be checked through:

```text
foreign keys
unique constraints
not-null constraints
check constraints
transactions
```

---

# 71. Foreign Keys

Where relationships exist:

```text
project_id
member_id
grant_id
user_id
```

foreign-key integrity SHOULD be enforced.

---

# 72. Unique Constraints

At minimum:

```text
member_number
project_number
grant_number
username
```

SHALL be unique.

---

# 73. Check Constraints

Examples:

```text
amount >= 0
end_date >= start_date
```

where appropriate.

---

# 74. Referential Integrity

Historical records SHALL not be orphaned.

Example:

A voucher line referencing a project SHALL reference a valid project or use an explicitly allowed null relationship.

---

# 75. Deletion Policy

MFM SHALL prefer:

```text
DEACTIVATE
ARCHIVE
CANCEL
REVERSE
```

over destructive deletion when history exists.

---

# 76. Financial Deletion

Posted financial transactions SHALL never be physically deleted through normal application functionality.

Corrections use:

```text
REVERSAL
```

or controlled adjustment.

---

# 77. Membership Deletion

Historical members SHALL normally be:

```text
LEFT
```

rather than deleted.

---

# 78. Project Deletion

Projects with financial history SHALL not be deleted.

Use:

```text
CANCELLED
```

or:

```text
COMPLETED
```

---

# 79. Grant Deletion

Grant records with historical activity SHALL be retained.

Use:

```text
REJECTED
WITHDRAWN
COMPLETED
```

---

# 80. Document Deletion

Important historical documents SHOULD be archived rather than destroyed.

---

# 81. Configuration Architecture

Configuration SHALL be centralised.

Recommended:

```text
config.py
settings repository
```

The GUI SHALL not maintain separate hidden configuration values.

---

# 82. Configuration Categories

```text
DATABASE
STORAGE
ACCOUNTING
MEMBERSHIP
PROJECTS
SECURITY
REPORTING
BACKUP
```

---

# 83. Configuration Validation

On startup:

```text
LOAD
 ↓
VALIDATE
 ↓
DEFAULTS
 ↓
READY
```

Invalid configuration SHALL produce a clear error.

---

# 84. File Structure

Recommended target architecture:

```text
MaritimForeningsManager/
|
+-- run.py
+-- requirements.txt
+-- README.md
|
+-- src/
|   |
|   +-- main.py
|   |
|   +-- config/
|   |   +-- settings.py
|   |
|   +-- database/
|   |   +-- db.py
|   |   +-- schema.py
|   |   +-- migrations/
|   |
|   +-- models/
|   |
|   +-- repositories/
|   |
|   +-- services/
|   |
|   +-- reports/
|   |
|   +-- gui/
|   |
|   +-- security/
|   |
|   +-- infrastructure/
|   |
|   +-- utils/
|
+-- data/
|   +-- mfm.db
|
+-- documents/
|
+-- backups/
|
+-- exports/
|
+-- tests/
```

---

# 85. Existing Project Compatibility

Existing MFM files MAY be retained if they follow these boundaries.

The objective is not to rewrite every file.

The objective is to remove architectural conflicts.

---

# 86. Import Rule

Imports SHOULD flow toward lower-level abstractions.

Avoid circular dependencies.

Example of prohibited pattern:

```text
services → gui
```

Services SHALL not import GUI modules.

---

# 87. Circular Dependency Prevention

Preferred:

```text
models
 ↓
repositories
 ↓
services
 ↓
gui
```

Cross-cutting services use controlled interfaces.

---

# 88. Main Entry Point

`run.py` SHOULD remain a thin launcher.

Example conceptual flow:

```text
run.py
 ↓
src.main.start_app()
 ↓
Application bootstrap
 ↓
GUI
```

---

# 89. Application Bootstrap

A dedicated bootstrap component MAY create:

```text
database
repositories
services
security
reporting
GUI
```

This avoids uncontrolled global state.

---

# 90. Dependency Construction

Preferred:

```text
Database
 ↓
Repositories
 ↓
Services
 ↓
GUI
```

Dependencies SHALL be created in a predictable order.

---

# 91. Global State

MFM SHOULD minimise global mutable state.

Examples to avoid:

```text
global database connection
global current user
global accounting service
```

without controlled lifecycle.

---

# 92. Current User Context

The current user SHOULD be represented by a session/context object.

Services receive or access the authenticated context through a controlled mechanism.

---

# 93. Application Context

An `ApplicationContext` MAY contain:

```text
database
current_user
services
configuration
```

This is preferable to arbitrary globals.

---

# 94. GUI Event Flow

Example:

```text
Button Click
 ↓
Validate Form
 ↓
Call Service
 ↓
Service Authorises
 ↓
Service Executes
 ↓
Audit
 ↓
Return Result
 ↓
Refresh GUI
```

---

# 95. GUI Refresh

After a successful change, the relevant view SHALL refresh from authoritative data.

The GUI SHALL not simply alter a displayed number and assume persistence succeeded.

---

# 96. Service Result

Services MAY return structured results:

```text
success
data
message
errors
```

or use typed application exceptions.

Consistency is more important than the exact mechanism.

---

# 97. User Validation

Basic field validation may occur in GUI.

Business validation SHALL occur in the service.

Example:

```text
GUI:
email looks valid

Service:
member rules satisfied
```

---

# 98. Database Validation

Database constraints provide final structural protection.

Three levels:

```text
GUI validation
SERVICE validation
DATABASE constraints
```

---

# 99. Error Propagation

Errors SHALL move upward in controlled form:

```text
Database Exception
 ↓
Repository Exception
 ↓
Service/Application Error
 ↓
GUI Message
```

Raw database errors SHOULD not be shown directly to ordinary users.

---

# 100. Reporting Export Flow

```text
User
 ↓
Report GUI
 ↓
ReportService
 ↓
Authoritative Services
 ↓
Report Model
 ↓
Exporter
 ↓
XLSX / PDF / CSV
```

---

# 101. Document Flow

```text
User
 ↓
Document GUI
 ↓
DocumentService
 ↓
StorageService
 ↓
File System
 ↓
AuditService
```

---

# 102. Grant Flow

```text
User
 ↓
Grant GUI
 ↓
GrantService
 ↓
GrantRepository
 ↓
Database
 ↓
AuditService
```

---

# 103. Project Flow

```text
User
 ↓
Project GUI
 ↓
ProjectService
 ↓
ProjectRepository
 ↓
Database
```

Financial view:

```text
ProjectFinancialService
 ↓
AccountingService
 ↓
Ledger
```

---

# 104. Membership Flow

```text
User
 ↓
Member GUI
 ↓
MembershipService
 ↓
MemberRepository
 ↓
Database
```

Financial flow:

```text
MembershipService
 ↓
AccountingService
```

---

# 105. Accounting Flow

```text
User
 ↓
Accounting GUI
 ↓
AccountingService
 ↓
AccountingRepository
 ↓
Database
 ↓
AuditService
```

---

# 106. Security Flow

```text
Login
 ↓
AuthService
 ↓
UserRepository
 ↓
Session
 ↓
PermissionService
```

Every protected service uses the current security context.

---

# 107. Backup Flow

```text
User / Scheduler
 ↓
BackupService
 ↓
Database Backup
 ↓
Document Backup
 ↓
Verification
 ↓
Audit
```

---

# 108. Restore Flow

```text
Administrator
 ↓
RestoreService
 ↓
Confirmation
 ↓
Backup Validation
 ↓
Restore
 ↓
Integrity Check
 ↓
Audit
```

---

# 109. Backup Architecture

A backup SHALL cover:

```text
DATABASE
DOCUMENTS
CONFIGURATION REQUIRED FOR RESTORE
```

The backup strategy SHALL be documented.

---

# 110. Export Directory

Generated reports SHALL use a controlled export directory.

The system SHOULD prevent accidental writing to arbitrary system paths.

---

# 111. Document Directory

The document root SHALL be configurable.

The application SHALL normalise and validate paths.

---

# 112. Database Directory

The database path SHALL be configurable.

Production and test databases SHALL remain separate.

---

# 113. Packaging

MFM v1.0 SHOULD eventually be distributable as a Windows application.

The packaging mechanism is separate from the application architecture.

---

# 114. Windows Desktop Target

The application is intended for ordinary Windows use by an association.

The user should not need to understand:

```text
Python
SQLite
database schema
repository
service layer
```

to operate MFM.

---

# 115. User Experience Principle

The application SHALL prioritise:

```text
SIMPLE
CLEAR
SAFE
CONSISTENT
```

---

# 116. Main Use Cases

MFM v1.0 SHALL support these practical workflows:

```text
1. Register member
2. Generate membership fees
3. Register payment
4. Enter invoice/voucher
5. Post accounting
6. Reconcile bank
7. Create project
8. Create project budget
9. Track project expenditure
10. Register grant
11. Track grant
12. Store documents
13. Generate reports
14. Review dashboard
15. Backup system
```

---

# 117. End-to-End Membership Workflow

```text
Create Member
 ↓
Create Membership
 ↓
Generate Fee
 ↓
Register Payment
 ↓
Accounting
 ↓
Dashboard
```

---

# 118. End-to-End Project Workflow

```text
Create Project
 ↓
Create Budget
 ↓
Approve Budget
 ↓
Execute Project
 ↓
Post Costs
 ↓
Track Variance
 ↓
Close Project
 ↓
Final Report
```

---

# 119. End-to-End Grant Workflow

```text
Create Grant
 ↓
Prepare
 ↓
Submit
 ↓
Approve
 ↓
Receive Funding
 ↓
Accounting
 ↓
Project Funding
 ↓
Report
 ↓
Complete
```

---

# 120. End-to-End Document Workflow

```text
Select File
 ↓
Validate
 ↓
Store
 ↓
Checksum
 ↓
Link
 ↓
Audit
 ↓
Retrieve
```

---

# 121. End-to-End Financial Workflow

```text
Source Document
 ↓
Voucher
 ↓
Validation
 ↓
Posting
 ↓
Ledger
 ↓
Reconciliation
 ↓
Reports
```

---

# 122. End-to-End Governance Workflow

```text
Data
 ↓
Report
 ↓
Review
 ↓
Board / Treasurer Decision
 ↓
Authorised Action
 ↓
Audit
```

---

# 123. Cross-Module Transaction Example

A grant payment for a restoration project:

```text
Grant G-2027-001
       ↓
Project P-2027-001
       ↓
Bank receipt
       ↓
AccountingService
       ↓
Voucher
       ↓
Project financials
       ↓
Grant received
       ↓
Dashboard
```

There is one financial transaction, not several competing records.

---

# 124. Cross-Module Integrity

The same event SHALL not create contradictory amounts.

Example:

```text
Accounting receipt = 50,000
Grant received = 50,000
Project funding = 50,000
```

These are views of the same authoritative financial event.

---

# 125. Source of Truth Matrix

| Information | Authoritative Source |
|---|---|
| Member identity | Membership |
| Membership status | Membership |
| Fee obligation | Membership |
| Posted accounting | Accounting Core |
| Bank balance | Accounting Core |
| Project definition | Projects |
| Project budget | Budget |
| Project actual | Accounting Core |
| Grant status | Grants |
| Grant approval | Grants |
| Grant cash received | Accounting Core |
| Document metadata | Documents |
| Physical file | Document Storage |
| User identity | Security |
| Permissions | Security |
| Audit history | Audit |
| Management report | Reporting |

---

# 126. Duplicate Data Rule

If the same value appears in multiple modules, one source SHALL be authoritative.

Example:

```text
Project budget
```

belongs to:

```text
BudgetService
```

A dashboard merely displays it.

---

# 127. Calculated Data Rule

Calculated values SHOULD be derived rather than manually maintained.

Examples:

```text
Outstanding fee
Project variance
Funding gap
Dashboard totals
```

---

# 128. Financial Calculation Rule

Financial totals SHALL use posted accounting data.

Drafts SHALL not affect official financial reports unless explicitly requested.

---

# 129. Audit Rule

Every material state-changing operation SHALL be auditable.

Read-only operations do not all need audit events.

---

# 130. Security Rule

Every protected operation SHALL be authorised before state change.

---

# 131. Document Rule

Document metadata and file storage SHALL remain consistent.

---

# 132. Backup Rule

A backup SHALL be considered complete only when both database and required document storage are included.

---

# 133. Reporting Rule

Reports SHALL never silently invent or approximate authoritative financial figures.

---

# 134. Integration Error Handling

If one module calls another and the downstream operation fails:

```text
NO PARTIAL SUCCESS
```

where the operation is transactional.

---

# 135. Example Payment Failure

If payment registration fails while accounting is unavailable:

```text
Fee remains unchanged
Accounting remains unchanged
Audit remains unchanged
User receives error
```

No partial payment status SHALL be saved.

---

# 136. Example Document Failure

If file storage succeeds but metadata creation fails:

The system SHALL clean up the orphaned file where possible.

If cleanup is impossible, an administrator warning SHALL be created.

---

# 137. Example Project Failure

If project creation fails:

```text
No incomplete project
No orphan budget
No audit claiming success
```

---

# 138. Example Grant Failure

If grant creation succeeds but required audit fails:

```text
ROLLBACK
```

where the operation requires atomic auditing.

---

# 139. Application Shutdown

Normal shutdown SHALL:

```text
stop background tasks
close database connections
flush logs
close GUI
```

---

# 140. Unexpected Shutdown

The database transaction model SHALL protect against partial committed transactions.

SQLite recovery mechanisms SHALL be allowed to operate normally.

---

# 141. Database Backup Before Major Changes

Before major schema migrations, the application SHOULD create or require a verified backup.

---

# 142. Versioning

Application version SHALL be visible.

Example:

```text
MFM v1.0.0
```

Database schema version SHALL be separate.

---

# 143. Compatibility

Application startup SHOULD verify that the database schema is compatible.

If not:

```text
MIGRATION REQUIRED
```

The application SHALL not silently use an incompatible schema.

---

# 144. Upgrade Process

Recommended:

```text
BACKUP
 ↓
VERIFY
 ↓
MIGRATE
 ↓
VERIFY
 ↓
START APPLICATION
```

---

# 145. Rollback Strategy

If migration fails:

```text
STOP
 ↓
REPORT FAILURE
 ↓
RESTORE BACKUP
```

The exact automated rollback mechanism may depend on migration complexity.

---

# 146. Development Priorities

The implementation priority SHALL be:

```text
1. Correctness
2. Data integrity
3. Security
4. Usability
5. Reporting
6. Performance
7. Optional sophistication
```

---

# 147. Complexity Control

MFM v1.0 SHALL not implement enterprise features merely because they are technically possible.

Avoid unnecessary:

```text
microservices
message brokers
distributed databases
cloud orchestration
complex workflow engines
```

---

# 148. Deployment Model

Recommended v1.0:

```text
Single Windows application
+
SQLite database
+
controlled document directory
+
local backup
```

This is sufficient for a small association.

---

# 149. Future Multi-User Model

If future requirements justify a networked deployment, the service boundaries should allow migration toward:

```text
Desktop / Web Client
        ↓
Application Server
        ↓
Database
```

This is not required for v1.0.

---

# 150. Performance Target

For normal association data volumes:

```text
screen response < 2 seconds
```

SHOULD be the general target for common operations.

Large exports may take longer.

---

# 151. Reliability Target

The application SHALL prioritise:

```text
no lost transactions
no silent data corruption
no duplicate financial posting
```

over visual sophistication.

---

# 152. Observability

Administrators SHOULD be able to identify:

```text
application error
database error
backup failure
document failure
authentication problem
```

through logs and system-health information.

---

# 153. Maintenance

The architecture SHALL permit maintenance of one module without unnecessary changes to unrelated modules.

Example:

Changing document storage should not require rewriting accounting.

---

# 154. Refactoring Rule

When existing code violates the architecture:

```text
IDENTIFY
 ↓
ISOLATE
 ↓
REFACTOR
 ↓
TEST
```

Do not perform uncontrolled rewrites.

---

# 155. Existing MFM Error Prevention

The architecture specifically prevents common errors such as:

```text
undefined service variable
wrong module import
GUI calling missing service
database connection created in wrong layer
accounting logic in GUI
circular imports
```

The implementation SHALL use explicit imports and dependency construction.

---

# 156. Import Validation

Application startup or automated tests SHOULD verify critical imports.

Example:

```text
src.main
src.services
src.repositories
src.gui
```

A broken import SHALL fail early during development.

---

# 157. Service Availability

The application bootstrap SHALL construct required services before opening dependent GUI modules.

---

# 158. Missing Dependency

If a required service cannot be constructed:

```text
APPLICATION STARTUP FAILURE
```

rather than allowing a later `NameError` or `AttributeError`.

---

# 159. Database Service Availability

If the database service is unavailable, the application SHALL show a controlled startup error.

---

# 160. GUI Error Prevention

GUI modules SHALL receive service dependencies explicitly where practical.

This reduces hidden globals and undefined variables.

---

# 161. Code Quality

MFM v1.0 code SHOULD follow:

- clear naming;
- small functions;
- single responsibility;
- explicit dependencies;
- type hints where useful;
- docstrings for important services;
- consistent error handling.

---

# 162. Naming Convention

Python files:

```text
snake_case.py
```

Classes:

```text
PascalCase
```

Functions:

```text
snake_case()
```

Constants:

```text
UPPER_CASE
```

---

# 163. Service Naming

Use:

```text
AccountingService
MemberService
ProjectService
GrantService
DocumentService
```

Avoid vague names such as:

```text
Helper
Manager
Utils
```

for major business components.

---

# 164. Repository Naming

Use:

```text
AccountingRepository
MemberRepository
ProjectRepository
```

---

# 165. GUI Naming

GUI file names should identify purpose:

```text
main_window.py
dashboard.py
members.py
projects.py
grants.py
documents.py
reports.py
```

---

# 166. Testing Directory

Recommended:

```text
tests/
├── unit/
├── services/
├── repositories/
├── integration/
├── security/
└── regression/
```

---

# 167. Test Naming

Examples:

```text
test_create_member()
test_duplicate_project_number()
test_payment_updates_fee()
test_unauthorised_posting()
```

---

# 168. Application Acceptance

MFM v1.0 SHALL be considered functionally integrated when the following complete workflows operate:

```text
Member → Fee → Payment → Accounting → Report

Project → Budget → Expense → Accounting → Report

Grant → Approval → Payment → Accounting → Project → Report

Document → Project/Grant → Retrieval → Backup

User → Login → Permission → Action → Audit
```

---

# 169. Final Integration Test

The final integration test SHOULD execute a realistic association scenario:

```text
Create member
 ↓
Create membership
 ↓
Generate fee
 ↓
Register payment
 ↓
Create project
 ↓
Create budget
 ↓
Create grant
 ↓
Approve grant
 ↓
Receive funding
 ↓
Post project expense
 ↓
Attach documents
 ↓
Generate reports
 ↓
Review dashboard
 ↓
Verify audit
 ↓
Create backup
```

Expected:

```text
NO DATA INCONSISTENCY
NO DUPLICATE ACCOUNTING
ALL MATERIAL ACTIONS AUDITED
REPORTS RECONCILE
BACKUP COMPLETE
```

---

# 170. Definition of Done

System Integration & Application Architecture v1.0 is complete when:

- the application has clear layers;
- GUI is separated from business logic;
- services are explicit;
- repositories are explicit;
- database access is centralised;
- modules integrate through services;
- accounting remains authoritative;
- security is centralised;
- audit is centralised;
- documents are controlled;
- reporting is read-oriented;
- backup is integrated;
- transactions are atomic;
- imports are controlled;
- tests are separated from production;
- startup is controlled;
- configuration is centralised;
- the application can be packaged as a coherent Windows application.

---

# 171. Final Architecture

The final MFM v1.0 architecture is:

```text
                         USER
                           |
                           v
                    +-------------+
                    |     GUI     |
                    +------+------+ 
                           |
                           v
                 +-------------------+
                 | APPLICATION LAYER |
                 +---------+---------+
                           |
       +------------------+------------------+
       |          |          |        |       |
   MEMBERS  ACCOUNTING PROJECTS GRANTS DOCUMENTS
       |          |          |        |       |
       +----------+----------+--------+-------+
                           |
                    +------+------+
                    | REPOSITORIES|
                    +------+------+
                           |
                    +------+------+
                    |   DATABASE  |
                    +-------------+

CROSS-CUTTING:
SECURITY
AUDIT
REPORTING
DOCUMENT STORAGE
BACKUP
CONFIGURATION
LOGGING
```

---

# 172. Governing Architectural Rules

```text
RULE 1
GUI SHALL NOT CONTAIN CORE BUSINESS LOGIC.

RULE 2
SERVICES SHALL ENFORCE BUSINESS RULES.

RULE 3
REPOSITORIES SHALL OWN PERSISTENCE ACCESS.

RULE 4
ACCOUNTING CORE SHALL BE THE FINANCIAL SOURCE OF TRUTH.

RULE 5
REPORTING SHALL NOT CREATE AUTHORITATIVE DATA.

RULE 6
SECURITY SHALL BE ENFORCED BELOW THE GUI.

RULE 7
MATERIAL STATE CHANGES SHALL BE AUDITED.

RULE 8
HISTORICAL FINANCIAL DATA SHALL NOT BE DELETED.

RULE 9
DOCUMENT STORAGE SHALL BE CONTROLLED.

RULE 10
BACKUPS SHALL INCLUDE DATABASE AND REQUIRED DOCUMENTS.

RULE 11
TESTS SHALL NEVER MODIFY PRODUCTION DATA.

RULE 12
MFM v1.0 SHALL REMAIN PROPORTIONATE TO A SMALL ASSOCIATION.
```

---

# 173. Practical Architecture Statement

MFM v1.0 is intentionally not an enterprise platform in the commercial sense.

It is a structured association application with:

```text
ONE APPLICATION
ONE DATABASE
ONE ACCOUNTING TRUTH
ONE SECURITY MODEL
ONE AUDIT TRAIL
CONTROLLED DOCUMENT STORAGE
CLEAR REPORTING
```

This is sufficient for the intended association use case.

---

# 174. Final Governing Principle

> **MFM v1.0 shall be simple enough for volunteers and robust enough to protect the association's financial, membership, project and documentary history.**

The architecture therefore follows:

```text
SIMPLE
   +
MODULAR
   +
TRACEABLE
   +
SECURE
   +
MAINTAINABLE
```

# END OF MFM v1.0 SYSTEM INTEGRATION & APPLICATION ARCHITECTURE
