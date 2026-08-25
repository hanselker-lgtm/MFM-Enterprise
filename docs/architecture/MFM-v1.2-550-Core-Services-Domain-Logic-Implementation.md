# MFM v1.2-550 – Core Services & Domain Logic Implementation

Version: 1.2

Document ID: MFM-v1.2-550

Status: Implementation Execution Baseline

---

# 1. Purpose

This document defines the implementation baseline for MFM Core Services and Domain Logic.

It follows the established MFM v1.2 architecture and the preceding implementation documents:

- MFM v1.2-500 – Architecture Consolidation & Implementation Readiness
- MFM v1.2-510 – Implementation Backlog, Work Packages & Traceability
- MFM v1.2-520 – Implementation Execution, Coding Standards & Development Workflow
- MFM v1.2-530 – Database Implementation, Schema Evolution & Migration Execution
- MFM v1.2-540 – Security Hardening, Secrets Management & Access Control Execution

The purpose is to define how MFM business capabilities are implemented through controlled services and domain logic.

The document establishes:

- Service Boundaries
- Domain Responsibilities
- Use-Case Execution
- Validation
- Transaction Boundaries
- Authorization
- Error Handling
- Audit
- Domain Events where justified
- Cross-Domain Coordination
- Accounting Protection
- Testing
- Implementation Patterns

---

# 2. Scope

This document covers the core application/service layer for:

- Accounting
- Membership
- Projects
- Grants
- Documents
- Administration
- Security
- Notifications
- Reporting
- Backup and Maintenance
- Cross-Cutting Services

The exact physical module names may follow the existing MFM source tree.

---

# 3. Core Architectural Principle

The service layer is the controlled execution boundary between presentation and persistence.

The standard flow is:

```text
GUI / API / Job

↓

Application Service

↓

Domain Validation

↓

Authorization

↓

Repository / External Adapter

↓

Commit

↓

Audit / Result
```

The service layer must not become a generic pass-through layer with no business responsibility.

---

# 4. Domain Ownership

Each domain owns its own business concepts and rules.

Examples:

```text
Accounting
→ Financial Ledger

Membership
→ Member Records

Projects
→ Project Records

Grants
→ Grant Records

Documents
→ Document Metadata and Lifecycle

Security
→ Users, Roles and Permissions
```

Cross-domain services coordinate but do not silently take ownership of another domain's authoritative data.

---

# 5. Authoritative Financial Rule

The following rule is mandatory:

> **Accounting Core is the sole authoritative financial ledger.**

Project budgets, grant budgets, reports and dashboards may reference financial information.

They must not create a second authoritative ledger.

---

# 6. Application Service vs Domain Service

MFM distinguishes between:

### Application Service

Coordinates a complete use case.

Examples:

```text
register_member()

post_voucher()

create_project()

submit_grant_application()

archive_document()
```

### Domain Service

Encapsulates business rules that do not naturally belong to one entity.

Examples:

```text
voucher_balance_validator

membership_status_policy

grant_deadline_policy
```

---

# 7. Service Responsibilities

Services should:

- Validate Use-Case Inputs
- Authorize Actions
- Coordinate Domain Rules
- Control Transactions
- Call Repositories
- Call External Adapters
- Create Audit Events
- Return Clear Results

Services should not:

- Render GUI
- Contain SQL Strings Everywhere
- Store Secrets
- Become a Second Database
- Bypass Domain Ownership

---

# 8. Service Interface Principle

Services should expose business-oriented methods.

Prefer:

```text
post_voucher()
```

over:

```text
update_voucher_status()
```

when posting is a complete business operation.

---

# 9. Result Model

Services should return predictable results.

A conceptual result may contain:

```text
success

entity_id

status

warnings

errors

correlation_id
```

The exact implementation may use project-specific result classes or exceptions.

---

# 10. Validation Layers

Validation is distributed:

```text
GUI Validation
    ↓
Service Validation
    ↓
Domain Validation
    ↓
Database Constraints
```

