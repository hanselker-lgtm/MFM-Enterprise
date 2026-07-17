# CAP-006 Capability Integration Report

Date: 2026-07-17
Capability: Document & Archive Management

## Integration Scope

CAP-006 integrates through feature API boundaries and attachment references only.

### Upstream Feature APIs used

1. Documents capability (`mfm.application.features.documents`)
- `CreateDocumentFeature`
- `RegisterDocumentVersionFeature`
- `AttachReferenceFeature`
- `ArchiveDocumentFeature`

## Cross-Capability Integration Model

CAP-006 links documents to external capabilities using `Attachment.target_capability` with allowed values:

- `MEMBERSHIP`
- `ORGANIZATION`
- `EVENTS`
- `BILLING`
- `PROJECTS`

These links are reference-only and do not access foreign repositories.

## Architectural Boundaries

- No direct repository access into Membership, Organization, Events, Billing, or Projects.
- No modifications to internals of integrated capabilities.
- All orchestration performed via feature DTOs and capability-local repository.

## Data and Flow Summary

1. Create document
- CAP-006 calls `CreateDocumentFeature`.
- CAP-006 persists folder/category/archive metadata in its own repository.

2. Add version
- CAP-006 calls `RegisterDocumentVersionFeature`.
- CAP-006 updates capability-local version metadata.

3. Attach reference
- CAP-006 calls `AttachReferenceFeature`.
- CAP-006 stores allowed cross-capability attachment metadata.

4. Archive
- CAP-006 calls `ArchiveDocumentFeature`.
- CAP-006 records archive reason and timestamp.

5. Reporting
- CAP-006 reporting reads only `DocumentArchiveRepository` and emits per-capability link counts.

## Validation

- `python -m pytest -q`
- `python -m ruff check .`
