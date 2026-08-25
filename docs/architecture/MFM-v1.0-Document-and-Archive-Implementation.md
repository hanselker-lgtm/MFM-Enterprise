# MFM v1.0 DOCUMENT & ARCHIVE IMPLEMENTATION

## MaritimForeningsManager

**Version:** 1.0  
**Status:** Implementation Baseline  
**Architecture position:** Document & Archive Layer  
**Predecessor:** MFM v1.0 Grants & Funding Implementation

---

## Executive Summary

MFM v1.0 Document & Archive provides a practical central document layer for a small non-profit association. It stores each physical document once, preserves versions, controls access, connects documents to members, projects, grants, accounting and governance, and maintains an auditable archive.

The central rule is:

```text
ONE DOCUMENT
      ↓
ONE CONTROLLED STORE
      ↓
MANY BUSINESS REFERENCES
```

The module SHALL remain simple, reliable and usable by volunteers.

---

# 1. Purpose

Defines the practical v1.0 document and archive layer for a small non-profit association. It manages document metadata, classification, references, versions, retention, search, access, project/member/grant/accounting links, archive status and audit without attempting to become a full enterprise document-management platform.

## Implementation Record 1

- **Architecture object:** Purpose
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 2. Governing Principle

> A document is an organisational record whose physical content is stored once, while MFM maintains controlled metadata, relationships, access, lifecycle and audit history.

## Implementation Record 2

- **Architecture object:** Governing Principle
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 3. Scope

Mandatory capabilities:

```text
DOCUMENT REGISTER
DOCUMENT METADATA
CLASSIFICATION
CATEGORIES
TAGS
DOCUMENT REFERENCES
VERSIONING
ARCHIVE STATUS
SEARCH
ACCESS CONTROL
PROJECT LINKS
MEMBER LINKS
GRANT LINKS
ACCOUNTING LINKS
AUDIT
BACKUP/RESTORE
EXPORT
```

Out of scope for v1.0:

```text
full OCR platform
electronic signature provider
records-management certification engine
enterprise content-distribution network
AI autonomous filing
```

## Implementation Record 3

- **Architecture object:** Scope
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 4. Architecture Position

The document layer sits beside the business modules:

```text
MEMBERS ─────┐
PROJECTS ────┤
ACCOUNTING ──┼──→ DOCUMENTS & ARCHIVE
GRANTS ──────┤
GOVERNANCE ──┘
                  ↓
                AUDIT
```

Business modules reference documents. They do not create independent document stores.

## Implementation Record 4

- **Architecture object:** Architecture Position
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 5. Document Entity

Minimum:

```text
id
document_number
title
category_id
status
created_by
created_at
updated_at
```

Recommended:

```text
description
file_name
mime_type
file_size
checksum
version
archived_at
archived_by
```

## Implementation Record 5

- **Architecture object:** Document Entity
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 6. Document Number

Document numbers SHALL be unique and stable.

Example:

```text
DOC-2026-000001
DOC-2026-000002
```

The number SHALL be allocated by the service layer.

## Implementation Record 6

- **Architecture object:** Document Number
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 7. Document Metadata

Metadata SHOULD include:

```text
title
description
category
tags
owner
created date
document date
status
version
file type
file size
checksum
```

Metadata is not a substitute for the document itself.

## Implementation Record 7

- **Architecture object:** Document Metadata
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 8. Document Categories

Recommended initial categories:

```text
ACCOUNTING
BANK
MEMBERSHIP
PROJECT
GRANT
GOVERNANCE
MEETING
CONTRACT
INSURANCE
VESSEL
CORRESPONDENCE
LEGAL
TECHNICAL
ARCHIVE
OTHER
```

Categories SHALL be configurable where practical.

## Implementation Record 8

- **Architecture object:** Document Categories
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 9. Document Status

Recommended:

```text
DRAFT
ACTIVE
SUPERSEDED
ARCHIVED
VOID
```

A void document remains historically traceable and SHALL not be silently deleted.

## Implementation Record 9

- **Architecture object:** Document Status
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 10. Document Lifecycle

```text
CREATE
  ↓
CLASSIFY
  ↓
ACTIVE
  ↓
SUPERSEDED / ARCHIVED
  ↓
RETENTION / DISPOSAL
```

## Implementation Record 10

- **Architecture object:** Document Lifecycle
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 11. File Storage Boundary

The document metadata layer and physical file storage are separate concerns.

```text
DocumentService
      ↓
DocumentRepository
      ↓
FileStorageProvider
```

The database stores metadata and storage references, not arbitrary large binary blobs unless the selected storage implementation explicitly requires it.

## Implementation Record 11

- **Architecture object:** File Storage Boundary
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 12. Storage Provider

v1.0 MAY use a controlled local filesystem directory.

The application SHALL not depend on a user's desktop path.

Recommended structure:

```text
data/
  documents/
    2026/
      DOC-2026-000001/
```

## Implementation Record 12

- **Architecture object:** Storage Provider
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 13. Storage Reference