The service/domain layer is authoritative for business rules.

---

# 11. Authorization Sequence

For protected operations:

```text
Receive Request

↓

Authenticate User Context

↓

Authorize Permission

↓

Validate Business Rules

↓

Execute

↓

Audit
```

Authorization must happen before sensitive state changes.

---

# 12. Service Transaction Boundary

A business operation that must succeed or fail together should execute within one transaction.

Example:

```text
Post Voucher

↓

Validate

↓

Write Ledger Entries

↓

Write Audit Reference

↓

Commit
```

---

# 13. Service Error Handling

Expected business errors should be represented clearly.

Examples:

```text
ValidationError

AuthorizationError

NotFoundError

ConflictError

BusinessRuleError

PersistenceError

IntegrationError
```

Technical exceptions must not be exposed directly to normal users.

---

# 14. Service Logging

Important service operations should create technical logs where useful.

Logging must not replace business audit.

Example:

```text
Service Log
→ Technical diagnosis

Audit Event
→ Organizational accountability
```

---

# 15. Correlation IDs

Long-running or cross-service operations may use a correlation ID.

The ID should flow through:

```text
GUI

↓

Service

↓

Repository

↓

Integration

↓

Audit
```

---

# 16. Accounting Core Service

The Accounting Core service is responsible for:

- Voucher Validation
- Posting
- Reversal
- Period Control
- Account Validation
- Ledger Integrity
- Accounting Queries

---

# 17. Accounting Posting

Posting should follow:

```text
Receive Voucher

↓

Authorize

↓

Validate Accounts

↓

Validate Period

↓

Validate Balance

↓

Create Ledger Entries

↓

Audit

↓

Commit
```

---

# 18. Accounting Balance Rule

A voucher must satisfy the established debit/credit balance rule.

Conceptually:

```text
Total Debit = Total Credit
```

The service must reject an unbalanced voucher.

---

# 19. Accounting Period Rule

If a period is closed:

```text
Normal Posting

→ Rejected
```

A controlled reversal or correction process must be used where appropriate.

---

# 20. Accounting Reversal

Reversal should be an explicit business operation.

It must:

- Identify Original Entry
- Validate Reversal Permission
- Validate Period
- Create Reversal
- Preserve History
- Audit Action

Original posted financial history must remain intact.

---

# 21. Accounting Query Services

Reporting and dashboard components must obtain authoritative financial information through Accounting Core query services.

They must not directly modify the ledger.

---

# 22. Accounting Service API

Conceptual operations:

```text
create_voucher()

validate_voucher()

post_voucher()

reverse_voucher()

get_voucher()

get_account_balance()

get_period_status()

get_ledger_entries()
```

Exact method names may follow the existing implementation.

---

# 23. Accounting Invariants

The Accounting Core should protect:

```text
Debit = Credit

Posted entries are immutable

Closed periods are protected

Reversals preserve history

Audit is maintained
```

---

# 24. Membership Core Service

Membership service responsibilities include:

- Create Member
- Update Member
- Change Membership Status
- Search Members
- Membership History
- Archive Member
- Membership Reporting

---

# 25. Member Creation

Member creation should:

```text
Validate Input

↓

Check Unique Membership Number

↓

Create Member

↓

Create Required History

↓

Audit
```

---

# 26. Membership Status

Status transitions should be controlled.

Example:

```text
Prospective

↓

Active

↓

Suspended

↓

Inactive

↓

Archived
```

The actual status model follows the established MFM design.

---

# 27. Membership History

Where history is required, status changes should be recorded rather than silently overwriting the previous state.

---

# 28. Membership Service API

Conceptual operations:

```text
create_member()

update_member()

change_member_status()

get_member()

search_members()

get_membership_history()

archive_member()
```

---

# 29. Project Core Service

Project services are responsible for:

- Project Creation
- Project Lifecycle
- Milestones
- Tasks
- Planning
- Budget Planning
- Project Status
- Project Reporting

---

# 30. Project Creation

Project creation should:

```text
Validate Project

↓

Assign Identifier

↓

Set Initial State

↓

Save

↓

Audit
```

---

# 31. Project Lifecycle

A typical lifecycle may be:

```text
Planned

↓

Active

↓

Completed

↓

Archived
```

The exact lifecycle may include additional states.

---

# 32. Project Budget Rule

Project budgets are planning information.

Actual posted financial transactions remain in Accounting Core.

A project service may request:

```text
Actual Spend

```

from Accounting Core, but should not create authoritative ledger entries itself.

---

# 33. Project Financial Reference

A project may have:

- Budget
- Forecast
- Actual
- Variance

The semantics must be explicit.

For example:

```text
Budget
→ Project planning value

Actual
→ Accounting Core derived value
```

---

# 34. Project Service API

Conceptual operations:

```text
create_project()

update_project()

change_project_status()

create_task()

update_task()

add_milestone()

get_project_actuals()

get_project_variance()
```

---

# 35. Grant Core Service

Grant service responsibilities include:

- Grant Discovery
- Application
- Deadline Management
- Award Management
- Reporting Requirements
- Grant Lifecycle

---

# 36. Grant Application

A grant application may move through:

```text
Identified

↓

Planned

↓

Draft

↓

Submitted

↓

Awarded / Rejected

↓

Closed
```

---

# 37. Grant Deadline Rule

Grant deadlines should be validated and surfaced to users.

The service should prevent invalid state transitions where appropriate.

---

# 38. Grant Financial Rule

Grant budgets and requested amounts are grant-management information.

Actual accounting remains authoritative in Accounting Core.

---

# 39. Grant Service API

Conceptual operations:

```text
create_grant()

update_grant()

create_application()

submit_application()

record_award()

record_deadline()

get_grant_status()
```

---

# 40. Document Core Service

Document service responsibilities include:

- Upload
- Metadata
- Versioning
- Classification
- Linking
- Retention
- Archive
- Controlled Deletion

---

# 41. Document Upload

Upload should follow:

```text
Receive File

↓

Validate Type / Size

↓

Generate Safe Storage Name

↓

Store File

↓

Calculate Checksum where required

↓

Create Metadata

↓

Audit
```

---

# 42. Document Versioning

A new document version should preserve the previous version.

Example:

```text
Document 100

Version 1

↓

Version 2

↓

Version 3
```

Previous versions must remain available according to retention rules.

---

# 43. Document Hold

If a document is under hold:

```text
Delete

→ Rejected
```

The hold state must be checked in the service layer.

---

# 44. Document Archive

Archiving should change lifecycle state without unnecessarily deleting the original file.

---

# 45. Document Service API

Conceptual operations:

```text
upload_document()

update_metadata()

create_version()

archive_document()

place_hold()

release_hold()

delete_document()
```

---

# 46. Security Service

Security services are responsible for:

- Authentication
- Password Verification
- Session Creation
- Authorization
- User Lifecycle
- Role Management
- Permission Management

---

# 47. Authentication Service

Conceptual operations:

```text
authenticate()

logout()

create_session()

expire_session()

change_password()
```

---

# 48. Authorization Service

Conceptual operations:

```text
has_permission()

require_permission()

get_user_roles()

get_user_permissions()
```

---

# 49. Security Service Rule

Authorization decisions must be centralized enough to remain consistent.

Avoid implementing slightly different permission checks in every GUI screen.

---

# 50. Administration Service

Administration services manage:

- Organization Settings
- System Configuration
- User Administration
- Maintenance
- Diagnostics
- Backup Operations
- Migration Status

---

# 51. Configuration Service

Configuration service responsibilities:

```text
Load

Validate

Provide

Update where authorized

Audit Changes
```

---

# 52. Notification Service

Notification service responsibilities include:

- Create Notification
- Queue
- Deliver
- Retry
- Track Status

---

# 53. Notification Flow

```text
Business Service

↓

Notification Request

↓

Notification Queue

↓

Provider Adapter

↓

Delivery

↓

Status

↓

Audit where required
```

