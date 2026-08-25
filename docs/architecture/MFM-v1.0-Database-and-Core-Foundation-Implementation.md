# MFM v1.0 DATABASE & CORE FOUNDATION IMPLEMENTATION

## MaritimForeningsManager — Konkret implementeringsgrundlag for database, application bootstrap, configuration and core infrastructure

**Version:** 1.0  
**Status:** Implementation Baseline  
**Parent:** MFM v1.0 Implementation Baseline & Development Plan  
**Purpose:** Establish the concrete technical foundation on which the remaining MFM v1.0 modules SHALL be implemented

---

# 1. Purpose

This document converts the MFM v1.0 architecture into a concrete implementation baseline for the lowest application layer.

It defines:

- project structure;
- application startup;
- configuration;
- database connection;
- SQLite setup;
- schema versioning;
- migrations;
- transaction handling;
- base models;
- repository conventions;
- application context;
- logging;
- error handling;
- test database;
- backup foundation;
- implementation rules.

This document SHALL be treated as the foundation for the implementation files that follow.

---

# 2. Scope

This file covers the technical foundation only.

It does not implement the complete:

- accounting module;
- membership module;
- project module;
- grant module;
- document module;
- reporting module.

Those modules SHALL build on this foundation.

---

# 3. Core Principle

> **The foundation must be boring, predictable and reliable.**

The core infrastructure SHALL avoid unnecessary abstraction.

Preferred:

```text
Python
  ↓
Application Context
  ↓
Services
  ↓
Repositories
  ↓
SQLite
```

---

# 4. Target Project Structure

```text
MaritimForeningsManager/
│
├── run.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── schema.py
│   │   └── migrations/
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── base.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── base.py
│   │
│   ├── services/
│   │   └── __init__.py
│   │
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   └── logging_config.py
│   │
│   └── utils/
│       └── __init__.py
│
├── data/
├── documents/
├── backups/
├── exports/
│
└── tests/
    ├── unit/
    ├── integration/
    └── data/
```

---

# 5. Entry Point

The application SHALL have one primary entry point:

```text
run.py
```

Its responsibility SHALL be minimal.

Conceptually:

```python
from src.main import start_app

if __name__ == "__main__":
    start_app()
```

---

# 6. Entry Point Rule

`run.py` SHALL not:

- create database tables;
- implement business logic;
- create GUI widgets;
- contain accounting logic;
- manage user permissions.

It only starts the application.

---

# 7. Main Application

`src/main.py` SHALL coordinate startup.

Conceptual sequence:

```text
start_app()
    ↓
load settings
    ↓
configure logging
    ↓
initialize database
    ↓
verify schema
    ↓
create repositories
    ↓
create services
    ↓
create application context
    ↓
start GUI
```

---

# 8. Startup Failure

Any critical startup failure SHALL stop normal application startup.

Examples:

```text
database cannot be opened
schema migration failed
configuration invalid
required directory cannot be created
```

The application SHALL show a controlled message.

---

# 9. Configuration

Configuration SHALL be centralised.

The application SHALL not contain unrelated hard-coded paths throughout the codebase.

---

# 10. Settings Object

A settings object SHOULD expose:

```text
application_name
application_version
database_path
document_root
backup_root
export_root
log_root
test_mode
```

---

# 11. Default Paths

Recommended:

```text
data/mfm.db
documents/
backups/
exports/
logs/
```

Paths MAY be changed later through configuration.

---

# 12. Path Handling

Python `pathlib.Path` SHOULD be used for file-system paths.

Avoid manually concatenating paths with:

```text
/
\
```

---

# 13. Directory Initialization

Startup MAY create required directories:

```text
data
documents
backups
exports
logs
```

Creation SHALL be idempotent.

---

# 14. Production and Test Paths

Production:

```text
data/mfm.db
```

Test:

```text
tests/data/test.db
```

The two environments SHALL remain separate.

---

# 15. Database Technology

MFM v1.0 SHALL use:

```text
SQLite
```

for the initial deployment.

SQLite is appropriate because MFM is intended for a small association and a local Windows application.

---

# 16. SQLite Connection

The database module SHALL provide a controlled connection mechanism.

A central `Database` or `DatabaseManager` component SHOULD be used.

---

# 17. Connection Requirements

Connections SHOULD enable:

