# Capability Portfolio

Scope: remaining capabilities in the roadmap that are not LOCKED.

## Portfolio Summary

Only two roadmap capabilities remain outside the LOCKED state:
- Organization
- Asset Core

Both capabilities have completed review evidence and are ready for final lock work.

## Prioritized Implementation Order

| Priority | Capability ID | Capability Name | Current Status | Dependencies | Estimated Size | Business Value | Technical Risk | Recommended Priority |
|---|---|---|---|---|---|---|---|---|
| 1 | ORG-000..ORG-011 | Organization | REVIEW | Identity/reference boundaries only; foundational consumer/provider for other business capabilities | S | 5 | 2 | Highest |
| 2 | ASSET-000..ASSET-007 | Asset Core | REVIEW | Organization identity/reference boundaries; downstream operational capabilities may consume asset identities | S | 4 | 2 | High |

## Capability Notes

### Organization
- Review evidence: `organization_capability_review.md`
- Current state: review-approved and ready for lock
- Rationale: it is the broader foundational business capability and a dependency anchor for several downstream capabilities.

### Asset Core
- Review evidence: `asset_capability_review.md`
- Current state: review-approved and ready for lock
- Rationale: it is also ready, but is slightly less central than Organization in terms of cross-capability dependency pressure.

## Recommended Next Capability

Organization

## Prioritization Rationale

1. Organization has the highest dependency centrality among the remaining non-locked capabilities.
2. It is already review-complete, so the remaining work is mainly final lock governance rather than functional implementation.
3. Unlocking Organization first reduces the chance of rework in downstream capabilities that depend on organization identity and governance boundaries.
4. Asset Core is also review-complete and should follow immediately after Organization.

## Baseline Constraint

No new implementation work is proposed here. This portfolio only records the recommended order for the remaining non-LOCKED roadmap capabilities.