---

# 54. Notification Independence

A failed notification should not normally roll back an already committed business transaction unless the business requirement explicitly makes communication part of the transaction.

Example:

```text
Grant Saved

↓

Email Fails

→ Grant remains saved

→ Notification becomes Failed
```

---

# 55. Integration Service

Integration services coordinate external systems.

Responsibilities:

- Request Validation
- Provider Authentication
- Adapter Selection
- Retry
- Error Handling
- Status

---

# 56. Integration Boundary

External systems must remain behind adapters.

```text
MFM Service

↓

Integration Service

↓

Provider Adapter

↓

External System
```

---

# 57. Integration Failure

External failure should not corrupt internal business state.

Where possible:

```text
Business Transaction

↓

Commit

↓

External Notification / Integration

↓

Retry if Required
```

The exact sequence depends on the business requirement.

---

# 58. Reporting Service

Reporting services assemble information from authoritative domains.

Examples:

```text
Accounting

Membership

Projects

Grants

Documents
```

---

# 59. Reporting Ownership Rule

The reporting service does not own the source data.

It may:

- Query
- Aggregate
- Format
- Export
- Cache derived results

It must not become an alternate business ledger.

---

# 60. Dashboard Service

Dashboard services should provide optimized read models where needed.

A dashboard value should have clear provenance.

Example:

```text
Actual Project Spend

Source:
Accounting Core

As Of:
17 August 2026
```

---

# 61. Backup Service

Backup service responsibilities include:

- Create Backup
- Verify Backup
- List Backups
- Restore
- Report Status

---

# 62. Restore Service

Restore is a privileged operation.

Flow:

```text
Authorize

↓

Confirm

↓

Protect Current Database

↓

Restore

↓

Validate

↓

Restart

↓

Smoke Test
```

---

# 63. Maintenance Service

Maintenance operations may include:

- Integrity Check
- Log Review
- Cleanup
- Backup Verification
- Database Maintenance

---

# 64. Workflow Service

Where workflow is required, it may coordinate:

- Status Changes
- Approvals
- Tasks
- Notifications

Workflow should not become a second business domain.

---

# 65. Cross-Domain Operations

Some use cases involve multiple domains.

Example:

```text
Create Grant Project

↓

Create Project

↓

Create Grant Link

↓

Create Documents

↓

Notify User
```

The coordinating service should respect each domain's ownership.

---

# 66. Cross-Domain Transaction Rule

Do not create large distributed-style transactions unless necessary.

For local SQLite operations, use one transaction where the business operation truly requires atomicity.

For external communication, prefer asynchronous follow-up where appropriate.

---

# 67. Domain Events

Domain events may be introduced when useful.

Examples:

```text
MemberRegistered

VoucherPosted

GrantAwarded

DocumentArchived
```

Events should be meaningful business facts.

---

# 68. Event Ownership

The domain that owns the fact publishes the event.

Example:

```text
Accounting Core

→ VoucherPosted
```

Other services may react.

They do not become owners of the accounting fact.

---

# 69. Event Reliability

Events that trigger important work should have:

- Unique Event ID
- Timestamp
- Source
- Entity Reference
- Processing Status where needed

---

# 70. Event Idempotency

Consumers should avoid applying the same event twice.

Example:

```text
Event ID 1001

↓

Processed

↓

Event ID 1001 again

↓

Ignored / Already Processed
```

---

# 71. Service-to-Service Calls

Cross-domain calls should use defined service interfaces.

Avoid:

```text
ProjectService

→ Direct SQL into Accounting tables
```

Prefer:

```text
ProjectService

↓

AccountingQueryService
```

---

# 72. Query vs Command

MFM should distinguish:

### Query

Reads information.

### Command

Changes state.

Examples:

```text
get_member()
→ Query

register_member()
→ Command
```

---

# 73. Command Validation

Commands should validate:

- Authorization
- Input
- Current State
- Business Rules

before changing data.

---

# 74. State Transitions

State transitions should be explicit.