```sql
PRAGMA foreign_keys = ON;
```

Foreign keys SHALL be enforced.

---

# 18. Row Access

The application SHOULD use a row factory that permits named column access.

This improves readability.

---

# 19. Connection Lifecycle

The application SHALL avoid uncontrolled persistent connections.

Preferred:

```text
open
 ↓
operation
 ↓
commit / rollback
 ↓
close
```

or a controlled application-scoped connection manager.

---

# 20. Transactions

A transaction SHALL group changes that must succeed together.

Example:

```text
BEGIN
 ↓
write A
 ↓
write B
 ↓
write audit
 ↓
COMMIT
```

---

# 21. Rollback

If an operation fails:

```text
ROLLBACK
```

No partial business transaction SHALL remain.

---

# 22. Transaction Context

A transaction context manager SHOULD be provided.

Conceptually:

```python
with database.transaction() as connection:
    ...
```

---

# 23. Read Operations

Read-only queries SHOULD not require explicit write transactions.

---

# 24. Write Operations

Repositories performing multiple related writes SHOULD receive an existing transaction connection rather than opening unrelated connections.

---

# 25. Transaction Ownership

The service layer SHOULD own transaction boundaries for business operations.

Repositories perform persistence work.

---

# 26. Example

Correct:

```text
MembershipService
    ↓
BEGIN TRANSACTION
    ↓
MemberRepository
FeeRepository
AccountingRepository
AuditRepository
    ↓
COMMIT
```

Incorrect:

```text
MemberRepository commits
FeeRepository commits
AccountingRepository commits
```

because partial success becomes possible.

---

# 27. Database Schema Version

The database SHALL contain a schema version.

Recommended table:

```text
schema_version
```

with one current version.

---

# 28. Schema Version Fields

Minimum:

```text
version
updated_at
```

---

# 29. Initial Schema

The first release SHALL have:

```text
version = 1
```

---

# 30. Migration Model

Future migrations SHALL be numbered:

```text
001_initial.py
002_membership.py
003_accounting.py
004_projects.py
```

The exact numbering may change during development.

---

# 31. Migration Principle

Migrations SHALL be:

- ordered;
- explicit;
- testable;
- deterministic.

---

# 32. Migration Startup

Startup logic:

```text
read current schema version
        ↓
compare required version
        ↓
apply pending migrations
        ↓
verify
```

---

# 33. Migration Failure

If a migration fails:

```text
rollback
log error
stop startup
```

The application SHALL not continue against a partially migrated database.

---

# 34. Backup Before Migration

Before a production schema migration, a verified backup SHOULD exist.

---

# 35. Initial Core Schema

The foundation SHOULD establish tables required by the architecture.

At minimum:

```text
schema_version
users
roles
permissions
user_roles
role_permissions
audit_events
```

Business-module tables MAY be introduced by their respective modules.

---

# 36. User Table

Conceptual fields:

```text
id
username
display_name
password_hash
status
created_at
updated_at
last_login_at
```

---

# 37. Role Table

Conceptual:

```text
id
name
description
```

---

# 38. Permission Table

Conceptual:

```text
id
name
description
```

---

# 39. User Role Table

Conceptual:

```text
user_id
role_id
```

A unique constraint SHALL prevent duplicate assignments.

---

# 40. Role Permission Table

Conceptual:

```text
role_id
permission_id
```

A unique constraint SHALL prevent duplicates.

---

# 41. Audit Table

Conceptual:

```text
id
timestamp
user_id
event_type
entity_type
entity_id
description
old_value
new_value
reason
```

---

# 42. Audit Immutability

Normal application operations SHALL not update or delete audit events.

---

# 43. Audit Foreign Keys

The audit user reference MAY be nullable where an event occurred before authentication or during system startup.

Historical audit integrity remains more important than forced user linkage.

---

# 44. Base Model

A simple base model convention MAY define:

```text
id
created_at
updated_at
```

Not every entity must inherit every field if it is not appropriate.

---

# 45. Model Principle

Models represent data.

They SHALL not:

- open GUI windows;
- access widgets;
- perform SQL directly;
- decide permissions.

---

# 46. Repository Principle

Repositories translate between:

```text
domain/application objects
```

and:

```text
database rows
```

---

# 47. Repository Base

A base repository MAY provide:

```text
connection
execute
fetch_one
fetch_all
```

but SHALL remain lightweight.

---

# 48. Repository SQL

SQL SHALL use parameters.

Correct:

```python
connection.execute(
    "SELECT * FROM users WHERE id = ?",
    (user_id,)
)
```

Incorrect:

```python
connection.execute(
    f"SELECT * FROM users WHERE id = {user_id}"
)
```

---

# 49. SQL Injection Rule

User-controlled values SHALL never be concatenated into SQL.

---

# 50. Repository Error Handling

Repositories SHOULD translate low-level database errors into application-relevant exceptions where practical.

---

# 51. Service Layer

Services coordinate:

```text
validation
permission
transaction
repository
audit
result
```

---

# 52. Application Context

A central context SHOULD expose:

```text
settings
database
services
current_user/session
```

---

# 53. Dependency Construction

The application bootstrap SHALL construct dependencies explicitly.

Conceptual:

```text
database
 ↓
repositories
 ↓
services
 ↓
context
 ↓
GUI
```

---

# 54. Avoid Global Services

Do not solve dependency problems by adding:

```python
global account_service
```

or similar variables.

This was one of the failure patterns identified during earlier MFM development.

---

# 55. Service Injection

If `ReportService` needs `AccountingService`, it SHALL receive it explicitly.

Conceptually:

```python
ReportService(accounting_service=accounting_service)
```

---

# 56. Circular Import Prevention

Services SHALL not import GUI modules.

GUI modules may import service interfaces or receive services through application context.

---

# 57. Import Direction

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

Configuration and infrastructure are shared lower-level components.

---

# 58. Infrastructure

Infrastructure MAY contain:

```text
database
logging
file storage
backup
export
```

These components SHALL not contain association-specific GUI logic.

---

# 59. Logging

Logging SHALL be configured centrally.

Recommended:

```text
logs/mfm.log
```

---

# 60. Log Levels

Use:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Production SHOULD default to `INFO` or a similarly useful level.

---

# 61. Log Format

Recommended:

```text
timestamp
level
module
message
```

---

# 62. Logging Sensitive Data

Logs SHALL not contain:

```text
password
password hash
authentication token
unnecessary member personal data
```

---

# 63. Application Exceptions

MFM SHOULD define application-level exceptions such as:

```text
ApplicationError
ValidationError
PermissionError
BusinessRuleError
DatabaseError
ConfigurationError
```

---

# 64. Exception Hierarchy

Conceptually:

```text
ApplicationError
├── ValidationError
├── PermissionError
├── BusinessRuleError
├── DatabaseError
└── ConfigurationError
```

---

# 65. GUI Error Boundary

The GUI SHALL translate application exceptions into understandable messages.

---

# 66. Unexpected Exception

Unexpected exceptions SHALL:

```text
log technical details
show safe user message
avoid exposing stack trace
```

---

# 67. Health Check

The application SHOULD have a basic startup health check:

```text
database
schema
directories
configuration
```

---

# 68. Health Status

Possible:

```text
OK
WARNING
ERROR
```

---

# 69. Database Health

Check:

```text
database opens
foreign keys enabled
schema version valid
```

---

# 70. Storage Health

Check required directories:

```text
documents
backups
exports
logs
```

---

# 71. Configuration Health

Invalid configuration SHALL stop or degrade only the affected subsystem.

---

# 72. Backup Foundation

A backup service SHALL eventually support:

```text
database backup
document backup
verification
restore
```

---

# 73. Database Backup

SQLite backup SHOULD use the SQLite backup API or another reliable mechanism rather than copying an actively changing database blindly.

---

# 74. Document Backup

Required document files SHALL be copied into the backup structure.

---

# 75. Backup Manifest

A backup SHOULD include a manifest:

```text
backup_id
created_at
application_version
schema_version
database_file
document_count
```

---

# 76. Backup Verification

After creation:

```text
backup exists
database backup readable
required documents present
manifest valid
```

---

# 77. Restore Foundation

Restore SHALL be administrator-controlled.

Before restore:

```text
confirm
verify backup
protect current state
```

---

# 78. Test Database

Automated tests SHALL use a separate SQLite database.

---

# 79. Test Database Lifecycle

Recommended:

```text
create
 ↓
migrate
 ↓
seed
 ↓
test
 ↓
destroy/reset
```

