# Inventory Capability Review (INV-007)

## Purpose
Review CAP-12 Inventory implementation (INV-001 through INV-006) for design conformance, scope control, architecture and boundary integrity, transaction behavior, public API behavior, E2E truth, and lock readiness.

This is a review waypoint only. No implementation changes are introduced by INV-007.

## Baseline And Roadmap Verification
Post-push baseline commit:
- fb2109a96376735359126bd6c0a551476fd4d001

Roadmap source:
- docs/architecture/capability_roadmap.md

Roadmap evidence:
- CAP-12 Inventory (INV) status is PLANNED
- CAP-13 Procurement remains PROVISIONAL

Roadmap result:
- COMPLIANT. No roadmap conflict detected for INV-007 review-only progression.

## Authoritative Sources Reviewed
- docs/design/inventory.md
- docs/architecture/capability_roadmap.md
- src/mfm/domain/inventory/*
- tests/domain/inventory/test_inventory_domain.py
- src/mfm/database/mappers/inventory_mapper.py
- src/mfm/database/models/inventory_item_model.py
- src/mfm/database/models/inventory_stock_position_model.py
- src/mfm/database/models/inventory_stock_movement_model.py
- tests/database/test_inventory_mapper.py
- src/mfm/repositories/inventory_repository.py
- src/mfm/infrastructure/persistence/sqlite/sqlite_inventory_repository.py
- tests/database/test_sqlite_inventory_repository.py
- src/mfm/application/inventory/*
- tests/application/inventory/test_inventory_use_cases.py
- src/mfm/application/features/inventory/*
- tests/application/features/inventory/test_inventory_features.py
- tests/application/features/inventory/test_inventory_feature_e2e_workflows.py
- tests/architecture/test_dependency_guard.py
- tests/architecture/test_feature_api_architecture.py
- maintenance_capability_review.md
- certificate_capability_review.md
- voyage_capability_review.md
- /memories/repo/notes.md

## Review Pattern
Pattern used follows mature capability-review precedent in root review documents with:
- evidence-backed layer-by-layer assessment
- explicit boundary checks
- architecture and test-gate evidence
- final lock recommendation without changing roadmap lock state

## Scope Review
Classification: COMPLIANT

Verified implemented scope aligns with approved Inventory first-scope behavior:
- Inventory item identity and reference
- descriptive state and unit of measure
- location-scoped stock positions
- movement history
- receive/issue/adjust operations
- minimum stock and low-stock query
- active/inactive lifecycle
- create/get/list/low-stock application and feature workflows

Out-of-scope features remain unimplemented as expected:
- procurement workflows
- supplier ownership
- purchase orders/reordering
- lot/batch/serial tracking
- financial valuation ownership

## Domain Review
Classification: COMPLIANT

Evidence highlights:
- Aggregate root and invariants are domain-owned in src/mfm/domain/inventory/inventory_item.py
- Quantity semantics enforce Decimal-only authority and positive/non-negative constraints via UnitOfMeasure and StockPosition.
- Receive/issue/adjust lifecycle and insufficient-stock rules are domain-owned.
- Inactive stock mutation is blocked by domain _require_active.
- Deactivation requires zero total quantity; reactivation requires inactive status.
- Domain events exist for item creation/lifecycle/stock operations.
- Historical stock truth helper explained_quantity_from_history is implemented and tested.

Restoration semantics:
- InventoryMapper.to_domain_inventory_item reconstructs state and clears restoration events with item.pull_events(), preventing false restoration event emissions.

## Persistence Review
Classification: COMPLIANT

Evidence highlights:
- Persistence models represent approved state only (item, positions, movements).
- Mapper preserves movement order and contextual fields across roundtrip.
- Historical stock truth survives roundtrip in tests/database/test_inventory_mapper.py and tests/database/test_sqlite_inventory_repository.py.
- Lifecycle status survives persistence roundtrip.
- No persistence model leakage into feature responses.

SQLite lifecycle ownership:
- Inventory mapper/repository tests use deterministic session/connection/engine teardown patterns.
- INV-006 E2E workflow includes explicit close/dispose and reopen proof.

## Repository Review
Classification: COMPLIANT

Evidence highlights:
- Contract and implementation alignment across add/get/update/exists/list/get_low_stock.
- Reference uniqueness enforced in add and update paths.
- Deterministic ordering provided in list via item_reference + created_at ordering.
- Low-stock semantics implemented as derived query over domain low_stock flag.
- Repository does not own commits; flush only. Commit ownership remains in application UnitOfWork.

## Application Review
Classification: COMPLIANT

Evidence highlights:
- Use-case coverage matches approved set: create/get/list/receive/issue/adjust/deactivate/reactivate/low-stock.
- Services are orchestrators over domain and repository contracts.
- Success paths commit via UoW; failed operations do not commit invalid states.
- Duplicate/not-found/insufficient-stock behavior is mapped through established exceptions.
- No concrete SQLite repository or SQLAlchemy model dependency in application service code.

## Feature Layer Review
Classification: COMPLIANT

Evidence highlights:
- Public execute(request) façade pattern is used consistently.
- Immutable request/response DTOs and mapping to/from application DTOs are implemented.
- Feature exceptions map established service exception semantics.
- Public exports in src/mfm/application/features/inventory/__init__.py are complete and consistent with approved surface.
- Feature layer does not mutate aggregates, calculate stock, access persistence, or own transactions.

## End-To-End Review
Classification: COMPLIANT

INV-006 proves real stack behavior through:
- Feature -> Application -> Domain -> Repository Contract -> SQLite Repository -> Mapper/Models -> SQLite

Workflows verified in tests/application/features/inventory/test_inventory_feature_e2e_workflows.py:
- create/retrieve/list
- historical stock truth
- insufficient stock failure truth
- low-stock semantics
- deactivate/reactivate
- persistence reopen with deterministic resource lifecycle

No fake repository substitutes are used in INV-006 E2E workflows.

## Historical Stock Truth Review
Classification: COMPLIANT

Canonical journey verified:
- initial 10.0
- receive +5.0
- issue -3.0
- adjust -1.0
- resulting 11.0

Evidence exists in domain, mapper/repository roundtrip tests, and INV-006 E2E reopen workflow.

## Active/Inactive Lifecycle Review
Classification: COMPLIANT

Verified:
- default active state
- deactivate/reactivate operations
- persistence of status through roundtrip
- public feature representation as status string

Observed behavior aligns with design-defined restriction that inactive items cannot mutate stock.

## Low-Stock Semantics Review
Classification: COMPLIANT

Verified:
- low-stock is derived from total_quantity < minimum_stock_level
- equal-to-threshold is not low stock
- repository/application/feature behaviors align
- deterministic results preserved through list ordering and filtering
- no procurement side effects

## Procurement Boundary Review
Classification: COMPLIANT

No Inventory production behavior found for:
- purchase-order creation
- supplier selection
- purchase approval
- automatic reorder
- procurement infrastructure dependency

Low-stock remains inventory state/query behavior only.

## Locked Capability Protection Review
Classification: COMPLIANT

No evidence of reverse dependency pressure or ownership drift into locked capabilities:
- Asset Core
- Fleet
- Technical Configuration
- Maintenance
- Certificates and Compliance
- Voyages

Inventory uses only approved opaque references where designed (notably optional vessel_id on StockLocation).

## Architecture Review
Classification: COMPLIANT

Required direction is preserved:
- Feature -> Application -> Domain/Repository Contract -> Infrastructure

Forbidden dependency checks remain green in permanent architecture tests:
- Domain has no application/feature/database/sqlalchemy dependency.
- Feature layer has no SQLAlchemy model dependency.

Inventory-focused feature guard test additionally checks for sqlalchemy/sqlite repository/session leakage markers.

## Test Evidence
Focused Inventory strict evidence (-W error):
- tests/domain/inventory/test_inventory_domain.py
- tests/database/test_inventory_mapper.py
- tests/database/test_sqlite_inventory_repository.py
- tests/application/inventory/test_inventory_use_cases.py
- tests/application/features/inventory/test_inventory_features.py
- tests/application/features/inventory/test_inventory_feature_e2e_workflows.py
- Result: 75 passed

Architecture strict evidence (-W error):
- tests/architecture/test_dependency_guard.py
- tests/architecture/test_feature_api_architecture.py
- Result: 10 passed

Full suite strict:
- python -m pytest -q -W error --maxfail=1 -ra
- Result: 982 passed

Full suite normal:
- python -m pytest -q
- Result: 982 passed

## Classified Findings
Material findings:
- None

Non-material findings:
- OUT OF SCOPE: Procurement capability actions are intentionally not present in CAP-12 and remain deferred to CAP-13.

## Unresolved Material Findings
- None

## Final Lock Recommendation
Recommendation: READY FOR LOCK

Rationale:
- Approved scope is implemented without material drift.
- Domain owns business rules and invariants.
- Persistence preserves historical truth and lifecycle state.
- Repository/application transaction ownership is aligned.
- Public feature boundary is clean.
- E2E workflows prove real-stack behavior including reopen durability.
- Historical stock truth and low-stock semantics are preserved across layers.
- Procurement boundary remains clean.
- Architecture tests and full strict baseline pass.
- No unresolved material GAP or DEFECT findings.

## Lock Status Governance
CAP-12 lock status is not changed in INV-007.
INV-008 is the lock-decision execution waypoint.