Avoid arbitrary:

```text
update_status("anything")
```

Prefer controlled operations:

```text
submit_application()

approve_application()

reject_application()
```

where business rules require them.

---

# 75. Idempotent Commands

Some commands should be safely repeatable.

Examples:

```text
Enable User

Queue Notification

Generate Backup
```

The exact idempotency strategy depends on the operation.

---

# 76. Concurrency

Even in a small SQLite application, service operations should consider concurrent actions.

Examples:

```text
Two users edit same member

Two users post related data

Administrator changes configuration
```

The service should detect conflicts where necessary.

---

# 77. Optimistic Concurrency

Where useful, entities may use a version value:

```text
version = 7
```

Update requires expected version:

```text
Expected 7

Actual 8

→ Conflict
```

This prevents silent overwriting.

---

# 78. Audit Service

Audit should be exposed as a controlled service.

Conceptual operation:

```text
record_event()
```

The service should standardize:

- User
- Action
- Entity
- Result
- Time
- Correlation ID

---

# 79. Audit Failure

For security-critical operations, audit failure should be handled carefully.

If the operation cannot be accountable without audit, the business transaction may need to fail.

The exact rule should be defined by operation risk.

---

# 80. Service Security

Every state-changing service should determine:

```text
Who?

What?

On Which Entity?

Under Which Permission?

```

---

# 81. Service Input Objects

Where practical, use explicit request objects.

Example:

```text
PostVoucherRequest

RegisterMemberRequest

CreateProjectRequest

SubmitGrantRequest
```

This makes interfaces easier to test.

---

# 82. Service Output Objects

Service outputs should avoid exposing unnecessary database internals.

Return meaningful business information.

---

# 83. Service Dependency Injection

Services may receive dependencies such as:

```text
Repository

AuthorizationService

AuditService

NotificationService
```

This improves testing and avoids hard-coded global dependencies.

---

# 84. Service Composition

Application services may coordinate domain services.

Example:

```text
GrantApplicationService

↓

GrantDomainService

↓

DocumentService

↓

NotificationService
```

The composition should remain understandable.

---

# 85. Avoid Service Loops

Avoid dependency cycles such as:

```text
ProjectService

→ GrantService

→ ProjectService
```

If such a cycle appears, reconsider the boundary.

---

# 86. Shared Services

Cross-cutting services may include:

- Configuration
- Audit
- Security
- Notification
- File Storage
- Time
- Correlation
- Diagnostics

Shared services must remain generic enough to avoid owning domain data.

---

# 87. Time Service

For testability, important business operations may use an application time service.

This supports:

- Deterministic Tests
- Deadline Testing
- Period Testing
- Audit Timestamping

---

# 88. ID Generation

Entity identifiers should be generated consistently.

The identifier strategy must support:

- Uniqueness
- Stable References
- Testing
- Migration

---

# 89. Repository Contract

Repositories should provide clear persistence operations.

Example:

```text
MemberRepository

get()

find()

save()

update()

archive()
```

Business rules remain in services.

---

# 90. Repository Error Handling

Repository errors should be translated into meaningful application exceptions where appropriate.

For example:

```text
Database UNIQUE violation

↓

DuplicateMemberError
```

rather than exposing raw SQL errors to the GUI.

---

# 91. Service Error Mapping

The application layer may map errors:

```text
DuplicateMemberError

↓

Member already exists.
```

Technical details remain in diagnostics.

---

# 92. Business Invariants

Important invariants must be explicit.

Examples:

```text
Member number unique

Voucher balanced

Closed period protected

Held document protected

Unauthorized user rejected
```

---

# 93. Invariant Testing

Every critical invariant should have automated tests.

---

# 94. Core Service Testing

Tests should cover:

- Valid Commands
- Invalid Commands
- Authorization
- State Transitions
- Persistence
- Transactions
- Audit
- Notifications
- Integration Failure

---

# 95. Accounting Service Tests

Minimum:

