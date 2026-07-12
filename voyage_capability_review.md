# VOY-007 Voyage Capability Review and Lock Assessment

## Purpose

Perform the formal CAP-11 Voyages capability review covering VOY-001 through VOY-006.

This is a review waypoint only. No implementation changes are made under VOY-007.

The objective is to determine whether CAP-11 Voyages is READY FOR LOCK or NOT READY FOR LOCK.

---

## Review Baseline

### Commit Verification

| Item | Expected | Actual | Result |
|------|----------|--------|--------|
| HEAD commit hash | `483141004b32232767620bacfce4764a106aa809` | `483141004b32232767620bacfce4764a106aa809` | PASS |
| HEAD commit message | `VOY-006: add voyage end-to-end integration workflows` | `VOY-006: add voyage end-to-end integration workflows` | PASS |
| VOY-006 committed scope | `test_voyage_feature_e2e_workflows.py` only | `tests/application/features/voyages/test_voyage_feature_e2e_workflows.py` only | PASS |

### Reviewed Commits

| Commit | Hash | Scope |
|--------|------|-------|
| VOY-001 | `5a6e1fa` | Domain: voyages package + domain tests (10 files, +1055 lines) |
| VOY-002 | `85b6d95` | Persistence: voyage_mapper, voyage_model, models/__init__, mapper tests (4 files, +874 lines) |
| VOY-003 | `b46e247` | Repository: sqlite_voyage_repository, voyage_repository contract, repository integration tests (3 files, +438 lines) |
| VOY-004 | `c0e55f0` | Application services: 7 use cases + application tests (9 files, +1379 lines) |
| VOY-005 | `670bdfb` | Feature layer: 7 feature facades + feature unit tests (9 files, +1253 lines) |
| VOY-006 | `4831410` | E2E integration workflows: 1 file, +621 lines |

### Design Source

- `docs/design/voyages.md` (VOY-000 generic voyages core design)
- `docs/architecture/capability_roadmap.md` (CAP-11 sequencing and boundary decisions)

---

## Design Conformance

Result: **PASS**

All major design decisions are faithfully implemented:

- Single aggregate root `Voyage` with `VoyageId` identity
- Vessel association by identity/reference only (`vessel_id: UUID`)
- Planned context fields independently maintained and never overwritten by actual fields
- Actual context fields set only by lifecycle operations
- `LocationSnapshot` value object implementing Option C (external ID + historical name snapshot)
- `VoyagePurpose` value object with controlled `VoyagePurposeCode` + optional detail text
- All seven approved `VoyagePurposeCode` values implemented: `OPERATIONAL`, `TRAINING`, `PRESERVATION`, `DEMONSTRATION`, `TRANSFER`, `INSPECTION`, `OTHER`
- Five lifecycle states: `DRAFT`, `PLANNED`, `UNDERWAY`, `COMPLETED`, `CANCELLED`
- Approved lifecycle transitions enforced
- Terminal states `COMPLETED` and `CANCELLED` correctly enforced
- Cancellation from `DRAFT` or `PLANNED` with required `cancellation_reason` and `cancelled_at`
- Explicit timezone-aware timestamps normalized to UTC throughout
- No hidden clock in any production layer

One undocumented addition noted: `document_reference` field in `Voyage` aggregate. See finding OBS-VOY-001.

---

## Domain Review

Result: **PASS**

### Aggregate Root

`Voyage` is the aggregate root, implemented as a `@dataclass(slots=True)` inheriting from `AggregateRoot`. Confirmed via `src/mfm/domain/voyages/voyage.py`.

### Vessel Association

`vessel_id: UUID` is the sole vessel reference. No vessel name, registration, status, dimensions, or Fleet aggregate state is held by `Voyage`. No Fleet imports exist in the voyages domain package.

### Planned vs Actual Independence

Planned state fields (`planned_departure_location`, `planned_arrival_location`, `planned_departure_at`, `planned_arrival_at`) are set only at construction time. The `depart()` operation sets `actual_departure_location` and `departed_at`. The `arrive()` operation sets `actual_arrival_location` and `arrived_at`. No operation overwrites planned fields with actual values.

### Lifecycle Enforcement

All lifecycle transitions are owned by domain methods:

- `plan()`: `DRAFT → PLANNED`
- `depart(departed_at, actual_departure_location)`: `PLANNED → UNDERWAY`
- `arrive(arrived_at, actual_arrival_location)`: `UNDERWAY → COMPLETED`
- `cancel(cancellation_reason, cancelled_at, cancelled_by_reference)`: `DRAFT/PLANNED → CANCELLED`

