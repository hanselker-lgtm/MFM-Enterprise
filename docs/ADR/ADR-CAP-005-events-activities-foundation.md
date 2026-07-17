# ADR-CAP-005: Events & Activities Foundation

Date: 2026-07-17
Status: Accepted

## Context

CAP-005 introduces event and activity management capability under strict constraints:

- use Feature APIs only for cross-capability orchestration
- no direct repository access across capabilities
- do not modify Membership, Billing, Organization, or Accounting internals

## Decision

Implement CAP-005 as an isolated `events_activities` capability:

1. Domain
- Added `Event`, `Activity`, `Registration`, `Attendance`, `Venue`, and `Schedule`.
- Added aggregate boundary `EventActivityProfile` to centralize event mutations.

2. Repository
- Added `EventsActivitiesRepository` contract.
- Added `SQLiteEventsActivitiesRepository` adapter as process-local baseline persistence.

3. Service + Feature API
- Added `EventsActivitiesService` operations:
  - create event
  - add activity
  - register participant
  - record attendance
- Added `ManageEventsActivitiesFeature` with immutable request/response DTOs and exception mapping.

4. Workflow
- Added `EventsActivitiesWorkflow` to orchestrate feature execution in workflow contexts.

5. Reporting API
- Added `EventsActivitiesSummaryService` and `EventsActivitiesSummaryFeature`.
- Added reporting DTOs for event-level counts.

6. GUI
- Added route `operations.events-activities` with optional shell loader injection.

## Consequences

Positive:
- CAP-005 is independently testable and deployable.
- Boundaries remain architecture-compliant and DTO-safe.
- No protected internals were modified.

Trade-offs:
- Persistence adapter is process-local and should be replaced by durable persistence in future increments.

Out of scope:
- changes to Membership/Billing/Organization/Accounting internals
- cross-capability repository coupling