```text
Balanced Posting

Unbalanced Posting

Closed Period

Invalid Account

Reversal

Unauthorized Posting

Audit

Rollback
```

---

# 96. Membership Service Tests

Minimum:

```text
Create Member

Duplicate Number

Update Member

Status Change

Archive

History

Authorization
```

---

# 97. Project Service Tests

Minimum:

```text
Create Project

Status Transition

Task

Milestone

Budget Planning

Accounting Actuals

Authorization
```

---

# 98. Grant Service Tests

Minimum:

```text
Create Grant

Application

Submission

Deadline

Award

Project Link

Authorization
```

---

# 99. Document Service Tests

Minimum:

```text
Upload

Invalid File

Version

Metadata

Hold

Archive

Delete Restriction

Authorization
```

---

# 100. Security Service Tests

Minimum:

```text
Login

Invalid Credentials

Disabled User

Permission

Role

Session

Logout

Password Change
```

---

# 101. Notification Service Tests

Minimum:

```text
Queue

Send

Failure

Retry

Duplicate Prevention

Status
```

---

# 102. Integration Service Tests

Minimum:

```text
Valid Provider

Provider Failure

Timeout

Invalid Response

Retry

Credential Failure
```

---

# 103. Reporting Service Tests

Minimum:

```text
Correct Source

Correct Aggregation

Filters

Permissions

Export

Accounting Values
```

---

# 104. Backup Service Tests

Minimum:

```text
Backup

Verification

Invalid Backup

Restore

Authorization

Recovery Validation
```

---

# 105. Service Test Isolation

Tests should replace external dependencies with controlled test doubles where practical.

Examples:

```text
Fake Email Adapter

Fake Clock

Test Repository

Mock External Provider
```

---

# 106. Integration Test Environment

Integration tests should use:

- Test Database
- Test Documents
- Sandbox Providers
- Test Users

---

# 107. Service Performance

Services should avoid unnecessary:

- Database Queries
- File Reads
- External Calls

However, premature optimization should be avoided.

---

# 108. Service Caching

Caching may be used for read-heavy, stable information.

Cached values must have clear invalidation behavior.

Never cache authoritative financial truth in a way that can become misleading.

---

# 109. Accounting Cache Rule

If accounting values are cached:

```text
Cache

↓

Accounting Core

↓

Refresh / Validate
```

The cache remains derived.

---

# 110. Background Services

Long operations may use jobs.

Examples:

- Large Export
- Backup
- Document Processing
- Email Batch
- Report Generation

---

# 111. Background Job Boundary

The job should invoke the same application services used by normal operations where practical.

Avoid duplicating business rules inside job scripts.

---

# 112. Service Configuration

Services should obtain configuration through the configuration service.

Do not hard-code:

- Paths
- Email Servers
- Provider URLs
- Timeouts
- Business Thresholds

unless the value is genuinely a fixed invariant.

---

# 113. Service Documentation

Each significant service should document:

- Purpose
- Inputs
- Outputs
- Errors
- Authorization
- Transaction Behavior
- Side Effects

---

# 114. Service Implementation Checklist

Before completing a service operation:

```text
Purpose                 ✓

Owner                   ✓

Authorization           ✓

Validation              ✓

Transaction             ✓

Repository              ✓

Error Handling          ✓

Audit                   ✓

Tests                   ✓

Documentation           ✓
```

---

# 115. Domain Boundary Checklist

For every new feature ask:

1. Which domain owns the business fact?
2. Which service changes it?
3. Which repository persists it?
4. Who may execute it?
5. What must be audited?
6. What happens if it fails?
7. Does it affect Accounting Core?

---

# 116. Anti-Patterns

Avoid:

### GUI Business Logic

Business rules implemented only in screens.

### Fat Repository

Repository contains domain rules.

### God Service

One service owns unrelated domains.

### Direct SQL from GUI

Presentation bypasses service layer.

### Parallel Ledger

Another module stores authoritative financial transactions.

### Hidden Side Effects

A simple query unexpectedly changes data.

---

# 117. Example Correct Flow

