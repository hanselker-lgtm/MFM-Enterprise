# PROJ-000 — Projects Capability Design

Status: Draft
Capability: CAP-14 Projects (PROJ)

## Mission

Projects is responsible for planning, coordinating, tracking and governing
multi-domain work across MFM Enterprise.

Projects does not execute operational work.

Operational work remains owned by the originating capability.

---

# Responsibilities

Projects owns:

- Project
- Project Phase
- Milestone
- Project Activity
- Project Assignment
- Project Timeline
- Project Status

Projects coordinates:

- Maintenance work
- Procurement work
- Inventory reservations
- Fleet activities

Projects never owns those records.

---

# Non Responsibilities

Projects never owns:

- Inventory Items
- Purchase Orders
- Maintenance Work Orders
- Certificates
- Documents
- Accounting
- Contact data
- Organisations

Those remain inside their own bounded contexts.

---

# Aggregate Root

Project

Only one aggregate root exists in version 1.

---

# Public Use Cases

Create Project

Update Project

Archive Project

Plan Activity

Assign Member

Complete Milestone

Close Project

Search Projects

List Active Projects

List Archived Projects

---

# External References

Project may reference only identifiers.

Allowed:

AssetId

OrganisationId

PurchaseOrderId

InventoryItemId

MaintenanceWorkOrderId

DocumentId

CertificateId

No foreign aggregates are allowed.

---

# Lifecycle

Draft

↓

Planned

↓

Active

↓

On Hold

↓

Completed

↓

Archived

No transition skips validation.

---

# Success Criteria

Projects coordinates work.

Projects never owns work performed by another capability.