---

# 80. Test Seed Data

Seed data MAY include:

```text
test admin
test treasurer
test member
test project
test account
```

All test data SHALL be clearly synthetic.

---

# 81. Test Mode

A test mode MAY be used to select test paths.

Production mode SHALL never accidentally use test data.

---

# 82. Database Reset

A development utility MAY provide:

```text
reset_test_database()
```

It SHALL never operate on production data without an explicit safety mechanism.

---

# 83. Core Tests

Foundation tests SHALL cover:

```text
database creation
schema version
foreign keys
transaction commit
transaction rollback
repository parameterisation
configuration
logging
```

---

# 84. Test — Database Creation

Expected:

```text
database file created
schema_version exists
core tables exist
```

---

# 85. Test — Foreign Keys

Create a child record referencing a nonexistent parent.

Expected:

```text
constraint failure
```

---

# 86. Test — Transaction Commit

Write valid records.

Expected:

```text
records persist
```

---

# 87. Test — Transaction Rollback

Write valid record A.

Write invalid record B.

Expected:

```text
A is not persisted
```

if both belong to the same transaction.

---

# 88. Test — Schema Migration

Start at version 1.

Apply migration.

Expected:

```text
version increments
required changes exist
```

---

# 89. Test — Migration Failure

Simulate migration failure.

Expected:

```text
database not left in partial migration state
startup blocked
```

---

# 90. Test — Configuration

Load default settings.

Expected:

```text
valid paths
valid application version
valid database path
```

---

# 91. Test — Production/Test Separation

Attempt to run tests.

Expected:

```text
test database selected
production database untouched
```

---

# 92. Test — Logging

Trigger a controlled error.

Expected:

```text
error logged
no password logged
```

---

# 93. Test — Dependency Construction

Create application context.

Expected:

```text
database exists
repositories available
services available
```

---

# 94. Test — Import Health

Import:

```text
src.main
src.database
src.repositories
src.services
```

Expected:

```text
no circular import
no missing module
```

---

# 95. Startup Contract

`start_app()` SHALL:

```text
load config
configure logging
initialize database
verify schema
construct services
launch application
```

---

# 96. Startup Contract — Failure

If database initialization fails:

```text
do not construct normal GUI
show controlled error
log technical cause
```

---

# 97. Main Window Contract

The GUI SHALL receive an application context.

It SHALL not recreate the database independently.

---

# 98. Application Context Contract

The context SHOULD provide access to:

```text
settings
database
security
accounting
membership
projects
grants
documents
reports
backup
```

As modules are implemented.

---

# 99. Incremental Context

Early implementation may contain only:

```text
settings
database
```

Later services are added without changing the fundamental bootstrap pattern.

---

# 100. Core Infrastructure Files

Minimum first implementation:

```text
run.py
src/main.py
src/config/settings.py
src/database/db.py
src/database/schema.py
src/models/base.py
src/repositories/base.py
src/infrastructure/logging_config.py
```

---

# 101. File Responsibility — run.py

Only:

```text
launch application
```

---

# 102. File Responsibility — main.py

Responsible for:

```text
bootstrap
dependency construction
GUI launch
```

---

# 103. File Responsibility — settings.py

Responsible for:

```text
paths
version
configuration
```

---

# 104. File Responsibility — db.py

Responsible for:

```text
connection
transactions
database lifecycle
```

---

# 105. File Responsibility — schema.py

Responsible for:

```text
schema initialization
schema version
migration coordination
```

---

# 106. File Responsibility — base.py

Responsible for:

```text
common model conventions
```

Only where useful.

---

# 107. File Responsibility — repositories/base.py

Responsible for:

```text
common repository database helpers
```

---

# 108. File Responsibility — logging_config.py

Responsible for:

```text
central logging configuration
```

---

# 109. Configuration Object

Recommended conceptual structure:

```python
@dataclass
class Settings:
    application_name: str
    application_version: str
    database_path: Path
    document_root: Path
    backup_root: Path
    export_root: Path
    log_root: Path
    test_mode: bool = False
```

---

# 110. Settings Factory

Provide:

```text
get_settings()
```

The factory SHALL construct predictable paths relative to the application root where appropriate.

---

# 111. Application Root

The application SHOULD determine its project/application root rather than depending on the current working directory.

