# MFM v1.2-470 – Data Lifecycle, Retention & Information Governance Architecture

Version: 1.2

Document ID: MFM-v1.2-470

Status: Functional Expansion

---

# 1. Purpose

This document defines the Data Lifecycle, Retention & Information Governance Architecture for MaritimForeningsManager (MFM) v1.2.

The objective is to establish a practical framework for managing information throughout its lifecycle:

- Creation
- Capture
- Active Use
- Modification
- Classification
- Archiving
- Retention
- Legal Hold
- Anonymization
- Deletion
- Disposal

The architecture is designed for a small non-profit organization and therefore emphasizes clear ownership, controlled retention and practical administration rather than unnecessary information-management complexity.

The architecture complements the existing Security, Document, Backup, Data Migration and Business Continuity architectures.

---

# 2. Objectives

The information governance architecture shall support:

- Data Classification
- Data Ownership
- Data Lifecycle Management
- Retention Policies
- Archiving
- Legal / Administrative Holds
- Controlled Deletion
- Anonymization
- Data Quality
- Information Discovery
- Historical Preservation
- Compliance Support
- Auditability

---

# 3. Information Governance Principles

MFM follows these principles:

- Data Has an Owner
- Data Has a Purpose
- Data Has a Lifecycle
- Retention Is Controlled
- Historical Information Is Preserved Where Required
- Deletion Is Deliberate
- Security Applies Throughout the Lifecycle
- Authoritative Data Is Not Duplicated
- Derived Data Can Be Rebuilt Where Practical
- Legal or Organizational Requirements Take Precedence Over Convenience

---

# 4. Data Lifecycle

The standard lifecycle is:

```text
Create

↓

Capture

↓

Validate

↓

Active Use

↓

Maintain

↓

Archive

↓

Retain

↓

Review

↓

Delete / Anonymize / Preserve
```

Not every data category uses every stage.

---

# 5. Data Ownership

Each data domain has a responsible owner.

| Data Domain | Authoritative Owner |
|---|---|
| Members | Membership Module |
| Financial Transactions | Accounting Core |
| Projects | Project Module |
| Grants | Grants & Funding |
| Documents | Document Module |
| Users / Roles | Security / Administration |
| Workflow State | Workflow Module |
| Reports | Reporting as derived output |
| Audit Records | Audit Service |

Data ownership determines where authoritative changes occur.

---

# 6. Authoritative Data Principle

MFM shall maintain one authoritative source for each business domain.

Examples:

```text
Financial Truth

↓

Accounting Core
```

```text
Membership Truth

↓

Membership Module
```

```text
Document Truth

↓

Document Repository
```

Reports, dashboards, exports and integrations are derived representations.

They must not become competing authoritative records.

---

# 7. Data Classification

MFM may classify information as:

### Public

Information suitable for public communication.

### Internal

Information intended for normal organizational use.

### Confidential

Information requiring controlled access.

### Restricted

Highly sensitive information requiring limited access.

The organization may adapt these classifications to its actual needs.

---

# 8. Personal Data

Potential personal data includes:

- Name
- Address
- Telephone
- Email
- Membership Information
- Emergency Contact Information
- Consent Information
- User Account Information

Personal data shall only be stored when operationally justified.

---

# 9. Financial Data

Financial information includes:

- Vouchers
- Ledger Entries
- Invoices
- Receipts
- Bank Transactions
- Budgets
- Financial Reports
- Reconciliation Records

Financial records are subject to domain-specific retention and audit requirements.

Accounting Core remains authoritative.

---

# 10. Document Data

Documents may include:

- Legal Records
- Historical Material
- Grant Documents
- Accounting Evidence
- Board Records
- Membership Documents
- Project Documents
- Correspondence

Document lifecycle management is coordinated by the Document Module.

---

# 11. Metadata

Document and business metadata may include:

- Creation Date
- Modified Date
- Owner
- Category
- Status
- Source
- Version
- Retention Class
- Security Classification

Metadata must remain linked to the appropriate authoritative record.

---

# 12. Data Quality

Data quality controls include:

- Required Fields
- Valid Formats
- Valid References
- Duplicate Detection
- Consistency Checks
- Historical Integrity
- Controlled Corrections

Data quality problems should be corrected through the responsible domain service.

---

# 13. Data Capture

Data may enter MFM through:

- User Entry
- Import
- Integration
- Migration
- Document Upload
- Workflow
- Generated Records

All entry paths must pass appropriate validation.

---

# 14. Data Modification

Changes to business data shall occur through authorized services.

Where history is important, the system should preserve:

- Previous Value
- New Value
- User
- Timestamp
- Reason where appropriate

This is especially important for financial, security and governance data.

---

# 15. Versioning

Versioning may apply to:

- Documents
- Policies
- Templates
- Important Configuration
- Certain Business Records