Each document record SHOULD contain a stable internal storage reference.

Do not expose internal filesystem paths as the document identity.

## Implementation Record 13

- **Architecture object:** Storage Reference
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 14. File Integrity

A checksum SHOULD be stored for each uploaded file.

Recommended algorithm:

```text
SHA-256
```

The checksum supports integrity verification and duplicate detection.

## Implementation Record 14

- **Architecture object:** File Integrity
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 15. Duplicate Detection

When a new file has the same checksum as an existing document, the system MAY warn that the file already exists.

It SHALL not silently replace the existing document.

## Implementation Record 15

- **Architecture object:** Duplicate Detection
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 16. Document Version

A document may have versions:

```text
v1
v2
v3
```

A new version SHALL preserve the previous version's history.

## Implementation Record 16

- **Architecture object:** Document Version
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 17. Version Rule

The latest version is the active version unless explicitly superseded or archived.

## Implementation Record 17

- **Architecture object:** Version Rule
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 18. Version Relationship

Recommended:

```text
document_series_id
version_number
previous_version_id
```

This permits a document family to retain its history.

## Implementation Record 18

- **Architecture object:** Version Relationship
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 19. Version Immutability

Once a version has been formally archived or superseded, its physical content SHALL remain immutable.

## Implementation Record 19

- **Architecture object:** Version Immutability
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 20. Document Replacement

Replacing a file SHALL create a new version rather than overwrite the old file.

## Implementation Record 20

- **Architecture object:** Document Replacement
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 21. Document Date

The document date is the date stated on the document, which may differ from upload date.

## Implementation Record 21

- **Architecture object:** Document Date
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 22. Created Date

Created-at records when MFM created the document record.

## Implementation Record 22

- **Architecture object:** Created Date
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 23. Archive Date

Archive date records when the document entered archived status.

## Implementation Record 23

- **Architecture object:** Archive Date
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 24. Document Owner

A document MAY have an owner user.

Ownership does not automatically grant unrestricted access.

## Implementation Record 24

- **Architecture object:** Document Owner
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 25. Access Control

Recommended permissions:

```text
VIEW_DOCUMENTS
CREATE_DOCUMENT
EDIT_DOCUMENT_METADATA
UPLOAD_DOCUMENT_VERSION
ARCHIVE_DOCUMENT
DELETE_DOCUMENT
EXPORT_DOCUMENT
MANAGE_DOCUMENT_CATEGORIES
```

Physical deletion should be highly restricted.

## Implementation Record 25

- **Architecture object:** Access Control
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 26. Default Delete Rule

For documents with business or audit relevance, logical archival is preferred to physical deletion.

## Implementation Record 26

- **Architecture object:** Default Delete Rule
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 27. Business Record Protection

Documents linked to:

```text
accounting
grants
projects
governance
```

SHALL normally be protected from physical deletion.

## Implementation Record 27

- **Architecture object:** Business Record Protection
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 28. Member Documents

Examples:

```text
membership application
consent
correspondence
membership documentation
```

Member document access SHALL respect existing membership privacy controls.

## Implementation Record 28

- **Architecture object:** Member Documents
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 29. Project Documents

Examples:

```text
project plan
quotes
invoices
photos
completion report
```

Project links SHALL reference the project entity rather than duplicate project data.

## Implementation Record 29

- **Architecture object:** Project Documents
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 30. Grant Documents

Examples:

```text
application
award letter
conditions
budget
report
```

Grant records SHALL reference documents rather than store duplicate copies.

## Implementation Record 30

- **Architecture object:** Grant Documents
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 31. Accounting Documents

Examples:

```text
invoice
receipt
bank statement
voucher support
```

Accounting references SHALL remain traceable to the document.

## Implementation Record 31

- **Architecture object:** Accounting Documents
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 32. Governance Documents

Examples:

```text
agenda
minutes
board decision
constitution
policy
```

Governance documents may require restricted access.

## Implementation Record 32

- **Architecture object:** Governance Documents
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 33. Document Link Entity

A controlled document-link mechanism MAY use:

```text
document_id
entity_type
entity_id
link_type
created_by
created_at
```

This supports multiple business modules without duplicating files.

## Implementation Record 33

- **Architecture object:** Document Link Entity
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 34. Link Types

Examples:

```text
PRIMARY_SUPPORT
ATTACHMENT
EVIDENCE
CORRESPONDENCE
APPROVAL
REPORT
RECEIPT
```

## Implementation Record 34

- **Architecture object:** Link Types
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 35. Link Validation

A link SHALL reference an existing document and a valid target entity.

Invalid links SHALL be rejected.

## Implementation Record 35

- **Architecture object:** Link Validation
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 36. No Orphaned References

When a business record is archived, its document references remain available unless explicitly removed under retention policy.

## Implementation Record 36

- **Architecture object:** No Orphaned References
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 37. Document Search

Search SHOULD support:

```text
document number
title
category
tag
file name
date
status
linked project
linked grant
```

