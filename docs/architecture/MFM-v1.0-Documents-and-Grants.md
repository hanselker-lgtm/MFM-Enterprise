# MFM v1.0 DOCUMENTS & GRANTS

## MaritimForeningsManager — Dokumenthåndtering, fondsansøgninger og finansieringsopfølgning

**Version:** 1.0  
**Status:** Development Baseline  
**Parent:** MFM v1.0 Projects & Budget  
**Purpose:** Define the practical document and grant-management module for an almennyttig association

---

# 1. Purpose

The Documents & Grants module provides a controlled and understandable way to manage association documents and funding applications.

It SHALL support:

- document registration;
- document metadata;
- document categories;
- document relationships;
- file storage references;
- checksum and integrity information;
- project documents;
- member documents;
- accounting document references;
- grant applications;
- funders;
- application deadlines;
- requested funding;
- approved funding;
- grant payments;
- reporting deadlines;
- grant status;
- grant documents;
- funding overview;
- audit trail.

The module SHALL remain deliberately simple.

---

# 2. Core Principle

> **Documents are evidence and working material; grants are funding processes; accounting remains the authoritative source for actual financial transactions.**

Therefore:

```text
DOCUMENT
   ↓
EVIDENCE / INFORMATION

GRANT
   ↓
FUNDING PROCESS
   ↓
PROJECT
   ↓
ACCOUNTING CORE
```

The module SHALL not become a general document-management platform or a second financial system.

---

# 3. Architectural Position

```text
MFM ARCHITECTURE
       ↓
DATABASE FOUNDATION
       ↓
ACCOUNTING CORE
       ↓
MEMBERSHIP
       ↓
PROJECTS & BUDGET
       ↓
DOCUMENTS & GRANTS
```

Documents and grants integrate with projects, members and accounting without taking over their responsibilities.

---

# 4. Scope

The module SHALL cover:

1. Document registration
2. Document storage references
3. Document metadata
4. Document categories
5. Document search
6. Document linking
7. Document integrity
8. Grant records
9. Funders
10. Grant applications
11. Grant status
12. Grant budgets
13. Grant payments
14. Reporting deadlines
15. Grant documents
16. Funding overview
17. Export
18. Audit

---

# 5. Out of Scope

MFM v1.0 SHALL NOT attempt to become:

- SharePoint;
- a full electronic document-management system;
- a cloud storage platform;
- a digital signature platform;
- a grant marketplace;
- an automatic funding application writer;
- an autonomous grant decision system.

---

# 6. Document Architecture

```text
FILE SYSTEM
    |
    +--- documents/
    |
DATABASE
    |
    +--- document metadata
    |
    +--- entity relationship
    |
    +--- checksum
    |
    +--- audit
```

The database stores document metadata and references.

The actual file remains in controlled file storage.

---

# 7. Document Entity

Minimum fields:

```text
file_name
storage_path
document_type
entity_type
entity_id
checksum
file_size
created_by
created_at
```

Additional metadata MAY include:

```text
title
description
document_date
version
status
```

---

# 8. Document Number

MFM MAY assign an internal document identifier.

Example:

```text
DOC-000001
DOC-000002
```

This identifier SHALL remain stable even if the file name changes.

---

# 9. Document Types

Recommended categories:

```text
GENERAL
MEMBER
MEMBERSHIP
ACCOUNTING
VOUCHER
BANK
PROJECT
GRANT
CONTRACT
INVOICE
REPORT
MEETING
GOVERNANCE
TECHNICAL
PHOTO
OTHER
```

The association MAY configure additional types.

---

# 10. Document Status

Recommended:

```text
ACTIVE
ARCHIVED
SUPERSEDED
DELETED
```

Deleted document metadata SHOULD remain auditable where appropriate.

---

# 11. Document Version

A document MAY have versions.

Example:

```text
ProjectPlan v1
ProjectPlan v2
ProjectPlan v3
```

