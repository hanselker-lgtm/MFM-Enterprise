# MFM v1.1-230 – Security Architecture, Authentication & Authorization

Version: 1.1

Document ID: MFM-v1.1-230

Status: Technical Implementation

---

# 1. Purpose

The Security Architecture defines how MaritimForeningsManager (MFM) v1.1 protects users, data, documents and system resources.

Security is implemented as a cross-cutting architectural concern affecting every module within the application.

The objectives are:

- Confidentiality
- Integrity
- Availability
- Accountability
- Auditability
- Least Privilege
- Operational Simplicity

---

# 2. Security Objectives

The security architecture shall ensure:

- Secure Authentication
- Strong Authorization
- Complete Audit Logging
- Secure Data Storage
- Controlled Access
- Protection against accidental misuse
- Secure Backup and Recovery
- Future extensibility

---

# 3. Security Architecture

```
User

↓

Authentication

↓

Authorization

↓

Service Layer

↓

Repositories

↓

SQLite Database

↓

Audit
```

Every request passes through the security layer before business logic is executed.

---

# 4. Security Principles

The architecture follows these principles:

- Least Privilege
- Default Deny
- Role-Based Access Control (RBAC)
- Separation of Duties
- Defense in Depth
- Complete Audit Trail
- Secure by Default

---

# 5. Authentication

Version 1.1 supports:

```
Username

+

Password
```

Authentication occurs before the Main Window is loaded.

Only authenticated users may access the application.

---

# 6. Password Storage

Passwords are never stored in plaintext.

Storage requirements:

- Salted
- Secure Hash
- One-way encryption
- No password recovery
- Password reset only

Recommended algorithm:

```
Argon2id

or

bcrypt
```

---

# 7. Login Workflow

```
Start

↓

Login Screen

↓

Credential Validation

↓

Password Verification

↓

Role Loading

↓

Permission Loading

↓

Dashboard
```

Failed authentication terminates the workflow.

---

# 8. Session Management

Each login creates a session.

Session contains:

```
Session ID

User ID

Role

Login Time

Last Activity

Computer Name

Application Version
```

Expired sessions require re-authentication.

---

# 9. Failed Login Protection

Configurable limits:

```
Maximum Failed Logins

5

↓

Temporary Lock

15 Minutes

↓

Administrator Unlock
```

Security events are logged.

---

# 10. Authorization

Authorization is role-based.

Examples:

Administrator

↓

Full Access

Treasurer

↓

Accounting

Secretary

↓

Membership

Project Manager

↓

Projects

Auditor

↓

Read Only

Permissions are evaluated before every business operation.

---

# 11. Permission Structure

Permission hierarchy:

```
Module

↓

Function

↓

Operation
```

Example:

```
Accounting

↓

Voucher

↓

Post
```

Permissions are granular.

---

# 12. Module Security

Every module verifies permissions.

Membership

- View
- Edit
- Archive

Accounting

- View
- Create Voucher
- Post Voucher

Projects

- Create
- Modify
- Close

Grants

- Apply
- Award
- Report

Documents

- Upload
- Download
- Archive

Administration

- Users
- Configuration
- Backup

---

# 13. Security Service

Responsibilities:

- Login
- Logout
- Authentication
- Authorization
- Session Validation
- Password Validation
- Permission Checks

The Security Service is consumed by every module.

---

# 14. Data Protection

Sensitive data includes:

- Password Hashes
- Personal Information
- Financial Information
- Audit Records
- Security Logs

Sensitive information is protected through controlled access.

---

# 15. Document Security

Every document has:

- Owner
- Access Rights
- Version History
- Audit Trail

Documents inherit permissions from linked business entities where appropriate.

---

# 16. Audit Security

Every security event is audited.

Examples:

- Login
- Logout
- Failed Login
- Password Reset
- User Created
- Permission Changed
- Role Changed
- Backup Executed

Audit records cannot be modified.

---

# 17. Configuration Security

Only administrators may modify:

- Roles
- Permissions
- Number Series
- Backup Configuration
- Email Settings
- System Parameters

Configuration changes are audited.

---

# 18. Backup Security

Backup protection includes:

- Administrator Access
- Integrity Verification
- Checksum Validation
- Restore Confirmation

Future versions may support encrypted backup archives.

---

# 19. Logging

Security logs include:

- Login Events
- Authorization Failures
- Configuration Changes
- Backup Operations
- Restore Operations
- Integrity Errors

Logs are stored separately from business data where practical.

---

# 20. Security Notifications

Notifications are generated for:

- Failed Login Attempts
- Locked Accounts
- Backup Failure
- Restore Failure
- Configuration Changes
- Administrator Actions

Notifications assist operational monitoring.

---

# 21. Secure Development Guidelines

All developers shall follow:

- Input Validation
- Parameterized SQL
- No Hardcoded Passwords
- Exception Handling
- Principle of Least Privilege
- Repository Pattern
- Service Layer Validation

Business logic never bypasses security checks.

---

# 22. Validation

Security validation includes:

- Password Complexity
- Session Validity
- Role Assignment
- Permission Availability
- User Status
- Active Account Verification

Validation occurs before business processing.

---

# 23. Future Authentication

Future versions may support:

- Microsoft Entra ID
- LDAP
- Active Directory
- OAuth2
- OpenID Connect
- Multi-Factor Authentication
- Hardware Security Keys

The current architecture accommodates future authentication providers.

---

# 24. Compliance

The security architecture supports:

- GDPR principles
- Data Minimization
- Accountability
- Auditability
- Secure Data Retention
- Access Control

Compliance remains configurable according to organizational requirements.

---

# 25. Security Governance

Responsibilities:

Administrator

- User Administration
- Role Management
- Configuration

Treasurer

- Financial Authority

Secretary

- Membership Administration

Auditor

- Read-only verification

Security responsibilities remain separated.

---

# 26. Security Review

Periodic reviews should verify:

- User Accounts
- Roles
- Permissions
- Failed Logins
- Backup Integrity
- Audit Completeness
- Configuration Changes

Reviews support continuous improvement.

---

# 27. Future Enhancements

Future releases may include:

- Security Dashboard
- MFA
- SSO
- API Authentication
- Security Compliance Reports
- Risk Scoring
- Intrusion Detection
- Passwordless Authentication

These enhancements build upon the existing security architecture.

---

# 28. Summary

The Security Architecture provides a comprehensive framework for authentication, authorization, auditing and operational protection throughout MFM v1.1.

By combining role-based access control, centralized authentication, secure configuration management and immutable audit logging, the architecture protects both organizational data and system integrity while remaining appropriate for a desktop application used by small maritime and non-profit associations.

---

# Next Document

**MFM v1.1-240 – Audit, Logging & Compliance Architecture**

---

# END OF DOCUMENT