Versioning should not be introduced unnecessarily for simple records where audit history is sufficient.

---

# 16. Archiving

Archiving moves inactive information out of normal operational workflows while preserving it for historical or legal purposes.

Examples:

```text
Inactive Project

↓

Archived Project
```

```text
Old Document

↓

Archive
```

Archiving does not mean deletion.

---

# 17. Archive Requirements

Archived data should retain:

- Identity
- Original Context
- Relevant Metadata
- Historical Relationships
- Provenance
- Retention Information

Archived records should remain discoverable to authorized users.

---

# 18. Historical Preservation

Historical information may be important for:

- Association History
- Accounting
- Grants
- Projects
- Membership
- Maritime / Cultural Archives
- Board Records

Where historical meaning would be lost through transformation, the original information should be preserved where practical.

---

# 19. Retention Policy

A retention policy defines:

```text
What Data

+

Why Retained

+

How Long

+

Who Owns It

+

When Reviewed

+

What Happens Afterwards
```

Retention periods are configured according to organizational and legal requirements.

MFM does not itself determine legal retention periods.

---

# 20. Retention Classes

MFM may define retention classes such as:

- Short Term
- Operational
- Long Term
- Permanent / Historical
- Legal Hold

The actual period is configuration data.

---

# 21. Retention Metadata

A record subject to retention may contain:

```text
Retention Class

Retention Start Date

Review Date

Retention End Date

Retention Owner

Hold Status

Disposition Status
```

Not every record requires every field.

---

# 22. Retention Start Date

Retention may begin from:

- Record Creation
- Transaction Date
- Membership End Date
- Project Completion
- Grant Closure
- Document Finalization
- Contract Expiry

The appropriate trigger is defined by the data domain.

---

# 23. Retention Review

Before deletion, the system may require review.

Workflow:

```text
Retention Period Reached

↓

Review

↓

Delete

OR

Archive

OR

Extend Retention

OR

Apply Hold
```

Deletion should not occur automatically where legal or historical significance is uncertain.

---

# 24. Legal / Administrative Hold

A hold prevents ordinary disposition.

A hold may be applied because of:

- Legal Matter
- Audit
- Investigation
- Funding Requirement
- Historical Preservation
- Organizational Decision

Hold status overrides normal deletion.

---

# 25. Hold Structure

A hold may contain:

- Hold ID
- Reason
- Created By
- Created Date
- Scope
- Start Date
- End Date
- Status

The hold itself is audited.

---

# 26. Hold Release

A hold may be released only by an authorized user.

After release:

```text
Hold Removed

↓

Retention Re-Evaluated

↓

Review

↓

Disposition if Appropriate
```

Release must be recorded.

---

# 27. Deletion Principles

Deletion shall be:

- Authorized
- Deliberate
- Traceable
- Domain-Aware
- Retention-Aware

Hard deletion should be restricted.

---

# 28. Soft Deletion

Where appropriate, records may first be marked:

```text
Active

↓

Archived / Inactive

↓

Pending Deletion

↓

Deleted
```

Soft deletion supports recovery and review.

Not all data should use soft deletion indefinitely.

---

# 29. Anonymization

Where personal information no longer needs to identify a person, anonymization may be considered.

Example:

```text
Member Record

↓

Historical Record

↓

Personal Identifiers Removed

↓

Historical Aggregate Preserved
```

Anonymization must not corrupt accounting or audit integrity.

---

# 30. Accounting Data Retention

Accounting records require special handling.

They may be retained even when related personal information would otherwise qualify for deletion.

Where required:

```text
Personal Identity

↓

Minimize / Anonymize where permissible

```

while:

```text
Financial Transaction

↓

Retained in Accounting Core
```

The exact approach depends on applicable legal requirements.

---

# 31. Audit Data Retention

Audit records support:

- Accountability
- Security
- Incident Investigation
- Compliance

Audit retention should be sufficiently long to support these purposes.

Audit records must not be casually deleted because they contain historical system evidence.

---

# 32. Security Log Retention

Security logs may have shorter or longer retention depending on:

- Security Risk
- Incident Requirements
- Storage
- Organizational Policy

Sensitive information in logs should be minimized.

---

# 33. Document Retention

Document retention may depend on:

- Document Category
- Legal Importance
- Historical Value
- Grant Requirements
- Accounting Requirements
- Organizational Policy

The Document Module remains responsible for document storage.

---

# 34. Membership Retention

Membership data may have different lifecycle stages:

```text
Active Member

↓

Former Member

↓

Archived Membership

↓

Review

↓

Deletion / Anonymization where appropriate
```

Historical membership information may be retained for organizational and historical reasons.

---

# 35. Project Retention

Projects may transition:

```text
Active

↓

Completed

↓

Archived

↓

Retention Review
```

Project documents and historical records remain linked.

