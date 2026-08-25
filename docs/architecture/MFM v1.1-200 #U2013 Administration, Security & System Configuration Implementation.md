# MFM v1.1-200 – Administration, Security & System Configuration Implementation

Version: 1.1

Document ID: MFM-v1.1-200

Status: Technical Implementation

---

# 1. Purpose

The Administration, Security & System Configuration Module provides centralized administration of MaritimForeningsManager (MFM) v1.1.

This module controls system-wide configuration, user administration, security policies, application parameters and operational settings.

It is the administrative backbone of the application.

Business data remains owned by their respective modules.

---

# 2. Responsibilities

The module manages:

- User Administration
- Roles
- Permissions
- Authentication
- Password Policies
- System Configuration
- Number Series
- Application Parameters
- Email Configuration
- Logging Configuration
- Backup Configuration
- License Information
- System Health

---

# 3. Architectural Principles

The module follows these principles:

- Centralized administration
- Least privilege
- Role-based access control
- Separation of duties
- Auditability
- Secure defaults
- Configuration without code changes

---

# 4. Module Architecture

```
Administration GUI

↓

Administration Controller

↓

Administration Service

↓

Security Service

↓

Configuration Service

↓

Repositories

↓

SQLite Database
```

Business modules consume configuration but never modify it directly.

---

# 5. Core Components

```
User Management

Role Management

Permission Management

Authentication

Security Policies

Application Settings

Number Series

Email Settings

Backup Settings

Logging Settings

System Information

License Management
```

Each component owns one administrative domain.

---

# 6. User Management

Each user contains:

```
User ID

Username

Full Name

Email

Password Hash

Status

Assigned Role

Language

Theme

Last Login

Failed Login Count
```

Passwords are never stored in plain text.

---

# 7. User Status

Supported states:

- Pending
- Active
- Locked
- Disabled
- Archived

Locked users require administrator action or automatic unlock according to policy.

---

# 8. Role Management

Default roles include:

- Administrator
- Chairman
- Treasurer
- Secretary
- Membership Administrator
- Project Manager
- Grant Manager
- Auditor
- Read-Only User

Organizations may define additional custom roles.

---

# 9. Permission Model

Permissions are grouped by module.

Examples:

Membership

- View
- Create
- Edit
- Archive
- Export

Accounting

- View Accounts
- Create Voucher
- Post Voucher
- Reverse Voucher
- Close Fiscal Year

Projects

- Create
- Edit
- Complete
- Archive

Grants

- Apply
- Award
- Report

Documents

- Upload
- Download
- Version
- Archive

Administration

- Users
- Roles
- Configuration
- Backup
- Restore

---

# 10. Authentication

Supported authentication:

- Username / Password

Future versions may support:

- Microsoft Entra ID
- LDAP
- Active Directory
- Multi-Factor Authentication (MFA)

Authentication is centralized.

---

# 11. Password Policy

Configurable parameters:

- Minimum Length
- Complexity
- Expiration
- Password History
- Failed Login Limit
- Lockout Duration

Recommended defaults:

```
Minimum Length:

12 characters

Password History:

10

Maximum Failed Logins:

5
```

---

# 12. Session Management

Each session records:

- Login Time
- Logout Time
- User
- Client Computer
- Session ID
- Last Activity

Inactive sessions expire automatically.

---

# 13. System Configuration

System configuration includes:

- Organization Name
- Address
- Logo
- Fiscal Year Settings
- Currency
- Time Zone
- Date Format
- Language

Configuration changes take effect immediately where possible.

---

# 14. Number Series

Automatic numbering supports:

- Members
- Projects
- Grants
- Vouchers
- Documents
- Meetings
- Reports

Number formats are configurable.

---

# 15. Email Configuration

Supports:

- SMTP Server
- Port
- Encryption
- Authentication
- Default Sender
- Reply Address

Email templates are centrally managed.

---

# 16. Logging Configuration

Logging settings include:

- Log Level
- Log Rotation
- Retention Period
- Log Location

Audit logging cannot be disabled.

---

# 17. Backup Configuration

Administrator configures:

- Backup Location
- Schedule
- Retention
- Compression
- Verification

Configuration is shared with the Backup Module.

---

# 18. System Health

The administration dashboard displays:

- Database Status
- Backup Status
- Disk Space
- Application Version
- Active Users
- Failed Logins
- Pending Maintenance

Health information is read-only.

---

# 19. Security Monitoring

Security monitoring includes:

- Failed Login Attempts
- Locked Accounts
- Permission Changes
- Administrator Activity
- Backup Failures
- Configuration Changes

Suspicious events generate notifications.

---

# 20. License Information

System stores:

- Product Name
- Version
- Build Number
- Installation Date
- Organization
- License Type

Future commercial editions may extend license management.

---

# 21. Audit

The following actions are audited:

- User Created
- User Disabled
- Password Reset
- Role Changed
- Permission Changed
- Configuration Updated
- Login
- Logout
- Backup Configuration Changed

Administrative audit records are immutable.

---

# 22. User Interface

Primary screens:

- User Management
- Roles
- Permissions
- System Configuration
- Email Settings
- Number Series
- Logging
- Backup Configuration
- System Information

Secondary dialogs:

- Create User
- Reset Password
- Assign Role
- Edit Permission
- Configure System

The interface follows the standard MFM GUI framework.

---

# 23. Validation Rules

Examples:

- Username must be unique.
- Email format must be valid.
- Roles must exist before assignment.
- Permissions must reference valid modules.
- Number series must be unique.
- Configuration values must match expected formats.

Validation occurs within the Administration and Security Services.

---

# 24. Integration

The module integrates with all other modules.

Examples:

Membership

- User ownership
- Responsible administrators

Accounting

- Posting permissions
- Fiscal year access

Projects

- Project Manager assignment

Grants

- Responsible Officer

Documents

- Document ownership
- Access permissions

Reporting

- Report visibility
- Dashboard personalization

The Administration Module never modifies business data directly.

---

# 25. Future Enhancements

Future releases may support:

- Multi-Factor Authentication (MFA)
- Single Sign-On (SSO)
- OAuth2/OpenID Connect
- Microsoft Entra ID Integration
- Active Directory Synchronization
- Security Policy Templates
- Centralized Configuration Repository
- Automatic Compliance Reports

These enhancements shall preserve the existing role-based security architecture.

---

# 26. Governance

The Administration, Security & System Configuration Module governs the operational environment of MFM.

It defines **who** may access the system, **what** they may do and **how** the application is configured, while leaving ownership of business information to the individual functional modules.

This separation maintains security, auditability and long-term maintainability.

---

# 27. Summary

The Administration, Security & System Configuration Module provides centralized control of users, permissions, authentication, configuration and operational settings for MFM v1.1.

It establishes a secure and maintainable foundation for the application by implementing role-based access control, configurable system settings and comprehensive audit logging.

Together with the previously defined implementation documents, this module completes the technical implementation architecture required to operate MFM as a secure, reliable and maintainable Windows desktop application for small maritime and non-profit associations.

---

# Next Document

**MFM v1.1-210 – Backup, Restore & Maintenance Module Implementation**

---

# END OF DOCUMENT