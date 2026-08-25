# MFM v1.0 – Administration & Configuration Implementation

Version: 1.0

Status: Implementation Baseline

---

# 1. Purpose

The Administration & Configuration module provides the central administrative functionality for MaritimForeningsManager (MFM) v1.0.

The module is responsible for:

- System configuration
- User administration
- Role management
- Master data
- Application settings
- Configuration management
- Operational administration

The module does **not** own business data.

It only controls how the system operates.

---

# 2. Architectural Principles

The module follows the overall MFM architecture:

- Simple
- Reliable
- Auditable
- Maintainable
- Easy for volunteers

Configuration is separated from operational data.

Business modules remain responsible for their own information.

---

# 3. Overall Architecture

```
Administrator

↓

Administration UI

↓

Administration Service

↓

Configuration Service

↓

Security Service

↓

Database
```

Only Administration Service may modify configuration.

---

# 4. Responsibilities

Administration includes:

- User Management
- Role Management
- Permission Management
- System Configuration
- Number Series
- Reference Data
- E-mail Configuration
- Document Configuration
- Backup Configuration
- Logging Configuration
- Maintenance
- Version Information

---

# 5. User Administration

Each user contains:

- User ID
- Username
- Full Name
- Email
- Role
- Status
- Last Login
- Created Date
- Password Hash
- Password Expiry

Status:

- Active
- Disabled
- Locked
- Archived

---

# 6. Role Administration

Standard roles:

- Administrator
- Chairman
- Treasurer
- Secretary
- Membership Administrator
- Project Manager
- Grant Manager
- Auditor
- User

Roles are configurable.

---

# 7. Permission Model

Permissions are assigned per module.

Example:

Membership

- Read
- Create
- Edit
- Delete

Accounting

- Read
- Post
- Close Fiscal Year

Projects

- Read
- Edit
- Close

Documents

- Read
- Upload
- Archive

Security is enforced by the existing SecurityContext and service layer.

GUI visibility is never security.

---

# 8. Master Data

Central master data includes:

Membership

- Categories
- Types
- Status

Projects

- Categories
- Status
- Priorities

Funding

- Categories
- Status
- Funding Types

Documents

- Categories
- Types

Accounting

- Fiscal Years
- VAT Configuration
- Payment Methods

---

# 9. Number Series

Automatically maintained numbering:

- Members
- Projects
- Grants
- Documents
- Accounting Vouchers
- Meetings

Number series must remain unique.

---

# 10. Membership Configuration

Administrator configures:

- Membership Fees
- Family Membership
- Reduced Membership
- Due Dates
- Reminder Policy

Configuration affects future billing only.

---

# 11. Accounting Configuration

Configuration includes:

- Fiscal Year
- Bank Accounts
- Default Accounts
- Payment Types
- VAT Settings
- Project References

Accounting Core remains the only authoritative financial ledger.

---

# 12. Document Configuration

Configuration includes:

- Document Types
- Categories
- Storage Limits
- Allowed File Types
- Version Rules
- Archive Rules

One physical document.

Multiple business references.

---

# 13. Project Configuration

Administrator configures:

- Project Categories
- Default Milestones
- Budget Templates
- Project Templates
- Standard Documents

---

# 14. Grant Configuration

Configuration includes:

- Funding Categories
- Application Status
- Reporting Deadlines
- Standard Workflows

---

# 15. Dashboard Configuration

Dashboard settings include:

- Enabled Widgets
- Default Layout
- Role-specific Views
- Favourite Reports

---

# 16. Email Configuration

Administrator configures:

- SMTP Server
- Port
- Encryption
- Authentication
- Sender Address
- Signature

Connection testing is supported.

---

# 17. System Parameters

Examples:

- Language
- Date Format
- Currency
- Decimal Precision
- Time Zone
- Default Printer

Every change is audited.

---

# 18. Maintenance

Maintenance functions include:

- Database Optimisation
- Index Rebuild
- Reference Integrity Check
- Document Integrity Check
- Checksum Verification

---

# 19. Audit Management

Administrator may:

- Search Audit Log
- Filter Events
- Export Logs
- Archive Historical Logs

Audit entries are immutable.

---

# 20. Backup Configuration

Configuration includes:

- Backup Location
- Retention
- Compression
- Verification
- Scheduling

Actual backup implementation is described in the Backup & Restore document.

---

# 21. System Information

System displays:

- Application Version
- Database Version
- Build Number
- Installation Date
- Last Update

---

# 22. Help

Integrated help includes:

- User Manual
- Administration Guide
- Technical Information
- Error Logs

---

# 23. Audit

The following events are logged:

- Login
- Logout
- Configuration Changes
- User Changes
- Role Changes
- Permission Changes
- Exports
- Maintenance Operations

Audit records cannot be modified.

---

# 24. Future Extensions

Future versions may include:

- Active Directory
- Microsoft Entra ID
- Single Sign-On
- Multi-Factor Authentication
- Central Policy Management

These are optional extensions.

---

# 25. Summary

Administration & Configuration provides the operational backbone of MFM v1.0.

It centralises system configuration, user administration, permissions, master data and operational settings while keeping business data within the appropriate business modules.

The module follows the architectural principles of simplicity, reliability, auditability and maintainability, ensuring that MFM remains a practical solution for a small non-profit association rather than evolving into a full ERP platform.

---

# End of Document