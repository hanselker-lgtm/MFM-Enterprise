# MFM v1.2-520 – Implementation Execution, Coding Standards & Development Workflow

Version: 1.2

Document ID: MFM-v1.2-520

Status: Implementation Execution Baseline

---

# 1. Purpose

This document defines the practical implementation execution model, coding standards and development workflow for MaritimForeningsManager (MFM) v1.2.

It follows:

**MFM v1.2-500 – Architecture Consolidation & Implementation Readiness**

and

**MFM v1.2-510 – Implementation Backlog, Work Packages & Traceability**

The purpose is to provide a consistent method for turning approved MFM work packages into maintainable, tested and traceable software.

The document defines:

- Development Workflow
- Coding Standards
- Project Structure
- Naming
- Service Boundaries
- Database Access
- Error Handling
- Logging
- Testing
- Code Review
- Git Workflow
- Configuration
- Secrets
- Documentation
- Definition of Done
- Implementation Safety

---

# 2. Scope

This document applies to MFM application development, including:

- GUI
- Application Services
- Domain Services
- Repositories
- Database
- Document Services
- Security
- Workflow
- Notifications
- Integrations
- Reporting
- Administration
- Testing
- Deployment Support

It applies to new features, bug fixes, refactoring and maintenance.

---

# 3. Development Principles

MFM development follows these principles:

- Keep Business Rules in Domain Services
- Keep GUI Logic in the Presentation Layer
- Keep Database Access in Repositories
- Keep External Systems Behind Adapters
- Prefer Small Understandable Components
- Avoid Unnecessary Abstraction
- Test Important Business Rules
- Preserve Traceability
- Protect Data Integrity
- Prefer Explicit Code Over Clever Code

---

# 4. Implementation Flow

The standard workflow is:

```text
Backlog Item

↓

Clarify Requirements

↓

Review Architecture

↓

Create Implementation Branch

↓

Implement

↓

Write / Update Tests

↓

Run Local Validation

↓

Code Review

↓

Integration

↓

Regression Test

↓

Release Candidate
```

---

# 5. Work Selection

Developers should select work from the approved implementation backlog.

A task should be:

- Ready
- Assigned
- Architecturally Defined
- Testable
- Within the current work package

Unplanned scope should not silently enter an implementation task.

---

# 6. Task Preparation

Before coding, confirm:

- Task ID
- Work Package
- Requirement
- Architecture Reference
- Dependencies
- Acceptance Criteria
- Test Expectations

Example:

```text
TASK-510-11-05

Work Package:
WP-510-11

Purpose:
Implement notification retry.

Architecture:
MFM v1.2-490

Test:
Retry and failure tests.
```

---

# 7. Branch Strategy

A practical Git model is:

```text
main

├── feature/*
├── fix/*
├── refactor/*
└── release/*
```

Feature branches should normally be created from the current integration baseline.

The exact branching strategy may evolve with project scale.

---

# 8. Branch Naming

Recommended names:

```text
feature/accounting-voucher-validation

feature/notification-queue

feature/backup-verification

fix/member-duplicate-validation

fix/document-upload-error

refactor/repository-structure
```

Names should describe the actual work.

---

# 9. Commit Principles

Commits should be:

- Focused
- Understandable
- Small enough to review
- Buildable where practical
- Related to one logical change

Avoid large commits containing unrelated changes.

---

# 10. Commit Naming

Recommended style:

```text
feat(accounting): validate voucher balance

fix(membership): prevent duplicate member number

refactor(database): centralize migration handling

test(grants): add deadline workflow tests

docs(operations): update restore procedure
```

---

# 11. Commit Traceability

Where practical, commits should reference the backlog task.

Example:

```text
feat(notification): add retry queue [TASK-510-11-05]
```

This makes implementation history easier to understand.

---

# 12. Project Structure

The implementation should preserve a clear layered structure.

A conceptual structure is:

```text
MFM
│
├── src
│   ├── gui
│   ├── services
│   ├── domain
│   ├── repositories
│   ├── database
│   ├── security
│   ├── workflow
│   ├── notifications
│   ├── integrations
│   ├── reporting
│   └── core
│
├── tests
│
├── migrations
│
├── docs
│
├── scripts
│
└── deployment
```

The exact physical structure may follow the established MFM source tree where different naming already exists.

