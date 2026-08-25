# MFM v1.1-220 – Integration Architecture & Inter-Module Communication

Version: 1.1

Document ID: MFM-v1.1-220

Status: Technical Implementation

---

# 1. Purpose

The Integration Architecture defines how all functional modules within MaritimForeningsManager (MFM) v1.1 communicate while preserving loose coupling, clear ownership and a single source of truth.

The architecture ensures that each module owns its own business domain while exposing services to other modules through controlled interfaces.

No module may directly manipulate another module's internal data.

---

# 2. Integration Objectives

The integration architecture shall provide:

- Loose Coupling
- High Cohesion
- Service-based Communication
- Single Source of Truth
- Transaction Safety
- Maintainability
- Scalability
- Testability

---

# 3. Architectural Overview

```
                    +----------------------+
                    |      Dashboard       |
                    +----------+-----------+
                               |
                               |
     -------------------------------------------------------
     |         |         |         |         |             |
     |         |         |         |         |             |
Membership Accounting Projects Grants Documents Administration
     |         |         |         |         |             |
     -------------------------------------------------------
                               |
                        Service Layer
                               |
                     Repository Layer
                               |
                          SQLite Database
```

Every module communicates through the Service Layer.

---

# 4. Integration Principles

The following principles are mandatory.

## Single Ownership

Every business entity has exactly one owner.

Example:

```
Members

↓

Membership Module
```

---

## Single Financial Authority

Only the Accounting Module creates financial transactions.

Other modules may request postings but never create ledger entries.

---

## Service-Oriented Communication

Communication always occurs through public services.

Example:

```
MemberService

↓

AccountingService

↓

VoucherService
```

No module accesses another module's repositories.

---

## Read-Only Reporting

The Reporting Module consumes data only.

It never modifies business information.

---

# 5. Integration Layers

```
GUI

↓

Controller

↓

Service

↓

Repository

↓

Database
```

Cross-module communication occurs exclusively at the Service layer.

---

# 6. Module Ownership

| Module | Owns |
|---------|------|
| Membership | Members |
| Accounting | Financial Ledger |
| Projects | Projects |
| Grants | Grant Administration |
| Documents | Files |
| Administration | Users & Configuration |
| Reporting | Reports (Read-only) |

Ownership is exclusive.

---

# 7. Communication Patterns

Supported patterns:

```
Direct Service Call

↓

Read Model

↓

Reference Lookup

↓

Notification

↓

Future Event Bus
```

Direct database communication between modules is prohibited.

---

# 8. Membership Integration

Membership communicates with:

Accounting

Purpose:

Membership Fee Requests

Documents

Purpose:

Applications

Reporting

Purpose:

Statistics

Administration

Purpose:

User Permissions

---

# 9. Accounting Integration

Accounting receives requests from:

Membership

Projects

Grants

Administration

Accounting publishes financial information to:

Reporting

Dashboard

Audit

Accounting never accepts direct database writes from other modules.

---

# 10. Project Integration

Projects communicate with:

Documents

Grants

Accounting

Reporting

Project budgets remain planning information.

Financial values originate from Accounting.

---

# 11. Grant Integration

Grants communicate with:

Projects

Accounting

Documents

Reporting

Grant payments are recorded only by Accounting.

---

# 12. Document Integration

Documents support:

Membership

Accounting

Projects

Grants

Administration

Reporting

Documents never own business information.

They own physical files only.

---

# 13. Administration Integration

Administration provides:

Authentication

Authorization

Configuration

Logging

Permissions

Every module consumes administrative services.

---

# 14. Reporting Integration

Reporting consumes information from:

Membership

Accounting

Projects

Grants

Documents

Administration

Reporting performs no business transactions.

---

# 15. Shared Services

Shared services include:

```
Audit Service

Notification Service

Configuration Service

Backup Service

Restore Service

Logging Service

Validation Service
```

Shared services contain no module-specific business logic.

---

# 16. Data References

Modules communicate using identifiers.

Example:

```
Project

↓

project_id

↓

Accounting Reference
```

Entire business objects are not duplicated.

---

# 17. Transaction Boundaries

Example:

```
Membership Fee

↓

Membership Validation

↓

Accounting Posting

↓

Audit

↓

Reporting Refresh
```

The Accounting Service owns the financial transaction.

---

# 18. Error Handling

Every service returns:

- Success
- Validation Error
- Authorization Error
- Business Exception
- System Exception

Errors propagate through the Service Layer.

---

# 19. Dependency Rules

Allowed:

```
GUI

↓

Service

↓

Repository
```

Not allowed:

```
GUI

↓

Repository
```

Not allowed:

```
Repository

↓

Repository
```

---

# 20. Event Flow Example

New Member

```
Create Member

↓

Member Repository

↓

Audit

↓

Notification

↓

Dashboard Update
```

No financial transaction occurs.

---

# 21. Financial Event Example

Membership Payment

```
Membership Service

↓

Accounting Service

↓

Voucher Repository

↓

Audit

↓

Dashboard

↓

Reports
```

Accounting remains authoritative.

---

# 22. Security Integration

Every service requests:

```
Current User

↓

Permissions

↓

Authorization

↓

Business Logic
```

Unauthorized requests are rejected before execution.

---

# 23. Audit Integration

Every module records:

Create

Update

Archive

Restore

Delete Attempt

Configuration Change

Audit records are centralized.

---

# 24. Performance

Integration targets:

Service Call

< 50 ms

Repository Call

< 20 ms

Dashboard Refresh

< 2 seconds

Large Reports

< 10 seconds

Performance is continuously monitored.

---

# 25. Future Integration

Future releases may introduce:

- REST API
- GraphQL API
- Plugin Framework
- Mobile Client
- Cloud Synchronization
- External Accounting Integration
- Government Reporting APIs

The Service Layer remains the integration boundary.

---

# 26. Governance

Every new module must:

- Own its own business entities.
- Expose public services.
- Consume services rather than repositories.
- Respect module ownership.
- Maintain complete auditability.
- Avoid duplicated business information.

Architectural reviews shall verify compliance.

---

# 27. Summary

The Integration Architecture establishes the communication framework for all MFM v1.1 modules.

By enforcing service-oriented communication, strict ownership boundaries and centralized financial authority, the architecture provides a maintainable, scalable and highly cohesive system.

The result is a modular desktop application where every component performs a clearly defined responsibility while collaborating through stable, well-defined interfaces.

---

# Next Document

**MFM v1.1-230 – Security Architecture, Authentication & Authorization**

---

# END OF DOCUMENT