## Implementation Record 37

- **Architecture object:** Document Search
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 38. Search Security

Search results SHALL be filtered by the user's document access rights before display.

## Implementation Record 38

- **Architecture object:** Search Security
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 39. Tags

Tags provide flexible classification.

Examples:

```text
2026
restoration
grant
board
invoice
Álvur
```

Tags are metadata and SHALL not replace formal categories.

## Implementation Record 39

- **Architecture object:** Tags
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 40. Tag Management

Tags may be created by authorised users.

The system should avoid uncontrolled tag proliferation through sensible search/autocomplete support.

## Implementation Record 40

- **Architecture object:** Tag Management
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 41. Document Preview

Where the file type is supported, the GUI MAY provide a preview.

Preview failure SHALL not damage the stored document.

## Implementation Record 41

- **Architecture object:** Document Preview
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 42. Download

Downloading a document SHALL require `VIEW_DOCUMENTS` or an equivalent access permission.

## Implementation Record 42

- **Architecture object:** Download
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 43. Export

Exporting documents in bulk SHALL require explicit permission.

Bulk export SHOULD be audited.

## Implementation Record 43

- **Architecture object:** Export
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 44. Document Audit

Minimum events:

```text
DOCUMENT_CREATED
DOCUMENT_METADATA_UPDATED
DOCUMENT_VERSION_CREATED
DOCUMENT_VIEWED
DOCUMENT_DOWNLOADED
DOCUMENT_LINKED
DOCUMENT_UNLINKED
DOCUMENT_ARCHIVED
DOCUMENT_RESTORED
DOCUMENT_VOIDED
DOCUMENT_EXPORTED
```

## Implementation Record 44

- **Architecture object:** Document Audit
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 45. Audit Principle

The audit record identifies:

```text
actor
timestamp
action
document
context
```

Sensitive file content SHALL not be copied into audit logs.

## Implementation Record 45

- **Architecture object:** Audit Principle
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 46. Database Tables

Recommended:

```text
documents
document_versions
document_categories
document_tags
document_links
document_access
```

`document_access` is optional if role-based access is sufficient for v1.0.

## Implementation Record 46

- **Architecture object:** Database Tables
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 47. Documents Table

```text
id
document_number
title
description
category_id
status
current_version_id
owner_user_id
created_by
created_at
updated_at
archived_at
archived_by
```

## Implementation Record 47

- **Architecture object:** Documents Table
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 48. Document Versions Table

```text
id
document_series_id
version_number
file_name
mime_type
file_size
storage_reference
checksum_sha256
created_by
created_at
superseded_at
```

## Implementation Record 48

- **Architecture object:** Document Versions Table
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 49. Categories Table

```text
id
name
description
active
created_at
updated_at
```

## Implementation Record 49

- **Architecture object:** Categories Table
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 50. Tags Table

```text
id
name
created_at
```

## Implementation Record 50

- **Architecture object:** Tags Table
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 51. Document Tag Links

```text
document_id
tag_id
```

Use a composite uniqueness constraint:

```text
(document_id, tag_id)
```

## Implementation Record 51

- **Architecture object:** Document Tag Links
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 52. Document Links Table

```text
id
document_id
entity_type
entity_id
link_type
created_by
created_at
```

## Implementation Record 52

- **Architecture object:** Document Links Table
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 53. Foreign Keys

Enforce:

```text
documents.category_id → document_categories.id
document_versions.document_series_id → documents.id
document_tags.document_id → documents.id
document_tags.tag_id → document_tags.id
document_links.document_id → documents.id
```

The exact version relationship may use a dedicated series table if preferred.

## Implementation Record 53

- **Architecture object:** Foreign Keys
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 54. Indexes

Recommended:

```text
documents.document_number
documents.status
documents.category_id
documents.created_at
document_versions.document_series_id
document_versions.checksum_sha256
document_links.entity_type
document_links.entity_id
```

## Implementation Record 54

- **Architecture object:** Indexes
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 55. Repository Layer

Recommended:

```text
DocumentRepository
DocumentVersionRepository
DocumentCategoryRepository
DocumentTagRepository
DocumentLinkRepository
```

## Implementation Record 55

- **Architecture object:** Repository Layer
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 56. Service Layer

Recommended:

```text
DocumentService
DocumentVersionService
DocumentSearchService
DocumentArchiveService
DocumentLinkService
```

## Implementation Record 56

- **Architecture object:** Service Layer
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 57. Upload Flow

```text
Select File
 ↓
Validate Permission
 ↓
Validate File
 ↓
Calculate Checksum
 ↓
Store File
 ↓
Create Metadata
 ↓
Create Version
 ↓
Create Audit
 ↓
Commit
```

## Implementation Record 57

- **Architecture object:** Upload Flow
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 58. Upload Failure

If metadata creation or audit fails after file storage, the system SHALL clean up the unreferenced physical file or mark it for safe recovery.

No orphaned file should silently accumulate.

## Implementation Record 58