---

# 13. Layer Responsibilities

### GUI

Responsible for:

- Display
- User Interaction
- Input Collection
- Presentation Validation
- User Feedback

### Application Services

Responsible for:

- Coordinating use cases
- Transaction boundaries
- Service orchestration

### Domain Services

Responsible for:

- Business Rules
- Business State Changes
- Domain Validation

### Repositories

Responsible for:

- Persistence
- Queries
- Database Interaction

### Integration Adapters

Responsible for:

- External APIs
- Provider Protocols
- External Authentication

---

# 14. GUI Boundary

The GUI must not contain authoritative business logic.

Avoid:

```python
if debit != credit:
    save_to_database()
```

when the accounting rule belongs to Accounting Core.

Prefer:

```text
GUI

↓

AccountingService

↓

Accounting validation

↓

Repository
```

The GUI may display validation results.

---

# 15. Service Boundary

A service should expose meaningful business operations.

Prefer:

```text
post_voucher()
approve_grant()
register_member()
archive_document()
```

over generic operations that expose database internals.

---

# 16. Repository Boundary

Repositories should provide persistence operations.

Examples:

```text
get_member()
save_member()
find_projects()
get_voucher()
```

Repositories should not decide whether a financial voucher is legally or operationally allowed to post.

---

# 17. Domain Rules

Business rules belong in domain or application services.

Examples:

- Voucher must balance.
- Closed periods cannot receive ordinary postings.
- Duplicate member numbers are prohibited.
- Documents under hold cannot be deleted.
- Unauthorized users cannot perform privileged operations.

---

# 18. Transaction Boundaries

Operations that must succeed or fail together should use a transaction.

Example:

```text
Post Voucher

↓

Validate

↓

Write Ledger

↓

Write Audit

↓

Commit
```

If a required operation fails:

```text
Rollback
```

where supported.

---

# 19. Accounting Transaction Safety

Financial operations require special protection.

A posting operation must not result in:

```text
Debit Saved

Credit Failed
```

The complete accounting transaction must be atomic.

---

# 20. Error Handling

Errors should be handled at appropriate layers.

### GUI

Shows user-friendly message.

### Service

Handles business and application failure.

### Repository

Handles persistence failure.

### Integration

Handles external provider failure.

### Logging

Records technical information required for diagnosis.

---

# 21. Exception Principles

Do not silently ignore exceptions.

Avoid:

```python
try:
    operation()
except Exception:
    pass
```

Instead:

```text
Catch

↓

Handle or Propagate

↓

Log where appropriate

↓

Provide User Feedback
```

---

# 22. Error Categories

Errors may be categorized as:

- Validation Error
- Authorization Error
- Business Rule Error
- Persistence Error
- Integration Error
- Configuration Error
- System Error

The category should influence the response.

---

# 23. User-Facing Errors

User-facing errors should explain:

- What happened
- Whether data was changed
- What to do next

Avoid exposing stack traces to ordinary users.

---

# 24. Technical Diagnostics

Technical diagnostics may contain:

- Exception Type
- Stack Trace
- Module
- Operation
- Correlation ID
- Timestamp

Sensitive information must be excluded.

---

# 25. Correlation IDs

Important operations may receive a correlation ID.

Example:

```text
MFM-2026-00482
```

The ID can connect:

- User Action
- Service Operation
- Database Operation
- Integration Attempt
- Error
- Audit Event

---

# 26. Logging

Logging should use appropriate levels:

### DEBUG

Development diagnostics.

### INFO

Normal significant operation.

### WARNING

Unexpected but recoverable condition.

### ERROR

Operation failed.

### CRITICAL

System or data-integrity threat.

---

# 27. Logging Rules

Logs must not contain:

- Passwords
- API Tokens
- Encryption Keys
- Full Sensitive Credentials
- Unnecessary Personal Data

Sensitive values should be masked.

---

# 28. Configuration

Configuration should distinguish:

```text
Application Settings

Organization Settings

User Preferences

Secrets
```

These categories must not be mixed.

---

# 29. Configuration Access

Application code should access configuration through a controlled configuration service where practical.

Avoid scattering environment-variable or configuration-file parsing throughout the application.

---

# 30. Secrets

Secrets include:

- Passwords
- API Keys
- Tokens
- Encryption Material
- Provider Credentials

Secrets must not be committed to source control.

---

# 31. Environment Configuration

Development, test and production should use separate configuration.

Example:

```text
Development

DB = test database

Email = sandbox
```

```text
Production

DB = production database

Email = production provider
```

---

# 32. Database Coding Standards

Database access should:

- Use Parameterized Queries
- Avoid String Concatenation for User Input
- Use Transactions
- Respect Foreign Keys
- Use Appropriate Indexes
- Avoid Uncontrolled Direct SQL

---

# 33. SQL Injection Prevention

Never construct SQL using raw user input.

Avoid:

```python
sql = "SELECT * FROM members WHERE name = '" + name + "'"
```

Use parameterized operations.

---

# 34. Migration Standards

Each migration should be:

- Versioned
- Ordered
- Repeat-Safe where possible
- Tested
- Documented
- Recoverable

Migration scripts should not depend on a developer's local machine state.

---

# 35. Database Schema Changes

Schema changes require:

1. Migration
2. Test
3. Upgrade Validation
4. Backup Consideration
5. Documentation

Direct production schema edits are prohibited except controlled emergency procedures.

---

# 36. Naming Standards

Use consistent naming.

Python modules:

```text
snake_case.py
```

Classes:

```text
PascalCase
```

Functions:

```text
snake_case
```

Constants:

```text
UPPER_SNAKE_CASE
```

Database tables should follow the established MFM schema convention.

---

# 37. Naming Principles

Names should describe meaning.

Prefer:

```text
calculate_project_budget()
```

over:

```text
process_data()
```

Prefer:

```text
get_active_members()
```

over:

```text
get_records()
```

---

# 38. Boolean Naming

Boolean values should be understandable.

Examples:

```text
is_active
is_posted
has_permission
is_archived
```

---

# 39. Function Size

Functions should remain focused.

If a function performs:

```text
Validation

+

Database Access

+

Email

+

GUI Update

+

Reporting
```

it should normally be split into smaller responsibilities.

---

# 40. Class Responsibility

A class should have a clear responsibility.

Avoid large classes that contain:

- GUI
- Database
- Business Logic
- Email
- Configuration
- Security

all together.

---

# 41. Duplication

Avoid unnecessary duplication.

However, do not create complex abstractions merely to remove a few repeated lines.

The priority is maintainability.

---

# 42. Comments

Comments should explain:

- Why
- Important Constraints
- Non-Obvious Decisions
- Workarounds

Avoid comments that simply repeat the code.

---

# 43. Documentation Strings

Public services and important functions should have concise documentation.

Example:

```text
Post a validated accounting voucher.

Raises:
- ValidationError
- AuthorizationError
- PersistenceError
```

---

# 44. Type Hints

Where supported by the implementation language and project conventions, use type hints for:

- Public Service Methods
- Repository Interfaces
- Complex Data Structures
- Configuration Objects

Type hints should improve clarity rather than create unnecessary complexity.

---

# 45. Data Transfer Objects

Where useful, service boundaries may use explicit DTOs or equivalent structures.

Examples:

```text
MemberCreateRequest

VoucherPostRequest

GrantUpdateRequest

NotificationRequest
```

This reduces accidental coupling to database models.

---

# 46. Domain Models

Domain models should represent meaningful business concepts.

Examples:

```text
Member

Project

Grant

Voucher

Document

Notification
```

---

# 47. Repository Models

Persistence models may differ from domain models when necessary.

The repository layer is responsible for mapping between persistence and domain representations where such separation exists.

---

# 48. GUI Models

GUI models should not expose raw database structures unnecessarily.

The GUI should receive information appropriate for presentation.

---

# 49. Validation Standards

Validation should be performed at multiple levels:

```text
GUI

↓

Service

↓

Database
```

Each level protects a different concern.

---

# 50. GUI Validation

GUI validation handles:

- Required fields
- Format
- User guidance
- Immediate feedback

It is not the final authority.

---

# 51. Service Validation

Service validation handles:

- Business Rules
- Authorization
- State Transitions
- Domain Constraints

It is authoritative for application behavior.

---

# 52. Database Validation

Database constraints protect:

- Referential Integrity
- Uniqueness
- Required Relationships
- Data Types

