# ADR-CAP-003: Contact & Communication Foundation

Date: 2026-07-17
Status: Accepted

## Context

CAP-003 requires a dedicated Contact & Communication capability that follows existing DDD architecture while remaining independent from:

- Accounting
- Membership
- Organization

Required capability artifacts include domain concepts for contact methods and communication preferences, repository abstraction, service/feature/workflow boundaries, reporting API, GUI shell route integration, and testable architecture.

## Decision

Implement CAP-003 as a standalone capability package `contact_communication` across layers:

1. Domain
- Added `ContactMethod`, `CommunicationPreference`, `Notification`, `EmailAddress`, `PhoneNumber`, `PostalAddress`.
- Added aggregate root `ContactCommunicationProfile` to coordinate methods, preference, and notifications.

2. Repositories
- Added `ContactCommunicationRepository` contract.
- Added `SQLiteContactCommunicationRepository` process-local adapter for profile persistence.

3. Services and Feature API
- Added `ContactCommunicationService` with immutable request/response DTOs.
- Added `ManageContactCommunicationFeature` with standardized validation and exception mapping.

4. Workflow
- Added `ContactCommunicationWorkflow` as a workflow-level wrapper around the feature API.

5. Reporting API
- Added `ContactCommunicationSummaryService` and `ContactCommunicationSummaryFeature`.
- Added `ContactCommunicationSummaryResponse` DTO for method/notification metrics.

6. GUI Shell
- Added route `operations.contact-communication` with optional dedicated loader hook.

## Consequences

Positive:
- CAP-003 delivers a complete independent contact communication foundation using established DDD layering.
- Feature boundaries are immutable DTOs and architecture-safe.
- Existing Accounting, Membership, and Organization modules remain unchanged.

Trade-offs:
- The repository adapter is process-local and should be replaced by dedicated persistent models in a later increment.
- Initial capability scope prioritizes foundation and integration points over delivery-channel infrastructure.

Out of scope:
- accounting behavior changes
- membership behavior changes
- organization behavior changes