This prevents errors when launched from a shortcut.

---

# 112. Working Directory Rule

MFM SHALL not assume:

```text
os.getcwd()
```

is the application root.

---

# 113. Database Path Rule

Database paths SHALL be absolute or reliably resolved paths before opening.

---

# 114. Storage Root Rule

Document storage SHALL be resolved once in configuration.

Modules SHALL not invent their own document roots.

---

# 115. Export Root Rule

All report exports SHOULD be placed under the configured export root.

---

# 116. Logging Root Rule

All application logs SHOULD be placed under the configured log root.

---

# 117. Database Connection API

A minimal API MAY provide:

```text
connect()
close()
execute()
fetch_one()
fetch_all()
transaction()
```

The implementation SHALL avoid unnecessary complexity.

---

# 118. Repository API

A repository MAY provide:

```text
get_by_id()
list()
create()
update()
```

Specific repositories SHOULD expose domain-specific methods.

---

# 119. Domain-Specific Repository Methods

Example:

```text
MemberRepository.get_active_members()
FeeRepository.get_outstanding()
ProjectRepository.get_active_projects()
```

These are preferable to placing business queries in GUI code.

---

# 120. Service API

Services SHOULD expose business operations rather than generic CRUD only.

Example:

```text
MembershipService.generate_fee()
AccountingService.post_voucher()
ProjectService.close_project()
GrantService.record_approval()
```

---

# 121. Generic CRUD Limitation

Avoid building an application where every module consists only of:

```text
create()
read()
update()
delete()
```

Business workflows need explicit operations.

---

# 122. Delete Policy

Core infrastructure SHALL support safe deletion policies.

Business modules decide whether deletion is allowed.

---

# 123. IDs

SQLite integer primary keys MAY be used internally.

Public business identifiers SHOULD be separate where needed:

```text
MEM-0001
PROJ-0001
GRANT-0001
```

---

# 124. Timestamps

Timestamps SHOULD be stored consistently.

Recommended:

```text
UTC internally
localized for display
```

For a local association application, a consistent local convention may be used if documented.

---

# 125. Date Storage

Dates SHOULD be stored in ISO-compatible form:

```text
YYYY-MM-DD
```

---

# 126. Amount Storage

Financial amounts SHALL not use floating-point arithmetic for authoritative accounting.

Use integer minor units or `Decimal`.

Recommended:

```text
Decimal
```

at service level and a controlled database representation.

---

# 127. Currency

MFM v1.0 SHALL use a defined primary currency.

For the intended Danish association:

```text
DKK
```

is the default.

The architecture SHALL allow later extension if needed.

---

# 128. Money Rule

Never use:

```python
float
```

for authoritative accounting calculations.

---

# 129. Decimal Rule

All financial calculations SHALL use:

```text
Decimal
```

or integer minor units consistently.

---

# 130. Validation Rule

Before persistence:

```text
validate
normalize
persist
```

---

# 131. Null Rule

Database NULL SHALL be used only where the field is genuinely optional.

Avoid meaningless NULL values.

---

# 132. Status Values

Statuses SHOULD use controlled values.

Avoid arbitrary free-text status fields for business-critical workflows.

---

# 133. Enum Strategy

Python enums MAY represent controlled status values.

Database storage can use stable strings.

---

# 134. Naming

Database table names SHOULD be consistent.

Recommended:

```text
users
roles
permissions
audit_events
```

---

# 135. Indexes

Indexes SHALL be created for frequently searched fields.

Examples:

```text
username
member_number
project_number
grant_number
audit timestamp
```

---

# 136. Index Rule

Do not create indexes without a query or integrity reason.

---

# 137. Foreign Key Rule

Every relationship SHALL be intentional.

Examples:

```text
project_id
member_id
grant_id
user_id
```

---

# 138. Unique Constraint Rule

Business identifiers SHALL have unique constraints where required.

---

# 139. Audit Timestamp Index

`audit_events.timestamp` SHOULD be indexed for audit browsing.

---

# 140. User Username Index

`users.username` SHALL be unique.

---

# 141. Core Schema Acceptance

The database foundation SHALL be considered complete when:

```text
application starts
database opens
schema verifies
migrations work
transactions work
logging works
test database works
```

---

# 142. Development Sequence

Implement the foundation in this order:

```text
1. settings.py
2. db.py
3. schema.py
4. logging_config.py
5. base models
6. base repository
7. main.py
8. run.py
9. tests
```

---

# 143. Why This Order

Configuration must exist before database paths.

Database must exist before repositories.

Repositories must exist before services.

Bootstrap must construct everything in dependency order.

---

# 144. First Working Milestone

The first milestone SHALL be:

```text
python run.py
```

resulting in a working application shell with:

```text
database initialized
schema verified
logging active
main window opens
```

No accounting or membership features are required at this milestone.

---

# 145. Second Working Milestone

Add:

```text
User
Role
Permission
Login
```

The application can then have a controlled authenticated shell.

---

# 146. Third Working Milestone

Add:

```text
Chart of Accounts
Voucher
Posting
Trial Balance
```

This establishes financial correctness.

---

# 147. Fourth Working Milestone

Add:

```text
Members
Membership
Fees
Payments
```

---

# 148. Fifth Working Milestone

Add:

```text
Projects
Budgets
```

---

# 149. Sixth Working Milestone

Add:

```text
Grants
Documents
```

---

# 150. Seventh Working Milestone

Add:

```text
Reports
Dashboard
Backup
```

---

# 151. Final Working Milestone

Complete:

```text
integration
security
testing
packaging
acceptance
```

---

# 152. Implementation Rule — One Stable Baseline

When a foundation component works and tests pass, treat it as a stable baseline.

Do not continually redesign it while building unrelated modules.

---

# 153. Implementation Rule — Small Changes

Prefer:

```text
small change
 ↓
test
 ↓
commit
```

rather than large uncontrolled changes.

---

# 154. Implementation Rule — Regression

Every repaired defect SHOULD receive a regression test.

---

# 155. Implementation Rule — No Hidden Fixes

A workaround SHALL be documented.

Avoid hidden changes that only make one screen work.

---

# 156. Implementation Rule — One Source of Truth

Configuration:

```text
one source
```

Database:

```text
one production database
```

Accounting:

```text
one financial source
```

Security:

```text
one permission model
```

Audit:

```text
one audit service
```

---

# 157. Error Prevention

The foundation specifically addresses common MFM development failures:

```text
NameError
ModuleNotFoundError
ImportError
circular imports
undefined service
wrong database path
test/production confusion
```

---

# 158. Undefined Service Prevention

Every service dependency SHALL be constructed before use.

Conceptually:

```python
accounting_service = AccountingService(...)
project_service = ProjectService(
    accounting_service=accounting_service
)
```

Never assume a variable exists.

---

# 159. Import Error Prevention

Every package directory SHOULD contain:

```text
__init__.py
```

where the chosen Python packaging approach requires it.

---

# 160. Module Path Consistency

Use one consistent import style throughout the application.

Do not mix incompatible import paths such as:

```text
gui.main_window
src.gui.main_window
```

arbitrarily.

---

# 161. Recommended Import Style

When launching from the project root, use:

```text
from src....
```

consistently.

---

# 162. GUI Import Rule

GUI modules SHALL import services from their actual package location.

No dynamic guessing of module names.

---

# 163. Test Import Rule

Tests SHALL import the application using the same package structure as production.

---

# 164. Main Window Dependency Rule

The main window SHALL receive services/context.

It SHALL not contain:

```text
from database... import random helper
```

for every operation.

---

# 165. Database Schema Ownership

Schema changes SHALL have one owner:

```text
src/database/
```

Business modules may provide migration definitions but shall not independently create tables at runtime.

---

# 166. Table Creation Rule

Do not scatter:

```sql
CREATE TABLE
```

through services or GUI modules.

---

# 167. Seed Data

Initial system data such as standard roles and permissions MAY be seeded during initialization.

Seed operations SHALL be idempotent.

---

# 168. Default Roles

Recommended initial roles:

```text
ADMIN
TREASURER
BOARD
MEMBER_ADMIN
PROJECT_MANAGER
READ_ONLY
```

---

# 169. Default Permissions

Seed only permissions required by the v1.0 modules.

Avoid hundreds of unused permissions.

---

# 170. Default Administrator

A first-run administrator setup SHOULD require explicit password creation.

Do not ship a universal default password.

---

# 171. First-Run Flow

Recommended:

```text
FIRST START
 ↓
DATABASE INITIALIZE
 ↓
CREATE ADMINISTRATOR
 ↓
LOGIN
 ↓
DASHBOARD
```

---

# 172. First-Run Safety

The initial administrator password SHALL never be hard-coded.

---

# 173. First-Run Completion

Once administrator setup is complete:

```text
first_run = false
```

or equivalent state SHALL be stored.

---

# 174. Configuration Storage

User-editable configuration MAY be stored separately from database business data.

Do not place passwords in configuration files.

---

# 175. Backup Configuration

Backup paths and schedules MAY be configured.

The backup configuration itself SHALL be included in recovery documentation.

---

# 176. Core Security Baseline

Even before all business modules exist:

```text
password hashing
role checks
audit
```

SHALL be established.

---

# 177. Core Audit Baseline

At minimum audit:

```text
login
user creation
role change
configuration changes
```

As business modules are added, their material actions are added.

---

# 178. Core Logging Baseline

Log:

```text
startup
shutdown
database initialization
migration
errors
backup
restore
```

---

# 179. Startup Log Example

Conceptually:

```text
INFO Application starting
INFO Configuration loaded
INFO Database initialized
INFO Schema version 1
INFO Services constructed
INFO GUI starting
```

---

# 180. Shutdown Log Example

```text
INFO Application shutting down
INFO Database closed
INFO Application stopped
```

---

# 181. Database Error Log Example

Technical logs MAY include:

```text
ERROR Database operation failed
```

with diagnostic details.

User messages remain simpler.

---

# 182. Backup Log Example

```text
INFO Backup started
INFO Database backup completed
INFO Document backup completed
INFO Backup verification completed
```

---

# 183. Restore Log Example

```text
WARNING Restore requested
INFO Backup verified
INFO Restore completed
INFO Integrity check completed
```

---

# 184. Application Health

The main application MAY expose:

```text
Database: OK
Schema: OK
Storage: OK
Backup: OK
```

---

# 185. Core GUI Shell

The first GUI milestone may contain:

```text
MFM
Dashboard
Administration
Exit
```

Business modules are added later.

---

# 186. GUI Shell Rule

The GUI shell SHALL start even if optional modules are not yet implemented, provided the core foundation is healthy.

---

# 187. Missing Module Handling

If an optional module is not yet implemented, the application SHALL not crash.

It may show:

```text
Feature not yet available.
```

during development.

---

# 188. Production Rule

Incomplete development placeholders SHALL not be included in the final production release.

---

# 189. Version Display

The GUI SHOULD display:

```text
MFM v1.0
```

and optionally schema version.

---

# 190. Developer Diagnostic

A development-only diagnostic screen MAY show:

```text
Python version
database path
schema version
application version
```

This SHOULD be hidden from ordinary users.

---

# 191. Core Foundation Checklist

```text
[ ] run.py exists
[ ] src.main exists
[ ] settings exists
[ ] database manager exists
[ ] schema version exists
[ ] migrations exist
[ ] logging exists
[ ] application context exists
[ ] base repository exists
[ ] test database exists
```

---

# 192. Database Checklist

```text
[ ] SQLite connection
[ ] foreign keys
[ ] transactions
[ ] rollback
[ ] schema initialization
[ ] schema migration
[ ] indexes
[ ] constraints
```

---

# 193. Startup Checklist

```text
[ ] configuration loaded
[ ] paths resolved
[ ] directories created
[ ] database opened
[ ] schema verified
[ ] services constructed
[ ] GUI launched
```

---

# 194. Security Checklist

```text
[ ] password hashing
[ ] first-run admin setup
[ ] roles
[ ] permissions
[ ] audit
[ ] no plaintext passwords
```

---

# 195. Test Checklist

```text
[ ] database creation
[ ] transaction commit
[ ] transaction rollback
[ ] migration
[ ] test isolation
[ ] import health
[ ] configuration
[ ] logging
```

---

# 196. Release Gate — Foundation

The foundation SHALL not be considered complete until:

```text
run.py starts successfully
database initializes
schema verifies
test database works
transaction tests pass
imports pass
logging works
```

---

# 197. Practical Implementation Guidance

The next implementation work SHALL create the foundation files before adding complex business screens.

Do not begin with:

```text
advanced dashboard
AI
complex reports
```

