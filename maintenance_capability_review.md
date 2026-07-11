# MAINT-007 Maintenance Capability Review and Lock Assessment

## Executive Summary
MAINT-006 pre-review gates are verified green and correctly scoped. CAP-09 Maintenance implementation is broadly aligned with MAINT-000 design across Domain, Persistence, Repositories, Application, Feature API, and E2E workflows. 

Review conclusion: **READY FOR LOCK**.

MAINT-007A resolved the lock-blocking findings with minimal CAP-09-internal corrections and regression tests. Historical permanence is now protected at repository level, and overdue behavior is now directly covered by domain tests.

## Scope Reviewed
- Design source:
  - docs/design/maintenance.md
- Implementation chain reviewed:
  - MAINT-001 domain
  - MAINT-002 persistence + mapper
  - MAINT-003 repositories
  - MAINT-004 application services
  - MAINT-005 feature API
  - MAINT-006 end-to-end workflows
- Architecture tests reviewed:
  - tests/architecture/test_dependency_guard.py
  - tests/architecture/test_feature_api_architecture.py
- Key validation tests reviewed:
  - tests/domain/maintenance/test_maintenance_domain.py
  - tests/database/test_maintenance_mapper.py
  - tests/database/test_sqlite_maintenance_repositories.py
  - tests/application/maintenance/test_maintenance_use_cases.py
  - tests/integration/test_maintenance_end_to_end.py

## Domain Assessment
Status: PASS (with one downstream persistence blocker).

Verified:
- Aggregate split matches design: MaintenancePlan + WorkOrder.
- MaintenancePlan enforces target consistency and duplicate requirement signature invariants.
- WorkOrder enforces lifecycle and chronology via domain methods.
- MaintenanceTarget is identity/reference only (target_type + UUID target_id).
- Target type validation is enforced in domain and application parsing.
- MaintenanceInterval is immutable and domain-validates due_basis compatibility.
- Due calculation is domain-owned via MaintenancePlan.calculate_due and requirement logic.
- No hidden system clock dependencies observed in domain flow.
- Completion history is created by WorkOrder.complete and mapped to MaintenanceRecord.
- No Technical Configuration lifecycle logic in MAINT domain.
- No Fleet domain logic copied into MAINT domain.

## Aggregate Boundary Assessment
Status: PASS.

- MaintenancePlan owns requirement consistency and due evaluation orchestration.
- WorkOrder owns execution lifecycle transitions and completion record creation.
- Cross-aggregate coordination is in application layer, not merged into one aggregate.
- No separate MaintenanceRecord aggregate root present.

## Maintenance Target Assessment
Status: PASS.

- Identity/reference-only model enforced.
- Stable UUID identity preserved through persistence roundtrip.
- Target queries are by target_type + target_id, no cross-capability object joins.

## Due Calculation Assessment
Status: PASS.

Verified:
- Domain-owned deterministic due logic.
- Explicit as_of_date and running-hours input required by API/domain flow.
- No date.today()/datetime.now() hidden dependency in maintenance flow.
- Calendar and running-hours due paths validated in domain/application/E2E tests.
- No telemetry introduced.

Additional verification:
- Direct overdue behavior coverage added for calendar and running-hours paths.

## Work Order Lifecycle Assessment
Status: PASS.

Verified:
- Valid transitions accepted (PLANNED -> OPEN -> IN_PROGRESS -> COMPLETED).
- Invalid transitions rejected (e.g., start without open, complete without in-progress, cancelled cannot complete).
- Chronology guard enforced (completed_at cannot precede started_at).
- Completed order cannot restart.
- Completion creates MaintenanceRecord from domain lifecycle.
- Application/feature layers orchestrate; they do not mutate status fields directly.

## Maintenance History Assessment
Status: PASS.

Verified by MAINT-006 and lower-layer tests:
- Historical records are created and preserved across plan updates.
- Record A retains A-context and Record B retains B-context after DB roundtrips.
- History retrieval is not reconstructed from current plan fields only.
- Tests validate snapshot content (notes/findings/timestamps), not only IDs.

Explicit review answer:
- Does Maintenance preserve historical truth independently of current plan state?
  - **Yes.** Historical truth is preserved independently of current planning state, including under delete attempts for completed/history-bearing work orders.

## Historical Snapshot Integrity Assessment
Status: PASS.