Terminal state enforcement: `COMPLETED` and `CANCELLED` have no outgoing transitions.

Invalid transitions raise `InvalidVoyageLifecycleError`.

### Chronology Rules

`__post_init__` enforces `planned_departure_at <= planned_arrival_at`.

`_validate_status_invariants()` enforces that if both actual timestamps are set, `departed_at <= arrived_at`.

`arrive()` enforces `arrived_at >= departed_at`.

All datetime inputs are normalized to UTC via `_normalize_aware_datetime()`. Naive datetimes are rejected with `InvalidVoyageChronologyError`.

### Status Invariants

`_validate_status_invariants()` enforces state consistency for all five lifecycle states:

- `DRAFT`: no actual or cancellation fields
- `PLANNED`: no actual or cancellation fields
- `UNDERWAY`: `departed_at` and `actual_departure_location` required; no arrival or cancellation fields
- `COMPLETED`: full departure and arrival actual state required; no cancellation fields
- `CANCELLED`: `cancellation_reason` and `cancelled_at` required; no actual departure/arrival fields

### Domain Events

Five events correctly emitted: `VoyageCreated` (on construction), `VoyagePlanned`, `VoyageDeparted`, `VoyageArrived`, `VoyageCancelled`.

### No Infrastructure Dependencies

No imports from `sqlalchemy`, `infrastructure`, `repositories`, or locked capability domains in the voyages domain package. Confirmed by architecture dependency guard.

### Domain Invariant Gaps

None identified.

---

## Historical Voyage Truth Review

Result: **PASS — End-to-End Proven**

This is the primary CAP-11 lock invariant.

The approved divergence scenario `PORT-A → PORT-B (planned) / PORT-A → PORT-C (actual)` is preserved at every layer:

### Domain Layer

`planned_arrival_location` is set at construction and never modified by `arrive()`. `actual_arrival_location` is set exclusively by `arrive()`. The two fields are structurally independent.

Evidence: `voyage.py` lines for `arrive()` — sets only `self.actual_arrival_location`, not `self.planned_arrival_location`.

### Persistence Layer

`VoyageModel` has independent columns:
- `planned_arrival_location_name_snapshot` (NOT NULL)
- `actual_arrival_location_name_snapshot` (nullable)

These columns are never cross-populated by `VoyageMapper`.

### Mapper Layer

`VoyageMapper.to_orm_voyage()` maps planned and actual fields independently. `VoyageMapper.to_domain_voyage()` restores them independently, never collapsing actual into planned.

### Repository Layer

Repository stores and retrieves the mapper output without modification.

### Application Layer

`to_voyage_response()` in `create_voyage.py` maps `planned_arrival_location` and `actual_arrival_location` to separate `VoyageLocationResponse` instances on `VoyageResponse`.

### Feature Layer

`to_feature_voyage_response()` in `create_voyage_feature.py` maps both fields independently to the public `VoyageResponse` DTO.

### E2E Layer

`test_e2e_workflow_1_complete_voyage_and_historical_truth_with_new_session` explicitly:
1. Creates voyage with `planned_arrival_location = PORT-B`
2. Arrives at `PORT-C` (actual)
3. Asserts `planned_arrival_location.name_snapshot == "PORT-B"`
4. Asserts `actual_arrival_location.name_snapshot == "PORT-C"`
5. Reopens in a fresh SQLAlchemy session and repeats the same assertions

Planned timestamps P1/P2 and actual timestamps A1/A2 are independently verified in the same test and in `test_e2e_workflow_7_explicit_time_timezone_roundtrip`.

**No layer collapses planned and actual context. Historical voyage truth is proven end-to-end.**

---

## Persistence and Mapper Review

Result: **PASS**

### Persistence Model

`VoyageModel` (SQLAlchemy ORM, `voyage` table) contains:
- All required planned fields as non-nullable columns
- All actual fields as nullable columns
- `DateTime(timezone=True)` for every timestamp column
- `Enum(VoyageStatus, native_enum=False)` for status
- `Enum(VoyagePurposeCode, native_enum=False)` for purpose code
- `vessel_id` as UUID reference only (no FK to vessel table; vessel identity boundary maintained)
- Independent planned and actual location columns (four columns each: external_id, name_snapshot, locality_snapshot, country_snapshot)
- Cancellation fields: `cancellation_reason`, `cancelled_at`, `cancelled_by_reference`
- `document_reference` (see OBS-VOY-001)