Database constraints are the final technical safety net.

---

# 53. Testing Standards

Every significant feature should include tests appropriate to its risk.

Minimum expectations:

```text
Business Rule

→ Unit / Service Test

Persistence

→ Repository Test

Workflow

→ Integration Test

Critical User Flow

→ System / UI Test where practical
```

---

# 54. Test Naming

Tests should describe behavior.

Example:

```text
test_post_voucher_requires_balanced_entries()

test_member_number_must_be_unique()

test_document_under_hold_cannot_be_deleted()
```

---

# 55. Test Isolation

Tests should not depend on:

- Production Database
- Production Documents
- Production Email
- External Provider State

Tests should use controlled fixtures or test environments.

---

# 56. Test Data

Test data should be deterministic.

Tests should create the state they require rather than depending on previous test execution.

---

# 57. Regression Tests

Every fixed defect should receive a regression test where practical.

Example:

```text
Bug

↓

Fix

↓

Regression Test

↓

Future Protection
```

---

# 58. Accounting Testing

Accounting tests require stronger coverage.

At minimum:

- Balanced Voucher
- Unbalanced Voucher
- Posting
- Reversal
- Closed Period
- Invalid Account
- Duplicate Reference
- Audit

---

# 59. Security Testing

Security tests include:

- Invalid Login
- Unauthorized Access
- Role Restriction
- Privileged Access
- Session Expiry
- Credential Protection

---

# 60. Integration Testing

Integration tests should cover:

- Authentication
- Valid Request
- Invalid Request
- Timeout
- Provider Failure
- Retry
- Duplicate Prevention

External tests should use sandbox providers where possible.

---

# 61. Code Review

Code review should assess:

- Correctness
- Architecture
- Security
- Tests
- Readability
- Data Integrity
- Error Handling

---

# 62. Review Questions

Reviewers should ask:

1. Does this belong in this layer?
2. Does it bypass a service?
3. Does it create duplicate data ownership?
4. Is Accounting Core protected?
5. Is the error handling safe?
6. Is the change tested?
7. Is migration required?
8. Is documentation required?

---

# 63. Refactoring

Refactoring is encouraged when it improves:

- Clarity
- Testability
- Reliability
- Maintainability

Large refactoring should be separated from unrelated feature work where practical.

---

# 64. Dependency Management

Dependencies should be:

- Necessary
- Supported
- Versioned
- Reviewed
- Tested

Avoid adding a dependency for functionality that can be implemented simply with existing project capabilities.

---

# 65. Dependency Updates

Updates should be evaluated for:

- Security
- Compatibility
- License
- Maintenance
- Breaking Changes

Critical security updates may receive priority.

---

# 66. External Libraries

Before introducing a library, consider:

- Is it necessary?
- Is it maintained?
- Does it increase deployment complexity?
- Does it introduce security risk?
- Does it duplicate existing functionality?

---

# 67. API Design

Internal APIs should:

- Have Clear Names
- Have Defined Inputs
- Have Defined Outputs
- Validate Inputs
- Return Predictable Errors

Avoid unstable internal interfaces.

---

# 68. External API Adapters

External API implementations must be isolated.

Example:

```text
External Provider

↓

ProviderAdapter

↓

IntegrationService

↓

Domain Service
```

External provider-specific code must not spread throughout MFM.

---

# 69. Notification Coding

Notifications should be requested through a notification service.

Business code should not directly call SMTP libraries.

Prefer:

```text
GrantService

↓

NotificationService

↓

EmailAdapter
```

---

# 70. Background Job Coding

Jobs should:

- Be Idempotent where practical
- Record Status
- Handle Failure
- Respect Retry Limits
- Log Correlation IDs
- Avoid Duplicate Business Effects

---

# 71. Job Idempotency

For example:

```text
Generate Monthly Report

↓

Check Existing Job / Report Identity

↓

If Already Completed

→ Do Not Duplicate
```

---

# 72. Document Coding

Document operations should:

- Preserve Original Files
- Validate Metadata
- Protect Access
- Calculate Checksums where required
- Separate Derived Data

OCR and search indexing must not replace the original document.

---

# 73. File Handling

Temporary files should:

- Use Controlled Locations
- Have Predictable Cleanup
- Avoid Sensitive Exposure
- Be Closed Correctly
- Handle Failure Safely