The latest approved version SHOULD be clearly identifiable.

Historical versions SHOULD not be silently overwritten.

---

# 12. File Naming

The application SHOULD encourage meaningful names.

Example:

```text
2027-03-15_Grant-Application_Fond-X.pdf
```

The system SHALL not require users to understand technical storage paths.

---

# 13. Storage Directory

Recommended:

```text
MFM/
├── data/
│   └── mfm.db
├── documents/
│   ├── members/
│   ├── projects/
│   ├── grants/
│   ├── accounting/
│   └── general/
├── backups/
└── exports/
```

The root directory SHALL be configurable.

---

# 14. Storage Abstraction

The application SHOULD use a `DocumentService`.

GUI code SHALL not directly manipulate arbitrary storage paths.

```text
GUI
 ↓
DocumentService
 ↓
Storage
```

---

# 15. Document Upload

Recommended workflow:

```text
SELECT FILE
   ↓
VALIDATE FILE
   ↓
COPY TO CONTROLLED STORAGE
   ↓
CALCULATE CHECKSUM
   ↓
CREATE METADATA
   ↓
LINK ENTITY
   ↓
AUDIT
```

Failure SHALL not create incomplete metadata.

---

# 16. Document Validation

Minimum checks:

- file exists;
- file can be read;
- file size is valid;
- supported type;
- destination available.

The application SHOULD reject empty files.

---

# 17. Supported File Types

MFM v1.0 SHOULD support common formats:

```text
PDF
DOCX
XLSX
CSV
TXT
JPG
JPEG
PNG
```

The list SHALL be configurable.

---

# 18. File Size

A configurable maximum file size SHOULD be supported.

The application SHALL provide a clear message when the limit is exceeded.

---

# 19. Checksum

Important documents SHOULD receive a SHA-256 checksum.

Conceptually:

```text
FILE
 ↓
SHA-256
 ↓
STORE CHECKSUM
```

This supports integrity checking.

---

# 20. Document Integrity Check

When requested:

```text
CURRENT FILE
      ↓
CALCULATE SHA-256
      ↓
COMPARE DATABASE CHECKSUM
      ↓
MATCH / CHANGED / MISSING
```

A changed file SHALL be reported.

---

# 21. Document Opening

The application SHOULD open documents using the operating system's associated application.

The document service SHALL validate that the file exists before opening it.

---

# 22. Missing Document

If a referenced file is missing:

```text
FILE NOT FOUND
```

The system SHALL show:

- document name;
- expected location;
- entity;
- last known metadata.

It SHALL not silently remove the database record.

---

# 23. Document Relocation

If files are moved outside MFM, the system MAY provide:

```text
Locate Missing File
```

After selecting the new file:

```text
VERIFY CHECKSUM
 ↓
UPDATE PATH
 ↓
AUDIT
```

---

# 24. Document Deletion

Deletion SHALL be controlled.

Recommended:

```text
USER REQUESTS DELETE
 ↓
CHECK PERMISSION
 ↓
CHECK ENTITY
 ↓
CONFIRM
 ↓
DELETE / ARCHIVE
 ↓
AUDIT
```

Documents supporting financial or legal history SHOULD be archived rather than physically destroyed.

---

# 25. Document Archive

Archived documents remain searchable but are not normally presented as current working documents.

Archive status:

```text
ACTIVE → ARCHIVED
```

---

# 26. Document Relationships

Documents MAY be linked to:

```text
MEMBER
MEMBERSHIP
VOUCHER
PROJECT
GRANT
ASSET
GENERAL
```

The relationship SHALL use:

```text
entity_type
entity_id
```

or a dedicated relationship table if multiple relationships are required.

---

# 27. Multiple Relationships

A document MAY relate to more than one entity.

Example:

```text
Grant Decision
   ↓
Grant G-2027-001
   ↓
Project P-2027-001
```