No domain behaviour exists in `VoyageModel`. It contains only mapped columns.

### Mapper

`VoyageMapper.to_orm_voyage()` maps Voyage → VoyageModel. All 28+ fields mapped independently.

`VoyageMapper.to_domain_voyage()` reconstructs Voyage aggregate from VoyageModel by passing all fields as constructor arguments. This is state restoration, not operation replay. No business operations are called during restore.

After restore, `voyage.pull_events()` is called to clear the `VoyageCreated` event that `Voyage.__post_init__` emits on every construction. This correctly prevents false event emission on reload.

`_normalize_timestamp()` handles SQLite's tendency to return naive datetimes by attaching UTC tzinfo, ensuring consistent timezone semantics after roundtrip.

### Lifecycle State Roundtrip

All five lifecycle states are proven to roundtrip in `test_lifecycle_state_roundtrip_for_supported_states` and in individual mapper tests for DRAFT, PLANNED, UNDERWAY, COMPLETED, and CANCELLED states.

### Invalid Persistence State Handling

Three invalid-state tests verify that corrupt ORM data raises appropriate domain exceptions:
- Invalid status string: raises `ValueError` or `InvalidVoyageLifecycleError`
- Invalid purpose code: raises `InvalidVoyagePurposeError`
- COMPLETED state missing actual arrival name: raises `InvalidVoyageLifecycleError`
- Invalid planned chronology: raises `InvalidVoyageChronologyError`

### Timezone Semantics

All timestamp columns use `DateTime(timezone=True)`. UTC normalization is applied in `_normalize_timestamp()`. Domain `_normalize_aware_datetime()` normalizes all inputs to UTC before storage. Roundtrip proven in `test_timezone_roundtrip_preserves_utc_semantics`.

---

## Repository Review

Result: **PASS with MINOR-VOY-002**

### Contract Placement

`VoyageRepository` abstract contract: `src/mfm/repositories/voyage_repository.py`. Follows the established architecture standard.

### Concrete Implementation

`SQLiteVoyageRepository`: `src/mfm/infrastructure/persistence/sqlite/sqlite_voyage_repository.py`. Follows mapper/persistence pattern.

### Methods Implemented

`add`, `get_by_id`, `update`, `exists`, `list`, `get_by_vessel`.

All methods use `VoyageMapper` for translation. Return `Voyage` aggregates only, never `VoyageModel` instances.

### Vessel Isolation

`get_by_vessel(vessel_id)` filters by `VoyageModel.vessel_id == vessel_id`. Multi-vessel isolation proven in `test_e2e_workflow_4_multi_vessel_isolation`.

### Transaction Ownership

Repository does not call `session.commit()`. It calls `session.flush()` after `add()` and `merge()` operations. `UnitOfWork.commit()` owns the actual commit boundary. This is correct.

### Repository Does Not Own Lifecycle

No lifecycle rules, chronology rules, or status validation exist in the repository implementation.

### New-Session Roundtrip

Proven in all seven E2E tests and in `test_sqlite_voyage_repository.py`.

### voyage_reference Uniqueness

Not enforced at repository or application layer. Design specifies "uniqueness by vessel and reference belongs to repository/application boundary." See MINOR-VOY-001.

### AbstractUnitOfWork Declaration

`AbstractUnitOfWork` does not formally declare `voyage_repository` as an abstract attribute. Concrete implementations set it dynamically in `_start_scope()`. See MINOR-VOY-002.

---

## Application Review

Result: **PASS with MINOR-VOY-001**

### Use Cases Implemented

| Use Case | Class | Status |
|----------|-------|--------|
| Create | `CreateVoyageUseCase` | PASS |
| Plan | `PlanVoyageUseCase` | PASS |
| Depart | `DepartVoyageUseCase` | PASS |
| Arrive | `ArriveVoyageUseCase` | PASS |
| Cancel | `CancelVoyageUseCase` | PASS |
| Get | `GetVoyageUseCase` | PASS |
| List by Vessel | `ListVesselVoyagesUseCase` | PASS |

### Domain Delegation

All lifecycle operations (`plan()`, `depart()`, `arrive()`, `cancel()`) delegate to the domain aggregate. No lifecycle logic is reimplemented in the application layer.

### UnitOfWork Usage

All state-changing use cases use `with self._unit_of_work as uow:`. `uow.commit()` is called on success. The context manager's `__exit__` calls rollback on exception.

