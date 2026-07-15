# INV-000 Generic Inventory Core Design

## Purpose
Inventory defines a generic stock management capability for maritime associations,
preserved vessels, workshops, vessel stores, technical spare parts, and
consumable materials.

CAP-12 first scope is design only and is limited to:
- inventory item definition
- stock quantity ownership
- stock location ownership
- stock movement history
- controlled receipt, issue, and adjustment operations
- optional low-stock indication

Inventory must remain generic. It must not hardcode vessel names,
manufacturers, suppliers, or jurisdiction-specific concepts.

## Bounded Context
Inventory is a standalone bounded context.

Inventory owns:
- inventory item identity
- item reference and item definition
- unit of measure used for authoritative stock quantity
- current stock quantity by inventory-owned location
- historical stock movements
- stock receipt
- stock issue or consumption
- stock adjustment
- optional minimum stock level
- inventory item status
- low-stock state derived from owned stock and minimum level

Inventory does not own:
- Asset lifecycle or Asset metadata
- Vessel lifecycle or Fleet registration
- Technical Configuration lifecycle or specifications
- Maintenance plans, work orders, or completion state
- supplier management or purchase order lifecycle
- certificate lifecycle or compliance findings
- financial valuation or accounting postings
- warehouse optimization, barcode infrastructure, RFID, or scanner workflows

## Primary Domain Model Decision
Decision: Option B.

CAP-12 should be modeled as an InventoryItem aggregate that owns current stock
state together with append-only movement history.

Evaluation summary:
- Option A, mutable quantity without owned movement history, is too weak for
  auditability and correction control.
- Option C, InventoryItem plus separate StockMovement aggregate, adds
  cross-aggregate consistency complexity before CAP-12 has evidence for it.
- Option D, pure ledger-style derivation from movements only, is robust but
  introduces avoidable persistence and query complexity for first scope.

Chosen model:
- InventoryItem is the aggregate root.
- InventoryItem owns item definition, status, minimum stock level,
  location-scoped balances, and append-only StockMovement entities.
- Movement history is the authoritative explanation of stock change.
- Current quantity is an aggregate-owned derived cache updated only through
  domain operations that also append movement history.

This is the smallest robust model that preserves historical truth, supports
future Procurement and Maintenance references, and avoids a generic ledger
framework.

## Aggregate Boundary
Primary aggregate root:
- InventoryItem

InventoryItem owns:
- inventory_item_id
- item_reference
- name
- optional description
- unit_of_measure
- optional minimum_stock_level
- status
- zero or more StockPosition entities keyed by StockLocation
- append-only StockMovement entities

StockPosition entity responsibility:
- hold authoritative current quantity for one StockLocation within the parent
  InventoryItem aggregate
- ensure one current balance per location per item

StockMovement entity responsibility:
- record one business-significant stock change for the parent InventoryItem
- preserve movement type, quantity, location, timestamp, and optional
  external reference or note

Aggregate invariants:
- item_reference is unique at repository or application boundary
- all quantities use the InventoryItem unit_of_measure
- movement quantity must be positive
- StockPosition quantities must be non-negative
- total quantity equals the sum of owned StockPosition quantities
- stock can change only through receipt, issue, and adjustment operations

## Inventory Item
Primary item concept:
- InventoryItem represents a stock-managed definition, not a uniquely tracked
  installed asset.

Required state:
- inventory_item_id
- item_reference
- name
- unit_of_measure
- status

Optional state:
- description
- minimum_stock_level

State intentionally not included in first scope:
- supplier ownership
- purchase order state
- financial cost state
- lot or serial tracking state
- certificate state

Item-reference uniqueness responsibility:
- item_reference is required and must be unique across the Inventory
  capability scope.
- uniqueness enforcement belongs to the repository or application boundary.
- the domain validates presence and basic format rules only.

## Item Identity vs Asset Identity
Decision:
- InventoryItem identity is distinct from Asset identity.
- CAP-12 first scope does not allow an InventoryItem to own or embed an
  Asset identity reference.

