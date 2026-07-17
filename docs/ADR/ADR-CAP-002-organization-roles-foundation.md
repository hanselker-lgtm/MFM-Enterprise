# ADR-CAP-002: Organization & Roles Foundation

Date: 2026-07-17
Status: Accepted

## Context

CAP-002 requires an independent Organization & Roles capability while preserving existing DDD layering and avoiding changes to Accounting and Membership behavior.

The codebase already contains legacy organization aggregates (organization, board, committee, role), but CAP-002 requires an explicit foundation package with dedicated lifecycle flow:

- Role
- Assignment
- Committee
- Board
- ElectionPeriod
- Permission
- Responsibility
- repository abstraction
- service, feature API, workflow, reporting API, GUI shell route

## Decision

Implement an independent `organization_roles` capability using existing architecture patterns:

1. Domain
- Added dedicated package `mfm.domain.organization_roles`.
- Added entities/value objects/enums: `Role`, `Assignment`, `Committee`, `Board`, `ElectionPeriod`, `Permission`, `Responsibility`.
- Added aggregate root `OrganizationRolesFoundation` to coordinate role governance state.

2. Repositories
- Added repository contract `OrganizationRolesRepository`.
- Added adapter `SQLiteOrganizationRolesRepository` backed by process-local storage to keep CAP-002 independent from legacy organization persistence.

3. Services and Feature API
- Added `OrganizationRolesService` with request/response DTOs and domain validation mapping.
- Added `ManageOrganizationRolesFeature` with immutable request/response DTOs and standardized exception translation.

4. Workflow
- Added `OrganizationRolesWorkflow` wrapper for workflow-level orchestration.

5. Reporting API
- Added `OrganizationRolesSummaryService` and `OrganizationRolesSummaryFeature`.
- Added `OrganizationRolesSummaryResponse` DTO.

6. GUI Shell
- Added operations route `operations.organization-roles` and optional loader hook `organization_roles_workspace_loader`.

7. Exports
- Wired feature, workflow, and reporting model exports to align with architecture checks.

## Consequences

Positive:
- CAP-002 now has a complete and independent foundation flow from domain through presentation route.
- Existing Membership and Accounting capabilities remain untouched.
- Public feature boundaries stay DTO-safe and architecture-compliant.

Trade-offs:
- Current repository adapter is process-local and should be replaced with dedicated persistence models in a future increment.
- CAP-002 intentionally avoids coupling to legacy organization persistence to keep capability independence explicit.

Out of scope:
- accounting behavior changes
- membership behavior changes
- migration of legacy organization aggregates into CAP-002