Evidence:
- MAINT-006 workflow 5 explicitly verifies A/B context separation across reloads.
- Mapper/repository tests verify record fields persist independently from updated plan instructions/interval.

## Persistence and Mapper Assessment
Status: PASS.

Verified:
- SQLAlchemy 2.x typed mappings are used (Mapped/mapped_column/relationship).
- Domain is persistence-independent.
- Mapper separates domain and ORM models.
- MaintenanceTarget, MaintenanceInterval, MaintenancePlan, WorkOrder roundtrip behavior validated.
- Completion timestamps, findings, notes, performer references roundtrip correctly in scope.
- History is persisted as MaintenanceRecord under WorkOrder and not recomputed from plan.
- No Fleet persistence internals required for maintenance persistence.
- No TECH persistence internals required for maintenance persistence.

Correction:
- Repository delete now rejects deletion for completed/history-bearing work orders, preserving immutable maintenance records.

## Repository Assessment
Status: PASS.

Verified:
- Aggregate-root repositories only: MaintenancePlanRepository and WorkOrderRepository.
- No MaintenanceRecordRepository.
- SQLite adapters implement contracts.
- UnitOfWork/session pattern followed.
- Repositories do not own commit lifecycle.
- Mappers used consistently; repositories return domain aggregates.
- No domain due/lifecycle logic embedded in repositories.
- Target querying uses identity/reference only.

Correction detail:
- WorkOrderRepository.delete now blocks destructive deletion for completed/history-bearing work orders.
- Historical records remain preserved under attempted delete.

## Application Assessment
Status: PASS.

Verified:
- Immutable request/response DTOs.
- Contract-based repository access.
- UnitOfWork usage with explicit commit on success.
- Failure rollback behavior covered in tests.
- Domain owns due and lifecycle behavior.
- Application orchestrates and maps exceptions.
- No SQLAlchemy/persistence-model imports in maintenance application services.
- No Fleet/TECH infrastructure imports in maintenance application services.
- Response mapping uses API-safe primitives/DTOs.

## Feature API Assessment
Status: PASS.

Verified:
- Public API execute(request) standard followed.
- Immutable request/response DTOs in feature layer.
- Feature layer depends on application services, not repositories.
- No direct lifecycle mutation/due logic/record construction in features.
- Exception mapping is consistent.
- Public representations are API-safe (target/interval/status/history).
- No domain aggregate/entity/value-object leakage in response DTOs.
- No persistence model leakage.

## End-to-End Assessment
Status: PASS.

MAINT-006 workflows reviewed and pass through real stack:
- Feature -> Application -> Domain -> Repository -> Mapper -> SQLAlchemy -> SQLite -> Reload -> Public API verification.

Verified workflows:
1. Vessel maintenance plan
2. Technical component maintenance
3. Due maintenance calculation
4. WorkOrder completion lifecycle
5. Permanent historical snapshot
6. Propulsion engine maintenance
7. Pitch propeller inspection finding
8. Vessel hull inspection
9. Failure and rollback
10. Capability boundaries

No mocks are used where full integration is feasible.

## Technical Configuration Boundary Assessment
Status: PASS.

Verified:
- MAINT targets TechnicalComponent identity via MaintenanceTarget.
- MAINT plans/executes/records findings/history only.
- No install/remove/replace operations executed by MAINT.
- Pitch-propeller finding workflow records possible replacement required without replace_component execution.

Explicit review answer:
- Can Maintenance evolve without modifying locked Technical Configuration?
  - **Yes, based on current architecture and MAINT-006 evidence.**

## Fleet Boundary Assessment
Status: PASS.

Verified:
- Vessel maintenance targets vessel identity/reference only.
- MAINT does not mutate Vessel state.
- No Fleet infrastructure internals imported by MAINT code.
- Vessel-target workflow does not require TechnicalComponent.

## Performer / Organization Boundary Assessment
Status: PASS.

Verified:
- PerformerReference is identity/reference only in maintenance scope.
- No ownership/import coupling to Member/Volunteer/Organization aggregates/infrastructure.

Assessment:
- Boundary is suitable for future performer validation/integration without changing maintenance domain ownership.

## Finance Boundary Assessment
Status: PASS.

Verified:
- No accounting posting logic in MAINT.
- No Finance domain or infrastructure dependency in MAINT.