The system SHOULD support multiple relationships without duplicating the physical file.

---

# 28. Document Search

Search SHOULD support:

- file name;
- title;
- type;
- entity;
- date;
- project;
- grant;
- status.

---

# 29. Document Filters

Recommended:

```text
Document Type
Status
Date
Project
Grant
Member
```

---

# 30. Document List

Recommended columns:

```text
Document
Type
Date
Related To
Status
Version
```

---

# 31. Document Detail

The document detail view SHOULD show:

```text
Title
File Name
Type
Date
Version
Status
Related Entities
File Size
Checksum
Created By
Created At
```

---

# 32. Document Audit

Material events:

```text
DOCUMENT_CREATED
DOCUMENT_UPDATED
DOCUMENT_LINKED
DOCUMENT_UNLINKED
DOCUMENT_ARCHIVED
DOCUMENT_RELOCATED
DOCUMENT_DELETED
DOCUMENT_INTEGRITY_FAILED
```

---

# 33. Document Service

Recommended methods:

```text
add_document()
update_document()
get_document()
search_documents()
link_document()
unlink_document()
open_document()
archive_document()
delete_document()
verify_integrity()
locate_missing_file()
```

---

# 34. Document Repository

`DocumentRepository` SHALL manage:

- metadata;
- relationships;
- queries;
- audit references.

File operations SHOULD be handled by a storage component rather than by SQL repositories.

---

# 35. Storage Service

A `DocumentStorageService` MAY handle:

```text
store_file()
read_file()
delete_file()
move_file()
calculate_checksum()
verify_checksum()
```

---

# 36. Grant Architecture

A grant represents a funding opportunity or application.

Minimum:

```text
funder
project
application_date
deadline
requested_amount
approved_amount
status
reporting_deadline
notes
```

---

# 37. Grant Number

Every grant record SHOULD have a unique internal number.

Example:

```text
G-2027-001
G-2027-002
```

---

# 38. Funder

A funder is the organisation or source providing or considering financial support.

Fields MAY include:

```text
name
contact
website
email
phone
notes
```

A dedicated funders table MAY be introduced when multiple applications to the same funder are expected.

---

# 39. Grant Status

Recommended:

```text
IDEA
PREPARING
SUBMITTED
UNDER_REVIEW
APPROVED
PARTIALLY_APPROVED
REJECTED
WITHDRAWN
COMPLETED
```

---

# 40. Grant Lifecycle

```text
IDEA
 ↓
PREPARING
 ↓
SUBMITTED
 ↓
UNDER_REVIEW
 ↓
APPROVED
 ↓
COMPLETED
```

Alternative:

```text
SUBMITTED → REJECTED
SUBMITTED → WITHDRAWN
```

---

# 41. Grant Application

A grant application SHOULD record:

- funder;
- project;
- application date;
- deadline;
- requested amount;
- purpose;
- status;
- contact;
- notes.

---

# 42. Grant Deadline

The application SHALL clearly show:

```text
APPLICATION DEADLINE
```

The system SHOULD provide warnings for upcoming deadlines.

---

# 43. Grant Requested Amount

`requested_amount` represents the amount requested from the funder.

It SHALL not be confused with:

```text
project budget
approved funding
paid funding
```

---

# 44. Approved Amount

`approved_amount` represents the amount formally approved.

It MAY be lower than requested.

Example:

```text
Requested  100,000
Approved    75,000
```

---

# 45. Grant Payment

A grant payment represents actual money received.

Fields:

```text
grant_id
payment_date
amount
voucher_id
reference
```

Actual payment SHALL be reflected in the Accounting Core.

---

# 46. Grant Payment Rule

Grant payment records SHALL not be used to fabricate financial balances.

The actual accounting transaction remains authoritative.

```text
Grant Payment
      ↓
AccountingService
      ↓
Voucher
```

---

# 47. Grant Funding Status

The system SHOULD calculate:

```text
Requested
Approved
Received
Outstanding
```

Example:

```text
Requested   100,000
Approved     80,000
Received     50,000
Outstanding  30,000
```

---

# 48. Grant Funding Gap

For a project:

```text
Project Budget
-
Confirmed Funding
=
Funding Gap
```

Grant information contributes to confirmed funding only according to configured status rules.

A submitted application SHALL not automatically count as confirmed funding.

---

# 49. Confirmed Funding Rule

Recommended:

```text
APPROVED
```

counts as confirmed.

```text
SUBMITTED
```

does not count as confirmed unless explicitly configured.

---

# 50. Grant Reporting Deadline

Approved grants MAY have reporting deadlines.

The system SHOULD show:

```text
REPORT DUE
```

and provide warning status.

---

# 51. Grant Deadline Status

Recommended:

```text
OK
DUE_SOON
OVERDUE
COMPLETED
```

Thresholds SHALL be configurable.

---

# 52. Grant Documents

Typical grant documents:

```text
APPLICATION
BUDGET
PROJECT_DESCRIPTION
QUOTATION
APPROVAL
REJECTION
PAYMENT_CONFIRMATION
REPORT
CORRESPONDENCE
OTHER
```

Documents SHALL be linked to the grant.

---

# 53. Grant Application Package

A grant application MAY provide a checklist:

```text
Project description
Budget
Association information
Accounts
Quotes
Board approval
Other attachments
```

The checklist is administrative and SHALL not replace the actual documents.

---

# 54. Grant Readiness

The application MAY calculate:

```text
REQUIRED DOCUMENTS
+
COMPLETED CHECKLIST
=
READINESS
```

A missing required document SHOULD generate a warning.

---

# 55. Grant Review

Before submission:

```text
CHECK DEADLINE
CHECK AMOUNT
CHECK PROJECT
CHECK BUDGET
CHECK DOCUMENTS
CHECK APPROVAL
```

The system SHOULD allow a human review step.

---

# 56. Grant Submission

MFM v1.0 SHALL not assume direct electronic submission to funders.

Instead:

```text
APPLICATION READY
 ↓
EXPORT / OPEN DOCUMENTS
 ↓
USER SUBMITS EXTERNALLY
 ↓
USER RECORDS SUBMISSION
```

---

# 57. Submission Record

A submission MAY record:

```text
submission_date
method
reference
contact
notes
```

---

# 58. Grant Approval

When approval is recorded:

```text
status = APPROVED
approved_amount = amount
approval_date = date
```

The approval document SHOULD be attached.

---

# 59. Partial Approval

If:

```text
requested = 100,000
approved = 60,000
```

status:

```text
PARTIALLY_APPROVED
```

The system SHALL retain both values.

---

# 60. Grant Rejection

Rejection SHALL preserve:

- requested amount;
- application date;
- funder;
- project;
- rejection date;
- reason if provided;
- application documents.

---

# 61. Grant Completion

A grant MAY be completed when:

```text
funding received
+
project/reporting completed
```

The exact policy is association-specific.

---

# 62. Grant Service

Recommended methods:

```text
create_grant()
update_grant()
submit_grant()
record_approval()
record_rejection()
record_payment()
set_reporting_deadline()
complete_grant()
get_funding_status()
get_deadlines()
```

---

# 63. Grant Repository

`GrantRepository` SHALL manage:

- grant records;
- grant payments;
- funder information;
- status;
- deadlines.

It SHALL not write directly to accounting tables.

---

# 64. Grant Accounting Integration

The architecture SHALL be:

```text
GrantService
      ↓
AccountingService
      ↓
AccountingRepository
      ↓
Database
```

---

# 65. Project Integration

Grant relationship:

```text
Project
   |
   +--- Grant 1
   |
   +--- Grant 2
   |
   +--- Grant 3
```

One project MAY have multiple grant applications.

---

# 66. Multiple Funding Sources