Financial transactions remain in Accounting Core.

---

# 36. Grant Retention

Grant records may require long-term retention because of:

- Funding Agreements
- Reporting
- Audits
- Financial Evidence
- Historical Documentation

Retention periods should be configured according to the relevant funding requirements.

---

# 37. Workflow Retention

Workflow records include:

- Tasks
- Approvals
- Rejections
- Notifications
- Escalations

Workflow history may be retained to support accountability.

Completed operational tasks may have shorter retention than formal approval records.

---

# 38. Reporting Data

Reports are generally derived outputs.

Where a report represents an important historical decision or formal submission, the generated report may itself become an archived document.

Otherwise, reports may be regenerated from authoritative data.

---

# 39. Exported Data

Exported files are outside the immediate control of MFM after creation.

Therefore:

- Export activity is audited.
- Sensitive exports are restricted.
- Exported files should have appropriate classification.
- Users remain responsible for external copies.

MFM may provide warnings for sensitive exports.

---

# 40. Temporary Data

Temporary files may be created for:

- Import
- Export
- OCR
- Report Generation
- Backup
- Migration

Temporary data should be automatically removed after successful completion unless required for diagnostics.

---

# 41. Derived Data

Derived information includes:

- Search Indexes
- Dashboard Aggregations
- OCR Text
- Report Caches
- Statistics

Derived data may be rebuilt from authoritative sources where practical.

Therefore:

```text
Authoritative Data

→ Preserve

Derived Data

→ Rebuild if Required
```

---

# 42. Search Index Lifecycle

Search indexes follow:

```text
Create

↓

Update

↓

Rebuild

↓

Replace

↓

Delete
```

Search indexes are not authoritative records.

A failed search index must not cause deletion of source documents.

---

# 43. Cache Lifecycle

Caches may be:

- Created
- Refreshed
- Invalidated
- Rebuilt
- Deleted

Caches must never be treated as permanent business records.

---

# 44. Data Disposal

Disposition methods may include:

- Logical Deletion
- Physical Deletion
- Secure File Deletion
- Anonymization
- Archive

The method depends on data type and retention requirements.

---

# 45. File Disposal

When documents are approved for disposal:

```text
Verify Retention

↓

Verify No Hold

↓

Authorize

↓

Delete

↓

Record Disposition
```

The system should not delete documents merely because they are old.

---

# 46. Database Disposal

Database records may only be removed through controlled domain services.

Direct SQL deletion of production business data is prohibited except under controlled recovery or emergency procedures.

---

# 47. Data Subject Requests

Where applicable, the organization may need to process requests concerning personal data.

Workflow:

```text
Request

↓

Verify Identity

↓

Identify Data

↓

Check Legal / Retention Restrictions

↓

Respond / Correct / Restrict / Delete where permitted

↓

Audit
```

MFM supports the technical workflow but does not replace legal assessment.

---

# 48. Data Correction

Corrections should:

- Preserve Auditability
- Use Domain Services
- Avoid Unauthorized Direct Database Changes
- Preserve Financial Integrity

For accounting, corrections must follow Accounting Core procedures.

---

# 49. Data Discovery

Authorized administrators may search for:

- Person
- Member
- Document
- Project
- Grant
- Transaction
- Audit Event

Search results remain subject to authorization.

---

# 50. Information Inventory

The system documentation should maintain an information inventory identifying:

- Data Category
- Owner
- Purpose
- Classification
- Retention Class
- Storage Location
- Authoritative Source
- Derived Copies
- Disposal Method

The inventory supports governance.

---

# 51. Data Lineage

Important data should have traceable lineage where practical.

Example:

```text
Source Document

↓

Grant Application

↓

Project

↓

Accounting Transactions

↓

Financial Report
```

The lineage identifies relationships without duplicating the underlying data.

---

# 52. Master Data Lifecycle

Master data follows:

```text
Create

↓

Approve

↓

Active

↓

Modify

↓

Deactivate

↓

Archive
```

Master data should not be casually deleted when historical records reference it.

---

# 53. Reference Data

Reference values may include:

- Membership Categories
- Account Categories
- Grant Types
- Project Statuses
- Document Categories
- Workflow States

Inactive reference values remain available for historical records where necessary.

---

# 54. Data Governance Roles

Responsibilities include:

### Data Owner

Responsible for meaning and business use.

### System Administrator

Responsible for technical controls.

### Domain Administrator

Responsible for operational data within the domain.

### Ordinary User

Responsible for accurate and appropriate data entry.

---

# 55. Retention Administration

Authorized administrators may:

- Define Retention Classes
- Assign Retention Policies
- Review Expiring Records
- Apply Holds
- Release Holds
- Approve Disposition

All sensitive retention changes are audited.

---

# 56. Retention Dashboard

The Administration Dashboard may show:

- Records Approaching Retention End
- Records Under Hold
- Pending Disposition
- Archived Records
- Retention Exceptions
- Policy Changes

The dashboard should not automatically delete records.

---

# 57. Retention Exceptions

Exceptions may arise from:

- Legal Hold
- Grant Requirements
- Accounting Requirements
- Historical Preservation
- Investigation
- Organizational Decision

Exceptions must be documented.

---

# 58. Historical / Cultural Archive

MFM may contain information with permanent historical value.

Examples:

- Association History
- Maritime History
- Vessel History
- Historical Photographs
- Original Correspondence
- Board Records
- Restoration Documentation

Such material may be assigned a Permanent / Historical retention class.

Historical preservation may override ordinary operational deletion.

---

# 59. Data Migration and Lifecycle

During migration:

```text
Source Data

↓

Preserve Provenance

↓

Map Retention Information

↓

Validate

↓

Import

↓

Reconcile
```

Migration must not accidentally reset or remove important historical retention information.

---

# 60. Backup and Lifecycle

Backups are copies of data, not independent business records.

When production data is deleted according to approved retention rules, backup copies may remain until their own retention cycle expires.

This must be considered when evaluating complete data deletion.

---

# 61. Disaster Recovery and Lifecycle

Recovered data must preserve:

- Retention Metadata
- Hold Status
- Archive Status
- Audit History

Recovery must not unintentionally reset lifecycle state.

---

# 62. Security and Lifecycle

Security applies to every lifecycle stage:

```text
Create → Active → Archive → Retain → Dispose
```

Archived information remains protected.

Deletion does not remove the requirement to protect data during the disposal process.

---

# 63. Lifecycle Audit

The system may audit:

- Retention Assignment
- Archive
- Hold Creation
- Hold Release
- Disposition Approval
- Deletion
- Anonymization
- Policy Change

Audit records provide evidence of controlled information management.

---

# 64. Data Governance Reporting

Reports may include:

- Data Inventory
- Retention Status
- Archive Status
- Legal Holds
- Pending Disposition
- Data Classification
- Data Owner
- Data Quality Issues

Reports are permission controlled.

---

# 65. Performance

Lifecycle operations should avoid blocking normal application use.

Large operations such as:

- Archive
- Bulk Classification
- Index Rebuild
- Bulk Anonymization
- Large Document Disposal

should normally execute as controlled background jobs.

---

# 66. Bulk Operations

Bulk lifecycle operations require:

- Scope
- Preview
- Validation
- Authorization
- Confirmation
- Audit

Example:

```text
Select Records

↓

Preview

↓

Validate Holds

↓

Confirm

↓

Execute

↓

Audit
```

---

# 67. Safety Controls

The system should prevent:

- Deletion Under Hold
- Unauthorized Bulk Deletion
- Deletion of Accounting Records
- Deletion of Required Audit Evidence
- Cross-Organization Disposition
- Untracked Anonymization

High-risk operations require elevated permission.

---

# 68. Testing

Lifecycle testing includes:

- Retention Assignment
- Archive
- Hold
- Hold Release
- Deletion
- Anonymization
- Backup Interaction
- Restore
- Accounting Protection
- Document Protection
- Audit
- Bulk Operations

Tests must verify that authoritative records remain protected.

---

# 69. Future Enhancements

Future releases may support:

- Automated Retention Review
- Advanced Legal Hold
- Records Management
- Data Classification Wizard
- Automated Anonymization
- Data Discovery Reports
- Information Lineage Visualization
- Policy Templates
- Automated Disposal Workflows

Automation must remain reviewable and auditable.

---

# 70. Governance

Information governance shall remain proportionate to the organization's size.

The objective is not to create a large records-management bureaucracy.

The recommended model is:

```text
Clear Ownership

+

Simple Retention Classes

+

Controlled Archive

+

Explicit Deletion

+

Reliable Audit
```

This provides practical control without unnecessary complexity.

---

# 71. Summary

The Data Lifecycle, Retention & Information Governance Architecture establishes a complete lifecycle model for MFM information.

It provides:

- Data Ownership
- Classification
- Lifecycle Management
- Retention
- Archive
- Legal / Administrative Hold
- Controlled Deletion
- Anonymization
- Data Quality
- Data Lineage
- Historical Preservation
- Governance Reporting

The central principle is:

> **Data should be retained because it has a defined purpose or obligation, preserved because it has historical or operational value, and deleted only when authorized and appropriate.**

The architecture also preserves the fundamental MFM rule:

> **Lifecycle management controls information around authoritative business data; it does not create parallel business truth.**

Accounting Core remains the sole authoritative financial ledger.

---

# Next Document

**MFM v1.2-480 – User Experience, Accessibility & Human-Centered Interaction Architecture**

---

# END OF DOCUMENT