- **Architecture object:** Upload Failure
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 59. Atomicity

Where physical storage cannot participate in a database transaction, use a controlled two-phase approach:

```text
TEMP STORAGE
 ↓
DATABASE COMMIT
 ↓
PROMOTE TO FINAL STORAGE
```

or an equivalent recoverable strategy.

## Implementation Record 59

- **Architecture object:** Atomicity
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 60. Storage Recovery

A maintenance check MAY identify:

```text
database reference without file
file without database reference
checksum mismatch
```

These conditions SHALL be reported rather than silently corrected.

## Implementation Record 60

- **Architecture object:** Storage Recovery
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 61. Checksum Verification

On access or scheduled maintenance, checksum verification MAY be performed.

A mismatch SHALL produce an integrity warning and audit event.

## Implementation Record 61

- **Architecture object:** Checksum Verification
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 62. Archive

Archiving removes a document from normal active workflows while retaining it for historical access according to permissions.

## Implementation Record 62

- **Architecture object:** Archive
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 63. Restore from Archive

An authorised user may restore an archived document.

The restore SHALL be audited.

## Implementation Record 63

- **Architecture object:** Restore from Archive
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 64. Void

A void document remains available for historical traceability but is excluded from normal active selection.

## Implementation Record 64

- **Architecture object:** Void
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 65. Physical Deletion

Physical deletion should be reserved for:

```text
temporary files
accidental uploads
legally required disposal
```

and require elevated permission.

## Implementation Record 65

- **Architecture object:** Physical Deletion
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 66. Retention

v1.0 provides retention metadata and manual/archive controls.

The association's legal and accounting retention policy remains authoritative.

## Implementation Record 66

- **Architecture object:** Retention
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 67. Retention Metadata

Optional fields:

```text
retention_class
retention_until
disposal_eligible
```

## Implementation Record 67

- **Architecture object:** Retention Metadata
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 68. No Automatic Destruction

MFM SHALL not automatically destroy records merely because a retention date has passed unless the association explicitly configures and authorises such behaviour.

## Implementation Record 68

- **Architecture object:** No Automatic Destruction
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 69. Legal Hold

A future legal-hold function may prevent disposal.

For v1.0, a simple:

```text
disposal_blocked
```

flag may be sufficient where required.

## Implementation Record 69

- **Architecture object:** Legal Hold
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 70. Backup

Document files and document metadata SHALL be included in the association's backup strategy.

## Implementation Record 70

- **Architecture object:** Backup
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 71. Backup Consistency

A backup SHALL contain enough information to restore:

```text
metadata
versions
links
files
audit references
```

## Implementation Record 71

- **Architecture object:** Backup Consistency
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 72. Restore Test

After restore, verify:

```text
document count
version count
file existence
checksum
links
permissions
```

## Implementation Record 72

- **Architecture object:** Restore Test
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 73. Document Import

Optional CSV/XLSX metadata import may be supported.

Physical file import SHALL require controlled mapping and validation.

## Implementation Record 73

- **Architecture object:** Document Import
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 74. Import Flow

```text
Preview
 ↓
Validate
 ↓
User Confirm
 ↓
Import
 ↓
Audit
```

## Implementation Record 74

- **Architecture object:** Import Flow
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 75. Document Export

A metadata export may include:

```text
document number
title
category
status
version
created date
links
```

Do not export unnecessary private data.

## Implementation Record 75

- **Architecture object:** Document Export
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 76. Document Bundle

A future project or grant report may generate a controlled bundle of linked documents.

v1.0 should keep this simple and permission-controlled.

## Implementation Record 76

- **Architecture object:** Document Bundle
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 77. No Duplicate Storage

If the same file is linked to multiple entities, store the file once and create multiple document links.

## Implementation Record 77

- **Architecture object:** No Duplicate Storage
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 78. Document Relationships

One document may relate to:

```text
project
grant
member
accounting voucher
meeting
```

without copying the file.

## Implementation Record 78

- **Architecture object:** Document Relationships
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 79. Meeting Documents

Meeting agendas and minutes may link to a governance meeting record if such a module exists.

## Implementation Record 79

- **Architecture object:** Meeting Documents
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 80. Policy Documents

Policies may be stored with controlled versioning so the association can identify which version was active at a given time.

## Implementation Record 80

- **Architecture object:** Policy Documents
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 81. Constitution

The association constitution should be treated as a controlled governance document with strong version history and restricted modification.

## Implementation Record 81

- **Architecture object:** Constitution
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 82. Accounting Document Link

An accounting voucher may reference supporting documents through `document_links`.

Accounting remains authoritative for the financial transaction.

## Implementation Record 82

- **Architecture object:** Accounting Document Link
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 83. Grant Document Link

A funding application may reference:

```text
application letter
budget
quotes
decision
award
report
```

## Implementation Record 83

- **Architecture object:** Grant Document Link
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 84. Project Document Link

A project may reference all supporting material without duplicating files.

## Implementation Record 84

