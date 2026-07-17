# CAP-004 Capability Integration Report

Date: 2026-07-17
Capability: Membership Fees & Billing

## Integration Scope

CAP-004 integrates with existing capabilities through Feature APIs only.

### Upstream Feature APIs used

1. `CreateAnnualContingentFeature` (`mfm.application.features.annual_contingent_generation`)
- Used to generate invoices and journal drafts for billing runs.
- Called from CAP-004 service with `CreateAnnualContingentRequest`.

### Architectural Boundaries

- No direct repository access from CAP-004 into Membership, Accounting, or Organization capabilities.
- No modifications to `mfm.domain.accounting` or accounting persistence internals.
- No duplicated invoice domain logic: CAP-004 `Invoice`, `InvoiceLine`, and `Payment` reuse finance domain implementations.

## Data and Flow Summary

1. Fee schedule setup
- CAP-004 persists schedule in `MembershipBillingRepository`.

2. Billing run
- CAP-004 service invokes `CreateAnnualContingentFeature`.
- CAP-004 stores only run summaries in profile history.

3. Reminder management
- CAP-004 stores reminder artifacts in its own repository.

4. Reporting
- CAP-004 reporting reads only `MembershipBillingRepository`.

## Risk Notes

- Process-local repository adapter is suitable for foundation scope but must be replaced for durable production billing history.
- Annual contingent feature behavior is now a dependency for CAP-004 invoice creation semantics.

## Validation

- Full test suite and lint run required:
  - `python -m pytest -q`
  - `python -m ruff check .`