Rationale:
- quantities such as paint, screws, filters, wire, or oil are stock-managed
  inventory concepts, not uniquely tracked Assets.
- allowing item-level Asset identity in first scope would blur the locked
  Asset Core boundary and encourage duplicate lifecycle ownership.

Boundary rule:
- a uniquely tracked engine, pump, or radio remains an Asset concern.
- Inventory may later integrate with Assets by explicit roadmap decision, but
  CAP-12 does not model stocked assets as Asset-linked inventory items.

## Quantity Model
Decision:
- authoritative stock quantities use Decimal semantics.
- binary floating-point is not allowed for authoritative stock state.

Rules:
- quantity precision is controlled by the item unit_of_measure.
- stored and compared quantities are normalized to the unit scale.
- stock quantity may be zero.
- movement quantity must be strictly greater than zero.
- current stock quantity may not be negative in first scope.
- minimum_stock_level, when present, must be non-negative and use the same
  unit semantics as stock quantity.

Equality semantics:
- quantities are equal after normalization to the unit scale.
- examples: 10.0 litre and 10.00 litre are equal when the unit scale permits
  two decimal places.

## Unit of Measure
Decision: Option B.

UnitOfMeasure should be an immutable value object owned by Inventory.

Approved model:
- unit_code
- decimal_places
- optional display_name

Rationale:
- a fixed enum is too rigid for future extension.
- a separate configurable identity or aggregate is too heavy for CAP-12.
- an immutable value object keeps semantics explicit without creating a Unit
  capability.

Boundary rules:
- unit_code is capability-controlled, not arbitrary free text.
- UnitOfMeasure is owned by Inventory and does not depend on Fleet,
  Maintenance, Technical Configuration, or Procurement.
- first-scope examples such as piece, litre, kilogram, and metre are valid
  examples, not a hardcoded exhaustive list.

## Stock Location
Decision: Option B.

StockLocation should be an immutable Inventory-owned value object.

Approved model:
- location_key
- location_name
- optional vessel_id reference

Rationale:
- free-text-only location is too weak for stable per-location balances.
- a separate StockLocation aggregate is not justified by CAP-12 first scope.
- an owned value object is sufficient to distinguish workshop, warehouse,
  vessel store, room, locker, or shelf without creating a Facilities or
  Warehouse Management capability.

First-scope rule:
- Inventory distinguishes stock by location.
- the same InventoryItem may hold separate StockPosition balances across
  multiple StockLocation values.

## Vessel Boundary
Decision:
- stock may optionally be associated with a vessel through StockLocation.
- vessel association is reference only via optional vessel_id.

Boundary rules:
- Inventory does not own Vessel aggregate state.
- Inventory does not store vessel registration, vessel lifecycle, or technical
  vessel identity.
- Inventory has no Fleet infrastructure dependency.

## Stock Movement Model
Movement types included in first scope:
- RECEIPT
- ISSUE
- ADJUSTMENT_INCREASE
- ADJUSTMENT_DECREASE

Movement rules:
- every stock-changing operation appends exactly one movement record for the
  affected location
- movement quantity is always positive
- movement timestamp is explicitly supplied by the caller
- movement may carry an optional external reference and optional note when
  justified by the use case

Transfer decision:
- location transfer is out of scope for CAP-12 first scope.
- no atomic transfer operation is defined in INV-000.

## Historical Stock Truth
Decision:
- movement history is authoritative historical truth.
- current quantity is a controlled aggregate-owned derived cache.

Consequences:
- Inventory must not support an unrestricted set_quantity operation.
- a stock correction must be expressed as an explicit adjustment operation.
- a stock explanation is reconstructed from append-only StockMovement history,
  while current quantity remains immediately available from owned StockPosition
  balances.

Example supported by the model:
- opening balance 10.0
- receipt +5.0
- issue -3.0
- adjustment -1.0
- current quantity 11.0

