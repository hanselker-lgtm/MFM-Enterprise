# PROC-000 Generic Procurement Core Design

## Purpose
Procurement defines a generic purchasing capability for maritime associations, preserved vessels, workshops, and restoration programs.

The scope is domain design only. The capability is generic and does not hardcode suppliers, procurement systems, inventory internals, or accounting/bookkeeping behavior.

## Bounded Context
Procurement is a standalone bounded context.

Procurement owns:
- purchase order identity
- purchase order number/reference
- purchase order lifecycle
- purchase order line commitments
- approval state and approval history
- supplier reference snapshots
- receipt relationship history
- purchasing history

Procurement does not own:
- supplier master data or organization master data
- contact master data
- inventory quantities, movements, or low-stock semantics
- maintenance plans, work orders, or maintenance history
- technical configuration lifecycle or technical component ownership
- vessel lifecycle or fleet registration
- certificate lifecycle or compliance findings
- accounting postings, ledger state, or invoice matching

## Capability Boundary Map
- Purchase order lifecycle: OWNED BY THIS CAPABILITY
- Purchase order lines and committed quantities: OWNED BY THIS CAPABILITY
- Supplier master data: OUT OF SCOPE / OWNED ELSEWHERE
- Organization and Contact master data: OUT OF SCOPE / OWNED BY ORGANIZATION AND CONTACT
- Inventory quantities, stock truth, movements, and low-stock state: OUT OF SCOPE / OWNED BY INVENTORY
- Goods receipt inventory mutation: OUT OF SCOPE / OWNED BY INVENTORY
- Maintenance consumption: OUT OF SCOPE / OWNED BY MAINTENANCE
- Technical component ownership: OUT OF SCOPE / OWNED BY TECHNICAL CONFIGURATION
- Fleet and vessel ownership: OUT OF SCOPE / OWNED BY FLEET
- Certificate readiness or expiry handling: OUT OF SCOPE / OWNED BY CERTIFICATES AND COMPLIANCE
- Accounting and invoice matching: OUT OF SCOPE / OWNED BY FINANCE OR ACCOUNTING

## Aggregate Boundary
Primary aggregate root:
- PurchaseOrder

Boundary decision:
- One aggregate root is sufficient for CAP-13 first scope.
- PurchaseOrder owns header state, line state, approval state, receipt history, and cancellation truth.
- No secondary aggregate is required in first scope.

## Purchase Order Aggregate
PurchaseOrder aggregate state (first scope):

Required:
- purchase_order_id
- purchase_order_number
- supplier_reference
- status
- currency
- created_at

Optional:
- supplier_name_snapshot
- supplier_contact_snapshot
- notes
- requested_by_reference
- approved_by_reference
- approved_at
- ordered_at
- external_order_reference
- cancelled_at
- cancellation_reason

State ownership rules:
- purchase_order_number is unique within the Procurement capability scope.
- supplier_reference is an opaque external reference and does not own supplier master data.
- supplier snapshots preserve historical readability even if external supplier metadata changes later.
- order header values are immutable after the order leaves DRAFT except for append-only history fields permitted by lifecycle rules.

## Purchase Order Line
PurchaseOrderLine is an entity owned by PurchaseOrder.

Required line state:
- purchase_order_line_id
- description_snapshot
- quantity
- unit_price

Optional line state:
- inventory_item_reference
- expected_delivery_at
- line_note

Derived line state:
- line_total
- received_quantity
- outstanding_quantity

Line ownership rules:
- line quantity must be positive.
- unit_price must be non-negative.
- line_total is derived from quantity and unit_price.
- received_quantity is derived from receipt history.
- line edits are allowed only while the order is DRAFT.

## Supplier Boundary
Supplier is represented as an opaque external or organization reference.

Decision:
- Supplier is not a Procurement-owned master-data concept.
- Procurement stores supplier_reference and optional supplier snapshots only.
- Procurement does not own organization master data, contact master data, or supplier catalog data.