before the database and service foundation is stable.

---

# 198. Practical Development Loop

Use:

```text
EDIT
 ↓
RUN
 ↓
TEST
 ↓
FIX
 ↓
COMMIT
```

Repeat frequently.

---

# 199. Source Control

The project SHOULD use Git.

Recommended commit boundaries:

```text
foundation
database
security
accounting
membership
projects
grants
documents
reporting
integration
release
```

---

# 200. Commit Rule

A commit SHOULD represent a coherent change.

Avoid committing a half-finished unrelated collection of changes.

---

# 201. Backup Before Refactoring

Before major structural refactoring:

```text
backup source
backup database
```

---

# 202. Development Safety

Never test destructive database migration code against:

```text
data/mfm.db
```

Use a test database first.

---

# 203. Production Safety

Production database operations SHALL require normal service workflows.

Developers SHALL not manually edit production accounting tables.

---

# 204. Accounting Data Protection

Direct SQL modification of posted financial records is prohibited as a normal operational practice.

---

# 205. Foundation Completion Definition

The foundation is complete when it provides:

```text
CONFIGURATION
+
DATABASE
+
MIGRATION
+
TRANSACTION
+
LOGGING
+
APPLICATION CONTEXT
+
TEST FOUNDATION
```

---

# 206. Next Implementation Layer

After this foundation is stable, the next concrete implementation layer SHALL be:

```text
MFM v1.0 SECURITY & USER IMPLEMENTATION
```

followed by:

```text
ACCOUNTING CORE IMPLEMENTATION
```

The security layer is established early so later business modules can be protected from the beginning.

---

# 207. Architectural Continuity

This implementation document follows:

```text
MFM Architecture Baseline
        ↓
MFM System Integration Architecture
        ↓
MFM Implementation Baseline
        ↓
MFM Database & Core Foundation
```

No new architectural layer is being invented.

---

# 208. Complexity Control

The foundation SHALL remain small.

Do not create separate frameworks for:

```text
database
logging
configuration
dependency injection
events
```

unless actual requirements justify them.

---

# 209. Dependency Injection

MFM may use simple constructor injection.

A full dependency-injection framework is unnecessary for v1.0.

---

# 210. Event Bus

An event bus is not required for v1.0.

Direct service coordination is acceptable.

---

# 211. Message Queue

No message queue is required.

---

# 212. API Layer

No REST API is required for the local v1.0 application.

---

# 213. Service Layer Size

Services SHOULD remain focused.

Avoid one giant:

```text
MFMManager
```

class.

---

# 214. Database Manager Size

The database manager SHALL focus on:

```text
connections
transactions
schema lifecycle
```

It SHALL not become a generic business service.

---

# 215. Settings Manager Size

Settings SHALL focus on configuration.

It SHALL not perform business operations.

---

# 216. Logging Manager Size

Logging configuration SHALL remain infrastructure.

---

# 217. Foundation Failure Handling

If any core component fails:

```text
FAIL EARLY
FAIL CLEARLY
FAIL SAFELY
```

---

# 218. Final Foundation Architecture

```text
run.py
  ↓
main.py
  ↓
ApplicationContext
  |
  +-- Settings
  +-- Database
  +-- Repositories
  +-- Services
  +-- Security
  +-- Audit
  +-- Infrastructure
  ↓
GUI
```

---

# 219. Final Database Architecture

```text
Application
    ↓
Service
    ↓
Repository
    ↓
Transaction
    ↓
SQLite
```

---

# 220. Final Development Architecture

```text
FOUNDATION
   ↓
SECURITY
   ↓
ACCOUNTING
   ↓
MEMBERSHIP
   ↓
PROJECTS
   ↓
GRANTS
   ↓
DOCUMENTS
   ↓
REPORTING
   ↓
BACKUP
   ↓
INTEGRATION
   ↓
TEST
   ↓
PACKAGE
```

---

# 221. Final Governing Principle

> **Build the foundation once, keep it simple, and let every later MFM module depend on the same reliable infrastructure.**

The immediate implementation objective is:

```text
RUN
 ↓
INITIALIZE
 ↓
VERIFY
 ↓
TEST
 ↓
BUILD NEXT
```

# END OF MFM v1.0 DATABASE & CORE FOUNDATION IMPLEMENTATION