---

# 74. Import Coding

Imports should use:

```text
Read

↓

Validate

↓

Preview

↓

Confirm

↓

Process

↓

Report Results
```

Large imports should use background jobs where appropriate.

---

# 75. Export Coding

Exports should:

- Respect Permissions
- Apply Filters
- Identify Scope
- Record Export Activity
- Avoid Excessive Memory Use

---

# 76. Bulk Operations

Bulk operations require:

- Scope
- Preview
- Validation
- Confirmation
- Progress
- Result
- Audit

---

# 77. Security Coding Standards

Security-sensitive code should:

- Fail Closed
- Validate Authorization
- Avoid Logging Secrets
- Use Secure Credential Handling
- Avoid Client-Side-Only Authorization

---

# 78. Authorization

Authorization must be enforced in services.

A hidden GUI button is not sufficient security.

Example:

```text
GUI hides Delete

but

Service also rejects Delete without permission
```

---

# 79. Audit Coding

Important operations should create audit records through the audit service.

Avoid manually creating inconsistent audit entries in many GUI components.

---

# 80. Configuration Coding

Configuration should be loaded once through controlled services where practical.

Avoid:

```text
Module A reads config file

Module B reads environment

Module C reads registry

Module D uses hard-coded value
```

Prefer a consistent configuration model.

---

# 81. Environment Safety

Production environment should be identifiable.

Development tools should provide safeguards against accidental production access.

---

# 82. Feature Flags

Feature flags may be used for:

- Incomplete Features
- Controlled Rollout
- Optional Integrations

Feature flags must not become a permanent substitute for proper architecture.

---

# 83. Database Transactions

Transaction boundaries should be defined at the application/service layer.

Repositories may participate in transactions but should not independently commit pieces of one business operation.

---

# 84. Financial Transaction Boundary

For Accounting Core:

```text
Validate

↓

Authorize

↓

Post

↓

Audit

↓

Commit
```

A financial posting must not partially complete.

---

# 85. Logging and Audit Separation

Logs and audit records serve different purposes.

### Logs

Technical diagnosis.

### Audit

Business and security accountability.

Neither should be treated as a replacement for the other.

---

# 86. Operational Diagnostics

Diagnostics should be safe to run in production.

A diagnostic output should contain:

- Version
- Environment
- Database Status
- Storage Status
- Backup Status
- Job Status
- Integration Status
- Recent Error Summary

Secrets must be excluded.

---

# 87. Coding for Recovery

Important operations should be designed with recovery in mind.

Ask:

- What happens if the process stops halfway?
- Can the operation be retried?
- Can it be detected as already completed?
- Can it be rolled back?
- Can the result be validated?

---

# 88. Coding for Migration

Code changes affecting schema must include migration planning.

The implementation should support:

```text
Old Schema

↓

Migration

↓

New Schema

↓

Validation
```

---

# 89. Migration Compatibility

Where practical, changes should be compatible with existing data during transition.

Destructive transformations require explicit planning and backup.

---

# 90. Release Branch Protection

The release branch should not receive unreviewed changes.

Production release should use an identified version.

---

# 91. Build Reproducibility

The same source version should produce a predictable build.

Build dependencies should be documented.

---

# 92. Installation Testing

Installation testing should include:

- Clean PC
- Existing MFM Version
- Upgrade
- Missing Configuration
- Invalid Configuration
- Uninstall where supported

---

# 93. Upgrade Testing

Upgrade tests should verify:

- Application Starts
- Database Migrates
- Existing Data Remains
- Documents Remain
- Users Remain
- Accounting Remains Correct
- Configuration Remains Valid

---

# 94. Rollback / Recovery

If upgrade fails:

```text
Stop

↓

Protect Database

↓

Use Recovery Procedure

↓

Restore if Required

↓

Validate

↓

Resolve
```

Automatic rollback is desirable where safe but must not be assumed.

---

# 95. Production Deployment

Production deployment should follow:

```text
Backup

↓

Deploy

↓

Migrate

↓

Validate

↓

Smoke Test

↓

Monitor
```

---

# 96. Post-Deployment Monitoring

After release, monitor:

- Startup
- Errors
- Database
- Jobs
- Backups
- Integrations
- User Reports

Critical failures may require rollback or recovery.

