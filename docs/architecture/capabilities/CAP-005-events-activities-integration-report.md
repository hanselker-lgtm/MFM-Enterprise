# CAP-005 Capability Integration Report

Date: 2026-07-17
Capability: Events & Activities Foundation

## Integration Scope

CAP-005 currently operates within its own capability boundary and does not require cross-capability repository access.

## Architectural Boundaries

- No direct repository access into Membership, Billing, Organization, or Accounting capabilities.
- No modifications to Membership, Billing, Organization, or Accounting internals.
- Feature/API boundary is preserved through immutable request/response DTOs.

## Data and Flow Summary

1. Event setup
- CAP-005 service creates `Venue`, `Schedule`, `Event` and persists `EventActivityProfile`.

2. Activity management
- CAP-005 service appends `Activity` records to profile boundary.

3. Registration
- CAP-005 service appends `Registration` records to profile boundary.

4. Attendance
- CAP-005 service appends `Attendance` records with registration/activity validation.

5. Reporting
- CAP-005 reporting reads only `EventsActivitiesRepository`.

## Risk Notes

- Process-local repository adapter is suitable for foundation scope but not durable production history.

## Validation

- Full suite and lint gates:
  - `python -m pytest -q`
  - `python -m ruff check .`