Assessment:
- WorkOrder identity can be used by separate future integration without changing maintenance aggregate ownership.

## Architecture Compliance
Status: PASS.

Executed:
- python -m pytest -q tests/architecture/test_dependency_guard.py tests/architecture/test_feature_api_architecture.py

Result:
- 10 passed

## Locked Capability Protection
Status: PASS.

Verified:
- MAINT-006 commit b1ab560ff81abdc92809e6c557b3316c209327f8 is scoped to:
  - tests/integration/test_maintenance_end_to_end.py
- No locked capability production changes detected in MAINT-006 scope:
  - Asset Core unchanged
  - Fleet unchanged
  - Technical Configuration unchanged

## Documentation Assessment
Status: PARTIAL PASS.

Reviewed:
- docs/design/maintenance.md
- CHANGELOG.md
- /memories/repo/notes.md

Assessment:
- Design document aligns with implemented architecture and behavior intent.
- CHANGELOG does not currently include explicit MAINT milestone entries (observation only; not a lock blocker).
- Repo memory has no conflicting maintenance review standard.

No documentation corrections applied in this review.

## Findings

### BLOCKER
1. Historical records can be physically deleted via WorkOrder delete cascade.
- Exact location:
  - src/mfm/database/models/work_order_model.py (records relationship cascade delete-orphan)
  - src/mfm/infrastructure/persistence/sqlite/sqlite_work_order_repository.py (delete)
  - tests/database/test_sqlite_maintenance_repositories.py (delete path validates deletability)
- Violated rule/concern:
  - Permanent maintenance history should not be destructible through normal repository delete semantics.
- Impact:
  - Historical truth can be removed if delete is invoked, undermining immutable/permanent record guarantees.
- Minimal required correction:
  - Prevent deletion of completed WorkOrders (and/or WorkOrders with maintenance_record), or enforce archival-only behavior while preserving records.
  - Add regression test proving history persistence under attempted delete.
- Resolution status:
  - CORRECTED in src/mfm/infrastructure/persistence/sqlite/sqlite_work_order_repository.py
  - Regression test: tests/database/test_sqlite_maintenance_repositories.py::test_work_order_repository_crud_get_by_requirement_and_lifecycle_roundtrip
  - Verification result: PASS

### MAJOR
1. Overdue behavior is implemented but not directly tested.
- Exact location:
  - src/mfm/domain/maintenance/maintenance_requirement.py (is_overdue)
  - tests/domain/maintenance/test_maintenance_domain.py (no direct overdue assertions)
- Concern:
  - Missing direct test coverage for supported overdue path.
- Impact:
  - Potential silent regressions in overdue semantics.
- Minimal required correction:
  - Add focused overdue tests for calendar and running-hours where supported.
- Resolution status:
  - CORRECTED in tests/domain/maintenance/test_maintenance_domain.py
  - Regression tests:
    - tests/domain/maintenance/test_maintenance_domain.py::test_maintenance_calendar_overdue_behaviour
    - tests/domain/maintenance/test_maintenance_domain.py::test_maintenance_running_hours_overdue_behaviour
  - Verification result: PASS

### MINOR
1. Changelog coverage for maintenance milestones is incomplete.
- Exact location:
  - CHANGELOG.md
- Concern:
  - Capability status traceability is weaker than implementation state.
- Impact:
  - Documentation discoverability/traceability only.
- Minimal required correction:
  - Add MAINT milestone entries aligned with actual commits.

### OBSERVATION
1. MAINT-006 E2E coverage is strong and exercises real stack end-to-end with public API verification and boundary checks.

## Risks
- Historical snapshot corruption: low after delete-protection correction and regression validation.
- Plan/history coupling: low in normal flow (A/B snapshot tests validate decoupling).
- Hidden clock dependency: low (explicit date/hour input model).
- WorkOrder lifecycle inconsistency: low (domain guards + tests).
- Cross-capability target leakage: low (identity/reference model).
- TECH ownership leakage: low (no replacement lifecycle execution by MAINT).
- Repository history deletion: low after repository deletion guard correction.
- Public API domain leakage: low (feature architecture and response typing enforce API-safe DTOs).
- Transaction rollback integrity: low (application tests and E2E rollback scenario validate).

## Lock Recommendation
**READY FOR LOCK**

Condition satisfied:
- Lock-blocking blocker and major findings are corrected with passing regression tests.