## Receipt Operation
Domain operation concept:
- receive_stock(location, quantity, occurred_at, external_reference optional,
  note optional)

Preconditions:
- InventoryItem status must be ACTIVE
- quantity must be positive after normalization
- location must be valid
- occurred_at must be explicitly supplied

Effects:
- create or update the location StockPosition
- append a RECEIPT movement
- increase current quantity for the location and the aggregate total
- preserve optional reference or note when supplied
- emit StockReceived

No hidden clock is allowed.

## Issue / Consumption Operation
Domain operation concept:
- issue_stock(location, quantity, occurred_at, external_reference optional,
  note optional)

Preconditions:
- InventoryItem status must be ACTIVE
- quantity must be positive after normalization
- location must be valid
- sufficient stock must exist at the chosen location
- occurred_at must be explicitly supplied

Effects:
- decrease current quantity for the chosen location and aggregate total
- append an ISSUE movement
- preserve optional destination or use reference when supplied
- emit StockIssued

Boundary note:
- an issue may optionally carry a WorkOrder or other external identity
  reference as metadata only.
- Inventory records stock leaving Inventory; it does not complete a
  Maintenance workflow.

## Adjustment Operation
Decision:
- stock adjustment is included in first scope.

Domain operation concept:
- adjust_stock_to_count(location, counted_quantity, reason, occurred_at,
  note optional)

Preconditions:
- InventoryItem status must be ACTIVE
- counted_quantity must be non-negative after normalization
- reason is required
- occurred_at must be explicitly supplied
- location must be valid
- counted_quantity must differ from the current location quantity

Effects:
- compute the delta between counted_quantity and current location quantity
- append ADJUSTMENT_INCREASE or ADJUSTMENT_DECREASE accordingly
- update the location StockPosition to the counted quantity
- update aggregate total consistently
- emit StockAdjusted

Adjustment policy:
- adjustment is the only approved correction mechanism in first scope.
- no silent overwrite of historical stock truth is allowed.

## Negative Stock Policy
Decision:
- negative stock is not allowed in CAP-12 first scope.

Rationale:
- first-scope Inventory should reflect physically available stock.
- delayed registration and counting discrepancies are handled through explicit
  receipt or adjustment operations, not by allowing negative balances.

Responsibility:
- the aggregate enforces non-negative current quantity at the affected
  location and in total.

## Minimum Stock Level
Decision:
- minimum_stock_level is included in first scope.
- it is optional.

Rules:
- when present, it must be non-negative
- it uses the same UnitOfMeasure semantics as current stock
- low-stock state is derived when total current quantity is below the minimum
  stock level

Boundary rule:
- Inventory exposes low-stock state only.
- Inventory does not create purchase orders or perform reordering.

## Procurement Boundary
Procurement is outside CAP-12.

Inventory must not own:
- suppliers
- purchase orders
- purchase approvals
- invoice matching
- purchasing contracts

Approved integration stance:
- a RECEIPT movement may optionally carry a future procurement reference as an
  immutable external reference only.
- Inventory has no Procurement repository or infrastructure dependency.

## Maintenance Boundary
Maintenance is locked and protected.

Inventory must not:
- create MaintenancePlan
- create MaintenanceRequirement
- create WorkOrder
- complete WorkOrder
- create MaintenanceRecord

Approved integration stance:
- an ISSUE movement may optionally carry a WorkOrder identity or external work
  reference as metadata only.
- Inventory does not load, validate, or mutate Maintenance aggregates.
- Maintenance consumption integration remains an application or integration
  concern outside the Inventory aggregate.

## Technical Configuration Boundary
Technical Configuration is locked and protected.

Decision:
- CAP-12 first scope does not add a technical_component_id reference to
  InventoryItem.

Rationale:
- Inventory remains generic at item-definition level.
- direct component linkage would add coupling without a first-scope invariant
  that requires it.