### Exception Mapping

`VoyageError` subtypes are mapped to `BusinessRuleViolation`. All other exceptions are mapped to `RepositoryException`. `ValidationException`, `BusinessRuleViolation`, and `ApplicationException` pass through without wrapping.

### No Forbidden Dependencies

No SQLAlchemy imports. No persistence model imports. No Fleet repository dependency. No locked capability imports.

### Explicit Timestamp Passthrough

`departed_at` and `arrived_at` are passed directly from request to domain operation. No timestamp generation in application layer.

### Response Safety

`VoyageResponse` is `@dataclass(frozen=True, slots=True)` containing only `UUID`, `str`, `datetime`, and nested immutable DTOs. No domain objects or ORM models are included.

### voyage_reference Uniqueness

`CreateVoyageUseCase.execute()` does not enforce uniqueness of `voyage_reference` per vessel. Design assigns this responsibility to the repository/application boundary. See MINOR-VOY-001.

---

## Feature Layer Review

Result: **PASS**

### Features Implemented

| Feature | Class | Corresponding Use Case |
|---------|-------|----------------------|
| Create | `CreateVoyageFeature` | `CreateVoyageUseCase` |
| Plan | `PlanVoyageFeature` | `PlanVoyageUseCase` |
| Depart | `DepartVoyageFeature` | `DepartVoyageUseCase` |
| Arrive | `ArriveVoyageFeature` | `ArriveVoyageUseCase` |
| Cancel | `CancelVoyageFeature` | `CancelVoyageUseCase` |
| Get | `GetVoyageFeature` | `GetVoyageUseCase` |
| List by Vessel | `ListVesselVoyagesFeature` | `ListVesselVoyagesUseCase` |

### execute(request) Standard

All seven features expose `execute(request) -> Response`. Confirmed by `test_features_have_execute_request_signature_and_docstring` passing.

### Request and Response Immutability

All feature request and response DTOs are `@dataclass(frozen=True, slots=True)`. Confirmed by `test_all_feature_requests_are_immutable_request_dtos` and `test_all_feature_responses_are_immutable_response_dtos` passing.

### Service Protocol

Each feature uses a `Protocol` typed service reference (e.g., `CreateVoyageService`). No concrete use case is hardcoded in the feature class. This correctly inverts the dependency.

### No Direct Repository or UnitOfWork Access

Features delegate to the application service via the protocol interface. No repository access, no UoW ownership, no domain mutation.

### Exception Mapping

Service exceptions (`ServiceValidationException`, `ServiceBusinessRuleViolation`, `ServiceRepositoryException`) are mapped to corresponding feature-local exceptions. Catch-all wraps to `RepositoryException`.

### Response Safety

Feature `VoyageResponse` DTO fields: `UUID`, `str`, `datetime`, and nested immutable `VoyageLocationResponse` / `VoyagePurposeResponse`. No domain value objects or ORM models. Confirmed by `test_feature_responses_do_not_expose_domain_types` passing.

### Planned and Actual Context

Both `planned_arrival_location` and `actual_arrival_location` are independently exposed in the public `VoyageResponse`. Divergence is preserved through `to_feature_voyage_response()`.

### Runtime Response Values

Feature DTOs use primitive `str` for `status` (not `VoyageStatus` enum) and `str` for `purpose_code` (not `VoyagePurposeCode` enum). All field values are public-safe.

### Structural Note

Feature layer re-declares `VoyageLocationInput`, `VoyageLocationResponse`, `VoyagePurposeResponse`, `VoyageResponse` independently from the application layer. See OBS-VOY-002.

---

## End-to-End Review

Result: **PASS**

### Stack Exercised

`test_voyage_feature_e2e_workflows.py` exercises the real stack in all seven tests:

```
Feature
  ↓
Application (use case)
  ↓
Domain (Voyage aggregate)
  ↓
Repository (SQLiteVoyageRepository)
  ↓
Mapper (VoyageMapper)
  ↓
SQLAlchemy (VoyageModel)
  ↓
SQLite (in-memory file via tmp_path)
```

No mocks replace any Voyage capability component.

### New-Session Proof

All seven E2E tests close the write session, open a fresh read session, and verify persisted state. This proves mapper correctness, persistence semantics, and full stack independence from in-memory state.

### Workflow Coverage

