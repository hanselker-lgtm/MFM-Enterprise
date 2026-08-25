# MFM v1.2-400 – Multi-Organization, Roles & Delegated Administration Architecture

Version: 1.2

Document ID: MFM-v1.2-400

Status: Functional Expansion

---

# 1. Purpose

This document defines the Multi-Organization, Roles & Delegated Administration Architecture for MaritimForeningsManager (MFM) v1.2.

The objective is to prepare MFM for organizations that need to manage more than one organizational unit, association, vessel, project environment or delegated administrative responsibility while preserving the simplicity appropriate for a small non-profit organization.

The architecture expands organizational and authorization capabilities without turning MFM into an unnecessarily complex enterprise multi-tenant ERP system.

The existing architectural principles remain mandatory:

- Accounting Core remains the sole authoritative financial ledger.
- Each business domain retains ownership of its own data.
- Security remains centralized.
- Audit remains centralized.
- Administration is controlled through explicit roles and permissions.
- Delegation never removes accountability.

---

# 2. Objectives

The architecture shall support:

- Organizational Units
- Optional Multi-Organization Operation
- Role-Based Administration
- Delegated Responsibilities
- Scoped Permissions
- Organizational Context
- User Assignments
- Role Delegation
- Separation of Duties
- Administrative Workflows
- Cross-Organization Reporting where authorized

---

# 3. Architectural Philosophy

MFM shall support organizational growth without introducing unnecessary complexity.

The default operating model remains:

```text
One Organization

↓

Multiple Functional Modules

↓

Central Security

↓

Central Administration
```

Multi-organization capability is optional.

Organizations that only operate one association should not be forced to configure unnecessary organizational structures.

---

# 4. Organizational Model

The organizational hierarchy may be represented as:

```text
Organization

↓

Organizational Unit

↓

Functional Area

↓

Users / Roles
```

Examples of organizational units may include:

- Association
- Vessel
- Museum
- Workshop
- Local Branch
- Project Office

The actual structure is configurable.

---

# 5. Organization Entity

An organization record may contain:

- Organization ID
- Name
- Short Name
- Registration Number
- Address
- Contact Information
- Default Currency
- Default Language
- Status
- Creation Date
- Archive Status

The organization record is owned by the Administration Module.

---

# 6. Organizational Unit

An organizational unit represents a subdivision of an organization.

It may contain:

- Unit ID
- Organization
- Name
- Description
- Parent Unit
- Responsible User
- Status

Units may form a hierarchy where required.

---

# 7. Organizational Context

The active organizational context determines which records a user may access.

Example:

```text
User

↓

Organization A

↓

Vessel Unit

↓

Projects / Documents / Members
```

Context switching must be explicit.

Users must always be able to identify which organizational context they are operating within.

---

# 8. Single-Organization Mode

For a normal small association, the system operates in simplified mode:

```text
Organization

↓

All Authorized Data
```

No additional organizational selection is required.

This remains the recommended default for most MFM installations.

---

# 9. Multi-Organization Mode

Where enabled, a user may have access to more than one organization.

Example:

```text
User A

├── Organization A
└── Organization B
```

Access is determined by explicit assignments.

A user does not automatically gain access to all organizations.

---

# 10. User Organization Assignment

Each assignment contains:

- User
- Organization
- Role
- Scope
- Start Date
- End Date
- Status

Assignments are auditable.

Expired assignments automatically lose their associated access.

---

# 11. Role Architecture

Roles define groups of permissions.

Examples:

- System Administrator
- Organization Administrator
- Treasurer
- Membership Administrator
- Project Manager
- Grant Manager
- Document Administrator
- Board Member
- Standard User
- Read-Only User

Roles are configurable within defined security boundaries.

---

# 12. Permission Model

Permissions may control:

- View
- Create
- Modify
- Archive
- Approve
- Export
- Configure
- Administer

Permissions are assigned to roles rather than individual users wherever practical.

---

# 13. Scoped Permissions

Permissions may be scoped by:

- Organization
- Organizational Unit
- Module
- Record Type
- Project
- Function

Example:

```text
Project Manager

↓

Project Module

↓

Assigned Projects Only
```

Scoped permissions reduce unnecessary access.

---

# 14. Permission Evaluation

Authorization follows:

```text
User

↓

Authentication

↓

Organization Assignment

↓

Role

↓

Permission

↓

Scope

↓

Access Decision
```

Every protected operation is evaluated against the current authorization context.

---

# 15. Delegated Administration

Delegated administration allows responsibility to be assigned without granting full system administration rights.

Examples:

- Membership Administrator manages members.
- Treasurer manages accounting.
- Grant Manager manages funding.
- Document Administrator manages archives.

This supports least privilege.

---

# 16. Delegation

A responsibility may be delegated temporarily.

A delegation contains:

- Delegator
- Delegate
- Responsibility
- Scope
- Start Date
- End Date
- Reason
- Status

Delegation is auditable.

---

# 17. Temporary Access

Temporary access may be granted for:

- Holiday Coverage
- Treasurer Replacement
- Project Assignment
- External Audit
- System Migration
- Special Events

Temporary permissions automatically expire.

---

# 18. Separation of Duties

MFM shall support separation of duties where required.

Examples:

```text
Voucher Preparation

≠

Voucher Approval
```

```text
Grant Application Preparation

≠

Grant Approval
```

```text
User Creation

≠

User Permission Approval
```

The exact control requirements are configurable.

---

# 19. Accounting Security

Accounting permissions require special protection.

Examples:

- View Ledger
- Create Draft Voucher
- Approve Voucher
- Post Voucher
- Reverse Voucher
- Close Period
- Reconcile Bank
- Export Financial Data

Only authorized Accounting users may perform these actions.

Delegated administration shall never allow unauthorized users to bypass Accounting controls.

---

# 20. Organization-Specific Accounting

Where multiple organizations are enabled, Accounting records must identify the applicable organization.

Example:

```text
Organization A

↓

Accounting Core

↓

Ledger
```

```text
Organization B

↓

Accounting Core

↓

Ledger
```

The accounting model must prevent accidental mixing of financial transactions between organizations.

---

# 21. Shared Accounting

Where organizational policy requires consolidated reporting, the architecture may support controlled consolidation.

Consolidation is analytical.

It does not merge the underlying organization-specific ledgers.

Example:

```text
Organization A Ledger
        \
         \
          → Consolidated Report
         /
Organization B Ledger
```

Each ledger remains authoritative within its own organization.

---

# 22. Shared Members

Where permitted, a person may have relationships with more than one organization.

The architecture distinguishes:

```text
Person

↓

Membership Relationship

↓

Organization
```

Membership status remains organization-specific.

The system must avoid duplicating the person unnecessarily while preserving independent membership relationships.

---

# 23. Shared Documents

Documents may be referenced by multiple organizational entities where authorized.

The Document Module remains the sole owner of physical files.

Access to a shared document is evaluated against all applicable security scopes.

---

# 24. Shared Projects

Projects normally belong to one organization.

Where cross-organization projects are required, the project may reference participating organizations.

Project ownership remains explicit.

Financial responsibility must remain clearly defined.

---

# 25. Cross-Organization Access

Cross-organization access is not automatic.

It requires:

- Explicit Permission
- Defined Scope
- Appropriate Role
- Auditability

Examples:

- System Administrator
- Authorized Board Reporting
- Consolidated Accounting Review
- Central Archive Administration

---

# 26. Organizational Data Isolation

Where organizations are logically separated, the system must prevent accidental data exposure.

Every query involving organization-scoped data must apply the appropriate organization filter.

Security enforcement must occur in the Service Layer and, where appropriate, lower-level repository controls.

---

# 27. User Interface

The administration interface may include:

- Organization Selector
- Current Organization Indicator
- User Organization Assignments
- Role Assignment
- Delegation Management
- Permission Overview
- Access Review
- Organizational Settings

The active organization must be visually clear.

---

# 28. Organization Selector

In multi-organization mode:

```text
Current Organization:
[ Maritime Association A ▼ ]
```

Changing organization context requires validation.

The system must not carry stale context into a new operation.

---

# 29. Access Review

Authorized administrators may review:

- Users
- Roles
- Organizations
- Assignments
- Delegations
- Expiring Access
- High-Privilege Accounts

Access review supports governance and security.

---

# 30. Privileged Access

High-privilege roles include:

- System Administrator
- Organization Administrator
- Security Administrator

Privileged access shall be:

- Explicit
- Audited
- Reviewable
- Limited

Where practical, administrative accounts should not be used for ordinary operational work.

---

# 31. Role Templates

MFM may provide standard role templates.

Examples:

```text
Treasurer

Membership Administrator

Grant Manager

Project Manager

Document Administrator

Board Viewer
```

Templates provide sensible defaults while allowing controlled customization.

---

# 32. Role Inheritance

Role inheritance may be supported where it simplifies administration.

Example:

```text
Organization Administrator

↓

Membership Administrator

↓

Member Read
```

Inheritance must remain explicit and visible to administrators.

Circular role inheritance is prohibited.

---

# 33. Permission Conflicts

The authorization system shall identify potentially conflicting permissions.

Examples:

- Create User + Approve Own User
- Prepare Voucher + Approve Own Voucher
- Prepare Grant + Approve Own Grant

Conflict warnings support separation-of-duties controls.

---

# 34. Delegation Workflow

Delegation workflow:

```text
Delegator

↓

Create Delegation

↓

Define Scope

↓

Define Period

↓

Approval if Required

↓

Active Delegation

↓

Expiration

↓

Audit
```

Delegations may be revoked before their planned expiration.

---

# 35. Emergency Access

Emergency administrative access may be supported under controlled conditions.

Emergency access requires:

- Explicit Authorization
- Reason
- Time Limit
- Audit
- Post-Event Review

Emergency access must not become a permanent alternative to normal authorization.

---

# 36. Organization Lifecycle

Organizations may have states:

- Draft
- Active
- Suspended
- Archived

Archived organizations remain available for historical reporting where permitted.

---

# 37. Organizational Unit Lifecycle

Units may have states:

- Active
- Inactive
- Archived

Historical records retain their original organizational relationship.

---

# 38. Data Ownership

Ownership rules remain:

| Domain | Owner |
|---|---|
| Users & Roles | Administration / Security |
| Members | Membership |
| Ledger | Accounting Core |
| Projects | Project Module |
| Grants | Grants & Funding |
| Documents | Document Module |
| Reports | Reporting |
| Workflows | Workflow Module |

Organizational structure provides scope; it does not replace domain ownership.

---

# 39. Audit

The following actions are audited:

- Organization Created
- Organization Updated
- Organization Archived
- Unit Created
- User Assigned
- Role Assigned
- Role Removed
- Delegation Created
- Delegation Revoked
- Permission Changed
- Emergency Access Granted
- Organization Context Changed where required
- Access Review Completed

Audit records remain immutable.

---

# 40. Security

Security controls include:

- Authentication
- Role-Based Access Control
- Scoped Authorization
- Least Privilege
- Separation of Duties
- Temporary Access
- Delegated Administration
- Audit Logging

Security enforcement remains centralized.

---

# 41. Data Protection

Multi-organization capability must protect against:

- Cross-organization data leakage
- Incorrect context selection
- Unauthorized exports
- Unauthorized reporting
- Shared-document overexposure

Exports must apply the same organizational and role-based restrictions as normal viewing.

---

# 42. Reporting

Authorized reporting may include:

- Organization Overview
- Organization Financial Summary
- Consolidated Reporting
- Membership by Organization
- Project Portfolio
- Grant Portfolio
- Document Statistics

Reports must clearly identify organizational scope.

---

# 43. Performance

Target values:

```text
Organization Selection

< 1 second

Permission Evaluation

< 100 ms

Standard Access Check

< 100 ms

Organization Dashboard

< 3 seconds
```

Large cross-organization reports may execute asynchronously.

---

# 44. Backup & Recovery

Backup includes:

- Organizations
- Organizational Units
- User Assignments
- Roles
- Permissions
- Delegations
- Audit Records
- Organization Configuration

Restore must preserve organizational relationships.

---

# 45. Migration

When enabling multi-organization support for an existing single-organization installation:

```text
Existing MFM

↓

Create Default Organization

↓

Assign Existing Records

↓

Assign Existing Users

↓

Validate Scope

↓

Enable Organizational Context
```

Existing data must not be duplicated.

---

# 46. Testing

Testing shall include:

- Single-Organization Mode
- Multi-Organization Mode
- Role Assignment
- Permission Evaluation
- Delegation
- Expiration
- Cross-Organization Access
- Export Restrictions
- Consolidated Reporting
- Separation of Duties
- Emergency Access
- Migration

Security boundary testing is mandatory.

---

# 47. Future Enhancements

Future releases may support:

- Organization Templates
- Advanced Policy Engine
- Attribute-Based Access Control
- Central Identity Provider
- Single Sign-On
- External Directory Integration
- Multi-Organization Consolidated Budgeting
- Cross-Organization Workflow
- Advanced Delegation Rules

These enhancements shall remain compatible with the core role and scope model.

---

# 48. Governance

Multi-organization functionality is an optional capability.

The default MFM deployment should remain simple.

Organizations should activate multi-organization functionality only when operationally justified.

The architecture shall never require a small association to manage unnecessary organizational complexity.

---

# 49. Summary

The Multi-Organization, Roles & Delegated Administration Architecture extends MFM v1.2 with controlled organizational scoping and more flexible administrative responsibility.

It introduces:

- Organizational Units
- Multi-Organization Support
- Role-Based Administration
- Scoped Permissions
- Delegated Responsibilities
- Temporary Access
- Separation of Duties
- Cross-Organization Reporting

The design remains intentionally lightweight.

The most important architectural rule remains:

> **Organizational scope controls access; domain ownership controls business truth.**

Accounting Core remains the sole authoritative financial ledger. Membership, Projects, Grants, Documents, Reporting and Workflow retain ownership of their respective domains.

---

# Next Document

**MFM v1.2-410 – Advanced Security, Audit & Compliance Architecture**

---

# END OF DOCUMENT