---

# 97. Coding Standards Review

Coding standards should be reviewed periodically.

Changes may be required when:

- Project Structure Changes
- New Framework Is Introduced
- Security Requirements Change
- Team Size Changes
- Deployment Model Changes

---

# 98. Small-Team Principle

The coding standard should remain practical for a small development effort.

Avoid requiring:

- Excessive ceremony
- Large approval chains
- Complex enterprise tooling
- Documentation for trivial changes

Controls should be proportional to risk.

---

# 99. Implementation Discipline

The preferred development cycle is:

```text
Small Change

↓

Run Tests

↓

Review

↓

Integrate

↓

Repeat
```

This is safer than accumulating a large untested implementation batch.

---

# 100. Final Development Checklist

Before merging a significant change:

```text
Task Identified          ✓

Architecture Reviewed   ✓

Code Implemented        ✓

Tests Added              ✓

Security Reviewed       ✓

Errors Handled          ✓

Audit Considered        ✓

Documentation Updated   ✓

Migration Considered    ✓

Accounting Boundary     ✓
```

---

# 101. Final Release Checklist

Before release:

```text
Build                   ✓

Tests                   ✓

Migration               ✓

Security                ✓

Backup                  ✓

Restore                 ✓

Installation            ✓

Upgrade                 ✓

Smoke Test              ✓

Documentation           ✓

Release Notes           ✓
```

---

# 102. Definition of Done

A development task is considered complete only when:

1. The implementation satisfies the acceptance criteria.
2. The correct service owns the behavior.
3. Tests pass.
4. Security is enforced.
5. Error handling is implemented.
6. Audit requirements are satisfied.
7. Documentation is updated where necessary.
8. Database migration is included where required.
9. No parallel business truth has been introduced.

---

# 103. Definition of Ready

A task is ready for development when:

- Requirement is clear.
- Architecture is known.
- Dependencies are identified.
- Acceptance criteria exist.
- Test approach is known.
- Required design decisions are resolved.

---

# 104. Architectural Escalation

A developer should stop and escalate when a task appears to require:

- New Data Ownership
- New Financial Ledger
- Major Database Redesign
- New Security Model
- New External Dependency
- New Deployment Model

The correct response is architectural review, not an undocumented local workaround.

---

# 105. Implementation Exception

If an implementation exception is necessary:

```text
Identify

↓

Document

↓

Assess Risk

↓

Approve

↓

Implement

↓

Create Follow-Up
```

Exceptions should not become invisible permanent architecture.

---

# 106. Technical Debt

Technical debt should be explicitly recorded.

Examples:

- Temporary Compatibility Code
- Deferred Refactoring
- Missing Automation
- Known Performance Limitation

Debt should have an owner and reason.

---

# 107. Code Ownership

Code ownership should align with domain responsibility.

Examples:

```text
Accounting Code

→ Accounting Domain Responsibility
```

```text
Membership Code

→ Membership Domain Responsibility
```

Cross-cutting code should have an identified technical owner.

---

# 108. Knowledge Transfer

Important implementation knowledge should not exist only in one developer's memory.

Use:

- Documentation
- ADRs
- Runbooks
- Tests
- Source Comments where appropriate

This supports organizational resilience.

---

# 109. Long-Term Maintainability

Code should be written for the future maintainers of the association.

Prefer:

```text
Clear

Predictable

Documented

Tested
```

over:

```text
Clever

Highly Abstract

Difficult to Diagnose
```

---

# 110. Summary

MFM v1.2-520 defines the practical rules for executing the implementation backlog.

It establishes:

- Development Workflow
- Coding Standards
- Layer Boundaries
- Database Standards
- Testing Standards
- Error Handling
- Logging
- Security
- Git Workflow
- Code Review
- Deployment Safety
- Migration Discipline
- Recovery Awareness
- Definition of Ready
- Definition of Done

The central implementation principle is:

> **Implement the simplest correct solution that respects the established architecture, protects data integrity and can be tested and maintained by the organization.**

The financial ownership principle remains:

> **Accounting Core is the sole authoritative financial ledger.**

All development decisions must preserve that rule.

---

# Next Document

**MFM v1.2-530 – Database Implementation, Schema Evolution & Migration Execution**

---

# END OF DOCUMENT