A project MAY be financed by:

```text
Grant
Grant
Donation
Association Funds
Sponsor
Other
```

The project funding view SHALL aggregate these without duplicating accounting data.

---

# 67. Funding Overview

Project funding dashboard SHOULD show:

```text
PROJECT BUDGET
APPROVED GRANTS
OTHER CONFIRMED FUNDING
TOTAL CONFIRMED
FUNDING GAP
```

---

# 68. Funding Forecast

A future enhancement MAY show:

```text
CONFIRMED
+
LIKELY
+
PENDING
```

These categories SHALL be clearly separated.

Only confirmed funding SHOULD be included in the official funding figure.

---

# 69. Grant Risk

Simple warnings MAY include:

```text
DEADLINE SOON
MISSING DOCUMENT
FUNDING GAP
REPORT OVERDUE
APPROVAL BELOW REQUEST
PAYMENT OUTSTANDING
```

No complex scoring engine is required.

---

# 70. Grant Dashboard

Recommended:

```text
OPEN APPLICATIONS
DEADLINES THIS MONTH
APPROVED FUNDING
PENDING PAYMENTS
REPORTS DUE
```

---

# 71. Document Dashboard

Recommended:

```text
RECENT DOCUMENTS
MISSING FILES
INTEGRITY ERRORS
ARCHIVED DOCUMENTS
PROJECT DOCUMENTS
GRANT DOCUMENTS
```

---

# 72. Document Permissions

Recommended:

```text
VIEW_DOCUMENT
ADD_DOCUMENT
EDIT_DOCUMENT
DELETE_DOCUMENT
ARCHIVE_DOCUMENT
EXPORT_DOCUMENT
VERIFY_DOCUMENT
```

---

# 73. Grant Permissions

Recommended:

```text
VIEW_GRANT
CREATE_GRANT
EDIT_GRANT
SUBMIT_GRANT
RECORD_APPROVAL
RECORD_PAYMENT
CLOSE_GRANT
EXPORT_GRANT
```

---

# 74. Separation of Authority

Preparing a grant does not automatically grant authority to approve its financial consequences.

```text
PREPARE
 ↓
REVIEW
 ↓
AUTHORISE
 ↓
SUBMIT
```

The actual approval authority remains with the association.

---

# 75. Grant Approval and Accounting

Recording an approved grant does not automatically mean money has been received.

Therefore:

```text
APPROVED
≠
RECEIVED
```

The accounting entry is created when the actual financial event occurs according to the association's accounting method.

---

# 76. Document and Grant Audit

Material grant events:

```text
GRANT_CREATED
GRANT_UPDATED
GRANT_SUBMITTED
GRANT_APPROVED
GRANT_PARTIALLY_APPROVED
GRANT_REJECTED
GRANT_PAYMENT_REGISTERED
GRANT_COMPLETED
GRANT_DEADLINE_CHANGED
```

---

# 77. Negative Testing — Documents

```text
Missing file → BLOCK
Unsupported type → BLOCK
Zero-size file → BLOCK
Duplicate document reference → WARN / CONTROL
Unauthorised deletion → BLOCK
Missing stored file → WARN
Checksum mismatch → ALERT
Unauthorised export → BLOCK
Invalid entity reference → BLOCK
Database failure during registration → ROLLBACK
```

---

# 78. Negative Testing — Grants

```text
Duplicate grant number → BLOCK
Missing funder → BLOCK
Missing project where required → BLOCK
Negative requested amount → BLOCK
Negative approved amount → BLOCK
Approved > requested → WARN / BLOCK according to policy
Payment > approved amount → WARN / CONTROL
Submit without required data → BLOCK
Unauthorised approval → BLOCK
Invalid status transition → BLOCK
Report deadline before submission → WARN
```

---

# 79. Acceptance Test — Document

Add a valid PDF to a project.

Expected:

```text
file stored
metadata created
checksum stored
project link created
audit event created
```