Boundary rule:
- Inventory does not own component lifecycle, machinery configuration,
  technical specifications, or equipment state.

## Certificates Boundary
Certificates and Compliance is locked and protected.

Decision:
- expiry-controlled stock is out of scope for CAP-12 first scope.

Consequences:
- Inventory does not add certificate dependencies.
- Inventory does not model certificate lifecycle, compliance findings, or
  expiry policy windows.
- lot-level expiry remains out of scope together with lot tracking.

## Lot / Batch / Serial Tracking Decision
Decision:
- advanced lot, batch, and serial tracking are out of scope for CAP-12 first
  scope.

Rationale:
- repository evidence does not justify warehouse-management complexity in the
  first Inventory capability slice.
- generic stock by item and location is sufficient for documented scenarios.

## Valuation / Finance Boundary
Decision:
- authoritative financial valuation is out of scope.
- InventoryItem does not own monetary value or accounting state in CAP-12.

Boundary rules:
- no ledger accounts
- no VAT
- no depreciation
- no financial posting
- no cost accounting

If future finance integration requires informational cost snapshots, that must
be approved explicitly outside INV-000.

## Item Status / Lifecycle
Decision:
- InventoryItem has a minimal lifecycle with ACTIVE and INACTIVE.

Allowed transitions:
- ACTIVE -> INACTIVE
- INACTIVE -> ACTIVE

Behavior rules:
- new items start as ACTIVE
- inactive items may be read and listed but may not receive, issue, or adjust
  stock
- deactivation requires total current quantity to be zero so stock is not
  stranded in an inactive item definition

## Time and Timezone Policy
Decision:
- stock movement timestamps use timezone-aware datetime.

Policy:
- every stock-changing operation receives occurred_at explicitly
- timestamps are compared in normalized UTC semantics for deterministic
  ordering and persistence-independent domain behavior
- no hidden datetime.now, datetime.today, date.today, or time.time usage is
  allowed in domain operations

## Domain Events
Meaningful Inventory domain events in first scope:
- InventoryItemCreated
- StockReceived
- StockIssued
- StockAdjusted
- InventoryItemDeactivated
- InventoryItemReactivated

Event guidance:
- events are emitted only for business-significant state changes
- no event inflation for trivial field edits or derived low-stock reads

## Repository Contract
Minimum aggregate repository contract:
- add(item)
- get_by_id(inventory_item_id)
- get_by_reference(item_reference)
- update(item)
- exists_by_reference(item_reference)
- list()
- get_low_stock()

Repository rules:
- repository returns InventoryItem aggregates
- repository does not expose persistence models
- item_reference uniqueness is enforced at the repository or application
  boundary
- no speculative reporting or location-analytics queries are included in first
  scope

## Application Use Cases
First-scope application use cases:
- CreateInventoryItem
- ReceiveStock
- IssueStock
- AdjustStock
- DeactivateInventoryItem
- ReactivateInventoryItem
- GetInventoryItem
- ListInventoryItems
- ListLowStockItems

Use case rules:
- all write use cases operate through explicit UnitOfWork boundaries later in
  implementation
- all requests and responses are immutable DTOs
- boundary validation and duplicate-reference enforcement stay outside the
  domain aggregate where appropriate

## Public Feature API
Expected public feature entry points follow the established execute(request)
standard:
- CreateInventoryItemFeature
- ReceiveStockFeature
- IssueStockFeature
- AdjustStockFeature
- DeactivateInventoryItemFeature
- ReactivateInventoryItemFeature
- GetInventoryItemFeature
- ListInventoryItemsFeature
- ListLowStockItemsFeature

Public API rules:
- request DTOs are immutable
- response DTOs are immutable
- responses expose primitive or API-safe fields only
- no aggregate leakage
- no value object leakage
- no persistence leakage

Expected response shape guidance:
- item summary responses expose identifiers, references, names, unit_code,
  status, total_quantity, optional minimum_stock_level, and low_stock flag