Boundary rules:
- supplier_reference is an identity/reference only field.
- any future mapping to Organization or Contact must be handled by an explicit boundary integration.
- Procurement must not import Organization or Contact infrastructure merely to keep supplier history.

## Money and Currency
Procurement order pricing uses the repository's established Money pattern.

Approved semantics:
- amount is Decimal-based and normalized to two decimal places
- currency is an ISO currency code represented by the established Currency model
- float is not allowed for authoritative money values
- line_total and order_total use the same currency as the purchase order

Order pricing rules:
- all lines in a purchase order must use the same currency
- unit_price is stored as Money
- line_total is derived from quantity and unit_price
- order_total is derived from the sum of line totals
- accounting/bookkeeping behavior remains out of scope

## Lifecycle
PurchaseOrder lifecycle states in first scope:
- DRAFT
- SUBMITTED
- APPROVED
- ORDERED
- PARTIALLY_RECEIVED
- RECEIVED
- CANCELLED

Allowed transitions:
- DRAFT -> SUBMITTED
- DRAFT -> CANCELLED
- DRAFT -> DRAFT (amendment only; no lifecycle change)
- SUBMITTED -> APPROVED
- SUBMITTED -> CANCELLED
- APPROVED -> ORDERED
- APPROVED -> CANCELLED
- ORDERED -> PARTIALLY_RECEIVED
- ORDERED -> RECEIVED
- ORDERED -> CANCELLED
- PARTIALLY_RECEIVED -> RECEIVED
- PARTIALLY_RECEIVED -> CANCELLED

Not allowed:
- transitions out of RECEIVED
- transitions out of CANCELLED
- direct DRAFT -> APPROVED
- direct SUBMITTED -> ORDERED
- direct APPROVED -> RECEIVED without an order record

Terminal states:
- RECEIVED
- CANCELLED

Ownership of transition rules:
- all lifecycle transition rules belong to the Procurement domain.
- approval and ordering transitions are not delegated to a generic workflow engine.

## Historical Procurement Truth
Procurement preserves historical truth for order creation, line commitments, approvals, ordering, receipts, and cancellation.

Rules:
- purchase_order_number and supplier snapshots are preserved for historical readability.
- line description snapshots are preserved even if upstream item names change later.
- receipt history is append-only.
- current status is a projection of lifecycle state plus receipt history, not a replacement for that history.

Receipt truth:
- each receipt record preserves receipt_reference, received_at, and received line quantities.
- a receipt record does not rewrite prior receipt records.
- receipt history is sufficient to reconstruct partial and final receipt state.

Restoration semantics:
- persistence restoration must reconstruct the PurchaseOrder aggregate without replaying business operations.
- restoration must not emit false creation, approval, ordering, or receipt events.

## Domain Events
Capability-owned domain events in first scope:
- PurchaseOrderCreated
- PurchaseOrderAmended
- PurchaseOrderSubmitted
- PurchaseOrderApproved
- PurchaseOrderOrdered
- PurchaseReceiptRecorded
- PurchaseOrderCancelled

Event guidance:
- events represent business facts, not technical persistence steps.
- events do not couple directly to locked capability implementations.
- any future cross-capability reactions belong to explicit integration governance.

## Repository Contract
Minimum aggregate repository contract:
- add(order)
- get_by_id(purchase_order_id)
- get_by_number(purchase_order_number)
- update(order)
- exists_by_number(purchase_order_number)
- list()
- list_by_state(status)
- list_by_supplier_reference(supplier_reference)

Repository rules:
- repository returns PurchaseOrder aggregates
- repository does not expose persistence models
- purchase_order_number uniqueness is enforced at the repository or application boundary
- repository does not own transaction commit/rollback if UnitOfWork conventions assign that responsibility to application services

## Application Use Cases
Approved first-scope application use cases:
- CreatePurchaseOrder
- AmendDraftPurchaseOrder
- SubmitPurchaseOrder
- ApprovePurchaseOrder
- PlacePurchaseOrder
- RecordPurchaseReceipt
- CancelPurchaseOrder
- GetPurchaseOrder
- ListPurchaseOrders
- ListPurchaseOrdersByState
- ListPurchaseOrdersBySupplier

