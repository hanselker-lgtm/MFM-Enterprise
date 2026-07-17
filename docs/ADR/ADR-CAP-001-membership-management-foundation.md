# ADR-CAP-001: Membership Management Foundation

Date: 2026-07-17
Status: Accepted

## Context

CAP-001 requires a dedicated Membership Management capability aligned with the existing DDD architecture.
The existing codebase already contained member and membership domain objects, but capability coverage was incomplete for:

- membership aggregate persistence repository
- category-oriented membership classification
- explicit membership management service and feature API boundary
- workflow wrapper for membership operations
- reporting API for membership management metrics
- GUI shell route for membership workspace integration

Constraints:

- no accounting changes
- no project changes
- follow existing architecture conventions (domain -> repositories -> application services/features -> workflow/reporting)

## Decision

Implement the Membership Management Foundation with the following scope:

1. Domain
- Added MembershipCategory enum.
- Extended MembershipType with category and validation.

2. Repositories and Persistence
- Added MembershipRepository contract.
- Added Membership ORM model, mapper, and SQLite repository.
- Wired membership repository into SQLAlchemyUnitOfWork.
- Extended MembershipType persistence mapping with category.

3. Services and Feature API
- Added MembershipManagementService for register/change-status/list membership operations.
- Added ManageMembershipFeature as transport-safe feature API with validation and exception mapping.

4. Workflow
- Added MembershipManagementWorkflow wrapper to execute membership feature operations in workflow style.

5. Reporting API
- Added MembershipSummaryService and MembershipSummaryFeature.
- Added summary DTOs for status/category metrics.

6. GUI Shell
- Added operations.memberships route and optional memberships workspace loader in application shell.

7. Tests
- Added domain, mapper, repository, service, feature, workflow, reporting, and presentation tests for CAP-001 behavior.

## Consequences

Positive:

- Membership capability now has a complete DDD baseline from domain to reporting.
- Membership persistence is no longer session-placeholder based in UnitOfWork.
- Category-based classification enables capability-level management and reporting.

Trade-offs:

- Membership category adds a persistence field that must remain stable across future migrations.
- Workflow remains a thin orchestrator by design; business rules stay in domain/service layers.

Out of scope:

- accounting behavior changes
- project behavior changes
- advanced UI implementation beyond shell route integration