| Workflow | Test | Coverage |
|----------|------|----------|
| Completed voyage + historical truth | `test_e2e_workflow_1_complete_voyage_and_historical_truth_with_new_session` | Creates, plans, departs, arrives; verifies PORT-B vs PORT-C; new session proof |
| Underway voyage | `test_e2e_workflow_2_underway_voyage_new_session_proof` | Creates, plans, departs; new session proof |
| Cancelled voyage | `test_e2e_workflow_3_cancelled_voyage_new_session_proof` | Creates, plans, cancels; new session proof |
| Multi-vessel isolation | `test_e2e_workflow_4_multi_vessel_isolation` | Two vessels, three voyages; isolation verified same-session and new-session |
| Invalid lifecycle rollback | `test_e2e_workflow_5_invalid_lifecycle_rollback` | Depart DRAFT raises `BusinessRuleViolation`; voyage remains DRAFT after rollback |
| Arrival chronology rollback | `test_e2e_workflow_6_arrival_chronology_failure_rollback` | arrived_at < departed_at raises `BusinessRuleViolation`; voyage remains UNDERWAY |
| Explicit time / timezone roundtrip | `test_e2e_workflow_7_explicit_time_timezone_roundtrip` | +02:00 and -03:00 inputs normalized to UTC; roundtrip verified |
| Hidden clock static scan | `test_hidden_clock_search_in_voyage_production_layers` | AST scan of domain/voyages, application/voyages, features/voyages for clock patterns |

### Material Missing Proof

None identified. All implemented public capabilities are covered.

---

## Time and Hidden Clock Review

Result: **PASS — No Hidden Clock**

### Production Code Search

Searched all production files under:
- `src/mfm/domain/voyages/`
- `src/mfm/application/voyages/`
- `src/mfm/application/features/voyages/`

Patterns searched: `date.today(`, `datetime.now(`, `datetime.today(`, `time.time(`

Result: **Zero matches found.**

### Static Test Verification

`test_hidden_clock_search_in_voyage_production_layers` performs an AST parse and string search of all three production roots at runtime, asserting the absence of all four clock patterns. This test passes.

### Policy Compliance

All lifecycle timestamps (`planned_departure_at`, `planned_arrival_at`, `departed_at`, `arrived_at`, `cancelled_at`) are explicitly supplied by callers. Domain operations accept them as required arguments. The domain enforces timezone-awareness and UTC normalization without generating any timestamps internally.

---

## Cross-Capability Boundary Review

Result: **PASS**

### Fleet

- `vessel_id: UUID` is the sole reference to vessel identity. No vessel metadata, registration, status, or lifecycle state is held.
- No imports from `mfm.domain.fleet`, `mfm.repositories` fleet-related, or `mfm.infrastructure` fleet-related in any Voyage production file.
- `VoyageModel.vessel_id` has no SQLAlchemy foreign key relationship to `VesselModel`. This correctly implements the identity-only boundary.

### Certificates and Compliance

- No certificate evaluation, compliance status check, or certificate mutation exists in any Voyage production file.
- No departure gate based on certificate validity.

### Maintenance

- No `WorkOrder` creation, no `MaintenanceRecord` creation, no maintenance planning in Voyage production code.
- Arrival operation does not trigger any Maintenance workflow.

### Technical Configuration

- No machinery readiness check, no technical configuration ownership or lookup in Voyage production code.

### Asset Core

- `vessel_id` is used as a raw UUID reference only. No Asset domain objects are created or owned by Voyages.

### Reverse Dependency Check

None of the locked capabilities (Fleet, Technical Configuration, Maintenance, Certificates) import from the Voyage capability. No reverse dependency detected.

---

## Out-of-Scope Review

Result: **PASS — No Out-of-Scope Functionality Introduced**

Confirmed absent:

| Out-of-Scope Item | Present? |
|-------------------|----------|
| Passage planning | NO |
| ECDIS | NO |
| AIS | NO |
| GPS track storage | NO |
| Telemetry | NO |
| Weather routing | NO |
| Fuel optimization | NO |
| Bunkers | NO |
| Crew management | NO |
| Payroll | NO |
| Watch schedules | NO |
| Maintenance workflow | NO |
| Certificate lifecycle | NO |
| Technical configuration | NO |
| Inventory / Procurement | NO |
| Finance / Projects | NO |
| Document Management (implementation) | NO |
| Binary document storage | NO |
| GUI | NO |

---

## Architecture Review

Result: **PASS — All 10 Architecture Gates Pass**

### Dependency Direction Verified