---

# 80. Acceptance Test — Missing Document

Delete or move the physical file outside MFM.

Run integrity check.

Expected:

```text
MISSING
```

The metadata remains intact.

---

# 81. Acceptance Test — Grant

Create:

```text
G-2027-001
Funder = Example Foundation
Project = P-2027-001
Requested = 100,000
```

Expected:

```text
status = PREPARING
```

---

# 82. Acceptance Test — Submission

Submit the grant.

Expected:

```text
status = SUBMITTED
submission date recorded
audit event exists
```

---

# 83. Acceptance Test — Approval

Approve:

```text
Requested = 100,000
Approved = 75,000
```

Expected:

```text
status = PARTIALLY_APPROVED
approved_amount = 75,000
```

---

# 84. Acceptance Test — Payment

Receive:

```text
50,000
```

Expected:

```text
Received = 50,000
Outstanding = 25,000
Accounting transaction exists
```

---

# 85. Acceptance Test — Funding Gap

Project budget:

```text
200,000
```

Confirmed funding:

```text
150,000
```

Expected:

```text
Funding gap = 50,000
```

Submitted but unapproved grants SHALL not automatically reduce the confirmed funding gap.

---

# 86. Acceptance Test — Reporting Deadline

Grant report due:

```text
2027-10-15
```

Expected:

```text
deadline visible
status calculated
warning when configured threshold is reached
```

---

# 87. Document Import

Future bulk document import MAY support:

```text
folder scan
```

but SHALL not automatically create arbitrary entity relationships without user confirmation.

---

# 88. Grant Import

Existing grant data MAY be imported from CSV/XLSX.

Flow:

```text
IMPORT
 ↓
VALIDATE
 ↓
PREVIEW
 ↓
CONFIRM
 ↓
CREATE
 ↓
AUDIT
```

---

# 89. Grant Export

Grant export SHOULD include:

```text
Grant Number
Funder
Project
Application Date
Deadline
Requested
Approved
Received
Status
Reporting Deadline
```

---

# 90. Document Export

Document export MAY provide:

```text
metadata CSV
```

and optionally:

```text
selected files
```

Physical file export SHALL preserve file names and integrity.

---

# 91. Backup

The standard MFM backup SHALL include:

```text
database
+
document storage
```

A database-only backup is not sufficient when important documents are stored externally.

---

# 92. Backup Verification

A complete backup SHOULD verify:

```text
DATABASE PRESENT
DOCUMENTS PRESENT
DATABASE INTEGRITY
DOCUMENT CHECKSUMS
```

---

# 93. Restore

Restore sequence:

```text
RESTORE DATABASE
 ↓
RESTORE DOCUMENTS
 ↓
VERIFY DATABASE
 ↓
VERIFY DOCUMENT CHECKSUMS
 ↓
VERIFY REFERENCES
```

---

# 94. Orphan Detection

The system SHOULD detect:

```text
DATABASE DOCUMENT WITHOUT FILE
FILE WITHOUT DATABASE RECORD
```

These SHALL be reported.

---

# 95. Grant Reporting

A grant report MAY combine:

```text
Project description
Budget
Actual expenditure
Funding
Documents
Status
```

Actual financial numbers SHALL come from Accounting Core.

---

# 96. Grant Financial Traceability

A grant payment should be traceable:

```text
Grant
 ↓
Payment
 ↓
Voucher
 ↓
Voucher line
 ↓
Bank / account
```

---

# 97. Project Financial Traceability

The project can be traced through:

```text
Project
 ↓
Grant
 ↓
Payment
 ↓
Accounting
```

or:

```text
Project
 ↓
Voucher line
 ↓
Account
```

---

# 98. GUI Navigation

Recommended:

```text
Documents
 ├── Document List
 ├── Search
 └── Integrity Check

Grants
 ├── Grant List
 ├── New Grant
 ├── Deadlines
 └── Reports
```