- detailed responses may include primitive location balance DTOs and primitive
  movement history DTOs

## Failure Model
Domain failure categories:
- invalid item reference format
- invalid quantity
- invalid unit of measure
- invalid stock location
- insufficient stock
- invalid adjustment request
- inactive item operation
- invalid lifecycle transition

Application or boundary failure categories:
- duplicate item reference
- item not found
- invalid external reference format where policy applies
- repository or infrastructure failure

Mapping rule:
- the domain is responsible for aggregate invariants and business rules
- application or feature layers map boundary and repository failures to the
  established public exception model

## Generic Maritime Validation Scenarios
Scenario 1 - Paint:
- Item: Marine paint
- Unit: litre
- Opening quantity: 10.0
- Receive: 5.0
- Issue: 3.0
- Approved model explanation: 10.0 + 5.0 - 3.0 = 12.0 through preserved
  movement history

Scenario 2 - Spare filter:
- Item: Oil filter
- Unit: piece
- Opening quantity: 5
- Issue: 2
- Approved model explanation: quantity remains coherent because piece uses the
  same authoritative unit semantics as stock balance and movements

Scenario 3 - Maintenance reference:
- an ISSUE movement may carry a WorkOrder identity reference as external
  metadata
- Inventory records the reference only
- Inventory does not load or mutate WorkOrder state

Scenario 4 - Vessel stock:
- stock may be recorded at a StockLocation that includes an optional vessel_id
  reference
- Inventory uses vessel identity reference only
- no Vessel aggregate ownership is introduced

Scenario 5 - Stock correction:
- physical count differs from recorded quantity
- adjust_stock_to_count computes a delta and records an explicit adjustment
  movement
- no silent set_quantity mutation is allowed

Scenario 6 - Low stock:
- current total quantity falls below optional minimum_stock_level
- Inventory can expose low_stock state
- Inventory does not create a purchase order

## Non-Goals
CAP-12 first scope non-goals:
- supplier management
- purchase orders
- procurement approvals
- invoice matching
- accounting
- VAT
- financial ledger posting
- depreciation
- Maintenance workflow ownership
- WorkOrder lifecycle ownership
- Vessel lifecycle ownership
- Technical Configuration ownership
- certificate lifecycle
- warehouse optimization
- barcode infrastructure
- RFID
- automated scanners
- advanced lot tracking
- serial-number fleet
- hazardous material regulation workflows
- binary document storage
- GUI

## Design Recommendation
READY FOR DOMAIN IMPLEMENTATION

## Capability Status (CAP-12 Inventory)

Status: LOCKED

Status pr. 2026-07-15:
- INV-000: design dokumenteret.
- INV-001: domain implementeret og testet.
- INV-002: SQLAlchemy persistence + mapper implementeret og testet.
- INV-003: repository contract + SQLite repository implementeret og testet.
- INV-004: application services implementeret og testet.
- INV-005: feature layer implementeret og testet.
- INV-006: end-to-end integration workflows implementeret og testet.
- INV-007: capability review dokumenteret i inventory_capability_review.md med konklusion READY FOR LOCK.
- INV-008: capability locked.

Lock-regler:
- Eksisterende public Inventory API betragtes som stabil.
- Kun fejlrettelser maa aendre laast adfaerd uden ny plan.
- Inventory capability behavior is frozen.
- Domain invariants are protected.
- Persistence and mapper semantics are protected.
- Repository contract semantics are protected.
- Application-service behavior is protected.
- Public Feature API behavior is protected.
- Historical stock truth is protected.
- Active/inactive lifecycle semantics are protected.
- Low-stock semantics are protected.
- Procurement boundary is protected.
- Dependency direction is protected.
- Asset Core, Fleet, Technical Configuration, Maintenance, Certificates and Compliance, and Voyages remain protected locked capabilities.
- Inventory must not introduce reverse dependencies into locked capabilities.
- Future changes to locked Inventory require explicit governance action under the repository lock rules.