```text
User

↓

Project Screen

↓

ProjectService.create_project()

↓

Authorization

↓

Project Validation

↓

ProjectRepository.save()

↓

AuditService.record_event()

↓

Result

↓

GUI
```

---

# 118. Example Accounting Flow

```text
User

↓

Accounting Screen

↓

AccountingService.post_voucher()

↓

Authorization

↓

Voucher Validation

↓

Period Validation

↓

Balance Validation

↓

Ledger Repository

↓

Audit

↓

Commit

↓

Result
```

---

# 119. Example Grant Flow

```text
User

↓

GrantService.submit_application()

↓

Authorization

↓

Grant Validation

↓

GrantRepository

↓

Document Link

↓

Notification Queue

↓

Audit

↓

Result
```

---

# 120. Example Document Flow

```text
User

↓

DocumentService.upload_document()

↓

Authorization

↓

File Validation

↓

Storage

↓

Metadata Repository

↓

Audit

↓

Result
```

---

# 121. Service Evolution

Services should evolve through controlled changes.

When a service becomes too large:

```text
Identify Responsibilities

↓

Separate by Business Capability

↓

Add Tests

↓

Refactor

↓

Validate
```

---

# 122. Backward Compatibility

Existing service behavior should remain stable unless a deliberate breaking change is approved.

Changes affecting existing workflows require regression testing.

---

# 123. Service Versioning

Internal service interfaces do not necessarily require formal version numbers.

Versioning is required when:

- External Consumers Depend on the Interface
- Compatibility Cannot Be Maintained
- Major Contract Changes Occur

---

# 124. Core Service Release Gate

A core service is release-ready when:

- Business Rules Pass
- Authorization Passes
- Transactions Are Safe
- Audit Is Correct
- Tests Pass
- No Ownership Violation Exists

---

# 125. Implementation Traceability

Core services should trace:

```text
Requirement

↓

Architecture

↓

Work Package

↓

Service

↓

Test

↓

Release
```

Example:

```text
REQ-ACC-001

↓

Accounting Architecture

↓

WP-510-03

↓

AccountingService.post_voucher()

↓

Accounting Regression Suite

↓

MFM 1.2.x
```

---

# 126. Small-Association Principle

Core services should remain understandable to future maintainers.

Avoid introducing:

- Distributed Service Architecture
- Message Brokers
- Complex Workflow Engines
- Heavy Dependency Injection Frameworks

unless actual requirements justify them.

For the current MFM scale, simple in-process services are preferred.

---

# 127. Core Service Security Gate

Before release verify:

```text
Authentication

Authorization

Least Privilege

Input Validation

Audit

Secret Protection

Error Handling
```

---

# 128. Core Service Recovery Gate

For important operations verify:

```text
Failure Handling

Rollback / Transaction

Retry where safe

Idempotency where required

Recovery Procedure
```

---

# 129. Core Service Performance Gate

Verify that normal workflows remain responsive.

Investigate:

- Slow Queries
- Excessive Calls
- Repeated Loads
- Large Exports

Only optimize where evidence shows a need.

---

# 130. Final Principles

The MFM service layer must remain:

```text
Explicit

Testable

Secure

Traceable

Maintainable
```

The implementation should favor correctness over unnecessary abstraction.

---

# 131. Summary

MFM v1.2-550 defines the implementation baseline for Core Services and Domain Logic.

It establishes:

- Domain Ownership
- Application Services
- Domain Services
- Validation
- Authorization
- Transactions
- Error Handling
- Audit
- Cross-Domain Coordination
- Accounting Protection
- Notifications
- Integrations
- Reporting
- Backup
- Testing
- Service Evolution

The central rule remains:

> **The service layer coordinates business behavior, while each domain retains ownership of its authoritative business facts.**

And for financial truth:

> **Accounting Core is the sole authoritative financial ledger.**

---

# 132. Next Document

**MFM v1.2-560 – Repository, Persistence Services & Data Access Implementation**

---

# END OF DOCUMENT