Use case rules:
- CreatePurchaseOrder creates a DRAFT order.
- AmendDraftPurchaseOrder is allowed only while the order is DRAFT.
- SubmitPurchaseOrder moves the order from DRAFT to SUBMITTED.
- ApprovePurchaseOrder records approval metadata and moves the order to APPROVED.
- PlacePurchaseOrder moves the order to ORDERED and may capture an external order reference.
- RecordPurchaseReceipt appends receipt history and can move ORDERED orders into PARTIALLY_RECEIVED or RECEIVED.
- CancelPurchaseOrder is allowed only while the order is not RECEIVED.

## Public Feature API
Expected public feature entry points follow the established execute(request) standard:
- CreatePurchaseOrderFeature
- AmendDraftPurchaseOrderFeature
- SubmitPurchaseOrderFeature
- ApprovePurchaseOrderFeature
- PlacePurchaseOrderFeature
- RecordPurchaseReceiptFeature
- CancelPurchaseOrderFeature
- GetPurchaseOrderFeature
- ListPurchaseOrdersFeature
- ListPurchaseOrdersByStateFeature
- ListPurchaseOrdersBySupplierFeature

Public API rules:
- request DTOs are immutable
- response DTOs are immutable
- responses expose primitive or API-safe fields only
- no aggregate leakage
- no persistence leakage
- no mutable domain internals

Expected response shape guidance:
- order summary responses expose order identity, number, supplier reference, status, currency, order total, receipt status, and timestamps
- detailed responses may include primitive line DTOs and primitive receipt DTOs

## Inventory Boundary
Inventory is locked and protected.

Procurement boundary result:
- Procurement may hold opaque inventory_item_reference values on purchase order lines when approved by a future boundary contract.
- Procurement does not own inventory_item identity, stock quantity truth, stock movement truth, receive, issue, adjust, minimum-stock semantics, low-stock state, or active/inactive inventory lifecycle.
- Procurement must not directly update Inventory quantity.
- Procurement must not create Inventory movements.
- Procurement must not calculate Inventory historical truth.
- Procurement must not own low-stock semantics.
- Procurement must not automatically mutate Inventory.
- any future goods-receipt integration is a capability boundary concern and is not implemented in PROC-000.

## Dependency Direction
Allowed dependency direction:
- Feature
  - Application
  - Domain / Repository Contract
  - Infrastructure

Forbidden dependencies:
- Procurement domain must not depend on Inventory infrastructure internals.
- Procurement domain must not depend on locked capability implementation details.
- Procurement must not create reverse dependencies into Inventory, Fleet, Technical Configuration, Maintenance, Certificates and Compliance, or Voyages.
- Procurement must not import Organization or Contact infrastructure solely to model a supplier reference.

## Locked Capability Protection
Review of locked capabilities relevant to CAP-13:

- Asset Core: protected and unchanged.
- Fleet: protected and unchanged.
- Technical Configuration: protected and unchanged.
- Maintenance: protected and unchanged.
- Certificates and Compliance: protected and unchanged.
- Voyages: protected and unchanged.
- Inventory: protected and unchanged.

This design requires no modification to locked capability behavior.

If a future Procurement scenario requires changes to a locked capability, that scenario must be handled by a separate explicit governance decision before implementation.

## Non-Goals
CAP-13 first scope non-goals:
- supplier master-data management
- contact master-data management
- accounting postings
- invoice matching
- payment execution
- tax or VAT processing
- automatic reorder behavior
- inventory quantity mutation
- inventory low-stock calculation
- maintenance work-order ownership
- fleet ownership
- technical component ownership
- certificate lifecycle ownership
- project management ownership
- binary document storage
- GUI

## Design Recommendation
READY FOR DOMAIN IMPLEMENTATION

## Capability Status (CAP-13 Procurement)

Status: PLANNED

Status pr. 2026-07-15:
- PROC-000: design documented.
