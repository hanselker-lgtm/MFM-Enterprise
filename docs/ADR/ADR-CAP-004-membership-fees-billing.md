# ADR-CAP-004: Membership Fees & Billing

Date: 2026-07-17
Status: Accepted

## Context

CAP-004 requires membership fee and billing capability with strict architectural constraints:

- use Feature APIs only for cross-capability orchestration
- no direct repository access across capabilities
- do not modify Accounting internals
- do not duplicate invoice logic

The codebase already contains invoice/payment domain logic in `mfm.domain.finance` and annual contingent invoice generation in `CreateAnnualContingentFeature`.

## Decision

Implement CAP-004 as an independent `membership_billing` capability:

1. Domain
- Added `MembershipFee`, `FeeSchedule`, `Reminder` and aggregate `MembershipBillingProfile`.
- Added capability-level aliases for `Invoice`, `InvoiceLine`, and `Payment` that directly reuse finance domain implementations.

2. Repositories
- Added `MembershipBillingRepository` contract.
- Added `SQLiteMembershipBillingRepository` adapter (process-local persistence for capability foundation).

3. Services and Feature API
- Added `MembershipBillingService` with operations:
  - setup fee schedule
  - run billing
  - create reminder
- Added `ManageMembershipBillingFeature` with immutable request/response DTOs and exception mapping.

4. Workflow
- Added `MembershipBillingWorkflow` wrapper for feature orchestration.

5. Reporting API
- Added `MembershipBillingSummaryService` and `MembershipBillingSummaryFeature`.
- Added summary DTOs.

6. GUI
- Added route `operations.membership-billing` and optional loader in application shell.

## Consequences

Positive:
- Billing runs reuse `CreateAnnualContingentFeature`, avoiding duplicated invoice logic.
- CAP-004 stays decoupled from Accounting internals and cross-capability repository access.
- Feature boundaries remain DTO-safe and architecture-compliant.

Trade-offs:
- Current CAP-004 repository adapter is process-local and should be backed by dedicated persistence models in later increments.
- CAP-004 currently relies on annual contingent semantics for invoice generation cadence.

Out of scope:
- accounting internal refactors
- direct invoice logic reimplementation
- bypassing existing feature APIs for billing creation