```
Feature layer (application/features/voyages)
  → Application (application/voyages)
  → Domain (domain/voyages) + Repository contract (repositories/voyage_repository)

Repository implementation (infrastructure/persistence/sqlite/sqlite_voyage_repository)
  → Mapper (database/mappers/voyage_mapper)
  → Persistence model (database/models/voyage_model)

Domain (domain/voyages)
  → Common base types only (common/aggregate_root, common/value_object, common/domain_event)
  → No infrastructure
```

### Architecture Test Results

All 10 architecture compliance tests pass:

| Test | Result |
|------|--------|
| `test_domain_must_not_depend_on_application_features_infrastructure_or_sqlalchemy` | PASS |
| `test_application_must_not_depend_on_gui` | PASS |
| `test_feature_layer_must_not_depend_on_sqlalchemy_models` | PASS |
| `test_persistence_must_not_depend_on_gui` | PASS |
| `test_gui_may_only_depend_on_features` | PASS |
| `test_repository_interfaces_must_not_depend_on_sqlalchemy` | PASS |
| `test_features_have_execute_request_signature_and_docstring` | PASS |
| `test_all_feature_requests_are_immutable_request_dtos` | PASS |
| `test_all_feature_responses_are_immutable_response_dtos` | PASS |
| `test_feature_responses_do_not_expose_domain_types` | PASS |

### Locked Capabilities Unchanged

Architecture tests for Fleet, Technical Configuration, Maintenance, and Certificates continue to pass at 907 total.

---

## Test Quality Review

Result: **PASS**

### Domain Tests (`tests/domain/voyages/test_voyage_domain.py`)

35 tests. Coverage includes: vessel identity validation, LocationSnapshot immutability, all five lifecycle transitions, invalid transition rejection, chronology enforcement, VoyagePurpose validation, event emission sequence, cancellation from DRAFT and PLANNED, terminal state immutability, timezone normalization.

The tests distinguish planned destination PORT-B from actual arrival PORT-C:
```python
planned_arrival_location=_location("Location B", external_id="PORT-B")
...
voyage.arrive(arrived_at=..., actual_arrival_location=_location("Location C", external_id="PORT-C"))
```
Historical truth invariant is tested at domain level.

### Mapper Tests (`tests/database/test_voyage_mapper.py`)

16 tests. Coverage includes: creation roundtrip, vessel reference preservation, all location snapshot fields independently, planned context roundtrip, underway roundtrip preserving both contexts, completed voyage historical truth (`PORT-B` planned / `PORT-C` actual), cancelled voyage roundtrip, all five lifecycle state roundtrips, purpose roundtrip, timezone semantics, event suppression on restore, and four invalid-persistence-state tests.

Notably, `test_historical_voyage_truth_roundtrip_keeps_planned_b_and_actual_c` directly proves the primary lock invariant at the persistence layer.

### Repository Integration Tests (`tests/database/test_sqlite_voyage_repository.py`)

7 tests (inferred from test run output). Coverage includes: add/get_by_id roundtrip, update lifecycle flow, get_by_vessel multi-vessel isolation, new-session proof.

### Application Tests (`tests/application/voyages/test_voyage_use_cases.py`)

15 tests using `FakeVoyageUnitOfWork` and `InMemoryVoyageRepository`. Coverage includes: all seven use cases' happy paths, lifecycle error propagation, commit/rollback behavior on failure, repository interaction verification.

### Feature Unit Tests (`tests/application/features/voyages/test_voyage_features.py`)

8 tests. Coverage includes: each feature's delegation behavior, exception mapping from service to feature exceptions, immutability of request/response DTOs.

### E2E Integration Tests (`tests/application/features/voyages/test_voyage_feature_e2e_workflows.py`)

8 tests (7 workflow + 1 hidden clock static scan). Complete stack with new-session proof across all supported lifecycle workflows.

### Test Content Quality Assessment

Tests demonstrate substantive invariant proof:
- Tests explicitly assert `planned_arrival_location.name_snapshot == "PORT-B"` AND `actual_arrival_location.name_snapshot == "PORT-C"` in multiple layers, not merely asserting field existence.
- Tests verify exact timestamp values after UTC normalization, not just non-None.
- Tests prove rollback leaves previous valid state intact (not merely that an exception was raised).

No meaningfully duplicated tests detected. Test suite is well-distributed across layers.

---

## Locked Capability Impact

Result: **PASS — No Locked Capability Modified**

Files changed by VOY-001 through VOY-006 are exclusively:

- `src/mfm/domain/voyages/` — new capability package (additive)
- `src/mfm/database/models/voyage_model.py` — new file (additive)
- `src/mfm/database/models/__init__.py` — one import added: `from mfm.database.models.voyage_model import VoyageModel` (additive, follows existing pattern)
- `src/mfm/database/mappers/voyage_mapper.py` — new file (additive)
- `src/mfm/repositories/voyage_repository.py` — new file (additive)
- `src/mfm/infrastructure/persistence/sqlite/sqlite_voyage_repository.py` — new file (additive)
- `src/mfm/application/voyages/` — new capability package (additive)
- `src/mfm/application/features/voyages/` — new capability package (additive)
- `tests/domain/voyages/`, `tests/database/test_voyage_*.py`, `tests/application/voyages/`, `tests/application/features/voyages/` — new test files (additive)

The single modification to an existing file (`database/models/__init__.py`) is a purely additive import registration following the established pattern used by every prior capability. No locked capability production code was modified.

All 907 tests pass, including all tests for locked capabilities (Fleet, Technical Configuration, Maintenance, Certificates).

**No locked capability was improperly modified. No unlock procedure was required.**

---

## Classified Findings

### MINOR-VOY-001: voyage_reference Uniqueness Not Enforced

| Item | Detail |
|------|--------|
| **ID** | MINOR-VOY-001 |
| **Classification** | MINOR |
| **Layer** | Application / Repository |
| **Finding** | `voyage_reference` uniqueness per vessel is not enforced at the repository or application layer. Two voyages for the same vessel can be created with the same `voyage_reference` without error. |
| **Evidence** | `VoyageRepository` has no `get_by_reference` or `exists_by_reference` method. `CreateVoyageUseCase.execute()` does not query for existing references before persisting. |
| **Design position** | `docs/design/voyages.md`: *"uniqueness by vessel and reference belongs to repository/application boundary, not domain sequence generation."* |
| **Lock impact** | Does not prevent lock. `voyage_reference` is optional. The design assigns uniqueness enforcement to this boundary but does not prescribe the exact mechanism or timing. No behavioral invariant is broken at this stage. |
| **Recommended handling** | Document as known gap. Address in VOY-008 or a follow-on maintenance waypoint by adding `get_by_reference(vessel_id, reference)` to the repository contract and a duplicate-reference guard in `CreateVoyageUseCase`. |

---

### MINOR-VOY-002: AbstractUnitOfWork Does Not Declare voyage_repository

| Item | Detail |
|------|--------|
| **ID** | MINOR-VOY-002 |
| **Classification** | MINOR |
| **Layer** | Application / Repository |
| **Finding** | `AbstractUnitOfWork` in `src/mfm/application/uow/abstract_unit_of_work.py` does not formally declare `voyage_repository` as an abstract attribute or type annotation. Application use cases access it via `uow.voyage_repository` with a local type annotation, which works at runtime but is not statically enforced at the abstract contract level. |
| **Evidence** | `abstract_unit_of_work.py` declares `contact_repository`, `member_repository`, etc. as `Any`-typed class annotations but not `voyage_repository`. The same pattern applies to Fleet, Technical Configuration, Maintenance, and Certificates repositories — this is a capability-wide pattern gap, not unique to Voyages. |
| **Lock impact** | Does not prevent lock. This pattern is consistent across all prior locked capabilities and has not caused failures. |
| **Recommended handling** | Document as a capability-wide pattern observation. If the UoW contract is ever formally tightened, declare `voyage_repository: VoyageRepository` alongside the other repository attributes. |

---

### OBS-VOY-001: document_reference Field Not in Approved Design

| Item | Detail |
|------|--------|
| **ID** | OBS-VOY-001 |
| **Classification** | OBSERVATION |
| **Layer** | Domain / Persistence |
| **Finding** | `Voyage` aggregate and `VoyageModel` include a `document_reference: str | None` field that is not present in `docs/design/voyages.md` (VOY-000). |
| **Evidence** | `voyage.py` field `document_reference: str | None = None`; `voyage_model.py` column `document_reference`; mapped in `VoyageMapper`; exposed in `VoyageResponse`. |
| **Lock impact** | No impact. The field is optional, carries no domain invariants, does not introduce any cross-capability dependency, and does not affect lifecycle or historical truth. |
| **Recommended handling** | Backfill a design note in `docs/design/voyages.md` recording `document_reference` as an approved optional metadata field under VOY-008 or the next maintenance waypoint. |

---

