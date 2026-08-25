# MFM v1.1-120 – Service Layer Architecture & Business Services

Version: 1.1

Document ID: MFM-v1.1-120

Status: Technical Implementation

---

# 1. Purpose

This document defines the Service Layer architecture for MaritimForeningsManager (MFM) v1.1.

The Service Layer is the heart of the application.

It contains:

- Business Logic
- Validation
- Authorization
- Transaction Management
- Workflow Coordination
- Audit Integration

No business rules shall exist in:

- GUI
- Repository
- Database
- Reports

---

# 2. Layer Position

```
Presentation Layer

↓

Controllers

↓

SERVICE LAYER

↓

Repositories

↓

SQLite Database
```

The Service Layer is the only layer allowed to coordinate business operations.

---

# 3. Responsibilities

Every Service is responsible for:

- Business Rules
- Validation
- Transactions
- Authorization
- Repository Coordination
- Audit Logging
- Exception Handling

A Service never performs direct SQL.

---

# 4. Service Catalogue

The application consists of the following core services:

```
AuthenticationService

UserService

RoleService

MemberService

MembershipFeeService

AccountingService

ChartOfAccountsService

VoucherService

ProjectService

ProjectBudgetService

GrantService

GrantApplicationService

DocumentService

DocumentVersionService

ReportingService

DashboardService

ConfigurationService

BackupService

RestoreService

MaintenanceService

AuditService

NotificationService

ImportService

ExportService
```

Every service has one clearly defined responsibility.

---

# 5. Service Design Rules

Every Service:

- Owns one business domain
- Uses constructor dependency injection
- Uses repositories
- Never calls SQLite directly
- Returns strongly typed objects
- Throws domain-specific exceptions

---

# 6. Base Service

All services inherit common behaviour.

```
BaseService

├── Validation
├── Logging
├── Audit
├── Security
├── Transaction Support
└── Exception Handling
```

Business functionality is implemented only in derived services.

---

# 7. Member Service

Responsibilities:

- Create Member
- Update Member
- Archive Member
- Search Members
- Membership Validation
- Membership Status

Dependencies:

```
MemberRepository

AuditService

SecurityService
```

---

# 8. Accounting Service

Responsibilities:

- Create Voucher
- Validate Voucher
- Post Voucher
- Close Fiscal Year
- Generate Trial Balance
- Generate Balance Sheet

Dependencies:

```
VoucherRepository

AccountRepository

AuditService
```

Only this service may create accounting transactions.

---

# 9. Project Service

Responsibilities:

- Create Project
- Update Project
- Assign Members
- Budget Management
- Milestones
- Status Changes

Project Service never performs bookkeeping.

---

# 10. Grant Service

Responsibilities:

- Funding Opportunities
- Applications
- Awards
- Reporting
- Funding Status

Grant Service never creates accounting entries.

---

# 11. Document Service

Responsibilities:

- Upload Documents
- Download Documents
- Version Management
- Metadata
- Archive
- Restore

The Document Service owns all physical file handling.

---

# 12. Reporting Service

Responsibilities:

- Report Generation
- Dashboard Data
- KPIs
- Export
- Statistics

Reports are always read-only.

---

# 13. Configuration Service

Responsible for:

- Application Settings
- Number Series
- Email Settings
- Backup Settings
- Report Configuration

Changes require Administrator permissions.

---

# 14. Backup Service

Responsibilities:

- Full Backup
- Incremental Backup
- Verification
- Compression

No business logic exists here.

---

# 15. Restore Service

Responsibilities:

- Restore Backup
- Validate Backup
- Restore Database
- Restore Documents

Every restore operation requires administrator approval.

---

# 16. Maintenance Service

Responsible for:

- Database Optimization
- Cleanup
- Integrity Verification
- Index Maintenance
- Statistics

Maintenance never modifies accounting history.

---

# 17. Audit Service

The Audit Service records every critical event.

Examples:

```
Create Member

Update Member

Delete Member

Create Voucher

Post Voucher

Upload Document

Backup

Restore

Configuration Change
```

Audit logging is automatic.

---

# 18. Notification Service

Responsible for:

- Email
- System Notifications
- Reminder Messages
- Deadline Alerts

Notification delivery is asynchronous where practical.

---

# 19. Import Service

Supports importing:

- Members
- Chart of Accounts
- Projects
- Grant Lists

Imports always perform validation before committing.

---

# 20. Export Service

Supports export to:

- PDF
- Excel
- CSV
- JSON

Exports respect user permissions.

---

# 21. Service Communication

```
Member Service

↓

Project Service

↓

Grant Service

↓

Accounting Service

↓

Document Service

↓

Reporting Service
```

Services communicate only through public interfaces.

Repositories are never shared directly.

---

# 22. Transaction Management

Pattern:

```
Begin Transaction

↓

Validate

↓

Repository Operations

↓

Audit

↓

Commit

↓

Return Result
```

Failure triggers automatic rollback.

---

# 23. Exception Hierarchy

```
BusinessException

├── ValidationException
├── AuthorizationException
├── ConfigurationException
├── AccountingException
├── ProjectException
├── DocumentException
├── DatabaseException
└── BackupException
```

GUI displays user-friendly error messages.

---

# 24. Service Development Standards

Every Service shall:

- Have one responsibility
- Contain XML/Docstring documentation
- Be unit tested
- Use dependency injection
- Avoid duplicated code
- Avoid circular dependencies

Maximum recommended size:

- 500 source lines

Large services should be split into specialised services.

---

# 25. Example Workflow

Example:

Member pays annual membership.

```
GUI

↓

MemberController

↓

MembershipFeeService

↓

AccountingService

↓

VoucherRepository

↓

SQLite

↓

AuditService

↓

Reporting Refresh
```

The Membership module records the payment request.

The Accounting Service creates the financial transaction.

The Reporting Service reflects the updated information.

No duplicate financial information is stored.

---

# 26. Future Extensions

Future versions may introduce:

- Background Job Service
- Scheduler Service
- API Gateway
- Plugin Service
- AI Assistant Service
- Synchronization Service

Each extension shall remain independent and communicate through the Service Layer.

---

# 27. Summary

The Service Layer is the central implementation component of MFM v1.1.

It isolates all business logic from the user interface and database while coordinating validation, security, auditing and transactions.

This architecture ensures that every module remains independent, testable and maintainable while preserving the architectural principles established throughout the MFM project.

---

# Next Document

**MFM v1.1-130 – GUI Framework & User Interface Architecture**

---

# END OF DOCUMENT