- **Architecture object:** Project Document Link
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 85. Member Document Link

Member documents SHALL be visible only to users with the required membership/document permissions.

## Implementation Record 85

- **Architecture object:** Member Document Link
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 86. Privacy Boundary

The document module SHALL not weaken the privacy rules of the linked business module.

## Implementation Record 86

- **Architecture object:** Privacy Boundary
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 87. Access Resolution

A document request SHOULD evaluate:

```text
user role
document permission
entity relationship
document status
```

before granting access.

## Implementation Record 87

- **Architecture object:** Access Resolution
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 88. Sensitive Category

The association MAY mark categories as restricted.

Examples:

```text
LEGAL
MEMBER_PRIVATE
BOARD_CONFIDENTIAL
```

## Implementation Record 88

- **Architecture object:** Sensitive Category
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 89. Restricted Access

Restricted documents require explicit authority.

A visible title may still need to be hidden if metadata itself is confidential.

## Implementation Record 89

- **Architecture object:** Restricted Access
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 90. No Security by Filename

Security SHALL never depend on a hidden filename or filesystem path.

## Implementation Record 90

- **Architecture object:** No Security by Filename
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 91. File Naming

Stored physical names SHOULD be generated from stable identifiers rather than user-provided names.

Original filename remains metadata.

## Implementation Record 91

- **Architecture object:** File Naming
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 92. Path Safety

The system SHALL reject path traversal attempts and unsafe storage paths.

## Implementation Record 92

- **Architecture object:** Path Safety
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 93. File Type Validation

The system SHOULD validate:

```text
extension
MIME type
file signature
size
```

where practical.

## Implementation Record 93

- **Architecture object:** File Type Validation
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 94. Maximum File Size

A configurable maximum upload size SHALL protect the application from accidental oversized uploads.

## Implementation Record 94

- **Architecture object:** Maximum File Size
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 95. Configuration

Recommended:

```text
document_storage_root
max_file_size
allowed_file_types
default_category
checksum_algorithm
```

## Implementation Record 95

- **Architecture object:** Configuration
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 96. Allowed File Types

Typical:

```text
PDF
DOCX
XLSX
CSV
JPG
PNG
TXT
```

The list is configurable.

## Implementation Record 96

- **Architecture object:** Allowed File Types
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 97. Malware Boundary

MFM v1.0 SHALL not claim to provide antivirus protection. If an external scanner is available, files may be scanned before activation.

## Implementation Record 97

- **Architecture object:** Malware Boundary
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 98. Quarantine

If scanning is implemented:

```text
UPLOADED
 ↓
QUARANTINED
 ↓
SCANNED
 ↓
ACTIVE
```

A failed scan SHALL prevent activation.

## Implementation Record 98

- **Architecture object:** Quarantine
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 99. Document Service API

Recommended:

```text
create_document()
upload_version()
get_document()
list_documents()
search_documents()
archive_document()
restore_document()
void_document()
```

## Implementation Record 99

- **Architecture object:** Document Service API
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 100. Document Link API

```text
link_document()
unlink_document()
list_entity_documents()
```

Unlinking does not delete the document.

## Implementation Record 100

- **Architecture object:** Document Link API
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 101. Archive API

```text
archive()
restore()
get_archive()
```

## Implementation Record 101

- **Architecture object:** Archive API
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 102. No Direct SQL

GUI and business modules SHALL use the document services/repositories rather than direct SQL file manipulation.

## Implementation Record 102

- **Architecture object:** No Direct SQL
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 103. Transaction: Metadata

Metadata changes SHALL be transactional and audited.

## Implementation Record 103

- **Architecture object:** Transaction: Metadata
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 104. Transaction: Version

Version creation SHALL ensure:

```text
file exists
checksum valid
metadata valid
version unique
```

before activation.

## Implementation Record 104

- **Architecture object:** Transaction: Version
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 105. Transaction: Link

Document linking SHALL validate both source and target before committing.

## Implementation Record 105

- **Architecture object:** Transaction: Link
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 106. Transaction: Archive

Archive SHALL update state and audit atomically.

## Implementation Record 106

- **Architecture object:** Transaction: Archive
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 107. Failure Handling

If a document operation fails:

```text
preserve previous valid state
report error
do not partially overwrite metadata
```

## Implementation Record 107

- **Architecture object:** Failure Handling
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 108. Idempotency

Repeated archive/restore operations SHALL not create duplicate state transitions or duplicate audit events beyond the configured event semantics.

## Implementation Record 108

- **Architecture object:** Idempotency
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 109. Search Performance

For a small association, ordinary database indexes and metadata search are sufficient.

A full search engine is unnecessary for v1.0.

## Implementation Record 109

- **Architecture object:** Search Performance
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 110. Expected Scale

The module should comfortably support:

```text
tens of thousands of document records
multiple versions per record
hundreds of thousands of metadata links
```

without specialised infrastructure.

## Implementation Record 110

- **Architecture object:** Expected Scale
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 111. Document Dashboard

Recommended indicators:

```text
active documents
recent uploads
recent versions
archived documents
missing files
integrity warnings
```

## Implementation Record 111

- **Architecture object:** Document Dashboard
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 112. Project Document View

Project detail should show linked documents with:

```text
title
category
version
date
status
```

and access-controlled actions.

## Implementation Record 112

- **Architecture object:** Project Document View
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 113. Grant Document View

Award/application detail should show linked evidence documents and reporting files.

## Implementation Record 113

- **Architecture object:** Grant Document View
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 114. Accounting Document View

Voucher detail may show supporting invoices or receipts through document links.

## Implementation Record 114

- **Architecture object:** Accounting Document View
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 115. Member Document View

Member detail may show authorised documents without exposing restricted records to unauthorised users.

## Implementation Record 115

- **Architecture object:** Member Document View
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 116. Governance Document View

Meeting detail may show agenda, minutes and supporting material.

## Implementation Record 116

- **Architecture object:** Governance Document View
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 117. Document List Filters

Recommended:

```text
category
status
date
tag
linked entity
```

## Implementation Record 117

- **Architecture object:** Document List Filters
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 118. Document Sorting

Sort by:

```text
date
title
document number
category
updated
```

## Implementation Record 118

- **Architecture object:** Document Sorting
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 119. Version History UI

A document detail screen SHALL allow authorised users to see:

```text
version
date
creator
status
checksum
```

and access previous versions when permitted.

## Implementation Record 119

- **Architecture object:** Version History UI
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 120. Audit History UI

The document detail may show material audit history to authorised users.

## Implementation Record 120

- **Architecture object:** Audit History UI
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 121. Download Audit

Downloads of restricted or business-critical documents SHOULD be audited.

## Implementation Record 121

- **Architecture object:** Download Audit
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 122. Report Templates

Minimum reports:

```text
Document Register
Archive Register
Document Integrity Report
Project Document List
Grant Document List
Accounting Support Document List
```

## Implementation Record 122

- **Architecture object:** Report Templates
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 123. Document Register

Shows:

```text
number
title
category
status
version
created
updated
```

## Implementation Record 123

- **Architecture object:** Document Register
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 124. Archive Register

Shows:

```text
document
archive date
archived by
reason
status
```

## Implementation Record 124

- **Architecture object:** Archive Register
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 125. Integrity Report

Shows:

```text
missing file
checksum mismatch
orphan file
orphan reference
```

## Implementation Record 125

- **Architecture object:** Integrity Report
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 126. Document Retention Report

Optional report:

```text
retention class
retention date
disposal eligible
hold
```

## Implementation Record 126

- **Architecture object:** Document Retention Report
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 127. Security Test

Verify every permission:

```text
VIEW_DOCUMENTS
CREATE_DOCUMENT
EDIT_DOCUMENT_METADATA
UPLOAD_DOCUMENT_VERSION
ARCHIVE_DOCUMENT
DELETE_DOCUMENT
EXPORT_DOCUMENT
```

## Implementation Record 127

- **Architecture object:** Security Test
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 128. Negative Test: Missing File

Database points to a missing file.

Expected:

```text
INTEGRITY WARNING
```

Never silently show a healthy document state.

## Implementation Record 128

- **Architecture object:** Negative Test: Missing File
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 129. Negative Test: Checksum

Stored checksum differs from file checksum.

Expected:

```text
INTEGRITY ERROR
```

The system SHALL not silently replace the file.

## Implementation Record 129

- **Architecture object:** Negative Test: Checksum
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 130. Negative Test: Duplicate Link

Attempt to create the same document/entity/link type twice.

Expected:

```text
REJECTED or idempotent no-op
```

## Implementation Record 130

- **Architecture object:** Negative Test: Duplicate Link
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 131. Negative Test: Unauthorized Download

User without view permission attempts download.

Expected:

```text
DENIED
```

## Implementation Record 131

- **Architecture object:** Negative Test: Unauthorized Download
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 132. Negative Test: Unauthorized Archive

User without archive permission attempts archive.

Expected:

```text
DENIED
```

## Implementation Record 132

- **Architecture object:** Negative Test: Unauthorized Archive
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 133. Negative Test: Version Collision

Attempt to create an existing version number.

Expected:

```text
REJECTED
```

## Implementation Record 133

- **Architecture object:** Negative Test: Version Collision
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 134. Negative Test: Path Traversal

Malicious filename/path is supplied.

Expected:

```text
REJECTED
```

The storage provider SHALL generate safe internal paths.

## Implementation Record 134

- **Architecture object:** Negative Test: Path Traversal
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 135. Negative Test: Oversized File

File exceeds configured maximum.

Expected:

```text
REJECTED before activation
```

## Implementation Record 135

- **Architecture object:** Negative Test: Oversized File
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 136. Negative Test: Unsupported Type

Unsupported file type.

Expected:

```text
REJECTED
```

unless the type is added to configuration.

## Implementation Record 136