---

# 99. Project Integration GUI

From project detail:

```text
Documents
Grants
Funding
Reports
```

Users SHOULD be able to navigate between related records.

---

# 100. Document Detail GUI

Actions:

```text
Open
Edit
Link
Unlink
Archive
Delete
Verify
```

---

# 101. Grant Detail GUI

Sections:

```text
Overview
Application
Funding
Documents
Deadlines
Payments
History
```

---

# 102. Deadline Dashboard

The application SHOULD present upcoming deadlines sorted by date.

Example:

```text
2027-05-10 Grant application
2027-06-01 Grant report
2027-06-15 Funding documentation
```

---

# 103. Notifications

MFM v1.0 MAY provide local warnings.

Examples:

```text
Grant deadline in 7 days
Grant report overdue
Document missing
Funding gap remains
```

Notifications SHALL be informational and not replace human responsibility.

---

# 104. Document Service Error Handling

Examples:

```text
"The selected file could not be read."
"The document could not be stored."
"The referenced file is missing."
"The document has changed since it was registered."
"You do not have permission to delete this document."
```

---

# 105. Grant Service Error Handling

Examples:

```text
"The grant number already exists."
"The grant cannot be submitted because required information is missing."
"The approved amount cannot be negative."
"The selected project does not exist."
"You do not have permission to approve this grant."
```

---

# 106. Maintainability

Business rules SHALL reside in:

```text
document_service.py
grant_service.py
```

Storage concerns SHALL reside in:

```text
document_storage.py
```

GUI modules SHALL not implement file-storage or grant-accounting logic.

---

# 107. Suggested Files

```text
src/
├── models/
│   ├── document.py
│   └── grant.py
│
├── repositories/
│   ├── document_repository.py
│   └── grant_repository.py
│
├── services/
│   ├── document_service.py
│   ├── document_storage.py
│   └── grant_service.py
│
└── gui/
    ├── documents.py
    ├── document_detail.py
    ├── grants.py
    └── grant_detail.py
```

Existing files MAY be reused.

---

# 108. Development Sequence

```text
1. Document model
2. Grant model
3. Document repository
4. Grant repository
5. Storage service
6. Document service
7. Grant service
8. Project integration
9. Accounting integration
10. Document GUI
11. Grant GUI
12. Deadline views
13. Reports
14. Backup integration
15. Tests
```

---

# 109. Definition of Done

Documents & Grants v1.0 is complete when:

- documents can be stored;
- document metadata works;
- documents can be linked;
- documents can be searched;
- checksums work;
- missing files are detected;
- documents can be archived;
- grants can be created;
- funders can be recorded;
- grant status works;
- deadlines work;
- requested and approved amounts work;
- payments work;
- accounting integration works;
- grants can be linked to projects;
- grant documents work;
- funding overview works;
- reporting deadlines work;
- audit works;
- permissions work;
- negative tests pass;
- backup includes database and documents.

---

# 110. Relationship to Previous Modules

```text
Architecture Baseline
       ↓
Database Foundation
       ↓
Accounting Core
       ↓
Membership
       ↓
Projects & Budget
       ↓
Documents & Grants
```

The module uses:

```text
Database Foundation
Accounting Core
Projects & Budget
```

It does not replace them.

---

# 111. Practical Association Focus

The module is deliberately designed for a small association.

The objective is not to create a sophisticated enterprise document platform.

The objective is to answer simple questions reliably:

```text
Where is the document?
Which project does it belong to?
Which grant does it support?
What did we apply for?
What was approved?
What have we received?
What is still outstanding?
When is the next deadline?
```

---

# 112. Final Governing Principle

> **Documents preserve evidence. Grants organize funding. Projects provide context. Accounting records financial truth.**

The architecture SHALL keep these responsibilities separate while making them easy for users to navigate.

# END OF MFM v1.0 DOCUMENTS & GRANTS
