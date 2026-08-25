# PROJ-006 — End-to-End Workflows

Status: Draft

---

# Purpose

Describe complete business workflows crossing multiple capabilities while
preserving capability boundaries.

Projects orchestrates.

Other capabilities execute.

---

# Workflow 1

Create Restoration Project

Actor

Project Manager

Flow

Create Project

↓

Plan Milestones

↓

Plan Activities

↓

Assign Members

↓

Activate Project

Expected Result

Project becomes Active.

No operational work performed.

---

# Workflow 2

Procurement Request

Actor

Project Manager

Flow

Project Activity

↓

Request Procurement

↓

Procurement creates Purchase Order

↓

Purchase OrderId returned

↓

Project stores PurchaseOrderId as reference

Project never owns Purchase Order.

---

# Workflow 3

Inventory Reservation

Actor

Project Manager

Flow

Project Activity

↓

Request Inventory Reservation

↓

Inventory validates stock

↓

Reservation created

↓

ReservationId stored

Inventory remains owner.

---

# Workflow 4

Maintenance Work

Actor

Maintenance Planner

Flow

Project Activity

↓

Create Maintenance Work Order

↓

Maintenance executes work

↓

Completion event

↓

Project Activity marked Completed

Maintenance remains owner.

---

# Workflow 5

Project Completion

Preconditions

All mandatory milestones completed.

All mandatory activities completed.

Flow

Complete Project

↓

Archive Project

Expected Result

Project becomes read-only.

---

# Integration Contracts

Projects → Procurement

RequestPurchaseOrder()

Result

PurchaseOrderId

---

Projects → Inventory

RequestReservation()

Result

InventoryReservationId

---

Projects → Maintenance

RequestWorkOrder()

Result

MaintenanceWorkOrderId

---

Projects → Documents

AttachDocument()

Result

DocumentId

---

Projects → Certificates

ReferenceCertificate()

Result

CertificateId

---

# Failure Handling

External capability failure

↓

Project remains unchanged.

No partial completion.

---

# Consistency

Projects guarantees

Aggregate consistency.

Cross-capability consistency

handled through explicit application orchestration.

No distributed transactions.

---

# Integration Tests

Scenario 1

Create Project

Scenario 2

Project with Procurement

Scenario 3

Project with Inventory

Scenario 4

Project with Maintenance

Scenario 5

Project completion

Scenario 6

Archive Project

Scenario 7

Optimistic locking conflict

Scenario 8

Concurrent updates

---

# Acceptance Criteria

All workflows executable.

All integrations identifier-based.

No capability ownership violations.

No cross-capability persistence.

No distributed transactions.