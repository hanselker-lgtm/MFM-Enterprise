# PROJ-008 — Capability Lock

Status: LOCKED

Capability

CAP-14 Projects

Version

1.0

---

# Mission

Projects coordinates planning, execution tracking and governance of work.

Projects never performs operational work owned by another capability.

Mission is frozen.

---

# Aggregate

Frozen

Project

Child entities

ProjectMilestone

ProjectActivity

ProjectAssignment

ProjectReference

Aggregate boundary is frozen.

---

# Public Contract

Frozen

Commands

CreateProject

UpdateProject

ActivateProject

CompleteProject

ArchiveProject

CreateMilestone

CompleteMilestone

CreateActivity

CompleteActivity

AssignMember

RemoveAssignment

AddReference

Queries

GetProject

ListProjects

SearchProjects

ProjectDashboard

ProjectSummary

---

# External References

Allowed

AssetId

OrganisationId

ContactId

PurchaseOrderId

InventoryItemId

MaintenanceWorkOrderId

DocumentId

CertificateId

No additional references without architecture review.

---

# Architectural Constraints

Projects owns

Planning

Coordination

Timeline

Milestones

Assignments

Projects never owns

Inventory

Procurement

Maintenance

Fleet

Documents

Accounting

Certificates

Organisation

These boundaries are frozen.

---

# Integration Rules

Integration only through

Application Services

Feature Layer

Published Contracts

Identifiers

Direct repository access prohibited.

Direct ORM access prohibited.

Direct database access prohibited.

---

# Repository Rules

Repository returns

Complete Aggregate

or

Projection

Never partial aggregates.

Rule frozen.

---

# Persistence Rules

Persistence remains infrastructure.

Mapper contains no business logic.

Repository contains no business rules.

Domain remains authoritative.

Frozen.

---

# Review Result

Architecture

PASS

Domain

PASS

Persistence

PASS

Repository

PASS

Application

PASS

Feature

PASS

Integration

PASS

Documentation

PASS

---

# Capability Lock

Projects Capability is locked.

Future changes require:

Architecture Review

Capability Version Increment

Migration Assessment

Backward Compatibility Assessment

No breaking changes without explicit approval.

---

Approved By

Chief Architect

Date

YYYY-MM-DD