# ADR-CAP-006: Document & Archive Management

Date: 2026-07-17
Status: Accepted

## Context

CAP-006 requires document and archive capability with strict architecture constraints:

- use Feature APIs only
- integrate with Membership, Organization, Events, Billing, and Projects
- no direct repository access across capabilities

The codebase already exposes document lifecycle operations through document feature APIs.

## Decision

Implement CAP-006 as a dedicated `document_archive` capability that composes existing document feature APIs:

1. Domain
- Added `Document`, `Folder`, `Version`, `Attachment`, `Archive`, `Category`.

2. Repository
- Added `DocumentArchiveRepository` contract.
- Added `SQLiteDocumentArchiveRepository` adapter (process-local persistence baseline).

3. Service + Feature API
- Added `DocumentArchiveService` operations:
  - create document
  - add version
  - attach reference
  - archive record
- Added `ManageDocumentArchiveFeature` with immutable request/response DTOs and exception mapping.

4. Workflow
- Added `DocumentArchiveWorkflow` for workflow orchestration.

5. Reporting API
- Added `DocumentArchiveSummaryService` and `DocumentArchiveSummaryFeature`.
- Added summary DTOs including cross-capability integration link counts.

6. GUI
- Added route `operations.document-archive` and optional loader injection.

## Consequences

Positive:
- CAP-006 uses existing document feature APIs and avoids direct persistence coupling to other capabilities.
- Integration with Membership, Organization, Events, Billing, and Projects is explicit via attachment target capabilities and reporting counters.

Trade-offs:
- Repository adapter is process-local and should be replaced with durable persistence in future increments.

Out of scope:
- modifications to internals of Membership, Organization, Events, Billing, or Projects capabilities
