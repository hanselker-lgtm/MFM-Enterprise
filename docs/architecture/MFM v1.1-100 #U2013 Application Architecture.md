# MFM v1.1-100 – Application Architecture

Version: 1.1

Document ID: MFM-v1.1-100

Status: Implementation Architecture

---

# 1. Purpose

This document defines the software architecture of MaritimForeningsManager (MFM) v1.1.

Where MFM v1.0 established the functional architecture, MFM v1.1 defines the actual software implementation architecture.

The objective is to build a modern, maintainable desktop application using Python while preserving the principles established in the v1.0 baseline.

---

# 2. Architectural Objectives

The application shall be:

- Modular
- Maintainable
- Extensible
- Secure
- Auditable
- Easy to understand
- Easy to deploy

The software architecture shall prioritize simplicity over technical complexity.

---

# 3. Technology Stack

## Programming Language

Python 3.13+

---

## GUI

PySide6 (Qt)

Reason:

- Native Windows appearance
- Mature framework
- Long-term support
- Excellent documentation

---

## Database

SQLite

Reason:

- Zero administration
- Portable
- Reliable
- ACID compliant

---

## ORM

SQLAlchemy 2.x

Reason:

- Strong typing
- Migration support
- Clean object model

---

## Reporting

ReportLab

OpenPyXL

CSV

---

## Configuration

YAML

---

## Logging

Python Logging Framework

---

## Packaging

PyInstaller

---

# 4. High-Level Architecture

```
+------------------------------------------------------+
|                  Presentation Layer                  |
|------------------------------------------------------|
| PySide6 Windows                                      |
| Dialogs                                              |
| Menus                                                |
| Navigation                                           |
+------------------------------------------------------+

                    │

                    ▼

+------------------------------------------------------+
|                  Application Layer                   |
|------------------------------------------------------|
| Controllers                                          |
| Services                                             |
| Validation                                           |
| Business Rules                                       |
+------------------------------------------------------+

                    │

                    ▼

+------------------------------------------------------+
|                    Domain Layer                      |
|------------------------------------------------------|
| Membership                                           |
| Accounting                                           |
| Projects                                             |
| Grants                                               |
| Documents                                            |
| Reporting                                            |
+------------------------------------------------------+

                    │

                    ▼

+------------------------------------------------------+
|                Infrastructure Layer                  |
|------------------------------------------------------|
| SQLAlchemy                                           |
| SQLite                                               |
| Document Storage                                     |
| Logging                                              |
| Backup                                               |
+------------------------------------------------------+
```

---

# 5. Solution Structure

```
MFM/

│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│
├── database/
│
├── gui/
│
├── services/
│
├── repositories/
│
├── models/
│
├── security/
│
├── reporting/
│
├── documents/
│
├── backup/
│
├── utilities/
│
├── resources/
│
├── tests/
│
└── migrations/
```

---

# 6. Layer Responsibilities

## GUI Layer

Responsible for:

- Windows
- Dialogs
- Menus
- User interaction

Contains no business logic.

---

## Controller Layer

Responsible for:

- Coordinating GUI
- Calling Services
- Validation
- Navigation

---

## Service Layer

Responsible for:

- Business rules
- Transactions
- Validation
- Authorization

Every module exposes services.

Example:

```
MembershipService

AccountingService

ProjectService

GrantService

DocumentService

ReportingService
```

---

## Repository Layer

Responsible for:

- Database access

Repositories never contain business logic.

Example:

```
MemberRepository

VoucherRepository

ProjectRepository
```

---

## Domain Layer

Contains

- Entity classes
- Enumerations
- Value Objects

No GUI code.

---

## Infrastructure Layer

Contains

- SQLite
- File Storage
- Logging
- Backup
- Import/Export

---

# 7. Module Overview

```
Membership

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

Every module communicates through services.

---

# 8. Dependency Rules

Allowed

GUI

↓

Services

↓

Repositories

↓

Database

Forbidden

Repository

↓

GUI

Forbidden

GUI

↓

Database

Forbidden

GUI

↓

SQLite

---

# 9. Event Flow

Example

```
User clicks

↓

Controller

↓

Membership Service

↓

Validation

↓

Repository

↓

Database

↓

Audit

↓

GUI Refresh
```

---

# 10. Dependency Injection

Services receive dependencies through constructors.

Example

```
MembershipService(
    member_repository,
    audit_service,
    security_service
)
```

Advantages

- Testability

- Loose coupling

- Easy replacement

---

# 11. Transaction Handling

Only Services create transactions.

Example

```
Service

↓

Begin Transaction

↓

Repository

↓

Commit

↓

Audit
```

Repositories never commit.

---

# 12. Error Handling

Application uses structured exceptions.

Example

```
ValidationException

AuthorizationException

DatabaseException

DocumentException

BusinessRuleException
```

GUI converts exceptions into user-friendly messages.

---

# 13. Logging Architecture

Central logging service.

Levels

- Debug

- Information

- Warning

- Error

- Critical

Audit logging remains separate.

---

# 14. Security Architecture

Authentication

↓

SecurityContext

↓

Authorization

↓

Service

↓

Repository

Permissions are always verified inside the Service layer.

---

# 15. Configuration

Configuration stored in YAML.

Example

```
database.yaml

logging.yaml

backup.yaml

mail.yaml

application.yaml
```

---

# 16. Naming Conventions

Classes

PascalCase

```
MemberService
```

Methods

snake_case

```
create_member()
```

Variables

snake_case

Constants

UPPER_CASE

---

# 17. Code Standards

Maximum method size

50 lines

Preferred class size

Below 500 lines

One responsibility per class.

Avoid duplicated code.

---

# 18. Documentation Standards

Every public class contains

- Description

- Parameters

- Returns

- Exceptions

Every Service is documented.

---

# 19. Testing Strategy

Every Service

↓

Unit Tests

↓

Integration Tests

↓

Acceptance Tests

Repositories tested separately.

---

# 20. Future Scalability

Architecture allows future replacement of

SQLite

↓

PostgreSQL

without affecting

GUI

Services

Business Logic

Only Repository implementations change.

---

# 21. Versioning

Semantic Versioning

Major

Minor

Patch

Example

```
1.1.0

1.1.1

1.2.0

2.0.0
```

---

# 22. Coding Philosophy

The MFM codebase shall always prefer:

- Readability
- Predictability
- Maintainability
- Simplicity

over:

- Clever code
- Premature optimization
- Complex inheritance
- Hidden side effects

---

# 23. Development Workflow

Feature

↓

Implementation

↓

Unit Test

↓

Integration Test

↓

Review

↓

Merge

↓

Release

---

# 24. Production Principles

Production builds shall be:

- Reproducible
- Versioned
- Signed (future)
- Backed up
- Tested

Every release shall include release notes.

---

# 25. Summary

This document establishes the software architecture for MFM v1.1.

It transforms the functional architecture defined in MFM v1.0 into a modern Python application architecture based on layered design, service-oriented business logic, repository-based persistence and a clean separation of concerns.

The architecture is intentionally conservative, prioritizing long-term maintainability, auditability and simplicity over unnecessary technical complexity.

This document serves as the foundation for all subsequent implementation documents in the MFM v1.1 series.

---

# Next Document

**MFM v1.1-110 – Database Schema & Data Model**

---

# END OF DOCUMENT