- **Architecture object:** Negative Test: Unsupported Type
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 137. Scenario 1: Upload Invoice

```text
Upload invoice
 ↓
Category ACCOUNTING
 ↓
Link voucher
 ↓
Audit
```

Expected one physical document with one accounting link.

## Implementation Record 137

- **Architecture object:** Scenario 1: Upload Invoice
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 138. Scenario 2: Grant Package

```text
Create application
 ↓
Upload application
 ↓
Upload budget
 ↓
Upload quotes
 ↓
Link all to application
```

Expected no duplicate storage and complete traceability.

## Implementation Record 138

- **Architecture object:** Scenario 2: Grant Package
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 139. Scenario 3: Project Photos

Multiple photographs link to the same project.

Expected independent documents with shared project reference, no duplicate project records.

## Implementation Record 139

- **Architecture object:** Scenario 3: Project Photos
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 140. Scenario 4: Versioned Minutes

```text
Minutes v1
 ↓
Correction
 ↓
Minutes v2
```

Expected v1 retained and v2 active.

## Implementation Record 140

- **Architecture object:** Scenario 4: Versioned Minutes
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 141. Scenario 5: Archive

```text
Active document
 ↓
Archive
 ↓
Search active list
```

Expected document absent from normal active workflow but available through archive to authorised users.

## Implementation Record 141

- **Architecture object:** Scenario 5: Archive
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 142. Scenario 6: Restore

```text
Archived
 ↓
Restore
```

Expected active state restored and audit created.

## Implementation Record 142

- **Architecture object:** Scenario 6: Restore
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 143. Scenario 7: Integrity Failure

Delete or corrupt a test file outside MFM.

Expected integrity scan identifies the discrepancy.

## Implementation Record 143

- **Architecture object:** Scenario 7: Integrity Failure
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 144. Scenario 8: Access

Restricted board document accessed by authorised user.

Expected success.

Unauthorised user:

```text
DENIED
```

## Implementation Record 144

- **Architecture object:** Scenario 8: Access
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 145. Scenario 9: Multi-Link

One invoice document links to:

```text
project
accounting voucher
grant
```

Expected one stored document and three controlled references.

## Implementation Record 145

- **Architecture object:** Scenario 9: Multi-Link
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 146. Scenario 10: Backup Restore

Backup and restore a dataset containing documents.

Expected metadata, files, versions, links and audit remain consistent.

## Implementation Record 146

- **Architecture object:** Scenario 10: Backup Restore
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 147. AI Assistance

AI MAY assist with:

```text
document classification suggestion
tag suggestion
summary
duplicate detection
missing-document detection
search assistance
```

AI output SHALL be treated as a recommendation unless explicitly approved.

## Implementation Record 147

- **Architecture object:** AI Assistance
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 148. AI Boundary

AI SHALL NOT autonomously:

```text
delete records
change retention policy
release confidential documents
archive legally significant records
alter accounting evidence
```

## Implementation Record 148

- **Architecture object:** AI Boundary
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 149. AI Workflow

```text
DOCUMENT
 ↓
AI ANALYSIS
 ↓
SUGGESTION
 ↓
HUMAN CONFIRMATION
 ↓
METADATA UPDATE
 ↓
AUDIT
```

## Implementation Record 149

- **Architecture object:** AI Workflow
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 150. Autonomous Safe State

If AI confidence is low or document classification conflicts with policy:

```text
leave document unchanged
request human review
```

## Implementation Record 150

- **Architecture object:** Autonomous Safe State
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 151. Recovery

After storage failure:

```text
identify temp files
verify database references
verify checksums
repair or quarantine
audit recovery
```

## Implementation Record 151

- **Architecture object:** Recovery
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 152. No Silent Repair

The system SHALL never silently substitute a different document to repair a missing or corrupt file.

## Implementation Record 152

- **Architecture object:** No Silent Repair
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 153. Document Reconciliation

Reconciliation should compare:

```text
database documents
database versions
physical files
checksums
links
```

## Implementation Record 153

- **Architecture object:** Document Reconciliation
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 154. Reconciliation Status

Recommended:

```text
HEALTHY
WARNING
ERROR
```

## Implementation Record 154

- **Architecture object:** Reconciliation Status
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 155. Project Closure

Closing a project SHALL retain all linked documents.

Documents do not disappear because the project is completed.

## Implementation Record 155

- **Architecture object:** Project Closure
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 156. Grant Closure

Closing an award SHALL retain application, award, reporting and evidence documents.

## Implementation Record 156

- **Architecture object:** Grant Closure
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 157. Member Closure

A member record becoming inactive SHALL not automatically delete historical documents.

## Implementation Record 157

- **Architecture object:** Member Closure
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 158. Accounting Closure

Closing an accounting period SHALL not remove supporting documents.

## Implementation Record 158

- **Architecture object:** Accounting Closure
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 159. Governance Archive

Governance documents should remain accessible according to their retention and access policy.

## Implementation Record 159

- **Architecture object:** Governance Archive
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 160. No Automatic Deletion