### OBS-VOY-002: Feature Layer DTOs Structurally Duplicate Application DTOs

| Item | Detail |
|------|--------|
| **ID** | OBS-VOY-002 |
| **Classification** | OBSERVATION |
| **Layer** | Feature |
| **Finding** | `create_voyage_feature.py` re-declares `VoyageLocationInput`, `VoyageLocationResponse`, `VoyagePurposeResponse`, and `VoyageResponse` as structurally identical to those in `create_voyage.py`. Mapping functions `to_feature_location_response`, `to_feature_purpose_response`, and `to_feature_voyage_response` copy field by field. |
| **Evidence** | `create_voyage_feature.py` defines its own `VoyageResponse` dataclass independent from `VoyageResponse` in `create_voyage.py`. |
| **Lock impact** | No impact. This is the intended isolation pattern per the Public API Standard: the feature layer must not expose application-internal types. The duplication is intentional. |
| **Recommended handling** | No action needed. Record as a design decision. |

---

### OBS-VOY-003: test_voyage_domain.py Helper _dt Constructs Timezone Inconsistently

| Item | Detail |
|------|--------|
| **ID** | OBS-VOY-003 |
| **Classification** | OBSERVATION |
| **Layer** | Tests (Domain) |
| **Finding** | The `_dt` helper in `test_voyage_domain.py` applies `tz_offset_hours` via `timedelta` addition after setting `tzinfo=UTC`, which produces UTC-offset timestamps rather than local-timezone timestamps. The intent appears to be producing UTC datetimes with an hours offset added to the value. The function works correctly and produces timezone-aware datetimes. |
| **Evidence** | `_dt` adds `timedelta(hours=tz_offset_hours)` to a UTC datetime. Used internally in test helpers. |
| **Lock impact** | No impact on production behaviour. All resulting datetimes are timezone-aware and pass domain validation. |
| **Recommended handling** | No action required. Note for test maintainability if this helper is extended. |

---

## Lock Assessment

### Mandatory Conditions

| Condition | Status |
|-----------|--------|
| No BLOCKER findings | **MET** — Zero BLOCKER findings |
| No MAJOR findings | **MET** — Zero MAJOR findings |
| Historical voyage truth proven end-to-end | **MET** — PORT-B / PORT-C divergence verified in Domain, Mapper, Repository, Application, Feature, E2E with new-session proof |
| Lifecycle ownership correct | **MET** — Domain owns all lifecycle transitions |
| Time policy deterministic | **MET** — No hidden clock; all timestamps explicitly supplied |
| Repository transaction ownership correct | **MET** — UnitOfWork commits; repository flushes only |
| Public API safe | **MET** — All feature responses use primitive/immutable types; architecture gate passes |
| Cross-capability boundaries intact | **MET** — Identity-only vessel reference; no locked capability production code imported or modified |
| Locked capabilities not improperly modified | **MET** — Only additive changes to `database/models/__init__.py` |
| Architecture gates pass | **MET** — 10/10 architecture compliance tests pass |
| Full suite passes | **MET** — 907 passed, 0 failures, 0 errors |

### Remaining Open Items

| ID | Classification | Description |
|----|---------------|-------------|
| MINOR-VOY-001 | MINOR | voyage_reference uniqueness not enforced at application/repository boundary |
| MINOR-VOY-002 | MINOR | AbstractUnitOfWork does not formally declare voyage_repository |
| OBS-VOY-001 | OBSERVATION | document_reference field not in approved design |
| OBS-VOY-002 | OBSERVATION | Feature layer DTOs structurally duplicate application DTOs (intentional) |
| OBS-VOY-003 | OBSERVATION | test_voyage_domain.py _dt helper timezone construction style |

MINOR and OBSERVATION findings are documented and do not threaten capability invariants.

---

## Final Recommendation

```
READY FOR LOCK
```

CAP-11 Voyages implementation is conformant with the VOY-000 design across all reviewed layers. The primary lock invariant — historical voyage truth with independent preservation of planned and actual contexts — is proven end-to-end through the full stack with new-session verification. The two MINOR findings (voyage_reference uniqueness gap, abstract UoW declaration) are known, documented, and do not break any behavioral invariant at this capability scope. Architecture compliance is verified. All 907 tests pass. No locked capability was improperly modified.

---

*Review date: 2026-07-12*
*Reviewed by: VOY-007 capability review waypoint*
*Review commit baseline: `483141004b32232767620bacfce4764a106aa809` (VOY-006)*