Business records SHALL not be deleted merely because they are old or no longer active.

## Implementation Record 160

- **Architecture object:** No Automatic Deletion
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 161. Release Acceptance

The module is accepted when:

```text
documents can be created
files can be stored
versions work
links work
search works
archive works
restore works
access control works
audit works
integrity checks work
backup/restore works
```

## Implementation Record 161

- **Architecture object:** Release Acceptance
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 162. Release Blockers

Release SHALL be blocked by:

```text
unsafe storage paths
lost files
checksum mismatch not detected
unauthorised access
version history loss
broken business links
missing audit
inability to restore documents
```

## Implementation Record 162

- **Architecture object:** Release Blockers
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 163. Implementation Order

Implement:

```text
1. storage provider
2. document metadata
3. categories
4. versions
5. links
6. search
7. archive
8. permissions
9. audit
10. reports
11. integrity checks
12. backup/restore tests
```

## Implementation Record 163

- **Architecture object:** Implementation Order
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 164. First Milestone

```text
Upload document
 ↓
Store metadata
 ↓
View document
```

## Implementation Record 164

- **Architecture object:** First Milestone
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 165. Second Milestone

```text
Create version
 ↓
View version history
 ↓
Restore/access old version
```

## Implementation Record 165

- **Architecture object:** Second Milestone
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 166. Third Milestone

```text
Link document
 ↓
Open project/grant/accounting record
 ↓
View linked document
```

## Implementation Record 166

- **Architecture object:** Third Milestone
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 167. Fourth Milestone

```text
Archive
 ↓
Restore
 ↓
Audit
```

## Implementation Record 167

- **Architecture object:** Fourth Milestone
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 168. Fifth Milestone

```text
Backup
 ↓
Restore
 ↓
Verify checksum
 ↓
Verify links
```

## Implementation Record 168

- **Architecture object:** Fifth Milestone
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 169. Final Architecture

```text
                    DOCUMENT SERVICE
                          ↓
                 ┌────────┴────────┐
                 ↓                 ↓
             METADATA          FILE STORAGE
                 ↓                 ↓
             VERSIONING       CHECKSUM
                 ↓                 ↓
                 └────────┬────────┘
                          ↓
                       LINKS
                          ↓
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
       PROJECT          GRANTS         ACCOUNTING
          ↓               ↓               ↓
          └───────────────┼───────────────┘
                          ↓
                        AUDIT
                          ↓
                       ARCHIVE
```

## Implementation Record 169

- **Architecture object:** Final Architecture
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 170. Final Rules

```text
RULE 1
Store each physical document once.

RULE 2
Use links to connect documents to business records.

RULE 3
Never overwrite a historical document version.

RULE 4
Business records remain authoritative for their own data.

RULE 5
Document access never bypasses business-module privacy.

RULE 6
Archive before delete whenever practical.

RULE 7
Integrity failures enter a safe state.

RULE 8
AI may suggest classification but does not gain authority.

RULE 9
Backups must include files and metadata.

RULE 10
The document system must remain simple enough for volunteers.
```

## Implementation Record 170

- **Architecture object:** Final Rules
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 171. Next Layer

The next implementation layer should be:

```text
MFM v1.0 Reporting & Dashboard Implementation
```

It will turn the existing accounting, membership, project, grants and document layers into practical operational and board-level dashboards and reports.

## Implementation Record 171

- **Architecture object:** Next Layer
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.

# 172. Governing Principle

> **MFM shall store organisational documents once, preserve their history, connect them to the association's real business records, protect access, and make retrieval simple without turning a small non-profit application into an enterprise records-management system.**

## Implementation Record 172

- **Architecture object:** Governing Principle
- **Layer:** Document & Archive
- **Authority:** Human-authorised operation
- **Security:** Existing MFM SecurityContext and permissions
- **Audit:** Required for material state changes
- **Failure handling:** Preserve last valid state; quarantine unsafe storage state
- **Lifecycle:** Create → Validate → Store → Link → Audit → Archive
- **Acceptance:** Deterministic, traceable, recoverable and proportionate to a small association.


# 193. Final Acceptance Checklist

```text
[ ] Document register implemented
[ ] Secure storage implemented
[ ] Metadata implemented
[ ] Categories implemented
[ ] Tags implemented
[ ] Versioning implemented
[ ] Document links implemented
[ ] Search implemented
[ ] Archive implemented
[ ] Restore implemented
[ ] Access control implemented
[ ] Audit implemented
[ ] Checksum integrity implemented
[ ] Backup includes files
[ ] Restore test passed
[ ] Project integration passed
[ ] Grant integration passed
[ ] Accounting integration passed
[ ] Membership integration passed
[ ] Negative tests passed
```

# 194. Release Decision

The Document & Archive module may enter MFM v1.0 release only when documents can be stored, retrieved, linked, protected, versioned and restored without loss of historical integrity.

# END OF MFM v1.0 DOCUMENT & ARCHIVE IMPLEMENTATION
